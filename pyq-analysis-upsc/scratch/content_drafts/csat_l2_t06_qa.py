# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 6 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Same mix as Tests 1-5 (playbook B.7) with none of their question shapes: the multiplier for a perfect cube,
terminating decimals, two primes with an odd sum, the largest of three numbers from their ratio and LCM, an
exponent equation, numbers with exactly three divisors, the last two digits of 7²⁰²⁵, three-set inclusion and
exclusion; runners on a circular track in one direction, a delay at three-quarters speed, counting telegraph posts,
trains at right angles; a ratio from percentages, provisions for a fort, a working partner, a vessel refilled with
the second liquid, three vessels at once; a slab tax, fresh and dried grapes, compound interest doubling; a
recursion, a series whose differences double; letters with repeats, a circular table; Heron's triangle, a sphere in
a cylinder; the machines fallacy, leaving before the end; the bat and the ball, squares on a chessboard, the
three- and five-litre jugs, cutting a log; and two data-sufficiency items (a statement that is always true, and
sums and differences that do not fix signs). The build spreads the topics through the paper
(csat_common.interleave). Difficulty 3 easy / 19 medium / 12 hard; every key is worked out in code by check()."""
import math
from collections import deque
from fractions import Fraction as F
from itertools import permutations
import csat_common as c
from csat_common import N, DS, QA

def ndiv(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

def inr(n):
    """Indian digit grouping: 500000 -> '5,00,000'."""
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts + [tail])

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    ks = [k for k in range(1, 5000) if round((1620 * k) ** (1 / 3)) ** 3 == 1620 * k]
    assert 1620 == 2 ** 2 * 3 ** 4 * 5 and 1620 * 5 == 90 ** 2 and 1620 * ks[0] == 90 ** 3
    return str(ks[0])
N(QA, "Number Theory", "easy",
  "What is the smallest positive number by which 1620 must be multiplied so that the product is a perfect cube?",
  "वह सबसे छोटी धनात्मक संख्या कौन-सी है जिससे 1620 को गुणा करने पर गुणनफल एक पूर्ण घन हो जाए?",
  ["5", "30", "90", "450"], 3,
  "1620 = 2² × 3⁴ × 5. In a perfect cube every prime appears to a power that is a multiple of 3, so 2² needs one more 2, 3⁴ needs two more 3s (to reach 3⁶) and 5 needs two more 5s: "
  "the multiplier is 2 × 3² × 5² = 450, and 1620 × 450 = 729,000 = 90³. 5 is the multiplier that would make a perfect square (1620 × 5 = 8100 = 90²), not a cube; 30 = 2 × 3 × 5 raises each power by only one; "
  "90 is the cube root of the product, not the multiplier.",
  "1620 = 2² × 3⁴ × 5। पूर्ण घन में हर अभाज्य की घात 3 का गुणज होती है, इसलिए 2² को एक और 2, 3⁴ को दो और 3 (3⁶ तक पहुँचने के लिए) और 5 को दो और 5 चाहिए: "
  "गुणक 2 × 3² × 5² = 450 है, और 1620 × 450 = 729,000 = 90³। 5 वह गुणक है जो पूर्ण वर्ग बनाता (1620 × 5 = 8100 = 90²), घन नहीं; 30 = 2 × 3 × 5 हर घात को केवल एक बढ़ाता है; "
  "90 गुणनफल का घनमूल है, गुणक नहीं।",
  "qa-nt-multiplier-for-a-perfect-cube", _nt1)

def _nt2():
    def terminates(fr):
        d = fr.denominator
        for p in (2, 5):
            while d % p == 0:
                d //= p
        return d == 1
    opts = ["13/30", "9/35", "17/48", "21/70"]
    hits = [o for o in opts if terminates(F(*map(int, o.split("/"))))]
    assert hits == ["21/70"]
    return hits[0]
N(QA, "Number Theory", "medium",
  "Which one of the following fractions can be written as a terminating decimal?",
  "निम्नलिखित भिन्नों में से किसे सांत दशमलव के रूप में लिखा जा सकता है?",
  ["13/30", "9/35", "17/48", "21/70"], 3,
  "A fraction in its lowest terms is a terminating decimal only when its denominator has no prime factor other than 2 and 5. 21/70 reduces to 3/10 = 0.3, so it terminates, even though 70 has the factor 7, which cancels. "
  "The others keep a factor of 3 or 7 in the denominator: 13/30 = 0.4333... (30 = 2 × 3 × 5), 9/35 = 0.257142857142... (35 = 5 × 7) and 17/48 = 0.3541666... (48 = 2⁴ × 3).",
  "किसी भिन्न को न्यूनतम रूप में लिखने पर वह सांत दशमलव तभी होती है जब उसके हर में 2 और 5 के अलावा कोई अभाज्य गुणनखंड न हो। 21/70 घटकर 3/10 = 0.3 हो जाती है, इसलिए वह सांत है, यद्यपि 70 में 7 का गुणनखंड है, जो कट जाता है। "
  "बाक़ियों के हर में 3 या 7 का गुणनखंड बचा रहता है: 13/30 = 0.4333... (30 = 2 × 3 × 5), 9/35 = 0.257142857142... (35 = 5 × 7) और 17/48 = 0.3541666... (48 = 2⁴ × 3)।",
  "qa-nt-terminating-decimal", _nt2)

def _nt3():
    isp = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))
    prods = {p * (99 - p) for p in range(2, 98) if isp(p) and isp(99 - p)}
    assert prods == {194}
    return f"{prods.pop():,}"
N(QA, "Number Theory", "medium",
  "The sum of two prime numbers is 99. What is their product?",
  "दो अभाज्य संख्याओं का योग 99 है। उनका गुणनफल क्या है?",
  ["194", "2,444", "2,450", "9,603"], 0,
  "The sum of two numbers is odd only when one of them is even and the other odd. The only even prime is 2, so the numbers are 2 and 97, and 97 is indeed prime: the product is 2 × 97 = 194. "
  "2,450 = 49 × 50 and 2,444 = 47 × 52 split 99 into two nearly equal numbers, but 49, 50 and 52 are not primes; 9,603 = 97 × 99 multiplies the larger prime by the sum.",
  "दो संख्याओं का योग विषम तभी होता है जब उनमें से एक सम और दूसरी विषम हो। एकमात्र सम अभाज्य 2 है, इसलिए संख्याएँ 2 और 97 हैं, और 97 सचमुच अभाज्य है: गुणनफल 2 × 97 = 194। "
  "2,450 = 49 × 50 और 2,444 = 47 × 52 संख्या 99 को लगभग बराबर दो भागों में बाँटते हैं, पर 49, 50 और 52 अभाज्य नहीं हैं; 9,603 = 97 × 99 बड़े अभाज्य को योग से गुणा करता है।",
  "qa-nt-two-primes-with-sum-99", _nt3)

def _nt4():
    ks = [k for k in range(1, 500) if math.lcm(3 * k, 4 * k, 5 * k) == 1800]
    assert ks == [30] and math.gcd(90, 120, 150) == 30
    return str(5 * ks[0])
N(QA, "Number Theory", "medium",
  "Three numbers are in the ratio 3 : 4 : 5 and their LCM is 1800. What is the largest of the three numbers?",
  "तीन संख्याएँ 3 : 4 : 5 के अनुपात में हैं और उनका LCM 1800 है। तीनों संख्याओं में सबसे बड़ी संख्या क्या है?",
  ["30", "90", "120", "150"], 3,
  "Write the numbers as 3k, 4k and 5k. Since 3, 4 and 5 have no common factor, their LCM is 3 × 4 × 5 × k = 60k, so 60k = 1800 and k = 30. The numbers are 90, 120 and 150, and the largest is 150. "
  "30 is the common factor k, which is the HCF; 90 and 120 are the smallest and the middle number.",
  "संख्याओं को 3k, 4k और 5k लिखिए। चूँकि 3, 4 और 5 का कोई उभयनिष्ठ गुणनखंड नहीं है, उनका LCM 3 × 4 × 5 × k = 60k है, इसलिए 60k = 1800 और k = 30। संख्याएँ 90, 120 और 150 हैं, और सबसे बड़ी 150 है। "
  "30 उभयनिष्ठ गुणनखंड k, यानी HCF, है; 90 और 120 सबसे छोटी और बीच की संख्याएँ हैं।",
  "qa-nt-ratio-and-lcm-largest-number", _nt4)

def _nt5():
    return str(next(x for x in range(0, 30) if 3 ** (x + 1) + 3 ** x == 108))
N(QA, "Number Theory", "medium",
  "If 3ˣ⁺¹ + 3ˣ = 108, what is the value of x?",
  "यदि 3ˣ⁺¹ + 3ˣ = 108, तो x का मान क्या है?",
  ["3", "4", "27", "81"], 0,
  "Take 3ˣ out as a common factor: 3ˣ × (3 + 1) = 108, so 3ˣ = 27 = 3³ and x = 3. Check: 3⁴ + 3³ = 81 + 27 = 108. "
  "27 is the value of 3ˣ and 81 the value of 3ˣ⁺¹, not the value of x; x = 4 would give 3⁵ + 3⁴ = 324.",
  "3ˣ को उभयनिष्ठ गुणनखंड के रूप में बाहर निकालिए: 3ˣ × (3 + 1) = 108, अतः 3ˣ = 27 = 3³ और x = 3। जाँच: 3⁴ + 3³ = 81 + 27 = 108। "
  "27, 3ˣ का मान है और 81, 3ˣ⁺¹ का, x का नहीं; x = 4 से 3⁵ + 3⁴ = 324 मिलता है।",
  "qa-nt-exponent-equation", _nt5)

N(QA, "Number Theory", "hard",
  "How many positive integers less than 200 have exactly three positive divisors?",
  "200 से छोटे कितने धनात्मक पूर्णांकों के ठीक तीन धनात्मक भाजक हैं?",
  ["4", "6", "13", "14"], 1,
  "A number has exactly three divisors only if it is the square of a prime: p² has the divisors 1, p and p². The primes with p² below 200 are 2, 3, 5, 7, 11 and 13 (13² = 169, while 17² = 289 is too large), "
  "giving six numbers: 4, 9, 25, 49, 121 and 169. 14 counts every perfect square up to 14² = 196, and 13 drops only 1² -- but a square of a composite number such as 36 has more than three divisors; "
  "4 stops at 7², the squares below 100.",
  "किसी संख्या के ठीक तीन भाजक तभी होते हैं जब वह किसी अभाज्य का वर्ग हो: p² के भाजक 1, p और p² होते हैं। जिन अभाज्यों के लिए p², 200 से छोटा है वे 2, 3, 5, 7, 11 और 13 हैं (13² = 169, जबकि 17² = 289 बहुत बड़ा है), "
  "यानी छह संख्याएँ: 4, 9, 25, 49, 121 और 169। 14, 14² = 196 तक के हर पूर्ण वर्ग को गिनता है, और 13 केवल 1² छोड़ता है -- पर 36 जैसी भाज्य संख्या के वर्ग के तीन से अधिक भाजक होते हैं; "
  "4, 7² पर रुक जाता है, यानी 100 से छोटे वर्ग।",
  "qa-nt-exactly-three-divisors", lambda: str(sum(1 for n in range(1, 200) if ndiv(n) == 3)))

N(QA, "Number Theory", "medium",
  "What are the last two digits of 7²⁰²⁵?",
  "7²⁰²⁵ के अंतिम दो अंक क्या हैं?",
  ["01", "07", "43", "49"], 1,
  "The last two digits of the powers of 7 repeat in a cycle of four: 7¹ = 07, 7² = 49, 7³ = 343 → 43, 7⁴ = 2401 → 01, and then 07 again. Since 2025 = 4 × 506 + 1, 7²⁰²⁵ ends in the same two digits as 7¹: 07. "
  "The other options are the endings of the neighbouring powers: 01 for 7²⁰²⁴, 49 for 7²⁰²⁶ and 43 for 7²⁰²⁷.",
  "7 की घातों के अंतिम दो अंक चार के चक्र में दोहराते हैं: 7¹ = 07, 7² = 49, 7³ = 343 → 43, 7⁴ = 2401 → 01, और फिर 07। चूँकि 2025 = 4 × 506 + 1, 7²⁰²⁵ के अंतिम दो अंक वही हैं जो 7¹ के: 07। "
  "बाक़ी विकल्प पड़ोसी घातों के अंतिम अंक हैं: 7²⁰²⁴ के लिए 01, 7²⁰²⁶ के लिए 49 और 7²⁰²⁷ के लिए 43।",
  "qa-nt-last-two-digits-of-7-to-2025", lambda: str(pow(7, 2025, 100)).zfill(2))

N(QA, "Number Theory", "hard",
  "How many of the integers from 1 to 1000 are divisible by none of 4, 6 and 10?",
  "1 से 1000 तक के कितने पूर्णांक 4, 6 और 10 में से किसी से भी विभाज्य नहीं हैं?",
  ["366", "484", "634", "750"], 2,
  "Use inclusion and exclusion. Multiples of 4: 250; of 6: 166; of 10: 100. Multiples of both 4 and 6 (that is, of 12): 83; of 4 and 10 (of 20): 50; of 6 and 10 (of 30): 33. Multiples of all three (of 60): 16. "
  "So 250 + 166 + 100 - 83 - 50 - 33 + 16 = 366 numbers are divisible by at least one of them, and 1000 - 366 = 634 are divisible by none. 366 is the count divisible by at least one; "
  "484 subtracts 250 + 166 + 100 = 516 without adding back the overlaps; 750 removes only the multiples of 4.",
  "समावेशन-अपवर्जन का प्रयोग कीजिए। 4 के गुणज: 250; 6 के: 166; 10 के: 100। 4 और 6 दोनों के (यानी 12 के) गुणज: 83; 4 और 10 के (20 के): 50; 6 और 10 के (30 के): 33। तीनों के (60 के) गुणज: 16। "
  "अतः 250 + 166 + 100 - 83 - 50 - 33 + 16 = 366 संख्याएँ उनमें से कम से कम एक से विभाज्य हैं, और 1000 - 366 = 634 किसी से भी विभाज्य नहीं। 366 कम से कम एक से विभाज्य संख्याओं की गिनती है; "
  "484 में 250 + 166 + 100 = 516 घटाया गया है पर अतिव्यापन वापस नहीं जोड़ा गया; 750 केवल 4 के गुणज हटाता है।",
  "qa-nt-divisible-by-none-of-4-6-10", lambda: str(sum(1 for n in range(1, 1001) if n % 4 and n % 6 and n % 10)))

# ---------------------------------------------------------------- Speed-Distance-Time (4)
N(QA, "Speed-Distance-Time", "hard",
  "Two runners start together from the same point of a circular track 400 m long and run in the same direction at 12 m/s and 8 m/s. After how many seconds will they meet again for the first time?",
  "दो धावक 400 मीटर लंबे एक वृत्ताकार ट्रैक के एक ही बिंदु से एक साथ दौड़ना शुरू करते हैं और एक ही दिशा में 12 मीटर/सेकंड तथा 8 मीटर/सेकंड की चाल से दौड़ते हैं। वे पहली बार कितने सेकंड बाद फिर मिलेंगे?",
  ["20", "50", "100", "400"], 2,
  "Running in the same direction, the faster runner gains 12 - 8 = 4 m on the slower one every second, and they meet again when the gain is one full lap, 400 m: 400 ÷ 4 = 100 seconds. "
  "20 s is the time they would take to meet if they ran in opposite directions (400 ÷ (12 + 8)); 50 s is the time the slower runner takes for one lap (400 ÷ 8); 400 is the length of the track, not a time.",
  "एक ही दिशा में दौड़ते हुए तेज़ धावक हर सेकंड धीमे धावक पर 12 - 8 = 4 मीटर की बढ़त बनाता है, और वे तब फिर मिलते हैं जब बढ़त पूरे एक चक्कर, 400 मीटर, की हो जाए: 400 ÷ 4 = 100 सेकंड। "
  "20 सेकंड वह समय है जिसमें वे मिलते यदि विपरीत दिशाओं में दौड़ते (400 ÷ (12 + 8)); 50 सेकंड धीमे धावक का एक चक्कर लगाने का समय है (400 ÷ 8); 400 ट्रैक की लंबाई है, समय नहीं।",
  "qa-sdt-runners-same-direction-on-a-track", lambda: str(F(400, 12 - 8)))

def _sdt2():
    t = next(t for t in range(1, 600) if t * (F(4, 3) - 1) == 30)
    return f"{t // 60} hour{'s' if t // 60 > 1 else ''}" + (f" {t % 60} minutes" if t % 60 else "")
N(QA, "Speed-Distance-Time", "medium",
  "A man reaches his office 30 minutes late when he drives at three-quarters of his usual speed. How long does he usually take to reach the office?",
  "एक व्यक्ति अपनी सामान्य चाल की तीन-चौथाई चाल से गाड़ी चलाने पर अपने दफ़्तर 30 मिनट देर से पहुँचता है। वह सामान्यतः दफ़्तर पहुँचने में कितना समय लेता है?",
  ["1 hour 30 minutes", "2 hours", "2 hours 30 minutes", "3 hours"], 0,
  "At three-quarters of the speed the journey takes 4/3 of the usual time, so the delay is one-third of the usual time. A delay of 30 minutes is therefore one-third of 90 minutes: the usual time is 1 hour 30 minutes "
  "(and the slower journey takes 2 hours). For the other options the delay would not be 30 minutes: a usual time of 2 hours gives a delay of 40 minutes, 2 hours 30 minutes gives 50 minutes, and 3 hours gives 1 hour.",
  "तीन-चौथाई चाल पर यात्रा में सामान्य समय का 4/3 लगता है, इसलिए देरी सामान्य समय का एक-तिहाई होती है। 30 मिनट की देरी इसलिए 90 मिनट का एक-तिहाई है: सामान्य समय 1 घंटा 30 मिनट है "
  "(और धीमी यात्रा में 2 घंटे लगते हैं)। बाक़ी विकल्पों में देरी 30 मिनट नहीं होती: सामान्य समय 2 घंटे हो तो देरी 40 मिनट, 2 घंटे 30 मिनट हो तो 50 मिनट, और 3 घंटे हो तो 1 घंटा होती है।",
  "qa-sdt-late-at-three-quarters-speed", _sdt2,
  opts_hi=["1 घंटा 30 मिनट", "2 घंटे", "2 घंटे 30 मिनट", "3 घंटे"])

def _sdt3():
    metres = (21 - 1) * 50
    return f"{round(F(metres, 60) * F(18, 5))} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "A passenger in a moving train counts 21 telegraph posts in exactly one minute. If the posts are 50 metres apart, what is the speed of the train?",
  "चलती रेलगाड़ी में बैठा एक यात्री ठीक एक मिनट में 21 टेलीग्राफ़ खंभे गिनता है। यदि खंभे 50 मीटर की दूरी पर हैं, तो रेलगाड़ी की चाल क्या है?",
  ["50 km/h", "57 km/h", "60 km/h", "63 km/h"], 2,
  "21 posts have 20 gaps between them, so the train covers 20 × 50 = 1000 m in 60 seconds: 1000/60 = 50/3 m/s, which is 50/3 × 18/5 = 60 km/h. 63 km/h counts 21 gaps (1050 m) and 57 km/h counts 19 gaps (950 m); "
  "50 km/h multiplies the speed in m/s by 3 instead of by 3.6.",
  "21 खंभों के बीच 20 अंतराल होते हैं, इसलिए रेलगाड़ी 60 सेकंड में 20 × 50 = 1000 मीटर चलती है: 1000/60 = 50/3 मीटर/सेकंड, जो 50/3 × 18/5 = 60 किमी/घंटा है। 63 किमी/घंटा 21 अंतराल (1050 मीटर) गिनता है और 57 किमी/घंटा 19 अंतराल (950 मीटर); "
  "50 किमी/घंटा मीटर/सेकंड वाली चाल को 3.6 के बजाय 3 से गुणा करता है।",
  "qa-sdt-counting-telegraph-posts", _sdt3,
  opts_hi=["50 किमी/घंटा", "57 किमी/घंटा", "60 किमी/घंटा", "63 किमी/घंटा"])

N(QA, "Speed-Distance-Time", "easy",
  "Two trains leave a station at the same time, one going east at 40 km/h and the other going north at 30 km/h. How far apart are they after 3 hours?",
  "दो रेलगाड़ियाँ एक स्टेशन से एक ही समय पर चलती हैं, एक पूर्व की ओर 40 किमी/घंटा से और दूसरी उत्तर की ओर 30 किमी/घंटा से। 3 घंटे बाद वे एक-दूसरे से कितनी दूर हैं?",
  ["30 km", "90 km", "120 km", "150 km"], 3,
  "In 3 hours the first train is 40 × 3 = 120 km east of the station and the second 30 × 3 = 90 km north. East and north are at right angles, so the distance between the trains is the hypotenuse of a right triangle with sides 120 km and 90 km: "
  "√(120² + 90²) = 30 × √(16 + 9) = 150 km. 90 km and 120 km are the distances covered by the two trains; 30 km is the gap that would result if both ran in the same direction ((40 - 30) × 3).",
  "3 घंटे में पहली रेलगाड़ी स्टेशन से 40 × 3 = 120 किमी पूर्व में और दूसरी 30 × 3 = 90 किमी उत्तर में है। पूर्व और उत्तर समकोण पर हैं, इसलिए रेलगाड़ियों के बीच की दूरी 120 किमी और 90 किमी भुजाओं वाले समकोण त्रिभुज का कर्ण है: "
  "√(120² + 90²) = 30 × √(16 + 9) = 150 किमी। 90 किमी और 120 किमी दोनों रेलगाड़ियों द्वारा तय दूरियाँ हैं; 30 किमी वह अंतर है जो दोनों के एक ही दिशा में चलने पर होता ((40 - 30) × 3)।",
  "qa-sdt-trains-at-right-angles", lambda: f"{round(math.hypot(40 * 3, 30 * 3))} km",
  opts_hi=["30 किमी", "90 किमी", "120 किमी", "150 किमी"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    r = F(40, 100) * 60 / (F(50, 100) * 40)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a college, 60% of the students are boys. If 40% of the boys and 50% of the girls live in the hostel, what is the ratio of boys to girls in the hostel?",
  "एक महाविद्यालय में 60% विद्यार्थी लड़के हैं। यदि 40% लड़के और 50% लड़कियाँ छात्रावास में रहती हैं, तो छात्रावास में लड़कों और लड़कियों का अनुपात क्या है?",
  ["3 : 2", "4 : 5", "5 : 6", "6 : 5"], 3,
  "Take 100 students: 60 boys and 40 girls. In the hostel there are 40% of 60 = 24 boys and 50% of 40 = 20 girls, a ratio of 24 : 20 = 6 : 5. "
  "3 : 2 is the ratio of boys to girls in the whole college; 4 : 5 is only the ratio of the two percentages, 40 : 50; 5 : 6 is the answer upside down.",
  "100 विद्यार्थी मानिए: 60 लड़के और 40 लड़कियाँ। छात्रावास में 60 का 40% = 24 लड़के और 40 का 50% = 20 लड़कियाँ हैं, अनुपात 24 : 20 = 6 : 5। "
  "3 : 2 पूरे महाविद्यालय में लड़कों और लड़कियों का अनुपात है; 4 : 5 केवल दोनों प्रतिशतों का अनुपात, 40 : 50, है; 5 : 6 उत्तर को उलट देता है।",
  "qa-rm-hostel-ratio-from-percentages", _rm1)

N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A fort has provisions for 200 men for 40 days. After 10 days, 50 men leave the fort. For how many more days will the remaining provisions last the men who are left?",
  "एक क़िले में 200 आदमियों के लिए 40 दिन की रसद है। 10 दिन बाद 50 आदमी क़िला छोड़कर चले जाते हैं। शेष रसद बचे हुए आदमियों के लिए कितने और दिन चलेगी?",
  ["30", "36", "40", "50"], 2,
  "The provisions are 200 × 40 = 8,000 man-days. In 10 days the 200 men use 2,000 of them, leaving 6,000. For the 150 men who remain that lasts 6,000 ÷ 150 = 40 more days. "
  "30 is the number of days left on the original plan, which would hold only if nobody had left; 36 and 50 do not fit the 6,000 man-days left (150 men would use 5,400 in 36 days and 7,500 in 50).",
  "रसद 200 × 40 = 8,000 आदमी-दिन है। 10 दिनों में 200 आदमी उसका 2,000 उपयोग कर लेते हैं, और 6,000 बचता है। बचे 150 आदमियों के लिए यह 6,000 ÷ 150 = 40 और दिन चलेगा। "
  "30 मूल योजना के बचे दिन हैं, जो तभी सही होते जब कोई गया न होता; 36 और 50 बचे 6,000 आदमी-दिन से मेल नहीं खाते (150 आदमी 36 दिन में 5,400 और 50 दिन में 7,500 उपयोग करते)।",
  "qa-rm-provisions-for-a-fort", lambda: str(F(200 * 40 - 200 * 10, 150)))

def _rm3():
    mgmt = F(10, 100) * 10000
    a = mgmt + (10000 - mgmt) * F(12, 12 + 18)
    return f"₹{int(a):,}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A and B invest ₹12,000 and ₹18,000 in a business. A manages the business and is paid 10% of the profit for doing so; the rest of the profit is shared in the ratio of their investments. "
  "If the total profit is ₹10,000, how much does A receive in all?",
  "A और B किसी व्यवसाय में ₹12,000 और ₹18,000 लगाते हैं। A व्यवसाय का प्रबंधन करता है और इसके लिए उसे लाभ का 10% मिलता है; शेष लाभ उनके निवेश के अनुपात में बाँटा जाता है। "
  "यदि कुल लाभ ₹10,000 है, तो A को कुल कितना मिलता है?",
  ["₹4,000", "₹4,600", "₹5,400", "₹6,000"], 1,
  "A's pay for managing is 10% of ₹10,000 = ₹1,000. The remaining ₹9,000 is shared in the ratio 12,000 : 18,000 = 2 : 3, so A gets 2/5 of ₹9,000 = ₹3,600 and B gets ₹5,400. A receives ₹1,000 + ₹3,600 = ₹4,600. "
  "₹4,000 is 2/5 of the whole profit, with no pay for managing; ₹5,400 is B's final share; ₹6,000 is B's share by investment alone, 3/5 of ₹10,000.",
  "प्रबंधन के लिए A का पारिश्रमिक ₹10,000 का 10% = ₹1,000 है। शेष ₹9,000 निवेश के अनुपात 12,000 : 18,000 = 2 : 3 में बँटता है, इसलिए A को ₹9,000 का 2/5 = ₹3,600 और B को ₹5,400 मिलते हैं। A को कुल ₹1,000 + ₹3,600 = ₹4,600 मिलते हैं। "
  "₹4,000 पूरे लाभ का 2/5 है, प्रबंधन के पारिश्रमिक के बिना; ₹5,400 B का अंतिम हिस्सा है; ₹6,000 केवल निवेश के आधार पर B का हिस्सा है, ₹10,000 का 3/5।",
  "qa-rm-working-partner-and-sleeping-partner", _rm3)

def _rm4():
    sols = []
    for total in range(12, 400, 12):
        p, q = F(7 * total, 12), F(5 * total, 12)
        p2, q2 = p - F(9 * 7, 12), q - F(9 * 5, 12) + 9
        if p2 * 9 == q2 * 7:
            sols.append(p)
    assert len(sols) == 1
    return str(sols[0])
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A vessel contains two liquids P and Q in the ratio 7 : 5. When 9 litres of the mixture are drawn off and the vessel is filled with Q, the ratio of P to Q becomes 7 : 9. How many litres of P were in the vessel at first?",
  "एक पात्र में दो द्रव P और Q 7 : 5 के अनुपात में हैं। जब मिश्रण के 9 लीटर निकाल लिए जाते हैं और पात्र को Q से भर दिया जाता है, तो P और Q का अनुपात 7 : 9 हो जाता है। शुरू में पात्र में P के कितने लीटर थे?",
  ["21", "28", "36", "45"], 0,
  "Let the vessel hold 12k litres: 7k of P and 5k of Q. Drawing off 9 litres removes 9 × 7/12 = 5.25 litres of P and 3.75 litres of Q, and refilling with Q brings back 9 litres of it: P = 7k - 5.25, Q = 5k - 3.75 + 9 = 5k + 5.25. "
  "Then (7k - 5.25) : (5k + 5.25) = 7 : 9 gives 63k - 47.25 = 35k + 36.75, so 28k = 84 and k = 3. The vessel holds 36 litres and P was 7 × 3 = 21 litres (afterwards 15.75 : 20.25 = 7 : 9). "
  "36 is the whole vessel; 28 takes 7/9 of it; 45 adds the 9 litres drawn off to the total.",
  "मान लीजिए पात्र में 12k लीटर है: 7k लीटर P और 5k लीटर Q। 9 लीटर निकालने पर 9 × 7/12 = 5.25 लीटर P और 3.75 लीटर Q निकल जाते हैं, और Q से भरने पर उसके 9 लीटर वापस आ जाते हैं: P = 7k - 5.25, Q = 5k - 3.75 + 9 = 5k + 5.25। "
  "तब (7k - 5.25) : (5k + 5.25) = 7 : 9 से 63k - 47.25 = 35k + 36.75, अतः 28k = 84 और k = 3। पात्र में 36 लीटर है और P शुरू में 7 × 3 = 21 लीटर था (बाद में 15.75 : 20.25 = 7 : 9)। "
  "36 पूरा पात्र है; 28 उसका 7/9 लेता है; 45 निकाले गए 9 लीटर को कुल में जोड़ देता है।",
  "qa-rm-drawn-off-and-refilled-with-the-second-liquid", _rm4)

def _rm5():
    milk = F(4, 5) * 30 + F(3, 4) * 20 + F(3, 5) * 10
    water = 60 - milk
    r = milk / water
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "Three vessels whose capacities are in the ratio 3 : 2 : 1 are completely filled with mixtures of milk and water in the ratios 4 : 1, 3 : 1 and 3 : 2 respectively. "
  "All three are emptied into one large vessel. What is the ratio of milk to water in the large vessel?",
  "तीन पात्रों की धारिताएँ 3 : 2 : 1 के अनुपात में हैं और वे क्रमशः 4 : 1, 3 : 1 और 3 : 2 के अनुपात वाले दूध और पानी के मिश्रणों से पूरे भरे हैं। "
  "तीनों को एक बड़े पात्र में उँडेल दिया जाता है। बड़े पात्र में दूध और पानी का अनुपात क्या है?",
  ["2 : 1", "5 : 2", "3 : 1", "7 : 2"], 2,
  "Let the capacities be 30, 20 and 10 litres. Milk: 4/5 of 30 = 24, 3/4 of 20 = 15 and 3/5 of 10 = 6, in all 45 litres. Water: 6 + 5 + 4 = 15 litres. The ratio of milk to water is 45 : 15 = 3 : 1. "
  "5 : 2 adds the ratio terms directly (4 + 3 + 3 : 1 + 1 + 2), as if the vessels held equal amounts; 2 : 1 and 7 : 2 do not match the totals of 45 litres of milk and 15 of water.",
  "धारिताएँ 30, 20 और 10 लीटर मानिए। दूध: 30 का 4/5 = 24, 20 का 3/4 = 15 और 10 का 3/5 = 6, कुल 45 लीटर। पानी: 6 + 5 + 4 = 15 लीटर। दूध और पानी का अनुपात 45 : 15 = 3 : 1। "
  "5 : 2 अनुपात के पदों को सीधे जोड़ता है (4 + 3 + 3 : 1 + 1 + 2), मानो पात्रों में बराबर मात्रा हो; 2 : 1 और 7 : 2, 45 लीटर दूध और 15 लीटर पानी के कुल से मेल नहीं खाते।",
  "qa-rm-three-vessels-emptied-together", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    x = next(x for x in range(300000, 2000000, 10000)
             if F(10, 100) * min(x, 300000) + F(20, 100) * max(x - 300000, 0) == 70000)
    return "₹" + inr(x)
N(QA, "Percentage & Profit-Loss", "medium",
  "In a certain country, income up to ₹3,00,000 is taxed at 10% and the part of the income above ₹3,00,000 at 20%. A person pays a total tax of ₹70,000. What is the person's income?",
  "किसी देश में ₹3,00,000 तक की आय पर 10% कर लगता है और ₹3,00,000 से ऊपर की आय के भाग पर 20%। एक व्यक्ति कुल ₹70,000 कर देता है। उस व्यक्ति की आय क्या है?",
  ["₹3,50,000", "₹5,00,000", "₹6,50,000", "₹7,00,000"], 1,
  "The tax on the first ₹3,00,000 is 10% = ₹30,000, so the other ₹40,000 of tax is 20% of the income above ₹3,00,000, which is therefore ₹2,00,000. The income is ₹3,00,000 + ₹2,00,000 = ₹5,00,000. "
  "₹7,00,000 applies 10% to the whole income and ₹3,50,000 applies 20% to it; ₹6,50,000 forgets the ₹30,000 already paid on the first slab (₹70,000 ÷ 20% = ₹3,50,000 added to ₹3,00,000).",
  "पहले ₹3,00,000 पर कर 10% = ₹30,000 है, इसलिए कर के शेष ₹40,000, ₹3,00,000 से ऊपर की आय का 20% हैं, जो इसलिए ₹2,00,000 है। आय ₹3,00,000 + ₹2,00,000 = ₹5,00,000 है। "
  "₹7,00,000 पूरी आय पर 10% लगाता है और ₹3,50,000 उस पर 20%; ₹6,50,000 पहले स्तर पर पहले ही दिए ₹30,000 को भूल जाता है (₹70,000 ÷ 20% = ₹3,50,000, जिसे ₹3,00,000 में जोड़ा गया)।",
  "qa-pp-slab-tax-and-income", _pp1)

N(QA, "Percentage & Profit-Loss", "hard",
  "Fresh grapes contain 90% water by weight and dried grapes contain 20% water. How many kilograms of dried grapes can be obtained from 100 kg of fresh grapes?",
  "ताज़े अंगूरों में भार के हिसाब से 90% पानी होता है और सूखे अंगूरों में 20% पानी। 100 किग्रा ताज़े अंगूरों से कितने किलोग्राम सूखे अंगूर मिल सकते हैं?",
  ["10 kg", "12.5 kg", "20 kg", "87.5 kg"], 1,
  "100 kg of fresh grapes hold 10 kg of dry matter (10%). Dried grapes are 80% dry matter, so the same 10 kg is 80% of their weight: 10 ÷ 0.8 = 12.5 kg. "
  "10 kg forgets that dried grapes still hold 20% water; 20 kg takes 20% of the fresh weight; 87.5 kg is the weight of water lost, not the weight that is left.",
  "100 किग्रा ताज़े अंगूरों में 10 किग्रा शुष्क पदार्थ (10%) होता है। सूखे अंगूर 80% शुष्क पदार्थ हैं, इसलिए वही 10 किग्रा उनके भार का 80% है: 10 ÷ 0.8 = 12.5 किग्रा। "
  "10 किग्रा यह भूल जाता है कि सूखे अंगूरों में भी 20% पानी रहता है; 20 किग्रा ताज़े भार का 20% लेता है; 87.5 किग्रा घटे हुए पानी का भार है, बचा हुआ भार नहीं।",
  "qa-pp-fresh-and-dried-grapes", lambda: f"{float(F(10) / F(8, 10)):g} kg",
  opts_hi=["10 किग्रा", "12.5 किग्रा", "20 किग्रा", "87.5 किग्रा"])

N(QA, "Percentage & Profit-Loss", "medium",
  "At a certain rate of compound interest, compounded annually, a sum of money doubles itself in 5 years. In how many years will it become 8 times itself?",
  "वार्षिक रूप से संयोजित किसी चक्रवृद्धि ब्याज दर पर कोई धनराशि 5 वर्षों में दोगुनी हो जाती है। वह कितने वर्षों में अपनी 8 गुनी हो जाएगी?",
  ["15", "20", "35", "40"], 0,
  "Doubling takes 5 years each time, and 8 = 2 × 2 × 2, so three doublings take 3 × 5 = 15 years. 35 years is the answer for simple interest, where the sum grows by 100% in 5 years (20% a year) "
  "and needs 700% to become 8 times: 700 ÷ 20 = 35; 20 years is four doublings, which gives 16 times; 40 multiplies 5 by 8.",
  "हर बार दोगुना होने में 5 वर्ष लगते हैं, और 8 = 2 × 2 × 2, इसलिए तीन बार दोगुना होने में 3 × 5 = 15 वर्ष लगते हैं। 35 वर्ष साधारण ब्याज का उत्तर है, जिसमें धनराशि 5 वर्षों में 100% (20% प्रति वर्ष) बढ़ती है "
  "और 8 गुनी होने के लिए 700% चाहिए: 700 ÷ 20 = 35; 20 वर्ष चार बार दोगुना होना है, जिससे 16 गुना होता है; 40, 5 को 8 से गुणा करता है।",
  "qa-pp-compound-interest-doubling-to-eight-times", lambda: str(5 * round(math.log2(8))))

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    a = 3
    for _ in range(4):
        a = 2 * a - 1
    return str(a)
N(QA, "Sequences & Series", "medium",
  "In a sequence, the first term is 3 and every later term is one less than twice the term before it. What is the fifth term?",
  "एक अनुक्रम का पहला पद 3 है और हर बाद का पद अपने पिछले पद के दोगुने से 1 कम है। पाँचवाँ पद क्या है?",
  ["17", "18", "33", "63"], 2,
  "The terms are 3, then 2 × 3 - 1 = 5, 2 × 5 - 1 = 9, 2 × 9 - 1 = 17 and 2 × 17 - 1 = 33. The fifth term is 33. "
  "17 is the fourth term; 18 doubles one less than the previous term instead of taking one less than the double; 63 is the fifth term if each term were one more than twice the one before (3, 7, 15, 31, 63).",
  "पद हैं 3, फिर 2 × 3 - 1 = 5, 2 × 5 - 1 = 9, 2 × 9 - 1 = 17 और 2 × 17 - 1 = 33। पाँचवाँ पद 33 है। "
  "17 चौथा पद है; 18, पिछले पद के दोगुने से एक कम लेने के बजाय पिछले पद से एक कम का दोगुना लेता है; 63 पाँचवाँ पद होता यदि हर पद पिछले के दोगुने से एक अधिक होता (3, 7, 15, 31, 63)।",
  "qa-ss-twice-the-last-term-less-one", _ss1)

def _ss2():
    s = [7, 10, 16, 28, None, 100]
    d = [s[1] - s[0], s[2] - s[1], s[3] - s[2]]
    assert d == [3, 6, 12]
    x = s[3] + 2 * d[2] * 1                 # next difference is twice the last, 24
    assert x == 52 and 100 - x == 48 == 2 * 24
    return str(x)
N(QA, "Sequences & Series", "hard",
  "What number should replace the question mark in the series 7, 10, 16, 28, ?, 100?",
  "श्रेणी 7, 10, 16, 28, ?, 100 में प्रश्नचिह्न के स्थान पर कौन-सी संख्या आएगी?",
  ["40", "52", "56", "64"], 1,
  "The differences between the terms are 3, 6, 12, ... -- each is double the one before. So the next differences are 24 and 48: 28 + 24 = 52 and 52 + 48 = 100, which fits the last term. "
  "40 adds the previous difference, 12, again; 56 doubles the term itself; 64 is the average of its neighbours, 28 and 100.",
  "पदों के बीच के अंतर 3, 6, 12, ... हैं -- हर अंतर पिछले का दोगुना है। इसलिए अगले अंतर 24 और 48 हैं: 28 + 24 = 52 और 52 + 48 = 100, जो अंतिम पद से मेल खाता है। "
  "40 पिछला अंतर, 12, फिर से जोड़ता है; 56 स्वयं पद को दोगुना करता है; 64 अपने पड़ोसी पदों, 28 और 100, का औसत है।",
  "qa-ss-differences-that-double", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
N(QA, "Permutation & Combination", "medium",
  "How many different arrangements of the letters of the word BANANA are possible?",
  "BANANA शब्द के अक्षरों की कितनी भिन्न व्यवस्थाएँ संभव हैं?",
  ["60", "120", "360", "720"], 0,
  "The word has 6 letters, with A three times and N twice, so the number of arrangements is 6!/(3! × 2!) = 720/12 = 60. "
  "720 = 6! treats all the letters as different; 360 = 6!/2! corrects only for the two Ns, and 120 = 6!/3! corrects only for the three As.",
  "शब्द में 6 अक्षर हैं, जिनमें A तीन बार और N दो बार आता है, इसलिए व्यवस्थाओं की संख्या 6!/(3! × 2!) = 720/12 = 60 है। "
  "720 = 6! सभी अक्षरों को भिन्न मानता है; 360 = 6!/2! केवल दो N के लिए सुधार करता है, और 120 = 6!/3! केवल तीन A के लिए।",
  "qa-pc-arrangements-of-banana", lambda: str(len(set(permutations("BANANA")))))

def _pc2():
    count = 0
    for p in permutations(range(6)):         # persons 0..5 in seats 0..5; person 0 is X and person 1 is Y
        if p[0] != 0:                        # X fixed in seat 0: one arrangement per rotation class
            continue
        if p.index(1) in (1, 5):             # Y in a seat next to X's
            count += 1
    assert count == 48 and 2 * math.factorial(4) == 48
    return str(count)
N(QA, "Permutation & Combination", "hard",
  "In how many ways can 6 people be seated around a circular table so that two particular people, X and Y, sit next to each other?",
  "6 व्यक्तियों को एक गोल मेज़ के चारों ओर कितने तरीकों से बैठाया जा सकता है कि दो विशेष व्यक्ति, X और Y, एक-दूसरे के बगल में बैठें?",
  ["24", "48", "120", "240"], 1,
  "Treat X and Y as one block. Five units around a circular table can be arranged in (5 - 1)! = 24 ways, and X and Y can change places inside the block in 2 ways: 24 × 2 = 48. "
  "24 forgets the two orders of X and Y; 120 arranges the five units as if they stood in a row (5!); 240 does the same and also swaps X and Y.",
  "X और Y को एक खंड मानिए। एक गोल मेज़ के चारों ओर पाँच इकाइयाँ (5 - 1)! = 24 तरीकों से व्यवस्थित हो सकती हैं, और खंड के भीतर X और Y 2 तरीकों से स्थान बदल सकते हैं: 24 × 2 = 48। "
  "24, X और Y के दो क्रम भूल जाता है; 120 पाँच इकाइयों को ऐसे व्यवस्थित करता है जैसे वे पंक्ति में हों (5!); 240 वही करता है और X तथा Y की अदला-बदली भी जोड़ता है।",
  "qa-pc-circular-table-two-seated-together", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    a, b, cc = 13, 14, 15
    s = F(a + b + cc, 2)
    area = math.isqrt(int(s * (s - a) * (s - b) * (s - cc)))
    assert area * area == s * (s - a) * (s - b) * (s - cc) and area == 84
    return f"{float(F(2 * area, b)):g} cm"
N(QA, "Geometry & Mensuration", "medium",
  "The sides of a triangle are 13 cm, 14 cm and 15 cm. What is the length of the perpendicular drawn to the side of 14 cm from the opposite corner?",
  "एक त्रिभुज की भुजाएँ 13 सेमी, 14 सेमी और 15 सेमी हैं। सामने के शीर्ष से 14 सेमी वाली भुजा पर डाले गए लंब की लंबाई क्या है?",
  ["11.2 cm", "12 cm", "12.9 cm", "13 cm"], 1,
  "The semi-perimeter is 21, so by Heron's formula the area is √(21 × 8 × 7 × 6) = √7056 = 84 cm². The altitude on the side of 14 cm is 2 × 84 ÷ 14 = 12 cm. "
  "11.2 cm is the altitude on the side of 15 cm (168 ÷ 15); 12.9 cm is the altitude on the side of 13 cm (168 ÷ 13); 13 cm is a side of the triangle, not an altitude.",
  "अर्ध-परिमाप 21 है, इसलिए हीरोन के सूत्र से क्षेत्रफल √(21 × 8 × 7 × 6) = √7056 = 84 वर्ग सेमी है। 14 सेमी वाली भुजा पर लंब 2 × 84 ÷ 14 = 12 सेमी है। "
  "11.2 सेमी 15 सेमी वाली भुजा पर लंब है (168 ÷ 15); 12.9 सेमी 13 सेमी वाली भुजा पर लंब है (168 ÷ 13); 13 सेमी त्रिभुज की एक भुजा है, लंब नहीं।",
  "qa-gm-altitude-of-a-13-14-15-triangle", _gm1,
  opts_hi=["11.2 सेमी", "12 सेमी", "12.9 सेमी", "13 सेमी"])

def _gm2():
    rise = (F(4, 3) * F(22, 7) * F(7, 2) ** 3) / (F(22, 7) * 49)
    assert rise == F(7, 6)
    wrong = (F(4, 3) * F(22, 7) * F(7, 2) ** 3) / (F(22, 7) * F(7, 2) ** 2)
    assert wrong == F(14, 3)
    return f"{rise.numerator}/{rise.denominator} cm"
N(QA, "Geometry & Mensuration", "hard",
  "A cylindrical vessel of radius 7 cm contains water. A solid metal sphere of radius 3.5 cm is dropped into it and sinks completely, with no water overflowing. By how much does the water level rise? (Take π = 22/7.)",
  "7 सेमी त्रिज्या वाले एक बेलनाकार पात्र में पानी है। 3.5 सेमी त्रिज्या वाला एक ठोस धातु का गोला उसमें डाला जाता है और पूरी तरह डूब जाता है, पानी बाहर नहीं गिरता। पानी का स्तर कितना ऊपर उठता है? (π = 22/7 लीजिए।)",
  ["7/6 cm", "3.5 cm", "14/3 cm", "7 cm"], 0,
  "The sphere has volume 4/3 × π × (3.5)³ = 4/3 × 22/7 × 343/8 = 539/3 cm³. The water rises as if this volume were spread over the base of the vessel, whose area is π × 7² = 154 cm². "
  "The rise is (539/3) ÷ 154 = 7/6 cm, about 1.17 cm. 3.5 cm is the radius of the sphere and 7 cm its diameter, neither of which has anything to do with the volume; "
  "14/3 cm divides by the area of a circle of radius 3.5 cm (38.5 cm²) instead of the vessel's base.",
  "गोले का आयतन 4/3 × π × (3.5)³ = 4/3 × 22/7 × 343/8 = 539/3 घन सेमी है। पानी ऐसे उठता है मानो यह आयतन पात्र के आधार पर फैला हो, जिसका क्षेत्रफल π × 7² = 154 वर्ग सेमी है। "
  "उठान (539/3) ÷ 154 = 7/6 सेमी, लगभग 1.17 सेमी, है। 3.5 सेमी गोले की त्रिज्या और 7 सेमी उसका व्यास है, जिनका आयतन से कोई संबंध नहीं; "
  "14/3 सेमी पात्र के आधार के बजाय 3.5 सेमी त्रिज्या वाले वृत्त के क्षेत्रफल (38.5 वर्ग सेमी) से भाग देता है।",
  "qa-gm-sphere-dropped-into-a-cylinder", _gm2,
  opts_hi=["7/6 सेमी", "3.5 सेमी", "14/3 सेमी", "7 सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    per_machine = F(5, 5)                    # articles per machine in 5 minutes
    minutes = F(100, 100 * per_machine) * 5
    return f"{minutes} minute{'s' if minutes > 1 else ''}"
N(QA, "Time & Work", "medium",
  "If 5 machines take 5 minutes to make 5 articles, how long would 100 machines take to make 100 articles?",
  "यदि 5 मशीनें 5 वस्तुएँ बनाने में 5 मिनट लेती हैं, तो 100 मशीनें 100 वस्तुएँ बनाने में कितना समय लेंगी?",
  ["1 minute", "5 minutes", "20 minutes", "100 minutes"], 1,
  "Each machine makes one article in 5 minutes (5 machines make 5 articles in 5 minutes). So 100 machines, each making one article in the same time, make 100 articles in 5 minutes. "
  "100 minutes scales the time with the number of articles and forgets that there are now 100 machines; 1 minute and 20 minutes would mean that each machine works faster or slower than before, which the data do not say.",
  "हर मशीन 5 मिनट में एक वस्तु बनाती है (5 मशीनें 5 मिनट में 5 वस्तुएँ बनाती हैं)। इसलिए 100 मशीनें, जिनमें से हर एक उतने ही समय में एक वस्तु बनाती है, 100 वस्तुएँ 5 मिनट में बनाती हैं। "
  "100 मिनट समय को वस्तुओं की संख्या के साथ बढ़ा देता है और भूल जाता है कि अब 100 मशीनें हैं; 1 मिनट और 20 मिनट का अर्थ होता कि हर मशीन पहले से तेज़ या धीमी चलती है, जो आँकड़े नहीं कहते।",
  "qa-tw-machines-and-articles", _tw1,
  opts_hi=["1 मिनट", "5 मिनट", "20 मिनट", "100 मिनट"])

def _tw2():
    sols = [T for T in range(1, 60) if 3 * (T - 2) + 2 * (T - 3) + T == 30]
    assert sols == [7]
    return str(sols[0])
N(QA, "Time & Work", "hard",
  "A, B and C can finish a job alone in 10, 15 and 30 days respectively. They start working together, but A leaves 2 days before the work is finished and B leaves 3 days before it is finished; C works till the end. "
  "In how many days is the work finished?",
  "A, B और C अकेले किसी काम को क्रमशः 10, 15 और 30 दिनों में पूरा कर सकते हैं। वे साथ काम शुरू करते हैं, पर A काम पूरा होने से 2 दिन पहले और B काम पूरा होने से 3 दिन पहले चला जाता है; C अंत तक काम करता है। "
  "काम कितने दिनों में पूरा होता है?",
  ["4", "5", "6", "7"], 3,
  "Let the work take T days. C works all T days, A works T - 2 days and B works T - 3 days. In units of 1/30 of the job a day, A does 3, B does 2 and C does 1, so 3(T - 2) + 2(T - 3) + T = 30, that is 6T - 12 = 30 and T = 7. "
  "Check: A works 5 days (15 units), B 4 days (8 units) and C 7 days (7 units): 30 units in all. 5 days is the time if all three stayed to the end (6 units a day); 4 and 6 do not satisfy the equation.",
  "मान लीजिए काम में T दिन लगते हैं। C सभी T दिन काम करता है, A, T - 2 दिन और B, T - 3 दिन। काम के 1/30 भाग प्रतिदिन की इकाई में A के 3, B के 2 और C के 1 हैं, इसलिए 3(T - 2) + 2(T - 3) + T = 30, यानी 6T - 12 = 30 और T = 7। "
  "जाँच: A 5 दिन (15 इकाइयाँ), B 4 दिन (8 इकाइयाँ) और C 7 दिन (7 इकाइयाँ) काम करते हैं: कुल 30 इकाइयाँ। 5 दिन वह समय है जब तीनों अंत तक रुकते (प्रतिदिन 6 इकाइयाँ); 4 और 6 समीकरण को संतुष्ट नहीं करते।",
  "qa-tw-two-workers-leave-before-the-end", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (4)
N(QA, "Puzzle Hybrid", "easy",
  "A bat and a ball together cost ₹110. The bat costs ₹100 more than the ball. How much does the ball cost?",
  "एक बल्ले और एक गेंद की कुल क़ीमत ₹110 है। बल्ला गेंद से ₹100 महँगा है। गेंद की क़ीमत कितनी है?",
  ["₹5", "₹10", "₹55", "₹100"], 0,
  "If the ball costs x, the bat costs x + 100, so 2x + 100 = 110 and x = 5: the ball costs ₹5 and the bat ₹105. "
  "₹10 comes from subtracting 100 from 110 without noticing that the bat's price already includes the ball's; ₹100 is the difference between the two prices, and ₹55 is half of the total.",
  "यदि गेंद की क़ीमत x है, तो बल्ले की x + 100, इसलिए 2x + 100 = 110 और x = 5: गेंद ₹5 की और बल्ला ₹105 का है। "
  "₹10, 110 में से 100 घटाने से आता है, यह देखे बिना कि बल्ले की क़ीमत में गेंद की क़ीमत पहले से शामिल है; ₹100 दोनों क़ीमतों का अंतर है, और ₹55 कुल का आधा।",
  "qa-ph-bat-and-ball", lambda: "₹" + str(next(x for x in range(0, 111) if x + (x + 100) == 110)))

N(QA, "Puzzle Hybrid", "medium",
  "How many squares of all sizes are there on a chessboard, which is an 8 × 8 board of 64 small squares?",
  "शतरंज की बिसात पर, जो 64 छोटे वर्गों वाली 8 × 8 की बिसात है, सभी आकारों के कुल कितने वर्ग हैं?",
  ["64", "140", "204", "1296"], 2,
  "Squares with a side of k small squares fit in (9 - k)² positions, so the total is 8² + 7² + 6² + 5² + 4² + 3² + 2² + 1² = 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 204. "
  "64 counts only the small squares; 140 leaves out those 64 and adds the rest; 1296 = 36² is the number of rectangles of all shapes, squares included.",
  "k छोटे वर्गों की भुजा वाले वर्ग (9 - k)² स्थानों पर आ सकते हैं, इसलिए कुल 8² + 7² + 6² + 5² + 4² + 3² + 2² + 1² = 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 204। "
  "64 केवल छोटे वर्ग गिनता है; 140 उन 64 को छोड़कर बाक़ी जोड़ता है; 1296 = 36² सभी आकृतियों के आयतों की संख्या है, वर्गों सहित।",
  "qa-ph-squares-on-a-chessboard", lambda: str(sum((9 - k) ** 2 for k in range(1, 9))))

def _ph3():
    cap = (3, 5)
    seen, queue = {(0, 0): 0}, deque([(0, 0)])
    while queue:
        a, b = queue.popleft()
        if b == 4:
            return str(seen[(a, b)])
        nxt = {(cap[0], b), (a, cap[1]), (0, b), (a, 0)}
        pour = min(a, cap[1] - b)
        nxt.add((a - pour, b + pour))
        pour = min(b, cap[0] - a)
        nxt.add((a + pour, b - pour))
        for st in nxt:
            if st not in seen:
                seen[st] = seen[(a, b)] + 1
                queue.append(st)
N(QA, "Puzzle Hybrid", "hard",
  "You have two empty jugs, one holding 3 litres and the other 5 litres, and a tap with unlimited water. A step is filling a jug completely, emptying a jug completely, or pouring from one jug into the other "
  "until the first is empty or the second is full. What is the least number of steps in which exactly 4 litres can be measured in the 5-litre jug?",
  "आपके पास दो ख़ाली जग हैं, एक 3 लीटर का और दूसरा 5 लीटर का, और असीमित पानी वाला एक नल। एक चरण का अर्थ है किसी जग को पूरा भरना, किसी जग को पूरा ख़ाली करना, या एक जग से दूसरे में तब तक उँडेलना जब तक पहला ख़ाली न हो जाए या दूसरा भर न जाए। "
  "5 लीटर के जग में ठीक 4 लीटर नापने के लिए कम से कम कितने चरण चाहिए?",
  ["4", "5", "6", "8"], 2,
  "One route takes 6 steps: fill the 5-litre jug; pour it into the 3-litre jug, leaving 2 litres in the 5-litre jug; empty the 3-litre jug; pour the 2 litres into it; fill the 5-litre jug again; "
  "pour into the 3-litre jug, which has room for only 1 litre, leaving 4 litres in the 5-litre jug. Starting with the 3-litre jug takes 8 steps, and a search of every state shows that nothing shorter than 6 steps works.",
  "एक रास्ते में 6 चरण लगते हैं: 5 लीटर का जग भरिए; उसे 3 लीटर के जग में उँडेलिए, जिससे 5 लीटर के जग में 2 लीटर बचता है; 3 लीटर का जग ख़ाली कीजिए; उसमें वे 2 लीटर उँडेलिए; 5 लीटर का जग फिर भरिए; "
  "3 लीटर के जग में उँडेलिए, जिसमें केवल 1 लीटर की जगह है, और 5 लीटर के जग में 4 लीटर बचते हैं। 3 लीटर के जग से शुरू करने पर 8 चरण लगते हैं, और सभी अवस्थाओं की खोज से पता चलता है कि 6 चरणों से कम में काम नहीं बनता।",
  "qa-ph-three-and-five-litre-jugs", _ph3)

N(QA, "Puzzle Hybrid", "medium",
  "A carpenter takes 6 minutes to cut a long log into 4 pieces. At the same rate, how long will he take to cut an identical log into 8 pieces?",
  "एक बढ़ई एक लंबे लट्ठे को 4 टुकड़ों में काटने में 6 मिनट लेता है। उसी दर से वह वैसे ही एक लट्ठे को 8 टुकड़ों में काटने में कितना समय लेगा?",
  ["12 minutes", "14 minutes", "16 minutes", "21 minutes"], 1,
  "Cutting a log into 4 pieces takes 3 cuts, so each cut takes 6 ÷ 3 = 2 minutes. Cutting it into 8 pieces takes 7 cuts: 7 × 2 = 14 minutes. "
  "12 minutes makes the time proportional to the number of pieces; 16 minutes counts 8 cuts; 21 minutes takes 3 minutes a cut, as if the 4 pieces had needed only 2 cuts.",
  "लट्ठे को 4 टुकड़ों में काटने में 3 कट लगते हैं, इसलिए हर कट में 6 ÷ 3 = 2 मिनट लगते हैं। 8 टुकड़ों में काटने में 7 कट लगते हैं: 7 × 2 = 14 मिनट। "
  "12 मिनट समय को टुकड़ों की संख्या के समानुपाती मानता है; 16 मिनट 8 कट गिनता है; 21 मिनट हर कट के 3 मिनट लेता है, मानो 4 टुकड़ों के लिए केवल 2 कट चाहिए थे।",
  "qa-ph-cutting-a-log-into-pieces", lambda: f"{(8 - 1) * F(6, 4 - 1)} minutes",
  opts_hi=["12 मिनट", "14 मिनट", "16 मिनट", "21 मिनट"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    ns = range(-50, 51)
    s1 = [n % 2 == 0 for n in ns if (n + 3) % 2 == 1]
    s2 = [n % 2 == 0 for n in ns if (n * n - n) % 2 == 0]
    both = [n % 2 == 0 for n in ns if (n + 3) % 2 == 1 and (n * n - n) % 2 == 0]
    return _ds(s1, s2, both)
DS(QA, "medium",
   "Is the integer n even?",
   "क्या पूर्णांक n सम है?",
   "n + 3 is an odd number.", "n + 3 एक विषम संख्या है।",
   "n² - n is divisible by 2.", "n² - n, 2 से विभाज्य है।",
   0,
   "Statement I: if n + 3 is odd, then n is even -- sufficient. Statement II: n² - n = n(n - 1) is the product of two consecutive integers, one of which is even, so it is divisible by 2 for every integer n, odd or even -- "
   "it tells us nothing about n. So the question can be answered using I alone but not using II alone. The trap is to treat II as information about n when it is always true.",
   "कथन I: यदि n + 3 विषम है, तो n सम है -- पर्याप्त। कथन II: n² - n = n(n - 1) दो क्रमागत पूर्णांकों का गुणनफल है, जिनमें से एक सम होता है, इसलिए यह हर पूर्णांक n के लिए, चाहे सम हो या विषम, 2 से विभाज्य है -- "
   "यह n के बारे में कुछ नहीं बताता। अतः प्रश्न का उत्तर केवल I से दिया जा सकता है, केवल II से नहीं। जाल II को n की जानकारी मान लेना है जबकि वह सदा सत्य है।",
   "qa-ds-is-n-even-a-statement-that-is-always-true", _ds1)

def _ds2():
    nz = [n for n in range(-12, 13) if n]
    pairs = [(p, q) for p in nz for q in nz]
    s1 = [p * q > 0 for p, q in pairs if p + q > 0]
    s2 = [p * q > 0 for p, q in pairs if p - q > 0]
    both = [p * q > 0 for p, q in pairs if p + q > 0 and p - q > 0]
    return _ds(s1, s2, both)
DS(QA, "hard",
   "Is the product of the non-zero integers p and q positive?",
   "क्या शून्येतर पूर्णांकों p और q का गुणनफल धनात्मक है?",
   "p + q is positive.", "p + q धनात्मक है।",
   "p - q is positive.", "p - q धनात्मक है।",
   3,
   "Statement I alone: p = 5, q = 3 gives a positive product, but p = 5, q = -3 also has a positive sum and a negative product -- not sufficient. Statement II alone: both of those pairs have a positive p - q (2 and 8), so it fails in the same way. "
   "Together, both pairs still satisfy both statements, and their products are +15 and -15, so the question cannot be answered. The trap is to think that a positive sum and a positive difference force p and q to be positive.",
   "कथन I अकेला: p = 5, q = 3 से गुणनफल धनात्मक है, पर p = 5, q = -3 का योग भी धनात्मक है और गुणनफल ऋणात्मक -- पर्याप्त नहीं। कथन II अकेला: उन दोनों जोड़ियों में p - q धनात्मक है (2 और 8), इसलिए यह उसी तरह विफल होता है। "
   "दोनों साथ: दोनों जोड़ियाँ अब भी दोनों कथनों को संतुष्ट करती हैं, और उनके गुणनफल +15 और -15 हैं, इसलिए प्रश्न का उत्तर नहीं दिया जा सकता। जाल यह सोचना है कि धनात्मक योग और धनात्मक अंतर p और q को धनात्मक बना देते हैं।",
   "qa-ds-sign-of-a-product-from-a-sum-and-a-difference", _ds2)
