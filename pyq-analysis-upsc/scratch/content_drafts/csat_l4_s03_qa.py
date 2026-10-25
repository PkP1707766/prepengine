# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 3 -- Quantitative Aptitude (37 items: 35 in the Quant slots, 2 in the data-sufficiency block).

Layout C, the 2026 shape of the paper: Quant-heavy, with number theory the largest bucket (10). Exam-level mix
(7 easy / 19 medium / 11 hard), with none of the shapes of Levels 1-3 or Simulators 1-2: three primes that add to 100,
what always holds for 0 < a < b < 1, four equal powers of 2 added, sixth powers up to 1,000, the smallest number with
digit sum 25, the largest three-digit multiple of 4 with distinct digits, a number left on a board after differences,
two-digit numbers whose squares end in themselves, the smallest prime factor of 3^5 + 5^3, three-digit repdigits
divisible by 9; a man in a tunnel and a train behind him, a cyclist who turns back for a walker, a car and a train on
the same distance, a runner's pace; what doubling the largest value changes, a required run rate, sand for concrete, a
transfer that raises both averages; a smaller pack at a lower price, what is left after shares of what is left, the
GST a trader pays over; a sum of repunits, a series of products; six people paired off, scoops chosen with repeats,
three birthdays on different weekdays; the litres in a cylindrical tank, an isosceles triangle with one angle of 40°, a
quadrilateral from its corners; sprinklers when one breaks, a day's pay with overtime; a clock in a mirror, four people
and one torch, a rope round the Earth, buying and selling the same item twice; and two data-sufficiency items. Every
key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
import math
import random
import csat_common as c
from csat_common import N, T, S2, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

isprime = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))

# ---------------------------------------------------------------- Number Theory (10)
def _nt1():
    ps = [p for p in range(2, 100) if isprime(p)]
    sols = {tuple(sorted(t)) for t in combinations(ps, 3) if sum(t) == 100 and any(abs(x - y) == 36 for x, y in combinations(t, 2))}
    assert sols == {(2, 31, 67)}
    return str(max(sols.pop()))
N(QA, "Number Theory", "hard",
  "Three different prime numbers add up to 100, and one of them is 36 more than another. What is the largest of the three?",
  "तीन अलग-अलग अभाज्य संख्याओं का योग 100 है, और उनमें से एक दूसरी से 36 अधिक है। तीनों में सबसे बड़ी क्या है?",
  ["31", "59", "67", "71"], 2,
  "Three odd primes would add up to an odd number, so one of the three must be 2, the only even prime. The other two add up to 98. If they differ by 36 they are 67 and 31, both prime. (The difference cannot involve 2, since 38 is not prime.) So the primes are 2, 31 and 67, and the largest is 67. "
  "31 is the smaller of the pair; 59 and 71 do not fit with 2 and a partner to make 100 with a difference of 36.",
  "तीन विषम अभाज्य संख्याओं का योग विषम होता, इसलिए तीनों में से एक 2 होनी चाहिए, एकमात्र सम अभाज्य। बाक़ी दो का योग 98 है। यदि उनमें 36 का अंतर है तो वे 67 और 31 हैं, दोनों अभाज्य। (अंतर में 2 शामिल नहीं हो सकती, क्योंकि 38 अभाज्य नहीं।) अतः अभाज्य संख्याएँ 2, 31 और 67 हैं, और सबसे बड़ी 67 है। "
  "31 जोड़े की छोटी संख्या है; 59 और 71, 2 और किसी साथी के साथ 36 के अंतर से 100 नहीं बनातीं।",
  "qa-nt-three-primes-that-add-to-100", _nt1)

def _nt2():
    grid = [k / 200 for k in range(1, 200)]
    pairs = [(a, b) for a in grid for b in grid if a < b]
    one = all(a * a < b * b for a, b in pairs)
    two = all(1 / a < 1 / b for a, b in pairs)
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Number Theory", "medium",
   "If 0 < a < b < 1, which of the following statements is/are always correct?",
   "यदि 0 < a < b < 1, तो निम्नलिखित में से कौन-सा/से कथन हमेशा सही है/हैं?",
   ["a² < b²", "1/a < 1/b"], ["a² < b²", "1/a < 1/b"],
   0,
   "1: both numbers are positive, and squaring keeps the order of positive numbers, so a² < b² -- always correct. "
   "2: taking reciprocals of positive numbers reverses their order: a < b gives 1/a > 1/b (for example a = 1/4, b = 1/2 give 4 > 2). So 2 is never correct.",
   "1: दोनों संख्याएँ धनात्मक हैं, और धनात्मक संख्याओं का वर्ग उनका क्रम बनाए रखता है, इसलिए a² < b² -- हमेशा सही। "
   "2: धनात्मक संख्याओं के व्युत्क्रम लेने से उनका क्रम उलट जाता है: a < b से 1/a > 1/b मिलता है (जैसे a = 1/4, b = 1/2 से 4 > 2)। इसलिए 2 कभी सही नहीं।",
   "qa-nt-what-always-holds-for-0-a-b-1", check=_nt2)

def _nt3():
    assert 4 * 2 ** 10 == 2 ** 12
    return "2¹²"
N(QA, "Number Theory", "easy",
  "What is 2¹⁰ + 2¹⁰ + 2¹⁰ + 2¹⁰ equal to?",
  "2¹⁰ + 2¹⁰ + 2¹⁰ + 2¹⁰ किसके बराबर है?",
  ["2¹²", "2¹⁴", "2⁴⁰", "8¹⁰"], 0,
  "Four equal terms make 4 × 2¹⁰ = 2² × 2¹⁰ = 2¹². 2⁴⁰ multiplies the exponents as though the terms were multiplied together; 8¹⁰ = 2³⁰ and 2¹⁴ have no basis.",
  "चार बराबर पद 4 × 2¹⁰ = 2² × 2¹⁰ = 2¹² बनाते हैं। 2⁴⁰ घातांकों को ऐसे गुणा करता है मानो पदों को आपस में गुणा किया गया हो; 8¹⁰ = 2³⁰ और 2¹⁴ का कोई आधार नहीं।",
  "qa-nt-four-equal-powers-of-2-added", _nt3)

def _nt4():
    sixth = [n for n in range(1, 1001) if round(n ** (1 / 2)) ** 2 == n and round(n ** (1 / 3)) ** 3 == n]
    assert sixth == [1, 64, 729]
    return str(len(sixth))
N(QA, "Number Theory", "medium",
  "How many whole numbers from 1 to 1,000 are both perfect squares and perfect cubes?",
  "1 से 1,000 तक की कितनी पूर्ण संख्याएँ पूर्ण वर्ग भी हैं और पूर्ण घन भी?",
  ["2", "3", "4", "10"], 1,
  "A number that is both a square and a cube is a sixth power: 1⁶ = 1, 2⁶ = 64 and 3⁶ = 729, while 4⁶ = 4,096 is too large. So there are three. "
  "2 leaves out 1; 10 is the number of cubes up to 1,000; 4 has no basis.",
  "जो संख्या वर्ग भी हो और घन भी, वह छठी घात होती है: 1⁶ = 1, 2⁶ = 64 और 3⁶ = 729, जबकि 4⁶ = 4,096 बहुत बड़ी है। अतः ऐसी तीन हैं। "
  "2 संख्या 1 को छोड़ देता है; 10, 1,000 तक के घनों की संख्या है; 4 का कोई आधार नहीं।",
  "qa-nt-sixth-powers-up-to-1000", _nt4)

def _nt5():
    return str(next(n for n in range(1, 10000) if sum(map(int, str(n))) == 25))
N(QA, "Number Theory", "medium",
  "What is the smallest whole number whose digits add up to 25?",
  "वह सबसे छोटी पूर्ण संख्या कौन-सी है जिसके अंकों का योग 25 है?",
  ["799", "889", "979", "997"], 0,
  "Two digits can add up to at most 18, so at least three are needed. With three digits the number is smallest when the first digit is as small as possible, which means the last two are as large as possible: 9 and 9, leaving 25 - 18 = 7 for the first. So the answer is 799. "
  "889, 979 and 997 also have digit sum 25, but each is larger than 799.",
  "दो अंकों का योग अधिक से अधिक 18 हो सकता है, इसलिए कम से कम तीन अंक चाहिए। तीन अंकों में संख्या तब सबसे छोटी है जब पहला अंक जितना हो सके छोटा हो, यानी बाक़ी दो जितने हो सकें बड़े: 9 और 9, जिससे पहले के लिए 25 - 18 = 7 बचता है। अतः उत्तर 799 है। "
  "889, 979 और 997 का अंक-योग भी 25 है, पर हर एक 799 से बड़ी है।",
  "qa-nt-the-smallest-number-with-digit-sum-25", _nt5)

