# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 2 -- Quantitative Aptitude (17 items: 16 in the Quant slots, 1 in the data-sufficiency block).

The half paper's share of Level 2's Quant mix (number theory 4, speed 2, percentage 2, ratio 2, work 1, counting 1,
geometry 1, series 1, puzzles 2, data sufficiency 1), at the foundation level: difficulty 5 easy / 9 medium / 3 hard.
None of Level 2's Quant shapes or Mini 1's is reused: the order of operations, a number as much above one value as below
another, the squares between 100 and 1,000, successive division; an overnight train, walking one way and riding back;
a population two years ago, copies needed to break even; the fourth proportional, an expression from a ratio; work rates
from parts of a job; at least one head in three tosses; the surface area gained by cutting a cube into small cubes;
a letter series with growing gaps; a bouncing ball's total path, the weekday of a New Year's Day two years on; and a
cost price that one statement settles. The rows are written in the order they take on the paper, and every key is
worked out in code by check()."""
import datetime as dt
from fractions import Fraction as F
from itertools import product
from csat_common import N, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- the order of operations
def _ops():
    v = 48 / 6 * 2 + 3 * (4 - 1)
    assert 48 / (6 * 2) + 3 * 3 == 13 and 48 / 6 * 2 + 3 * 4 - 1 == 27 and (48 / 6 * 2 + 3) * (4 - 1) == 57
    return str(int(v))
N(QA, "Number Theory", "easy",
  "What is the value of 48 ÷ 6 × 2 + 3 × (4 - 1)?",
  "48 ÷ 6 × 2 + 3 × (4 - 1) का मान क्या है?",
  ["13", "25", "27", "57"], 1,
  "Work out the bracket first: 4 - 1 = 3. Division and multiplication come next, from left to right: 48 ÷ 6 = 8, then 8 × 2 = 16, and 3 × 3 = 9. Addition comes last: 16 + 9 = 25. "
  "13 multiplies 6 × 2 before dividing (48 ÷ 12 = 4, + 9), which breaks the left-to-right rule; 27 ignores the bracket (16 + 3 × 4 - 1); 57 adds before multiplying ((16 + 3) × 3).",
  "पहले कोष्ठक हल कीजिए: 4 - 1 = 3। फिर भाग और गुणा, बाएँ से दाएँ: 48 ÷ 6 = 8, फिर 8 × 2 = 16, और 3 × 3 = 9। जोड़ अंत में: 16 + 9 = 25। "
  "13, भाग देने से पहले 6 × 2 कर लेता है (48 ÷ 12 = 4, + 9), जो बाएँ से दाएँ के नियम को तोड़ता है; 27 कोष्ठक की अनदेखी करता है (16 + 3 × 4 - 1); 57 गुणा से पहले जोड़ देता है ((16 + 3) × 3)।",
  "qa-nt-the-order-of-operations", _ops)

# 2 -- a letter series with growing gaps
def _letters():
    s = "ACFJO"
    gaps = [ord(b) - ord(a) for a, b in zip(s, s[1:])]
    assert gaps == [2, 3, 4, 5]
    return chr(ord(s[-1]) + gaps[-1] + 1)
N(QA, "Sequences & Series", "medium",
  "Which letter comes next in the series A, C, F, J, O, ... ?",
  "श्रेणी A, C, F, J, O, ... में अगला अक्षर कौन-सा है?",
  ["R", "S", "T", "U"], 3,
  "The gaps between the letters grow by one each time: A to C is 2 places, C to F is 3, F to J is 4 and J to O is 5. The next gap is 6, and 6 places after O (the 15th letter) is U (the 21st). "
  "T repeats the last gap of 5, S repeats a gap of 4, and R moves on by only 3.",
  "अक्षरों के बीच का अंतर हर बार एक बढ़ता है: A से C, 2 स्थान; C से F, 3; F से J, 4 और J से O, 5। अगला अंतर 6 है, और O (15वाँ अक्षर) से 6 स्थान आगे U (21वाँ) है। "
  "T अंतिम अंतर 5 को दोहराता है, S अंतर 4 को, और R केवल 3 स्थान आगे बढ़ता है।",
  "qa-ss-a-letter-series-with-growing-gaps", _letters)

# 4 -- copies needed to break even
def _even():
    n = next(k for k in range(1, 10000) if 25 * k >= 2000 + 15 * k)
    assert 2000 / 25 == 80 and 2000 / 40 == 50 and -(-2000 // 15) == 134
    return str(n)
N(QA, "Percentage & Profit-Loss", "medium",
  "A small press spends ₹2,000 to set up a printing job and ₹15 on paper and ink for each copy it prints. It sells each copy for ₹25. How many copies must it print and sell to cover its costs exactly?",
  "एक छोटा छापाख़ाना किसी छपाई के काम को तैयार करने पर ₹2,000 और छापी गई हर प्रति के काग़ज़ व स्याही पर ₹15 ख़र्च करता है। वह हर प्रति ₹25 में बेचता है। अपनी लागत ठीक-ठीक निकालने के लिए उसे कितनी प्रतियाँ छापकर बेचनी होंगी?",
  ["50", "80", "134", "200"], 3,
  "Each copy sold brings in ₹25 and costs ₹15, so it leaves ₹10 towards the set-up cost of ₹2,000. The press breaks even after 2,000 ÷ 10 = 200 copies (200 × 25 = ₹5,000 = 2,000 + 200 × 15). "
  "80 divides the set-up cost by the price and forgets the ₹15 that each copy costs; 134 divides it by the cost of a copy; 50 divides it by the price and the cost added together.",
  "बेची गई हर प्रति ₹25 लाती है और उस पर ₹15 लगता है, इसलिए वह ₹2,000 की तैयारी-लागत के लिए ₹10 छोड़ती है। छापाख़ाना 2,000 ÷ 10 = 200 प्रतियों के बाद लागत निकाल लेता है (200 × 25 = ₹5,000 = 2,000 + 200 × 15)। "
  "80 तैयारी-लागत को मूल्य से भाग देता है और हर प्रति पर लगने वाले ₹15 भूल जाता है; 134 उसे एक प्रति की लागत से भाग देता है; 50 उसे मूल्य और लागत के योग से भाग देता है।",
  "qa-pp-copies-needed-to-break-even", _even)

# 8 -- successive division
def _succ():
    rs = {n % 20 for n in range(1, 2000) if n % 4 == 3 and (n // 4) % 5 == 2}
    assert rs == {11} and (5 * 3 + 2) % 20 == 17
    return str(rs.pop())
N(QA, "Number Theory", "hard",
  "A number leaves a remainder of 3 when it is divided by 4. The quotient so obtained leaves a remainder of 2 when it is divided by 5. What is the remainder when the number is divided by 20?",
  "एक संख्या को 4 से भाग देने पर शेषफल 3 आता है। इस प्रकार मिले भागफल को 5 से भाग देने पर शेषफल 2 आता है। संख्या को 20 से भाग देने पर शेषफल क्या होगा?",
  ["5", "6", "11", "17"], 2,
  "Let the number be 4q + 3, where the quotient q = 5k + 2. Then the number is 4(5k + 2) + 3 = 20k + 11, so the remainder on division by 20 is 11 (for example, 11, 31 and 51 all fit). "
  "5 adds the two remainders and 6 multiplies them; 17 combines them the wrong way round, as 5 × 3 + 2.",
  "मान लीजिए संख्या 4q + 3 है, जहाँ भागफल q = 5k + 2। तब संख्या 4(5k + 2) + 3 = 20k + 11 है, अतः 20 से भाग देने पर शेषफल 11 है (उदाहरण के लिए 11, 31 और 51 सभी शर्तें पूरी करती हैं)। "
  "5 दोनों शेषफलों को जोड़ता है और 6 उन्हें गुणा करता है; 17 उन्हें उलटे क्रम में जोड़ता है, 5 × 3 + 2 के रूप में।",
  "qa-nt-successive-division", _succ)

# 10 -- a population two years ago
def _pop():
    now = 12100
    then = F(now) / F(11, 10) ** 2
    assert then == 10000 and now * F(81, 100) == 9801 and now * F(8, 10) == 9680 and F(now) / F(11, 10) == 11000
    return f"{int(then):,}"
N(QA, "Percentage & Profit-Loss", "easy",
  "The population of a town grows by 10 per cent every year. It is 12,100 now. What was it two years ago?",
  "एक कस्बे की जनसंख्या हर वर्ष 10 प्रतिशत बढ़ती है। अभी वह 12,100 है। दो वर्ष पहले वह कितनी थी?",
  ["9,680", "9,801", "10,000", "11,000"], 2,
  "Each year the population is multiplied by 1.1, so two years ago it was 12,100 ÷ 1.1 ÷ 1.1 = 12,100 ÷ 1.21 = 10,000 (10,000 → 11,000 → 12,100). "
  "11,000 is the population one year ago; 9,801 takes 10 per cent off twice, but a 10 per cent rise is undone by dividing by 1.1, not by taking 10 per cent off; 9,680 takes 20 per cent off at once.",
  "हर वर्ष जनसंख्या 1.1 से गुणा होती है, इसलिए दो वर्ष पहले वह 12,100 ÷ 1.1 ÷ 1.1 = 12,100 ÷ 1.21 = 10,000 थी (10,000 → 11,000 → 12,100)। "
  "11,000 एक वर्ष पहले की जनसंख्या है; 9,801 दो बार 10 प्रतिशत घटाता है, पर 10 प्रतिशत वृद्धि 1.1 से भाग देकर उलटती है, 10 प्रतिशत घटाकर नहीं; 9,680 एक साथ 20 प्रतिशत घटाता है।",
  "qa-pp-a-population-two-years-ago", _pop)

# 11 -- work rates from parts of a job
def _parts():
    a = F(3) / F(1, 4)                 # 1/4 of the job in 3 days
    b = F(8) / F(1, 3)                 # 1/3 of the job in 8 days
    t = 1 / (1 / a + 1 / b)
    assert (a, b) == (12, 24) and (a + b) / 2 == 18 and a + b == 36
    return str(t)
N(QA, "Time & Work", "medium",
  "A can do one-fourth of a job in 3 days, and B can do one-third of it in 8 days. Working together, in how many days can A and B finish the whole job?",
  "A किसी काम का एक-चौथाई भाग 3 दिनों में कर सकता है, और B उसका एक-तिहाई भाग 8 दिनों में। साथ काम करते हुए A और B पूरा काम कितने दिनों में समाप्त कर सकते हैं?",
  ["8", "11", "18", "36"], 0,
  "A does a quarter in 3 days, so the whole job alone in 12 days; B does a third in 8 days, so the whole job in 24 days. Together they do 1/12 + 1/24 = 3/24 = 1/8 of the job a day, and finish it in 8 days. "
  "11 adds the 3 and the 8 days given for the parts; 18 is the average of 12 and 24 days, and 36 their sum -- times for a whole job cannot be averaged or added.",
  "A एक-चौथाई भाग 3 दिनों में करता है, यानी अकेले पूरा काम 12 दिनों में; B एक-तिहाई भाग 8 दिनों में करता है, यानी पूरा काम 24 दिनों में। साथ मिलकर वे प्रतिदिन 1/12 + 1/24 = 3/24 = 1/8 काम करते हैं, और उसे 8 दिनों में पूरा करते हैं। "
  "11, भागों के लिए दिए 3 और 8 दिनों को जोड़ता है; 18, 12 और 24 दिनों का औसत है, और 36 उनका योग -- पूरे काम के समयों का औसत या योग नहीं लिया जा सकता।",
  "qa-tw-work-rates-from-parts-of-a-job", _parts)

# 16 -- the surface area gained by cutting a cube into small cubes
def _cube():
    big = 6 * 4 ** 2
    small = 4 ** 3 * 6 * 1 ** 2
    assert (big, small) == (96, 384)
    return f"{small // big} times"
N(QA, "Geometry & Mensuration", "medium",
  "A solid cube of side 4 cm is cut into small cubes of side 1 cm. The total surface area of all the small cubes together is how many times the surface area of the original cube?",
  "4 सेमी भुजा वाले एक ठोस घन को 1 सेमी भुजा वाले छोटे घनों में काटा जाता है। सभी छोटे घनों का कुल पृष्ठीय क्षेत्रफल मूल घन के पृष्ठीय क्षेत्रफल का कितना गुना है?",
  ["4 times", "6 times", "16 times", "64 times"], 0,
  "The original cube has a surface area of 6 × 4² = 96 cm². It makes 4³ = 64 small cubes, each with a surface area of 6 × 1² = 6 cm², so together they have 64 × 6 = 384 cm², which is 384 ÷ 96 = 4 times as much. "
  "64 times is the number of small cubes, which counts each small cube as if it had as much surface as the big one; 16 times is the ratio of the face areas (4² to 1²); 6 times confuses the number of faces with the answer.",
  "मूल घन का पृष्ठीय क्षेत्रफल 6 × 4² = 96 वर्ग सेमी है। उससे 4³ = 64 छोटे घन बनते हैं, जिनमें से हर एक का पृष्ठीय क्षेत्रफल 6 × 1² = 6 वर्ग सेमी है, इसलिए सबका योग 64 × 6 = 384 वर्ग सेमी है, जो 384 ÷ 96 = 4 गुना है। "
  "64 गुना छोटे घनों की संख्या है, जो हर छोटे घन को बड़े घन जितने पृष्ठ वाला मान लेता है; 16 गुना फलकों के क्षेत्रफलों का अनुपात है (4² और 1²); 6 गुना फलकों की संख्या को उत्तर मान लेता है।",
  "qa-gm-cutting-a-cube-into-small-cubes", _cube,
  opts_hi=["4 गुना", "6 गुना", "16 गुना", "64 गुना"])

# 17 -- an overnight train
def _train():
    leave, arrive = dt.datetime(2026, 1, 1, 22, 45), dt.datetime(2026, 1, 2, 6, 15)
    hours = F(int((arrive - leave).total_seconds()), 3600)
    assert hours == F(15, 2) and F(525) / 7 == 75 and F(525) / F(25, 4) == 84
    return f"{F(525) / hours} km/h"
N(QA, "Speed-Distance-Time", "easy",
  "A train leaves a station at 10:45 p.m. and reaches its destination, 525 km away, at 6:15 a.m. the next day. What is its average speed?",
  "एक ट्रेन रात 10:45 बजे एक स्टेशन से चलती है और 525 किमी दूर अपने गंतव्य पर अगले दिन सुबह 6:15 बजे पहुँचती है। उसकी औसत चाल क्या है?",
  ["60 km/h", "70 km/h", "75 km/h", "84 km/h"], 1,
  "From 10:45 p.m. to midnight is 1 hour 15 minutes, and from midnight to 6:15 a.m. is 6 hours 15 minutes: 7 hours 30 minutes in all. The average speed is 525 ÷ 7.5 = 70 km/h. "
  "75 km/h drops the half hour (525 ÷ 7); 84 km/h takes the arrival time, 6 hours 15 minutes, as the length of the journey (525 ÷ 6.25); 60 km/h would need a journey of 8 hours 45 minutes.",
  "रात 10:45 से आधी रात तक 1 घंटा 15 मिनट है, और आधी रात से सुबह 6:15 तक 6 घंटे 15 मिनट: कुल 7 घंटे 30 मिनट। औसत चाल 525 ÷ 7.5 = 70 किमी/घंटा है। "
  "75 किमी/घंटा आधा घंटा छोड़ देता है (525 ÷ 7); 84 किमी/घंटा पहुँचने के समय 6 घंटे 15 मिनट को यात्रा की अवधि मान लेता है (525 ÷ 6.25); 60 किमी/घंटा के लिए 8 घंटे 45 मिनट की यात्रा चाहिए।",
  "qa-sdt-an-overnight-train", _train,
  opts_hi=["60 किमी/घंटा", "70 किमी/घंटा", "75 किमी/घंटा", "84 किमी/घंटा"])

# 21 -- the squares between 100 and 1,000
def _squares():
    n = sum(1 for k in range(1, 100) if 100 < k * k < 1000)
    assert sum(1 for k in range(1, 100) if 100 <= k * k < 1000) == 22 and sum(1 for k in range(1, 100) if k * k < 1000) == 31
    return str(n)
N(QA, "Number Theory", "medium",
  "How many perfect squares are greater than 100 and less than 1,000?",
  "कितने पूर्ण वर्ग 100 से बड़े और 1,000 से छोटे हैं?",
  ["20", "21", "22", "31"], 1,
  "100 = 10² is not greater than 100, so the first square counted is 11² = 121. 31² = 961 is below 1,000 but 32² = 1,024 is not, so the last is 31². The squares from 11² to 31² number 31 - 11 + 1 = 21. "
  "22 counts 100 itself; 20 subtracts 11 from 31 without adding one back; 31 counts every square below 1,000, from 1² up.",
  "100 = 10², 100 से बड़ा नहीं है, इसलिए गिना जाने वाला पहला वर्ग 11² = 121 है। 31² = 961, 1,000 से छोटा है पर 32² = 1,024 नहीं, इसलिए अंतिम 31² है। 11² से 31² तक के वर्ग 31 - 11 + 1 = 21 हैं। "
  "22, 100 को भी गिन लेता है; 20, 31 में से 11 घटाकर एक नहीं जोड़ता; 31, 1² से शुरू करके 1,000 से नीचे के हर वर्ग को गिनता है।",
  "qa-nt-the-squares-between-100-and-1000", _squares)

# 22 -- walking one way and riding back
def _walk():
    walk_one = F(5, 2)                 # walking both ways takes 5 hours
    ride_one = F(7, 2) - walk_one      # walking one way and riding back takes 3 1/2 hours
    assert ride_one == 1 and 5 - F(7, 2) == F(3, 2) and F(7, 2) / 2 == F(7, 4)
    return f"{int(2 * ride_one)} h"
N(QA, "Speed-Distance-Time", "hard",
  "A man walks to his office and comes back home by bus, taking 3 hours 30 minutes in all. If he walked both ways, he would take 5 hours. How long would he take if he went both ways by bus?",
  "एक व्यक्ति अपने कार्यालय पैदल जाता है और बस से घर लौटता है, जिसमें कुल 3 घंटे 30 मिनट लगते हैं। यदि वह दोनों ओर पैदल जाए, तो उसे 5 घंटे लगेंगे। यदि वह दोनों ओर बस से जाए, तो उसे कितना समय लगेगा?",
  ["1 h", "1 h 30 min", "1 h 45 min", "2 h"], 3,
  "Walking both ways takes 5 hours, so walking one way takes 2 hours 30 minutes. Walking one way and riding back takes 3 hours 30 minutes, so the bus ride one way takes 3 h 30 min - 2 h 30 min = 1 hour, and both ways by bus take 2 hours. "
  "1 hour is the bus ride one way only; 1 hour 30 minutes subtracts the two given times (5 h - 3 h 30 min); 1 hour 45 minutes halves the mixed journey, as if walking and riding took equally long.",
  "दोनों ओर पैदल जाने में 5 घंटे लगते हैं, इसलिए एक ओर पैदल 2 घंटे 30 मिनट लगते हैं। एक ओर पैदल और लौटते समय बस में 3 घंटे 30 मिनट लगते हैं, इसलिए एक ओर की बस यात्रा 3 घंटे 30 मिनट - 2 घंटे 30 मिनट = 1 घंटा है, और दोनों ओर बस से 2 घंटे लगेंगे। "
  "1 घंटा केवल एक ओर की बस यात्रा है; 1 घंटा 30 मिनट दिए गए दोनों समयों को घटाता है (5 घंटे - 3 घंटे 30 मिनट); 1 घंटा 45 मिनट मिली-जुली यात्रा को आधा करता है, मानो पैदल और बस में बराबर समय लगता हो।",
  "qa-sdt-walking-one-way-and-riding-back", _walk,
  opts_hi=["1 घंटा", "1 घंटा 30 मिनट", "1 घंटा 45 मिनट", "2 घंटे"])

# 24 -- an expression from a ratio
def _expr():
    a, b = F(3), F(4)
    r = (5 * a - 2 * b) / (5 * a + 2 * b)
    assert r == F(7, 23) and F(5 - 2, 5 + 2) == F(3, 7)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "If a : b = 3 : 4, what is the value of (5a - 2b) : (5a + 2b)?",
  "यदि a : b = 3 : 4, तो (5a - 2b) : (5a + 2b) का मान क्या है?",
  ["3 : 7", "15 : 8", "23 : 7", "7 : 23"], 3,
  "Put a = 3k and b = 4k: 5a - 2b = 15k - 8k = 7k and 5a + 2b = 15k + 8k = 23k, so the ratio is 7 : 23. "
  "23 : 7 turns the answer upside down; 15 : 8 is 5a : 2b; 3 : 7 drops a and b and keeps only the numbers (5 - 2) : (5 + 2).",
  "a = 3k और b = 4k रखिए: 5a - 2b = 15k - 8k = 7k और 5a + 2b = 15k + 8k = 23k, अतः अनुपात 7 : 23 है। "
  "23 : 7 उत्तर को उलट देता है; 15 : 8, 5a : 2b है; 3 : 7, a और b को छोड़कर केवल संख्याएँ (5 - 2) : (5 + 2) रखता है।",
  "qa-rm-an-expression-from-a-ratio", _expr)

# 30 -- at least one head in three tosses
def _heads():
    outcomes = list(product("HT", repeat=3))
    p = F(sum(1 for o in outcomes if "H" in o), len(outcomes))
    assert F(sum(1 for o in outcomes if o.count("H") == 1), 8) == F(3, 8)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "medium",
  "Three fair coins are tossed together. What is the probability of getting at least one head?",
  "तीन न्यायसंगत सिक्के एक साथ उछाले जाते हैं। कम से कम एक चित (head) आने की प्रायिकता क्या है?",
  ["3/8", "1/2", "3/4", "7/8"], 3,
  "Three coins give 2³ = 8 equally likely outcomes. Only one of them, tail-tail-tail, has no head, so the probability of at least one head is 1 - 1/8 = 7/8. "
  "3/8 is the chance of exactly one head; 3/4 is the chance of at least one head with two coins; 1/2 is the chance of a head on a single coin.",
  "तीन सिक्कों से 2³ = 8 समान रूप से संभव परिणाम मिलते हैं। उनमें से केवल एक, पट-पट-पट, में कोई चित नहीं है, इसलिए कम से कम एक चित की प्रायिकता 1 - 1/8 = 7/8 है। "
  "3/8 ठीक एक चित की प्रायिकता है; 3/4 दो सिक्कों में कम से कम एक चित की प्रायिकता है; 1/2 एक सिक्के पर चित की प्रायिकता है।",
  "qa-pc-at-least-one-head-in-three-tosses", _heads)

# 32 -- a number as much above one value as below another
def _mid():
    x = F(36 + 86, 2)
    assert x - 36 == 86 - x
    return str(x)
N(QA, "Number Theory", "easy",
  "A number is as much greater than 36 as it is less than 86. What is the number?",
  "एक संख्या 36 से उतनी ही अधिक है जितनी वह 86 से कम है। वह संख्या क्या है?",
  ["61", "72", "86", "122"], 0,
  "If the number is x, then x - 36 = 86 - x, so 2x = 122 and x = 61 -- the number halfway between 36 and 86 (61 - 36 = 25 = 86 - 61). "
  "122 is the sum of 36 and 86, not half of it; 72 doubles 36; 86 is the upper value itself.",
  "यदि संख्या x है, तो x - 36 = 86 - x, अतः 2x = 122 और x = 61 -- यानी 36 और 86 के ठीक बीच की संख्या (61 - 36 = 25 = 86 - 61)। "
  "122, 36 और 86 का योग है, उसका आधा नहीं; 72, 36 को दुगुना करता है; 86 स्वयं ऊपरी मान है।",
  "qa-nt-as-much-above-one-value-as-below-another", _mid)

# 37 -- a bouncing ball's total path
def _ball():
    h, total = F(32), F(32)
    for _ in range(200):               # each bounce goes up and comes down again
        h /= 2
        total += 2 * h
    assert abs(total - 96) < F(1, 10 ** 9) and 32 + 16 == 48 and 32 + 16 + 8 + 4 + 2 + 1 < 64
    return "96"
N(QA, "Puzzle Hybrid", "hard",
  "A ball is dropped from a height of 32 m. Each time it hits the ground, it bounces back up to half the height from which it fell, and it goes on bouncing in this way. What is the total distance it travels, up and down, before it comes to rest?",
  "एक गेंद को 32 मी की ऊँचाई से गिराया जाता है। हर बार ज़मीन से टकराने पर वह उस ऊँचाई की आधी ऊँचाई तक वापस उछलती है जिससे वह गिरी थी, और इसी तरह उछलती रहती है। रुकने से पहले वह ऊपर और नीचे कुल कितनी दूरी तय करती है?",
  ["48 m", "64 m", "96 m", "128 m"], 2,
  "The first fall is 32 m. After that the ball rises 16 m and falls 16 m, rises 8 m and falls 8 m, and so on. The rises add up to 16 + 8 + 4 + ... = 32 m, and so do the falls after the first, so the total is 32 + 32 + 32 = 96 m. "
  "64 m counts the falls only (32 + 16 + 8 + ...); 48 m stops after the first bounce (32 + 16); 128 m counts the first drop twice as well, as if the ball had also been thrown up to 32 m.",
  "पहली गिरावट 32 मी है। उसके बाद गेंद 16 मी उठती और 16 मी गिरती है, 8 मी उठती और 8 मी गिरती है, और इसी तरह। उठानों का योग 16 + 8 + 4 + ... = 32 मी है, और पहली के बाद की गिरावटों का भी, इसलिए कुल 32 + 32 + 32 = 96 मी है। "
  "64 मी केवल गिरावटें गिनता है (32 + 16 + 8 + ...); 48 मी पहली उछाल के बाद रुक जाता है (32 + 16); 128 मी पहली गिरावट को भी दो बार गिनता है, मानो गेंद पहले 32 मी ऊपर भी फेंकी गई हो।",
  "qa-ph-a-bouncing-ball-s-total-path", lambda: _ball() + " m",
  opts_hi=["48 मी", "64 मी", "96 मी", "128 मी"])

# 38 -- the weekday of a New Year's Day two years on
def _cal():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    assert days[dt.date(2027, 1, 1).weekday()] == "Friday" and days[dt.date(2028, 1, 1).weekday()] == "Saturday"
    return days[dt.date(2029, 1, 1).weekday()]
N(QA, "Puzzle Hybrid", "medium",
  "1 January 2027 is a Friday. On which day of the week will 1 January 2029 fall?",
  "1 जनवरी 2027 को शुक्रवार है। 1 जनवरी 2029 को सप्ताह का कौन-सा दिन होगा?",
  ["Saturday", "Sunday", "Monday", "Tuesday"], 2,
  "A year of 365 days is 52 weeks and 1 day, so the same date falls one weekday later the next year; a leap year of 366 days moves it on by two. 2027 is an ordinary year, so 1 January 2028 is a Saturday. "
  "2028 is a leap year (it has a 29 February), so 1 January 2029 is two days after Saturday: a Monday. Sunday forgets that 2028 is a leap year; Saturday moves on only one year; Tuesday counts two leap years.",
  "365 दिनों का वर्ष 52 सप्ताह और 1 दिन होता है, इसलिए अगले वर्ष वही तारीख़ एक दिन आगे पड़ती है; 366 दिनों का अधिवर्ष उसे दो दिन आगे ले जाता है। 2027 सामान्य वर्ष है, इसलिए 1 जनवरी 2028 को शनिवार है। "
  "2028 अधिवर्ष है (उसमें 29 फ़रवरी है), इसलिए 1 जनवरी 2029 शनिवार से दो दिन बाद होगा: सोमवार। रविवार यह भूल जाता है कि 2028 अधिवर्ष है; शनिवार केवल एक वर्ष आगे बढ़ता है; मंगलवार दो अधिवर्ष गिन लेता है।",
  "qa-ph-new-year-s-day-two-years-on", _cal,
  opts_hi=["शनिवार", "रविवार", "सोमवार", "मंगलवार"])

# 40 -- the fourth proportional
def _fourth():
    x = F(9 * 12, 4)
    assert F(4, 9) == F(12, x)
    return str(x)
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "What is the fourth proportional to 4, 9 and 12?",
  "4, 9 और 12 का चतुर्थानुपाती क्या है?",
  ["18", "21", "24", "27"], 3,
  "The fourth proportional x satisfies 4 : 9 = 12 : x, so 4x = 9 × 12 = 108 and x = 27 (12 is three times 4, so x is three times 9). "
  "24 doubles 12 instead of following the ratio; 18 doubles 9; 21 adds 9 and 12.",
  "चतुर्थानुपाती x के लिए 4 : 9 = 12 : x, अतः 4x = 9 × 12 = 108 और x = 27 (12, 4 का तीन गुना है, इसलिए x, 9 का तीन गुना है)। "
  "24, अनुपात के बजाय 12 को दुगुना करता है; 18, 9 को दुगुना करता है; 21, 9 और 12 को जोड़ता है।",
  "qa-rm-the-fourth-proportional", _fourth)

# ---- the data-sufficiency block's Quant item
def _ds1():
    costs = range(100, 1001)
    s1 = [c for c in costs if F(c) * F(6, 5) == 540]                     # sold at ₹540, a 20% profit
    s2 = [c for c in costs if True]                                        # the profit is ₹90: any cost works
    both = [c for c in s1 if c + 90 == 540]
    assert s1 == [450] and both == [450]
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the cost price of an article?",
   "एक वस्तु का क्रय मूल्य क्या है?",
   "The article was sold for ₹540 at a profit of 20 per cent.",
   "वस्तु ₹540 में 20 प्रतिशत लाभ पर बेची गई।",
   "The article's selling price was ₹90 more than its cost price.",
   "वस्तु का विक्रय मूल्य उसके क्रय मूल्य से ₹90 अधिक था।",
   0,
   "Statement I: the selling price is 120 per cent of the cost, so the cost is ₹540 ÷ 1.2 = ₹450 -- sufficient. Statement II gives only the profit, ₹90, which fits any cost price -- not sufficient. "
   "(The two agree: ₹540 - ₹450 = ₹90.) Statement I alone answers the question, but II alone does not.",
   "कथन I: विक्रय मूल्य लागत का 120 प्रतिशत है, अतः लागत ₹540 ÷ 1.2 = ₹450 है -- पर्याप्त। कथन II केवल लाभ, ₹90, बताता है, जो किसी भी क्रय मूल्य के साथ बैठ सकता है -- पर्याप्त नहीं। "
   "(दोनों मेल खाते हैं: ₹540 - ₹450 = ₹90।) कथन I अकेले प्रश्न का उत्तर देता है, पर II अकेले नहीं।",
   "qa-ds-a-cost-price-one-statement-settles", _ds1)
