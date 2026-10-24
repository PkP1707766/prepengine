# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 3 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Level 3's harder mix (3 easy / 17 medium / 14 hard) with none of the shapes of Level 2 Tests 1-7, Level 1 Minis 1-3 or
Level 3 Tests 1-2: the one perfect cube, numbers divisible by 8 and by 12, a three-digit number twelve times its digit
sum, a quotient of small decimals, a sum of squares divided by 7, consecutive odd squares, two-digit numbers three times
their digit product, the square root of 12 + 2√35; a swimmer carried by a current, a car and a cyclist who arrive apart,
a boat that turns back for a log, a cyclist who rests; a misread pair in an average, a compound ratio, the largest of
five distinct numbers, a rectangle from a ratio and a perimeter, a taxi fare shared by stretches; 'buy three, get one free',
a percentage-point rise, a cost rise that eats a margin; differences that are squares, the sum of triangular numbers;
exactly three heads in five tosses, sweets with at least two each; rain on a hectare, five lines and a circle; a line
held back by its slowest machine, a filler that stops every hour; the largest amount ₹3 and ₹5 stamps cannot make, a
bus fare shared by fewer people, the cuts that make 27 cubes, the digit 1 on a 24-hour clock; and two
data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import product
import math
import csat_common as c
from csat_common import N, S2, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

def _two(one, two):
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _is_cube(n):
    r = round(n ** (1 / 3))
    return any((r + k) ** 3 == n for k in (-1, 0, 1))

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    hit = [n for n in (2500, 3300, 4000, 4913) if _is_cube(n)]
    assert hit == [4913] and 17 ** 3 == 4913 and 15 ** 3 == 3375 and 16 ** 3 == 4096
    return "4,913"
N(QA, "Number Theory", "easy",
  "Which one of the following is the cube of a natural number?",
  "निम्नलिखित में से कौन-सी संख्या किसी प्राकृत संख्या का घन है?",
  ["2,500", "3,300", "4,000", "4,913"], 3,
  "17³ = 17 × 289 = 4,913. The others are not cubes: 2,500 = 50² is a square, and 3,300 and 4,000 lie between 14³ = 2,744, 15³ = 3,375 and 16³ = 4,096 without equalling any of them.",
  "17³ = 17 × 289 = 4,913। बाक़ी घन नहीं हैं: 2,500 = 50² एक वर्ग है, और 3,300 तथा 4,000, 14³ = 2,744, 15³ = 3,375 और 16³ = 4,096 के बीच हैं पर इनमें से किसी के बराबर नहीं।",
  "qa-nt-the-one-perfect-cube", _nt1)

def _nt2():
    ns = [n for n in range(1, 20001) if n % 8 == 0 and n % 12 == 0]
    return _two(all(n % 96 == 0 for n in ns), all(n % 24 == 0 for n in ns))
S2(QA, "Number Theory", "medium",
   "Which of the following statements is/are correct?",
   "निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
   ["Every number that is divisible by both 8 and 12 is divisible by 96.", "Every number that is divisible by both 8 and 12 is divisible by 24."],
   ["हर वह संख्या जो 8 और 12 दोनों से विभाज्य है, 96 से विभाज्य है।", "हर वह संख्या जो 8 और 12 दोनों से विभाज्य है, 24 से विभाज्य है।"],
   1,
   "Only 2 is correct. A number divisible by both 8 and 12 is a multiple of their LCM, 24 (8 = 2³ and 12 = 2² × 3, so the LCM is 2³ × 3), and every multiple of 24 is divisible by 24. "
   "1 multiplies the two divisors instead of taking their LCM: 24 itself is divisible by both 8 and 12 but not by 96. Multiplying works only for divisors that share no factor, such as 8 and 9.",
   "केवल 2 सही है। जो संख्या 8 और 12 दोनों से विभाज्य है वह उनके LCM, 24 का गुणज है (8 = 2³ और 12 = 2² × 3, इसलिए LCM = 2³ × 3), और 24 का हर गुणज 24 से विभाज्य है। "
   "1 दोनों भाजकों का LCM लेने के बजाय उन्हें गुणा करता है: 24 स्वयं 8 और 12 दोनों से विभाज्य है पर 96 से नहीं। गुणा करना केवल उन भाजकों के लिए चलता है जिनमें कोई उभयनिष्ठ गुणनखंड न हो, जैसे 8 और 9।",
   "qa-nt-divisible-by-8-and-by-12", check=_nt2, craft="inference")

def _nt3():
    xs = [n for n in range(100, 1000) if n == 12 * sum(map(int, str(n)))]
    assert xs == [108]
    return str(len(xs))
N(QA, "Number Theory", "hard",
  "How many three-digit numbers are equal to 12 times the sum of their digits?",
  "तीन अंकों की कितनी संख्याएँ अपने अंकों के योग के 12 गुने के बराबर हैं?",
  ["0", "1", "2", "3"], 1,
  "Write the number as 100a + 10b + c. Then 100a + 10b + c = 12(a + b + c), that is 88a = 2b + 11c. The right side is at most 2 × 9 + 11 × 9 = 117, so a = 1 and 2b + 11c = 88. Since 2b is even, 11c must be even, so c is even; c = 8 gives 2b = 0 and b = 0, while c = 6 gives b = 11, which is not a digit. "
  "So only 108 works (12 × (1 + 0 + 8) = 108). 0 misses it; 2 and 3 count numbers that fail the equation.",
  "संख्या को 100a + 10b + c लिखिए। तब 100a + 10b + c = 12(a + b + c), यानी 88a = 2b + 11c। दायाँ पक्ष अधिकतम 2 × 9 + 11 × 9 = 117 है, इसलिए a = 1 और 2b + 11c = 88। चूँकि 2b सम है, 11c सम होना चाहिए, अतः c सम है; c = 8 से 2b = 0 और b = 0 मिलता है, जबकि c = 6 से b = 11, जो अंक नहीं है। "
  "अतः केवल 108 बैठता है (12 × (1 + 0 + 8) = 108)। 0 इसे चूक जाता है; 2 और 3 ऐसी संख्याएँ गिनते हैं जो समीकरण पूरा नहीं करतीं।",
  "qa-nt-a-number-twelve-times-its-digit-sum", _nt3)

def _nt4():
    v = (F(2, 10) * F(2, 10) + F(1, 100)) / (F(1, 10) * F(1, 10) + F(2, 100))
    assert v == F(5, 3)
    return "5/3"
N(QA, "Number Theory", "medium",
  "What is the value of (0.2 × 0.2 + 0.01) ÷ (0.1 × 0.1 + 0.02)?",
  "(0.2 × 0.2 + 0.01) ÷ (0.1 × 0.1 + 0.02) का मान क्या है?",
  ["1/3", "3/5", "5/3", "3"], 2,
  "The numerator is 0.04 + 0.01 = 0.05 and the denominator 0.01 + 0.02 = 0.03, so the value is 0.05 ÷ 0.03 = 5/3. "
  "3/5 turns the fraction upside down; 3 takes 0.2 × 0.2 as 0.4 and 0.1 × 0.1 as 0.1 (0.4 + 0.01 over 0.1 + 0.02 is about 3.4); 1/3 has no basis.",
  "अंश 0.04 + 0.01 = 0.05 है और हर 0.01 + 0.02 = 0.03, इसलिए मान 0.05 ÷ 0.03 = 5/3 है। "
  "3/5 भिन्न को उलट देता है; 3, 0.2 × 0.2 को 0.4 और 0.1 × 0.1 को 0.1 मान लेता है (0.4 + 0.01 बटा 0.1 + 0.02 लगभग 3.4 है); 1/3 का कोई आधार नहीं।",
  "qa-nt-a-quotient-of-small-decimals", _nt4)

