# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 8 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Layout B, the 2025 shape of the paper. Exam-level mix (8 easy / 16 medium / 10 hard), with none of the shapes of
Levels 1-3 or Simulators 1-7: a product with a zero factor hidden in it, two-digit primes whose digits are prime,
2026² less 2025 × 2027, a number added to its two rotations, the cubes from 1 to 10 added, the last digit of 1 to 2027
added, powers stacked two ways, the HCF of a sum and a product, what every whole-number right triangle shares; four
speeds in four units, two shots heard closer together, two travellers and one bicycle, a wife who meets an early train;
water mixed at two temperatures, a sex ratio turned into a count, urea bought by the bag, a hospital better in each group
but not overall; a cess charged on the tax, a dividend on the face value, two years at different rates; n³ - n, k × k!
added; the vowels of MOTHER in the even places, four counters that share no row or column, four tasks among three
volunteers; cubes packed in a box, the points of a five-pointed star; two rooms painted with help, three slices on a
grill that holds two; birthdays on 29 February, a silver bar cut to pay a worker daily, travellers who share their
loaves; and two data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import math
import random
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

# ---------------------------------------------------------------- Number Theory (9)
def _nt1():
    rng = random.Random(8)
    vals = {ch: rng.randint(-50, 50) for ch in "abcdefghijklmnopqrstuvwxyz"}
    prod = 1
    for ch in "abcdefghijklmnopqrstuvwxyz":
        prod *= vals["x"] - vals[ch]
    assert prod == 0
    return "0"
T(QA, "Number Theory", "easy",
  "The letters a, b, c, ..., z stand for 26 numbers, one for each letter of the alphabet. What is the value of the product (x - a)(x - b)(x - c) ... (x - z), which has one factor for every letter?",
  "अक्षर a, b, c, ..., z, वर्णमाला के हर अक्षर के लिए एक, कुल 26 संख्याओं को दर्शाते हैं। गुणनफल (x - a)(x - b)(x - c) ... (x - z) का मान क्या है, जिसमें हर अक्षर के लिए एक गुणनखंड है?",
  ["0", "1", "x²⁶", "It cannot be found unless the 26 numbers are known"],
  ["0", "1", "x²⁶", "26 संख्याएँ जाने बिना इसे नहीं निकाला जा सकता"],
  0,
  "x is itself one of the letters, so one of the 26 factors is (x - x) = 0, and a product with a zero factor is 0, whatever the other numbers are. "
  "1 and x²⁶ treat the factors as if they cancelled out or as if every other letter stood for 0; and the 26 numbers are not needed, because the single zero factor settles the product.",
  "x स्वयं भी एक अक्षर है, इसलिए 26 गुणनखंडों में से एक (x - x) = 0 है, और जिस गुणनफल में एक गुणनखंड शून्य हो वह 0 होता है, बाक़ी संख्याएँ चाहे जो हों। "
  "1 और x²⁶ गुणनखंडों को ऐसे लेते हैं मानो वे कट जाते हों या हर दूसरा अक्षर 0 हो; और 26 संख्याओं की आवश्यकता नहीं, क्योंकि एक शून्य गुणनखंड ही गुणनफल तय कर देता है।",
  "qa-nt-a-product-with-a-zero-factor-hidden-in-it", pos=0, check=_nt1)