def _nt6():
    return str(max(n for n in range(100, 1000) if n % 4 == 0 and len(set(str(n))) == 3))
N(QA, "Number Theory", "medium",
  "What is the largest three-digit number that is divisible by 4 and has three different digits?",
  "तीन अलग-अलग अंकों वाली वह सबसे बड़ी तीन अंकों की संख्या कौन-सी है जो 4 से विभाज्य है?",
  ["964", "972", "984", "996"], 2,
  "A number is divisible by 4 when its last two digits are. Start from the top: 996 and 988 are divisible by 4 but repeat a digit; 992 repeats 9; 984 has three different digits and 84 = 4 × 21. So the answer is 984. "
  "964 and 972 also qualify but are smaller; 996 repeats the 9.",
  "कोई संख्या 4 से तब विभाज्य होती है जब उसके अंतिम दो अंक हों। ऊपर से शुरू कीजिए: 996 और 988, 4 से विभाज्य हैं पर उनमें कोई अंक दोहराया गया है; 992 में 9 दोहराया गया है; 984 के तीनों अंक अलग हैं और 84 = 4 × 21। अतः उत्तर 984 है। "
  "964 और 972 भी योग्य हैं पर छोटी हैं; 996 में 9 दोहराया गया है।",
  "qa-nt-the-largest-three-digit-multiple-of-4-with-distinct-digits", _nt6)

def _nt7():
    rng = random.Random(7)
    finals = set()
    for _ in range(2000):
        xs = list(range(1, 11))
        while len(xs) > 1:
            i, j = sorted(rng.sample(range(len(xs)), 2), reverse=True)
            x, y = xs.pop(i), xs.pop(j)
            xs.append(abs(x - y))
        finals.add(xs[0])
    assert finals and all(f % 2 == 1 for f in finals) and sum(range(1, 11)) % 2 == 1
    return "It is always odd."
T(QA, "Number Theory", "hard",
  "The numbers 1, 2, 3, ..., 10 are written on a board. At each step any two numbers on the board are rubbed out and replaced by their difference (the larger minus the smaller). This is repeated until only one number is left. What can be said about that number?",
  "बोर्ड पर संख्याएँ 1, 2, 3, ..., 10 लिखी हैं। हर चरण में बोर्ड की कोई दो संख्याएँ मिटाकर उनकी जगह उनका अंतर (बड़ी में से छोटी) लिखा जाता है। यह तब तक दोहराया जाता है जब तक केवल एक संख्या न बचे। उस संख्या के बारे में क्या कहा जा सकता है?",
  ["It is always odd.", "It is always even.", "It is always 1.", "It may be any whole number from 0 to 10."],
  ["वह हमेशा विषम होती है।", "वह हमेशा सम होती है।", "वह हमेशा 1 होती है।", "वह 0 से 10 तक कोई भी पूर्ण संख्या हो सकती है।"],
  0,
  "Replacing x and y by x - y changes the sum of all the numbers by 2y, an even amount, so the sum never changes from odd to even or back. It starts at 1 + 2 + ... + 10 = 55, which is odd, so the last number -- which is the whole sum at the end -- is odd. "
  "It need not be 1: different orders of rubbing out can leave 1, 3, 5, 7 or 9. It can never be even, and so it cannot be any number from 0 to 10.",
  "x और y की जगह x - y लिखने से सभी संख्याओं का योग 2y, एक सम राशि, से बदलता है, इसलिए योग कभी विषम से सम या उलटा नहीं होता। वह 1 + 2 + ... + 10 = 55 से शुरू होता है, जो विषम है, इसलिए अंतिम संख्या -- जो अंत में पूरा योग है -- विषम है। "
  "उसका 1 होना आवश्यक नहीं: मिटाने के अलग-अलग क्रमों से 1, 3, 5, 7 या 9 बच सकती है। वह कभी सम नहीं हो सकती, इसलिए 0 से 10 तक कोई भी संख्या नहीं हो सकती।",
  "qa-nt-a-number-left-on-a-board-after-differences", pos=3, check=_nt7)

def _nt8():
    ns = [n for n in range(10, 100) if n * n % 100 == n]
    assert ns == [25, 76]
    return str(len(ns))
N(QA, "Number Theory", "hard",
  "For how many two-digit numbers n does n² end in the same two digits as n (for example, if n were 25, n² = 625 ends in 25)?",
  "दो अंकों की कितनी संख्याओं n के लिए n² उन्हीं दो अंकों पर समाप्त होता है जो n के हैं (उदाहरण के लिए, यदि n = 25 हो, तो n² = 625, जो 25 पर समाप्त होता है)?",
  ["0", "1", "2", "3"], 2,
  "We need n² - n = n(n - 1) to be divisible by 100 = 4 × 25. Since n and n - 1 share no factor, one of them must take the 25 and, between them, the 4. If 25 divides n, then n = 25 or 75, and 4 must divide n - 1: 25 works (24), 75 does not (74). If 25 divides n - 1, then n = 26, 51 or 76, and 4 must divide n: only 76 works. "
  "So n = 25 (625) or n = 76 (5,776): two numbers. 1 stops at the example; 3 adds a number such as 75 or 50 that fails.",
  "हमें चाहिए कि n² - n = n(n - 1), 100 = 4 × 25 से विभाज्य हो। चूँकि n और n - 1 का कोई गुणनखंड साझा नहीं, उनमें से एक को 25 लेना होगा और दोनों के बीच 4। यदि 25, n को विभाजित करे, तो n = 25 या 75, और 4 को n - 1 को विभाजित करना होगा: 25 काम करता है (24), 75 नहीं (74)। यदि 25, n - 1 को विभाजित करे, तो n = 26, 51 या 76, और 4 को n को विभाजित करना होगा: केवल 76 काम करता है। "
  "अतः n = 25 (625) या n = 76 (5,776): दो संख्याएँ। 1 उदाहरण पर रुक जाता है; 3, 75 या 50 जैसी कोई विफल संख्या जोड़ देता है।",
  "qa-nt-two-digit-numbers-whose-squares-end-in-themselves", _nt8)

def _nt9():
    v = 3 ** 5 + 5 ** 3
    return str(min(p for p in range(2, v + 1) if v % p == 0))
N(QA, "Number Theory", "easy",
  "What is the smallest prime number that divides 3⁵ + 5³?",
  "3⁵ + 5³ को विभाजित करने वाली सबसे छोटी अभाज्य संख्या क्या है?",
  ["2", "3", "5", "23"], 0,
  "3⁵ and 5³ are both odd, and the sum of two odd numbers is even, so 2 divides it (indeed 243 + 125 = 368 = 2⁴ × 23). The trap is to look only for 3 or 5, which divide one term each but not the sum; 23 is the largest prime factor, not the smallest.",
  "3⁵ और 5³ दोनों विषम हैं, और दो विषम संख्याओं का योग सम होता है, इसलिए 2 उसे विभाजित करती है (वास्तव में 243 + 125 = 368 = 2⁴ × 23)। जाल केवल 3 या 5 देखना है, जो एक-एक पद को विभाजित करती हैं पर योग को नहीं; 23 सबसे बड़ा अभाज्य गुणनखंड है, सबसे छोटा नहीं।",
  "qa-nt-the-smallest-prime-factor-of-3-to-the-5-plus-5-cubed", _nt9)

def _nt10():
    return str(sum(1 for k in range(1, 10) if (111 * k) % 9 == 0))