def _nt5():
    s = sum(k * k for k in range(1, 20))
    assert s == 19 * 20 * 39 // 6 == 2470
    return str(s % 7)
N(QA, "Number Theory", "medium",
  "What is the remainder when 1² + 2² + 3² + ... + 19² is divided by 7?",
  "1² + 2² + 3² + ... + 19² को 7 से भाग देने पर शेषफल क्या है?",
  ["0", "2", "4", "6"], 3,
  "The sum of the first n squares is n(n + 1)(2n + 1)/6, so here it is 19 × 20 × 39 ÷ 6 = 2,470. Since 7 × 352 = 2,464, the remainder is 6. "
  "(Checking by remainders: the squares of 1 to 7 leave 1, 4, 2, 2, 4, 1, 0, a total of 14, divisible by 7; 19 numbers are two such blocks of seven plus 1² to 5², whose remainders add up to 13, which leaves 6.) 0 is what 1² + ... + 20² leaves; 2 and 4 are slips in adding the remainders.",
  "पहले n वर्गों का योग n(n + 1)(2n + 1)/6 है, इसलिए यहाँ वह 19 × 20 × 39 ÷ 6 = 2,470 है। चूँकि 7 × 352 = 2,464, शेषफल 6 है। "
  "(शेषफलों से जाँच: 1 से 7 के वर्ग 1, 4, 2, 2, 4, 1, 0 शेषफल देते हैं, कुल 14, जो 7 से विभाज्य है; 19 संख्याएँ सात-सात के दो खंड और 1² से 5² हैं, जिनके शेषफलों का योग 13 है, जो 6 बचाता है।) 0 वह शेषफल है जो 1² + ... + 20² देता है; 2 और 4 शेषफल जोड़ने की चूकें हैं।",
  "qa-nt-a-sum-of-squares-divided-by-7", _nt5)

def _nt6():
    diffs = [(2 * n + 1) ** 2 - (2 * n - 1) ** 2 for n in range(1, 500)]
    g = 0
    for x in diffs:
        g = math.gcd(g, x)
    assert g == 8 and 4 ** 2 - 2 ** 2 == 12
    return str(g)
N(QA, "Number Theory", "medium",
  "What is the largest number that always divides the difference between the squares of two consecutive odd numbers?",
  "वह सबसे बड़ी संख्या कौन-सी है जो दो क्रमागत विषम संख्याओं के वर्गों के अंतर को हमेशा विभाजित करती है?",
  ["2", "4", "8", "16"], 2,
  "Two consecutive odd numbers can be written 2n - 1 and 2n + 1, and (2n + 1)² - (2n - 1)² = 8n. So the difference is always a multiple of 8, and since 3² - 1² = 8 itself, nothing larger always divides it. "
  "16 divides 8n only when n is even (it fails for 3² - 1² = 8); 2 and 4 always divide the difference too, but they are not the largest such number.",
  "दो क्रमागत विषम संख्याएँ 2n - 1 और 2n + 1 लिखी जा सकती हैं, और (2n + 1)² - (2n - 1)² = 8n। अतः अंतर हमेशा 8 का गुणज है, और चूँकि 3² - 1² = 8 स्वयं है, इससे बड़ी कोई संख्या हमेशा विभाजित नहीं करती। "
  "16, 8n को केवल तब विभाजित करता है जब n सम हो (3² - 1² = 8 पर विफल होता है); 2 और 4 भी अंतर को हमेशा विभाजित करते हैं, पर वे सबसे बड़ी ऐसी संख्या नहीं हैं।",
  "qa-nt-consecutive-odd-squares", _nt6)

def _nt7():
    xs = [10 * a + b for a in range(1, 10) for b in range(10) if 10 * a + b == 3 * a * b]
    assert xs == [15, 24]
    return str(len(xs))
N(QA, "Number Theory", "hard",
  "How many two-digit numbers are equal to three times the product of their digits?",
  "दो अंकों की कितनी संख्याएँ अपने अंकों के गुणनफल के तीन गुने के बराबर हैं?",
  ["1", "2", "3", "4"], 1,
  "With digits a and b, 10a + b = 3ab, so b = 10a/(3a - 1) must be a whole number from 0 to 9. a = 1 gives b = 10/2 = 5 (15 = 3 × 1 × 5); a = 2 gives b = 20/5 = 4 (24 = 3 × 2 × 4); a = 3 gives 30/8 and a = 4 gives 40/11, neither whole, and for larger a, 10a/(3a - 1) falls below 4 without being whole. "
  "So there are exactly two, 15 and 24. 1 stops at the first; 3 and 4 count values that are not whole.",
  "अंकों a और b के साथ 10a + b = 3ab, इसलिए b = 10a/(3a - 1) को 0 से 9 तक की पूर्ण संख्या होना चाहिए। a = 1 से b = 10/2 = 5 (15 = 3 × 1 × 5); a = 2 से b = 20/5 = 4 (24 = 3 × 2 × 4); a = 3 से 30/8 और a = 4 से 40/11, कोई भी पूर्ण नहीं, और बड़े a के लिए 10a/(3a - 1) बिना पूर्ण हुए 4 से नीचे आ जाता है। "
  "अतः ठीक दो हैं, 15 और 24। 1 पहली पर रुक जाता है; 3 और 4 ऐसे मान गिनते हैं जो पूर्ण नहीं।",
  "qa-nt-three-times-the-digit-product", _nt7)

def _nt8():
    v = math.sqrt(12 + 2 * math.sqrt(35))
    assert abs(v - (math.sqrt(7) + math.sqrt(5))) < 1e-12
    assert abs(v - (math.sqrt(2) + math.sqrt(10))) > 1e-3 and abs(v - (2 + 2 * math.sqrt(2))) > 1e-3
    return "√7 + √5"
