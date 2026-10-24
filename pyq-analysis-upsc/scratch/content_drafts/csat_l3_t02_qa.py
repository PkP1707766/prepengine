# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 2 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Level 3's harder mix (3 easy / 18 medium / 13 hard) with none of the shapes of Level 2 Tests 1-7, Level 1 Minis 1-3 or
Level 3 Test 1: the factor that 1,001 lacks, the fewest square tiles for a floor, reciprocals from a sum and a product,
the digit sum of 999,999 × 777,777, three-digit numbers of odd digits, powers of 2 added and divided by 3, pairs with
1/m + 1/n = 1/6, digits whose product is 12; the tip of a shadow, a walk that is partly level and partly hill, a convoy
on a bridge, two walkers who meet off the midpoint; the largest and smallest of ten numbers, a journey part by cycle and
part on foot, shares in the ratio 1/2 : 1/3 : 1/4, literate women among the literate, a recipe's ratio; a price that
includes GST, a deposit's real return, a circle's radius cut by a fifth; the odd numbers that pass 1,000, the terms
common to two progressions; PINs with a repeated digit, a team that two people refuse to share; a rectangle from its
diagonal and perimeter, a square in a semicircle; cows on a field that keeps growing, a fence with a late painter;
negative marking, the weekday of 15 August 1947, the river crossing, a page number added twice; and two
data-sufficiency items (divisible by 9 two ways, students and benches). Every key is worked out in code by check()."""
import datetime
from collections import deque
from fractions import Fraction as F
from itertools import product
import csat_common as c
from csat_common import N, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    not_f = [d for d in (7, 11, 13, 17) if 1001 % d]
    assert 1001 == 7 * 11 * 13 and not_f == [17]
    return "17"
N(QA, "Number Theory", "easy",
  "Which one of the following is NOT a factor of 1,001?",
  "निम्नलिखित में से कौन-सा 1,001 का गुणनखंड नहीं है?",
  ["7", "11", "13", "17"], 3,
  "1,001 = 7 × 11 × 13 (7 × 143 = 1,001 and 143 = 11 × 13), so 7, 11 and 13 are its factors and 17 is not: 17 × 58 = 986 and 17 × 59 = 1,003. "
  "The factorisation is worth remembering: it is why any three-digit number written twice, such as 274,274, is divisible by 7, 11 and 13.",
  "1,001 = 7 × 11 × 13 (7 × 143 = 1,001 और 143 = 11 × 13), इसलिए 7, 11 और 13 इसके गुणनखंड हैं और 17 नहीं: 17 × 58 = 986 और 17 × 59 = 1,003। "
  "यह गुणनखंडन याद रखने योग्य है: इसी कारण दो बार लिखी गई कोई भी तीन अंकों की संख्या, जैसे 274,274, 7, 11 और 13 से विभाज्य होती है।",
  "qa-nt-the-factor-1001-lacks", _nt1)

def _nt2():
    from math import gcd
    g = gcd(450, 360)
    assert g == 90 and (450 // 45) * (360 // 45) == 80 and (450 // 30) * (360 // 30) == 180 and (450 // 18) * (360 // 18) == 500
    return str((450 // g) * (360 // g))
N(QA, "Number Theory", "medium",
  "A floor 4.5 m long and 3.6 m wide is to be covered with square tiles, all of one size, without cutting any tile. What is the least number of tiles needed?",
  "4.5 मीटर लंबे और 3.6 मीटर चौड़े एक फ़र्श को एक ही आकार की वर्गाकार टाइलों से, किसी टाइल को काटे बिना, ढकना है। कम से कम कितनी टाइलें चाहिए?",
  ["20", "80", "180", "500"], 0,
  "The fewest tiles means the largest tile whose side divides both 450 cm and 360 cm exactly: HCF(450, 360) = 90 cm. Then 450 ÷ 90 = 5 tiles fit along the length and 360 ÷ 90 = 4 along the width, 20 in all. "
  "80, 180 and 500 use tiles of 45, 30 and 18 cm, which also divide both sides but are not the largest such size.",
  "सबसे कम टाइलों का अर्थ है वह सबसे बड़ी टाइल जिसकी भुजा 450 सेमी और 360 सेमी दोनों को पूरा विभाजित करे: HCF(450, 360) = 90 सेमी। तब लंबाई में 450 ÷ 90 = 5 और चौड़ाई में 360 ÷ 90 = 4 टाइलें आती हैं, कुल 20। "
  "80, 180 और 500 क्रमशः 45, 30 और 18 सेमी की टाइलें लेते हैं, जो दोनों भुजाओं को विभाजित तो करती हैं पर सबसे बड़ा ऐसा आकार नहीं हैं।",
  "qa-nt-the-fewest-square-tiles-for-a-floor", _nt2)

def _nt3():
    xs = [(a, 50 - a) for a in range(1, 50) if a * (50 - a) == 400]
    assert xs[0] == (10, 40)
    s = F(1, xs[0][0]) + F(1, xs[0][1])
    return f"{s.numerator}/{s.denominator}"
N(QA, "Number Theory", "medium",
  "The sum of two numbers is 50 and their product is 400. What is the sum of their reciprocals?",
  "दो संख्याओं का योग 50 और गुणनफल 400 है। उनके व्युत्क्रमों का योग क्या है?",
  ["1/50", "1/40", "1/10", "1/8"], 3,
  "1/a + 1/b = (a + b)/ab = 50/400 = 1/8, without finding the numbers (they are 10 and 40: 1/10 + 1/40 = 5/40 = 1/8). "
  "1/50 is the reciprocal of the sum; 1/40 and 1/10 are the reciprocals of the two numbers taken one at a time.",
  "1/a + 1/b = (a + b)/ab = 50/400 = 1/8, संख्याएँ निकाले बिना (वे 10 और 40 हैं: 1/10 + 1/40 = 5/40 = 1/8)। "
  "1/50 योग का व्युत्क्रम है; 1/40 और 1/10 दोनों संख्याओं के अलग-अलग व्युत्क्रम हैं।",
  "qa-nt-reciprocals-from-a-sum-and-a-product", _nt3)

def _nt4():
    p = 999999 * 777777
    assert p == 777776222223
    return str(sum(int(d) for d in str(p)))
N(QA, "Number Theory", "hard",
  "What is the sum of the digits of the product 999,999 × 777,777?",
  "गुणनफल 999,999 × 777,777 के अंकों का योग क्या है?",
  ["45", "48", "51", "54"], 3,
  "999,999 × 777,777 = 777,777 × (1,000,000 - 1) = 777,777,000,000 - 777,777 = 777,776,222,223. Its digits add up to 7 × 5 + 6 + 2 × 5 + 3 = 54. "
  "The pattern holds for any six-digit multiplier that does not end in 0: the product begins with the number less 1 and ends with that number's nines' complement, so each pair of matching places adds up to 9 and the six pairs give 6 × 9 = 54.",
  "999,999 × 777,777 = 777,777 × (1,000,000 - 1) = 777,777,000,000 - 777,777 = 777,776,222,223। इसके अंकों का योग 7 × 5 + 6 + 2 × 5 + 3 = 54 है। "
  "यह नियम 0 पर न समाप्त होने वाले किसी भी छह अंकों के गुणक पर लागू होता है: गुणनफल उस संख्या में से 1 घटाकर शुरू होता है और उसके 'नौ के पूरक' पर समाप्त होता है, इसलिए हर मेल खाते स्थानों का जोड़ा 9 देता है और छह जोड़े 6 × 9 = 54 देते हैं।",
  "qa-nt-the-digit-sum-of-999999-times-777777", _nt4)

def _nt5():
    xs = [n for n in range(100, 1000) if all(int(d) % 2 for d in str(n))]
    assert len(xs) == 125 and sum(xs) == 125 * 555
    return f"{sum(xs):,}"
N(QA, "Number Theory", "medium",
  "What is the sum of all the three-digit numbers whose digits are all odd?",
  "उन सभी तीन अंकों की संख्याओं का योग क्या है जिनके सभी अंक विषम हैं?",
  ["62,500", "68,750", "69,000", "69,375"], 3,
  "Each of the three places can hold 1, 3, 5, 7 or 9, so there are 5 × 5 × 5 = 125 such numbers, and each odd digit appears in each place 25 times. Every place therefore averages 5, the numbers average 555, and the sum is 125 × 555 = 69,375. "
  "62,500 and 68,750 take the average as 500 and 550; 69,000 has no basis.",
  "तीनों स्थानों में से हर एक में 1, 3, 5, 7 या 9 आ सकता है, इसलिए ऐसी 5 × 5 × 5 = 125 संख्याएँ हैं, और हर विषम अंक हर स्थान पर 25 बार आता है। अतः हर स्थान का औसत 5 है, संख्याओं का औसत 555, और योग 125 × 555 = 69,375। "
  "62,500 और 68,750 औसत को 500 और 550 मान लेते हैं; 69,000 का कोई आधार नहीं।",
  "qa-nt-three-digit-numbers-of-odd-digits", _nt5)

def _nt6():
    r = sum(2 ** k for k in range(100)) % 3
    assert r == 0 and (2 ** 100 - 1) % 3 == 0
    return str(r)
N(QA, "Number Theory", "medium",
  "What is the remainder when 1 + 2 + 2² + 2³ + ... + 2⁹⁹ is divided by 3?",
  "1 + 2 + 2² + 2³ + ... + 2⁹⁹ को 3 से भाग देने पर शेषफल क्या है?",
  ["0", "1", "2", "It cannot be found without adding the terms"], 0,
  "Take the hundred terms in fifty pairs: 1 + 2 = 3, 2² + 2³ = 4 + 8 = 12, and in general 2²ᵏ + 2²ᵏ⁺¹ = 3 × 2²ᵏ. Every pair is a multiple of 3, so the whole sum is, and the remainder is 0. "
  "(Equivalently, the sum is 2¹⁰⁰ - 1, and 2¹⁰⁰ = 4⁵⁰ leaves remainder 1 on division by 3.) Nothing needs to be added up; the remainders 1 and 2 belong to sums with an odd number of terms.",
  "सौ पदों को पचास जोड़ों में लीजिए: 1 + 2 = 3, 2² + 2³ = 4 + 8 = 12, और सामान्यतः 2²ᵏ + 2²ᵏ⁺¹ = 3 × 2²ᵏ। हर जोड़ा 3 का गुणज है, इसलिए पूरा योग भी है, और शेषफल 0 है। "
  "(इसी तरह, योग 2¹⁰⁰ - 1 है, और 2¹⁰⁰ = 4⁵⁰ को 3 से भाग देने पर शेषफल 1 बचता है।) कुछ भी जोड़ने की आवश्यकता नहीं; शेषफल 1 और 2 विषम संख्या में पदों वाले योगों के होते हैं।",
  "qa-nt-powers-of-two-added-and-divided-by-three", _nt6,
  opts_hi=["0", "1", "2", "पदों को जोड़े बिना नहीं निकाला जा सकता"])

def _nt7():
    pairs = [(m, n) for m in range(1, 200) for n in range(1, 200) if F(1, m) + F(1, n) == F(1, 6)]
    assert len({tuple(sorted(p)) for p in pairs}) == 5
    return str(len(pairs))
N(QA, "Number Theory", "hard",
  "How many ordered pairs of natural numbers (m, n) satisfy 1/m + 1/n = 1/6?",
  "प्राकृत संख्याओं के कितने क्रमित युग्म (m, n) समीकरण 1/m + 1/n = 1/6 को संतुष्ट करते हैं?",
  ["4", "5", "8", "9"], 3,
  "Both m and n must exceed 6, since each reciprocal is less than 1/6. Clearing fractions, 6n + 6m = mn, which rearranges to (m - 6)(n - 6) = 36. So m - 6 can be any of the 9 divisors of 36 -- 1, 2, 3, 4, 6, 9, 12, 18, 36 -- each fixing n: "
  "the pairs run from (7, 42) to (42, 7), with (12, 12) in the middle. 5 counts each unordered pair once; 8 leaves out (12, 12); 4 leaves out both.",
  "m और n दोनों 6 से बड़े होने चाहिए, क्योंकि हर व्युत्क्रम 1/6 से छोटा है। भिन्न हटाने पर 6n + 6m = mn, जो (m - 6)(n - 6) = 36 बन जाता है। अतः m - 6, 36 के 9 भाजकों -- 1, 2, 3, 4, 6, 9, 12, 18, 36 -- में से कोई भी हो सकता है, और हर एक n तय करता है: "
  "युग्म (7, 42) से (42, 7) तक हैं, बीच में (12, 12)। 5 हर अक्रमित युग्म को एक बार गिनता है; 8, (12, 12) को छोड़ देता है; 4 दोनों को छोड़ता है।",
  "qa-nt-pairs-with-reciprocals-adding-to-one-sixth", _nt7)

def _nt8():
    xs = [n for n in range(100, 1000) if int(str(n)[0]) * int(str(n)[1]) * int(str(n)[2]) == 12]
    return str(len(xs))
N(QA, "Number Theory", "hard",
  "How many three-digit numbers have digits whose product is 12?",
  "तीन अंकों की कितनी संख्याओं के अंकों का गुणनफल 12 है?",
  ["6", "9", "12", "15"], 3,
  "No digit can be 0, and 12 splits into three digits in only three ways: 1 × 2 × 6, 1 × 3 × 4 and 2 × 2 × 3. The first two have three different digits and give 3! = 6 numbers each; 2, 2, 3 gives only 3 (223, 232, 322). The total is 6 + 6 + 3 = 15. "
  "12 forgets the case 2 × 2 × 3; 6 counts the orders of a single set; 9 counts each set's orders as 3.",
  "कोई अंक 0 नहीं हो सकता, और 12 को तीन अंकों में केवल तीन तरह से तोड़ा जा सकता है: 1 × 2 × 6, 1 × 3 × 4 और 2 × 2 × 3। पहले दो में तीन अलग अंक हैं और हर एक 3! = 6 संख्याएँ देता है; 2, 2, 3 केवल 3 देता है (223, 232, 322)। कुल 6 + 6 + 3 = 15। "
  "12, 2 × 2 × 3 वाली स्थिति भूल जाता है; 6 एक ही समूह के क्रम गिनता है; 9 हर समूह के क्रमों को 3 गिनता है।",
  "qa-nt-digits-whose-product-is-12", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    H, h, v = F(48, 10), F(16, 10), F(12, 10)
    tip = H / (H - h) * v                      # tip at x with x / H = (x - d) / h, so x = H d / (H - h)
    assert tip == F(18, 10) and h / (H - h) * v == F(6, 10)
    return "1.8 m/s"
N(QA, "Speed-Distance-Time", "hard",
  "A man 1.6 m tall walks away from a lamp post 4.8 m high at a steady 1.2 m/s on level ground. At what speed does the tip of his shadow move along the ground?",
  "1.6 मीटर लंबा एक व्यक्ति समतल ज़मीन पर 4.8 मीटर ऊँचे एक बिजली के खंभे से 1.2 मीटर/सेकंड की स्थिर चाल से दूर जाता है। उसकी छाया का सिरा ज़मीन पर किस चाल से चलता है?",
  ["0.6 m/s", "1.2 m/s", "1.8 m/s", "2.4 m/s"], 2,
  "Let the man be d from the post and the shadow's tip x from it. The lamp, the top of his head and the tip lie on one straight line, so by similar triangles x/4.8 = (x - d)/1.6, which gives x = 1.5d. The tip is always 1.5 times as far as the man, so it moves at 1.5 × 1.2 = 1.8 m/s. "
  "0.6 m/s is the rate at which the shadow itself lengthens (the tip's speed less the man's); 1.2 m/s is the man's speed; 2.4 m/s doubles it.",
  "मान लीजिए व्यक्ति खंभे से d दूरी पर है और छाया का सिरा x दूरी पर। बत्ती, उसके सिर का शीर्ष और छाया का सिरा एक सीधी रेखा में हैं, इसलिए समरूप त्रिभुजों से x/4.8 = (x - d)/1.6, जिससे x = 1.5d मिलता है। सिरा हमेशा व्यक्ति से 1.5 गुना दूर रहता है, इसलिए वह 1.5 × 1.2 = 1.8 मीटर/सेकंड से चलता है। "
  "0.6 मीटर/सेकंड वह दर है जिससे छाया स्वयं लंबी होती है (सिरे की चाल में से व्यक्ति की चाल घटाकर); 1.2 मीटर/सेकंड व्यक्ति की चाल है; 2.4 मीटर/सेकंड उसका दोगुना।",
  "qa-sdt-the-tip-of-a-shadow", _sdt1,
  opts_hi=["0.6 मीटर/सेकंड", "1.2 मीटर/सेकंड", "1.8 मीटर/सेकंड", "2.4 मीटर/सेकंड"])

def _sdt2():
    ds = set()
    for level in range(0, 25):
        for hill in range(0, 25):
            if F(2 * level, 4) + F(hill, 3) + F(hill, 6) == 6:
                ds.add(level + hill)
    assert ds == {12}
    return "12 km"
N(QA, "Speed-Distance-Time", "hard",
  "The road from a man's home to a temple is partly level and partly uphill. He walks at 4 km/h on the level, 3 km/h uphill and 6 km/h downhill, and the walk there and back takes 6 hours in all. How far is the temple from his home?",
  "एक व्यक्ति के घर से एक मंदिर तक की सड़क कुछ समतल है और कुछ चढ़ाई वाली। वह समतल पर 4 किमी/घंटा, चढ़ाई पर 3 किमी/घंटा और उतराई पर 6 किमी/घंटा चलता है, और आने-जाने में कुल 6 घंटे लगते हैं। मंदिर उसके घर से कितनी दूर है?",
  ["9 km", "12 km", "15 km", "24 km"], 1,
  "Let the level part be L km and the hill H km. The level part is walked both ways at 4 km/h, taking 2L/4 = L/2 hours; the hill is climbed at 3 km/h and descended at 6 km/h, taking H/3 + H/6 = H/2 hours. So the round trip takes (L + H)/2 = 6 hours, and the one-way distance L + H is 12 km. "
  "The split between level and hill does not matter, because the hill's up-and-down average equals the level speed. 24 km is the round trip; 9 km and 15 km do not give 6 hours.",
  "मान लीजिए समतल भाग L किमी और पहाड़ी भाग H किमी है। समतल भाग दोनों ओर 4 किमी/घंटा से चला जाता है, जिसमें 2L/4 = L/2 घंटे लगते हैं; पहाड़ी 3 किमी/घंटा से चढ़ी और 6 किमी/घंटा से उतरी जाती है, जिसमें H/3 + H/6 = H/2 घंटे लगते हैं। अतः आने-जाने में (L + H)/2 = 6 घंटे लगते हैं, और एक ओर की दूरी L + H, 12 किमी है। "
  "समतल और पहाड़ी का बँटवारा मायने नहीं रखता, क्योंकि पहाड़ी पर चढ़ने-उतरने का औसत समतल की चाल के बराबर है। 24 किमी आने-जाने की दूरी है; 9 किमी और 15 किमी से 6 घंटे नहीं आते।",
  "qa-sdt-a-walk-partly-level-and-partly-hill", _sdt2,
  opts_hi=["9 किमी", "12 किमी", "15 किमी", "24 किमी"])

def _sdt3():
    length = 20 * 10 + 19 * 5
    t = F(length + 200, F(18 * 1000, 3600))
    assert length == 295 and t == 99 and F(20 * 10 + 20 * 5 + 200, 5) == 100
    return f"{t} s"
N(QA, "Speed-Distance-Time", "medium",
  "A convoy of 20 trucks, each 10 m long, moves at 18 km/h with a gap of 5 m between one truck and the next. How long does the convoy take to cross a bridge 200 m long completely, from the moment the first truck enters it until the last truck leaves it?",
  "20 ट्रकों का एक काफ़िला, जिसमें हर ट्रक 10 मीटर लंबा है, 18 किमी/घंटा से चलता है और एक ट्रक तथा अगले के बीच 5 मीटर का अंतर है। पहले ट्रक के पुल पर चढ़ने से लेकर अंतिम ट्रक के उतरने तक, काफ़िले को 200 मीटर लंबा पुल पूरा पार करने में कितना समय लगता है?",
  ["40 s", "59 s", "99 s", "100 s"], 2,
  "18 km/h = 5 m/s. The convoy is 20 × 10 + 19 × 5 = 295 m long -- 20 trucks have only 19 gaps between them -- and to cross completely its front must travel the bridge's length plus its own: 200 + 295 = 495 m, which takes 99 s. "
  "100 s counts 20 gaps; 59 s is the time for the convoy to pass a single point; 40 s is the time for the first truck's front to cross the bridge alone.",
  "18 किमी/घंटा = 5 मीटर/सेकंड। काफ़िला 20 × 10 + 19 × 5 = 295 मीटर लंबा है -- 20 ट्रकों के बीच केवल 19 अंतर होते हैं -- और पूरा पार करने के लिए उसके अगले सिरे को पुल की लंबाई और अपनी लंबाई तय करनी होती है: 200 + 295 = 495 मीटर, जिसमें 99 सेकंड लगते हैं। "
  "100 सेकंड 20 अंतर गिनता है; 59 सेकंड वह समय है जिसमें काफ़िला एक बिंदु को पार करता है; 40 सेकंड वह समय है जिसमें केवल पहले ट्रक का अगला सिरा पुल पार करता है।",
  "qa-sdt-a-convoy-on-a-bridge", _sdt3,
  opts_hi=["40 सेकंड", "59 सेकंड", "99 सेकंड", "100 सेकंड"])

def _sdt4():
    ds = [d for d in range(1, 200) if F(4 * d, 8) - F(3 * d, 8) == 2]
    assert ds == [16]
    return f"{ds[0]} km"
N(QA, "Speed-Distance-Time", "medium",
  "P and Q start at the same time from towns X and Y and walk towards each other at 3 km/h and 5 km/h respectively. They meet 2 km from the point midway between X and Y. How far apart are X and Y?",
  "P और Q एक ही समय पर कस्बों X और Y से चलकर क्रमशः 3 किमी/घंटा और 5 किमी/घंटा से एक-दूसरे की ओर चलते हैं। वे X और Y के ठीक बीच वाले बिंदु से 2 किमी दूर मिलते हैं। X और Y कितनी दूर हैं?",
  ["8 km", "10 km", "12 km", "16 km"], 3,
  "In the same time they cover distances in the ratio of their speeds, 3 : 5, so P covers 3/8 of the distance d and Q covers 5/8 of it. The midpoint is at 4/8 of d from X, so they meet d/8 from it. Then d/8 = 2 and d = 16 km. "
  "8 km takes the 2 km to be a quarter of the distance (the difference between the two shares, 5/8 - 3/8); 10 and 12 km do not put the meeting point 2 km from the middle.",
  "समान समय में वे अपनी चालों के अनुपात 3 : 5 में दूरियाँ तय करते हैं, इसलिए P दूरी d का 3/8 भाग तय करता है और Q 5/8 भाग। बीच का बिंदु X से d का 4/8 है, इसलिए वे उससे d/8 दूर मिलते हैं। तब d/8 = 2 और d = 16 किमी। "
  "8 किमी, 2 किमी को दूरी का चौथाई (दोनों हिस्सों का अंतर, 5/8 - 3/8) मान लेता है; 10 और 12 किमी मिलन बिंदु को बीच से 2 किमी दूर नहीं रखते।",
  "qa-sdt-two-walkers-who-meet-off-the-midpoint", _sdt4,
  opts_hi=["8 किमी", "10 किमी", "12 किमी", "16 किमी"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    total = 10 * 25
    big, small = total - 9 * 23, total - 9 * 26
    assert (big, small) == (43, 16)
    return str(big - small)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The average of ten numbers is 25. If the largest of them is removed, the average of the other nine is 23; if instead the smallest is removed, the average of the other nine is 26. What is the difference between the largest and the smallest number?",
  "दस संख्याओं का औसत 25 है। यदि उनमें से सबसे बड़ी हटा दी जाए, तो शेष नौ का औसत 23 है; यदि इसके बजाय सबसे छोटी हटाई जाए, तो शेष नौ का औसत 26 है। सबसे बड़ी और सबसे छोटी संख्या का अंतर क्या है?",
  ["3", "16", "27", "43"], 2,
  "The ten numbers add up to 250. Without the largest, the nine add up to 9 × 23 = 207, so the largest is 43; without the smallest, they add up to 9 × 26 = 234, so the smallest is 16. The difference is 27 (equivalently, 9 × (26 - 23) = 27). "
  "3 is the difference between the two averages, not between the numbers; 43 and 16 are the largest and smallest themselves.",
  "दसों संख्याओं का योग 250 है। सबसे बड़ी के बिना नौ का योग 9 × 23 = 207 है, इसलिए सबसे बड़ी 43 है; सबसे छोटी के बिना योग 9 × 26 = 234 है, इसलिए सबसे छोटी 16 है। अंतर 27 है (इसी तरह, 9 × (26 - 23) = 27)। "
  "3 दोनों औसतों का अंतर है, संख्याओं का नहीं; 43 और 16 स्वयं सबसे बड़ी और सबसे छोटी संख्याएँ हैं।",
  "qa-rm-the-largest-and-smallest-of-ten-numbers", _rm1)

def _rm2():
    t_foot = F(15 * 5 - 60, 15 - 5)            # the shortfall from cycling all the way, made good at 10 km/h per hour
    assert t_foot == F(3, 2)
    return f"{float(t_foot * 5)} km"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A man covers 60 km in 5 hours, partly by cycle at 15 km/h and the rest on foot at 5 km/h. How far does he walk?",
  "एक व्यक्ति 5 घंटे में 60 किमी तय करता है, कुछ साइकिल से 15 किमी/घंटा की चाल पर और शेष पैदल 5 किमी/घंटा की चाल पर। वह कितना पैदल चलता है?",
  ["7.5 km", "10 km", "15 km", "52.5 km"], 0,
  "Had he cycled for all 5 hours he would have covered 75 km, 15 km more than he did. Every hour spent walking instead of cycling covers 10 km less, so he walked for 15 ÷ 10 = 1.5 hours, that is 1.5 × 5 = 7.5 km (and cycled 3.5 hours, 52.5 km). "
  "52.5 km is the distance cycled; 15 km is the shortfall; 10 km is the loss for each hour on foot.",
  "यदि वह पूरे 5 घंटे साइकिल चलाता तो 75 किमी तय करता, यानी 15 किमी अधिक। साइकिल के बजाय पैदल बिताया हर घंटा 10 किमी कम तय करता है, इसलिए वह 15 ÷ 10 = 1.5 घंटे पैदल चला, यानी 1.5 × 5 = 7.5 किमी (और 3.5 घंटे साइकिल पर, 52.5 किमी)। "
  "52.5 किमी साइकिल से तय दूरी है; 15 किमी कमी है; 10 किमी पैदल चलने के हर घंटे की हानि है।",
  "qa-rm-a-journey-part-by-cycle-and-part-on-foot", _rm2,
  opts_hi=["7.5 किमी", "10 किमी", "15 किमी", "52.5 किमी"])

def _rm3():
    w = [F(1, 2), F(1, 3), F(1, 4)]
    shares = [x / sum(w) * 1950 for x in w]
    assert shares == [900, 600, 450]
    return f"₹{int(shares[2])}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "₹1,950 is divided among A, B and C in the ratio 1/2 : 1/3 : 1/4. How much does C get?",
  "₹1,950 को A, B और C में 1/2 : 1/3 : 1/4 के अनुपात में बाँटा जाता है। C को कितना मिलता है?",
  ["₹450", "₹600", "₹650", "₹900"], 0,
  "Multiply the three fractions by 12, the LCM of 2, 3 and 4: the ratio becomes 6 : 4 : 3, with 13 parts in all. Each part is 1,950 ÷ 13 = ₹150, so C gets 3 × 150 = ₹450 (A ₹900, B ₹600). "
  "₹900 and ₹600 are A's and B's shares; ₹650 divides the money equally.",
  "तीनों भिन्नों को 2, 3 और 4 के LCM, 12 से गुणा कीजिए: अनुपात 6 : 4 : 3 बन जाता है, कुल 13 भाग। हर भाग 1,950 ÷ 13 = ₹150 है, इसलिए C को 3 × 150 = ₹450 मिलते हैं (A को ₹900, B को ₹600)। "
  "₹900 और ₹600, A और B के हिस्से हैं; ₹650 राशि को बराबर बाँटता है।",
  "qa-rm-shares-in-the-ratio-of-unit-fractions", _rm3)

def _rm4():
    men, women = F(60), F(40)
    lit_m, lit_w = men * F(3, 10), women * F(4, 10)
    f = lit_w / (lit_m + lit_w)
    assert f == F(8, 17)
    return f"{f.numerator}/{f.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a town, 60 per cent of the adults are men. 30 per cent of the men and 40 per cent of the women are literate. What fraction of the literate adults are women?",
  "एक कस्बे में 60 प्रतिशत वयस्क पुरुष हैं। 30 प्रतिशत पुरुष और 40 प्रतिशत महिलाएँ साक्षर हैं। साक्षर वयस्कों का कितना भाग महिलाएँ हैं?",
  ["2/5", "4/9", "8/17", "4/7"], 2,
  "Out of 100 adults, 60 are men and 40 women; 18 men and 16 women are literate, 34 in all, of whom 16/34 = 8/17 are women -- a little under half, even though a woman is more likely to be literate than a man. "
  "2/5 is the women's share of all adults; 4/7 = 40/(30 + 40) compares the two literacy rates and ignores the fact that there are more men; 4/9 has no basis.",
  "100 वयस्कों में 60 पुरुष और 40 महिलाएँ हैं; 18 पुरुष और 16 महिलाएँ साक्षर हैं, कुल 34, जिनमें 16/34 = 8/17 महिलाएँ हैं -- आधे से कुछ कम, यद्यपि किसी महिला के साक्षर होने की संभावना पुरुष से अधिक है। "
  "2/5 सभी वयस्कों में महिलाओं का हिस्सा है; 4/7 = 40/(30 + 40) दोनों साक्षरता दरों की तुलना करता है और इस तथ्य को अनदेखा करता है कि पुरुष अधिक हैं; 4/9 का कोई आधार नहीं।",
  "qa-rm-literate-women-among-the-literate", _rm4)

def _rm5():
    flour = F(35, 10) * F(5, 2)
    assert flour == F(875, 100)
    return "8.75 kg"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "A recipe uses flour and sugar in the ratio 5 : 2 by weight. How much flour is needed with 3.5 kg of sugar?",
  "एक व्यंजन-विधि में आटा और चीनी भार के अनुसार 5 : 2 के अनुपात में लगते हैं। 3.5 किग्रा चीनी के साथ कितना आटा चाहिए?",
  ["8.75 kg", "10 kg", "12.25 kg", "17.5 kg"], 0,
  "Flour is 5/2 times the sugar: 3.5 × 5/2 = 8.75 kg. 12.25 kg is the flour and sugar together; 17.5 kg multiplies the sugar by 5 without dividing by 2; 10 kg has no basis.",
  "आटा चीनी का 5/2 गुना है: 3.5 × 5/2 = 8.75 किग्रा। 12.25 किग्रा आटा और चीनी मिलाकर है; 17.5 किग्रा चीनी को 5 से गुणा करता है पर 2 से भाग नहीं देता; 10 किग्रा का कोई आधार नहीं।",
  "qa-rm-a-recipe-s-ratio", _rm5,
  opts_hi=["8.75 किग्रा", "10 किग्रा", "12.25 किग्रा", "17.5 किग्रा"])

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    p = F(2360) / F(118, 100)
    assert p == 2000 and 2360 - F(18, 100) * 2360 == F(193520, 100)
    return "₹2,000"
N(QA, "Percentage & Profit-Loss", "easy",
  "The price of an article, including GST at 18 per cent, is ₹2,360. What is its price before GST?",
  "18 प्रतिशत जीएसटी सहित एक वस्तु का मूल्य ₹2,360 है। जीएसटी से पहले उसका मूल्य क्या है?",
  ["₹1,935", "₹2,000", "₹2,124", "₹2,785"], 1,
  "The tax is charged on the price before tax, so 2,360 is 118 per cent of it: 2,360 ÷ 1.18 = ₹2,000 (and the GST is ₹360). "
  "₹1,935 takes 18 per cent off the price that already includes the tax, which removes too much; ₹2,785 adds the tax a second time; ₹2,124 has no basis.",
  "कर कर-पूर्व मूल्य पर लगता है, इसलिए 2,360 उसका 118 प्रतिशत है: 2,360 ÷ 1.18 = ₹2,000 (और जीएसटी ₹360)। "
  "₹1,935 कर-सहित मूल्य में से 18 प्रतिशत घटाता है, जो अधिक घटा देता है; ₹2,785 कर दोबारा जोड़ता है; ₹2,124 का कोई आधार नहीं।",
  "qa-pp-a-price-that-includes-gst", _pp1)

def _pp2():
    r = F(110, 100) / F(106, 100) - 1
    assert abs(float(r) * 100 - 3.77) < 0.01
    return f"{float(r) * 100:.2f} per cent"
N(QA, "Percentage & Profit-Loss", "hard",
  "A fixed deposit pays interest of 10 per cent for a year, and over the same year prices rise by 6 per cent. By about what percentage does the depositor's purchasing power grow?",
  "एक सावधि जमा एक वर्ष के लिए 10 प्रतिशत ब्याज देती है, और उसी वर्ष क़ीमतें 6 प्रतिशत बढ़ती हैं। जमाकर्ता की क्रय शक्ति लगभग कितने प्रतिशत बढ़ती है?",
  ["3.77 per cent", "4.00 per cent", "4.24 per cent", "16.60 per cent"], 0,
  "₹100 grows to ₹110, but goods that cost ₹100 now cost ₹106, so the money buys 110/106 = 1.0377 times as much: purchasing power grows by about 3.77 per cent. "
  "4 per cent simply subtracts the two rates, which is only an approximation; 4.24 per cent multiplies 4 by 1.06 instead of dividing; 16.6 per cent adds inflation to the return.",
  "₹100, ₹110 हो जाते हैं, पर जो सामान ₹100 का था वह अब ₹106 का है, इसलिए पैसा 110/106 = 1.0377 गुना ख़रीद पाता है: क्रय शक्ति लगभग 3.77 प्रतिशत बढ़ती है। "
  "4 प्रतिशत केवल दोनों दरों को घटाता है, जो मात्र एक सन्निकटन है; 4.24 प्रतिशत 4 को 1.06 से भाग देने के बजाय गुणा करता है; 16.6 प्रतिशत मुद्रास्फीति को प्रतिफल में जोड़ देता है।",
  "qa-pp-a-deposit-s-real-return", _pp2,
  opts_hi=["3.77 प्रतिशत", "4.00 प्रतिशत", "4.24 प्रतिशत", "16.60 प्रतिशत"])

def _pp3():
    fall = 1 - F(8, 10) ** 2
    assert fall == F(36, 100)
    return "36 per cent"
N(QA, "Percentage & Profit-Loss", "medium",
  "If the radius of a circle is reduced by 20 per cent, by what percentage does its area fall?",
  "यदि किसी वृत्त की त्रिज्या 20 प्रतिशत घटा दी जाए, तो उसका क्षेत्रफल कितने प्रतिशत घटता है?",
  ["20 per cent", "36 per cent", "40 per cent", "64 per cent"], 1,
  "Area varies as the square of the radius, so it becomes 0.8² = 0.64 of what it was: a fall of 36 per cent. "
  "64 per cent is the area that remains, not the fall; 20 per cent assumes that area changes in step with the radius; 40 per cent doubles the 20 per cent.",
  "क्षेत्रफल त्रिज्या के वर्ग के अनुसार बदलता है, इसलिए वह पहले का 0.8² = 0.64 हो जाता है: 36 प्रतिशत की कमी। "
  "64 प्रतिशत बचा हुआ क्षेत्रफल है, कमी नहीं; 20 प्रतिशत मान लेता है कि क्षेत्रफल त्रिज्या के साथ उसी अनुपात में बदलता है; 40 प्रतिशत, 20 प्रतिशत को दोगुना करता है।",
  "qa-pp-a-circle-s-radius-cut-by-a-fifth", _pp3,
  opts_hi=["20 प्रतिशत", "36 प्रतिशत", "40 प्रतिशत", "64 प्रतिशत"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    s, n = 0, 0
    while s <= 1000:
        n += 1
        s += 2 * n - 1
    assert s == n * n and 31 * 31 == 961
    return str(n)
N(QA, "Sequences & Series", "medium",
  "How many terms of the series 1 + 3 + 5 + 7 + ... must be added for the sum to exceed 1,000 for the first time?",
  "श्रेणी 1 + 3 + 5 + 7 + ... के कितने पद जोड़ने पर योग पहली बार 1,000 से अधिक होता है?",
  ["31", "32", "33", "500"], 1,
  "The sum of the first n odd numbers is n²: 1, 4, 9, 16, .... 31² = 961 is still below 1,000 and 32² = 1,024 is above it, so 32 terms are needed. "
  "31 terms fall short; 33 is one more than needed; 500 is the number of odd numbers below 1,000.",
  "पहली n विषम संख्याओं का योग n² होता है: 1, 4, 9, 16, ....। 31² = 961 अभी 1,000 से कम है और 32² = 1,024 उससे अधिक, इसलिए 32 पद चाहिए। "
  "31 पद कम पड़ते हैं; 33 आवश्यकता से एक अधिक है; 500, 1,000 से छोटी विषम संख्याओं की गिनती है।",
  "qa-ss-the-odd-numbers-that-pass-1000", _ss1)

def _ss2():
    a = set(range(3, 101, 4))
    b = set(range(2, 101, 7))
    common = sorted(a & b)
    assert common == [23, 51, 79]
    return str(sum(common))
N(QA, "Sequences & Series", "hard",
  "The progressions 3, 7, 11, 15, ... and 2, 9, 16, 23, ... are each continued as far as 100. What is the sum of the numbers that appear in both?",
  "समांतर श्रेणियाँ 3, 7, 11, 15, ... और 2, 9, 16, 23, ... दोनों 100 तक बढ़ाई जाती हैं। जो संख्याएँ दोनों में आती हैं उनका योग क्या है?",
  ["102", "130", "153", "181"], 2,
  "The first progression holds the numbers that leave remainder 3 on division by 4, the second those that leave remainder 2 on division by 7. The first number in both is 23, and after it the common numbers recur every LCM(4, 7) = 28: 23, 51, 79 (107 is past 100). Their sum is 153. "
  "102 and 130 miss one of the three; 181 adds 28 to the total as if there were a fourth term.",
  "पहली श्रेणी में वे संख्याएँ हैं जो 4 से भाग देने पर शेषफल 3 देती हैं, दूसरी में वे जो 7 से भाग देने पर शेषफल 2 देती हैं। दोनों में पहली संख्या 23 है, और उसके बाद उभयनिष्ठ संख्याएँ हर LCM(4, 7) = 28 पर आती हैं: 23, 51, 79 (107, 100 से आगे है)। इनका योग 153 है। "
  "102 और 130 तीन में से एक को छोड़ देते हैं; 181 योग में 28 ऐसे जोड़ता है मानो कोई चौथा पद हो।",
  "qa-ss-terms-common-to-two-progressions", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    rep = sum(1 for p in product(range(10), repeat=4) if len(set(p)) < 4)
    assert rep == 10 ** 4 - 10 * 9 * 8 * 7
    return f"{rep:,}"
N(QA, "Permutation & Combination", "hard",
  "A PIN is any string of four digits from 0 to 9, a leading 0 being allowed. How many PINs have at least one digit repeated?",
  "पिन 0 से 9 तक के चार अंकों की कोई भी शृंखला है, जिसमें शुरू में 0 भी हो सकता है। कितने पिन में कम से कम एक अंक दोहराया गया है?",
  ["4,960", "5,040", "6,561", "9,000"], 0,
  "Count the complement. There are 10⁴ = 10,000 PINs in all, and 10 × 9 × 8 × 7 = 5,040 of them have four different digits, so 10,000 - 5,040 = 4,960 repeat at least one digit. "
  "5,040 counts the PINs with no repeat; 9,000 is the number of four-digit numbers, which cannot begin with 0; 6,561 = 9⁴ has no basis here.",
  "पूरक गिनिए। कुल 10⁴ = 10,000 पिन हैं, और उनमें से 10 × 9 × 8 × 7 = 5,040 के चारों अंक अलग हैं, इसलिए 10,000 - 5,040 = 4,960 में कम से कम एक अंक दोहराया गया है। "
  "5,040 बिना दोहराव वाले पिन गिनता है; 9,000 चार अंकों की संख्याओं की गिनती है, जो 0 से शुरू नहीं हो सकतीं; 6,561 = 9⁴ का यहाँ कोई आधार नहीं।",
  "qa-pc-pins-with-a-repeated-digit", _pc1)

def _pc2():
    from itertools import combinations
    teams = [t for t in combinations(range(7), 4) if not (0 in t and 1 in t)]
    assert len(teams) == 35 - 10
    return str(len(teams))
N(QA, "Permutation & Combination", "medium",
  "A team of 4 is to be chosen from 7 people, two of whom refuse to be in the same team. In how many ways can the team be chosen?",
  "7 व्यक्तियों में से 4 की एक टीम चुननी है, जिनमें से दो एक ही टीम में रहने से मना करते हैं। टीम कितने तरीक़ों से चुनी जा सकती है?",
  ["10", "15", "20", "25"], 3,
  "Without the condition there are 7C4 = 35 teams. Those that contain both of the two people need 2 more from the other 5: 5C2 = 10. So 35 - 10 = 25 teams are allowed. "
  "10 counts the forbidden teams; 20 counts only the teams with exactly one of the two and leaves out the 5 with neither; 15 has no basis.",
  "शर्त के बिना 7C4 = 35 टीमें बनती हैं। जिनमें दोनों व्यक्ति हैं उनके लिए शेष 5 में से 2 और चाहिए: 5C2 = 10। अतः 35 - 10 = 25 टीमें अनुमत हैं। "
  "10 वर्जित टीमें गिनता है; 20 केवल दोनों में से ठीक एक वाली टीमें गिनता है और दोनों के बिना वाली 5 टीमें छोड़ देता है; 15 का कोई आधार नहीं।",
  "qa-pc-a-team-two-people-refuse-to-share", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    sols = [(l, w) for l in range(1, 17) for w in range(1, l + 1) if l + w == 17 and l * l + w * w == 169]
    assert sols == [(12, 5)]
    return f"{sols[0][0] * sols[0][1]} cm²"
N(QA, "Geometry & Mensuration", "medium",
  "The diagonal of a rectangle is 13 cm and its perimeter is 34 cm. What is its area?",
  "एक आयत का विकर्ण 13 सेमी और परिमाप 34 सेमी है। उसका क्षेत्रफल क्या है?",
  ["30 cm²", "60 cm²", "72 cm²", "120 cm²"], 1,
  "Length plus breadth is 17 and, by Pythagoras, length² + breadth² = 169. Since (l + b)² = l² + b² + 2lb, 289 = 169 + 2lb, so lb = 60 cm² (the sides are 12 and 5 cm). "
  "120 is 2lb, the step before halving; 30 halves once too often; 72 = 12 × 6 has no basis.",
  "लंबाई और चौड़ाई का योग 17 है और पाइथागोरस से लंबाई² + चौड़ाई² = 169। चूँकि (l + b)² = l² + b² + 2lb, 289 = 169 + 2lb, इसलिए lb = 60 वर्ग सेमी (भुजाएँ 12 और 5 सेमी हैं)। "
  "120, 2lb है, आधा करने से पहले का चरण; 30 एक बार अधिक आधा करता है; 72 = 12 × 6 का कोई आधार नहीं।",
  "qa-gm-a-rectangle-from-its-diagonal-and-perimeter", _gm1,
  opts_hi=["30 वर्ग सेमी", "60 वर्ग सेमी", "72 वर्ग सेमी", "120 वर्ग सेमी"])

def _gm2():
    r2 = 125                                  # (5√5)²
    s2 = F(r2) / F(5, 4)                      # s² + (s/2)² = r²
    assert s2 == 100
    return "10 cm"
N(QA, "Geometry & Mensuration", "hard",
  "A square is drawn inside a semicircle of radius 5√5 cm, with one side of the square lying along the diameter and the two other corners on the arc. What is the side of the square?",
  "5√5 सेमी त्रिज्या वाले एक अर्धवृत्त के भीतर एक वर्ग खींचा जाता है, जिसकी एक भुजा व्यास पर है और शेष दो कोने चाप पर। वर्ग की भुजा क्या है?",
  ["5 cm", "5√2 cm", "10 cm", "5√5 cm"], 2,
  "The square sits symmetrically on the diameter, so each upper corner is s/2 from the centre horizontally and s above it. That corner lies on the circle: (s/2)² + s² = (5√5)² = 125, so 5s²/4 = 125, s² = 100 and s = 10 cm. "
  "5√5 cm is the radius; 5√2 cm would be the side of a square whose diagonal is a diameter of a full circle of radius 5; 5 cm halves the right answer.",
  "वर्ग व्यास पर सममित रूप से रखा है, इसलिए हर ऊपरी कोना केंद्र से क्षैतिज रूप से s/2 और ऊपर s दूर है। वह कोना वृत्त पर है: (s/2)² + s² = (5√5)² = 125, अतः 5s²/4 = 125, s² = 100 और s = 10 सेमी। "
  "5√5 सेमी त्रिज्या है; 5√2 सेमी, 5 त्रिज्या वाले पूरे वृत्त में उस वर्ग की भुजा होती जिसका विकर्ण व्यास हो; 5 सेमी सही उत्तर का आधा है।",
  "qa-gm-a-square-in-a-semicircle", _gm2,
  opts_hi=["5 सेमी", "5√2 सेमी", "10 सेमी", "5√5 सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    sols = [(F(g), F(r)) for g in range(1, 400) for r in range(0, 40) if g + 20 * r == 10 * 20 and g + 10 * r == 15 * 10]
    assert sols == [(100, 5)]
    g, r = sols[0]
    return str(int((g + 5 * r) / 5))
N(QA, "Time & Work", "hard",
  "The grass in a field grows at a steady rate. 10 cows can eat all of it, including what grows meanwhile, in 20 days, and 15 cows can do so in 10 days. How many cows can eat it all in 5 days?",
  "एक खेत में घास एक स्थिर दर से उगती है। 10 गायें उसे, इस बीच उगने वाली घास सहित, 20 दिनों में खा सकती हैं, और 15 गायें 10 दिनों में। कितनी गायें उसे 5 दिनों में पूरा खा सकती हैं?",
  ["20", "25", "30", "40"], 1,
  "Measure grass in the amount one cow eats in a day. 10 cows in 20 days eat 200 units, and 15 cows in 10 days eat 150; the extra 50 units grew in the extra 10 days, so the grass grows 5 units a day and the field started with 200 - 20 × 5 = 100. "
  "In 5 days there are 100 + 25 = 125 units, which 125 ÷ 5 = 25 cows eat. 40 assumes the 200 units of the first case and no growth; 30 assumes the 150 units of the second; 20 uses the starting grass and ignores growth.",
  "घास को उस मात्रा में मापिए जो एक गाय एक दिन में खाती है। 10 गायें 20 दिनों में 200 इकाई खाती हैं, और 15 गायें 10 दिनों में 150; अतिरिक्त 50 इकाई अतिरिक्त 10 दिनों में उगीं, इसलिए घास प्रतिदिन 5 इकाई उगती है और खेत में आरंभ में 200 - 20 × 5 = 100 इकाई थीं। "
  "5 दिनों में 100 + 25 = 125 इकाई होती हैं, जिन्हें 125 ÷ 5 = 25 गायें खाती हैं। 40 पहली स्थिति की 200 इकाइयाँ और कोई वृद्धि न मानता है; 30 दूसरी स्थिति की 150 इकाइयाँ मानता है; 20 आरंभ की घास लेता है और वृद्धि को अनदेखा करता है।",
  "qa-tw-cows-on-a-field-that-keeps-growing", _tw1)

def _tw2():
    head = 4 * 3
    t = F(60 - head, 4 + 2)
    assert t == 8
    return f"{int(3 + t)} h"
N(QA, "Time & Work", "medium",
  "A paints 4 m² of a fence an hour and B paints 2 m² an hour. They are to paint 60 m² together, but B starts 3 hours after A. How long after A starts is the painting finished?",
  "A एक घंटे में बाड़ का 4 वर्ग मीटर रँगता है और B 2 वर्ग मीटर। उन्हें मिलकर 60 वर्ग मीटर रँगना है, पर B, A के 3 घंटे बाद शुरू करता है। A के शुरू करने के कितने समय बाद रँगाई पूरी होती है?",
  ["10 h", "11 h", "12 h", "15 h"], 1,
  "In his first 3 hours A paints 12 m² alone, leaving 48 m². Together they paint 6 m² an hour, so the rest takes 8 hours: 3 + 8 = 11 hours after A starts. "
  "10 h divides 60 by 6, ignoring B's late start; 15 h is A painting alone; 12 h adds B's delay to the joint time without allowing for A's work in it.",
  "अपने पहले 3 घंटों में A अकेला 12 वर्ग मीटर रँगता है, 48 वर्ग मीटर बचते हैं। साथ मिलकर वे प्रति घंटा 6 वर्ग मीटर रँगते हैं, इसलिए शेष में 8 घंटे लगते हैं: A के शुरू करने के 3 + 8 = 11 घंटे बाद। "
  "10 घंटे 60 को 6 से भाग देता है, B के देर से शुरू करने को अनदेखा करते हुए; 15 घंटे A का अकेले रँगना है; 12 घंटे संयुक्त समय में B की देरी जोड़ता है, उस दौरान A के काम का ध्यान रखे बिना।",
  "qa-tw-a-fence-with-a-late-painter", _tw2,
  opts_hi=["10 घंटे", "11 घंटे", "12 घंटे", "15 घंटे"])

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    cs = [k for k in range(0, 91) if 2 * k - F(2, 3) * (90 - k) == 100]
    assert cs == [60]
    return str(cs[0])
N(QA, "Puzzle Hybrid", "medium",
  "In a test, a correct answer earns 2 marks and a wrong answer loses one-third of that (2/3 of a mark); unanswered questions earn nothing. A candidate answers 90 questions and scores 100. How many of the answers were correct?",
  "एक परीक्षा में सही उत्तर पर 2 अंक मिलते हैं और ग़लत उत्तर पर उसका एक-तिहाई (2/3 अंक) कटता है; छोड़े गए प्रश्नों पर कुछ नहीं मिलता। एक उम्मीदवार 90 प्रश्नों के उत्तर देता है और 100 अंक पाता है। कितने उत्तर सही थे?",
  ["50", "55", "60", "65"], 2,
  "With c correct, 90 - c are wrong: 2c - (2/3)(90 - c) = 100. Multiply by 3: 6c - 180 + 2c = 300, so 8c = 480 and c = 60 (60 correct earn 120, 30 wrong lose 20). "
  "50 assumes no deduction for wrong answers; 55 and 65 do not give 100.",
  "c सही हों तो 90 - c ग़लत हैं: 2c - (2/3)(90 - c) = 100। 3 से गुणा कीजिए: 6c - 180 + 2c = 300, अतः 8c = 480 और c = 60 (60 सही से 120 मिलते हैं, 30 ग़लत से 20 कटते हैं)। "
  "50 ग़लत उत्तरों पर कोई कटौती नहीं मानता; 55 और 65 से 100 नहीं आता।",
  "qa-ph-negative-marking", _ph1)

def _ph2():
    d = datetime.date(1947, 8, 15).strftime("%A")
    assert d == "Friday"
    return d
N(QA, "Puzzle Hybrid", "hard",
  "On which day of the week did 15 August 1947 fall?",
  "15 अगस्त 1947 सप्ताह के किस दिन पड़ा था?",
  ["Monday", "Wednesday", "Thursday", "Friday"], 3,
  "Count the odd days (days beyond whole weeks) from the start of the calendar. 1,600 years leave 0 odd days; the 300 years 1601-1900 leave 5 + 5 + 5 = 15, that is 1. The 46 years 1901-1946 hold 11 leap years (1904 to 1944), giving 46 + 11 = 57 odd days, that is 1. "
  "From 1 January to 15 August 1947 there are 31 + 28 + 31 + 30 + 31 + 30 + 31 + 15 = 227 days, that is 3 odd days. In all 0 + 1 + 1 + 3 = 5 odd days, and counting Sunday as 0, day 5 is Friday. Thursday comes from dropping one odd day, for example by treating 1900 as a leap year.",
  "पंचांग के आरंभ से विषम दिन (पूरे सप्ताहों के बाद बचे दिन) गिनिए। 1,600 वर्षों में 0 विषम दिन बचते हैं; 1601-1900 के 300 वर्षों में 5 + 5 + 5 = 15, यानी 1। 1901-1946 के 46 वर्षों में 11 लीप वर्ष (1904 से 1944) हैं, जिनसे 46 + 11 = 57 विषम दिन, यानी 1। "
  "1 जनवरी से 15 अगस्त 1947 तक 31 + 28 + 31 + 30 + 31 + 30 + 31 + 15 = 227 दिन हैं, यानी 3 विषम दिन। कुल 0 + 1 + 1 + 3 = 5 विषम दिन, और रविवार को 0 गिनने पर दिन 5 शुक्रवार है। गुरुवार एक विषम दिन छोड़ देने से आता है, उदाहरण के लिए 1900 को लीप वर्ष मानने से।",
  "qa-ph-the-weekday-of-15-august-1947", _ph2,
  opts_hi=["सोमवार", "बुधवार", "गुरुवार", "शुक्रवार"])

def _ph3():
    start, goal = (frozenset("FWGC"), frozenset()), (frozenset(), frozenset("FWGC"))
    def safe(bank):
        return "F" in bank or not ({"W", "G"} <= bank or {"G", "C"} <= bank)
    seen, q = {start: 0}, deque([start])
    while q:
        near, far = q.popleft()
        here, there = (near, far) if "F" in near else (far, near)
        for item in [None] + [x for x in here if x != "F"]:
            move = {"F"} | ({item} if item else set())
            h2, t2 = here - move, there | move
            nxt = (h2, t2) if "F" in near else (t2, h2)
            if safe(nxt[0]) and safe(nxt[1]) and nxt not in seen:
                seen[nxt] = seen[(near, far)] + 1
                q.append(nxt)
    return str(seen[goal])
N(QA, "Puzzle Hybrid", "hard",
  "A farmer must take a wolf, a goat and a basket of cabbages across a river in a boat that can carry only the farmer and one of the three. The wolf cannot be left alone with the goat, nor the goat alone with the cabbages. What is the least number of crossings, counting each one-way trip as one crossing?",
  "एक किसान को एक भेड़िया, एक बकरी और पत्तागोभी की एक टोकरी नदी के पार ले जानी है, एक ऐसी नाव में जिसमें केवल किसान और तीनों में से एक समा सकता है। भेड़िये को बकरी के साथ, और बकरी को पत्तागोभी के साथ अकेला नहीं छोड़ा जा सकता। कम से कम कितनी बार नदी पार करनी होगी, हर एक ओर की यात्रा को एक बार गिनते हुए?",
  ["5", "6", "7", "9"], 2,
  "The goat must cross first, since leaving it with either of the others is not allowed. The farmer returns, takes the wolf (or the cabbages) across, and must bring the goat back so that it is not left with the wolf; he then takes the cabbages (or the wolf) across, returns, and finally takes the goat: "
  "goat over, back, wolf over, goat back, cabbages over, back, goat over -- 7 crossings. 5 is impossible, since some item must make a return trip; 6 would end with the farmer on the wrong bank.",
  "बकरी को सबसे पहले जाना होगा, क्योंकि उसे किसी भी दूसरे के साथ छोड़ना वर्जित है। किसान लौटता है, भेड़िये (या पत्तागोभी) को पार ले जाता है, और बकरी को वापस लाना होता है ताकि वह भेड़िये के साथ न रहे; फिर वह पत्तागोभी (या भेड़िये) को पार ले जाता है, लौटता है, और अंत में बकरी को ले जाता है: "
  "बकरी पार, वापसी, भेड़िया पार, बकरी वापस, पत्तागोभी पार, वापसी, बकरी पार -- 7 बार। 5 असंभव है, क्योंकि किसी वस्तु को वापसी यात्रा करनी ही पड़ती है; 6 पर किसान ग़लत किनारे पर रह जाता।",
  "qa-ph-the-river-crossing", _ph3)

def _ph4():
    for n in range(1, 100):
        base = n * (n + 1) // 2
        if base < 1986 <= base + n:
            assert n == 62 and 1986 - base == 33
            return str(1986 - base)
N(QA, "Puzzle Hybrid", "medium",
  "The pages of a book are numbered 1, 2, 3, .... When the page numbers were added up, one of them was added twice by mistake, and the total came to 1,986. Which page number was added twice?",
  "एक पुस्तक के पृष्ठ 1, 2, 3, .... क्रमांकित हैं। पृष्ठ संख्याएँ जोड़ते समय उनमें से एक ग़लती से दो बार जुड़ गई, और कुल 1,986 आया। कौन-सी पृष्ठ संख्या दो बार जुड़ी?",
  ["33", "53", "62", "95"], 0,
  "The correct total for n pages is n(n + 1)/2, and the wrong total exceeds it by a page number between 1 and n. For n = 62 the correct total is 1,953, and 1,986 - 1,953 = 33, which is a page of the book. For n = 61 the total is 1,891, which would need an extra 95 -- more than the number of pages; for n = 63 it is 2,016, already above 1,986. "
  "So the book has 62 pages and page 33 was added twice. 62 is the number of pages; 95 is the excess for 61 pages; 53 has no basis.",
  "n पृष्ठों का सही योग n(n + 1)/2 है, और ग़लत योग उससे 1 और n के बीच की किसी पृष्ठ संख्या जितना अधिक है। n = 62 के लिए सही योग 1,953 है, और 1,986 - 1,953 = 33, जो पुस्तक का एक पृष्ठ है। n = 61 के लिए योग 1,891 है, जिसके लिए 95 अतिरिक्त चाहिए -- पृष्ठों की संख्या से अधिक; n = 63 के लिए वह 2,016 है, जो पहले ही 1,986 से अधिक है। "
  "अतः पुस्तक में 62 पृष्ठ हैं और पृष्ठ 33 दो बार जुड़ा। 62 पृष्ठों की संख्या है; 95, 61 पृष्ठों के लिए अतिरिक्त है; 53 का कोई आधार नहीं।",
  "qa-ph-a-page-number-added-twice", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    ns = range(1, 100000)
    s1 = {n % 9 == 0 for n in ns if sum(map(int, str(n))) == 27}
    s2 = {n % 9 == 0 for n in ns if n % 3 == 0 and (n // 3) % 3 == 0}
    both = s1 & s2
    assert s1 == {True} and s2 == {True}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "Is the natural number n divisible by 9?",
   "क्या प्राकृत संख्या n, 9 से विभाज्य है?",
   "The digits of n add up to 27.", "n के अंकों का योग 27 है।",
   "n = 3k, where k is a natural number divisible by 3.", "n = 3k, जहाँ k, 3 से विभाज्य एक प्राकृत संख्या है।",
   1,
   "Statement I: a number is divisible by 9 exactly when its digits add up to a multiple of 9, and 27 is one -- so n is divisible by 9. Statement II: k = 3j, so n = 9j -- again divisible by 9. Each statement alone answers the question, with a yes.",
   "कथन I: कोई संख्या 9 से तभी विभाज्य होती है जब उसके अंकों का योग 9 का गुणज हो, और 27 ऐसा है -- इसलिए n, 9 से विभाज्य है। कथन II: k = 3j, इसलिए n = 9j -- फिर से 9 से विभाज्य। हर कथन अकेले प्रश्न का उत्तर देता है, हाँ में।",
   "qa-ds-divisible-by-nine-two-ways", _ds1)

def _ds2():
    s1 = {n for b in range(3, 200) for n in [3 * (b - 2)]}                    # I: three to a bench leaves 2 benches empty
    s2 = {n for b in range(1, 200) for n in [2 * b + 4]}                      # II: two to a bench leaves 4 standing
    both = {3 * (b - 2) for b in range(3, 200) if 3 * (b - 2) == 2 * b + 4}
    assert both == {24}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "How many students are there in a class that has a fixed number of benches?",
   "जिस कक्षा में बेंचों की संख्या निश्चित है, उसमें कितने विद्यार्थी हैं?",
   "When the students sit three to a bench, two benches are left empty.", "जब विद्यार्थी एक बेंच पर तीन बैठते हैं, तो दो बेंचें ख़ाली रह जाती हैं।",
   "When they sit two to a bench, four students are left standing.", "जब वे एक बेंच पर दो बैठते हैं, तो चार विद्यार्थी खड़े रह जाते हैं।",
   2,
   "With b benches, Statement I gives n = 3(b - 2) and Statement II gives n = 2b + 4; each alone fits many classes (I: 3, 6, 9, ...; II: 6, 8, 10, ...). "
   "Together, 3b - 6 = 2b + 4, so b = 10 and n = 24 (check: 24 students fill 8 benches at three a bench and 10 benches leave 4 standing at two a bench). Both statements are needed.",
   "b बेंचों के साथ कथन I से n = 3(b - 2) और कथन II से n = 2b + 4 मिलता है; हर एक अकेला कई कक्षाओं पर बैठता है (I: 3, 6, 9, ...; II: 6, 8, 10, ...)। "
   "दोनों साथ: 3b - 6 = 2b + 4, अतः b = 10 और n = 24 (जाँच: एक बेंच पर तीन बैठने पर 24 विद्यार्थी 8 बेंचें भरते हैं, और एक बेंच पर दो बैठने पर 10 बेंचों के बाद 4 खड़े रहते हैं)। दोनों कथन ज़रूरी हैं।",
   "qa-ds-students-and-benches", _ds2)