def _nt2():
    pr = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    found = [n for n in range(10, 100) if pr(n) and pr(n // 10) and pr(n % 10)]
    assert found == [23, 37, 53, 73]
    return str(len(found))
N(QA, "Number Theory", "easy",
  "How many two-digit prime numbers have both of their digits prime?",
  "दो अंकों की कितनी अभाज्य संख्याओं के दोनों अंक अभाज्य हैं?",
  ["4", "5", "6", "7"], 0,
  "The prime digits are 2, 3, 5 and 7. A two-digit prime cannot end in 2 or 5, so it ends in 3 or 7: 23, 27, 33, 37, 53, 57, 73 and 77. Of these 27 = 3 × 9, 33 = 3 × 11, 57 = 3 × 19 and 77 = 7 × 11 are not prime, leaving 23, 37, 53 and 73 -- four. "
  "5 lets 57 slip through, since it looks prime but is 3 × 19; 6 and 7 also keep numbers such as 27 or 33, whose digits are prime though the numbers are not.",
  "अभाज्य अंक 2, 3, 5 और 7 हैं। दो अंकों की अभाज्य संख्या 2 या 5 पर समाप्त नहीं हो सकती, इसलिए वह 3 या 7 पर समाप्त होगी: 23, 27, 33, 37, 53, 57, 73 और 77। इनमें 27 = 3 × 9, 33 = 3 × 11, 57 = 3 × 19 और 77 = 7 × 11 अभाज्य नहीं हैं; बचती हैं 23, 37, 53 और 73 -- चार। "
  "5, 57 को निकल जाने देता है, जो अभाज्य दिखती है पर 3 × 19 है; 6 और 7, 27 या 33 जैसी संख्याएँ भी रखते हैं, जिनके अंक तो अभाज्य हैं पर संख्याएँ नहीं।",
  "qa-nt-two-digit-primes-whose-digits-are-prime", _nt2)

def _nt3():
    v = 2026 ** 2 - 2025 * 2027
    assert v == 1
    return str(v)
N(QA, "Number Theory", "easy",
  "What is the value of 2026² - 2025 × 2027?",
  "2026² - 2025 × 2027 का मान क्या है?",
  ["-1", "0", "1", "2"], 2,
  "2025 × 2027 = (2026 - 1)(2026 + 1) = 2026² - 1, so 2026² - 2025 × 2027 = 2026² - (2026² - 1) = 1, with no long multiplication. "
  "-1 subtracts the wrong way round; 0 assumes the two products are equal; 2 counts the 1 by which each factor differs from 2026 twice.",
  "2025 × 2027 = (2026 - 1)(2026 + 1) = 2026² - 1, इसलिए 2026² - 2025 × 2027 = 2026² - (2026² - 1) = 1, बिना लंबे गुणा के। "
  "-1 उलटा घटाता है; 0 मान लेता है कि दोनों गुणनफल बराबर हैं; 2, हर गुणनखंड के 2026 से 1 के अंतर को दो बार गिनता है।",
  "qa-nt-2026-squared-less-2025-times-2027", _nt3)

def _nt4():
    sums = [100 * a + 10 * b + c_ + 100 * b + 10 * c_ + a + 100 * c_ + 10 * a + b
            for a, b, c_ in product(range(1, 10), repeat=3)]
    always = [d for d in (11, 27, 37, 99) if all(s % d == 0 for s in sums)]
    assert always == [37] and 125 + 251 + 512 == 888 == 37 * 24
    return "37"
N(QA, "Number Theory", "medium",
  "A three-digit number has the digits a, b and c, none of them zero. It is added to the two numbers formed by moving its digits round, to give abc + bca + cab (for example, 125 + 251 + 512). Which one of the following numbers always divides this sum?",
  "तीन अंकों की एक संख्या के अंक a, b और c हैं, जिनमें कोई शून्य नहीं। उसमें उसके अंकों को घुमाकर बनी दो संख्याएँ जोड़ी जाती हैं, जिससे abc + bca + cab मिलता है (उदाहरण के लिए, 125 + 251 + 512)। निम्नलिखित में से कौन-सी संख्या इस योग को सदा विभाजित करती है?",
  ["11", "27", "37", "99"], 2,
  "Each of a, b and c stands once in the hundreds place, once in the tens and once in the units, so the sum is 111a + 111b + 111c = 111(a + b + c) = 3 × 37 × (a + b + c). So 37 always divides it: 125 + 251 + 512 = 888 = 37 × 24. "
  "27 divides it only when a + b + c is a multiple of 9, and 11 and 99 only when 11 divides a + b + c; the example 888 is a multiple of none of them.",
  "a, b और c में से हर अंक एक बार सैकड़े, एक बार दहाई और एक बार इकाई के स्थान पर आता है, इसलिए योग 111a + 111b + 111c = 111(a + b + c) = 3 × 37 × (a + b + c) है। अतः 37 इसे सदा विभाजित करता है: 125 + 251 + 512 = 888 = 37 × 24। "
  "27 इसे तभी विभाजित करता है जब a + b + c, 9 का गुणज हो, और 11 तथा 99 तभी जब 11, a + b + c को विभाजित करे; उदाहरण का 888 इनमें से किसी का गुणज नहीं।",
  "qa-nt-a-number-added-to-its-two-rotations", _nt4)

def _nt5():
    s = sum(k ** 3 for k in range(1, 11))
    assert s == 55 ** 2 and sum(k ** 3 for k in range(1, 10)) == 2025 and sum(k ** 3 for k in range(1, 12)) == 4356
    assert sum(k * k for k in range(1, 11)) == 385
    return f"{s:,}"
N(QA, "Number Theory", "medium",
  "What is the value of 1³ + 2³ + 3³ + ... + 10³?",
  "1³ + 2³ + 3³ + ... + 10³ का मान क्या है?",
  ["385", "2,025", "3,025", "4,356"], 2,
  "The sum of the first n cubes is the square of the sum of the first n numbers: (1 + 2 + ... + 10)² = 55² = 3,025. (Check with a short case: 1³ + 2³ = 9 = 3².) "
  "385 is the sum of the squares 1² to 10², not the cubes; 2,025 = 45² stops at 9³; 4,356 = 66² runs on to 11³.",
  "पहले n घनों का योग पहली n संख्याओं के योग का वर्ग होता है: (1 + 2 + ... + 10)² = 55² = 3,025। (छोटे उदाहरण से जाँचें: 1³ + 2³ = 9 = 3²।) "
  "385, घनों का नहीं बल्कि 1² से 10² तक के वर्गों का योग है; 2,025 = 45², 9³ पर रुक जाता है; 4,356 = 66², 11³ तक चला जाता है।",
  "qa-nt-the-cubes-from-1-to-10-added", _nt5)

def _nt6():
    s = 2027 * 2028 // 2
    assert s == sum(range(1, 2028)) and (2027 * 2028) % 10 == 6
    return str(s % 10)
N(QA, "Number Theory", "medium",
  "What is the last digit of 1 + 2 + 3 + ... + 2027?",
  "1 + 2 + 3 + ... + 2027 का अंतिम अंक क्या है?",
  ["3", "6", "7", "8"], 3,
  "The sum is 2027 × 2028 ÷ 2 = 2027 × 1014. Its last digit is the last digit of 7 × 4 = 28: 8. "
  "6 is the last digit of 2027 × 2028 before it is halved; 3 halves that 6, but halving a number does not halve its last digit (56 ÷ 2 = 28, not 23); 7 is just the last digit of 2027.",
  "योग 2027 × 2028 ÷ 2 = 2027 × 1014 है। इसका अंतिम अंक 7 × 4 = 28 का अंतिम अंक है: 8। "
  "6, आधा करने से पहले 2027 × 2028 का अंतिम अंक है; 3 उस 6 को आधा करता है, पर किसी संख्या को आधा करने से उसका अंतिम अंक आधा नहीं होता (56 ÷ 2 = 28, 23 नहीं); 7 केवल 2027 का अंतिम अंक है।",
  "qa-nt-the-last-digit-of-1-to-2027-added", _nt6)

def _nt7():
    vals = {"2 raised to the power 3²": 2 ** (3 ** 2), "(2³)²": (2 ** 3) ** 2,
            "3 raised to the power 2²": 3 ** (2 ** 2), "(3²)²": (3 ** 2) ** 2}
    assert sorted(vals.values()) == [64, 81, 81, 512]
    return max(vals, key=vals.get)
T(QA, "Number Theory", "medium",
  "Which one of the following is the largest?",
  "निम्नलिखित में से कौन-सा सबसे बड़ा है?",
  ["2 raised to the power 3²", "(2³)²", "3 raised to the power 2²", "(3²)²"],
  ["2 की घात 3²", "(2³)²", "3 की घात 2²", "(3²)²"],
  0,
  "A power whose index is itself a power is worked from the top down: 2 raised to the power 3² is 2⁹ = 512. With brackets the inner power comes first, and the indices multiply: (2³)² = 2⁶ = 64 and (3²)² = 3⁴ = 81; and 3 raised to the power 2² is 3⁴ = 81. "
  "The trap is to read 2 raised to the power 3² as if it were (2³)², which gives only 64.",
  "जिस घात का घातांक स्वयं एक घात हो, उसे ऊपर से नीचे की ओर हल करते हैं: 2 की घात 3², 2⁹ = 512 है। कोष्ठक होने पर भीतर की घात पहले आती है और घातांक गुणा होते हैं: (2³)² = 2⁶ = 64 और (3²)² = 3⁴ = 81; और 3 की घात 2², 3⁴ = 81 है। "
  "जाल यह है कि 2 की घात 3² को (2³)² की तरह पढ़ा जाए, जिससे केवल 64 मिलता है।",
  "qa-nt-powers-stacked-two-ways", pos=3, check=_nt7)

def _nt8():
    for a in range(1, 80):
        for b in range(1, 80):
            if math.gcd(a, b) == 1:
                assert math.gcd(a + b, a * b) == 1
    assert math.gcd(13, 36) == 1 and math.gcd(8, 15) == 1
    return "1"
T(QA, "Number Theory", "hard",
  "a and b are positive integers whose HCF is 1. What is the HCF of a + b and ab?",
  "a और b ऐसे धनात्मक पूर्णांक हैं जिनका म.स. (HCF) 1 है। a + b और ab का म.स. क्या है?",
  ["1", "a + b", "ab", "It depends on the values of a and b"],
  ["1", "a + b", "ab", "यह a और b के मानों पर निर्भर है"],
  0,
  "Any prime that divides ab divides a or b -- say a. If it also divided a + b, it would divide (a + b) - a = b as well, and so would divide both a and b, whose HCF is 1. So no prime divides both a + b and ab, and their HCF is 1, whatever a and b are: 4 and 9 give 13 and 36; 3 and 5 give 8 and 15. "
  "a + b would need a + b to divide ab, which fails for 4 and 9; ab would need ab to divide a + b; and the values make no difference, as the proof shows.",
  "ab को विभाजित करने वाली कोई भी अभाज्य संख्या a या b को विभाजित करती है -- मान लें a को। यदि वह a + b को भी विभाजित करती, तो (a + b) - a = b को भी करती, और इस तरह a और b दोनों को, जिनका म.स. 1 है। इसलिए कोई अभाज्य a + b और ab दोनों को विभाजित नहीं करती, और उनका म.स. 1 है, a और b चाहे जो हों: 4 और 9 से 13 और 36 मिलते हैं; 3 और 5 से 8 और 15। "
  "a + b के लिए a + b को ab को विभाजित करना होता, जो 4 और 9 पर विफल है; ab के लिए ab को a + b को विभाजित करना होता; और जैसा प्रमाण दिखाता है, मानों से कोई अंतर नहीं पड़ता।",
  "qa-nt-the-hcf-of-a-sum-and-a-product", pos=3, check=_nt8)

def _nt9():
    one = two = True
    n = 0
    for a in range(1, 400):
        for b in range(a, 400):
            h = math.isqrt(a * a + b * b)
            if h * h == a * a + b * b:
                n += 1
                one &= any(x % 5 == 0 for x in (a, b, h))
                two &= (a * b) % 12 == 0                 # area ab/2 is a whole multiple of 6
    assert n > 100
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Number Theory", "hard",
   "Consider every right-angled triangle whose three sides are whole numbers, such as 3, 4, 5 or 5, 12, 13. Which of the following statements is/are true of every such triangle?",
   "हर ऐसे समकोण त्रिभुज पर विचार कीजिए जिसकी तीनों भुजाएँ पूर्ण संख्याएँ हैं, जैसे 3, 4, 5 या 5, 12, 13। निम्नलिखित में से कौन-सा/से कथन हर ऐसे त्रिभुज के लिए सत्य है/हैं?",
   ["At least one of its three sides is a multiple of 5.",
    "Its area is a whole number that is a multiple of 6."],
   ["उसकी तीनों भुजाओं में से कम से कम एक 5 की गुणज है।",
    "उसका क्षेत्रफल एक पूर्ण संख्या है जो 6 की गुणज है।"],
   2,
   "Both are true. 1: a square leaves remainder 0, 1 or 4 when divided by 5. If neither shorter side were a multiple of 5, their squares would add to something leaving 2, 3 or 0; 2 and 3 are impossible for the square of the longest side, and 0 makes the longest side a multiple of 5. So some side always is (3, 4, 5; 20, 21, 29; 8, 15, 17 through 15). "
   "2: one of the two shorter sides is always a multiple of 3 and one a multiple of 4, so their product is a multiple of 12 and the area, half that product, a multiple of 6: 3, 4, 5 gives 6; 5, 12, 13 gives 30; 8, 15, 17 gives 60.",
   "दोनों सत्य हैं। 1: किसी वर्ग को 5 से भाग देने पर शेष 0, 1 या 4 बचता है। यदि दोनों छोटी भुजाओं में से कोई 5 की गुणज न हो, तो उनके वर्गों के योग का शेष 2, 3 या 0 होगा; सबसे लंबी भुजा के वर्ग के लिए 2 और 3 असंभव हैं, और 0 का अर्थ है कि सबसे लंबी भुजा 5 की गुणज है। अतः कोई न कोई भुजा सदा 5 की गुणज होती है (3, 4, 5; 20, 21, 29; 8, 15, 17 में 15)। "
   "2: दोनों छोटी भुजाओं में से एक सदा 3 की गुणज और एक 4 की गुणज होती है, इसलिए उनका गुणनफल 12 का गुणज है और क्षेत्रफल, उस गुणनफल का आधा, 6 का गुणज: 3, 4, 5 से 6; 5, 12, 13 से 30; 8, 15, 17 से 60।",
   "qa-nt-what-every-whole-number-right-triangle-shares", check=_nt9)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    kmh = {"21 m/s": F(21) * F(18, 5), "77 km/h": F(77), "1.25 km a minute": F(5, 4) * 60, "1,300 m a minute": F(1300, 1000) * 60}
    assert sorted(kmh.values()) == [75, F(378, 5), 77, 78]
    return max(kmh, key=kmh.get)
T(QA, "Speed-Distance-Time", "easy",
  "Which one of the following speeds is the fastest?",
  "निम्नलिखित में से कौन-सी चाल सबसे तेज़ है?",
  ["1,300 m a minute", "21 m/s", "77 km/h", "1.25 km a minute"],
  ["1,300 मी प्रति मिनट", "21 मी/से", "77 किमी/घंटा", "1.25 किमी प्रति मिनट"],
  0,
  "Put all four in km/h. 21 m/s × 3.6 = 75.6 km/h; 77 km/h as it stands; 1.25 km a minute × 60 = 75 km/h; 1,300 m a minute = 1.3 km × 60 = 78 km/h. The fastest is 1,300 m a minute. "
  "77 km/h looks largest only because it is already in the larger unit; 21 m/s and 1.25 km a minute come to 75.6 and 75 km/h.",
  "चारों को किमी/घंटा में बदलें। 21 मी/से × 3.6 = 75.6 किमी/घंटा; 77 किमी/घंटा जैसा है; 1.25 किमी प्रति मिनट × 60 = 75 किमी/घंटा; 1,300 मी प्रति मिनट = 1.3 किमी × 60 = 78 किमी/घंटा। सबसे तेज़ 1,300 मी प्रति मिनट है। "
  "77 किमी/घंटा केवल इसलिए सबसे बड़ा दिखता है कि वह पहले से बड़ी इकाई में है; 21 मी/से और 1.25 किमी प्रति मिनट 75.6 और 75 किमी/घंटा बनते हैं।",
  "qa-sdt-four-speeds-in-four-units", pos=2, check=_sdt1)

def _sdt2():
    saved = 10 * 60 - (9 * 60 + 45)               # seconds by which the second sound is early
    gap = 330 * saved                             # metres the train ran between the shots
    v = F(gap, 600) * F(18, 5)
    assert v == F(297, 10) and round(float(F(gap, 585) * F(18, 5)), 1) == 30.5
    return f"{float(v):g} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "Two shots are fired from a train exactly 10 minutes apart, as it runs straight towards a man standing beside the track. The man hears the two shots 9 minutes 45 seconds apart. If sound travels at 330 m/s, what is the speed of the train?",
  "एक रेलगाड़ी से ठीक 10 मिनट के अंतर पर दो गोलियाँ चलाई जाती हैं, जब वह पटरी के किनारे खड़े एक व्यक्ति की ओर सीधी चल रही है। व्यक्ति दोनों गोलियों की आवाज़ 9 मिनट 45 सेकंड के अंतर पर सुनता है। यदि ध्वनि 330 मी/से से चलती है, तो रेलगाड़ी की चाल क्या है?",
  ["8.25 km/h", "29.7 km/h", "30.5 km/h", "59.4 km/h"], 1,
  "The second shot is fired nearer the man by the distance the train runs in 10 minutes, so its sound reaches him sooner by the time sound takes to cross that distance -- here 15 seconds. In 15 s sound covers 330 × 15 = 4,950 m, and the train covered those 4,950 m in 600 s: 8.25 m/s = 8.25 × 3.6 = 29.7 km/h. "
  "8.25 km/h forgets to turn m/s into km/h; 30.5 km/h divides by the 585 seconds the man heard instead of the 600 the train ran; 59.4 km/h doubles the answer, as if the sound went out and back like an echo.",
  "दूसरी गोली व्यक्ति के उतना निकट चलाई जाती है जितना रेलगाड़ी 10 मिनट में चलती है, इसलिए उसकी आवाज़ उतना पहले पहुँचती है जितना ध्वनि को वह दूरी पार करने में लगता है -- यहाँ 15 सेकंड। 15 से में ध्वनि 330 × 15 = 4,950 मी चलती है, और रेलगाड़ी ने ये 4,950 मी 600 से में तय किए: 8.25 मी/से = 8.25 × 3.6 = 29.7 किमी/घंटा। "
  "8.25 किमी/घंटा मी/से को किमी/घंटा में बदलना भूल जाता है; 30.5 किमी/घंटा रेलगाड़ी के 600 सेकंड के बजाय व्यक्ति द्वारा सुने 585 सेकंड से भाग देता है; 59.4 किमी/घंटा उत्तर को दोगुना करता है, मानो ध्वनि प्रतिध्वनि की तरह जाकर लौटी हो।",
  "qa-sdt-two-shots-heard-closer-together", _sdt2,
  opts_hi=["8.25 किमी/घंटा", "29.7 किमी/घंटा", "30.5 किमी/घंटा", "59.4 किमी/घंटा"])