N(QA, "Number Theory", "hard",
  "What is the value of √(12 + 2√35)?",
  "√(12 + 2√35) का मान क्या है?",
  ["√7 + √5", "√10 + √2", "2 + 2√2", "2√3 + √35"], 0,
  "Look for √a + √b with (√a + √b)² = a + b + 2√(ab) = 12 + 2√35, that is a + b = 12 and ab = 35: a = 7 and b = 5. So the value is √7 + √5 (about 4.88). "
  "(√10 + √2)² = 12 + 2√20 and (2 + 2√2)² = 12 + 8√2 have the right whole part but the wrong root; 2√3 + √35 simply takes the square root of each term, which is not allowed.",
  "ऐसा √a + √b ढूँढिए जिसके लिए (√a + √b)² = a + b + 2√(ab) = 12 + 2√35, यानी a + b = 12 और ab = 35: a = 7 और b = 5। अतः मान √7 + √5 है (लगभग 4.88)। "
  "(√10 + √2)² = 12 + 2√20 और (2 + 2√2)² = 12 + 8√2 का पूर्ण भाग सही है पर मूल ग़लत; 2√3 + √35 हर पद का अलग-अलग वर्गमूल लेता है, जो अनुमत नहीं।",
  "qa-nt-the-square-root-of-12-plus-2-root-35", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    t = F(60, 1)                               # seconds to cross at 1 m/s straight across
    return f"{int(t * F(1, 2))} m"
N(QA, "Speed-Distance-Time", "medium",
  "A river 60 m wide flows at 0.5 m/s. A swimmer who swims at 1 m/s in still water crosses it, keeping her body pointed straight at the opposite bank throughout. How far downstream of the point directly opposite her start does she land?",
  "60 मीटर चौड़ी एक नदी 0.5 मीटर/सेकंड से बहती है। शांत जल में 1 मीटर/सेकंड से तैरने वाली एक तैराक उसे पार करती है, पूरे समय अपने शरीर को ठीक सामने के किनारे की ओर रखते हुए। वह अपने आरंभ के ठीक सामने वाले बिंदु से धारा की दिशा में कितनी दूर पहुँचती है?",
  ["0 m", "15 m", "30 m", "60 m"], 2,
  "Her motion across the river and the drift with the current happen together and do not affect each other. Crossing 60 m at 1 m/s takes 60 s, and in those 60 s the current carries her 0.5 × 60 = 30 m downstream. "
  "0 m ignores the current; 60 m takes the drift to equal the width; 15 m halves the right answer.",
  "नदी के आर-पार उसकी गति और धारा के साथ बहना एक साथ होते हैं और एक-दूसरे को प्रभावित नहीं करते। 1 मीटर/सेकंड से 60 मीटर पार करने में 60 सेकंड लगते हैं, और उन 60 सेकंडों में धारा उसे 0.5 × 60 = 30 मीटर बहा ले जाती है। "
  "0 मीटर धारा को अनदेखा करता है; 60 मीटर बहाव को चौड़ाई के बराबर मान लेता है; 15 मीटर सही उत्तर का आधा है।",
  "qa-sdt-a-swimmer-carried-by-a-current", _sdt1,
  opts_hi=["0 मीटर", "15 मीटर", "30 मीटर", "60 मीटर"])

def _sdt2():
    ds = [d for d in range(1, 200) if F(d, 15) - F(d, 60) == F(9, 4)]
    assert ds == [45]
    return f"{ds[0]} km"
N(QA, "Speed-Distance-Time", "medium",
  "A car and a cyclist set off together from the same place for the same town. The car travels at 60 km/h and the cyclist at 15 km/h, and the car arrives 2 hours 15 minutes before the cyclist. How far away is the town?",
  "एक कार और एक साइकिल सवार एक ही स्थान से एक ही कस्बे के लिए साथ निकलते हैं। कार 60 किमी/घंटा और साइकिल सवार 15 किमी/घंटा से चलता है, और कार साइकिल सवार से 2 घंटे 15 मिनट पहले पहुँचती है। कस्बा कितनी दूर है?",
  ["45 km", "48 km", "54 km", "60 km"], 0,
  "For a distance d, the cyclist takes d/15 hours and the car d/60, so d/15 - d/60 = 3d/60 = d/20 hours, which must equal 2.25 hours: d = 45 km (the cyclist takes 3 hours, the car 45 minutes). "
  "48 km would make the gap 2 h 24 min; 54 and 60 km would make it 2 h 42 min and 3 h.",
  "दूरी d के लिए साइकिल सवार को d/15 घंटे और कार को d/60 घंटे लगते हैं, इसलिए d/15 - d/60 = 3d/60 = d/20 घंटे, जो 2.25 घंटे के बराबर होना चाहिए: d = 45 किमी (साइकिल सवार को 3 घंटे, कार को 45 मिनट)। "
  "48 किमी पर अंतर 2 घंटे 24 मिनट होता; 54 और 60 किमी पर 2 घंटे 42 मिनट और 3 घंटे।",
  "qa-sdt-a-car-and-a-cyclist-who-arrive-apart", _sdt2,
  opts_hi=["45 किमी", "48 किमी", "54 किमी", "60 किमी"])

def _sdt3():
    currents = set()
    for b in range(4, 40):                     # any boat speed above the current gives the same answer
        for cur in range(1, b):
            gap = (b - cur) * 1 + cur * 1      # after 1 hour: boat upstream, log downstream
            back = F(gap, (b + cur) - cur)     # the boat gains on the log at its own speed b
            if cur * (1 + back) == 6:
                currents.add(cur)
    assert currents == {3}
    return "3 km/h"
N(QA, "Speed-Distance-Time", "hard",
  "A boat going upstream passes a log floating downstream. One hour later the boat turns round and, going downstream, catches up with the log 6 km below the point where they first passed. If the boat's speed relative to the water never changes, what is the speed of the current?",
  "धारा के विरुद्ध जाती एक नाव धारा के साथ बहते एक लट्ठे के पास से गुज़रती है। एक घंटे बाद नाव मुड़ती है और धारा के साथ चलते हुए उस बिंदु से 6 किमी नीचे लट्ठे को पकड़ लेती है जहाँ वे पहली बार मिले थे। यदि जल के सापेक्ष नाव की चाल कभी नहीं बदलती, तो धारा की चाल क्या है?",
  ["2 km/h", "3 km/h", "4 km/h", "6 km/h"], 1,
  "Look at it from the water, which carries both the log and the boat. Relative to the water the log is at rest, and the boat moves away from it for one hour and then back at the same speed, so it takes one hour to return. "
  "The log therefore drifts for 2 hours in all and covers 6 km, so the current runs at 3 km/h -- whatever the boat's own speed. 6 km/h assumes that the log drifted for only an hour; 2 and 4 km/h do not fit the timings.",
  "इसे उस जल की दृष्टि से देखिए जो लट्ठे और नाव दोनों को ले जाता है। जल के सापेक्ष लट्ठा स्थिर है, और नाव एक घंटे उससे दूर जाती है और फिर उसी चाल से लौटती है, इसलिए लौटने में एक घंटा लगता है। "
  "अतः लट्ठा कुल 2 घंटे बहता है और 6 किमी तय करता है, इसलिए धारा 3 किमी/घंटा से बहती है -- नाव की अपनी चाल चाहे जो हो। 6 किमी/घंटा मान लेता है कि लट्ठा केवल एक घंटा बहा; 2 और 4 किमी/घंटा समयों पर नहीं बैठते।",
  "qa-sdt-a-boat-that-turns-back-for-a-log", _sdt3,
  opts_hi=["2 किमी/घंटा", "3 किमी/घंटा", "4 किमी/घंटा", "6 किमी/घंटा"])

def _sdt4():
    left, t = F(30), F(0)
    while True:
        leg = min(left, F(18 * 40, 60))        # 12 km in each 40-minute spell
        t += leg / 18 * 60
        left -= leg
        if left == 0:
            break
        t += 10
    assert t == 120
    return "2 h"
N(QA, "Speed-Distance-Time", "hard",
  "A cyclist rides at a steady 18 km/h but stops for 10 minutes after every 40 minutes of riding. How long does she take to cover 30 km, counting the stops on the way?",
  "एक साइकिल सवार 18 किमी/घंटा की स्थिर चाल से चलती है, पर हर 40 मिनट चलाने के बाद 10 मिनट रुकती है। रास्ते के ठहरावों को गिनते हुए, उसे 30 किमी तय करने में कितना समय लगता है?",
  ["1 h 40 min", "1 h 50 min", "2 h", "2 h 10 min"], 2,
  "Each 40-minute spell covers 18 × 40/60 = 12 km. After two spells and two stops (100 minutes) she has covered 24 km, and the last 6 km take 6/18 h = 20 minutes, after which no stop is needed: 120 minutes, or 2 hours. "
  "1 h 40 min is the riding time alone; 2 h 10 min adds a third stop after she has arrived; 1 h 50 min counts only one stop.",
  "हर 40 मिनट की अवधि में 18 × 40/60 = 12 किमी तय होते हैं। दो अवधियों और दो ठहरावों (100 मिनट) के बाद वह 24 किमी तय कर चुकी है, और अंतिम 6 किमी में 6/18 घंटे = 20 मिनट लगते हैं, जिसके बाद रुकने की आवश्यकता नहीं: 120 मिनट, यानी 2 घंटे। "
  "1 घंटा 40 मिनट केवल चलाने का समय है; 2 घंटे 10 मिनट पहुँचने के बाद तीसरा ठहराव जोड़ता है; 1 घंटा 50 मिनट केवल एक ठहराव गिनता है।",
  "qa-sdt-a-cyclist-who-rests", _sdt4,
  opts_hi=["1 घंटा 40 मिनट", "1 घंटा 50 मिनट", "2 घंटे", "2 घंटे 10 मिनट"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    total = 40 * 52 - (48 + 72) + (84 + 27)
    return f"{F(total, 40):.3f}".rstrip("0") if False else f"{float(F(total, 40))}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The average of 40 numbers was worked out as 52. It was later found that two of the numbers, 84 and 27, had been read as 48 and 72. What is the correct average?",
  "40 संख्याओं का औसत 52 निकाला गया। बाद में पता चला कि दो संख्याएँ, 84 और 27, 48 और 72 पढ़ ली गई थीं। सही औसत क्या है?",
  ["51.55", "51.775", "52.225", "52.45"], 1,
  "The wrong total was 40 × 52 = 2,080. The two misread numbers added 48 + 72 = 120 where the true ones add 84 + 27 = 111, so the correct total is 2,080 - 9 = 2,071 and the average 2,071 ÷ 40 = 51.775. "
  "52.225 adds the 9 instead of subtracting it; 51.55 and 52.45 take the change as 18.",
  "ग़लत योग 40 × 52 = 2,080 था। ग़लत पढ़ी गई दो संख्याओं ने 48 + 72 = 120 जोड़ा जबकि सही संख्याओं का योग 84 + 27 = 111 है, इसलिए सही योग 2,080 - 9 = 2,071 और औसत 2,071 ÷ 40 = 51.775 है। "
  "52.225, 9 घटाने के बजाय जोड़ता है; 51.55 और 52.45 परिवर्तन को 18 मानते हैं।",
  "qa-rm-a-misread-pair-in-an-average", _rm1)

def _rm2():
    a = F(2, 3) * F(4, 5) * F(15, 8)
    assert a == 1
    return "1 : 1"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "What is the ratio compounded of 2 : 3, 4 : 5 and 15 : 8?",
  "2 : 3, 4 : 5 और 15 : 8 का मिश्र (संयुक्त) अनुपात क्या है?",
  ["1 : 1", "8 : 15", "21 : 16", "120 : 1"], 0,
  "A compound ratio multiplies the first terms together and the second terms together: (2 × 4 × 15) : (3 × 5 × 8) = 120 : 120 = 1 : 1. "
  "21 : 16 adds the terms instead of multiplying them; 8 : 15 compounds only the first two ratios and turns the result round; 120 : 1 forgets to multiply the second terms.",
  "मिश्र अनुपात में पहले पदों को आपस में और दूसरे पदों को आपस में गुणा किया जाता है: (2 × 4 × 15) : (3 × 5 × 8) = 120 : 120 = 1 : 1। "
  "21 : 16 पदों को गुणा करने के बजाय जोड़ता है; 8 : 15 केवल पहले दो अनुपातों को मिलाकर परिणाम उलट देता है; 120 : 1 दूसरे पदों को गुणा करना भूल जाता है।",
  "qa-rm-a-compound-ratio", _rm2)

def _rm3():
    best = max(max(t) for t in [(1, 2, 3, 4, 50 - 10)] if len(set(t)) == 5)
    from itertools import combinations
    assert all(50 - sum(s) <= 40 for s in combinations(range(1, 40), 4))
    return str(best)
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "The average of five different positive whole numbers is 10. What is the largest possible value of the greatest of them?",
  "पाँच अलग-अलग धनात्मक पूर्ण संख्याओं का औसत 10 है। उनमें से सबसे बड़ी संख्या का अधिकतम संभव मान क्या है?",
  ["36", "38", "40", "46"], 2,
  "The five numbers add up to 50. To make the greatest as large as possible, make the other four as small as they can be while remaining different: 1, 2, 3 and 4, which add up to 10. That leaves 50 - 10 = 40. "
  "46 forgets that the numbers must be different (1 + 1 + 1 + 1 leaves 46); 36 and 38 do not make the other four as small as possible.",
  "पाँचों संख्याओं का योग 50 है। सबसे बड़ी को अधिकतम बनाने के लिए बाक़ी चार को अलग-अलग रहते हुए जितना छोटा हो सके रखिए: 1, 2, 3 और 4, जिनका योग 10 है। इससे 50 - 10 = 40 बचता है। "
  "46 भूल जाता है कि संख्याएँ अलग-अलग होनी चाहिए (1 + 1 + 1 + 1 से 46 बचता है); 36 और 38 बाक़ी चार को यथासंभव छोटा नहीं रखते।",
  "qa-rm-the-largest-of-five-distinct-numbers", _rm3)