N(QA, "Number Theory", "medium",
  "How many three-digit numbers with all three digits the same (111, 222, ..., 999) are divisible by 9?",
  "तीनों अंक समान वाली तीन अंकों की कितनी संख्याएँ (111, 222, ..., 999) 9 से विभाज्य हैं?",
  ["0", "1", "2", "3"], 3,
  "The number kkk has digit sum 3k, and it is divisible by 9 exactly when 3k is, that is when k is a multiple of 3: k = 3, 6 or 9, giving 333, 666 and 999. "
  "1 counts only 999; 0 and 2 miscount the multiples of 3 among the digits 1 to 9.",
  "संख्या kkk का अंक-योग 3k है, और वह ठीक तब 9 से विभाज्य है जब 3k हो, यानी जब k, 3 का गुणज हो: k = 3, 6 या 9, जिनसे 333, 666 और 999 मिलती हैं। "
  "1 केवल 999 गिनता है; 0 और 2, 1 से 9 तक के अंकों में 3 के गुणज ग़लत गिनते हैं।",
  "qa-nt-three-digit-repdigits-divisible-by-9", _nt10)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    man = F(3, 8)                               # how far into the tunnel, as a share of its length
    ratio = F(1) / (1 - 2 * man)                # running forward he gains 3/8 more before the train reaches the mouth
    assert ratio == 4
    return "4 : 1"
N(QA, "Speed-Distance-Time", "hard",
  "A man is three-eighths of the way through a railway tunnel when he hears a train coming from behind him. If he runs back to the entrance he will reach it just as the train does; if he runs on to the far end, the train will catch him exactly at the exit. He runs at the same speed either way. What is the ratio of the train's speed to the man's?",
  "एक व्यक्ति रेल-सुरंग के तीन-आठवें भाग तक पहुँचा है जब वह पीछे से आती रेलगाड़ी की आवाज़ सुनता है। यदि वह प्रवेश-द्वार की ओर वापस दौड़े, तो ठीक उसी क्षण वहाँ पहुँचेगा जब रेलगाड़ी; यदि वह आगे दूसरे छोर की ओर दौड़े, तो रेलगाड़ी उसे ठीक निकास पर पकड़ लेगी। दोनों ओर वह एक ही चाल से दौड़ता है। रेलगाड़ी और व्यक्ति की चालों का अनुपात क्या है?",
  ["2 : 1", "3 : 1", "4 : 1", "8 : 3"], 2,
  "In the time the train takes to reach the entrance, the man can run 3/8 of the tunnel's length. So if he runs forward, he is 3/8 + 3/8 = 6/8 of the way through when the train reaches the entrance. From then on the train covers the whole tunnel while he covers the last 2/8 of it, arriving together. "
  "So the train is 1 ÷ 2/8 = 4 times as fast. 8 : 3 compares the tunnel with the man's first position; 2 : 1 and 3 : 1 have no basis.",
  "जितने समय में रेलगाड़ी प्रवेश-द्वार तक पहुँचती है, उतने में व्यक्ति सुरंग की लंबाई का 3/8 दौड़ सकता है। इसलिए यदि वह आगे दौड़े, तो रेलगाड़ी के प्रवेश-द्वार पहुँचने पर वह 3/8 + 3/8 = 6/8 पार कर चुका होता है। तब से रेलगाड़ी पूरी सुरंग पार करती है जबकि वह अंतिम 2/8, और दोनों साथ पहुँचते हैं। "
  "अतः रेलगाड़ी 1 ÷ 2/8 = 4 गुना तेज़ है। 8 : 3 सुरंग की तुलना व्यक्ति की पहली स्थिति से करता है; 2 : 1 और 3 : 1 का कोई आधार नहीं।",
  "qa-sdt-a-man-in-a-tunnel-and-a-train-behind-him", _sdt1)

def _sdt2():
    t_turn = 2
    gap = (12 - 4) * t_turn
    t_meet = t_turn + F(gap, 12 + 4)
    return f"{4 * t_meet} km"
N(QA, "Speed-Distance-Time", "medium",
  "A cyclist and a walker leave a town together along the same road, the cyclist at 12 km/h and the walker at 4 km/h. After 2 hours the cyclist turns back and rides towards the walker at the same speed. How far from the town do they meet?",
  "एक साइकिल सवार और एक पैदल यात्री एक नगर से एक ही सड़क पर साथ निकलते हैं, साइकिल सवार 12 किमी/घंटा से और पैदल यात्री 4 किमी/घंटा से। 2 घंटे बाद साइकिल सवार मुड़ता है और उसी चाल से पैदल यात्री की ओर लौटता है। नगर से कितनी दूरी पर वे मिलते हैं?",
  ["8 km", "12 km", "16 km", "24 km"], 1,
  "After 2 hours the cyclist is 24 km out and the walker 8 km, 16 km behind. Riding back while the walker comes on, they close the 16 km at 12 + 4 = 16 km/h, so they meet 1 hour later. By then the walker has gone 3 hours at 4 km/h: 12 km from the town. "
  "8 km is where the walker was when the cyclist turned; 24 km is where the cyclist turned; 16 km is the gap between them at that moment.",
  "2 घंटे बाद साइकिल सवार 24 किमी दूर है और पैदल यात्री 8 किमी, 16 किमी पीछे। साइकिल सवार के लौटते और पैदल यात्री के आगे बढ़ते हुए वे 16 किमी की दूरी 12 + 4 = 16 किमी/घंटा से घटाते हैं, इसलिए वे 1 घंटे बाद मिलते हैं। तब तक पैदल यात्री 4 किमी/घंटा से 3 घंटे चल चुका है: नगर से 12 किमी। "
  "8 किमी वह स्थान है जहाँ साइकिल सवार के मुड़ते समय पैदल यात्री था; 24 किमी वह स्थान है जहाँ साइकिल सवार मुड़ा; 16 किमी उस क्षण उनके बीच की दूरी है।",
  "qa-sdt-a-cyclist-who-turns-back-for-a-walker", _sdt2,
  opts_hi=["8 किमी", "12 किमी", "16 किमी", "24 किमी"])

def _sdt3():
    car = next(v for v in range(1, 200) if 4 * v == 3 * (v + 20))
    return f"{4 * car} km"
N(QA, "Speed-Distance-Time", "medium",
  "A car takes 4 hours to cover a distance that a train covers in 3 hours. The train is 20 km/h faster than the car. How long is the distance?",
  "एक गाड़ी किसी दूरी को 4 घंटे में तय करती है जिसे एक रेलगाड़ी 3 घंटे में तय करती है। रेलगाड़ी गाड़ी से 20 किमी/घंटा तेज़ है। दूरी कितनी है?",
  ["60 km", "180 km", "200 km", "240 km"], 3,
  "If the car's speed is v, then 4v = 3(v + 20), so v = 60 km/h and the train's speed is 80 km/h. The distance is 4 × 60 = 3 × 80 = 240 km. "
  "60 km is the car's speed, not the distance; 180 km multiplies the car's speed by the train's time; 200 km has no basis.",
  "यदि गाड़ी की चाल v है, तो 4v = 3(v + 20), इसलिए v = 60 किमी/घंटा और रेलगाड़ी की चाल 80 किमी/घंटा। दूरी 4 × 60 = 3 × 80 = 240 किमी है। "
  "60 किमी गाड़ी की चाल है, दूरी नहीं; 180 किमी गाड़ी की चाल को रेलगाड़ी के समय से गुणा करता है; 200 किमी का कोई आधार नहीं।",
  "qa-sdt-a-car-and-a-train-on-the-same-distance", _sdt3,
  opts_hi=["60 किमी", "180 किमी", "200 किमी", "240 किमी"])

def _sdt4():
    return f"{60 // 5} km/h"