def _sdt3():
    best = None
    for tenth in range(0, 241):                   # Asha rides x km, x in steps of 0.1 km
        x = F(tenth, 10)
        ta = x / 12 + (24 - x) / 4
        tb = x / 6 + (24 - x) / 18
        if ta == tb:
            assert x / 12 <= x / 6                # the bicycle is waiting when Bina reaches it
            best = (x, ta)
    x, t = best
    assert x == F(84, 5) and t == F(16, 5)
    half_a, half_b = F(12, 12) + F(12, 4), F(12, 6) + F(12, 18)
    assert (half_a, half_b) == (4, F(8, 3))
    h, m = divmod(t * 60, 60)
    return f"{int(h)} h {int(m)} min"
N(QA, "Speed-Distance-Time", "hard",
  "Asha and Bina must both reach a town 24 km away, and they have one bicycle between them. Asha walks at 4 km/h and cycles at 12 km/h; Bina walks at 6 km/h and cycles at 18 km/h. They set out together: Asha rides some distance, leaves the bicycle by the road and walks on, while Bina walks until she reaches the bicycle and then rides the rest of the way. If they arrive at the same moment, how long does the journey take?",
  "आशा और बीना दोनों को 24 किमी दूर एक कस्बे तक पहुँचना है, और उनके पास एक ही साइकिल है। आशा 4 किमी/घंटा से चलती और 12 किमी/घंटा से साइकिल चलाती है; बीना 6 किमी/घंटा से चलती और 18 किमी/घंटा से साइकिल चलाती है। वे साथ निकलती हैं: आशा कुछ दूरी साइकिल से जाती है, साइकिल सड़क किनारे छोड़कर पैदल आगे बढ़ती है, जबकि बीना साइकिल तक पैदल पहुँचकर बाक़ी रास्ता साइकिल से तय करती है। यदि दोनों एक ही क्षण पहुँचती हैं, तो यात्रा में कितना समय लगता है?",
  ["2 h 40 min", "3 h 12 min", "3 h 20 min", "4 h"], 1,
  "Let Asha ride x km. Asha takes x/12 + (24 - x)/4 = 6 - x/6 hours; Bina takes x/6 + (24 - x)/18 = 4/3 + x/9 hours. Equal times: 6 - 4/3 = x/6 + x/9, so 14/3 = 5x/18 and x = 16.8 km. The journey takes 6 - 16.8/6 = 3.2 h = 3 h 12 min. (Bina reaches the bicycle after 16.8 ÷ 6 = 2.8 h; Asha left it there after 1.4 h, so it is waiting.) "
  "Leaving the bicycle half-way would not bring them in together: Asha would take 4 h and Bina 2 h 40 min, and 3 h 20 min is just the average of those two.",
  "मान लें आशा x किमी साइकिल से जाती है। आशा को x/12 + (24 - x)/4 = 6 - x/6 घंटे लगते हैं; बीना को x/6 + (24 - x)/18 = 4/3 + x/9 घंटे। समय बराबर: 6 - 4/3 = x/6 + x/9, अतः 14/3 = 5x/18 और x = 16.8 किमी। यात्रा में 6 - 16.8/6 = 3.2 घंटे = 3 घंटे 12 मिनट लगते हैं। (बीना 16.8 ÷ 6 = 2.8 घंटे बाद साइकिल तक पहुँचती है; आशा उसे 1.4 घंटे बाद वहाँ छोड़ चुकी थी, इसलिए साइकिल वहीं है।) "
  "साइकिल आधे रास्ते पर छोड़ने से वे साथ नहीं पहुँचतीं: आशा को 4 घंटे और बीना को 2 घंटे 40 मिनट लगते, और 3 घंटे 20 मिनट उन दोनों का औसत भर है।",
  "qa-sdt-two-travellers-and-one-bicycle", _sdt3,
  opts_hi=["2 घंटे 40 मिनट", "3 घंटे 12 मिनट", "3 घंटे 20 मिनट", "4 घंटे"])

def _sdt4():
    for D, v in ((30, 60), (12, 40), (45, 90)):          # distance home-station (km), car speed (km/h)
        drive = F(D, v)
        leave = 1 - drive                                # hours after 5 pm when she leaves home
        usual_home = 1 + drive
        # meeting t hours after 5 pm; she then drives back the distance she has covered
        t = (usual_home - F(1, 3) + leave) / 2
        covered = v * (t - leave)
        walked = D - covered
        assert 0 < walked < D and t + (t - leave) == usual_home - F(1, 3)
        assert t * 60 == 50
    return "50 min"