def _rm4():
    ks = [k for k in range(1, 50) if 2 * (3 * k + 2 * k) == 50]
    assert ks == [5] and 12 * 8 == 96 and 2 * (12 + 8) == 40
    k = ks[0]
    return f"{3 * k * 2 * k} cm²"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The length and breadth of a rectangle are in the ratio 3 : 2, and its perimeter is 50 cm. What is its area?",
  "एक आयत की लंबाई और चौड़ाई 3 : 2 के अनुपात में हैं, और उसका परिमाप 50 सेमी है। उसका क्षेत्रफल क्या है?",
  ["96 cm²", "120 cm²", "135 cm²", "150 cm²"], 3,
  "Let the sides be 3k and 2k. The perimeter is 2(3k + 2k) = 10k = 50, so k = 5: the sides are 15 cm and 10 cm and the area is 150 cm². "
  "96 cm² is the area of the 3 : 2 rectangle whose perimeter is 40 cm (12 by 8); 120 and 135 cm² belong to rectangles of other shapes.",
  "मान लीजिए भुजाएँ 3k और 2k हैं। परिमाप 2(3k + 2k) = 10k = 50 है, इसलिए k = 5: भुजाएँ 15 सेमी और 10 सेमी हैं और क्षेत्रफल 150 वर्ग सेमी है। "
  "96 वर्ग सेमी उस 3 : 2 वाले आयत का क्षेत्रफल है जिसका परिमाप 40 सेमी है (12 गुणा 8); 120 और 135 वर्ग सेमी दूसरे आकारों के आयतों के हैं।",
  "qa-rm-a-rectangle-from-a-ratio-and-a-perimeter", _rm4,
  opts_hi=["96 वर्ग सेमी", "120 वर्ग सेमी", "135 वर्ग सेमी", "150 वर्ग सेमी"])