N(QA, "Speed-Distance-Time", "easy",
  "A runner's pace is 5 minutes per kilometre. What is her speed?",
  "एक धावक की गति प्रति किलोमीटर 5 मिनट है। उसकी चाल क्या है?",
  ["12 km/h", "15 km/h", "20 km/h", "30 km/h"], 0,
  "At 5 minutes for each kilometre she covers 60 ÷ 5 = 12 km in an hour: 12 km/h. 15 km/h would be 4 minutes a kilometre, 20 km/h 3 minutes and 30 km/h 2 minutes.",
  "हर किलोमीटर में 5 मिनट से वह एक घंटे में 60 ÷ 5 = 12 किमी चलती है: 12 किमी/घंटा। 15 किमी/घंटा का अर्थ प्रति किलोमीटर 4 मिनट, 20 किमी/घंटा का 3 मिनट और 30 किमी/घंटा का 2 मिनट होगा।",
  "qa-sdt-a-runner-s-pace", _sdt4,
  opts_hi=["12 किमी/घंटा", "15 किमी/घंटा", "20 किमी/घंटा", "30 किमी/घंटा"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (4)
def _rm1():
    rng = random.Random(3)
    one = two = True
    for _ in range(500):
        xs = sorted(rng.sample(range(1, 500), 9))
        ys = xs[:-1] + [2 * xs[-1]]
        one = one and sorted(ys)[4] != xs[4]
        two = two and sum(ys) != sum(xs)
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Ratio, Mixtures & Alligation", "medium",
   "Nine different positive numbers are listed. If the largest of them is doubled, which of the following is/are certain to change?",
   "नौ अलग-अलग धनात्मक संख्याओं की सूची है। यदि उनमें सबसे बड़ी संख्या को दोगुना कर दिया जाए, तो निम्नलिखित में से कौन-सा/से निश्चित रूप से बदलेगा/बदलेंगे?",
   ["The median of the nine numbers", "The mean (average) of the nine numbers"],
   ["नौ संख्याओं की माध्यिका", "नौ संख्याओं का माध्य (औसत)"],
   1,
   "1: the median of nine numbers is the fifth in order; making the largest still larger does not alter which number stands fifth, so the median stays the same. "
   "2: doubling the largest number adds that number to the total, so the mean rises -- certain to change. Only the mean changes.",
   "1: नौ संख्याओं की माध्यिका क्रम में पाँचवीं संख्या है; सबसे बड़ी को और बड़ा करने से यह नहीं बदलता कि पाँचवें स्थान पर कौन है, इसलिए माध्यिका वही रहती है। "
   "2: सबसे बड़ी संख्या को दोगुना करने से वही संख्या कुल योग में जुड़ जाती है, इसलिए माध्य बढ़ता है -- निश्चित रूप से बदलता है। केवल माध्य बदलता है।",
   "qa-rm-what-doubling-the-largest-value-changes", check=_rm1)

def _rm2():
    r = F(282 - 4 * 10, 40)
    return f"{float(r):.2f}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a 50-over cricket match, a team chasing 282 has scored at 4 runs an over in the first 10 overs without losing a wicket. At what average rate must it score in the remaining 40 overs to reach 282?",
  "50 ओवर के एक क्रिकेट मैच में 282 का पीछा करती टीम ने पहले 10 ओवरों में बिना विकेट खोए 4 रन प्रति ओवर की दर से रन बनाए हैं। 282 तक पहुँचने के लिए उसे बाक़ी 40 ओवरों में किस औसत दर से रन बनाने होंगे?",
  ["5.50", "5.64", "6.05", "7.05"], 2,
  "The team has 40 runs, so it needs 282 - 40 = 242 more in 40 overs: 242 ÷ 40 = 6.05 runs an over. 5.64 is 282 spread over all 50 overs; 7.05 spreads 282 over the last 40 alone, forgetting the runs already made; 5.50 has no basis.",
  "टीम के 40 रन हैं, इसलिए उसे 40 ओवरों में 282 - 40 = 242 और चाहिए: 242 ÷ 40 = 6.05 रन प्रति ओवर। 5.64, 282 को सभी 50 ओवरों में बाँटता है; 7.05, पहले से बने रन भूलकर 282 को केवल अंतिम 40 ओवरों में बाँटता है; 5.50 का कोई आधार नहीं।",
  "qa-rm-a-required-run-rate", _rm2)

def _rm3():
    return f"{F(14 * 2, 1 + 2 + 4)} m³"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "Concrete is made by mixing cement, sand and gravel in the ratio 1 : 2 : 4 by volume. How much sand is needed for 14 m³ of the mix?",
  "कंक्रीट सीमेंट, रेत और बजरी को आयतन के अनुसार 1 : 2 : 4 के अनुपात में मिलाकर बनता है। मिश्रण के 14 घन मीटर के लिए कितनी रेत चाहिए?",
  ["2 m³", "4 m³", "7 m³", "8 m³"], 1,
  "The ratio has 1 + 2 + 4 = 7 parts, so each part is 14 ÷ 7 = 2 m³, and sand, 2 parts, is 4 m³. 2 m³ is the cement; 8 m³ is the gravel; 7 m³ halves the whole mix.",
  "अनुपात में 1 + 2 + 4 = 7 भाग हैं, इसलिए हर भाग 14 ÷ 7 = 2 घन मीटर है, और रेत, 2 भाग, 4 घन मीटर है। 2 घन मीटर सीमेंट है; 8 घन मीटर बजरी है; 7 घन मीटर पूरे मिश्रण का आधा करता है।",
  "qa-rm-sand-for-concrete", _rm3,
  opts_hi=["2 घन मीटर", "4 घन मीटर", "7 घन मीटर", "8 घन मीटर"])

def _rm4():
    A, B = [50, 60, 70, 80], [20, 30, 40]
    mean = lambda xs: F(sum(xs), len(xs))
    for s in A:
        nA, nB = [x for x in A if x != s], B + [s]
        if mean(nA) > mean(A) and mean(nB) > mean(B):
            assert mean(B) < s < mean(A)
    return "The student's score was below section A's average but above section B's."
T(QA, "Ratio, Mixtures & Alligation", "hard",
  "When one student moved from section A to section B of a class, the average score of section A went up and the average score of section B also went up. Which one of the following must be true?",
  "जब एक विद्यार्थी कक्षा के खंड A से खंड B में गया, तो खंड A का औसत अंक भी बढ़ा और खंड B का औसत अंक भी। निम्नलिखित में से कौन-सा अवश्य सत्य है?",
  ["The student's score was below section A's average but above section B's.",
   "The student's score was above the averages of both sections before the move.",
   "The student's score was below the averages of both sections before the move.",
   "The two sections must have had the same average before the student moved."],
  ["उस विद्यार्थी के अंक खंड A के औसत से कम पर खंड B के औसत से अधिक थे।",
   "उस विद्यार्थी के अंक जाने से पहले दोनों खंडों के औसत से अधिक थे।",
   "उस विद्यार्थी के अंक जाने से पहले दोनों खंडों के औसत से कम थे।",
   "विद्यार्थी के जाने से पहले दोनों खंडों का औसत अवश्य बराबर रहा होगा।"],
  0,
  "Removing a score raises an average only if that score was below it, so the student was below section A's average. Adding a score raises an average only if it is above it, so the student was above section B's. Both hold at once only if section B's average was lower than section A's, with the student's score in between. "
  "A score above both averages would have lowered A's; one below both would have lowered B's; and equal averages would leave no room for a score strictly between them.",
  "किसी अंक को हटाने से औसत तभी बढ़ता है जब वह अंक औसत से कम हो, इसलिए विद्यार्थी के अंक खंड A के औसत से कम थे। किसी अंक को जोड़ने से औसत तभी बढ़ता है जब वह औसत से अधिक हो, इसलिए विद्यार्थी के अंक खंड B के औसत से अधिक थे। दोनों एक साथ तभी संभव हैं जब खंड B का औसत खंड A से कम था, और विद्यार्थी के अंक उनके बीच। "
  "दोनों औसतों से अधिक अंक A का औसत घटा देते; दोनों से कम अंक B का औसत घटा देते; और बराबर औसतों में उनके ठीक बीच किसी अंक के लिए जगह नहीं बचती।",
  "qa-rm-a-transfer-that-raises-both-averages", pos=3, check=_rm4)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    ch = (F(38, 90) / F(40, 100) - 1) * 100
    assert round(float(ch), 1) == 5.6
    return "About 5.6 per cent rise"
N(QA, "Percentage & Profit-Loss", "medium",
  "A 100 g packet of biscuits that cost ₹40 is replaced by a 90 g packet costing ₹38. By about what percentage has the price per gram changed?",
  "₹40 वाले बिस्कुट के 100 ग्राम के पैकेट की जगह ₹38 का 90 ग्राम का पैकेट आ जाता है। प्रति ग्राम मूल्य लगभग कितने प्रतिशत बदला है?",
  ["5 per cent fall", "No change", "About 5.6 per cent rise", "10 per cent rise"], 2,
  "The old price was 40/100 = ₹0.40 a gram; the new price is 38/90, about ₹0.422 a gram -- a rise of about 5.6 per cent. "
  "'5 per cent fall' looks only at the price on the packet, which fell from ₹40 to ₹38; 'no change' assumes the smaller packet and lower price balance out; 10 per cent counts only the weight lost.",
  "पुराना मूल्य 40/100 = ₹0.40 प्रति ग्राम था; नया मूल्य 38/90, लगभग ₹0.422 प्रति ग्राम है -- लगभग 5.6 प्रतिशत की वृद्धि। "
  "'5 प्रतिशत कमी' केवल पैकेट पर छपे मूल्य को देखता है, जो ₹40 से ₹38 हुआ; 'कोई बदलाव नहीं' मान लेता है कि छोटा पैकेट और कम मूल्य एक-दूसरे को संतुलित करते हैं; 10 प्रतिशत केवल घटे वज़न को गिनता है।",
  "qa-pp-a-smaller-pack-at-a-lower-price", _pp1,
  opts_hi=["5 प्रतिशत कमी", "कोई बदलाव नहीं", "लगभग 5.6 प्रतिशत वृद्धि", "10 प्रतिशत वृद्धि"])