N(QA, "Speed-Distance-Time", "hard",
  "A man's train usually reaches his home station at 6 pm, and his wife, driving from home, arrives at the station at exactly 6 pm to drive him back. One day he takes an earlier train that arrives at 5 pm and starts walking home along the road. His wife leaves home at the usual time, drives at her usual speed, meets him on the way, turns round and drives him home. They reach home 20 minutes earlier than usual. For how long did he walk?",
  "एक व्यक्ति की रेलगाड़ी सामान्यतः शाम 6 बजे उसके घर के स्टेशन पहुँचती है, और उसकी पत्नी घर से गाड़ी चलाकर ठीक 6 बजे स्टेशन पहुँचती है ताकि उसे वापस ले आए। एक दिन वह पहले की रेलगाड़ी पकड़ता है जो 5 बजे पहुँचती है और सड़क के रास्ते पैदल घर की ओर चल पड़ता है। उसकी पत्नी सामान्य समय पर घर से निकलती है, सामान्य चाल से गाड़ी चलाती है, रास्ते में उससे मिलती है, मुड़ती है और उसे घर ले आती है। वे सामान्य से 20 मिनट पहले घर पहुँचते हैं। वह कितनी देर पैदल चला?",
  ["40 min", "45 min", "50 min", "60 min"], 2,
  "The 20 minutes saved are the drive she did not make -- from the meeting point to the station and back -- so that stretch takes 10 minutes each way. She therefore met him 10 minutes' drive short of the station, at 5:50 pm, the time she would have passed that point on a normal day. He had been walking since 5 pm: 50 minutes. "
  "60 min assumes he walked the whole hour he was early; 40 min takes the full 20 minutes off that hour, forgetting that the saving is split between the two directions; 45 min has no basis.",
  "बचे हुए 20 मिनट वह ड्राइव हैं जो उसे नहीं करनी पड़ी -- मिलन-स्थल से स्टेशन तक और वापस -- इसलिए वह हिस्सा हर ओर 10 मिनट का है। अतः वह उससे स्टेशन से 10 मिनट की ड्राइव पहले, शाम 5:50 पर मिली, उसी समय जब सामान्य दिन वह उस स्थान से गुज़रती। वह 5 बजे से चल रहा था: 50 मिनट। "
  "60 मिनट मान लेता है कि वह पूरा घंटा, जितना वह जल्दी आया, चलता रहा; 40 मिनट उस घंटे से पूरे 20 मिनट घटाता है, यह भूलकर कि बचत दोनों दिशाओं में बँटी है; 45 मिनट का कोई आधार नहीं।",
  "qa-sdt-a-wife-who-meets-an-early-train", _sdt4,
  opts_hi=["40 मिनट", "45 मिनट", "50 मिनट", "60 मिनट"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (4)
def _rm1():
    t = F(2 * 80 + 3 * 20, 5)
    assert t == 44 and F(80 + 20, 2) == 50 and F(3 * 80 + 2 * 20, 5) == 56
    return f"{t} °C"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "2 litres of water at 80 °C are mixed with 3 litres of water at 20 °C. If no heat is lost, what is the temperature of the mixture?",
  "80 °C के 2 लीटर पानी को 20 °C के 3 लीटर पानी में मिलाया जाता है। यदि कोई ऊष्मा नष्ट न हो, तो मिश्रण का तापमान क्या है?",
  ["44 °C", "50 °C", "53 °C", "56 °C"], 0,
  "The mixture's temperature is the average weighted by the amounts: (2 × 80 + 3 × 20) ÷ 5 = 220 ÷ 5 = 44 °C -- nearer 20 °C, because there is more of the cold water. "
  "50 °C is the plain average, which would need equal amounts; 56 °C puts the weights the wrong way round, (3 × 80 + 2 × 20) ÷ 5; 53 °C has no basis.",
  "मिश्रण का तापमान मात्राओं से भारित औसत है: (2 × 80 + 3 × 20) ÷ 5 = 220 ÷ 5 = 44 °C -- 20 °C के अधिक निकट, क्योंकि ठंडा पानी अधिक है। "
  "50 °C साधारण औसत है, जिसके लिए मात्राएँ बराबर होनी चाहिए; 56 °C भार उलट देता है, (3 × 80 + 2 × 20) ÷ 5; 53 °C का कोई आधार नहीं।",
  "qa-rm-water-mixed-at-two-temperatures", _rm1)

def _rm2():
    females = F(38800 * 940, 1940)
    assert females == 18800 and 38800 - females == 20000 and F(38800 * 47, 100) == 18236
    return f"{int(females):,}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A town's sex ratio is 940 -- that is, there are 940 females for every 1,000 males. If the town has 38,800 people, how many of them are female?",
  "एक कस्बे का लिंगानुपात 940 है -- अर्थात हर 1,000 पुरुषों पर 940 महिलाएँ हैं। यदि कस्बे में 38,800 लोग हैं, तो उनमें कितनी महिलाएँ हैं?",
  ["18,236", "18,800", "19,400", "20,000"], 1,
  "Out of every 1,000 + 940 = 1,940 people, 940 are female. 38,800 ÷ 1,940 = 20, so there are 20 × 940 = 18,800 females (and 20 × 1,000 = 20,000 males). "
  "18,236 takes 940 out of 2,000, that is 47% of the people, as if the ratio were of females to twice the males; 19,400 is half the town, ignoring the ratio; 20,000 is the number of males.",
  "हर 1,000 + 940 = 1,940 लोगों में 940 महिलाएँ हैं। 38,800 ÷ 1,940 = 20, इसलिए 20 × 940 = 18,800 महिलाएँ हैं (और 20 × 1,000 = 20,000 पुरुष)। "
  "18,236, 2,000 में से 940, यानी लोगों का 47%, लेता है, मानो अनुपात महिलाओं का पुरुषों की दोगुनी संख्या से हो; 19,400 अनुपात की अनदेखी कर कस्बे का आधा है; 20,000 पुरुषों की संख्या है।",
  "qa-rm-a-sex-ratio-turned-into-a-count", _rm2)

def _rm3():
    n = F(120) * F(3, 4)
    urea = n / F(46, 100)
    bags = math.ceil(urea / 45)
    assert n == 90 and 4 < urea / 45 < 5 and math.ceil(F(90, 45)) == 2 and math.ceil(F(120, 45)) == 3
    return str(bags)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A farmer has to apply 120 kg of nitrogen per hectare to a field of 0.75 hectare, using urea, which is 46% nitrogen by weight. Urea is sold only in whole bags of 45 kg. How many bags must the farmer buy?",
  "एक किसान को 0.75 हेक्टेयर के खेत में प्रति हेक्टेयर 120 किग्रा नाइट्रोजन यूरिया के रूप में डालनी है, जिसमें भार के अनुसार 46% नाइट्रोजन होती है। यूरिया केवल 45 किग्रा की पूरी बोरियों में बिकता है। किसान को कितनी बोरियाँ ख़रीदनी होंगी?",
  ["2", "3", "4", "5"], 3,
  "The field needs 120 × 0.75 = 90 kg of nitrogen. Since urea is 46% nitrogen, that takes 90 ÷ 0.46 ≈ 195.7 kg of urea, or 195.7 ÷ 45 ≈ 4.35 bags -- so 5 whole bags. "
  "4 rounds down and leaves the field short of nitrogen; 2 forgets that urea is only 46% nitrogen (90 ÷ 45); 3 forgets that and the field's size as well (120 ÷ 45 ≈ 2.7, rounded up).",
  "खेत को 120 × 0.75 = 90 किग्रा नाइट्रोजन चाहिए। यूरिया में 46% नाइट्रोजन है, इसलिए 90 ÷ 0.46 ≈ 195.7 किग्रा यूरिया लगेगा, यानी 195.7 ÷ 45 ≈ 4.35 बोरियाँ -- अतः 5 पूरी बोरियाँ। "
  "4 नीचे की ओर पूर्णांक बनाता है और खेत में नाइट्रोजन कम रह जाती है; 2 भूल जाता है कि यूरिया में केवल 46% नाइट्रोजन है (90 ÷ 45); 3 यह और खेत का आकार, दोनों भूल जाता है (120 ÷ 45 ≈ 2.7, ऊपर की ओर पूर्णांक)।",
  "qa-rm-urea-bought-by-the-bag", _rm3)

