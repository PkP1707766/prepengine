# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 4 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Same mix as Tests 1-3 (playbook B.7) with none of their question shapes: the test for 11, the least number to
add, primes between 50 and 100, 5a3b divisible by 36, a product from a sum and a sum of squares, the 100th digit
of 1/7, x dividing x² + 12, a remainder of 2 that is also a multiple of 7, times from a speed ratio, trains with a
staggered start, '15 km/h faster, an hour less', the hands of a clock meeting, shares in 5 : 2 : 4 : 3, a family's
average before a birth, a ratio after taking 9 from each, salaries after a rise and a fall, men-length-days,
profit as a share of price and of cost, compound less simple interest over three years, a car bought cheaper and
sold dearer, a sequence where n appears n times, the terms needed for a sum, three-digit numbers from 0-4, girls
kept apart, a path inside a field, a cylinder's volume, twice as efficient, man-hours, nine coins on a balance, a
frog in a well, passengers counted backwards, and a clock's strikes in a day. The build spreads the topics
through the paper (csat_common.interleave). Difficulty 3 easy / 19 medium / 12 hard; every key is worked out in
code by check()."""
import math
from fractions import Fraction as F
from itertools import permutations
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
    opts = ["2063", "4361", "5609", "6457"]
    return _only(o for o in opts if int(o) % 11 == 0)
N(QA, "Number Theory", "easy",
  "Which one of the following numbers is divisible by 11?",
  "निम्नलिखित संख्याओं में से कौन-सी 11 से विभाज्य है?",
  ["2063", "4361", "5609", "6457"], 3,
  "A number is divisible by 11 when the alternating sum of its digits is 0 or a multiple of 11: 6 - 4 + 5 - 7 = 0, so 6457 = 11 × 587. "
  "2063 has digits that add up to 11 -- the trap, since a digit sum tests divisibility by 3 or 9, not by 11 (its alternating sum is 5). 4361 and 5609 give alternating sums of 6 and -10.",
  "कोई संख्या 11 से तब विभाज्य होती है जब उसके अंकों का एकांतर योग 0 या 11 का गुणज हो: 6 - 4 + 5 - 7 = 0, अतः 6457 = 11 × 587। "
  "2063 के अंकों का योग 11 है -- यही जाल है, क्योंकि अंकों का योग 3 या 9 से विभाज्यता जाँचता है, 11 से नहीं (उसका एकांतर योग 5 है)। 4361 और 5609 के एकांतर योग 6 और -10 हैं।",
  "qa-nt-test-for-eleven", _nt1)

N(QA, "Number Theory", "medium",
  "What is the least number that must be added to 1000 to make the sum exactly divisible by 45?",
  "1000 में कम से कम कौन-सी संख्या जोड़ी जाए कि योग 45 से पूर्णतः विभाज्य हो जाए?",
  ["10", "35", "45", "55"], 1,
  "1000 = 45 × 22 + 10, so 1000 is 10 more than a multiple of 45 and 35 short of the next one, 45 × 23 = 1035. The least number to add is 35. "
  "10 is the remainder -- the least number to subtract, not to add; 45 is the divisor itself; 55 adds the remainder to the divisor.",
  "1000 = 45 × 22 + 10, अतः 1000, 45 के एक गुणज से 10 अधिक है और अगले गुणज, 45 × 23 = 1035, से 35 कम। जोड़ी जाने वाली सबसे छोटी संख्या 35 है। "
  "10 शेषफल है -- घटाई जाने वाली सबसे छोटी संख्या, जोड़ी जाने वाली नहीं; 45 स्वयं भाजक है; 55 शेषफल को भाजक में जोड़ देता है।",
  "qa-nt-least-number-to-add", lambda: str(next(k for k in range(0, 100) if (1000 + k) % 45 == 0)))

def _nt3():
    primes = [n for n in range(51, 100) if all(n % d for d in range(2, math.isqrt(n) + 1))]
    assert 91 not in primes and 51 not in primes and 57 not in primes
    return str(len(primes))
N(QA, "Number Theory", "medium",
  "How many prime numbers are there between 50 and 100?",
  "50 और 100 के बीच कितनी अभाज्य संख्याएँ हैं?",
  ["10", "11", "12", "13"], 0,
  "The primes between 50 and 100 are 53, 59, 61, 67, 71, 73, 79, 83, 89 and 97: ten. The usual slips are numbers that look prime but are not: "
  "counting 91 = 7 × 13 gives 11, adding 51 = 3 × 17 gives 12, and adding 57 = 3 × 19 as well gives 13.",
  "50 और 100 के बीच की अभाज्य संख्याएँ 53, 59, 61, 67, 71, 73, 79, 83, 89 और 97 हैं: दस। सामान्य भूलें वे संख्याएँ हैं जो अभाज्य लगती हैं पर हैं नहीं: "
  "91 = 7 × 13 को गिनने पर 11, उसके साथ 51 = 3 × 17 को भी गिनने पर 12, और 57 = 3 × 19 को भी गिनने पर 13 आता है।",
  "qa-nt-primes-from-50-to-100", _nt3)

def _nt4():
    num = lambda a, b: int(f"5{a}3{b}")
    pairs = [(a, b) for a in range(10) for b in range(10) if num(a, b) % 36 == 0]
    even = [(a, b) for a in range(10) for b in range(10) if b % 2 == 0 and num(a, b) % 9 == 0]
    last = [(a, b) for a in range(10) for b in range(10) if b % 4 == 0 and num(a, b) % 9 == 0]
    assert sorted(num(a, b) for a, b in pairs) == [5436, 5832] and len(even) == 5 and len(last) == 3
    return str(len(pairs))
N(QA, "Number Theory", "hard",
  "In the four-digit number 5a3b, a and b stand for digits. For how many pairs of digits (a, b) is the number divisible by 36?",
  "चार अंकों की संख्या 5a3b में a और b अंक हैं। अंकों के कितने युग्मों (a, b) के लिए यह संख्या 36 से विभाज्य है?",
  ["1", "2", "3", "5"], 1,
  "36 = 4 × 9, so the number must pass both tests. For 4, the last two digits 3b must form a multiple of 4: only 32 and 36. For 9, the digit sum 8 + a + b must be a multiple of 9, so a + b is 1 or 10: "
  "with b = 2, a = 8 (5832); with b = 6, a = 4 (5436). Two numbers. 5 comes from checking only that the number is even, and 3 from testing the last digit alone for 4 (b = 0, 4 or 8).",
  "36 = 4 × 9, इसलिए संख्या को दोनों जाँचें पार करनी होंगी। 4 के लिए अंतिम दो अंक 3b, 4 का गुणज होने चाहिए: केवल 32 और 36। 9 के लिए अंकों का योग 8 + a + b, 9 का गुणज होना चाहिए, इसलिए a + b, 1 या 10 है: "
  "b = 2 पर a = 8 (5832); b = 6 पर a = 4 (5436)। दो संख्याएँ। 5 केवल यह जाँचने से आता है कि संख्या सम है, और 3, 4 के लिए केवल अंतिम अंक जाँचने से (b = 0, 4 या 8)।",
  "qa-nt-5a3b-divisible-by-36", _nt4)

def _nt5():
    ab = F(22 ** 2 - 404, 2)
    roots = [t for t in range(-50, 51) if t * t - 22 * t + ab == 0]
    assert sorted(roots) == [2, 20]
    return str(ab)
N(QA, "Number Theory", "medium",
  "The sum of two numbers is 22 and the sum of their squares is 404. What is their product?",
  "दो संख्याओं का योग 22 और उनके वर्गों का योग 404 है। उनका गुणनफल क्या है?",
  ["40", "80", "202", "242"], 0,
  "(a + b)² = a² + b² + 2ab, so 22² = 484 = 404 + 2ab and ab = 40 (the numbers are 20 and 2). "
  "80 is 2ab, from forgetting to halve; 202 halves the sum of the squares; 242 halves the square of the sum.",
  "(a + b)² = a² + b² + 2ab, अतः 22² = 484 = 404 + 2ab और ab = 40 (संख्याएँ 20 और 2 हैं)। "
  "80, 2ab है, आधा करना भूलने से; 202 वर्गों के योग का आधा है; 242 योग के वर्ग का आधा है।",
  "qa-nt-product-from-sum-and-squares", _nt5)

def _nt6():
    digits, r = [], 1
    for _ in range(100):
        r *= 10
        digits.append(r // 7)
        r %= 7
    return str(digits[99])
N(QA, "Number Theory", "medium",
  "What is the 100th digit after the decimal point when 1/7 is written as a decimal?",
  "1/7 को दशमलव रूप में लिखने पर दशमलव बिंदु के बाद 100वाँ अंक क्या है?",
  ["1", "4", "5", "8"], 3,
  "1/7 = 0.142857 142857 ..., a block of six digits that repeats. 100 = 6 × 16 + 4, so the 100th digit is the 4th digit of the block: 8. "
  "4 takes the remainder 4 itself as the digit; 5 counts the block from zero and lands one place too late; 1 assumes that the 100th digit begins a new block.",
  "1/7 = 0.142857 142857 ..., छह अंकों का एक खंड जो दोहराता है। 100 = 6 × 16 + 4, इसलिए 100वाँ अंक खंड का चौथा अंक है: 8। "
  "4 शेषफल 4 को ही अंक मान लेता है; 5 खंड की गिनती शून्य से करता है और एक स्थान आगे पहुँच जाता है; 1 मान लेता है कि 100वाँ अंक नया खंड शुरू करता है।",
  "qa-nt-100th-digit-of-one-seventh", _nt6)

N(QA, "Number Theory", "hard",
  "For how many positive integers x is x² + 12 divisible by x?",
  "कितने धनात्मक पूर्णांकों x के लिए x² + 12, x से विभाज्य है?",
  ["2", "6", "12", "Infinitely many"], 1,
  "x always divides x², so x divides x² + 12 exactly when it divides 12: x = 1, 2, 3, 4, 6 or 12 -- six values. "
  "'Infinitely many' forgets the 12; 12 counts every number up to 12; 2 counts only the primes 2 and 3.",
  "x सदा x² को विभाजित करता है, इसलिए x, x² + 12 को ठीक तब विभाजित करता है जब वह 12 को विभाजित करे: x = 1, 2, 3, 4, 6 या 12 -- छह मान। "
  "'अनगिनत' 12 को भूल जाता है; 12, 12 तक की हर संख्या गिनता है; 2 केवल अभाज्य संख्याएँ 2 और 3 गिनता है।",
  "qa-nt-x-divides-x-squared-plus-12", lambda: str(sum(1 for x in range(1, 2000) if (x * x + 12) % x == 0)),
  opts_hi=["2", "6", "12", "अनगिनत"])

def _nt8():
    found = next(n for n in range(1, 2000) if all(n % d == 2 for d in (3, 4, 5, 6)) and n % 7 == 0)
    assert 242 % 7 and 62 % 7 and 122 % 7
    return str(found)
N(QA, "Number Theory", "hard",
  "What is the smallest number that leaves a remainder of 2 when divided by 3, 4, 5 or 6, and is exactly divisible by 7?",
  "वह सबसे छोटी संख्या कौन-सी है जो 3, 4, 5 या 6 से भाग देने पर 2 शेषफल छोड़ती है, और 7 से पूर्णतः विभाज्य है?",
  ["62", "122", "182", "242"], 2,
  "Numbers that leave remainder 2 on division by 3, 4, 5 and 6 are 2 more than a multiple of their LCM, 60: 62, 122, 182, 242, .... Testing them for 7, 62 and 122 leave remainders 6 and 3, "
  "while 182 = 7 × 26. 62 is the smallest number with the four remainders but is not a multiple of 7; 242, the next in the list, is not a multiple of 7 either.",
  "जो संख्याएँ 3, 4, 5 और 6 से भाग देने पर 2 शेषफल छोड़ती हैं, वे उनके LCM 60 के किसी गुणज से 2 अधिक होती हैं: 62, 122, 182, 242, ...। इन्हें 7 से जाँचने पर 62 और 122, 6 और 3 शेषफल छोड़ती हैं, "
  "जबकि 182 = 7 × 26। 62 चारों शेषफल वाली सबसे छोटी संख्या है पर 7 का गुणज नहीं; सूची की अगली संख्या 242 भी 7 का गुणज नहीं है।",
  "qa-nt-remainder-two-and-multiple-of-7", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    part = F(30, 4 - 3)                     # times are in the ratio 4 : 3
    return f"{4 * part} minutes"
N(QA, "Speed-Distance-Time", "easy",
  "The speeds of A and B are in the ratio 3 : 4. A takes 30 minutes more than B to cover the same distance. How long does A take?",
  "A और B की चालों का अनुपात 3 : 4 है। एक ही दूरी तय करने में A, B से 30 मिनट अधिक लेता है। A कितना समय लेता है?",
  ["22½ minutes", "40 minutes", "90 minutes", "120 minutes"], 3,
  "For a fixed distance, time varies inversely as speed, so the times are in the ratio 4 : 3. The difference, one part, is 30 minutes, so A takes 4 × 30 = 120 minutes and B 90. "
  "90 minutes is B's time; 40 and 22½ minutes apply the speed ratio, 4/3 or 3/4, to the 30-minute difference instead of to the times.",
  "निश्चित दूरी के लिए समय चाल के व्युत्क्रमानुपाती होता है, इसलिए समयों का अनुपात 4 : 3 है। अंतर, यानी एक भाग, 30 मिनट है, इसलिए A, 4 × 30 = 120 मिनट और B, 90 मिनट लेता है। "
  "90 मिनट B का समय है; 40 और 22½ मिनट चालों का अनुपात, 4/3 या 3/4, समयों के बजाय 30 मिनट के अंतर पर लगा देते हैं।",
  "qa-sdt-times-from-speed-ratio", _sdt1,
  opts_hi=["22½ मिनट", "40 मिनट", "90 मिनट", "120 मिनट"])

def _sdt2():
    after_eight = F(450 - 60, 60 + 90)      # hours after 8 a.m.
    minutes = 8 * 60 + after_eight * 60
    assert minutes.denominator == 1
    h, m = divmod(int(minutes), 60)
    return f"{h}:{m:02d} a.m."
N(QA, "Speed-Distance-Time", "medium",
  "Two stations, A and B, are 450 km apart. A train leaves A for B at 7 a.m., running at 60 km/h, and another leaves B for A at 8 a.m., running at 90 km/h. At what time do they meet?",
  "दो स्टेशन, A और B, 450 किमी दूर हैं। एक रेलगाड़ी सुबह 7 बजे A से B के लिए 60 किमी/घंटा की चाल से चलती है, और दूसरी सुबह 8 बजे B से A के लिए 90 किमी/घंटा की चाल से। वे किस समय मिलेंगी?",
  ["10:00 a.m.", "10:24 a.m.", "10:36 a.m.", "11:00 a.m."], 2,
  "By 8 a.m. the first train has run 60 km, leaving 390 km between them. From then on they close the gap at 60 + 90 = 150 km/h, so they meet 390/150 = 2.6 hours, or 2 hours 36 minutes, later: at 10:36 a.m. "
  "10:00 a.m. starts both trains at 7; 11:00 a.m. starts both at 8, ignoring the first train's hour; 10:24 a.m. takes away the second train's 90 km instead of the first train's 60.",
  "सुबह 8 बजे तक पहली रेलगाड़ी 60 किमी चल चुकी है, जिससे उनके बीच 390 किमी बचते हैं। उसके बाद वे 60 + 90 = 150 किमी/घंटा से दूरी घटाती हैं, इसलिए 390/150 = 2.6 घंटे, यानी 2 घंटे 36 मिनट, बाद मिलती हैं: सुबह 10:36 बजे। "
  "10:00 बजे दोनों रेलगाड़ियों को 7 बजे चला देता है; 11:00 बजे दोनों को 8 बजे चलाता है और पहली रेलगाड़ी का एक घंटा भूल जाता है; 10:24 बजे पहली रेलगाड़ी के 60 किमी के बजाय दूसरी के 90 किमी घटाता है।",
  "qa-sdt-trains-with-staggered-start", _sdt2,
  opts_hi=["सुबह 10:00 बजे", "सुबह 10:24 बजे", "सुबह 10:36 बजे", "सुबह 11:00 बजे"])

def _sdt3():
    d = 1 / (F(1, 60) - F(1, 75))
    return f"{d} km"
N(QA, "Speed-Distance-Time", "medium",
  "A car covers a certain distance at 60 km/h. Had it gone 15 km/h faster, it would have taken 1 hour less. What is the distance?",
  "एक कार कोई दूरी 60 किमी/घंटा की चाल से तय करती है। यदि वह 15 किमी/घंटा तेज़ चलती, तो उसे 1 घंटा कम लगता। दूरी कितनी है?",
  ["60 km", "75 km", "240 km", "300 km"], 3,
  "The trip takes d/60 hours now and d/75 hours at the higher speed; the difference is one hour, so d(1/60 - 1/75) = d/300 = 1 and d = 300 km (5 hours at 60 km/h, 4 hours at 75). "
  "60 km and 75 km are only what each speed covers in one hour; 240 km pairs the faster trip's 4 hours with the slower speed.",
  "यात्रा में अभी d/60 घंटे लगते हैं और अधिक चाल पर d/75 घंटे; अंतर एक घंटा है, इसलिए d(1/60 - 1/75) = d/300 = 1 और d = 300 किमी (60 किमी/घंटा पर 5 घंटे, 75 पर 4 घंटे)। "
  "60 किमी और 75 किमी केवल वे दूरियाँ हैं जो हर चाल एक घंटे में तय करती है; 240 किमी तेज़ यात्रा के 4 घंटों को धीमी चाल से गुणा कर देता है।",
  "qa-sdt-faster-by-15-an-hour-less", _sdt3,
  opts_hi=["60 किमी", "75 किमी", "240 किमी", "300 किमी"])

def _sdt4():
    t = F(120) / (6 - F(1, 2))             # minutes after 4:00
    assert t == F(240, 11) and F(120, 5) == 24
    whole = t.numerator // t.denominator
    rest = t - whole
    return f"{whole} {rest.numerator}/{rest.denominator} minutes past 4"
N(QA, "Speed-Distance-Time", "hard",
  "At what time between 4 o'clock and 5 o'clock are the hour hand and the minute hand of a clock exactly together?",
  "4 बजे और 5 बजे के बीच किस समय घड़ी की घंटे की सुई और मिनट की सुई ठीक एक साथ होती हैं?",
  ["20 minutes past 4", "21 9/11 minutes past 4", "22 minutes past 4", "24 minutes past 4"], 1,
  "At 4:00 the hour hand is 120° ahead of the minute hand. The minute hand turns 6° a minute and the hour hand 0.5°, so the minute hand gains 5.5° a minute and catches up after 120/5.5 = 240/11 = 21 9/11 minutes. "
  "20 minutes assumes that the hour hand stays at 4; 24 minutes takes the gain as 5° a minute; 22 minutes simply rounds.",
  "4:00 बजे घंटे की सुई मिनट की सुई से 120° आगे है। मिनट की सुई एक मिनट में 6° घूमती है और घंटे की सुई 0.5°, इसलिए मिनट की सुई हर मिनट 5.5° आगे बढ़ती है और 120/5.5 = 240/11 = 21 9/11 मिनट में बराबर पहुँच जाती है। "
  "20 मिनट मान लेता है कि घंटे की सुई 4 पर ही रुकी रहती है; 24 मिनट बढ़त को 5° प्रति मिनट मानता है; 22 मिनट केवल पूर्णांकन है।",
  "qa-sdt-clock-hands-meet-after-four", _sdt4,
  opts_hi=["4 बजकर 20 मिनट", "4 बजकर 21 9/11 मिनट", "4 बजकर 22 मिनट", "4 बजकर 24 मिनट"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "A sum of money is divided among A, B, C and D in the ratio 5 : 2 : 4 : 3. If C gets ₹1,000 more than D, what is B's share?",
  "एक धनराशि A, B, C और D में 5 : 2 : 4 : 3 के अनुपात में बाँटी जाती है। यदि C को D से ₹1,000 अधिक मिलते हैं, तो B का हिस्सा क्या है?",
  ["₹2,000", "₹3,000", "₹4,000", "₹5,000"], 0,
  "C and D differ by 4 - 3 = 1 part, so one part is ₹1,000, and B, with 2 parts, gets ₹2,000. ₹3,000 and ₹4,000 are D's and C's shares, and ₹5,000 is A's.",
  "C और D में 4 - 3 = 1 भाग का अंतर है, इसलिए एक भाग ₹1,000 है, और 2 भागों वाले B को ₹2,000 मिलते हैं। ₹3,000 और ₹4,000, D और C के हिस्से हैं, और ₹5,000, A का।",
  "qa-rm-shares-in-5-2-4-3", lambda: f"₹{2 * 1000 // (4 - 3):,}")

def _rm2():
    others_now = 6 * 22 - 7
    then = others_now - 5 * 7
    assert F(6 * 22 - 6 * 7, 6) == 15 and F(others_now, 5) == 25
    return str(F(then, 5))
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "The average age of a family of six is 22 years, and its youngest member is 7 years old. What was the average age of the family just before the youngest member was born?",
  "छह सदस्यों वाले एक परिवार की औसत आयु 22 वर्ष है, और उसका सबसे छोटा सदस्य 7 वर्ष का है। सबसे छोटे सदस्य के जन्म से ठीक पहले परिवार की औसत आयु क्या थी?",
  ["15", "18", "22", "25"], 1,
  "Today the six ages add up to 6 × 22 = 132, and without the youngest the other five add up to 125. Seven years ago each of them was 7 years younger, so their total was 125 - 35 = 90, "
  "and the family of five had an average age of 18. 15 takes 7 years off all six members and divides by 6; 25 drops the youngest but forgets to go back 7 years; 22 is today's average.",
  "आज छहों आयु का योग 6 × 22 = 132 है, और सबसे छोटे को छोड़कर बाक़ी पाँच का योग 125। सात वर्ष पहले उनमें से हर एक 7 वर्ष छोटा था, इसलिए उनका योग 125 - 35 = 90 था, "
  "और पाँच सदस्यों वाले परिवार की औसत आयु 18 थी। 15 छहों सदस्यों से 7 वर्ष घटाकर 6 से भाग देता है; 25 सबसे छोटे को हटाता है पर 7 वर्ष पीछे जाना भूल जाता है; 22 आज का औसत है।",
  "qa-rm-family-average-before-a-birth", _rm2)

def _rm3():
    xs = [x for x in range(1, 100) if F(3 * x - 9, 5 * x - 9) == F(12, 23)]
    return _only(3 * x for x in xs)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Two numbers are in the ratio 3 : 5. If 9 is subtracted from each of them, the ratio becomes 12 : 23. What is the smaller number?",
  "दो संख्याएँ 3 : 5 के अनुपात में हैं। यदि दोनों में से 9 घटा दिया जाए, तो अनुपात 12 : 23 हो जाता है। छोटी संख्या क्या है?",
  ["27", "33", "45", "55"], 1,
  "Let the numbers be 3x and 5x. (3x - 9)/(5x - 9) = 12/23 gives 69x - 207 = 60x - 108, so 9x = 99 and x = 11: the numbers are 33 and 55, and 24 : 46 = 12 : 23. "
  "55 is the larger number; 27 and 45 take 9 as the multiplier x.",
  "संख्याएँ 3x और 5x मानिए। (3x - 9)/(5x - 9) = 12/23 से 69x - 207 = 60x - 108, अतः 9x = 99 और x = 11: संख्याएँ 33 और 55 हैं, और 24 : 46 = 12 : 23। "
  "55 बड़ी संख्या है; 27 और 45, 9 को ही गुणक x मान लेते हैं।",
  "qa-rm-ratio-after-taking-9-from-each", _rm3)

def _rm4():
    r = (4 * F(12, 10)) / (5 * F(9, 10))
    assert (4 * F(12, 10)) / 5 == F(24, 25) and (4 * F(12, 10)) / (5 * F(11, 10)) == F(48, 55)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The salaries of A and B are in the ratio 4 : 5. If A's salary rises by 20% and B's falls by 10%, what is the new ratio of their salaries?",
  "A और B के वेतन 4 : 5 के अनुपात में हैं। यदि A का वेतन 20% बढ़ जाए और B का 10% घट जाए, तो उनके वेतनों का नया अनुपात क्या होगा?",
  ["4 : 5", "48 : 55", "24 : 25", "16 : 15"], 3,
  "Take the salaries as 4 and 5. A's becomes 4 × 1.2 = 4.8 and B's 5 × 0.9 = 4.5, so the new ratio is 4.8 : 4.5 = 16 : 15 -- A now earns more than B. "
  "24 : 25 applies only A's rise; 48 : 55 turns B's 10% fall into a rise; 4 : 5 assumes that the two changes cancel.",
  "वेतन 4 और 5 मानिए। A का वेतन 4 × 1.2 = 4.8 और B का 5 × 0.9 = 4.5 हो जाता है, इसलिए नया अनुपात 4.8 : 4.5 = 16 : 15 है -- अब A, B से अधिक कमाता है। "
  "24 : 25 केवल A की वृद्धि लगाता है; 48 : 55, B की 10% कमी को वृद्धि बना देता है; 4 : 5 मान लेता है कि दोनों बदलाव एक-दूसरे को काट देते हैं।",
  "qa-rm-salaries-after-a-rise-and-a-fall", _rm4)

def _rm5():
    days = 10 * F(60, 40) * F(8, 10)
    assert 10 * F(60, 40) == 15 and 10 * F(8, 10) == 8 and 10 * F(60, 40) * F(10, 8) == F(75, 4)
    return str(days)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "8 men can build a wall 40 m long in 10 days. Working at the same rate, how many days will 10 men take to build a wall 60 m long?",
  "8 पुरुष 40 मीटर लंबी एक दीवार 10 दिनों में बना सकते हैं। उसी दर से काम करते हुए 10 पुरुष 60 मीटर लंबी दीवार कितने दिनों में बनाएँगे?",
  ["8", "12", "15", "18¾"], 1,
  "A wall 1.5 times as long needs 1.5 times the work, and 10 men instead of 8 do it in 8/10 of the time: 10 × 1.5 × 0.8 = 12 days. "
  "15 ignores the extra men; 8 ignores the longer wall; 18¾ turns the ratio of men upside down.",
  "1.5 गुना लंबी दीवार के लिए 1.5 गुना काम चाहिए, और 8 के बजाय 10 पुरुष उसे 8/10 समय में कर लेते हैं: 10 × 1.5 × 0.8 = 12 दिन। "
  "15 अतिरिक्त पुरुषों को भूल जाता है; 8 लंबी दीवार को भूल जाता है; 18¾ पुरुषों का अनुपात उलट देता है।",
  "qa-rm-men-length-and-days", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    sp, profit = F(100), F(20)
    assert profit / (sp + profit) * 100 == F(50, 3)        # the 16⅔% distractor: 20% of cost as a share of price
    return f"{profit / (sp - profit) * 100}%"
N(QA, "Percentage & Profit-Loss", "medium",
  "A trader's profit is 20% of his selling price. What is his profit as a percentage of his cost price?",
  "एक व्यापारी का लाभ उसके विक्रय मूल्य का 20% है। उसका लाभ उसके क्रय मूल्य का कितना प्रतिशत है?",
  ["16⅔%", "20%", "25%", "80%"], 2,
  "Take the selling price as 100: the profit is 20, so the cost is 80, and the profit is 20/80 = 25% of the cost. "
  "20% repeats the figure on the wrong base; 16⅔% is the answer the other way round (a profit of 20% of cost, as a share of the price); 80% is the cost as a share of the price.",
  "विक्रय मूल्य 100 मानिए: लाभ 20 है, इसलिए लागत 80 है, और लाभ लागत का 20/80 = 25% है। "
  "20% वही आँकड़ा ग़लत आधार पर दोहराता है; 16⅔% उलटी स्थिति का उत्तर है (लागत का 20% लाभ, मूल्य के अंश के रूप में); 80% लागत को मूल्य के अंश के रूप में दिखाता है।",
  "qa-pp-profit-on-price-and-on-cost", _pp1)

def _pp2():
    gap = F(11, 10) ** 3 - 1 - F(3, 10)
    p = F(31) / gap
    assert gap == F(31, 1000) and F(31) / F(1, 100) == 3100 and F(31) / F(1, 1000) == 31000
    return f"₹{int(p):,}"
N(QA, "Percentage & Profit-Loss", "hard",
  "The difference between the compound interest and the simple interest on a sum of money for 3 years at 10% a year is ₹31. What is the sum?",
  "किसी धनराशि पर 10% वार्षिक दर से 3 वर्षों के चक्रवृद्धि ब्याज और साधारण ब्याज का अंतर ₹31 है। धनराशि क्या है?",
  ["₹1,000", "₹3,100", "₹10,000", "₹31,000"], 0,
  "On P at 10% for 3 years, compound interest is P(1.1³ - 1) = 0.331P and simple interest is 0.3P; the difference is 0.031P = ₹31, so P = ₹1,000. "
  "₹3,100 uses the two-year rule, difference = P × r², which does not hold over three years; ₹31,000 keeps only the r³ part; ₹10,000 misplaces the decimal point.",
  "P पर 10% की दर से 3 वर्षों का चक्रवृद्धि ब्याज P(1.1³ - 1) = 0.331P और साधारण ब्याज 0.3P है; अंतर 0.031P = ₹31, अतः P = ₹1,000। "
  "₹3,100 दो वर्ष वाला नियम, अंतर = P × r², लगाता है, जो तीन वर्षों पर लागू नहीं होता; ₹31,000 केवल r³ वाला भाग रखता है; ₹10,000 दशमलव बिंदु ग़लत जगह रखता है।",
  "qa-pp-ci-less-si-over-three-years", _pp2)

def _pp3():
    cost = next(cp for cp in range(1000, 100000, 1000) if F(9, 10) * cp + 4000 == F(125, 100) * F(8, 10) * cp)
    return f"₹{cost:,}"
N(QA, "Percentage & Profit-Loss", "hard",
  "A man sells a car at a loss of 10%. Had he bought it for 20% less and sold it for ₹4,000 more, he would have made a profit of 25%. How much did he pay for the car?",
  "एक व्यक्ति कार को 10% हानि पर बेचता है। यदि वह उसे 20% कम में ख़रीदता और ₹4,000 अधिक में बेचता, तो उसे 25% लाभ होता। उसने कार के लिए कितना दिया था?",
  ["₹32,000", "₹36,000", "₹40,000", "₹44,000"], 2,
  "Let the cost be C. He sold it for 0.9C. Bought for 0.8C and sold at a 25% profit, it would have fetched 1.25 × 0.8C = C, and that price is 0.9C + 4,000. So 0.9C + 4,000 = C, giving C = ₹40,000. "
  "₹36,000 is his actual selling price; ₹32,000 is the cheaper cost; ₹44,000 adds the ₹4,000 to the cost.",
  "लागत C मानिए। उसने कार 0.9C में बेची। 0.8C में ख़रीदकर 25% लाभ पर बेचने से उसे 1.25 × 0.8C = C मिलता, और वह मूल्य 0.9C + 4,000 है। अतः 0.9C + 4,000 = C, जिससे C = ₹40,000। "
  "₹36,000 उसका वास्तविक विक्रय मूल्य है; ₹32,000 सस्ती लागत है; ₹44,000 लागत में ₹4,000 जोड़ देता है।",
  "qa-pp-car-bought-cheaper-sold-dearer", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    seq = [n for n in range(1, 20) for _ in range(n)]
    return str(seq[49])
N(QA, "Sequences & Series", "medium",
  "In the sequence 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ..., each whole number n appears n times. What is the 50th term?",
  "अनुक्रम 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ... में हर पूर्ण संख्या n, n बार आती है। 50वाँ पद क्या है?",
  ["7", "9", "10", "11"], 2,
  "The last 9 is term 1 + 2 + ... + 9 = 45, and the ten 10s fill terms 46 to 55, so the 50th term is 10. "
  "9 stops at the 45th term; 7 comes from taking √50; 11 begins only after the 55th term.",
  "अंतिम 9, पद 1 + 2 + ... + 9 = 45 है, और दस 10, पद 46 से 55 तक भरते हैं, इसलिए 50वाँ पद 10 है। "
  "9, 45वें पद पर रुक जाता है; 7, √50 लेने से आता है; 11, 55वें पद के बाद ही शुरू होता है।",
  "qa-ss-each-n-appears-n-times", _ss1)

def _ss2():
    total = lambda n: F(n, 2) * (2 * 3 + (n - 1) * 4)
    assert (total(20), total(15), total(10)) == (820, 465, 210)
    return _only(n for n in range(1, 200) if total(n) == 1275)
N(QA, "Sequences & Series", "hard",
  "How many terms of the arithmetic progression 3, 7, 11, ... must be added together to make 1275?",
  "समांतर श्रेणी 3, 7, 11, ... के कितने पदों को जोड़ने पर योग 1275 होगा?",
  ["10", "15", "20", "25"], 3,
  "The sum of n terms is n/2 × [2 × 3 + (n - 1) × 4] = n(2n + 1). Setting n(2n + 1) = 1275: 25 × 51 = 1275, so n = 25. "
  "20 terms give only 820, 15 give 465 and 10 give 210.",
  "n पदों का योग n/2 × [2 × 3 + (n - 1) × 4] = n(2n + 1) है। n(2n + 1) = 1275 रखने पर: 25 × 51 = 1275, अतः n = 25। "
  "20 पदों का योग केवल 820, 15 का 465 और 10 का 210 है।",
  "qa-ss-terms-needed-for-a-sum", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    nums = [n for n in range(100, 1000) if set(str(n)) <= set("01234") and len(set(str(n))) == 3]
    return str(len(nums))
N(QA, "Permutation & Combination", "medium",
  "How many three-digit numbers with all their digits different can be formed using the digits 0, 1, 2, 3 and 4?",
  "अंकों 0, 1, 2, 3 और 4 से तीन अंकों की कितनी ऐसी संख्याएँ बनाई जा सकती हैं जिनके सभी अंक अलग-अलग हों?",
  ["48", "60", "64", "100"], 0,
  "The hundreds digit cannot be 0, so it has 4 choices; the tens digit can be any of the 4 digits left, including 0; the units digit has 3: 4 × 4 × 3 = 48. "
  "60 = 5 × 4 × 3 lets the number begin with 0; 100 = 4 × 5 × 5 allows digits to repeat; 64 = 4 × 4 × 4 gives every place four choices.",
  "सैकड़े का अंक 0 नहीं हो सकता, इसलिए उसके 4 विकल्प हैं; दहाई का अंक बचे 4 अंकों में से कोई भी हो सकता है, 0 सहित; इकाई के 3 विकल्प हैं: 4 × 4 × 3 = 48। "
  "60 = 5 × 4 × 3 संख्या को 0 से शुरू होने देता है; 100 = 4 × 5 × 5 अंकों को दोहराने देता है; 64 = 4 × 4 × 4 हर स्थान को चार विकल्प देता है।",
  "qa-pc-three-digit-numbers-from-0-to-4", _pc1)

def _pc2():
    people = ["B1", "B2", "B3", "B4", "B5", "G1", "G2", "G3"]
    ok = sum(1 for p in permutations(people) if not any(p[i][0] == p[i + 1][0] == "G" for i in range(7)))
    assert math.factorial(6) * math.factorial(3) == 4320 and 120 * math.comb(6, 3) == 2400
    return f"{ok:,}"
N(QA, "Permutation & Combination", "hard",
  "In how many ways can 5 boys and 3 girls sit in a row so that no two of the girls sit next to each other?",
  "5 लड़के और 3 लड़कियाँ एक पंक्ति में कितने तरीकों से बैठ सकते हैं कि कोई भी दो लड़कियाँ एक-दूसरे के बगल में न बैठें?",
  ["2,400", "4,320", "14,400", "40,320"], 2,
  "Seat the 5 boys first, in 5! = 120 ways. They leave 6 gaps -- at the two ends and between them -- and the 3 girls must take 3 different gaps: 6 × 5 × 4 = 120 ways. In all, 120 × 120 = 14,400. "
  "40,320 = 8! ignores the condition; 4,320 = 6! × 3! counts the seatings with all three girls together, the opposite case; 2,400 chooses the gaps but forgets that the girls can be arranged in them.",
  "पहले 5 लड़कों को 5! = 120 तरीकों से बैठाइए। वे 6 जगहें छोड़ते हैं -- दोनों छोरों पर और उनके बीच -- और 3 लड़कियों को 3 अलग-अलग जगहें लेनी होंगी: 6 × 5 × 4 = 120 तरीके। कुल 120 × 120 = 14,400। "
  "40,320 = 8! शर्त को अनदेखा करता है; 4,320 = 6! × 3! वे व्यवस्थाएँ गिनता है जिनमें तीनों लड़कियाँ साथ हों, उलटी स्थिति; 2,400 जगहें चुनता है पर भूल जाता है कि उनमें लड़कियों का क्रम भी बदल सकता है।",
  "qa-pc-girls-kept-apart", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    path = 40 * 30 - (40 - 4) * (30 - 4)
    assert 2 * (40 + 30) * 2 == 280 and 280 - 2 * 4 == 272 and (40 + 4) * (30 + 4) - 40 * 30 == 296
    return f"{path} m²"
N(QA, "Geometry & Mensuration", "medium",
  "A rectangular field is 40 m long and 30 m wide. A path 2 m wide runs along all four sides, inside the field. What is the area of the path?",
  "एक आयताकार मैदान 40 मीटर लंबा और 30 मीटर चौड़ा है। मैदान के भीतर चारों भुजाओं के साथ-साथ 2 मीटर चौड़ा एक रास्ता है। रास्ते का क्षेत्रफल क्या है?",
  ["264 m²", "272 m²", "280 m²", "296 m²"], 0,
  "The path is the field less the inner rectangle it leaves: 40 × 30 - (40 - 4)(30 - 4) = 1200 - 936 = 264 m². "
  "280 m² multiplies the perimeter, 140 m, by the width and so counts the four 2 m × 2 m corners twice; 272 m² takes off only two of those corners; 296 m² is the area of a 2 m path laid outside the field.",
  "रास्ता मैदान में से भीतर बचे आयत को घटाने पर मिलता है: 40 × 30 - (40 - 4)(30 - 4) = 1200 - 936 = 264 वर्ग मीटर। "
  "280 वर्ग मीटर परिमाप, 140 मीटर, को चौड़ाई से गुणा करता है और इस तरह 2 मीटर × 2 मीटर के चारों कोनों को दो बार गिनता है; 272 वर्ग मीटर उनमें से केवल दो कोने घटाता है; 296 वर्ग मीटर मैदान के बाहर बने 2 मीटर रास्ते का क्षेत्रफल है।",
  "qa-gm-path-inside-a-field", _gm1,
  opts_hi=["264 वर्ग मीटर", "272 वर्ग मीटर", "280 वर्ग मीटर", "296 वर्ग मीटर"])

def _gm2():
    change = (F(11, 10) ** 2 * F(9, 10) - 1) * 100
    assert F(11, 10) * F(9, 10) == F(99, 100)
    return f"Increases by {float(change):.1f}%"
N(QA, "Geometry & Mensuration", "hard",
  "The radius of a cylinder is increased by 10% and its height is reduced by 10%. What happens to its volume?",
  "एक बेलन की त्रिज्या 10% बढ़ाई जाती है और उसकी ऊँचाई 10% घटाई जाती है। उसके आयतन का क्या होता है?",
  ["Decreases by 10%", "Decreases by 1%", "No change", "Increases by 8.9%"], 3,
  "The volume is πr²h, so the radius counts twice. The new volume is 1.1² × 0.9 = 1.21 × 0.9 = 1.089 times the old: an increase of 8.9%. "
  "'No change' lets the +10% and -10% cancel; 'decreases by 1%' counts the radius only once (1.1 × 0.9 = 0.99); 'decreases by 10%' looks only at the height.",
  "आयतन πr²h है, इसलिए त्रिज्या दो बार गिनी जाती है। नया आयतन पुराने का 1.1² × 0.9 = 1.21 × 0.9 = 1.089 गुना है: 8.9% की वृद्धि। "
  "'कोई बदलाव नहीं' +10% और -10% को एक-दूसरे को काटने देता है; '1% घटता है' त्रिज्या को केवल एक बार गिनता है (1.1 × 0.9 = 0.99); '10% घटता है' केवल ऊँचाई को देखता है।",
  "qa-gm-cylinder-wider-and-shorter", _gm2,
  opts_hi=["10% घटता है", "1% घटता है", "कोई बदलाव नहीं", "8.9% बढ़ता है"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    b_rate = F(1, 3 * 12)                   # A does 2 parts and B 1 part each day; together 1/12 of the job
    return str(1 / (2 * b_rate))
N(QA, "Time & Work", "medium",
  "A is twice as efficient as B, and together they finish a job in 12 days. How many days would A take to do the job alone?",
  "A, B से दोगुना कुशल है, और दोनों मिलकर एक काम 12 दिनों में पूरा करते हैं। A अकेले वह काम कितने दिनों में करेगा?",
  ["6", "8", "12", "18"], 3,
  "Being twice as efficient, A does 2 parts of the work for every 1 that B does, so A does 2/3 of the job when they work together. Working alone, A takes 12 ÷ (2/3) = 18 days (and B 36). "
  "8 multiplies 12 by 2/3 instead of dividing; 6 halves the joint time; 12 is the time for both together.",
  "दोगुना कुशल होने से A, B के हर 1 भाग के मुक़ाबले 2 भाग काम करता है, इसलिए साथ काम करते हुए A काम का 2/3 करता है। अकेले A को 12 ÷ (2/3) = 18 दिन लगेंगे (और B को 36)। "
  "8, 12 को 2/3 से भाग देने के बजाय गुणा करता है; 6 संयुक्त समय को आधा करता है; 12 दोनों का मिलकर लगने वाला समय है।",
  "qa-tw-twice-as-efficient", _tw1)

def _tw2():
    men = F(15 * 8 * 12, 10 * 9)
    assert F(15 * 12, 10) == 18 and F(15 * 8, 9) == F(40, 3) and F(15 * 12, 10) * F(9, 8) == F(81, 4)
    return str(men)
N(QA, "Time & Work", "medium",
  "15 men working 8 hours a day can finish a job in 12 days. How many men are needed to finish it in 10 days, working 9 hours a day?",
  "दिन में 8 घंटे काम करते हुए 15 पुरुष एक काम 12 दिनों में पूरा कर सकते हैं। दिन में 9 घंटे काम करते हुए उसे 10 दिनों में पूरा करने के लिए कितने पुरुष चाहिए?",
  ["13⅓", "16", "18", "20¼"], 1,
  "The job needs 15 × 8 × 12 = 1,440 man-hours. In 10 days of 9 hours each, one man gives 90 hours, so 1,440 ÷ 90 = 16 men are needed. "
  "18 ignores the longer working day; 13⅓ ignores the shorter time allowed; 20¼ turns the ratio of hours upside down.",
  "काम के लिए 15 × 8 × 12 = 1,440 पुरुष-घंटे चाहिए। 9-9 घंटे के 10 दिनों में एक पुरुष 90 घंटे देता है, इसलिए 1,440 ÷ 90 = 16 पुरुष चाहिए। "
  "18 लंबे कार्यदिवस को भूल जाता है; 13⅓ दिए गए कम समय को भूल जाता है; 20¼ घंटों का अनुपात उलट देता है।",
  "qa-tw-man-hours", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    k = next(k for k in range(1, 9) if 3 ** k >= 9)      # each weighing has three outcomes
    return str(k)
N(QA, "Puzzle Hybrid", "hard",
  "Of 9 coins that look alike, one is slightly heavier than the rest. With a two-pan balance and no weights, what is the smallest number of weighings that will always find the heavier coin?",
  "एक जैसे दिखने वाले 9 सिक्कों में से एक बाक़ियों से थोड़ा भारी है। दो पलड़ों वाले तराज़ू से, बिना बाटों के, कम से कम कितनी तौलें भारी सिक्के को सदा ढूँढ लेंगी?",
  ["2", "3", "4", "8"], 0,
  "Each weighing has three outcomes -- left heavier, right heavier, or a balance -- so it can cut the suspects to a third. Put 3 coins on each pan: a heavier side holds the coin, and a balance puts it among the 3 left off. "
  "Weighing 1 of those 3 against another then finds it the same way. So 2 weighings always suffice, and 1 cannot, since one weighing tells apart only three cases. "
  "3 comes from halving the coins each time; 4 from weighing them in pairs; 8 from testing them one at a time.",
  "हर तौल के तीन परिणाम होते हैं -- बायाँ भारी, दायाँ भारी, या संतुलन -- इसलिए वह संदिग्ध सिक्कों को एक-तिहाई कर सकती है। हर पलड़े पर 3 सिक्के रखिए: भारी पलड़े में वह सिक्का है, और संतुलन होने पर वह बाहर रखे 3 में है। "
  "फिर उन 3 में से 1 को दूसरे के सामने तौलने पर वह इसी तरह मिल जाता है। अतः 2 तौलें सदा पर्याप्त हैं, और 1 नहीं, क्योंकि एक तौल केवल तीन स्थितियाँ अलग करती है। "
  "3 हर बार सिक्कों को आधा करने से आता है; 4 जोड़ियों में तौलने से; 8 एक-एक करके जाँचने से।",
  "qa-ph-nine-coins-two-weighings", _ph1)

def _ph2():
    height, day = 0, 0
    while True:
        day += 1
        height += 3
        if height >= 20:
            return f"{day}th"
        height -= 2
N(QA, "Puzzle Hybrid", "medium",
  "A frog at the bottom of a well 20 m deep climbs 3 m up each day and slips 2 m back each night. On which day does it get out of the well?",
  "20 मीटर गहरे कुएँ के तल पर बैठा एक मेंढक हर दिन 3 मीटर ऊपर चढ़ता है और हर रात 2 मीटर नीचे फिसल जाता है। वह किस दिन कुएँ से बाहर निकलेगा?",
  ["7th", "17th", "18th", "20th"], 2,
  "Each full day and night gains only 1 m, but on the last day the frog climbs out before it can slip back. After 17 days and nights it is 17 m up; on the 18th day it climbs 3 m to reach 20 m and is out. "
  "20th assumes a steady 1 m a day all the way to the top; 17th stops a day early; 7th ignores the slipping back (20 ÷ 3).",
  "हर पूरा दिन और रात केवल 1 मीटर की बढ़त देते हैं, पर अंतिम दिन मेंढक फिसलने से पहले ही बाहर निकल जाता है। 17 दिन और रातों के बाद वह 17 मीटर ऊपर है; 18वें दिन वह 3 मीटर चढ़कर 20 मीटर पर पहुँचता है और बाहर निकल जाता है। "
  "20वाँ मान लेता है कि ऊपर तक हर दिन 1 मीटर ही बढ़ेगा; 17वाँ एक दिन पहले रुक जाता है; 7वाँ फिसलने को अनदेखा करता है (20 ÷ 3)।",
  "qa-ph-frog-in-a-well", _ph2,
  opts_hi=["7वें दिन", "17वें दिन", "18वें दिन", "20वें दिन"])

def _ph3():
    start = [x for x in range(1, 500) if x % 5 == 0 and (F(4, 5) * x + 40) / 2 + 30 == 80]
    return _only(start)
N(QA, "Puzzle Hybrid", "medium",
  "A bus starts with some passengers. At the first stop one-fifth of them get off and 40 get on. At the second stop half of those on board get off and 30 get on. There are now 80 passengers. How many were there at the start?",
  "एक बस कुछ यात्रियों के साथ चलती है। पहले पड़ाव पर उनमें से पाँचवाँ भाग उतरता है और 40 चढ़ते हैं। दूसरे पड़ाव पर सवार यात्रियों में से आधे उतरते हैं और 30 चढ़ते हैं। अब 80 यात्री हैं। शुरू में कितने यात्री थे?",
  ["60", "75", "80", "100"], 1,
  "Work backwards from the end. Before the 30 boarded at the second stop there were 50, which was half of those on board before that stop: 100. Before the 40 boarded at the first stop there were 60, "
  "which was four-fifths of the starting number: 75. 100 stops one stop short; 60 forgets to undo the one-fifth who got off; 80 is the number now.",
  "अंत से पीछे की ओर चलिए। दूसरे पड़ाव पर 30 के चढ़ने से पहले 50 यात्री थे, जो उस पड़ाव से पहले सवार यात्रियों का आधा था: 100। पहले पड़ाव पर 40 के चढ़ने से पहले 60 थे, "
  "जो शुरुआती संख्या का चार-पाँचवाँ भाग था: 75। 100 एक पड़ाव पहले रुक जाता है; 60 उतरे हुए पाँचवें भाग को वापस जोड़ना भूल जाता है; 80 अभी की संख्या है।",
  "qa-ph-passengers-counted-backwards", _ph3)

N(QA, "Puzzle Hybrid", "medium",
  "A clock strikes once at 1 o'clock, twice at 2 o'clock, and so on, up to twelve times at 12 o'clock; it does not strike at the half-hours. How many times does it strike in a full day?",
  "एक घड़ी 1 बजे एक बार, 2 बजे दो बार, और इसी तरह 12 बजे बारह बार घंटा बजाती है; आधे घंटों पर वह नहीं बजती। एक पूरे दिन में वह कितनी बार बजती है?",
  ["78", "144", "156", "300"], 2,
  "In 12 hours the clock strikes 1 + 2 + ... + 12 = 78 times, and a day has two such rounds: 156. "
  "78 counts only half the day; 144 assumes 12 strikes every hour; 300 = 1 + 2 + ... + 24 treats the clock as striking up to 24.",
  "12 घंटों में घड़ी 1 + 2 + ... + 12 = 78 बार बजती है, और एक दिन में ऐसे दो चक्कर होते हैं: 156। "
  "78 केवल आधे दिन को गिनता है; 144 हर घंटे 12 बार बजना मानता है; 300 = 1 + 2 + ... + 24 घड़ी को 24 तक बजने वाली मानता है।",
  "qa-ph-strikes-of-a-clock-in-a-day", lambda: str(2 * sum(range(1, 13))))

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
DS(QA, "medium",
   "Is the integer x divisible by 15?",
   "क्या पूर्णांक x, 15 से विभाज्य है?",
   "x is divisible by 30.", "x, 30 से विभाज्य है।",
   "x is divisible by 5.", "x, 5 से विभाज्य है।",
   0,
   "Statement I: every multiple of 30 is a multiple of 15 -- yes, sufficient. Statement II: multiples of 5 include 15 (yes) and 10 (no) -- not sufficient. "
   "So the question can be answered using I alone but not using II alone.",
   "कथन I: 30 का हर गुणज 15 का गुणज है -- हाँ, पर्याप्त। कथन II: 5 के गुणजों में 15 (हाँ) भी है और 10 (नहीं) भी -- पर्याप्त नहीं। "
   "अतः प्रश्न का उत्तर केवल I से दिया जा सकता है, केवल II से नहीं।",
   "qa-ds-divisible-by-15",
   lambda: _ds([x % 15 == 0 for x in range(1, 3000) if x % 30 == 0], [x % 15 == 0 for x in range(1, 3000) if x % 5 == 0],
               [x % 15 == 0 for x in range(1, 3000) if x % 30 == 0 and x % 5 == 0]))

def _ds2():
    xs = [F(k, 2) for k in range(-40, 41)]
    one = [x for x in xs if x * x - 5 * x + 6 == 0]
    two = [x for x in xs if x * x - 3 * x == 0]
    assert sorted(one) == [2, 3] and sorted(two) == [0, 3]
    return _ds(one, two, [x for x in one if x in two])
DS(QA, "hard",
   "What is the value of x?",
   "x का मान क्या है?",
   "x² - 5x + 6 = 0", "x² - 5x + 6 = 0",
   "x² - 3x = 0", "x² - 3x = 0",
   2,
   "Statement I factorises as (x - 2)(x - 3) = 0, so x is 2 or 3 -- not sufficient. Statement II is x(x - 3) = 0, so x is 0 or 3 -- not sufficient. "
   "Together, the only value that satisfies both is 3, so the two statements together answer the question though neither does alone.",
   "कथन I के गुणनखंड (x - 2)(x - 3) = 0 हैं, अतः x, 2 या 3 है -- पर्याप्त नहीं। कथन II, x(x - 3) = 0 है, अतः x, 0 या 3 है -- पर्याप्त नहीं। "
   "दोनों साथ: दोनों को संतुष्ट करने वाला एकमात्र मान 3 है, इसलिए दोनों कथन साथ मिलकर उत्तर देते हैं, यद्यपि कोई अकेला नहीं देता।",
   "qa-ds-two-quadratics-share-a-root", _ds2)