def _pp2():
    s = F(9000 * 2) / (F(60, 100) * F(75, 100))
    return f"₹{int(s):,}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A person spends 40 per cent of her salary on rent and 25 per cent of what is left on food. She saves half of what then remains, and her savings come to ₹9,000. What is her salary?",
  "एक व्यक्ति अपने वेतन का 40 प्रतिशत किराये पर और बचे हुए का 25 प्रतिशत भोजन पर ख़र्च करती है। फिर जो बचता है उसका आधा वह बचाती है, और उसकी बचत ₹9,000 है। उसका वेतन कितना है?",
  ["₹30,000", "₹36,000", "₹40,000", "₹48,000"], 2,
  "After rent 60 per cent is left; food takes a quarter of that, leaving 0.6 × 0.75 = 45 per cent of the salary. Half of this, 22.5 per cent, is ₹9,000, so the salary is 9,000 ÷ 0.225 = ₹40,000. "
  "₹30,000 takes the 25 per cent on food as 25 per cent of the whole salary; ₹36,000 and ₹48,000 slip in the chain of shares.",
  "किराये के बाद 60 प्रतिशत बचता है; भोजन उसका एक-चौथाई लेता है, जिससे वेतन का 0.6 × 0.75 = 45 प्रतिशत बचता है। इसका आधा, 22.5 प्रतिशत, ₹9,000 है, इसलिए वेतन 9,000 ÷ 0.225 = ₹40,000 है। "
  "₹30,000 भोजन के 25 प्रतिशत को पूरे वेतन का 25 प्रतिशत मान लेता है; ₹36,000 और ₹48,000 भागों की कड़ी में चूकते हैं।",
  "qa-pp-what-is-left-after-shares-of-what-is-left", _pp2)

def _pp3():
    pay = 1500 * F(18, 100) - 1000 * F(18, 100)
    return f"₹{int(pay)}"