def _rm4():
    P = {"mild": (95, 100), "severe": (300, 500)}
    Q = {"mild": (450, 500), "severe": (50, 100)}
    rate = lambda d, k: F(*d[k])
    one = all(rate(P, k) > rate(Q, k) for k in P)
    overall = lambda d: F(sum(v[0] for v in d.values()), sum(v[1] for v in d.values()))
    two = overall(P) > overall(Q)
    assert one and not two and overall(P) == F(395, 600)
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Ratio, Mixtures & Alligation", "hard",
  "Two hospitals treated patients with the same illness last year. Hospital P treated 100 mild cases, of whom 95 recovered, and 500 severe cases, of whom 300 recovered. Hospital Q treated 500 mild cases, of whom 450 recovered, and 100 severe cases, of whom 50 recovered. Which of the following statements is/are correct?",
  "पिछले वर्ष दो अस्पतालों ने एक ही बीमारी के रोगियों का उपचार किया। अस्पताल P ने 100 हल्के मामलों का उपचार किया, जिनमें 95 ठीक हुए, और 500 गंभीर मामलों का, जिनमें 300 ठीक हुए। अस्पताल Q ने 500 हल्के मामलों का उपचार किया, जिनमें 450 ठीक हुए, और 100 गंभीर मामलों का, जिनमें 50 ठीक हुए। निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
  ["P's recovery rate was higher than Q's both for mild cases and for severe cases.",
   "P's recovery rate over all its patients was higher than Q's."],
  ["हल्के और गंभीर, दोनों प्रकार के मामलों में P की स्वस्थ होने की दर Q से अधिक थी।",
   "अपने सभी रोगियों को मिलाकर P की स्वस्थ होने की दर Q से अधिक थी।"],
  0,
  "1 is correct: for mild cases P had 95% against Q's 90%, and for severe cases 60% against 50%. "
  "2 is wrong: over all patients P had 395 of 600 recover (about 66%) and Q 500 of 600 (about 83%). The reversal comes from the mix of cases: most of P's patients were severe, most of Q's mild. So a hospital can do better in every group and still look worse overall -- which is why such rates should be compared group by group.",
  "1 सही है: हल्के मामलों में P की दर 95% थी और Q की 90%, गंभीर मामलों में 60% और 50%। "
  "2 ग़लत है: सभी रोगियों में P के 600 में से 395 ठीक हुए (लगभग 66%) और Q के 600 में से 500 (लगभग 83%)। यह उलटफेर मामलों के मिश्रण से आता है: P के अधिकांश रोगी गंभीर थे, Q के अधिकांश हल्के। इसलिए कोई अस्पताल हर समूह में बेहतर होकर भी कुल मिलाकर ख़राब दिख सकता है -- इसीलिए ऐसी दरों की तुलना समूह-दर-समूह करनी चाहिए।",
  "qa-rm-a-hospital-better-in-each-group-but-not-overall", check=_rm4)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    share = F(30) + F(30) * F(4, 100)
    assert share == F(312, 10)
    return f"{float(share):g}%"
N(QA, "Percentage & Profit-Loss", "easy",
  "Income tax is charged at 30% on a part of a person's income, and a cess of 4% is then charged on the tax. What percentage of that part of the income goes in tax and cess together?",
  "किसी व्यक्ति की आय के एक भाग पर 30% आयकर लगता है, और फिर कर पर 4% उपकर (सेस) लगता है। आय के उस भाग का कितना प्रतिशत कर और उपकर मिलाकर जाता है?",
  ["30.12%", "31.2%", "32%", "34%"], 1,
  "The cess is 4% of the tax, not of the income: 4% of 30 = 1.2, so together they take 30 + 1.2 = 31.2% of that part of the income. "
  "34% adds the 4 to the rate as if the cess were charged on the income; 30.12% takes 4% of 3 instead of 4% of 30; 32% has no basis.",
  "उपकर कर का 4% है, आय का नहीं: 30 का 4% = 1.2, इसलिए दोनों मिलकर आय के उस भाग का 30 + 1.2 = 31.2% लेते हैं। "
  "34% दर में 4 जोड़ देता है, मानो उपकर आय पर लगा हो; 30.12%, 30 के 4% के बजाय 3 का 4% लेता है; 32% का कोई आधार नहीं।",
  "qa-pp-a-cess-charged-on-the-tax", _pp1)

def _pp2():
    div = F(30, 100) * 10
    y = div / 40 * 100
    assert div == 3 and y == F(15, 2)
    return f"{float(y):g}%"
N(QA, "Percentage & Profit-Loss", "medium",
  "A company whose shares have a face value of ₹10 each declares a dividend of 30%. An investor had bought its shares at the market price of ₹40 each. What return does the dividend give the investor on the money invested?",
  "एक कंपनी, जिसके शेयरों का अंकित मूल्य ₹10 प्रति शेयर है, 30% लाभांश घोषित करती है। एक निवेशक ने उसके शेयर ₹40 प्रति शेयर के बाज़ार मूल्य पर ख़रीदे थे। लाभांश से निवेशक को लगाई गई राशि पर कितना प्रतिफल मिलता है?",
  ["3%", "7.5%", "12%", "30%"], 1,
  "A dividend percentage is reckoned on the face value: 30% of ₹10 = ₹3 a share. The investor paid ₹40 a share, so the return is 3 ÷ 40 = 7.5%. "
  "30% reads the dividend as a return on the price paid; 3% mistakes the ₹3 for a percentage; 12% multiplies 30% by 40/100 instead of scaling it by 10/40.",
  "लाभांश का प्रतिशत अंकित मूल्य पर गिना जाता है: ₹10 का 30% = ₹3 प्रति शेयर। निवेशक ने ₹40 प्रति शेयर दिए, इसलिए प्रतिफल 3 ÷ 40 = 7.5% है। "
  "30% लाभांश को चुकाए गए मूल्य पर प्रतिफल मान लेता है; 3%, ₹3 को प्रतिशत समझ लेता है; 12%, 30% को 10/40 से बदलने के बजाय 40/100 से गुणा करता है।",
  "qa-pp-a-dividend-on-the-face-value", _pp2)

def _pp3():
    g = F(105, 100) * F(125, 100)
    assert g == F(13125, 10000) and F(115, 100) ** 2 > g and 0.145 < math.sqrt(1.3125) - 1 < 0.147
    return "A little less than 15%"
