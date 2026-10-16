# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 3 -- Quantitative Aptitude (17 items: 16 in the Quant slots, 1 in the data-sufficiency block).

The half paper's share of Level 2's Quant mix, rotated across the three minis (this one has one percentage item and
three ratio items): number theory 4, speed 2, percentage 1, ratio 3, work 1, counting 1, geometry 1, series 1,
puzzles 2, data sufficiency 1, at the foundation level (5 easy / 9 medium / 3 hard). None of the shapes of Level 2,
Mini 1 or Mini 2 is reused: what is always even when n is odd, the prime among look-alikes, a telescoping product,
multiples of 7 that end in 7; metres covered in twelve seconds, where two cars meet; a tank filled from 40 to 70
per cent; two numbers from a ratio and a difference, the cheaper of two packs, an area on a map; one more worker each
day; two red balls drawn without replacement; a triangle's angles in a ratio; the series 1, 4, 27, 256; sweets shared
two ways, half and ₹10 more spent at each of three shops; and a square root whose sign is left open. The rows are
written in the order they take on the paper, and every key is worked out in code by check()."""
from fractions import Fraction as F
from csat_common import N, T, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- what is always even when n is odd
def _even():
    exprs = {"n³": lambda n: n ** 3, "2n + 1": lambda n: 2 * n + 1, "n² + 2": lambda n: n * n + 2, "n² + n": lambda n: n * n + n}
    always = [k for k, f in exprs.items() if all(f(n) % 2 == 0 for n in range(1, 200, 2))]
    assert always == ["n² + n"]
    return always[0]
N(QA, "Number Theory", "easy",
  "If n is an odd natural number, which one of the following is always even?",
  "यदि n एक विषम प्राकृत संख्या है, तो निम्नलिखित में से कौन-सा सदैव सम होगा?",
  ["n³", "2n + 1", "n² + 2", "n² + n"], 3,
  "An odd number times an odd number is odd, so n² and n³ are odd. n² + n is odd + odd, which is even (it is n(n + 1), the product of two consecutive numbers, one of which is always even). "
  "n³ is odd; 2n + 1 is even + 1, which is odd; and n² + 2 is odd + even, which is odd.",
  "विषम संख्या गुणा विषम संख्या विषम होती है, इसलिए n² और n³ विषम हैं। n² + n, विषम + विषम है, जो सम होता है (यह n(n + 1) है, यानी दो क्रमागत संख्याओं का गुणनफल, जिनमें से एक सदैव सम होती है)। "
  "n³ विषम है; 2n + 1, सम + 1 है, जो विषम है; और n² + 2, विषम + सम है, जो विषम है।",
  "qa-nt-what-is-always-even-when-n-is-odd", _even)

# 2 -- the series 1, 4, 27, 256
def _nn():
    s = [n ** n for n in range(1, 5)]
    assert s == [1, 4, 27, 256]
    return f"{5 ** 5:,}"
N(QA, "Sequences & Series", "medium",
  "What is the next term of the series 1, 4, 27, 256, ... ?",
  "श्रेणी 1, 4, 27, 256, ... का अगला पद क्या है?",
  ["625", "1,024", "3,125", "46,656"], 2,
  "Each term is a number raised to its own power: 1¹ = 1, 2² = 4, 3³ = 27, 4⁴ = 256. The next term is 5⁵ = 3,125. "
  "625 is 5⁴ and 1,024 is 4⁵ -- each gets the base or the power wrong; 46,656 is 6⁶, which skips a term.",
  "हर पद कोई संख्या है जिसकी घात वही संख्या है: 1¹ = 1, 2² = 4, 3³ = 27, 4⁴ = 256। अगला पद 5⁵ = 3,125 है। "
  "625, 5⁴ है और 1,024, 4⁵ -- दोनों में आधार या घात ग़लत है; 46,656, 6⁶ है, जो एक पद छोड़ देता है।",
  "qa-ss-each-number-to-its-own-power", _nn)

# 4 -- a tank filled from 40 to 70 per cent
def _tank():
    cap = F(60) / (F(70, 100) - F(40, 100))
    assert cap == 200 and F(60) / F(40, 100) == 150 and F(60) / F(1, 4) == 240 and F(60) / F(1, 5) == 300
    return str(cap)
N(QA, "Percentage & Profit-Loss", "medium",
  "A water tank is 40 per cent full. When 60 litres of water are added, it becomes 70 per cent full. What is the capacity of the tank, in litres?",
  "पानी की एक टंकी 40 प्रतिशत भरी है। उसमें 60 लीटर पानी डालने पर वह 70 प्रतिशत भर जाती है। टंकी की क्षमता कितने लीटर है?",
  ["150", "200", "240", "300"], 1,
  "The 60 litres raise the level from 40 to 70 per cent, so they are 30 per cent of the tank: the capacity is 60 ÷ 0.3 = 200 litres (80 litres become 140 litres). "
  "150 treats the 60 litres as the 40 per cent already in the tank; 240 and 300 would make the 60 litres a quarter and a fifth of the tank, not 30 per cent of it.",
  "60 लीटर स्तर को 40 से 70 प्रतिशत तक ले जाते हैं, इसलिए वे टंकी का 30 प्रतिशत हैं: क्षमता 60 ÷ 0.3 = 200 लीटर है (80 लीटर से 140 लीटर)। "
  "150, 60 लीटर को टंकी में पहले से मौजूद 40 प्रतिशत मान लेता है; 240 और 300 में 60 लीटर टंकी का एक-चौथाई और एक-पाँचवाँ होंगे, 30 प्रतिशत नहीं।",
  "qa-pp-a-tank-filled-from-40-to-70-per-cent", _tank)

# 8 -- multiples of 7 that end in 7
def _sevens():
    n = sum(1 for k in range(1, 1000) if k % 7 == 0 and k % 10 == 7)
    assert sum(1 for k in range(1, 1000) if k % 7 == 0) == 142 and 1001 // 7 == 143
    return str(n)
N(QA, "Number Theory", "hard",
  "How many natural numbers less than 1,000 are multiples of 7 and also have 7 as their units digit?",
  "1,000 से कम कितनी प्राकृत संख्याएँ 7 की गुणज हैं और उनका इकाई का अंक भी 7 है?",
  ["15", "16", "142", "143"], 0,
  "7 × k ends in 7 exactly when k ends in 1 (7 × 1 = 7, 7 × 11 = 77, 7 × 21 = 147, ...), since the units digit of 7 × k depends only on the units digit of k, and only 1 gives 7. "
  "So k = 1, 11, 21, ..., 141 (7 × 141 = 987; 7 × 151 = 1,057 is too big): 15 values. 16 counts one value too many; 142 is the number of all multiples of 7 below 1,000; 143 counts up to 1,001.",
  "7 × k का इकाई का अंक तभी 7 होता है जब k का इकाई का अंक 1 हो (7 × 1 = 7, 7 × 11 = 77, 7 × 21 = 147, ...), क्योंकि 7 × k का इकाई का अंक केवल k के इकाई के अंक पर निर्भर करता है, और केवल 1 से 7 मिलता है। "
  "अतः k = 1, 11, 21, ..., 141 (7 × 141 = 987; 7 × 151 = 1,057 बहुत बड़ा है): 15 मान। 16 एक मान अधिक गिनता है; 142, 1,000 से छोटे 7 के सभी गुणजों की संख्या है; 143, 1,001 तक गिनता है।",
  "qa-nt-multiples-of-7-that-end-in-7", _sevens)

# 10 -- metres covered in twelve seconds
def _metres():
    ms = F(90 * 1000, 3600)
    assert ms == 25
    return str(ms * 12)
N(QA, "Speed-Distance-Time", "easy",
  "A car runs at a steady 90 km/h. How many metres does it travel in 12 seconds?",
  "एक कार 90 किमी/घंटा की स्थिर चाल से चल रही है। वह 12 सेकंड में कितने मीटर चलती है?",
  ["250", "300", "360", "1,080"], 1,
  "90 km/h is 90,000 m in 3,600 s, or 25 metres a second (multiply km/h by 5/18). In 12 seconds the car goes 25 × 12 = 300 m. "
  "250 m is the distance in 10 seconds; 360 m takes 90 km/h as 30 m a second; 1,080 multiplies 90 by 12 without changing the units.",
  "90 किमी/घंटा यानी 3,600 सेकंड में 90,000 मी, यानी 25 मीटर प्रति सेकंड (किमी/घंटा को 5/18 से गुणा कीजिए)। 12 सेकंड में कार 25 × 12 = 300 मी चलती है। "
  "250 मी, 10 सेकंड की दूरी है; 360 मी, 90 किमी/घंटा को 30 मी प्रति सेकंड मान लेता है; 1,080, इकाइयाँ बदले बिना 90 को 12 से गुणा करता है।",
  "qa-sdt-metres-covered-in-twelve-seconds", _metres)

# 11 -- two red balls drawn without replacement
def _balls():
    p = F(4, 10) * F(3, 9)
    assert F(4, 10) ** 2 == F(4, 25) and F(6, 10) * F(5, 9) == F(1, 3)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "medium",
  "A bag holds 4 red balls and 6 blue balls. Two balls are drawn one after the other, without the first being put back. What is the probability that both are red?",
  "एक थैले में 4 लाल और 6 नीली गेंदें हैं। दो गेंदें एक के बाद एक निकाली जाती हैं, पहली को वापस रखे बिना। दोनों के लाल होने की प्रायिकता क्या है?",
  ["2/15", "4/25", "1/3", "2/5"], 0,
  "The first ball is red with probability 4/10. If it is, 3 red balls remain among 9, so the second is red with probability 3/9. Both are red with probability 4/10 × 3/9 = 12/90 = 2/15. "
  "4/25 = (4/10)² would be right only if the first ball were put back; 1/3 is the chance that both are blue (6/10 × 5/9); 2/5 is only the chance that the first ball is red.",
  "पहली गेंद के लाल होने की प्रायिकता 4/10 है। यदि वह लाल है, तो 9 में 3 लाल गेंदें बचती हैं, इसलिए दूसरी के लाल होने की प्रायिकता 3/9 है। दोनों के लाल होने की प्रायिकता 4/10 × 3/9 = 12/90 = 2/15 है। "
  "4/25 = (4/10)² तभी सही होता जब पहली गेंद वापस रख दी जाती; 1/3 दोनों के नीली होने की प्रायिकता है (6/10 × 5/9); 2/5 केवल पहली गेंद के लाल होने की प्रायिकता है।",
  "qa-pc-two-red-balls-without-replacement", _balls)

# 16 -- a telescoping product
def _tele():
    p = F(1)
    for k in range(2, 11):
        p *= 1 - F(1, k)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Number Theory", "medium",
  "What is the value of (1 - 1/2)(1 - 1/3)(1 - 1/4) ... (1 - 1/10)?",
  "(1 - 1/2)(1 - 1/3)(1 - 1/4) ... (1 - 1/10) का मान क्या है?",
  ["1/10", "1/9", "1/2", "9/10"], 0,
  "Each bracket is a simple fraction: 1/2 × 2/3 × 3/4 × ... × 9/10. Every numerator cancels the denominator before it, leaving 1/10. "
  "1/9 stops one bracket early, at (1 - 1/9); 1/2 is only the first bracket and 9/10 only the last.",
  "हर कोष्ठक एक सरल भिन्न है: 1/2 × 2/3 × 3/4 × ... × 9/10। हर अंश अपने से पहले के हर को काट देता है, और 1/10 बचता है। "
  "1/9 एक कोष्ठक पहले, (1 - 1/9) पर रुक जाता है; 1/2 केवल पहला कोष्ठक है और 9/10 केवल अंतिम।",
  "qa-nt-a-telescoping-product", _tele)

# 17 -- a triangle's angles in a ratio
def _angles():
    part = F(180, 2 + 3 + 4)
    return f"{4 * part}°"
N(QA, "Geometry & Mensuration", "easy",
  "The three angles of a triangle are in the ratio 2 : 3 : 4. What is the largest angle?",
  "किसी त्रिभुज के तीनों कोण 2 : 3 : 4 के अनुपात में हैं। सबसे बड़ा कोण कितना है?",
  ["20°", "40°", "60°", "80°"], 3,
  "The angles of a triangle add up to 180°, which is shared in 2 + 3 + 4 = 9 parts of 20° each. The angles are 40°, 60° and 80°, so the largest is 80°. "
  "20° is one part; 40° and 60° are the other two angles.",
  "त्रिभुज के कोणों का योग 180° है, जो 2 + 3 + 4 = 9 भागों में बँटता है, हर भाग 20°। कोण 40°, 60° और 80° हैं, इसलिए सबसे बड़ा 80° है। "
  "20° एक भाग है; 40° और 60° बाक़ी दो कोण हैं।",
  "qa-gm-a-triangle-s-angles-in-a-ratio", _angles)

# 21 -- the cheaper of two packs
_KEY_PACK = "The 750 g pack is cheaper, by about ₹13 a kilogram."
def _pack():
    a, b = F(96) / F(400, 1000), F(170) / F(750, 1000)
    assert a == 240 and round(float(a - b)) == 13 and 170 - 96 == 74
    return _KEY_PACK if b < a else None
T(QA, "Ratio, Mixtures & Alligation", "medium",
  "Tea is sold in a 400 g pack for ₹96 and in a 750 g pack for ₹170. Which one of the following is correct?",
  "चाय 400 ग्राम के पैक में ₹96 में और 750 ग्राम के पैक में ₹170 में बिकती है। निम्नलिखित में से कौन-सा सही है?",
  ["The 400 g pack is cheaper, by about ₹13 a kilogram.",
   "The two packs cost exactly the same per kilogram.",
   "The 750 g pack is cheaper, by about ₹74 a kilogram.",
   _KEY_PACK],
  ["400 ग्राम का पैक लगभग ₹13 प्रति किलोग्राम सस्ता है।",
   "दोनों पैक प्रति किलोग्राम ठीक बराबर क़ीमत के हैं।",
   "750 ग्राम का पैक लगभग ₹74 प्रति किलोग्राम सस्ता है।",
   "750 ग्राम का पैक लगभग ₹13 प्रति किलोग्राम सस्ता है।"], 3,
  "Compare the price of a kilogram. The 400 g pack costs 96 ÷ 0.4 = ₹240 a kilogram; the 750 g pack costs 170 ÷ 0.75 ≈ ₹226.67 a kilogram. The larger pack is cheaper by about ₹13.33 a kilogram. "
  "Saying the 400 g pack is cheaper gets the comparison the wrong way round; the packs do not cost the same per kilogram; and ₹74 is just the difference between the two prices, ₹170 - ₹96, which compares packs of different sizes.",
  "एक किलोग्राम का मूल्य तुलना कीजिए। 400 ग्राम का पैक 96 ÷ 0.4 = ₹240 प्रति किलोग्राम पड़ता है; 750 ग्राम का पैक 170 ÷ 0.75 ≈ ₹226.67 प्रति किलोग्राम। बड़ा पैक लगभग ₹13.33 प्रति किलोग्राम सस्ता है। "
  "400 ग्राम के पैक को सस्ता कहना तुलना को उलट देता है; पैक प्रति किलोग्राम बराबर क़ीमत के नहीं हैं; और ₹74 केवल दोनों क़ीमतों का अंतर है, ₹170 - ₹96, जो अलग-अलग आकार के पैकों की तुलना करता है।",
  "qa-rm-the-cheaper-of-two-packs", craft="application", pos=3, check=_pack)

# 22 -- an area on a map
def _map():
    km_per_cm = F(50000, 100000)                # 1 cm on the map is 50,000 cm = 0.5 km
    area = 6 * km_per_cm ** 2
    assert area == F(3, 2) and 6 * km_per_cm == 3
    return f"{float(area)} km²"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "On a map drawn to a scale of 1 : 50,000, a lake covers 6 square centimetres. What is the actual area of the lake?",
  "1 : 50,000 के पैमाने पर बने एक मानचित्र पर एक झील 6 वर्ग सेंटीमीटर में फैली है। झील का वास्तविक क्षेत्रफल कितना है?",
  ["0.75 km²", "1.5 km²", "3 km²", "6 km²"], 1,
  "At 1 : 50,000, 1 cm on the map is 50,000 cm, or 0.5 km, on the ground. A square centimetre on the map is therefore 0.5 km × 0.5 km = 0.25 km², and 6 cm² stand for 6 × 0.25 = 1.5 km². "
  "3 km² applies the scale of lengths to an area (6 × 0.5) without squaring it; 6 km² takes each square centimetre as a square kilometre; 0.75 km² halves the right answer once more.",
  "1 : 50,000 पर मानचित्र का 1 सेमी ज़मीन पर 50,000 सेमी, यानी 0.5 किमी है। अतः मानचित्र का एक वर्ग सेंटीमीटर 0.5 किमी × 0.5 किमी = 0.25 वर्ग किमी है, और 6 वर्ग सेमी, 6 × 0.25 = 1.5 वर्ग किमी दर्शाते हैं। "
  "3 वर्ग किमी लंबाई के पैमाने को वर्ग किए बिना क्षेत्रफल पर लगा देता है (6 × 0.5); 6 वर्ग किमी हर वर्ग सेंटीमीटर को एक वर्ग किलोमीटर मान लेता है; 0.75 वर्ग किमी सही उत्तर को एक बार और आधा कर देता है।",
  "qa-rm-an-area-on-a-map", _map,
  opts_hi=["0.75 वर्ग किमी", "1.5 वर्ग किमी", "3 वर्ग किमी", "6 वर्ग किमी"])

# 24 -- one more worker each day
def _workers():
    done, day = 0, 0
    while done < 36:
        day += 1
        done += day
    assert done == 36 and sum(range(1, 7)) == 21 and sum(range(1, 8)) == 28
    return {6: "6th", 7: "7th", 8: "8th", 9: "9th"}[day]
N(QA, "Time & Work", "medium",
  "A job needs 36 worker-days of work. One worker works on the first day, two on the second day, three on the third day, and so on, with one more worker each day. On which day is the job completed?",
  "एक काम के लिए 36 श्रमिक-दिवस का काम चाहिए। पहले दिन एक श्रमिक काम करता है, दूसरे दिन दो, तीसरे दिन तीन, और इसी तरह हर दिन एक श्रमिक अधिक। काम किस दिन पूरा होता है?",
  ["6th", "7th", "8th", "9th"], 2,
  "After n days the work done is 1 + 2 + ... + n = n(n + 1)/2 worker-days. After 6 days it is 21, after 7 days 28 and after 8 days 36, so the job is completed on the 8th day. "
  "The 6th day divides 36 by 6 as if six workers had worked every day; by the end of the 7th day only 28 worker-days are done; by the 9th day the job is already finished.",
  "n दिनों के बाद किया गया काम 1 + 2 + ... + n = n(n + 1)/2 श्रमिक-दिवस है। 6 दिनों के बाद यह 21, 7 दिनों के बाद 28 और 8 दिनों के बाद 36 है, इसलिए काम आठवें दिन पूरा होता है। "
  "छठा दिन 36 को 6 से ऐसे भाग देता है मानो हर दिन छह श्रमिक काम करते हों; सातवें दिन के अंत तक केवल 28 श्रमिक-दिवस का काम होता है; नौवें दिन तक काम पहले ही पूरा हो चुका होता है।",
  "qa-tw-one-more-worker-each-day", _workers,
  opts_hi=["छठे दिन", "सातवें दिन", "आठवें दिन", "नौवें दिन"])

# 31 -- the prime among look-alikes
def _prime():
    isprime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    ps = [n for n in (127, 133, 143, 161) if isprime(n)]
    assert ps == [127] and 133 == 7 * 19 and 143 == 11 * 13 and 161 == 7 * 23
    return str(ps[0])
N(QA, "Number Theory", "easy",
  "Which one of the following is a prime number?",
  "निम्नलिखित में से कौन-सी एक अभाज्य संख्या है?",
  ["127", "133", "143", "161"], 0,
  "To test a number below 169 for primality, it is enough to try the primes up to 11 (since 13² = 169). 127 is not divisible by 2, 3, 5, 7 or 11, so it is prime. "
  "The others only look prime: 133 = 7 × 19, 143 = 11 × 13 and 161 = 7 × 23.",
  "169 से छोटी किसी संख्या के अभाज्य होने की जाँच के लिए 11 तक के अभाज्यों से भाग देकर देखना पर्याप्त है (क्योंकि 13² = 169)। 127, 2, 3, 5, 7 या 11 से विभाज्य नहीं है, इसलिए वह अभाज्य है। "
  "बाक़ी केवल अभाज्य जैसी दिखती हैं: 133 = 7 × 19, 143 = 11 × 13 और 161 = 7 × 23।",
  "qa-nt-the-prime-among-look-alikes", _prime)

# 33 -- where two cars meet
def _meet():
    t = F(300, 60 + 40)
    assert t == 3
    return str(60 * t)
N(QA, "Speed-Distance-Time", "medium",
  "Two towns, A and B, are 300 km apart. At the same moment, a car leaves A for B at 60 km/h and another car leaves B for A at 40 km/h. How far from A will the two cars meet?",
  "दो कस्बे, A और B, 300 किमी दूर हैं। एक ही क्षण में एक कार A से B की ओर 60 किमी/घंटा से और दूसरी कार B से A की ओर 40 किमी/घंटा से चलती है। दोनों कारें A से कितनी दूरी पर मिलेंगी?",
  ["120 km", "150 km", "180 km", "200 km"], 2,
  "The cars close the gap at 60 + 40 = 100 km/h, so they meet after 300 ÷ 100 = 3 hours. In 3 hours the car from A covers 60 × 3 = 180 km, and the car from B 120 km. "
  "120 km is the distance from B; 150 km assumes they meet halfway, which would need equal speeds; 200 km shares the road as if the car from A were twice as fast.",
  "कारें 60 + 40 = 100 किमी/घंटा की दर से दूरी घटाती हैं, इसलिए वे 300 ÷ 100 = 3 घंटे बाद मिलती हैं। 3 घंटों में A वाली कार 60 × 3 = 180 किमी चलती है, और B वाली 120 किमी। "
  "120 किमी, B से दूरी है; 150 किमी मानता है कि वे बीच में मिलती हैं, जिसके लिए चालें बराबर होनी चाहिए; 200 किमी सड़क को ऐसे बाँटता है मानो A वाली कार दुगुनी तेज़ हो।",
  "qa-sdt-where-two-cars-meet", lambda: _meet() + " km",
  opts_hi=["120 किमी", "150 किमी", "180 किमी", "200 किमी"])

# 37 -- two numbers from a ratio and a difference
def _ratio():
    part = F(18, 7 - 5)
    assert (5 * part, 7 * part) == (45, 63) and 42 - 30 == 12
    return str(7 * part)
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "Two numbers are in the ratio 5 : 7, and their difference is 18. What is the larger number?",
  "दो संख्याएँ 5 : 7 के अनुपात में हैं, और उनका अंतर 18 है। बड़ी संख्या क्या है?",
  ["30", "42", "45", "63"], 3,
  "The difference of 7 - 5 = 2 parts is 18, so each part is 9. The numbers are 5 × 9 = 45 and 7 × 9 = 63; the larger is 63. "
  "45 is the smaller number; 30 and 42 are in the ratio 5 : 7 but differ by only 12, not 18.",
  "7 - 5 = 2 भागों का अंतर 18 है, इसलिए हर भाग 9 है। संख्याएँ 5 × 9 = 45 और 7 × 9 = 63 हैं; बड़ी 63 है। "
  "45 छोटी संख्या है; 30 और 42, 5 : 7 के अनुपात में तो हैं पर उनका अंतर केवल 12 है, 18 नहीं।",
  "qa-rm-two-numbers-from-a-ratio-and-a-difference", _ratio)

# 38 -- half and ₹10 more spent at each of three shops
def _left(m):
    for _ in range(3):
        m = m - (F(m, 2) + 10)
    return m
def _shops():
    start = next(x for x in range(1, 1000) if _left(x) == 0)
    back, wrong = 0, 0
    for _ in range(3):
        back, wrong = 2 * (back + 10), 2 * wrong + 10      # the right way back, and doubling before adding
    assert back == start == 140 and wrong == 70 and 2 * (2 * (0 + 10) + 10) == 60
    return str(start)
N(QA, "Puzzle Hybrid", "hard",
  "A man goes to three shops one after another. At each shop he spends half of the money he has and then ₹10 more. After the third shop he has no money left. How much money did he start with?",
  "एक व्यक्ति एक के बाद एक तीन दुकानों पर जाता है। हर दुकान पर वह अपने पास के धन का आधा और फिर ₹10 अधिक ख़र्च करता है। तीसरी दुकान के बाद उसके पास कुछ नहीं बचता। उसने कितने धन से शुरुआत की थी?",
  ["₹60", "₹70", "₹140", "₹280"], 2,
  "Work backwards. If he has m rupees on entering a shop, he leaves with m/2 - 10, so m = 2 × (what he leaves with + 10). After the third shop he has 0, so he entered it with 2 × 10 = ₹20; "
  "he entered the second with 2 × (20 + 10) = ₹60 and the first with 2 × (60 + 10) = ₹140. Check: 140 → 60 → 20 → 0. "
  "₹60 stops after working back through only two shops; ₹70 doubles before adding the ₹10 at each step (0 → 10 → 30 → 70); ₹280 doubles once too often.",
  "उलटी दिशा में चलिए। यदि दुकान में जाते समय उसके पास m रुपये हैं, तो वह m/2 - 10 लेकर निकलता है, अतः m = 2 × (निकलते समय की राशि + 10)। तीसरी दुकान के बाद उसके पास 0 है, इसलिए वह उसमें 2 × 10 = ₹20 लेकर गया; "
  "दूसरी में 2 × (20 + 10) = ₹60 और पहली में 2 × (60 + 10) = ₹140 लेकर। जाँच: 140 → 60 → 20 → 0। "
  "₹60 केवल दो दुकानों तक उलटा चलकर रुक जाता है; ₹70 हर क़दम पर ₹10 जोड़ने से पहले दुगुना कर देता है (0 → 10 → 30 → 70); ₹280 एक बार अधिक दुगुना करता है।",
  "qa-ph-half-and-ten-more-at-each-of-three-shops", lambda: "₹" + _shops())

# 40 -- sweets shared two ways
def _sweets():
    kids = next(k for k in range(1, 100) if 4 * k + 3 == 5 * k - 5)
    assert kids == 8 and 4 * kids == 32 and 5 * kids == 40
    return str(4 * kids + 3)
N(QA, "Puzzle Hybrid", "medium",
  "If 4 sweets are given to each child in a group, 3 sweets are left over; if 5 sweets are given to each child, 5 more sweets are needed. How many sweets are there?",
  "यदि किसी समूह के हर बच्चे को 4 मिठाइयाँ दी जाएँ, तो 3 मिठाइयाँ बच जाती हैं; यदि हर बच्चे को 5 मिठाइयाँ दी जाएँ, तो 5 मिठाइयाँ और चाहिए। कुल कितनी मिठाइयाँ हैं?",
  ["32", "35", "40", "43"], 1,
  "Giving one more sweet to each child uses up the 3 that were left over and the 5 that are still needed, 8 sweets in all, so there are 8 children. The sweets number 4 × 8 + 3 = 35 (check: 5 × 8 - 5 = 35). "
  "32 and 40 are the sweets that 4 and 5 per child would need; 43 adds the 3 left over to 40 instead of to 32.",
  "हर बच्चे को एक मिठाई अधिक देने में बची 3 मिठाइयाँ और अभी चाहिए 5 मिठाइयाँ, कुल 8 मिठाइयाँ लगती हैं, इसलिए बच्चे 8 हैं। मिठाइयाँ 4 × 8 + 3 = 35 हैं (जाँच: 5 × 8 - 5 = 35)। "
  "32 और 40 वे मिठाइयाँ हैं जो हर बच्चे को 4 और 5 देने में लगेंगी; 43, बची 3 मिठाइयों को 32 के बजाय 40 में जोड़ देता है।",
  "qa-ph-sweets-shared-two-ways", _sweets)

# ---- the data-sufficiency block's Quant item
def _ds1():
    xs = range(-100, 101)
    s1 = [x for x in xs if x * x == 49]
    s2 = [x for x in xs if x % 2 == 1]
    both = [x for x in s1 if x % 2 == 1]
    assert sorted(both) == [-7, 7]
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the value of the integer x?",
   "पूर्णांक x का मान क्या है?",
   "x² = 49.", "x² = 49।",
   "x is an odd number.", "x एक विषम संख्या है।",
   3,
   "Statement I gives x = 7 or x = -7 -- not sufficient. Statement II allows any odd number -- not sufficient. Together: both 7 and -7 are odd, so x could still be either. "
   "Even both statements together do not answer the question.",
   "कथन I से x = 7 या x = -7 -- पर्याप्त नहीं। कथन II कोई भी विषम संख्या होने देता है -- पर्याप्त नहीं। दोनों साथ: 7 और -7 दोनों विषम हैं, इसलिए x अब भी दोनों में से कोई भी हो सकता है। "
   "दोनों कथन साथ मिलकर भी प्रश्न का उत्तर नहीं देते।",
   "qa-ds-a-square-root-whose-sign-is-left-open", _ds1)