N(QA, "Percentage & Profit-Loss", "hard",
  "A trader buys goods for ₹1,000 plus 18 per cent GST and sells them for ₹1,500 plus 18 per cent GST. Under the GST rule that tax paid on purchases can be set off against tax collected on sales, how much GST must the trader pay to the government on this deal?",
  "एक व्यापारी ₹1,000 और उस पर 18 प्रतिशत जीएसटी देकर माल ख़रीदता है और उसे ₹1,500 और उस पर 18 प्रतिशत जीएसटी लेकर बेचता है। जीएसटी के इस नियम के अंतर्गत कि ख़रीद पर चुकाया कर बिक्री पर वसूले कर में समायोजित किया जा सकता है, इस सौदे पर व्यापारी को सरकार को कितना जीएसटी देना होगा?",
  ["₹90", "₹180", "₹270", "₹450"], 0,
  "The trader collects 18 per cent of ₹1,500 = ₹270 from the buyer, but has already paid 18 per cent of ₹1,000 = ₹180 to the seller. Setting the tax paid off against the tax collected leaves 270 - 180 = ₹90 -- which is 18 per cent of the ₹500 of value the trader added. "
  "₹270 forgets the set-off; ₹180 is the tax paid on the purchase; ₹450 adds the two.",
  "व्यापारी ख़रीदार से ₹1,500 का 18 प्रतिशत = ₹270 वसूलता है, पर विक्रेता को पहले ही ₹1,000 का 18 प्रतिशत = ₹180 चुका चुका है। चुकाए गए कर को वसूले गए कर में समायोजित करने पर 270 - 180 = ₹90 बचते हैं -- जो व्यापारी द्वारा जोड़े गए ₹500 के मूल्य का 18 प्रतिशत है। "
  "₹270 समायोजन भूल जाता है; ₹180 ख़रीद पर चुकाया कर है; ₹450 दोनों को जोड़ देता है।",
  "qa-pp-the-gst-a-trader-pays-over", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    t = str(sum(int("1" * k) for k in range(1, 7)))
    head, tail = t[:-3], t[-3:]                 # Indian grouping: the last three digits, then pairs
    pairs = []
    while head:
        pairs.insert(0, head[-2:]); head = head[:-2]
    return ",".join(pairs + [tail])
N(QA, "Sequences & Series", "medium",
  "What is the sum 1 + 11 + 111 + 1,111 + 11,111 + 1,11,111?",
  "योग 1 + 11 + 111 + 1,111 + 11,111 + 1,11,111 क्या है?",
  ["1,11,111", "1,21,212", "1,23,321", "1,23,456"], 3,
  "Add column by column from the right: the units column has six 1s, the tens five, the hundreds four, and so on down to one in the lakhs place. No column reaches 10, so there are no carries, and the sum reads 1, 2, 3, 4, 5, 6 from the left: 1,23,456. "
  "1,11,111 is just the last term; 1,23,321 and 1,21,212 misplace the column totals.",
  "दाईं ओर से स्तंभ-दर-स्तंभ जोड़िए: इकाई के स्तंभ में छह 1 हैं, दहाई में पाँच, सैकड़े में चार, और इसी तरह लाख के स्थान पर एक। कोई स्तंभ 10 तक नहीं पहुँचता, इसलिए कोई हासिल नहीं, और योग बाएँ से 1, 2, 3, 4, 5, 6 पढ़ा जाता है: 1,23,456। "
  "1,11,111 केवल अंतिम पद है; 1,23,321 और 1,21,212 स्तंभों के योग ग़लत जगह रखते हैं।",
  "qa-ss-a-sum-of-repunits", _ss1)

def _ss2():
    s = [1, 2]
    while len(s) < 7:
        s.append(s[-1] * s[-2])
    assert s[:6] == [1, 2, 2, 4, 8, 32]
    return str(s[6])
N(QA, "Sequences & Series", "medium",
  "What is the next number in the series 1, 2, 2, 4, 8, 32, ...?",
  "श्रेणी 1, 2, 2, 4, 8, 32, ... की अगली संख्या क्या है?",
  ["64", "128", "256", "512"], 2,
  "After the first two, each term is the product of the two before it: 1 × 2 = 2, 2 × 2 = 4, 2 × 4 = 8, 4 × 8 = 32, and so the next is 8 × 32 = 256. "
  "64 doubles the last term; 128 multiplies it by 4; 512 multiplies it by 16.",
  "पहले दो के बाद हर पद अपने से पहले के दो पदों का गुणनफल है: 1 × 2 = 2, 2 × 2 = 4, 2 × 4 = 8, 4 × 8 = 32, और इसलिए अगला 8 × 32 = 256 है। "
  "64 अंतिम पद को दोगुना करता है; 128 उसे 4 से गुणा करता है; 512 उसे 16 से।",
  "qa-ss-a-series-of-products", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    def pairings(xs):
        if not xs:
            return 1
        first, rest = xs[0], xs[1:]
        return sum(pairings(rest[:i] + rest[i + 1:]) for i in range(len(rest)))
    n = pairings(list("ABCDEF"))
    assert n == math.factorial(6) // (2 ** 3 * math.factorial(3))
    return str(n)
N(QA, "Permutation & Combination", "hard",
  "In how many ways can six people be split into three pairs (the order of the pairs, and of the two people within a pair, does not matter)?",
  "छह लोगों को तीन जोड़ों में कितने तरीक़ों से बाँटा जा सकता है (जोड़ों का क्रम, और किसी जोड़े के दोनों लोगों का क्रम, मायने नहीं रखता)?",
  ["15", "30", "45", "90"], 0,
  "Take any one person: her partner can be chosen in 5 ways. Of the four left, take one: his partner can be chosen in 3 ways. The last two form the third pair. So there are 5 × 3 × 1 = 15 splits. "
  "90 = 6C2 × 4C2 × 2C2 counts the same three pairs in each of their 3! = 6 orders; 45 and 30 remove only part of that over-counting.",
  "किसी एक व्यक्ति को लीजिए: उसका साथी 5 तरीक़ों से चुना जा सकता है। बचे चार में से एक को लीजिए: उसका साथी 3 तरीक़ों से। अंतिम दो तीसरा जोड़ा बनाते हैं। अतः 5 × 3 × 1 = 15 बँटवारे हैं। "
  "90 = 6C2 × 4C2 × 2C2 उन्हीं तीन जोड़ों को उनके 3! = 6 क्रमों में से हर एक में गिनता है; 45 और 30 उस अधिक गिनती का केवल एक भाग हटाते हैं।",
  "qa-pc-six-people-paired-off", _pc1)

def _pc2():
    return str(len(list(combinations_with_replacement(range(5), 3))))
N(QA, "Permutation & Combination", "hard",
  "An ice-cream shop has 5 flavours. A cup holds 3 scoops, and the same flavour may be chosen more than once. If the order of the scoops does not matter, how many different cups can be made?",
  "एक आइसक्रीम की दुकान में 5 स्वाद हैं। एक कप में 3 स्कूप आते हैं, और एक ही स्वाद एक से अधिक बार चुना जा सकता है। यदि स्कूपों का क्रम मायने नहीं रखता, तो कितने अलग-अलग कप बनाए जा सकते हैं?",
  ["10", "15", "20", "35"], 3,
  "Count by how many flavours are used. Three different flavours: 5C3 = 10 cups. Two flavours, one of them twice: 5 choices for the doubled flavour and 4 for the other, 20 cups. One flavour three times: 5 cups. In all 10 + 20 + 5 = 35 (the same as 7C3). "
  "10 forbids repeats; 20 counts only the cups with a repeated flavour; 15 has no basis.",
  "प्रयुक्त स्वादों की संख्या से गिनिए। तीन अलग स्वाद: 5C3 = 10 कप। दो स्वाद, उनमें से एक दो बार: दोहराए स्वाद के 5 विकल्प और दूसरे के 4, यानी 20 कप। एक ही स्वाद तीन बार: 5 कप। कुल 10 + 20 + 5 = 35 (जो 7C3 के बराबर है)। "
  "10 दोहराव की अनुमति नहीं देता; 20 केवल दोहराए स्वाद वाले कप गिनता है; 15 का कोई आधार नहीं।",
  "qa-pc-scoops-chosen-with-repeats", _pc2)

def _pc3():
    p = F(7 * 6 * 5, 7 ** 3)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "medium",
  "Three people are chosen at random. Assuming that each is equally likely to have been born on any day of the week, what is the probability that all three were born on different days of the week?",
  "तीन लोगों को यादृच्छिक रूप से चुना जाता है। यह मानते हुए कि हर एक के सप्ताह के किसी भी दिन जन्म की संभावना समान है, इसकी प्रायिकता क्या है कि तीनों का जन्म सप्ताह के अलग-अलग दिनों में हुआ?",
  ["1/7", "30/49", "5/7", "6/7"], 1,
  "The first person may have any day; the second must avoid it, with probability 6/7; the third must avoid both, with probability 5/7. So the probability is 6/7 × 5/7 = 30/49. "
  "6/7 checks only the first two people; 5/7 checks only the third; 1/7 is the chance that two given people share a day.",
  "पहले व्यक्ति का कोई भी दिन हो सकता है; दूसरे को उससे बचना है, प्रायिकता 6/7; तीसरे को दोनों से बचना है, प्रायिकता 5/7। अतः प्रायिकता 6/7 × 5/7 = 30/49 है। "
  "6/7 केवल पहले दो लोगों को जाँचता है; 5/7 केवल तीसरे को; 1/7 यह संभावना है कि दो दिए गए लोगों का दिन एक हो।",
  "qa-pc-three-birthdays-on-different-weekdays", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (3)
def _gm1():
    vol_m3 = F(22, 7) * F(7, 2) ** 2 * 4
    assert vol_m3 == 154
    litres = int(vol_m3 * 1000)
    t = str(litres)
    return "1,54,000 litres" if t == "154000" else t
N(QA, "Geometry & Mensuration", "medium",
  "A cylindrical water tank has an inner radius of 3.5 m and a depth of 4 m. How many litres of water does it hold when full? (Take π = 22/7.)",
  "एक बेलनाकार पानी की टंकी की भीतरी त्रिज्या 3.5 मीटर और गहराई 4 मीटर है। भरी होने पर उसमें कितने लीटर पानी आता है? (π = 22/7 लीजिए।)",
  ["15,400 litres", "1,54,000 litres", "15,40,000 litres", "1,54,00,000 litres"], 1,
  "The volume is πr²h = 22/7 × 3.5 × 3.5 × 4 = 154 m³. One cubic metre holds 1,000 litres, so the tank holds 154 × 1,000 = 1,54,000 litres. "
  "15,400 litres takes a cubic metre as 100 litres; 15,40,000 litres takes it as 10,000; 1,54,00,000 litres multiplies by 1,00,000.",
  "आयतन πr²h = 22/7 × 3.5 × 3.5 × 4 = 154 घन मीटर है। एक घन मीटर में 1,000 लीटर आते हैं, इसलिए टंकी में 154 × 1,000 = 1,54,000 लीटर आता है। "
  "15,400 लीटर एक घन मीटर को 100 लीटर मानता है; 15,40,000 लीटर उसे 10,000 मानता है; 1,54,00,000 लीटर 1,00,000 से गुणा करता है।",
  "qa-gm-the-litres-in-a-cylindrical-tank", _gm1,
  opts_hi=["15,400 लीटर", "1,54,000 लीटर", "15,40,000 लीटर", "1,54,00,000 लीटर"])

def _gm2():
    tris = set()
    for a in range(1, 179):
        for b in range(1, 179):
            cc = 180 - a - b
            if cc > 0 and 40 in (a, b, cc) and len({a, b, cc}) < 3:
                tris.add(tuple(sorted((a, b, cc))))
    assert tris == {(40, 40, 100), (40, 70, 70)}
    return "Either 70° and 70°, or 40° and 100°"
T(QA, "Geometry & Mensuration", "hard",
  "One angle of an isosceles triangle is 40°. What are its other two angles?",
  "एक समद्विबाहु त्रिभुज का एक कोण 40° है। उसके बाक़ी दो कोण क्या हैं?",
  ["Either 70° and 70°, or 40° and 100°", "70° and 70°, and nothing else", "40° and 100°, and nothing else",
   "It cannot be isosceles, since 40° does not divide 180°"],
  ["या तो 70° और 70°, या 40° और 100°", "70° और 70°, और कुछ नहीं", "40° और 100°, और कुछ नहीं",
   "वह समद्विबाहु नहीं हो सकता, क्योंकि 40°, 180° को विभाजित नहीं करता"],
  0,
  "The 40° angle may be the odd angle, between the two equal sides, leaving 140° to be shared equally: 70° and 70°. Or it may be one of the two equal angles, so that another angle is also 40° and the third is 180° - 80° = 100°. Both triangles exist. "
  "Each single answer misses one of the two cases; and nothing requires the angles of an isosceles triangle to divide 180°.",
  "40° का कोण विषम कोण हो सकता है, दो बराबर भुजाओं के बीच, जिससे 140° बराबर बँटता है: 70° और 70°। या वह दो बराबर कोणों में से एक हो सकता है, जिससे एक और कोण भी 40° है और तीसरा 180° - 80° = 100°। दोनों त्रिभुज संभव हैं। "
  "हर अकेला उत्तर दोनों में से एक स्थिति चूक जाता है; और कोई नियम नहीं कहता कि समद्विबाहु त्रिभुज के कोण 180° को विभाजित करें।",
  "qa-gm-an-isosceles-triangle-with-one-angle-of-40", pos=3, check=_gm2)

def _gm3():
    pts = [(0, 0), (4, 0), (4, 3), (0, 5)]
    area = abs(sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))) / 2
    return str(int(area))