def _rm5():
    per_km = F(900, 30)
    stretches = [(10, "ABC"), (10, "AB"), (10, "A")]       # the first 10 km all three ride, then C leaves, then B
    pay = {x: F(0) for x in "ABC"}
    for km, riders in stretches:
        for x in riders:
            pay[x] += per_km * km / len(riders)
    assert pay == {"A": 550, "B": 250, "C": 100}
    return f"₹{int(pay['B'])}"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A, B and C share a taxi from the same starting point. C gets off after 10 km, B after 20 km and A at the end of the 30 km ride. The fare is ₹900, charged at a flat rate per km, and each stretch of the road is paid for equally by those in the taxi on that stretch. How much does B pay?",
  "A, B और C एक ही आरंभ बिंदु से एक टैक्सी साझा करते हैं। C 10 किमी बाद, B 20 किमी बाद और A 30 किमी की यात्रा के अंत में उतरता है। किराया ₹900 है, जो प्रति किमी एक समान दर से लगता है, और सड़क के हर हिस्से का भुगतान उस हिस्से पर टैक्सी में बैठे लोग बराबर-बराबर करते हैं। B कितना भुगतान करता है?",
  ["₹150", "₹250", "₹300", "₹450"], 1,
  "The fare is ₹30 a km, so each 10-km stretch costs ₹300. The first stretch is shared by all three (₹100 each), the second by A and B (₹150 each), and the last is A's alone. B pays 100 + 150 = ₹250 (C pays ₹100 and A ₹550). "
  "₹300 divides the fare in proportion to the distances, 30 : 20 : 10, which charges B for the first stretch as if he had ridden it alone; ₹150 counts only the second stretch; ₹450 is half the fare.",
  "किराया ₹30 प्रति किमी है, इसलिए हर 10 किमी के हिस्से की लागत ₹300 है। पहला हिस्सा तीनों में बँटता है (₹100 प्रत्येक), दूसरा A और B में (₹150 प्रत्येक), और अंतिम केवल A का। B, 100 + 150 = ₹250 देता है (C ₹100 और A ₹550)। "
  "₹300 किराए को दूरियों 30 : 20 : 10 के अनुपात में बाँटता है, जो पहले हिस्से के लिए B से ऐसे वसूलता है मानो उसने वह अकेले तय किया हो; ₹150 केवल दूसरा हिस्सा गिनता है; ₹450 किराए का आधा है।",
  "qa-rm-a-taxi-fare-shared-by-stretches", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    d = 1 - F(3, 4)
    assert d == F(1, 4)
    return "25 per cent"
N(QA, "Percentage & Profit-Loss", "easy",
  "A shop offers 'buy three, get one free' on packets of tea of the same price. What is the effective discount on the packets taken home?",
  "एक दुकान एक ही मूल्य वाले चाय के पैकेटों पर 'तीन ख़रीदें, एक मुफ़्त पाएँ' का प्रस्ताव देती है। घर ले जाए गए पैकेटों पर वास्तविक छूट कितनी है?",
  ["20 per cent", "25 per cent", "30 per cent", "33⅓ per cent"], 1,
  "Four packets are taken home for the price of three, so the customer pays 3/4 of the full price: a discount of 1/4, that is 25 per cent. "
  "33⅓ per cent divides the free packet by the three paid for, not by the four taken; 20 and 30 per cent have no basis.",
  "चार पैकेट तीन के मूल्य में घर आते हैं, इसलिए ग्राहक पूरे मूल्य का 3/4 चुकाता है: 1/4 की छूट, यानी 25 प्रतिशत। "
  "33⅓ प्रतिशत मुफ़्त पैकेट को चुकाए गए तीन से भाग देता है, घर ले जाए गए चार से नहीं; 20 और 30 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-buy-three-get-one-free", _pp1,
  opts_hi=["20 प्रतिशत", "25 प्रतिशत", "30 प्रतिशत", "33⅓ प्रतिशत"])

def _pp2():
    r = (F(5) - 4) / 4
    assert r == F(1, 4)
    return "25 per cent"
N(QA, "Percentage & Profit-Loss", "medium",
  "The interest rate on a loan rises from 4 per cent to 5 per cent a year. By what percentage has the interest rate itself increased?",
  "एक ऋण पर ब्याज दर 4 प्रतिशत से बढ़कर 5 प्रतिशत वार्षिक हो जाती है। ब्याज दर स्वयं कितने प्रतिशत बढ़ी है?",
  ["1 per cent", "5 per cent", "20 per cent", "25 per cent"], 3,
  "The rate has gone up by 1 percentage point, from 4 to 5, and that rise is 1/4 of the old rate: an increase of 25 per cent. The interest payable on a given loan rises by the same 25 per cent. "
  "'1 per cent' confuses a percentage point with a per cent; 20 per cent divides the rise by the new rate instead of the old; 5 per cent is the new rate itself.",
  "दर 4 से 5 तक 1 प्रतिशत अंक बढ़ी है, और यह वृद्धि पुरानी दर का 1/4 है: 25 प्रतिशत की वृद्धि। किसी दिए गए ऋण पर देय ब्याज भी इसी 25 प्रतिशत से बढ़ता है। "
  "'1 प्रतिशत' प्रतिशत अंक को प्रतिशत से भ्रमित करता है; 20 प्रतिशत वृद्धि को पुरानी दर के बजाय नई दर से भाग देता है; 5 प्रतिशत स्वयं नई दर है।",
  "qa-pp-a-percentage-point-rise", _pp2,
  opts_hi=["1 प्रतिशत", "5 प्रतिशत", "20 प्रतिशत", "25 प्रतिशत"])

def _pp3():
    sp, cost = F(132, 100), F(110, 100)
    r = (sp - cost) / cost
    assert r == F(1, 5)
    return "20 per cent"
