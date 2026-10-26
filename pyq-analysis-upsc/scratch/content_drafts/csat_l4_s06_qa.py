# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 6 -- Quantitative Aptitude (37 items: 35 in the Quant slots, 2 in the data-sufficiency block).

Layout C, the 2026 shape: Quant-heavy, number theory the largest bucket (10). Exam-level mix (9 easy / 17 medium /
11 hard), with none of the shapes of Levels 1-3 or Simulators 1-5: two-digit numbers whose tens digit is the larger,
the LCM of three fractions, a fraction within a fraction, the average of the first ten multiples of 7, three
consecutive multiples of 9, what always divides n² + 3 for odd n, the smallest number whose digits multiply to 100, a
fraction found from two changes, √50 + √18, the two-digit squares and cubes added; a jogger round a park, a voyage
counted in days, a ferry's round trips, a walk along a moving train; seats shared by the largest remainder, marks
scaled to a top of 100, a recipe by cups turned into weight, a ratio from a sum and a difference; a price that covers
spoilage, 20 per cent extra or 20 per cent off, simple interest at changing rates; each term the sum of the three
before, the number of terms in an AP; a necklace of six beads, two dice that differ by 2, a first six on the third
roll; a cone beside a cylinder, the tops of two poles, a sector rolled into a cone; a well that gets harder to dig,
two cooks and a hundred rotis; an age equal to the digit sum of a birth year, the 100th day of 2027, seventeen camels
and a borrowed one, a bookworm through three volumes; and two data-sufficiency items. Every key is worked out in code
by check()."""
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
    n = sum(1 for k in range(10, 100) if k // 10 > k % 10)
    assert n == math.comb(10, 2)
    return str(n)
N(QA, "Number Theory", "medium",
  "How many two-digit numbers have a tens digit greater than their units digit (as in 52 or 90)?",
  "दो अंकों की कितनी संख्याओं का दहाई का अंक इकाई के अंक से बड़ा है (जैसे 52 या 90 में)?",
  ["36", "45", "54", "90"], 1,
  "Any two different digits from 0 to 9 give exactly one such number: put the larger first. The larger can never be 0, so every choice works, and there are 10C2 = 45 of them. "
  "36 = 9C2 leaves out the numbers that end in 0, such as 90; 90 is every two-digit number; 54 has no basis.",
  "0 से 9 तक के कोई भी दो अलग अंक ठीक एक ऐसी संख्या देते हैं: बड़े को पहले रखिए। बड़ा अंक कभी 0 नहीं हो सकता, इसलिए हर चुनाव चलता है, और ऐसे 10C2 = 45 हैं। "
  "36 = 9C2, 0 पर समाप्त होने वाली संख्याओं, जैसे 90, को छोड़ देता है; 90 दो अंकों की सभी संख्याएँ हैं; 54 का कोई आधार नहीं।",
  "qa-nt-two-digit-numbers-whose-tens-digit-is-larger", _nt1)

def _nt2():
    fr = [F(4, 5), F(6, 7), F(10, 21)]
    best = min(F(n, d) for d in range(1, 30) for n in range(1, 2000)
               if all((F(n, d) / f).denominator == 1 for f in fr))
    assert best == F(math.lcm(4, 6, 10), math.gcd(5, 7, 21))
    return str(best)
N(QA, "Number Theory", "hard",
  "What is the LCM of the fractions 4/5, 6/7 and 10/21 -- the smallest positive number that is a whole-number multiple of each?",
  "भिन्नों 4/5, 6/7 और 10/21 का LCM क्या है -- वह सबसे छोटी धनात्मक संख्या जो हर एक का पूर्ण-संख्या गुणज हो?",
  ["2/105", "4/7", "60", "120"], 2,
  "The LCM of fractions is the LCM of the numerators over the HCF of the denominators: LCM(4, 6, 10) = 60 and HCF(5, 7, 21) = 1, giving 60. Check: 60 is 75 × 4/5, 70 × 6/7 and 126 × 10/21. "
  "2/105 is the HCF of the fractions (HCF of the numerators over the LCM of the denominators); 4/7 divides 60 by the LCM of the denominators, 105, instead of their HCF; 120 is a common multiple but not the least.",
  "भिन्नों का LCM अंशों का LCM बटा हरों का HCF होता है: LCM(4, 6, 10) = 60 और HCF(5, 7, 21) = 1, जिससे 60 मिलता है। जाँच: 60 = 75 × 4/5, 70 × 6/7 और 126 × 10/21। "
  "2/105 भिन्नों का HCF है (अंशों का HCF बटा हरों का LCM); 4/7, 60 को हरों के HCF के बजाय उनके LCM, 105, से भाग देता है; 120 एक सार्व गुणज है पर सबसे छोटा नहीं।",
  "qa-nt-the-lcm-of-three-fractions", _nt2)

def _nt3():
    v = 1 + 1 / (1 + 1 / (1 + F(1, 2)))
    return f"{v.numerator}/{v.denominator}"
N(QA, "Number Theory", "medium",
  "What is the value of 1 + 1/(1 + 1/(1 + 1/2))?",
  "1 + 1/(1 + 1/(1 + 1/2)) का मान क्या है?",
  ["3/2", "8/5", "13/8", "5/3"], 1,
  "Work from the inside out: 1 + 1/2 = 3/2; then 1 + 1/(3/2) = 1 + 2/3 = 5/3; then 1 + 1/(5/3) = 1 + 3/5 = 8/5. "
  "3/2 and 5/3 stop one or two steps too soon; 13/8 goes one step too far. (The options are in order of size.)",
  "भीतर से बाहर की ओर चलिए: 1 + 1/2 = 3/2; फिर 1 + 1/(3/2) = 1 + 2/3 = 5/3; फिर 1 + 1/(5/3) = 1 + 3/5 = 8/5। "
  "3/2 और 5/3 एक या दो चरण पहले रुक जाते हैं; 13/8 एक चरण आगे चला जाता है। (विकल्प आकार के क्रम में हैं।)",
  "qa-nt-a-fraction-within-a-fraction", _nt3)

def _nt4():
    return str(F(sum(7 * k for k in range(1, 11)), 10)).replace("77/2", "38.5")
N(QA, "Number Theory", "easy",
  "What is the average of the first ten multiples of 7 (7, 14, ..., 70)?",
  "7 के पहले दस गुणजों (7, 14, ..., 70) का औसत क्या है?",
  ["38.5", "42", "49", "385"], 0,
  "The multiples are evenly spaced, so their average is the average of the first and last: (7 + 70) ÷ 2 = 38.5. "
  "385 is their sum, not their average; 42 and 49 are the 6th and 7th multiples.",
  "गुणज समान अंतराल पर हैं, इसलिए उनका औसत पहले और अंतिम का औसत है: (7 + 70) ÷ 2 = 38.5। "
  "385 उनका योग है, औसत नहीं; 42 और 49 छठा और सातवाँ गुणज हैं।",
  "qa-nt-the-average-of-the-first-ten-multiples-of-7", _nt4)

def _nt5():
    m = next(k for k in range(1, 100) if 9 * (k - 1) + 9 * k + 9 * (k + 1) == 162)
    return str(9 * (m + 1))
N(QA, "Number Theory", "easy",
  "Three consecutive multiples of 9 add up to 162. What is the largest of them?",
  "9 के तीन क्रमागत गुणजों का योग 162 है। उनमें सबसे बड़ा कौन-सा है?",
  ["54", "63", "72", "81"], 1,
  "Three consecutive multiples of 9 are evenly spaced, so the middle one is 162 ÷ 3 = 54, and they are 45, 54 and 63. The largest is 63. "
  "54 is the middle one; 72 and 81 go one and two steps too far.",
  "9 के तीन क्रमागत गुणज समान अंतराल पर हैं, इसलिए बीच वाला 162 ÷ 3 = 54 है, और वे 45, 54 और 63 हैं। सबसे बड़ा 63 है। "
  "54 बीच वाला है; 72 और 81 एक और दो चरण आगे चले जाते हैं।",
  "qa-nt-three-consecutive-multiples-of-9", _nt5)

def _nt6():
    g = 0
    for n in range(1, 400, 2):
        g = math.gcd(g, n * n + 3)
    return str(g)
N(QA, "Number Theory", "hard",
  "For every odd whole number n, n² + 3 is divisible by a certain number. What is the largest number that divides n² + 3 for every odd n?",
  "हर विषम पूर्ण संख्या n के लिए n² + 3 किसी निश्चित संख्या से विभाज्य है। वह सबसे बड़ी संख्या कौन-सी है जो हर विषम n के लिए n² + 3 को विभाजित करती है?",
  ["4", "6", "8", "12"], 0,
  "The square of an odd number is always 1 more than a multiple of 8 (1, 9, 25, 49, ...), so n² + 3 is 4 more than a multiple of 8: always divisible by 4, never by 8. The first values, 4, 12, 28, 52, have 4 as their greatest common factor. "
  "12 works for n = 3 but not for n = 1 or 5; 8 would need n² + 3 to be a multiple of 8, and it never is; 6 fails at once, since 4 is not a multiple of 6.",
  "विषम संख्या का वर्ग हमेशा 8 के किसी गुणज से 1 अधिक होता है (1, 9, 25, 49, ...), इसलिए n² + 3, 8 के किसी गुणज से 4 अधिक है: हमेशा 4 से विभाज्य, 8 से कभी नहीं। पहले मान 4, 12, 28, 52 हैं, जिनका सबसे बड़ा सार्व गुणनखंड 4 है। "
  "12, n = 3 पर चलता है पर n = 1 या 5 पर नहीं; 8 के लिए n² + 3 को 8 का गुणज होना होगा, और वह कभी नहीं होता; 6 तुरंत विफल है, क्योंकि 4, 6 का गुणज नहीं।",
  "qa-nt-what-always-divides-n-squared-plus-3", _nt6)

def _nt7():
    n = next(k for k in range(1, 10000) if math.prod(map(int, str(k))) == 100)
    assert all(math.prod(map(int, str(x))) == 100 for x in (455, 545, 1455, 2255))
    return str(n)
N(QA, "Number Theory", "hard",
  "What is the smallest positive whole number whose digits multiply to give 100?",
  "वह सबसे छोटी धनात्मक पूर्ण संख्या कौन-सी है जिसके अंकों का गुणनफल 100 है?",
  ["455", "545", "1455", "2255"], 0,
  "100 = 2² × 5², and each 5 must be a digit of its own. The 2² can be a single digit 4 or two digits 2 and 2; fewer digits make a smaller number, so use 4, 5 and 5. Placed in rising order they give 455. "
  "545 uses the same digits in a larger order; 2255 and 1455 have four digits where three are enough. All four options do multiply to 100.",
  "100 = 2² × 5², और हर 5 को अपना अलग अंक होना होगा। 2² एक अंक 4 हो सकता है या दो अंक 2 और 2; कम अंक छोटी संख्या बनाते हैं, इसलिए 4, 5 और 5 लीजिए। बढ़ते क्रम में वे 455 देते हैं। "
  "545 वही अंक बड़े क्रम में लेता है; 2255 और 1455 में चार अंक हैं जबकि तीन पर्याप्त हैं। चारों विकल्पों के अंकों का गुणनफल 100 ही है।",
  "qa-nt-the-smallest-number-whose-digits-multiply-to-100", _nt7)

def _nt8():
    sols = [F(n, d) for d in range(2, 50) for n in range(1, d) if F(n + 1, d) == F(1, 2) and F(n, d - 1) == F(1, 3)]
    assert sols == [F(1, 4)]
    return "1/4"
N(QA, "Number Theory", "medium",
  "A fraction becomes 1/2 when 1 is added to its numerator, and 1/3 when 1 is taken from its denominator. What is the fraction?",
  "किसी भिन्न के अंश में 1 जोड़ने पर वह 1/2 बन जाता है, और उसके हर में से 1 घटाने पर 1/3। वह भिन्न क्या है?",
  ["1/4", "2/7", "1/3", "3/8"], 0,
  "Call it n/d. Then 2(n + 1) = d and 3n = d - 1. Putting the first into the second: 3n = 2n + 1, so n = 1 and d = 4. The fraction is 1/4: check, 2/4 = 1/2 and 1/3 = 1/3. "
  "1/3 is one of the results, not the fraction; 2/7 and 3/8 satisfy neither condition.",
  "इसे n/d मानिए। तब 2(n + 1) = d और 3n = d - 1। पहले को दूसरे में रखने पर: 3n = 2n + 1, इसलिए n = 1 और d = 4। भिन्न 1/4 है: जाँच, 2/4 = 1/2 और 1/3 = 1/3। "
  "1/3 परिणामों में से एक है, भिन्न नहीं; 2/7 और 3/8 कोई भी शर्त पूरी नहीं करते।",
  "qa-nt-a-fraction-found-from-two-changes", _nt8)

def _nt9():
    a = 50 ** 0.5 + 18 ** 0.5
    assert abs(a - 8 * 2 ** 0.5) < 1e-9 and abs(a - 68 ** 0.5) > 0.5
    return "8√2"
T(QA, "Number Theory", "medium",
  "What is √50 + √18 in its simplest form?",
  "√50 + √18 अपने सरलतम रूप में क्या है?",
  ["8√2", "√68", "6√2", "4√3"], ["8√2", "√68", "6√2", "4√3"],
  0,
  "√50 = √(25 × 2) = 5√2 and √18 = √(9 × 2) = 3√2, so the sum is 8√2 (about 11.3). "
  "√68 adds the numbers under the roots, which is not allowed -- √68 is only about 8.2; 6√2 and 4√3 have no basis.",
  "√50 = √(25 × 2) = 5√2 और √18 = √(9 × 2) = 3√2, इसलिए योग 8√2 है (लगभग 11.3)। "
  "√68 मूलों के भीतर की संख्याओं को जोड़ देता है, जिसकी अनुमति नहीं -- √68 केवल लगभग 8.2 है; 6√2 और 4√3 का कोई आधार नहीं।",
  "qa-nt-root-50-plus-root-18", pos=3, check=_nt9)

def _nt10():
    sq = {k * k for k in range(4, 10)}
    cu = {k ** 3 for k in range(3, 5)}
    assert sum(sq) == 271 and (sq & cu) == {64}
    return str(sum(sq | cu))
N(QA, "Number Theory", "medium",
  "What is the sum of all the two-digit numbers that are perfect squares or perfect cubes, or both?",
  "दो अंकों की उन सभी संख्याओं का योग क्या है जो पूर्ण वर्ग या पूर्ण घन, या दोनों, हैं?",
  ["271", "298", "335", "362"], 1,
  "The two-digit squares are 16, 25, 36, 49, 64 and 81, adding to 271. The two-digit cubes are 27 and 64, but 64 is already counted. So the total is 271 + 27 = 298. "
  "271 leaves out the cube 27; 362 counts 64 twice; 335 adds 64 again but leaves out 27.",
  "दो अंकों के वर्ग 16, 25, 36, 49, 64 और 81 हैं, जिनका योग 271 है। दो अंकों के घन 27 और 64 हैं, पर 64 पहले ही गिना जा चुका है। अतः योग 271 + 27 = 298 है। "
  "271, घन 27 को छोड़ देता है; 362, 64 को दो बार गिनता है; 335, 64 को फिर जोड़ता है पर 27 को छोड़ देता है।",
  "qa-nt-the-two-digit-squares-and-cubes-added", _nt10)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    metres, minutes = 2 * (300 + 200), 5
    return f"{int(F(metres, 1000) / F(minutes, 60))} km/h"
N(QA, "Speed-Distance-Time", "easy",
  "A jogger runs once round the edge of a rectangular park 300 m long and 200 m wide in 5 minutes. What is the jogger's speed?",
  "एक धावक 300 मीटर लंबे और 200 मीटर चौड़े एक आयताकार पार्क के किनारे-किनारे एक चक्कर 5 मिनट में लगाता है। धावक की चाल क्या है?",
  ["5 km/h", "6 km/h", "10 km/h", "12 km/h"], 3,
  "Once round the park is the perimeter, 2 × (300 + 200) = 1,000 m = 1 km. One kilometre in 5 minutes is 12 km in an hour: 12 km/h. "
  "6 km/h uses only half the perimeter (300 + 200 m); 5 and 10 km/h have no basis.",
  "पार्क का एक चक्कर उसका परिमाप है, 2 × (300 + 200) = 1,000 मीटर = 1 किमी। 5 मिनट में एक किलोमीटर, यानी एक घंटे में 12 किमी: 12 किमी/घंटा। "
  "6 किमी/घंटा केवल आधा परिमाप (300 + 200 मीटर) लेता है; 5 और 10 किमी/घंटा का कोई आधार नहीं।",
  "qa-sdt-a-jogger-round-a-park", _sdt1,
  opts_hi=["5 किमी/घंटा", "6 किमी/घंटा", "10 किमी/घंटा", "12 किमी/घंटा"])

def _sdt2():
    start = dt.datetime(2027, 1, 4, 12, 0)                  # a Monday, noon
    assert start.strftime("%A") == "Monday"
    end = start + dt.timedelta(hours=2610 / 360 * 24)
    return f"{end.strftime('%A')} at {end.hour - 12} p.m."
T(QA, "Speed-Distance-Time", "medium",
  "A ship sails 360 km every day, at a steady speed day and night. It leaves port at noon on a Monday for a port 2,610 km away. When does it arrive?",
  "एक जहाज़ दिन-रात स्थिर चाल से हर दिन 360 किमी चलता है। वह सोमवार दोपहर 12 बजे 2,610 किमी दूर एक बंदरगाह के लिए निकलता है। वह कब पहुँचता है?",
  ["Monday at 6 p.m.", "Monday at 6 a.m.", "Tuesday at 6 a.m.", "Sunday at 6 p.m."],
  ["सोमवार शाम 6 बजे", "सोमवार सुबह 6 बजे", "मंगलवार सुबह 6 बजे", "रविवार शाम 6 बजे"],
  0,
  "2,610 ÷ 360 = 7.25 days, that is 7 days and 6 hours. Seven days after Monday noon is Monday noon again, and 6 hours later it is Monday at 6 p.m., the following week. "
  "Monday at 6 a.m. takes the 6 hours away instead of adding them; Tuesday at 6 a.m. adds 18 hours; Sunday at 6 p.m. counts only 6 days.",
  "2,610 ÷ 360 = 7.25 दिन, यानी 7 दिन और 6 घंटे। सोमवार दोपहर से सात दिन बाद फिर सोमवार दोपहर है, और 6 घंटे बाद अगले सप्ताह का सोमवार शाम 6 बजे। "
  "सोमवार सुबह 6 बजे 6 घंटे जोड़ने के बजाय घटाता है; मंगलवार सुबह 6 बजे 18 घंटे जोड़ता है; रविवार शाम 6 बजे केवल 6 दिन गिनता है।",
  "qa-sdt-a-voyage-counted-in-days", pos=3, check=_sdt2)

def _sdt3():
    cross, wait, day = F(3, 12) * 60, 10, 8 * 60
    trips = max(k for k in range(1, 100) if 2 * k * cross + (2 * k - 1) * wait <= day)
    assert cross == 15
    return str(trips)
N(QA, "Speed-Distance-Time", "medium",
  "A ferry crosses a river 3 km wide at 12 km/h. At each bank it waits 10 minutes before starting back. Starting from one bank at 8:00 a.m., how many complete round trips can it make by 4:00 p.m.?",
  "एक नौका 3 किमी चौड़ी नदी 12 किमी/घंटा से पार करती है। हर किनारे पर वह लौटने से पहले 10 मिनट रुकती है। एक किनारे से सुबह 8:00 बजे चलकर, शाम 4:00 बजे तक वह कितने पूरे आने-जाने के चक्कर लगा सकती है?",
  ["8", "9", "10", "16"], 1,
  "Each crossing takes 3 ÷ 12 hour = 15 minutes. A round trip is 15 minutes across, a 10-minute wait, 15 minutes back, and then a 10-minute wait before the next one: 50 minutes in all. The 9th round trip ends after 9 × 50 - 10 = 440 minutes, within the 480 minutes to 4:00 p.m.; a 10th would end at 490 minutes, too late. So 9. "
  "10 rounds 480 ÷ 50 = 9.6 up; 8 drops a trip; 16 forgets the waits.",
  "हर पार 3 ÷ 12 घंटा = 15 मिनट लेता है। एक चक्कर में 15 मिनट जाना, 10 मिनट रुकना, 15 मिनट लौटना, और फिर अगले से पहले 10 मिनट रुकना है: कुल 50 मिनट। 9वाँ चक्कर 9 × 50 - 10 = 440 मिनट बाद पूरा होता है, शाम 4 बजे तक के 480 मिनट के भीतर; 10वाँ 490 मिनट पर पूरा होता, बहुत देर से। अतः 9। "
  "10, 480 ÷ 50 = 9.6 को ऊपर पूर्णांकित करता है; 8 एक चक्कर छोड़ देता है; 16 रुकने को भूल जाता है।",
  "qa-sdt-a-ferry-s-round-trips-in-a-day", _sdt3)

def _sdt4():
    train, walk, length = F(72 * 1000, 3600), 2, 200
    t = length / walk
    return f"{indian(int((train + walk) * t))} m"
N(QA, "Speed-Distance-Time", "hard",
  "A train 200 m long moves at a steady 72 km/h. A passenger walks from the last coach to the front of the train at 2 m/s, measured along the train. How far does the passenger move over the ground during the walk?",
  "200 मीटर लंबी एक रेलगाड़ी स्थिर 72 किमी/घंटा से चल रही है। एक यात्री रेलगाड़ी के सापेक्ष 2 मीटर/सेकंड से अंतिम डिब्बे से आगे तक चलता है। चलने के दौरान यात्री ज़मीन पर कितनी दूरी तय करता है?",
  ["200 m", "1,800 m", "2,000 m", "2,200 m"], 3,
  "The walk along the train takes 200 ÷ 2 = 100 seconds. Over the ground the passenger moves at the train's speed plus the walking speed, 20 + 2 = 22 m/s, so in 100 seconds covers 2,200 m. "
  "200 m is the distance along the train; 2,000 m is how far the train itself moves in that time; 1,800 m would be right only for a walk towards the back.",
  "रेलगाड़ी के साथ चलने में 200 ÷ 2 = 100 सेकंड लगते हैं। ज़मीन पर यात्री रेलगाड़ी की चाल और चलने की चाल के योग, 20 + 2 = 22 मीटर/सेकंड, से चलता है, इसलिए 100 सेकंड में 2,200 मीटर तय करता है। "
  "200 मीटर रेलगाड़ी के साथ की दूरी है; 2,000 मीटर उस समय में स्वयं रेलगाड़ी की दूरी है; 1,800 मीटर केवल पीछे की ओर चलने पर सही होता।",
  "qa-sdt-a-walk-along-a-moving-train", _sdt4,
  opts_hi=["200 मीटर", "1,800 मीटर", "2,000 मीटर", "2,200 मीटर"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (4)
def _rm1():
    seats, share = 12, {"A": F(47, 100), "B": F(33, 100), "C": F(20, 100)}
    quota = {p: s * seats for p, s in share.items()}
    got = {p: math.floor(q) for p, q in quota.items()}
    left = seats - sum(got.values())
    for p in sorted(quota, key=lambda p: quota[p] - got[p], reverse=True)[:left]:
        got[p] += 1
    assert got == {"A": 6, "B": 4, "C": 2}
    return str(got["A"])
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A council of 12 seats is shared among three parties in proportion to their votes. Each party first gets the whole-number part of its exact share, and any seats left over go one each to the parties with the largest fractions left. Party A has 47 per cent of the votes, B 33 per cent and C 20 per cent. How many seats does A get?",
  "12 सीटों की एक परिषद तीन दलों में उनके मतों के अनुपात में बाँटी जाती है। पहले हर दल को अपने ठीक हिस्से का पूर्णांक भाग मिलता है, और बची हुई सीटें एक-एक करके सबसे बड़े बचे भिन्नों वाले दलों को जाती हैं। दल A के पास 47 प्रतिशत मत हैं, B के पास 33 प्रतिशत और C के पास 20 प्रतिशत। A को कितनी सीटें मिलती हैं?",
  ["4", "5", "6", "7"], 2,
  "The exact shares are 0.47 × 12 = 5.64, 0.33 × 12 = 3.96 and 0.20 × 12 = 2.4. The whole parts give 5, 3 and 2 -- 10 seats -- leaving 2. The largest fractions left are B's 0.96 and A's 0.64, so B and A get one more each: A 6, B 4, C 2. "
  "5 stops at the whole part; 7 gives A both spare seats; 4 is B's total.",
  "ठीक हिस्से 0.47 × 12 = 5.64, 0.33 × 12 = 3.96 और 0.20 × 12 = 2.4 हैं। पूर्णांक भाग 5, 3 और 2 देते हैं -- 10 सीटें -- और 2 बचती हैं। सबसे बड़े बचे भिन्न B का 0.96 और A का 0.64 हैं, इसलिए B और A को एक-एक और मिलती है: A 6, B 4, C 2। "
  "5 पूर्णांक भाग पर रुक जाता है; 7, A को दोनों बची सीटें दे देता है; 4, B का योग है।",
  "qa-rm-seats-shared-by-the-largest-remainder", _rm1)

def _rm2():
    return str(int(F(60, 80) * 100))
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "The marks in a test are scaled in proportion so that the top mark, 80, becomes 100. What does a mark of 60 become?",
  "एक परीक्षा के अंक अनुपात में ऐसे बढ़ाए जाते हैं कि सबसे ऊँचा अंक, 80, 100 बन जाए। 60 अंक क्या बनता है?",
  ["75", "80", "85", "90"], 0,
  "Every mark is multiplied by 100/80 = 1.25, so 60 becomes 60 × 1.25 = 75. "
  "80 adds the same 20 marks to every score, which is not scaling in proportion; 85 and 90 have no basis.",
  "हर अंक को 100/80 = 1.25 से गुणा किया जाता है, इसलिए 60, 60 × 1.25 = 75 बनता है। "
  "80 हर अंक में वही 20 अंक जोड़ता है, जो अनुपात में बढ़ाना नहीं है; 85 और 90 का कोई आधार नहीं।",
  "qa-rm-marks-scaled-to-a-top-of-100", _rm2)

def _rm3():
    r = F(3 * 120, 2 * 200)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a cake recipe, flour and sugar are measured in cups: 3 cups of flour to every 2 of sugar. A cup of flour weighs 120 g and a cup of sugar 200 g. What is the ratio of flour to sugar by weight?",
  "केक की एक विधि में आटा और चीनी कपों से नापे जाते हैं: हर 2 कप चीनी पर 3 कप आटा। एक कप आटे का भार 120 ग्राम और एक कप चीनी का 200 ग्राम है। भार के हिसाब से आटे और चीनी का अनुपात क्या है?",
  ["9 : 10", "10 : 9", "6 : 5", "3 : 2"], 0,
  "Three cups of flour weigh 3 × 120 = 360 g and two cups of sugar 2 × 200 = 400 g, so by weight the ratio is 360 : 400 = 9 : 10. "
  "3 : 2 is the ratio by cups; 10 : 9 turns the answer upside down; 6 : 5 has no basis. (The options are in order of size.)",
  "तीन कप आटे का भार 3 × 120 = 360 ग्राम और दो कप चीनी का 2 × 200 = 400 ग्राम है, इसलिए भार से अनुपात 360 : 400 = 9 : 10 है। "
  "3 : 2 कपों का अनुपात है; 10 : 9 उत्तर को उलट देता है; 6 : 5 का कोई आधार नहीं। (विकल्प आकार के क्रम में हैं।)",
  "qa-rm-a-ratio-by-cups-turned-into-a-ratio-by-weight", _rm3)

def _rm4():
    s, d = 7, 3
    r = F(s + d, s - d)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The sum of two numbers and their difference are in the ratio 7 : 3. What is the ratio of the larger number to the smaller?",
  "दो संख्याओं का योग और उनका अंतर 7 : 3 के अनुपात में हैं। बड़ी संख्या और छोटी संख्या का अनुपात क्या है?",
  ["2 : 1", "7 : 3", "5 : 2", "10 : 3"], 2,
  "Let the sum be 7k and the difference 3k. The larger number is half their total, (7k + 3k) ÷ 2 = 5k, and the smaller is half their difference, (7k - 3k) ÷ 2 = 2k. So the ratio is 5 : 2. "
  "7 : 3 repeats the ratio given; 10 : 3 compares the sum and difference added with the difference; 2 : 1 has no basis. (The options are in order of size.)",
  "योग 7k और अंतर 3k मानिए। बड़ी संख्या उनके योग का आधा है, (7k + 3k) ÷ 2 = 5k, और छोटी उनके अंतर का आधा, (7k - 3k) ÷ 2 = 2k। अतः अनुपात 5 : 2 है। "
  "7 : 3 दिया हुआ अनुपात ही दोहराता है; 10 : 3 योग और अंतर के जोड़ की तुलना अंतर से करता है; 2 : 1 का कोई आधार नहीं। (विकल्प आकार के क्रम में हैं।)",
  "qa-rm-a-ratio-from-a-sum-and-a-difference", _rm4)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    cost, kept = 40, F(8, 10)
    price = cost * F(12, 10) / kept
    return f"₹{int(price)}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A trader buys tomatoes at ₹40 a kg. A fifth of them spoil and cannot be sold. At what price per kg must the rest be sold for the trader to make a profit of 20 per cent on the whole cost?",
  "एक व्यापारी ₹40 प्रति किलो की दर से टमाटर ख़रीदता है। उनमें से पाँचवाँ भाग ख़राब हो जाता है और बिक नहीं सकता। पूरी लागत पर 20 प्रतिशत लाभ के लिए बाक़ी को किस मूल्य प्रति किलो पर बेचना होगा?",
  ["₹48", "₹50", "₹56", "₹60"], 3,
  "Take 10 kg, costing ₹400. A 20 per cent profit needs ₹480 from sales, but only 8 kg are left to sell, so each kg must fetch 480 ÷ 8 = ₹60. "
  "₹48 adds 20 per cent to ₹40 and forgets the spoilt fifth; ₹50 only covers the loss from spoiling, with no profit; ₹56 adds 20 per cent twice over.",
  "10 किलो लीजिए, जिनकी लागत ₹400 है। 20 प्रतिशत लाभ के लिए बिक्री से ₹480 चाहिए, पर बेचने के लिए केवल 8 किलो बचे हैं, इसलिए हर किलो से 480 ÷ 8 = ₹60 मिलने चाहिए। "
  "₹48, ₹40 में 20 प्रतिशत जोड़ता है और ख़राब हुए पाँचवें भाग को भूल जाता है; ₹50 केवल ख़राब होने की हानि पूरी करता है, कोई लाभ नहीं; ₹56 दो बार 20 प्रतिशत जोड़ता है।",
  "qa-pp-a-price-that-covers-spoilage", _pp1)

def _pp2():
    extra = 1 - F(1) / F(12, 10)                 # 20 per cent more for the same price
    off = F(20, 100)
    assert extra == F(1, 6) and off > extra
    return "The 20 per cent discount"
T(QA, "Percentage & Profit-Loss", "hard",
  "A pack of tea can be bought either with '20 per cent extra free' -- 20 per cent more tea for the same price -- or with '20 per cent off' the usual pack. Which gives the lower price for each gram of tea?",
  "चाय का एक पैकेट या तो '20 प्रतिशत अधिक मुफ़्त' -- उसी मूल्य में 20 प्रतिशत अधिक चाय -- के साथ, या सामान्य पैकेट पर '20 प्रतिशत छूट' के साथ ख़रीदा जा सकता है। किससे प्रति ग्राम चाय का मूल्य कम पड़ता है?",
  ["The 20 per cent discount", "The 20 per cent extra quantity", "They give exactly the same saving", "It depends on the price of the pack"],
  ["20 प्रतिशत छूट", "20 प्रतिशत अधिक मात्रा", "दोनों ठीक बराबर बचत देते हैं", "यह पैकेट के मूल्य पर निर्भर है"],
  0,
  "With 20 per cent extra, the price is spread over 1.2 times the tea, so each gram costs 1 ÷ 1.2 = 5/6 of the usual price -- a saving of 16⅔ per cent. With 20 per cent off, each gram costs 0.8 of the usual price -- a saving of 20 per cent. The discount is better. "
  "The two sound equal but are not, since 20 per cent more of the quantity is less than 20 per cent off the price; and the comparison is the same whatever the pack costs.",
  "20 प्रतिशत अधिक के साथ, मूल्य 1.2 गुना चाय पर फैलता है, इसलिए हर ग्राम सामान्य मूल्य का 1 ÷ 1.2 = 5/6 पड़ता है -- 16⅔ प्रतिशत की बचत। 20 प्रतिशत छूट के साथ हर ग्राम सामान्य मूल्य का 0.8 पड़ता है -- 20 प्रतिशत की बचत। छूट बेहतर है। "
  "दोनों बराबर लगते हैं पर हैं नहीं, क्योंकि मात्रा का 20 प्रतिशत अधिक मूल्य पर 20 प्रतिशत छूट से कम है; और पैकेट का मूल्य चाहे जो हो, तुलना वही रहती है।",
  "qa-pp-twenty-per-cent-extra-or-twenty-per-cent-off", pos=3, check=_pp2)

def _pp3():
    p = 5000
    interest = p * F(6, 100) * 2 + p * F(8, 100) * 3 + p * F(10, 100) * 1
    return f"₹{indian(int(interest))}"
N(QA, "Percentage & Profit-Loss", "medium",
  "₹5,000 is lent at simple interest of 6 per cent a year for the first 2 years, 8 per cent a year for the next 3 years, and 10 per cent a year after that. What is the total interest for 6 years?",
  "₹5,000 साधारण ब्याज पर पहले 2 वर्षों के लिए 6 प्रतिशत वार्षिक, अगले 3 वर्षों के लिए 8 प्रतिशत वार्षिक, और उसके बाद 10 प्रतिशत वार्षिक पर उधार दिया जाता है। 6 वर्षों का कुल ब्याज क्या है?",
  ["₹1,500", "₹2,000", "₹2,300", "₹2,400"], 2,
  "Simple interest is worked out on the ₹5,000 each year: 2 years at 6 per cent give ₹600, 3 years at 8 per cent ₹1,200, and the 6th year at 10 per cent ₹500. In all ₹2,300. "
  "₹2,400 charges 8 per cent for all 6 years; ₹1,500 and ₹2,000 have no basis.",
  "साधारण ब्याज हर वर्ष ₹5,000 पर निकाला जाता है: 6 प्रतिशत पर 2 वर्ष ₹600 देते हैं, 8 प्रतिशत पर 3 वर्ष ₹1,200, और 10 प्रतिशत पर छठा वर्ष ₹500। कुल ₹2,300। "
  "₹2,400 पूरे 6 वर्षों के लिए 8 प्रतिशत लगाता है; ₹1,500 और ₹2,000 का कोई आधार नहीं।",
  "qa-pp-simple-interest-at-changing-rates", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    s = [1, 1, 2]
    while len(s) < 8:
        s.append(s[-1] + s[-2] + s[-3])
    assert s[:7] == [1, 1, 2, 4, 7, 13, 24]
    return str(s[7])
N(QA, "Sequences & Series", "medium",
  "In the series 1, 1, 2, 4, 7, 13, 24, ..., what is the next term?",
  "श्रेणी 1, 1, 2, 4, 7, 13, 24, ... में अगला पद क्या है?",
  ["37", "40", "44", "48"], 2,
  "From the fourth term on, each term is the sum of the three before it: 1 + 1 + 2 = 4, 1 + 2 + 4 = 7, 2 + 4 + 7 = 13, 4 + 7 + 13 = 24. The next is 7 + 13 + 24 = 44. "
  "37 adds only the two terms before (13 + 24); 48 doubles the last term; 40 has no basis.",
  "चौथे पद से हर पद अपने से पहले के तीन पदों का योग है: 1 + 1 + 2 = 4, 1 + 2 + 4 = 7, 2 + 4 + 7 = 13, 4 + 7 + 13 = 24। अगला 7 + 13 + 24 = 44 है। "
  "37 केवल पहले के दो पद जोड़ता है (13 + 24); 48 अंतिम पद को दोगुना करता है; 40 का कोई आधार नहीं।",
  "qa-ss-each-term-the-sum-of-the-three-before", _ss1)

def _ss2():
    return str(len(range(5, 402, 4)))
N(QA, "Sequences & Series", "easy",
  "How many terms are there in the series 5, 9, 13, 17, ..., 401?",
  "श्रेणी 5, 9, 13, 17, ..., 401 में कितने पद हैं?",
  ["99", "100", "101", "396"], 1,
  "The terms go up by 4, from 5 to 401: (401 - 5) ÷ 4 = 99 steps, and one more term than steps, so 100 terms. "
  "99 counts the steps but not the first term; 396 is 401 - 5, the distance and not the count; 101 counts one term too many.",
  "पद 5 से 401 तक 4-4 बढ़ते हैं: (401 - 5) ÷ 4 = 99 कदम, और कदमों से एक पद अधिक, इसलिए 100 पद। "
  "99 कदम गिनता है पर पहला पद नहीं; 396, 401 - 5 है, दूरी, गिनती नहीं; 101 एक पद अधिक गिनता है।",
  "qa-ss-the-number-of-terms-in-an-ap", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    beads = "ABCDEF"
    seen = set()
    for p in permutations(beads):
        rots = [p[i:] + p[:i] for i in range(6)]
        forms = rots + [tuple(reversed(r)) for r in rots]
        seen.add(min(forms))
    return str(len(seen))
N(QA, "Permutation & Combination", "hard",
  "Six beads, all of different colours, are threaded on a loop of string to make a necklace. Necklaces that can be turned round or turned over to look the same count as one. How many different necklaces can be made?",
  "छह मनके, सभी अलग-अलग रंगों के, धागे के एक फंदे में पिरोकर हार बनाया जाता है। जो हार घुमाने या पलटने पर एक जैसे दिखें, वे एक ही गिने जाते हैं। कितने अलग-अलग हार बनाए जा सकते हैं?",
  ["60", "120", "360", "720"], 0,
  "In a row the beads could be arranged in 6! = 720 ways. On a loop, the 6 turnings of each arrangement look the same, leaving 720 ÷ 6 = 120; and a necklace can also be turned over, which pairs each arrangement with its mirror image, leaving 120 ÷ 2 = 60. "
  "120 allows for turning round but not for turning over, as for people at a round table; 720 counts arrangements in a row; 360 divides by 2 only.",
  "एक पंक्ति में मनके 6! = 720 तरीक़ों से रखे जा सकते थे। फंदे पर हर व्यवस्था के 6 घुमाव एक जैसे दिखते हैं, जिससे 720 ÷ 6 = 120 बचते हैं; और हार को पलटा भी जा सकता है, जो हर व्यवस्था को उसके दर्पण-प्रतिबिंब से जोड़ता है, जिससे 120 ÷ 2 = 60 बचते हैं। "
  "120 घुमाने की छूट देता है पर पलटने की नहीं, जैसे गोल मेज़ पर बैठे लोगों के लिए; 720 पंक्ति की व्यवस्थाएँ गिनता है; 360 केवल 2 से भाग देता है।",
  "qa-pc-a-necklace-of-six-different-beads", _pc1)

def _pc2():
    p = F(sum(1 for a in range(1, 7) for b in range(1, 7) if abs(a - b) == 2), 36)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "easy",
  "Two fair dice are thrown. What is the probability that the two numbers shown differ by exactly 2?",
  "दो निष्पक्ष पासे फेंके जाते हैं। दिखाई गई दोनों संख्याओं का अंतर ठीक 2 होने की प्रायिकता क्या है?",
  ["1/9", "1/6", "2/9", "1/3"], 2,
  "The pairs that differ by 2 are 1 and 3, 2 and 4, 3 and 5, and 4 and 6, each of which can come in either order on the two dice: 8 of the 36 equally likely outcomes, that is 2/9. "
  "1/9 counts each pair in one order only; 1/6 and 1/3 have no basis.",
  "2 के अंतर वाले जोड़े 1 और 3, 2 और 4, 3 और 5, तथा 4 और 6 हैं, जिनमें से हर एक दोनों पासों पर किसी भी क्रम में आ सकता है: 36 समान संभावित परिणामों में से 8, यानी 2/9। "
  "1/9 हर जोड़े को केवल एक क्रम में गिनता है; 1/6 और 1/3 का कोई आधार नहीं।",
  "qa-pc-two-dice-that-differ-by-2", _pc2)

def _pc3():
    p = F(5, 6) ** 2 * F(1, 6)
    assert 1 - F(5, 6) ** 3 == F(91, 216)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "medium",
  "A fair die is rolled again and again until a six appears. What is the probability that the first six comes on the third roll?",
  "एक निष्पक्ष पासा तब तक बार-बार फेंका जाता है जब तक छह न आए। पहला छह तीसरी बार फेंकने पर आने की प्रायिकता क्या है?",
  ["1/216", "1/36", "25/216", "91/216"], 2,
  "The first two rolls must not be sixes, each with chance 5/6, and the third must be a six, chance 1/6: 5/6 × 5/6 × 1/6 = 25/216. "
  "1/216 is three sixes in a row; 91/216 is the chance of at least one six in three rolls; 1/36 has no basis.",
  "पहली दो बार छह नहीं आना चाहिए, हर बार 5/6 की संभावना, और तीसरी बार छह आना चाहिए, संभावना 1/6: 5/6 × 5/6 × 1/6 = 25/216। "
  "1/216 लगातार तीन छह है; 91/216 तीन बार में कम से कम एक छह की संभावना है; 1/36 का कोई आधार नहीं।",
  "qa-pc-a-first-six-on-the-third-roll", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (3)
def _gm1():
    cyl = F(9)
    return f"{int(cyl / 3)} litres"
N(QA, "Geometry & Mensuration", "easy",
  "A cone and a cylinder have bases of the same radius and the same height. The cylinder holds 9 litres when full. How much does the cone hold?",
  "एक शंकु और एक बेलन के आधार की त्रिज्या और ऊँचाई समान हैं। बेलन भरा होने पर 9 लीटर रखता है। शंकु कितना रखता है?",
  ["3 litres", "4.5 litres", "6 litres", "27 litres"], 0,
  "A cone holds one-third of a cylinder with the same base and height (⅓πr²h against πr²h), so it holds 9 ÷ 3 = 3 litres. "
  "4.5 litres takes it as half; 6 litres as two-thirds, the share of a sphere in its cylinder; 27 litres multiplies by 3 instead of dividing.",
  "शंकु समान आधार और ऊँचाई वाले बेलन का एक-तिहाई रखता है (⅓πr²h बनाम πr²h), इसलिए वह 9 ÷ 3 = 3 लीटर रखता है। "
  "4.5 लीटर उसे आधा मानता है; 6 लीटर दो-तिहाई, जो बेलन में गोले का हिस्सा है; 27 लीटर भाग देने के बजाय 3 से गुणा करता है।",
  "qa-gm-a-cone-beside-a-cylinder", _gm1,
  opts_hi=["3 लीटर", "4.5 लीटर", "6 लीटर", "27 लीटर"])

def _gm2():
    d = math.hypot(12, 11 - 6)
    assert d == 13
    return "13 m"
N(QA, "Geometry & Mensuration", "medium",
  "Two vertical poles, 6 m and 11 m high, stand on level ground 12 m apart. How far apart are their tops?",
  "6 मीटर और 11 मीटर ऊँचे दो ऊर्ध्वाधर खंभे समतल ज़मीन पर 12 मीटर की दूरी पर खड़े हैं। उनके शीर्ष एक-दूसरे से कितनी दूर हैं?",
  ["5 m", "11 m", "12 m", "13 m"], 3,
  "The line joining the tops is the slanting side of a right triangle whose other sides are the 12 m between the poles and the 11 - 6 = 5 m difference in their heights: √(12² + 5²) = √169 = 13 m. "
  "5 m is the difference in height alone and 12 m the distance along the ground alone; 11 m is the taller pole's height.",
  "शीर्षों को जोड़ने वाली रेखा एक समकोण त्रिभुज की तिरछी भुजा है जिसकी अन्य भुजाएँ खंभों के बीच के 12 मीटर और उनकी ऊँचाइयों का 11 - 6 = 5 मीटर अंतर हैं: √(12² + 5²) = √169 = 13 मीटर। "
  "5 मीटर केवल ऊँचाई का अंतर है और 12 मीटर केवल ज़मीन पर की दूरी; 11 मीटर ऊँचे खंभे की ऊँचाई है।",
  "qa-gm-the-tops-of-two-poles", _gm2,
  opts_hi=["5 मीटर", "11 मीटर", "12 मीटर", "13 मीटर"])

def _gm3():
    arc = F(90, 360) * 2 * 14                     # in units of π
    r = arc / 2
    assert r == F(7, 2)
    return "3.5 cm"
N(QA, "Geometry & Mensuration", "hard",
  "A quarter of a circular sheet of radius 14 cm -- a sector with an angle of 90° -- is cut out and rolled up so that its two straight edges meet, forming a cone. What is the radius of the cone's base?",
  "14 सेमी त्रिज्या वाली एक वृत्ताकार चादर का एक चौथाई भाग -- 90° कोण वाला एक त्रिज्यखंड -- काटकर ऐसे मोड़ा जाता है कि उसकी दोनों सीधी किनारियाँ मिल जाएँ, जिससे एक शंकु बनता है। शंकु के आधार की त्रिज्या क्या है?",
  ["3.5 cm", "7 cm", "10.5 cm", "14 cm"], 0,
  "The curved edge of the sector becomes the rim of the cone's base. That edge is a quarter of the full circle, 2π × 14 ÷ 4 = 7π cm, and a base of radius r has a rim of 2πr, so 2πr = 7π and r = 3.5 cm. The 14 cm radius of the sheet becomes the cone's slant height. "
  "14 cm takes the sheet's radius for the base's; 7 cm halves it; 10.5 cm has no basis.",
  "त्रिज्यखंड की वक्र किनारी शंकु के आधार की परिधि बन जाती है। वह किनारी पूरे वृत्त का एक चौथाई है, 2π × 14 ÷ 4 = 7π सेमी, और r त्रिज्या के आधार की परिधि 2πr होती है, इसलिए 2πr = 7π और r = 3.5 सेमी। चादर की 14 सेमी त्रिज्या शंकु की तिरछी ऊँचाई बनती है। "
  "14 सेमी चादर की त्रिज्या को आधार की त्रिज्या मान लेता है; 7 सेमी उसे आधा करता है; 10.5 सेमी का कोई आधार नहीं।",
  "qa-gm-a-sector-rolled-into-a-cone", _gm3,
  opts_hi=["3.5 सेमी", "7 सेमी", "10.5 सेमी", "14 सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    hours = [1 + F(1, 2) * k for k in range(6)]
    return f"{float(sum(hours))} h"
N(QA, "Time & Work", "medium",
  "Digging a well gets harder with depth. The first metre takes 1 hour, and each later metre takes 30 minutes more than the one before. How long does it take to dig a well 6 m deep?",
  "गहराई के साथ कुआँ खोदना कठिन होता जाता है। पहला मीटर 1 घंटा लेता है, और हर अगला मीटर पिछले से 30 मिनट अधिक लेता है। 6 मीटर गहरा कुआँ खोदने में कितना समय लगता है?",
  ["9 h", "12 h", "13.5 h", "21 h"], 2,
  "The metres take 1, 1.5, 2, 2.5, 3 and 3.5 hours. These are in arithmetic progression, so their sum is 6 × (1 + 3.5) ÷ 2 = 13.5 hours. "
  "21 h gives every metre the 3.5 hours of the last; 9 h gives every metre only the 1.5 hours of the second; 12 h has no basis.",
  "मीटर 1, 1.5, 2, 2.5, 3 और 3.5 घंटे लेते हैं। ये समांतर श्रेणी में हैं, इसलिए उनका योग 6 × (1 + 3.5) ÷ 2 = 13.5 घंटे है। "
  "21 घंटे हर मीटर को अंतिम के 3.5 घंटे देता है; 9 घंटे हर मीटर को दूसरे के केवल 1.5 घंटे देता है; 12 घंटे का कोई आधार नहीं।",
  "qa-tw-a-well-that-gets-harder-to-dig", _tw1,
  opts_hi=["9 घंटे", "12 घंटे", "13.5 घंटे", "21 घंटे"])

def _tw2():
    rate = F(30, 10) + F(20, 10)                  # rotis a minute
    return f"{int(100 / rate)} minutes"
N(QA, "Time & Work", "easy",
  "One cook makes 30 rotis in 10 minutes and another makes 20 rotis in 10 minutes. Working together, how long do they take to make 100 rotis?",
  "एक रसोइया 10 मिनट में 30 रोटियाँ बनाता है और दूसरा 10 मिनट में 20। साथ काम करते हुए वे 100 रोटियाँ बनाने में कितना समय लेते हैं?",
  ["20 minutes", "25 minutes", "33⅓ minutes", "50 minutes"], 0,
  "Together they make 30 + 20 = 50 rotis in 10 minutes, so 100 rotis take 20 minutes. "
  "33⅓ minutes is the first cook alone and 50 minutes the second alone; 25 minutes has no basis.",
  "साथ मिलकर वे 10 मिनट में 30 + 20 = 50 रोटियाँ बनाते हैं, इसलिए 100 रोटियों में 20 मिनट लगते हैं। "
  "33⅓ मिनट अकेले पहले रसोइए का और 50 मिनट अकेले दूसरे का समय है; 25 मिनट का कोई आधार नहीं।",
  "qa-tw-two-cooks-and-a-hundred-rotis", _tw2,
  opts_hi=["20 मिनट", "25 मिनट", "33⅓ मिनट", "50 मिनट"])

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    years = [y for y in range(1900, 2027) if 2026 - y == sum(map(int, str(y)))]
    assert years == [2021] and all(2026 - y != sum(map(int, str(y))) for y in (2008, 2012, 2017))
    return str(years[0])
N(QA, "Puzzle Hybrid", "hard",
  "In 2026 a child's age, in whole years, is equal to the sum of the digits of the year in which the child was born. In which year was the child born?",
  "2026 में एक बच्चे की आयु, पूरे वर्षों में, उस वर्ष के अंकों के योग के बराबर है जिसमें बच्चे का जन्म हुआ। बच्चे का जन्म किस वर्ष हुआ?",
  ["2008", "2012", "2017", "2021"], 3,
  "Born in 20ab, the child is 26 - 10a - b years old, and the digit sum is 2 + a + b. Setting these equal gives 11a + 2b = 24, whose only solution in digits is a = 2, b = 1: born in 2021, aged 5, and 2 + 0 + 2 + 1 = 5. A birth year in the 1900s would need 11a + 2b = 116, impossible with single digits. "
  "2008 gives an age of 18 against a digit sum of 10; 2012 gives 14 against 5; 2017 gives 9 against 10 -- close, but not equal.",
  "20ab में जन्मा बच्चा 26 - 10a - b वर्ष का है, और अंक-योग 2 + a + b है। इन्हें बराबर रखने पर 11a + 2b = 24 मिलता है, जिसका अंकों में एकमात्र हल a = 2, b = 1 है: 2021 में जन्म, आयु 5, और 2 + 0 + 2 + 1 = 5। 1900 के दशकों के जन्म-वर्ष के लिए 11a + 2b = 116 चाहिए, जो एक-एक अंक से असंभव है। "
  "2008 से आयु 18 और अंक-योग 10; 2012 से 14 और 5; 2017 से 9 और 10 -- निकट, पर बराबर नहीं।",
  "qa-ph-an-age-equal-to-the-digit-sum-of-a-birth-year", _ph1)

def _ph2():
    d = dt.date(2027, 1, 1) + dt.timedelta(days=99)
    return f"{d.day} April"
T(QA, "Puzzle Hybrid", "easy",
  "Counting 1 January 2027 as the 1st day of the year, what is the date of the 100th day of 2027?",
  "1 जनवरी 2027 को वर्ष का पहला दिन मानते हुए, 2027 के 100वें दिन की तारीख़ क्या है?",
  ["10 April", "9 April", "11 April", "1 April"], ["10 अप्रैल", "9 अप्रैल", "11 अप्रैल", "1 अप्रैल"],
  0,
  "January, February and March 2027 have 31 + 28 + 31 = 90 days (2027 is not a leap year), so 31 March is the 90th day and the 100th day is 10 April. "
  "9 April gives February 29 days, as in a leap year; 11 April is 100 days after 1 January, which counts 1 January as day 0 rather than day 1; 1 April has no basis.",
  "जनवरी, फ़रवरी और मार्च 2027 में 31 + 28 + 31 = 90 दिन हैं (2027 अधिवर्ष नहीं), इसलिए 31 मार्च 90वाँ दिन है और 100वाँ दिन 10 अप्रैल है। "
  "9 अप्रैल फ़रवरी को 29 दिन देता है, जैसे अधिवर्ष में; 11 अप्रैल, 1 जनवरी के 100 दिन बाद है, जो 1 जनवरी को पहला दिन न मानकर शून्यवाँ मानता है; 1 अप्रैल का कोई आधार नहीं।",
  "qa-ph-the-100th-day-of-2027", pos=1, check=_ph2)

def _ph3():
    shares = F(1, 2) + F(1, 3) + F(1, 9)
    left = 1 - shares
    assert left == F(1, 18) and (18 * F(1, 2), 18 * F(1, 3), 18 * F(1, 9)) == (9, 6, 2) and 9 + 6 + 2 == 17
    return "1/18 of the herd"
T(QA, "Puzzle Hybrid", "medium",
  "A man's will leaves his 17 camels to his three sons: half to the eldest, a third to the second and a ninth to the youngest. A neighbour lends them one camel, making 18; the sons take 9, 6 and 2, and the neighbour's camel is given back. What share of the herd had the will itself left to no one?",
  "एक व्यक्ति की वसीयत उसके 17 ऊँटों को उसके तीन बेटों के लिए छोड़ती है: आधे सबसे बड़े को, एक-तिहाई दूसरे को और नौवाँ भाग सबसे छोटे को। एक पड़ोसी उन्हें एक ऊँट उधार देता है, जिससे 18 हो जाते हैं; बेटे 9, 6 और 2 लेते हैं, और पड़ोसी का ऊँट लौटा दिया जाता है। वसीयत ने स्वयं झुंड का कितना भाग किसी को नहीं दिया था?",
  ["None of it", "1/9 of the herd", "1/18 of the herd", "1/17 of the herd"],
  ["कुछ भी नहीं", "झुंड का 1/9", "झुंड का 1/18", "झुंड का 1/17"],
  2,
  "1/2 + 1/3 + 1/9 = 9/18 + 6/18 + 2/18 = 17/18, so the will gave away only 17/18 of the herd and left 1/18 to no one. That is why the borrowed camel works: 18 is divisible by 2, 3 and 9, the shares 9, 6 and 2 add to 17, and the 18th camel is free to go back. "
  "'None of it' assumes the shares add to the whole; 1/17 counts the borrowed camel against the 17; 1/9 is the youngest son's share.",
  "1/2 + 1/3 + 1/9 = 9/18 + 6/18 + 2/18 = 17/18, इसलिए वसीयत ने झुंड का केवल 17/18 भाग दिया और 1/18 किसी को नहीं दिया। इसीलिए उधार का ऊँट काम करता है: 18, 2, 3 और 9 से विभाज्य है, हिस्से 9, 6 और 2 जुड़कर 17 बनते हैं, और 18वाँ ऊँट लौटाया जा सकता है। "
  "'कुछ भी नहीं' मान लेता है कि हिस्से जुड़कर पूरा बनाते हैं; 1/17 उधार के ऊँट को 17 के मुक़ाबले गिनता है; 1/9 सबसे छोटे बेटे का हिस्सा है।",
  "qa-ph-seventeen-camels-and-a-borrowed-one", pos=2, check=_ph3)

def _ph4():
    pages, cover = F(2), F(1, 4)
    # On a shelf with spines facing out, a volume's first page lies on its right and its last page on its left, so the
    # worm crosses vol. 1's front cover, the whole of vol. 2 and vol. 3's back cover.
    path = cover + (cover + pages + cover) + cover
    assert path == 3 and 3 * (pages + 2 * cover) == F(15, 2)
    return "3 cm"
N(QA, "Puzzle Hybrid", "hard",
  "Three volumes of a book stand in order -- volume 1, 2 and 3 from left to right -- on a shelf, with their spines facing out, as books usually stand. In each volume the pages are 2 cm thick and each cover 0.25 cm. A bookworm bores in a straight line from the first page of volume 1 to the last page of volume 3. How far does it travel?",
  "एक पुस्तक के तीन खंड क्रम से -- बाएँ से दाएँ खंड 1, 2 और 3 -- एक शेल्फ़ पर खड़े हैं, जिल्द की पीठ बाहर की ओर, जैसे पुस्तकें प्रायः रखी जाती हैं। हर खंड में पृष्ठ 2 सेमी मोटे हैं और हर आवरण 0.25 सेमी। एक किताबी कीड़ा खंड 1 के पहले पृष्ठ से खंड 3 के अंतिम पृष्ठ तक सीधी रेखा में छेद करता है। वह कितनी दूरी तय करता है?",
  ["2.5 cm", "3 cm", "5.5 cm", "7.5 cm"], 1,
  "With the spine facing you, a book's front cover is on its right, so the first page of volume 1 lies against volume 2, and the last page of volume 3 lies against volume 2 too. The worm goes through volume 1's front cover (0.25 cm), the whole of volume 2 (0.25 + 2 + 0.25 cm) and volume 3's back cover (0.25 cm): 3 cm in all. "
  "7.5 cm takes the worm through all three volumes; 5.5 cm through the pages of two of them as well; 2.5 cm only through volume 2.",
  "पीठ आपकी ओर होने पर पुस्तक का अगला आवरण उसकी दाईं ओर होता है, इसलिए खंड 1 का पहला पृष्ठ खंड 2 से सटा है, और खंड 3 का अंतिम पृष्ठ भी खंड 2 से सटा है। कीड़ा खंड 1 के अगले आवरण (0.25 सेमी), पूरे खंड 2 (0.25 + 2 + 0.25 सेमी) और खंड 3 के पिछले आवरण (0.25 सेमी) से होकर जाता है: कुल 3 सेमी। "
  "7.5 सेमी कीड़े को तीनों खंडों से ले जाता है; 5.5 सेमी उनमें से दो के पृष्ठों से भी; 2.5 सेमी केवल खंड 2 से।",
  "qa-ph-a-bookworm-through-three-volumes", _ph4,
  opts_hi=["2.5 सेमी", "3 सेमी", "5.5 सेमी", "7.5 सेमी"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    isprime = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))
    s1 = {a for a in range(2, 92) if 91 % a == 0 and isprime(a)}
    s2 = set(range(11, 200))
    both = s1 & s2
    assert s1 == {7, 13} and both == {13}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the value of a?",
   "a का मान क्या है?",
   "a is a prime factor of 91.", "a, 91 का एक अभाज्य गुणनखंड है।",
   "a is greater than 10.", "a, 10 से बड़ा है।",
   2,
   "Statement I alone: 91 = 7 × 13, so a is 7 or 13. Statement II alone allows any number above 10. Together: a = 13. Both statements are needed.",
   "कथन I अकेले: 91 = 7 × 13, इसलिए a, 7 या 13 है। कथन II अकेले 10 से ऊपर की कोई भी संख्या होने देता है। दोनों मिलकर: a = 13। दोनों कथन आवश्यक हैं।",
   "qa-ds-a-prime-factor-of-91", _ds1)

def _ds2():
    s1 = {n % 4 == 1 for n in range(1, 400, 2)}
    s2 = {n % 4 == 1 for n in range(1, 400) if n * n % 8 == 1}
    both = s1 & s2
    assert s1 == s2 == {True, False}
    return _ds(s1, s2, both)
DS(QA, "hard",
   "Is the whole number n one more than a multiple of 4?",
   "क्या पूर्ण संख्या n, 4 के किसी गुणज से एक अधिक है?",
   "n is odd.", "n विषम है।",
   "n² leaves a remainder of 1 when divided by 8.", "n² को 8 से भाग देने पर शेषफल 1 बचता है।",
   3,
   "Statement I allows n = 5, which is one more than a multiple of 4, and n = 7, which is not. Statement II looks stronger but says no more: every odd square leaves remainder 1 on division by 8 (1, 9, 25, 49, ...), and only odd numbers have odd squares, so it too allows both 5 and 7. Even together the question cannot be answered.",
   "कथन I, n = 5 होने देता है, जो 4 के गुणज से एक अधिक है, और n = 7, जो नहीं है। कथन II अधिक मज़बूत लगता है पर इससे अधिक कुछ नहीं कहता: हर विषम वर्ग 8 से भाग देने पर शेष 1 छोड़ता है (1, 9, 25, 49, ...), और केवल विषम संख्याओं के वर्ग विषम होते हैं, इसलिए वह भी 5 और 7 दोनों होने देता है। दोनों मिलकर भी प्रश्न का उत्तर नहीं दिया जा सकता।",
   "qa-ds-one-more-than-a-multiple-of-4", _ds2)