N(QA, "Geometry & Mensuration", "easy",
  "A plot has corners at the points (0, 0), (4, 0), (4, 3) and (0, 5), the units being metres. What is its area in square metres?",
  "एक भूखंड के कोने बिंदुओं (0, 0), (4, 0), (4, 3) और (0, 5) पर हैं, इकाइयाँ मीटर में। उसका क्षेत्रफल वर्ग मीटर में क्या है?",
  ["16", "20", "24", "32"], 0,
  "Two sides are vertical (x = 0 and x = 4), so the plot is a trapezium with parallel sides of 5 m and 3 m, 4 m apart: area = 4 × (5 + 3)/2 = 16 m². "
  "20 takes the plot as a 4 × 5 rectangle; 32 forgets to halve the sum of the parallel sides; 24 has no basis.",
  "दो भुजाएँ ऊर्ध्वाधर हैं (x = 0 और x = 4), इसलिए भूखंड एक समलंब है जिसकी समांतर भुजाएँ 5 मीटर और 3 मीटर हैं, 4 मीटर की दूरी पर: क्षेत्रफल = 4 × (5 + 3)/2 = 16 वर्ग मीटर। "
  "20 भूखंड को 4 × 5 का आयत मान लेता है; 32 समांतर भुजाओं के योग का आधा करना भूल जाता है; 24 का कोई आधार नहीं।",
  "qa-gm-a-quadrilateral-from-its-corners", _gm3)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    t = 1 + F(3 * 4 - 3 * 1, 2)
    return f"{float(t):g} hours"
N(QA, "Time & Work", "medium",
  "Three identical sprinklers together water a lawn in 4 hours. After they have been running for 1 hour, one of them breaks down, and the other two carry on. How long does it take to water the whole lawn?",
  "तीन एक जैसे स्प्रिंकलर मिलकर एक लॉन को 4 घंटे में सींचते हैं। 1 घंटा चलने के बाद उनमें से एक ख़राब हो जाता है, और बाक़ी दो चलते रहते हैं। पूरे लॉन को सींचने में कितना समय लगता है?",
  ["4.5 hours", "5 hours", "5.5 hours", "6 hours"], 2,
  "The lawn needs 3 × 4 = 12 sprinkler-hours. The first hour supplies 3 of them, leaving 9, which two sprinklers supply in 4.5 hours. The total is 1 + 4.5 = 5.5 hours. "
  "4.5 hours forgets the first hour; 6 hours would be the time with two sprinklers from the start; 5 hours has no basis.",
  "लॉन को 3 × 4 = 12 स्प्रिंकलर-घंटे चाहिए। पहला घंटा उनमें से 3 देता है, 9 बचते हैं, जिन्हें दो स्प्रिंकलर 4.5 घंटे में देते हैं। कुल 1 + 4.5 = 5.5 घंटे। "
  "4.5 घंटे पहला घंटा भूल जाता है; 6 घंटे आरंभ से ही दो स्प्रिंकलर होने पर लगने वाला समय है; 5 घंटे का कोई आधार नहीं।",
  "qa-tw-sprinklers-when-one-breaks", _tw1,
  opts_hi=["4.5 घंटे", "5 घंटे", "5.5 घंटे", "6 घंटे"])