N(QA, "Percentage & Profit-Loss", "hard",
  "A shopkeeper was making a profit of 32 per cent on cost. His cost then rose by 10 per cent, but he kept his selling price unchanged. What is his profit now, as a percentage of the new cost?",
  "एक दुकानदार लागत पर 32 प्रतिशत लाभ कमा रहा था। फिर उसकी लागत 10 प्रतिशत बढ़ गई, पर उसने विक्रय मूल्य नहीं बदला। अब नई लागत के प्रतिशत के रूप में उसका लाभ कितना है?",
  ["20 per cent", "21.2 per cent", "22 per cent", "29 per cent"], 0,
  "Take the old cost as 100: the selling price is 132. The new cost is 110, so the profit is 22 on a cost of 110, which is 20 per cent. "
  "22 per cent subtracts the 10 per cent rise from the 32 per cent margin, forgetting that the margin is now measured on a larger cost; 21.2 and 29 per cent have no basis.",
  "पुरानी लागत 100 मानिए: विक्रय मूल्य 132 है। नई लागत 110 है, इसलिए लाभ 110 की लागत पर 22 है, जो 20 प्रतिशत है। "
  "22 प्रतिशत, 32 प्रतिशत के लाभ में से 10 प्रतिशत की वृद्धि घटाता है, यह भूलते हुए कि लाभ अब बड़ी लागत पर मापा जाता है; 21.2 और 29 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-a-cost-rise-that-eats-a-margin", _pp3,
  opts_hi=["20 प्रतिशत", "21.2 प्रतिशत", "22 प्रतिशत", "29 प्रतिशत"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    s = [1]
    for k in range(1, 6):
        s.append(s[-1] + k * k)
    assert s[:5] == [1, 2, 6, 15, 31]
    return str(s[5])
N(QA, "Sequences & Series", "medium",
  "What is the next number in the series 1, 2, 6, 15, 31, ...?",
  "श्रेणी 1, 2, 6, 15, 31, ... की अगली संख्या क्या है?",
  ["56", "57", "62", "63"], 0,
  "The differences are 1, 4, 9, 16 -- the squares of 1, 2, 3, 4 -- so the next difference is 5² = 25 and the next number 31 + 25 = 56. "
  "63 = 2 × 31 + 1 follows a doubling rule that does not fit the earlier terms (2 × 2 + 1 = 5, not 6); 57 and 62 do not follow from the differences.",
  "अंतर 1, 4, 9, 16 हैं -- 1, 2, 3, 4 के वर्ग -- इसलिए अगला अंतर 5² = 25 और अगली संख्या 31 + 25 = 56 है। "
  "63 = 2 × 31 + 1 दोगुना करने वाले नियम पर चलता है जो पहले के पदों पर नहीं बैठता (2 × 2 + 1 = 5, 6 नहीं); 57 और 62 अंतरों से नहीं निकलते।",
  "qa-ss-differences-that-are-squares", _ss1)

def _ss2():
    tri = [k * (k + 1) // 2 for k in range(1, 11)]
    assert sum(tri) == 10 * 11 * 12 // 6
    return str(sum(tri))
N(QA, "Sequences & Series", "hard",
  "What is the sum of the first ten terms of the series 1, 3, 6, 10, 15, ..., in which each term is the sum of the natural numbers up to its position?",
  "श्रेणी 1, 3, 6, 10, 15, ... के पहले दस पदों का योग क्या है, जिसमें हर पद अपने स्थान तक की प्राकृत संख्याओं का योग है?",
  ["220", "286", "330", "385"], 0,
  "The terms are k(k + 1)/2 for k = 1 to 10: 1, 3, 6, 10, 15, 21, 28, 36, 45 and 55, which add up to 220. (In general the first n such terms add up to n(n + 1)(n + 2)/6 = 10 × 11 × 12 ÷ 6 = 220.) "
  "385 is the sum of the first ten squares; 286 is the sum of the first eleven terms; 330 adds the eleventh term twice.",
  "पद k = 1 से 10 के लिए k(k + 1)/2 हैं: 1, 3, 6, 10, 15, 21, 28, 36, 45 और 55, जिनका योग 220 है। (सामान्यतः ऐसे पहले n पदों का योग n(n + 1)(n + 2)/6 = 10 × 11 × 12 ÷ 6 = 220 है।) "
  "385 पहले दस वर्गों का योग है; 286 पहले ग्यारह पदों का योग है; 330 ग्यारहवाँ पद दो बार जोड़ता है।",
  "qa-ss-the-sum-of-triangular-numbers", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    p = F(sum(1 for t in product("HT", repeat=5) if t.count("H") == 3), 32)
    assert p == F(5, 16)
    return "5/16"
N(QA, "Permutation & Combination", "medium",
  "A fair coin is tossed five times. What is the probability of getting exactly three heads?",
  "एक निष्पक्ष सिक्का पाँच बार उछाला जाता है। ठीक तीन चित आने की प्रायिकता क्या है?",
  ["1/32", "1/16", "3/16", "5/16"], 3,
  "There are 2⁵ = 32 equally likely sequences, and the three heads can fall in any 3 of the 5 tosses: 5C3 = 10 sequences. The probability is 10/32 = 5/16. "
  "1/32 is the chance of one particular sequence, such as HHHTT; 1/16 and 3/16 do not count the positions of the heads.",
  "कुल 2⁵ = 32 समान रूप से संभावित क्रम हैं, और तीन चित पाँच में से किन्हीं 3 उछालों में आ सकते हैं: 5C3 = 10 क्रम। प्रायिकता 10/32 = 5/16 है। "
  "1/32 किसी एक विशेष क्रम, जैसे HHHTT, की प्रायिकता है; 1/16 और 3/16 चितों के स्थानों को नहीं गिनते।",
  "qa-pc-exactly-three-heads-in-five-tosses", _pc1)

def _pc2():
    ways = [(a, b, 8 - a - b) for a in range(9) for b in range(9) if 8 - a - b >= 0 and min(a, b, 8 - a - b) >= 2]
    assert len(ways) == 6
    return str(len(ways))
N(QA, "Permutation & Combination", "hard",
  "In how many ways can 8 identical sweets be shared among 3 children so that each child gets at least 2 sweets?",
  "8 एक जैसी मिठाइयाँ 3 बच्चों में कितने तरीक़ों से बाँटी जा सकती हैं कि हर बच्चे को कम से कम 2 मिठाइयाँ मिलें?",
  ["2", "3", "5", "6"], 3,
  "Give each child 2 sweets first; 2 sweets are left to share freely among the 3 children. They can both go to one child (3 ways) or to two different children (3 ways): 6 in all, as the shares (4, 2, 2), (2, 4, 2), (2, 2, 4), (3, 3, 2), (3, 2, 3) and (2, 3, 3) show. "
  "3 counts only the ways in which one child gets both of the extra sweets; 2 and 5 miss some of the splits.",
  "पहले हर बच्चे को 2 मिठाइयाँ दीजिए; बची 2 मिठाइयाँ 3 बच्चों में स्वतंत्र रूप से बाँटनी हैं। वे दोनों एक बच्चे को जा सकती हैं (3 तरीक़े) या दो अलग बच्चों को (3 तरीक़े): कुल 6, जैसा हिस्से (4, 2, 2), (2, 4, 2), (2, 2, 4), (3, 3, 2), (3, 2, 3) और (2, 3, 3) दिखाते हैं। "
  "3 केवल वे तरीक़े गिनता है जिनमें एक बच्चे को दोनों अतिरिक्त मिठाइयाँ मिलें; 2 और 5 कुछ बँटवारे छोड़ देते हैं।",
  "qa-pc-sweets-with-at-least-two-each", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    litres = 10000 * F(2, 100) * 1000          # m² × m × litres per m³
    assert litres == 200000
    return "2,00,000 litres"
N(QA, "Geometry & Mensuration", "medium",
  "2 cm of rain falls on a field of 1 hectare. What volume of water falls on the field?",
  "1 हेक्टेयर के एक खेत पर 2 सेमी वर्षा होती है। खेत पर कितने आयतन का पानी गिरता है?",
  ["2,000 litres", "20,000 litres", "2,00,000 litres", "20,00,000 litres"], 2,
  "1 hectare = 10,000 m² and 2 cm = 0.02 m, so the volume is 10,000 × 0.02 = 200 m³. Since 1 m³ holds 1,000 litres, that is 2,00,000 litres. "
  "20,000 and 2,000 litres slip a power of 10 in the conversion; 20,00,000 litres takes 2 cm as 0.2 m.",
  "1 हेक्टेयर = 10,000 वर्ग मीटर और 2 सेमी = 0.02 मीटर, इसलिए आयतन 10,000 × 0.02 = 200 घन मीटर है। चूँकि 1 घन मीटर में 1,000 लीटर आते हैं, यह 2,00,000 लीटर है। "
  "20,000 और 2,000 लीटर रूपांतरण में 10 की घात चूकते हैं; 20,00,000 लीटर, 2 सेमी को 0.2 मीटर मान लेता है।",
  "qa-gm-rain-on-a-hectare", _gm1,
  opts_hi=["2,000 लीटर", "20,000 लीटर", "2,00,000 लीटर", "20,00,000 लीटर"])

def _gm2():
    lines, circle_pts = 5 * 4 // 2, 5 * 2
    return str(lines + circle_pts)
N(QA, "Geometry & Mensuration", "hard",
  "What is the greatest possible number of points at which five straight lines and one circle can intersect, counting both points where two lines cross and points where a line cuts the circle?",
  "पाँच सीधी रेखाएँ और एक वृत्त अधिक से अधिक कितने बिंदुओं पर प्रतिच्छेद कर सकते हैं, जिनमें वे बिंदु भी गिने जाएँ जहाँ दो रेखाएँ काटती हैं और वे भी जहाँ कोई रेखा वृत्त को काटती है?",
  ["10", "15", "18", "20"], 3,
  "Two lines meet at most once, so five lines give at most 5C2 = 10 crossings, if no two are parallel and no three pass through one point. A line cuts a circle at most twice, so the five lines give at most 5 × 2 = 10 more points. Arranged so that all these points are different, the total is 10 + 10 = 20. "
  "10 counts only the crossings of the lines (or only the points on the circle); 15 treats the circle as a sixth line (6C2 = 15); 18 has no basis.",
  "दो रेखाएँ अधिक से अधिक एक बार मिलती हैं, इसलिए पाँच रेखाएँ अधिकतम 5C2 = 10 प्रतिच्छेद देती हैं, यदि कोई दो समांतर न हों और कोई तीन एक बिंदु से न गुज़रें। एक रेखा वृत्त को अधिकतम दो बार काटती है, इसलिए पाँचों रेखाएँ अधिकतम 5 × 2 = 10 और बिंदु देती हैं। ऐसे रखने पर कि ये सब बिंदु अलग हों, कुल 10 + 10 = 20 हैं। "
  "10 केवल रेखाओं के प्रतिच्छेद (या केवल वृत्त पर के बिंदु) गिनता है; 15 वृत्त को छठी रेखा मानता है (6C2 = 15); 18 का कोई आधार नहीं।",
  "qa-gm-five-lines-and-a-circle", _gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    stages = (4, 6, 3)
    steady = 480 // max(stages)
    assert steady == 80 and 480 // sum(stages) == 36
    return str(steady)
N(QA, "Time & Work", "hard",
  "Every article made in a workshop passes through three machines in turn, which take 4, 6 and 3 minutes respectively for each article; each machine handles one article at a time and passes it on as soon as it is done. Once the line is running steadily, how many finished articles leave it in an 8-hour shift?",
  "एक कारख़ाने में बनी हर वस्तु क्रम से तीन मशीनों से गुज़रती है, जो हर वस्तु के लिए क्रमशः 4, 6 और 3 मिनट लेती हैं; हर मशीन एक बार में एक वस्तु सँभालती है और काम होते ही उसे आगे बढ़ा देती है। जब यह पंक्ति स्थिर रूप से चल रही हो, तो 8 घंटे की पाली में कितनी तैयार वस्तुएँ निकलती हैं?",
  ["36", "80", "120", "160"], 1,
  "With all three machines working at once on different articles, the line can go no faster than its slowest machine, which finishes one article every 6 minutes. In 480 minutes that is 480 ÷ 6 = 80 articles. "
  "36 = 480 ÷ 13 treats each article as passing through all three machines before the next one starts; 120 and 160 are the rates of the 4-minute and 3-minute machines, which the 6-minute machine holds back.",
  "तीनों मशीनें एक साथ अलग-अलग वस्तुओं पर काम करती हैं, इसलिए पंक्ति अपनी सबसे धीमी मशीन से तेज़ नहीं चल सकती, जो हर 6 मिनट में एक वस्तु पूरी करती है। 480 मिनट में यह 480 ÷ 6 = 80 वस्तुएँ हैं। "
  "36 = 480 ÷ 13 मानता है कि अगली वस्तु शुरू होने से पहले हर वस्तु तीनों मशीनों से गुज़र जाती है; 120 और 160, 4 मिनट और 3 मिनट वाली मशीनों की दरें हैं, जिन्हें 6 मिनट वाली मशीन रोक देती है।",
  "qa-tw-a-line-held-back-by-its-slowest-machine", _tw1)

def _tw2():
    active = 120 - 2 * 10
    assert active == 100
    return f"{active * 120 // 5:,}"
N(QA, "Time & Work", "medium",
  "A machine fills 120 bottles every 5 minutes. It is run for 2 hours, but in each hour it is stopped for 10 minutes for cleaning. How many bottles does it fill in the 2 hours?",
  "एक मशीन हर 5 मिनट में 120 बोतलें भरती है। उसे 2 घंटे चलाया जाता है, पर हर घंटे में सफ़ाई के लिए 10 मिनट रोका जाता है। 2 घंटों में वह कितनी बोतलें भरती है?",
  ["2,400", "2,640", "2,880", "3,000"], 0,
  "The machine fills 120 ÷ 5 = 24 bottles a minute. In 2 hours it runs for 120 - 2 × 10 = 100 minutes, so it fills 24 × 100 = 2,400 bottles. "
  "2,880 ignores the stops; 2,640 allows for only one of them; 3,000 has no basis.",
  "मशीन प्रति मिनट 120 ÷ 5 = 24 बोतलें भरती है। 2 घंटों में वह 120 - 2 × 10 = 100 मिनट चलती है, इसलिए 24 × 100 = 2,400 बोतलें भरती है। "
  "2,880 ठहरावों को अनदेखा करता है; 2,640 उनमें से केवल एक का ध्यान रखता है; 3,000 का कोई आधार नहीं।",
  "qa-tw-a-filler-that-stops-every-hour", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    makeable = {3 * a + 5 * b for a in range(40) for b in range(40)}
    gaps = [n for n in range(1, 60) if n not in makeable]
    assert gaps == [1, 2, 4, 7]
    return str(max(gaps))
N(QA, "Puzzle Hybrid", "hard",
  "Postage stamps are available only in values of ₹3 and ₹5, and any number of each may be used. What is the largest whole-rupee amount that cannot be made up exactly with these stamps?",
  "डाक टिकट केवल ₹3 और ₹5 के मूल्यों में उपलब्ध हैं, और हर एक कितने भी प्रयोग किए जा सकते हैं। वह सबसे बड़ी पूर्ण-रुपया राशि कौन-सी है जो इन टिकटों से ठीक-ठीक नहीं बनाई जा सकती?",
  ["1", "2", "4", "7"], 3,
  "₹8 = 3 + 5, ₹9 = 3 + 3 + 3 and ₹10 = 5 + 5 can all be made, and from three amounts in a row every larger amount follows by adding ₹3 stamps. Below 8, the amounts that cannot be made are ₹1, ₹2, ₹4 and ₹7 (7 is neither a multiple of 3 nor 5 plus a multiple of 3), so the largest is ₹7. "
  "₹1, ₹2 and ₹4 also cannot be made, but they are not the largest such amount.",
  "₹8 = 3 + 5, ₹9 = 3 + 3 + 3 और ₹10 = 5 + 5 सब बनाई जा सकती हैं, और लगातार तीन राशियों से आगे हर बड़ी राशि ₹3 के टिकट जोड़कर बनती है। 8 से नीचे जो राशियाँ नहीं बनतीं वे ₹1, ₹2, ₹4 और ₹7 हैं (7 न 3 का गुणज है न 5 जोड़ 3 का गुणज), इसलिए सबसे बड़ी ₹7 है। "
  "₹1, ₹2 और ₹4 भी नहीं बनतीं, पर वे सबसे बड़ी ऐसी राशि नहीं हैं।",
  "qa-ph-the-largest-amount-two-stamps-cannot-make", _ph1,
  opts_hi=["₹1", "₹2", "₹4", "₹7"])

def _ph2():
    ns = [n for n in range(5, 200) if F(4800, n - 4) - F(4800, n) == 40]
    assert ns == [24]
    return str(ns[0])
N(QA, "Puzzle Hybrid", "medium",
  "A group hires a bus for ₹4,800, the cost to be shared equally. When 4 people drop out, each of the others has to pay ₹40 more. How many people were in the group at first?",
  "एक समूह ₹4,800 में एक बस किराए पर लेता है, लागत बराबर बाँटी जानी है। जब 4 लोग हट जाते हैं, तो बाक़ी हर एक को ₹40 अधिक देने पड़ते हैं। आरंभ में समूह में कितने लोग थे?",
  ["16", "20", "24", "30"], 2,
  "With n people each pays 4,800/n; with n - 4 people each pays 4,800/(n - 4). The difference is 40: 4,800 × 4 = 40n(n - 4), so n(n - 4) = 480 and n = 24 (each paid ₹200 and then ₹240). "
  "20 is the number who remain; 16 and 30 do not give a ₹40 difference.",
  "n लोगों में हर एक 4,800/n देता है; n - 4 लोगों में हर एक 4,800/(n - 4)। अंतर 40 है: 4,800 × 4 = 40n(n - 4), अतः n(n - 4) = 480 और n = 24 (हर एक ने पहले ₹200 और फिर ₹240 दिए)। "
  "20 बचे हुए लोगों की संख्या है; 16 और 30 से ₹40 का अंतर नहीं आता।",
  "qa-ph-a-bus-fare-shared-by-fewer-people", _ph2)

def _ph3():
    cuts_per_axis = 2                            # two cuts split one direction into three; pieces in the middle need both
    total = 3 * cuts_per_axis
    assert total == 6
    return "6"
N(QA, "Puzzle Hybrid", "medium",
  "A wooden cube is to be cut into 27 equal smaller cubes. What is the least number of straight cuts needed, if the pieces may be rearranged between cuts?",
  "लकड़ी के एक घन को 27 बराबर छोटे घनों में काटना है। यदि कटों के बीच टुकड़ों को फिर से व्यवस्थित किया जा सकता हो, तो कम से कम कितने सीधे कट चाहिए?",
  ["6", "8", "9", "26"], 0,
  "Two cuts in each of the three directions do the job, 6 in all. Rearranging cannot save a cut: the small cube at the very centre has six faces, every one of them inside the big cube at the start, and a single straight cut can expose at most one face of it. So at least 6 cuts are needed. "
  "26 is the number of small cubes other than the centre one; 9 and 8 have no basis once each direction needs only two cuts.",
  "तीनों दिशाओं में से हर एक में दो कट काम कर देते हैं, कुल 6। पुनर्व्यवस्था से कोई कट नहीं बचता: ठीक बीच वाले छोटे घन के छह फलक हैं, जो आरंभ में सभी बड़े घन के भीतर हैं, और एक सीधा कट उसका अधिक से अधिक एक फलक खोल सकता है। अतः कम से कम 6 कट चाहिए। "
  "26 बीच वाले के अलावा छोटे घनों की संख्या है; जब हर दिशा में केवल दो कट चाहिए तो 9 और 8 का कोई आधार नहीं।",
  "qa-ph-the-cuts-that-make-27-cubes", _ph3)

def _ph4():
    n = sum(1 for h in range(24) for m in range(60) if "1" in f"{h:02d}{m:02d}")
    assert n == 1440 - 12 * 45
    return str(n)
N(QA, "Puzzle Hybrid", "hard",
  "A digital clock shows hours and minutes from 00:00 to 23:59. For how many minutes in a day does the display show the digit 1 at least once?",
  "एक डिजिटल घड़ी 00:00 से 23:59 तक घंटे और मिनट दिखाती है। एक दिन में कितने मिनटों तक प्रदर्शन में अंक 1 कम से कम एक बार दिखाई देता है?",
  ["540", "720", "900", "960"], 2,
  "Count the minutes with no 1 at all. Hours without a 1: 00 and 02 to 09 (9 of them) and 20, 22, 23 (3 more) -- 12 in all. Minutes without a 1: the tens digit can be 0, 2, 3, 4 or 5, and the units digit any of 0 and 2 to 9 -- 5 × 9 = 45. "
  "So 12 × 45 = 540 minutes show no 1, and 1,440 - 540 = 900 show at least one. 540 is the count without a 1; 720 is half the day; 960 has no basis.",
  "उन मिनटों को गिनिए जिनमें 1 बिलकुल नहीं है। 1 के बिना घंटे: 00 और 02 से 09 (9) तथा 20, 22, 23 (3 और) -- कुल 12। 1 के बिना मिनट: दहाई का अंक 0, 2, 3, 4 या 5 हो सकता है, और इकाई का 0 तथा 2 से 9 में से कोई -- 5 × 9 = 45। "
  "अतः 12 × 45 = 540 मिनटों में कोई 1 नहीं दिखता, और 1,440 - 540 = 900 में कम से कम एक। 540 बिना 1 वाली गिनती है; 720 दिन का आधा है; 960 का कोई आधार नहीं।",
  "qa-ph-the-digit-1-on-a-24-hour-clock", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    primes = [p for p in range(10, 100) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    squares = {k * k for k in range(1, 8) if k * k < 50}
    s1 = set(primes)
    s2 = {n for n in range(1, 100) if n + 2 in squares}
    both = s1 & s2
    assert both == {23, 47}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the value of the natural number n?",
   "प्राकृत संख्या n का मान क्या है?",
   "n is a two-digit prime number.", "n दो अंकों की एक अभाज्य संख्या है।",
   "n + 2 is a perfect square less than 50.", "n + 2, 50 से छोटा एक पूर्ण वर्ग है।",
   3,
   "Statement I allows any two-digit prime. Statement II allows n = 2, 7, 14, 23, 34 or 47 (n + 2 = 4, 9, 16, 25, 36 or 49). Together they still leave two values, 23 and 47, so n cannot be fixed. "
   "The question cannot be answered even with both statements.",
   "कथन I दो अंकों की किसी भी अभाज्य संख्या की अनुमति देता है। कथन II n = 2, 7, 14, 23, 34 या 47 की अनुमति देता है (n + 2 = 4, 9, 16, 25, 36 या 49)। दोनों साथ भी दो मान, 23 और 47, छोड़ते हैं, इसलिए n तय नहीं होता। "
   "दोनों कथनों के साथ भी प्रश्न का उत्तर नहीं दिया जा सकता।",
   "qa-ds-a-prime-two-less-than-a-square", _ds1)

def _ds2():
    prices = [(x, y) for x in range(1, 50) for y in range(1, 50)]
    s1 = {5 * x + 5 * y for x, y in prices if 3 * x + 2 * y == 50}
    s2 = {5 * x + 5 * y for x, y in prices if 2 * x + 3 * y == 40}
    both = {5 * x + 5 * y for x, y in prices if 3 * x + 2 * y == 50 and 2 * x + 3 * y == 40}
    assert both == {90} and len(s1) > 1 and len(s2) > 1
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the total cost of 5 pens and 5 pencils, each pen costing the same and each pencil costing the same?",
   "5 क़लमों और 5 पेंसिलों की कुल लागत क्या है, जहाँ हर क़लम का मूल्य समान है और हर पेंसिल का भी?",
   "3 pens and 2 pencils cost ₹50.", "3 क़लमें और 2 पेंसिलें ₹50 की हैं।",
   "2 pens and 3 pencils cost ₹40.", "2 क़लमें और 3 पेंसिलें ₹40 की हैं।",
   2,
   "Neither statement alone fixes the prices. Together, adding the two gives 5 pens and 5 pencils for 50 + 40 = ₹90 -- the question is answered without finding either price (which are ₹14 and ₹4). Both statements are needed.",
   "कोई भी कथन अकेला मूल्य तय नहीं करता। दोनों साथ: दोनों को जोड़ने पर 5 क़लमें और 5 पेंसिलें 50 + 40 = ₹90 की होती हैं -- प्रश्न का उत्तर किसी मूल्य को निकाले बिना मिल जाता है (जो ₹14 और ₹4 हैं)। दोनों कथन ज़रूरी हैं।",
   "qa-ds-pens-and-pencils-added-together", _ds2)