T(QA, "Percentage & Profit-Loss", "medium",
  "A deposit earns compound interest at 5% in its first year and 25% in its second. What single yearly rate, compounded over the same two years, would give the same final amount?",
  "एक जमा राशि पर पहले वर्ष 5% और दूसरे वर्ष 25% चक्रवृद्धि ब्याज मिलता है। उन्हीं दो वर्षों में चक्रवृद्धि होने वाली कौन-सी एक वार्षिक दर उतनी ही अंतिम राशि देगी?",
  ["A little less than 15%", "Exactly 15%", "A little more than 15%", "It depends on the size of the deposit"],
  ["15% से कुछ कम", "ठीक 15%", "15% से कुछ अधिक", "यह जमा राशि के आकार पर निर्भर है"],
  0,
  "Over the two years the deposit grows by 1.05 × 1.25 = 1.3125 times. At a steady 15% it would grow by 1.15² = 1.3225 times -- more. So the equal rate is a little less than 15% (about 14.6%). "
  "Exactly 15% averages the two rates, which works for simple interest but not when interest is compounded; the size of the deposit does not matter, since every rupee grows by the same factor.",
  "दो वर्षों में जमा राशि 1.05 × 1.25 = 1.3125 गुना होती है। स्थिर 15% पर वह 1.15² = 1.3225 गुना होती -- अधिक। इसलिए बराबर दर 15% से कुछ कम (लगभग 14.6%) है। "
  "ठीक 15% दोनों दरों का औसत लेता है, जो साधारण ब्याज में चलता है पर चक्रवृद्धि में नहीं; जमा राशि के आकार से अंतर नहीं पड़ता, क्योंकि हर रुपया उसी गुणक से बढ़ता है।",
  "qa-pp-two-years-at-different-rates", pos=3, check=_pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    s = [n ** 3 - n for n in range(1, 7)]
    assert s[:5] == [0, 6, 24, 60, 120] and s[5] == 5 * 6 * 7
    return str(s[5])
N(QA, "Sequences & Series", "medium",
  "What is the next number in the series 0, 6, 24, 60, 120, ...?",
  "श्रेणी 0, 6, 24, 60, 120, ... की अगली संख्या क्या है?",
  ["180", "200", "204", "210"], 3,
  "The terms are n³ - n for n = 1, 2, 3, ...: 1 - 1, 8 - 2, 27 - 3, 64 - 4, 125 - 5. The next is 216 - 6 = 210, which is also 5 × 6 × 7, the product of three numbers in a row like 4 × 5 × 6 = 120 before it. "
  "The gaps run 6, 18, 36, 60, growing by 12, 18, 24, so the next grows by 30 to 90: 120 + 90 = 210 again. 204 lets the gaps grow by 24 once more; 180 adds 60 again, as if the gaps had stopped growing; 200 has no basis.",
  "पद n = 1, 2, 3, ... के लिए n³ - n हैं: 1 - 1, 8 - 2, 27 - 3, 64 - 4, 125 - 5। अगला 216 - 6 = 210 है, जो 5 × 6 × 7 भी है, लगातार तीन संख्याओं का गुणनफल, जैसे उससे पहले 4 × 5 × 6 = 120। "
  "अंतर 6, 18, 36, 60 हैं, जो 12, 18, 24 से बढ़ते हैं, इसलिए अगला 30 बढ़कर 90 होता है: 120 + 90 = 210 फिर से। 204 अंतर को फिर 24 से बढ़ाता है; 180 फिर से 60 जोड़ता है, मानो अंतर बढ़ना रुक गया हो; 200 का कोई आधार नहीं।",
  "qa-ss-n-cubed-less-n", _ss1)

def _ss2():
    s = sum(k * math.factorial(k) for k in range(1, 10))
    assert s == math.factorial(10) - 1 and 9 * math.factorial(9) == 3265920
    return indian(s)
N(QA, "Sequences & Series", "hard",
  "What is the value of 1 × 1! + 2 × 2! + 3 × 3! + ... + 9 × 9!? (Here n! = 1 × 2 × 3 × ... × n, and 10! = 36,28,800.)",
  "1 × 1! + 2 × 2! + 3 × 3! + ... + 9 × 9! का मान क्या है? (यहाँ n! = 1 × 2 × 3 × ... × n, और 10! = 36,28,800।)",
  ["3,62,879", "32,65,920", "36,28,799", "36,28,800"], 2,
  "Each term can be rewritten: k × k! = (k + 1) × k! - k! = (k + 1)! - k!. So the sum is (2! - 1!) + (3! - 2!) + ... + (10! - 9!), and everything cancels except 10! - 1! = 36,28,800 - 1 = 36,28,799. (Check with a short case: 1 × 1! + 2 × 2! = 5 = 3! - 1.) "
  "36,28,800 forgets to subtract 1!; 32,65,920 is the last term, 9 × 9!, alone; 3,62,879 = 9! - 1 stops the pattern a step too early.",
  "हर पद को ऐसे लिखा जा सकता है: k × k! = (k + 1) × k! - k! = (k + 1)! - k!। इसलिए योग (2! - 1!) + (3! - 2!) + ... + (10! - 9!) है, और 10! - 1! = 36,28,800 - 1 = 36,28,799 के सिवा सब कट जाता है। (छोटे उदाहरण से जाँचें: 1 × 1! + 2 × 2! = 5 = 3! - 1।) "
  "36,28,800, 1! घटाना भूल जाता है; 32,65,920 केवल अंतिम पद, 9 × 9!, है; 3,62,879 = 9! - 1 पैटर्न को एक क़दम पहले रोक देता है।",
  "qa-ss-k-times-k-factorial-added", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    n = sum(1 for p in permutations("MOTHER") if all(p[i] not in "OE" for i in (0, 2, 4)))
    assert n == 3 * 2 * math.factorial(4)
    return str(n)
N(QA, "Permutation & Combination", "medium",
  "In how many ways can the letters of the word MOTHER be arranged so that the vowels always stand in even places (the 2nd, 4th or 6th)?",
  "शब्द MOTHER के अक्षरों को कितने प्रकार से व्यवस्थित किया जा सकता है कि स्वर सदा सम स्थानों (दूसरे, चौथे या छठे) पर रहें?",
  ["36", "48", "72", "144"], 3,
  "The vowels O and E go into two of the three even places: 3 × 2 = 6 ways. The four consonants M, T, H and R then fill the four places left, in 4! = 24 ways. In all, 6 × 24 = 144. "
  "48 = 2 × 24 lets the vowels use only one fixed pair of even places; 72 halves the answer, as if O and E could not change places; 36 has no basis.",
  "स्वर O और E तीन सम स्थानों में से दो में जाते हैं: 3 × 2 = 6 प्रकार। फिर चार व्यंजन M, T, H और R बचे चार स्थान 4! = 24 प्रकार से भरते हैं। कुल 6 × 24 = 144। "
  "48 = 2 × 24 स्वरों को सम स्थानों की केवल एक निश्चित जोड़ी देता है; 72 उत्तर को आधा करता है, मानो O और E आपस में स्थान न बदल सकें; 36 का कोई आधार नहीं।",
  "qa-pc-the-vowels-of-mother-in-the-even-places", _pc1)

def _pc2():
    cells = list(product(range(4), repeat=2))
    n = sum(1 for s in combinations(cells, 4) if len({r for r, _ in s}) == 4 and len({k for _, k in s}) == 4)
    assert n == 24 and math.comb(16, 4) == 1820
    return str(n)
N(QA, "Permutation & Combination", "easy",
  "Four identical counters are to be placed on the 16 squares of a 4 × 4 board so that no two of them are in the same row or in the same column. In how many ways can this be done?",
  "चार एक जैसी गोटियों को 4 × 4 बोर्ड के 16 खानों पर इस प्रकार रखना है कि कोई दो एक ही पंक्ति या एक ही स्तंभ में न हों। यह कितने प्रकार से किया जा सकता है?",
  ["24", "256", "576", "1,820"], 0,
  "Each row must hold exactly one counter. The counter in the first row can go in any of 4 columns, the one in the second row in any of the 3 columns left, then 2, then 1: 4 × 3 × 2 × 1 = 24. "
  "1,820 is the number of ways to choose any 4 of the 16 squares, ignoring the rule; 256 = 4⁴ lets two counters share a column; 576 = 24 × 24 treats the counters as if they were different from one another.",
  "हर पंक्ति में ठीक एक गोटी होनी चाहिए। पहली पंक्ति की गोटी 4 में से किसी भी स्तंभ में जा सकती है, दूसरी पंक्ति की बचे 3 में से किसी में, फिर 2, फिर 1: 4 × 3 × 2 × 1 = 24। "
  "1,820, नियम की अनदेखी कर 16 में से कोई भी 4 खाने चुनने के प्रकार हैं; 256 = 4⁴ दो गोटियों को एक ही स्तंभ में आने देता है; 576 = 24 × 24 गोटियों को एक-दूसरे से भिन्न मान लेता है।",
  "qa-pc-four-counters-that-share-no-row-or-column", _pc2)

def _pc3():
    n = sum(1 for f in product(range(3), repeat=4) if len(set(f)) == 3)
    assert n == 3 ** 4 - 3 * 2 ** 4 + 3 == math.comb(4, 2) * math.factorial(3) and 3 ** 4 - 3 * 2 ** 4 == 33
    return str(n)
N(QA, "Permutation & Combination", "hard",
  "Four different tasks are shared out among three volunteers so that each volunteer gets at least one task. In how many ways can this be done?",
  "चार अलग-अलग काम तीन स्वयंसेवकों में इस प्रकार बाँटे जाते हैं कि हर स्वयंसेवक को कम से कम एक काम मिले। यह कितने प्रकार से किया जा सकता है?",
  ["24", "33", "36", "81"], 2,
  "With four tasks and three people, one person gets two tasks and the others one each. Choose the pair of tasks that go together: C(4, 2) = 6 ways; then hand the three bundles -- the pair and the two single tasks -- to the three volunteers: 3! = 6 ways. In all, 6 × 6 = 36. (Or: 3⁴ = 81 ways in all, less 3 × 2⁴ = 48 that leave a chosen volunteer out, plus the 3 that were taken away twice: 81 - 48 + 3 = 36.) "
  "81 lets a volunteer get nothing; 33 = 81 - 48 forgets to add back the 3 cases in which two volunteers are left out; 24 = 4 × 3 × 2 gives out only three of the tasks.",
  "चार काम और तीन लोग हों तो एक को दो काम मिलते हैं और बाक़ी दोनों को एक-एक। साथ जाने वाले कामों की जोड़ी चुनें: C(4, 2) = 6 प्रकार; फिर तीन गठरियाँ -- जोड़ी और दो अकेले काम -- तीन स्वयंसेवकों को दें: 3! = 6 प्रकार। कुल 6 × 6 = 36। (या: कुल 3⁴ = 81 प्रकार, उनमें से 3 × 2⁴ = 48 घटाएँ जिनमें कोई चुना हुआ स्वयंसेवक छूटता है, और वे 3 जोड़ें जो दो बार घट गए: 81 - 48 + 3 = 36।) "
  "81 किसी स्वयंसेवक को ख़ाली हाथ रहने देता है; 33 = 81 - 48 उन 3 मामलों को वापस जोड़ना भूल जाता है जिनमें दो स्वयंसेवक छूटते हैं; 24 = 4 × 3 × 2 केवल तीन काम बाँटता है।",
  "qa-pc-four-tasks-among-three-volunteers", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    n = (7 // 2) * (9 // 2) * (11 // 2)
    assert n == 60 and (7 * 9 * 11) // 8 == 86 and 3 * 4 * 6 == 72 and 4 * 5 * 6 == 120
    return str(n)
N(QA, "Geometry & Mensuration", "medium",
  "How many cubes of side 2 cm can be packed into a closed box whose inside measures 7 cm × 9 cm × 11 cm, if the cubes are placed with their faces parallel to the sides of the box?",
  "2 सेमी भुजा वाले कितने घन एक बंद डिब्बे में भरे जा सकते हैं जिसकी भीतरी माप 7 सेमी × 9 सेमी × 11 सेमी है, यदि घनों को उनके फलक डिब्बे की भुजाओं के समानांतर रखकर रखा जाए?",
  ["60", "72", "86", "120"], 0,
  "Along the 7 cm side only 3 cubes fit (6 cm, with 1 cm to spare); along 9 cm, 4; along 11 cm, 5. So 3 × 4 × 5 = 60 cubes fit, and the leftover strips are too thin for any more. "
  "86 divides the volumes, 693 ÷ 8, as if the cubes could be cut to fill the gaps; 72 rounds 11 ÷ 2 up to 6; 120 rounds every side up.",
  "7 सेमी की भुजा के साथ केवल 3 घन आते हैं (6 सेमी, 1 सेमी बचता है); 9 सेमी के साथ 4; 11 सेमी के साथ 5। इसलिए 3 × 4 × 5 = 60 घन आते हैं, और बची पट्टियाँ और घनों के लिए बहुत पतली हैं। "
  "86 आयतनों का भाग, 693 ÷ 8, लेता है, मानो घनों को काटकर ख़ाली जगह भरी जा सके; 72, 11 ÷ 2 को बढ़ाकर 6 करता है; 120 हर भुजा को ऊपर की ओर पूर्णांक बनाता है।",
  "qa-gm-cubes-packed-in-a-box", _gm1)

def _gm2():
    def ang(p, q, r):                      # angle at q between q->p and q->r, in degrees
        a = (p[0] - q[0], p[1] - q[1]); b = (r[0] - q[0], r[1] - q[1])
        return math.degrees(math.acos((a[0] * b[0] + a[1] * b[1]) / math.hypot(*a) / math.hypot(*b)))
    rng = random.Random(8)
    tested = 0
    for _ in range(400):                   # random convex pentagons: corners at increasing angles round a centre
        ts = sorted(rng.uniform(0, 2 * math.pi) for _ in range(5))
        if min((ts[(i + 1) % 5] - ts[i]) % (2 * math.pi) for i in range(5)) < 0.3:
            continue
        pts = [(math.cos(t) * rng.uniform(0.8, 1.2), math.sin(t) * rng.uniform(0.8, 1.2)) for t in ts]
        if any(((pts[(i + 1) % 5][0] - pts[i][0]) * (pts[(i + 2) % 5][1] - pts[(i + 1) % 5][1])
                - (pts[(i + 1) % 5][1] - pts[i][1]) * (pts[(i + 2) % 5][0] - pts[(i + 1) % 5][0])) <= 0 for i in range(5)):
            continue                       # keep only convex ones
        tips = sum(ang(pts[(i + 2) % 5], pts[i], pts[(i + 3) % 5]) for i in range(5))
        assert abs(tips - 180) < 1e-6
        tested += 1
    assert tested >= 30
    return "180°"
N(QA, "Geometry & Mensuration", "medium",
  "A five-pointed star is drawn by joining each corner of a pentagon to the two corners that are not next to it (the pentagon need not be regular). What is the sum of the five angles at the points of the star?",
  "एक पंचभुज के हर कोने को उन दो कोनों से मिलाकर, जो उसके बग़ल में नहीं हैं, एक पाँच नोकों वाला तारा बनाया जाता है (पंचभुज का सम होना आवश्यक नहीं)। तारे की पाँचों नोकों पर बने कोणों का योग क्या है?",
  ["180°", "360°", "540°", "720°"], 0,
  "In a regular star each point is 36°, and 5 × 36° = 180°. The total stays 180° for any such star: in the triangle formed at one point, the two far angles are exterior angles of two small triangles, and each equals the sum of two of the other points' angles -- so the five point angles together make up the three angles of one triangle. "
  "540° is the angle sum of the pentagon itself; 360° is the sum of a polygon's exterior angles; 720° has no basis.",
  "सम तारे में हर नोक 36° की होती है, और 5 × 36° = 180°। ऐसे किसी भी तारे में योग 180° ही रहता है: किसी एक नोक पर बने त्रिभुज में, दूर के दोनों कोण दो छोटे त्रिभुजों के बाह्य कोण हैं, और हर एक बाक़ी में से दो नोकों के कोणों के योग के बराबर है -- इस प्रकार पाँचों नोकों के कोण मिलकर एक त्रिभुज के तीन कोण बनाते हैं। "
  "540° स्वयं पंचभुज के कोणों का योग है; 360° किसी बहुभुज के बाह्य कोणों का योग है; 720° का कोई आधार नहीं।",
  "qa-gm-the-points-of-a-five-pointed-star", _gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    r, s = F(1, 6), F(1, 3)                 # rooms per hour
    t1 = 1 / s                              # Sunil finishes his room
    left = 1 - r * t1                       # what remains of Ravi's room
    t = t1 + left / (r + s)
    assert t == 2 / (r + s) == 4
    return f"{t} h"
N(QA, "Time & Work", "medium",
  "Ravi can paint a room in 6 hours and Sunil can paint a room of the same size in 3 hours. Two such rooms are to be painted. Each starts on a room of their own, and whoever finishes first then helps the other. How long does it take to paint both rooms?",
  "रवि एक कमरा 6 घंटे में रंग सकता है और सुनील उसी आकार का कमरा 3 घंटे में। ऐसे दो कमरे रंगने हैं। दोनों अपना-अपना कमरा शुरू करते हैं, और जो पहले ख़त्म करता है वह फिर दूसरे की सहायता करता है। दोनों कमरे रंगने में कितना समय लगता है?",
  ["4 h", "4 h 30 min", "5 h", "6 h"], 0,
  "Sunil finishes his room in 3 hours, by which time Ravi has painted half of his. The other half takes them together (1/6 + 1/3 = 1/2 a room an hour) 1 more hour: 4 hours in all. Equivalently, both work the whole time on 2 rooms at 1/2 a room an hour. "
  "6 h is how long Ravi would take with no help; 4 h 30 min averages that with Sunil's 3 hours; 5 h has no basis.",
  "सुनील अपना कमरा 3 घंटे में ख़त्म करता है, तब तक रवि अपना आधा रंग चुका होता है। बचा आधा दोनों मिलकर (1/6 + 1/3 = 1/2 कमरा प्रति घंटा) 1 घंटे और में रंगते हैं: कुल 4 घंटे। दूसरे शब्दों में, दोनों पूरा समय 1/2 कमरा प्रति घंटा की दर से 2 कमरों पर काम करते हैं। "
  "6 घंटे वह समय है जो बिना सहायता के रवि को लगता; 4 घंटे 30 मिनट उसका सुनील के 3 घंटों से औसत है; 5 घंटे का कोई आधार नहीं।",
  "qa-tw-two-rooms-painted-with-help", _tw1,
  opts_hi=["4 घंटे", "4 घंटे 30 मिनट", "5 घंटे", "6 घंटे"])

def _tw2():
    # state: sides toasted per slice (0, 1 or 2); each 2-minute round toasts one side of at most two different slices
    start, goal = (0, 0, 0), (2, 2, 2)
    seen, frontier, rounds = {start}, [start], 0
    while goal not in seen:
        nxt = []
        for s in frontier:
            for pick in [p for k in (1, 2) for p in combinations(range(3), k)]:
                if all(s[i] < 2 for i in pick):
                    t = tuple(s[i] + (i in pick) for i in range(3))
                    if t not in seen:
                        seen.add(t); nxt.append(t)
        frontier, rounds = nxt, rounds + 1
    assert rounds == 3
    return f"{2 * rounds} min"
N(QA, "Time & Work", "hard",
  "A grill holds two slices of bread at a time and toasts one side of a slice in 2 minutes. Each slice must be toasted on both sides. What is the least time needed to toast three slices?",
  "एक ग्रिल पर एक समय में ब्रेड के दो स्लाइस आते हैं और वह एक स्लाइस का एक तरफ़ 2 मिनट में सेंकती है। हर स्लाइस दोनों तरफ़ सेंकनी है। तीन स्लाइस सेंकने में कम से कम कितना समय लगेगा?",
  ["4 min", "6 min", "8 min", "12 min"], 1,
  "There are 6 sides to toast and the grill does 2 at a time, so at least 3 rounds of 2 minutes are needed -- and 3 rounds are enough if no round is wasted: first A and B on side one; then A on side two and C on side one; then B and C on side two. That is 6 minutes. "
  "8 min finishes A and B together and then leaves C alone on the grill for two rounds, with a space empty; 12 min toasts the slices one at a time; 4 min would toast only 4 of the 6 sides.",
  "सेंकने को 6 तरफ़ हैं और ग्रिल एक बार में 2 सेंकती है, इसलिए कम से कम 2-2 मिनट के 3 दौर चाहिए -- और कोई दौर व्यर्थ न जाए तो 3 पर्याप्त हैं: पहले A और B की पहली तरफ़; फिर A की दूसरी और C की पहली तरफ़; फिर B और C की दूसरी तरफ़। यानी 6 मिनट। "
  "8 मिनट A और B को साथ पूरा करके फिर C को दो दौर अकेले ग्रिल पर छोड़ता है, जिसमें एक जगह ख़ाली रहती है; 12 मिनट स्लाइसों को एक-एक करके सेंकता है; 4 मिनट में 6 में से केवल 4 तरफ़ सिंकतीं।",
  "qa-tw-three-slices-on-a-grill-that-holds-two", _tw2,
  opts_hi=["4 मिनट", "6 मिनट", "8 मिनट", "12 मिनट"])

# ---------------------------------------------------------------- Puzzle Hybrid (3)
def _ph1():
    leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    n = sum(1 for y in range(2005, 2029) if leap(y))
    assert n == 6
    return str(n)
N(QA, "Puzzle Hybrid", "easy",
  "A girl was born on 29 February 2004. Up to and including 2028, how many of her birthdays will have fallen on 29 February itself (not counting the day she was born)?",
  "एक लड़की का जन्म 29 फ़रवरी 2004 को हुआ। 2028 तक (2028 सहित), उसके कितने जन्मदिन ठीक 29 फ़रवरी को पड़े होंगे (जन्म के दिन को न गिनते हुए)?",
  ["5", "6", "7", "24"], 1,
  "29 February comes only in leap years. After 2004 they are 2008, 2012, 2016, 2020, 2024 and 2028 -- six, since 2028 is counted. "
  "7 also counts 2004, the day she was born; 5 leaves out 2028; 24 counts every year, as if the date came each year.",
  "29 फ़रवरी केवल लीप वर्षों में आती है। 2004 के बाद ये 2008, 2012, 2016, 2020, 2024 और 2028 हैं -- छह, क्योंकि 2028 भी गिना जाता है। "
  "7, 2004 को भी गिनता है, जो उसके जन्म का दिन है; 5, 2028 को छोड़ देता है; 24 हर वर्ष को गिनता है, मानो वह तारीख़ हर वर्ष आती हो।",
  "qa-ph-birthdays-on-29-february", _ph1)

def _ph2():
    def works(pieces):
        totals = {sum(s) for k in range(len(pieces) + 1) for s in combinations(pieces, k)}
        return all(d in totals for d in range(1, 8))
    least = None
    for cuts in range(1, 7):
        for pos in combinations(range(1, 7), cuts):
            edges = (0,) + pos + (7,)
            if works([edges[i + 1] - edges[i] for i in range(len(edges) - 1)]):
                least = cuts
                break
        if least:
            break
    assert least == 2 and works([1, 2, 4])
    return str(least)
N(QA, "Puzzle Hybrid", "medium",
  "A worker is to be paid one-seventh of a silver bar at the end of each day for 7 days. The bar is marked into 7 equal parts, and pieces already paid may be taken back as change. What is the least number of cuts needed so that the worker can be paid exactly at the end of every day?",
  "एक श्रमिक को 7 दिनों तक हर दिन के अंत में चाँदी की एक छड़ का सातवाँ भाग दिया जाना है। छड़ पर 7 बराबर भाग अंकित हैं, और पहले दिए टुकड़े छुट्टे के रूप में वापस लिए जा सकते हैं। कम से कम कितने कट चाहिए ताकि श्रमिक को हर दिन के अंत में ठीक भुगतान हो सके?",
  ["1", "2", "3", "6"], 1,
  "Two cuts make pieces of 1, 2 and 4 parts, and every total from 1 to 7 is a sum of some of them. Day 1: give the 1. Day 2: give the 2 and take back the 1. Day 3: give the 1. Day 4: give the 4 and take back the 1 and the 2. Days 5 to 7 repeat the first three on top of the 4. "
  "One cut gives only two pieces, which can make at most three different totals, not seven; 3 cuts and 6 cuts work but are more than needed.",
  "दो कट 1, 2 और 4 भागों के टुकड़े बनाते हैं, और 1 से 7 तक हर योग इनमें से कुछ का जोड़ है। दिन 1: 1 दें। दिन 2: 2 दें और 1 वापस लें। दिन 3: 1 दें। दिन 4: 4 दें और 1 तथा 2 वापस लें। दिन 5 से 7, 4 के ऊपर पहले तीन दिन दोहराते हैं। "
  "एक कट से केवल दो टुकड़े बनते हैं, जिनसे अधिक से अधिक तीन अलग योग बनते हैं, सात नहीं; 3 और 6 कट भी चलते हैं पर आवश्यकता से अधिक हैं।",
  "qa-ph-a-silver-bar-cut-to-pay-a-worker-daily", _ph2)

def _ph3():
    each = F(8, 3)
    a, b = 5 - each, 3 - each
    share = (8 * a / (a + b), 8 * b / (a + b))
    assert share == (7, 1)
    return f"{share[0]} to the first, {share[1]} to the second"
N(QA, "Puzzle Hybrid", "hard",
  "Two travellers, one with 5 loaves and the other with 3, share a meal with a third traveller who has none. The 8 loaves are shared equally among the three. The third traveller then leaves 8 coins to pay for the bread eaten. How should the first two divide the 8 coins fairly?",
  "दो यात्री, एक के पास 5 रोटियाँ और दूसरे के पास 3, एक तीसरे यात्री के साथ भोजन बाँटते हैं जिसके पास कोई रोटी नहीं। 8 रोटियाँ तीनों में बराबर बँटती हैं। फिर तीसरा यात्री खाई गई रोटी के बदले 8 सिक्के छोड़ जाता है। पहले दो यात्रियों को 8 सिक्के उचित रूप से कैसे बाँटने चाहिए?",
  ["4 to the first, 4 to the second", "5 to the first, 3 to the second",
   "6 to the first, 2 to the second", "7 to the first, 1 to the second"], 3,
  "Each of the three ate 8/3 loaves. The first traveller had 5 = 15/3 and ate 8/3, so gave 7/3 to the third; the second had 3 = 9/3, ate 8/3 and gave only 1/3. The third traveller's 8/3 loaves came 7 parts from the first and 1 part from the second, so the coins should go 7 and 1. "
  "5 and 3 pays for the loaves each brought, though each also ate most of their own; 4 and 4 ignores who supplied the bread; 6 and 2 has no basis.",
  "तीनों में से हर एक ने 8/3 रोटियाँ खाईं। पहले यात्री के पास 5 = 15/3 थीं और उसने 8/3 खाईं, इसलिए 7/3 तीसरे को दीं; दूसरे के पास 3 = 9/3 थीं, उसने 8/3 खाईं और केवल 1/3 दी। तीसरे यात्री की 8/3 रोटियों में 7 भाग पहले से और 1 भाग दूसरे से आया, इसलिए सिक्के 7 और 1 में बँटने चाहिए। "
  "5 और 3 हर एक की लाई रोटियों का भुगतान करता है, जबकि हर एक ने अपनी अधिकांश रोटी स्वयं खाई; 4 और 4 इसकी अनदेखी करता है कि रोटी किसने दी; 6 और 2 का कोई आधार नहीं।",
  "qa-ph-travellers-who-share-their-loaves", _ph3,
  opts_hi=["पहले को 4, दूसरे को 4", "पहले को 5, दूसरे को 3", "पहले को 6, दूसरे को 2", "पहले को 7, दूसरे को 1"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    tri = [(a, b, c_) for a in range(1, 30) for b in range(a, 30) for c_ in range(b, 30) if a + b > c_]
    s1 = {len({50, 80, 180 - 130}) < 3}
    s2 = {b == a or c_ == b for a, b, c_ in tri if a + b + c_ == 3 * a}
    both = s1 & s2
    assert s1 == {True} and s2 == {True}
    return _ds(s1, s2, both)
DS(QA, "hard",
   "Does triangle ABC have at least two equal sides?",
   "क्या त्रिभुज ABC की कम से कम दो भुजाएँ बराबर हैं?",
   "Two of its angles are 50° and 80°.", "उसके दो कोण 50° और 80° हैं।",
   "Its perimeter is three times its shortest side.", "उसका परिमाप उसकी सबसे छोटी भुजा का तीन गुना है।",
   1,
   "Statement I alone: the third angle is 180° - 50° - 80° = 50°, so two angles are equal, and the sides opposite them are equal -- yes. "
   "Statement II alone: the other two sides are each at least as long as the shortest, so all three add up to three times the shortest only if both equal it. The triangle is equilateral, so it certainly has two equal sides -- yes. Either statement alone answers the question.",
   "कथन I अकेले: तीसरा कोण 180° - 50° - 80° = 50° है, इसलिए दो कोण बराबर हैं, और उनके सामने की भुजाएँ बराबर हैं -- हाँ। "
   "कथन II अकेले: बाक़ी दोनों भुजाएँ सबसे छोटी भुजा जितनी लंबी तो हैं ही, इसलिए तीनों का योग सबसे छोटी का तीन गुना तभी होगा जब दोनों उसके बराबर हों। त्रिभुज समबाहु है, इसलिए उसकी दो भुजाएँ निश्चित रूप से बराबर हैं -- हाँ। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "qa-ds-two-equal-sides-from-the-angles-or-the-perimeter", _ds1)

def _ds2():
    s1 = {math.gcd(3 * b, b) for b in range(1, 40)}
    s2 = {math.gcd(a, 12) for a in range(1, 100)}
    both = {math.gcd(36, 12)}
    assert len(s1) > 1 and len(s2) > 1 and both == {12}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the HCF of the positive integers a and b?",
   "धनात्मक पूर्णांकों a और b का म.स. (HCF) क्या है?",
   "a = 3b.", "a = 3b।",
   "b = 12.", "b = 12।",
   2,
   "Statement I alone shows that b divides a, so the HCF is b itself -- but it does not say what b is, so it gives no number. Statement II alone says nothing about a. Together, a = 36 and b = 12, and the HCF is 12. Both statements are needed.",
   "कथन I अकेले दिखाता है कि b, a को विभाजित करता है, इसलिए म.स. स्वयं b है -- पर वह यह नहीं बताता कि b क्या है, इसलिए कोई संख्या नहीं मिलती। कथन II अकेले a के बारे में कुछ नहीं कहता। दोनों मिलकर a = 36 और b = 12, और म.स. 12 है। दोनों कथन आवश्यक हैं।",
   "qa-ds-an-hcf-that-is-left-as-a-letter", _ds2)