def _tw2():
    extra = F(10000 // 5 - 8 * 200, 300)
    assert extra == F(4, 3)
    return "9 hours 20 minutes"
N(QA, "Time & Work", "medium",
  "A worker earns ₹200 an hour for the first 8 hours of a day and one and a half times that rate for every hour beyond 8. She works the same number of hours on each of 5 days and earns ₹10,000 in all. How long does she work each day?",
  "एक कामगार दिन के पहले 8 घंटों के लिए ₹200 प्रति घंटा और 8 के बाद के हर घंटे के लिए उसकी डेढ़ गुनी दर पाती है। वह 5 दिनों में से हर दिन बराबर घंटे काम करती है और कुल ₹10,000 कमाती है। वह हर दिन कितने समय काम करती है?",
  ["9 hours", "9 hours 20 minutes", "9 hours 30 minutes", "10 hours"], 1,
  "She earns ₹2,000 a day. The first 8 hours bring ₹1,600, leaving ₹400 at the overtime rate of ₹300 an hour: 4/3 hours, or 1 hour 20 minutes. So she works 9 hours 20 minutes a day. "
  "10 hours pays the extra time at the ordinary ₹200; 9 hours and 9 hours 30 minutes do not give ₹2,000.",
  "वह प्रतिदिन ₹2,000 कमाती है। पहले 8 घंटे ₹1,600 देते हैं, ₹400 ओवरटाइम दर ₹300 प्रति घंटा पर बचते हैं: 4/3 घंटे, यानी 1 घंटा 20 मिनट। अतः वह प्रतिदिन 9 घंटे 20 मिनट काम करती है। "
  "10 घंटे अतिरिक्त समय का भुगतान साधारण ₹200 पर करता है; 9 घंटे और 9 घंटे 30 मिनट से ₹2,000 नहीं बनते।",
  "qa-tw-a-day-s-pay-with-overtime", _tw2,
  opts_hi=["9 घंटे", "9 घंटे 20 मिनट", "9 घंटे 30 मिनट", "10 घंटे"])

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    h, m = 3, 40
    total = (12 * 60 - (h * 60 + m)) % (12 * 60)
    return f"{total // 60}:{total % 60:02d}"
N(QA, "Puzzle Hybrid", "easy",
  "A clock with ordinary hands shows 3:40. What time does its reflection in a mirror appear to show?",
  "सामान्य सुइयों वाली एक घड़ी 3:40 दिखाती है। दर्पण में उसका प्रतिबिंब कौन-सा समय दिखाता प्रतीत होता है?",
  ["3:20", "8:20", "8:40", "9:20"], 1,
  "A mirror reverses the dial left to right, so a time and its mirror image add up to 12:00. 12:00 - 3:40 = 8:20. "
  "8:40 reverses only the hour hand; 9:20 and 3:20 reverse only one of the hands or slip by an hour.",
  "दर्पण डायल को बाएँ-दाएँ उलट देता है, इसलिए कोई समय और उसका दर्पण-प्रतिबिंब मिलकर 12:00 बनाते हैं। 12:00 - 3:40 = 8:20। "
  "8:40 केवल घंटे की सुई उलटता है; 9:20 और 3:20 केवल एक सुई उलटते हैं या एक घंटे से चूकते हैं।",
  "qa-ph-a-clock-in-a-mirror", _ph1)

def _ph2():
    from functools import lru_cache
    times = (1, 2, 5, 10)
    @lru_cache(None)
    def best(left):
        if len(left) <= 2:
            return max(left)
        out = 10 ** 9
        for pair in combinations(left, 2):
            rest = tuple(x for x in left if x not in pair)
            over = tuple(sorted(set(times) - set(rest)))
            for back in over:
                out = min(out, max(pair) + back + best(tuple(sorted(rest + (back,)))))
        return out
    return f"{best(times)} minutes"
N(QA, "Puzzle Hybrid", "hard",
  "Four people must cross a narrow bridge at night. At most two can cross at a time, and every crossing needs the one torch, which must be carried back for the next pair. Alone they take 1, 2, 5 and 10 minutes to cross; a pair moves at the slower person's pace. What is the shortest time in which all four can get across?",
  "चार लोगों को रात में एक संकरा पुल पार करना है। एक बार में अधिक से अधिक दो पार कर सकते हैं, और हर बार पार करने के लिए एकमात्र टॉर्च चाहिए, जिसे अगले जोड़े के लिए वापस लाना पड़ता है। अकेले वे पार करने में 1, 2, 5 और 10 मिनट लेते हैं; जोड़ा धीमे व्यक्ति की चाल से चलता है। सभी चारों कम से कम कितने समय में पार कर सकते हैं?",
  ["15 minutes", "17 minutes", "18 minutes", "19 minutes"], 1,
  "Send the two fastest first (2 minutes), and the 1-minute person brings the torch back (1). Then the two slowest cross together (10), and the 2-minute person brings the torch back (2). Finally the two fastest cross again (2). Total 2 + 1 + 10 + 2 + 2 = 17 minutes. "
  "Letting the 1-minute person escort each of the others in turn takes 2 + 1 + 5 + 1 + 10 = 19 minutes: the saving comes from making the 5- and 10-minute people cross together. 15 minutes is not possible; 18 minutes has no basis.",
  "पहले दो सबसे तेज़ लोगों को भेजिए (2 मिनट), और 1 मिनट वाला टॉर्च वापस लाता है (1)। फिर दो सबसे धीमे साथ पार करते हैं (10), और 2 मिनट वाला टॉर्च वापस लाता है (2)। अंत में दो सबसे तेज़ फिर पार करते हैं (2)। कुल 2 + 1 + 10 + 2 + 2 = 17 मिनट। "
  "1 मिनट वाले को बारी-बारी से बाक़ी सबके साथ भेजने में 2 + 1 + 5 + 1 + 10 = 19 मिनट लगते हैं: बचत 5 और 10 मिनट वालों को साथ पार कराने से आती है। 15 मिनट संभव नहीं; 18 मिनट का कोई आधार नहीं।",
  "qa-ph-four-people-and-one-torch", _ph2,
  opts_hi=["15 मिनट", "17 मिनट", "18 मिनट", "19 मिनट"])

def _ph3():
    extra = lambda r: 2 * math.pi * (r + 1) - 2 * math.pi * r
    assert abs(extra(6371000) - extra(1) ) < 1e-6 and abs(extra(1) - 6.283) < 1e-3
    return "About 6.3 m"
T(QA, "Puzzle Hybrid", "hard",
  "A rope is stretched tightly round the Earth along the equator. It is then lengthened so that it can be held all the way round at a height of 1 m above the ground. Roughly how much longer must the rope be made?",
  "एक रस्सी भूमध्य रेखा के साथ पृथ्वी के चारों ओर कसकर लपेटी गई है। फिर उसे इतना लंबा किया जाता है कि उसे चारों ओर ज़मीन से 1 मीटर ऊपर थामा जा सके। रस्सी को लगभग कितना लंबा करना होगा?",
  ["About 6.3 m", "About 1 m", "About 63 km", "It depends on the size of the Earth, which is not given"],
  ["लगभग 6.3 मीटर", "लगभग 1 मीटर", "लगभग 63 किमी", "यह पृथ्वी के आकार पर निर्भर है, जो दिया नहीं गया"],
  0,
  "A circle of radius r has circumference 2πr, so raising the rope by 1 m all round makes its radius r + 1 and its length 2π(r + 1) -- longer by 2π × 1, about 6.3 m, whatever r is. The size of the Earth cancels out. "
  "63 km is the kind of figure intuition expects for so large a circle; 1 m forgets the factor 2π; and the size of the Earth is not needed.",
  "त्रिज्या r वाले वृत्त की परिधि 2πr है, इसलिए रस्सी को चारों ओर 1 मीटर ऊपर उठाने से उसकी त्रिज्या r + 1 और लंबाई 2π(r + 1) हो जाती है -- 2π × 1, यानी लगभग 6.3 मीटर अधिक, r चाहे जो हो। पृथ्वी का आकार कट जाता है। "
  "63 किमी वैसा आँकड़ा है जिसकी अंतर्ज्ञान इतने बड़े वृत्त के लिए अपेक्षा करता है; 1 मीटर गुणनखंड 2π भूल जाता है; और पृथ्वी के आकार की आवश्यकता नहीं।",
  "qa-ph-a-rope-round-the-earth", pos=0, check=_ph3)

def _ph4():
    gain = (7000 - 6000) + (9000 - 8000)
    assert (7000 + 9000) - (6000 + 8000) == gain
    return f"₹{gain // 1000} thousand profit"
N(QA, "Puzzle Hybrid", "medium",
  "A man buys a bicycle for ₹6,000 and sells it for ₹7,000. He then buys it back for ₹8,000 and sells it again for ₹9,000. In thousands of rupees, what is his overall gain or loss?",
  "एक व्यक्ति ₹6,000 में एक साइकिल ख़रीदकर ₹7,000 में बेचता है। फिर वह उसे ₹8,000 में वापस ख़रीदता है और ₹9,000 में फिर बेच देता है। हज़ार रुपये में उसका कुल लाभ या हानि क्या है?",
  ["₹1 thousand loss", "No profit, no loss", "₹1 thousand profit", "₹2 thousand profit"], 3,
  "Treat the two deals separately: bought at 6 and sold at 7 is a gain of 1; bought at 8 and sold at 9 is another gain of 1. In all he gains ₹2 thousand (he paid out 14 and took in 16). "
  "₹1 thousand profit counts the ₹1,000 by which he bought back above his own selling price as a loss set against the two gains -- but that money was not lost, it bought the bicycle he then sold; the other answers have no basis.",
  "दोनों सौदों को अलग देखिए: 6 में ख़रीदकर 7 में बेचना 1 का लाभ है; 8 में ख़रीदकर 9 में बेचना 1 का और लाभ। कुल मिलाकर उसे ₹2 हज़ार का लाभ होता है (उसने 14 दिए और 16 लिए)। "
  "₹1 हज़ार लाभ उस ₹1,000 को, जितना ऊपर उसने अपने ही बिक्री मूल्य से वापस ख़रीदा, दोनों लाभों के सामने हानि मान लेता है -- पर वह धन खोया नहीं गया, उससे वह साइकिल ख़रीदी गई जिसे उसने फिर बेचा; बाक़ी उत्तरों का कोई आधार नहीं।",
  "qa-ph-buying-and-selling-the-same-item-twice", _ph4,
  opts_hi=["₹1 हज़ार हानि", "न लाभ न हानि", "₹1 हज़ार लाभ", "₹2 हज़ार लाभ"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    pairs = [(x, y) for x in range(-30, 31) for y in range(-30, 31)]
    s1 = {x + y for x, y in pairs if x - y == 4}
    s2 = {x + y for x, y in pairs if x * x - y * y == 48}
    both = {x + y for x, y in pairs if x - y == 4 and x * x - y * y == 48}
    assert both == {12}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the value of x + y?",
   "x + y का मान क्या है?",
   "x - y = 4.", "x - y = 4।",
   "x² - y² = 48.", "x² - y² = 48।",
   2,
   "Statement I gives only the difference of x and y. Statement II alone allows many pairs (8 and 4, but also 7 and 1, -7 and -1, and others), with different sums. Together, x² - y² = (x + y)(x - y), so x + y = 48 ÷ 4 = 12 (x = 8, y = 4). Both are needed.",
   "कथन I केवल x और y का अंतर देता है। कथन II अकेला कई जोड़ों की अनुमति देता है (8 और 4, पर 7 और 1, -7 और -1 तथा अन्य भी), जिनके योग अलग हैं। दोनों साथ: x² - y² = (x + y)(x - y), इसलिए x + y = 48 ÷ 4 = 12 (x = 8, y = 4)। दोनों आवश्यक हैं।",
   "qa-ds-a-sum-from-a-difference-and-a-difference-of-squares", _ds1)

def _ds2():
    import itertools
    sets = [b for b in itertools.combinations_with_replacement(range(2, 11), 5) if max(b) == 10 and min(b) == 2]
    s1 = {F(sum(b), 5) for b in itertools.combinations_with_replacement(range(1, 11), 5) if max(b) == 10}
    s2 = {F(sum(b), 5) for b in itertools.combinations_with_replacement(range(2, 20), 5) if min(b) == 2}
    both = {F(sum(b), 5) for b in sets}
    assert len(both) > 1
    return _ds(s1, s2, both)
DS(QA, "easy",
   "What is the average weight of five boxes?",
   "पाँच बक्सों का औसत भार क्या है?",
   "The heaviest box weighs 10 kg.", "सबसे भारी बक्सा 10 किग्रा का है।",
   "The lightest box weighs 2 kg.", "सबसे हल्का बक्सा 2 किग्रा का है।",
   3,
   "Even together the statements fix only the two extreme weights; the other three boxes may weigh anything from 2 kg to 10 kg, so the average may be anywhere from 3.6 kg to 8.4 kg. The question cannot be answered.",
   "दोनों कथन साथ मिलकर भी केवल दो चरम भार तय करते हैं; बाक़ी तीन बक्से 2 किग्रा से 10 किग्रा तक कुछ भी हो सकते हैं, इसलिए औसत 3.6 किग्रा से 8.4 किग्रा के बीच कहीं भी हो सकता है। प्रश्न का उत्तर नहीं दिया जा सकता।",
   "qa-ds-an-average-from-the-heaviest-and-the-lightest", _ds2)
