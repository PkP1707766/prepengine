# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 3 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Same mix as Tests 1 and 2 (playbook B.7) with none of their question shapes: a factorial sum's remainder,
x² - y² factor pairs, remainders a fixed amount short of each divisor, squares as the numbers with an odd count
of divisors, odd divisors, a remainder carried from 136 to 17, reversed digits, four powers compared, pole and
platform, the bird between two cyclists, an escalator, stoppages, incomes and spending, a batting average,
2A = 3B = 4C, water added to change a ratio, two vessels mixed, price and consumption, a chain of sales, savings
that do not change, a GP, a wrong term, grid routes, prizes with repeats, a sliding ladder, an incircle, men and
women at work, work on alternate days, an unanswerable sets question, socks in the dark, two purchases, and
'twice as old as B was when'. The build spreads the topics through the paper (csat_common.interleave).
Difficulty 3 easy / 19 medium / 12 hard; every key is worked out in code by check()."""
import math
from fractions import Fraction as F
from itertools import product
import csat_common as c
from csat_common import N, S2, DS, QA

def ndiv(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)

def _two(one, two):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _only(values):
    """The single value a check produced, or '?' if the data allow more than one."""
    values = set(values)
    return str(values.pop()) if len(values) == 1 else "?"

# ---------------------------------------------------------------- Number Theory (8)
N(QA, "Number Theory", "medium",
  "What is the remainder when 1! + 2! + 3! + ... + 50! is divided by 12?",
  "1! + 2! + 3! + ... + 50! को 12 से भाग देने पर शेषफल क्या होगा?",
  ["0", "1", "3", "9"], 3,
  "From 4! = 24 onwards every factorial contains 4! and so is a multiple of 12. Only 1! + 2! + 3! = 1 + 2 + 6 = 9 is left over, and 9 is less than 12, so the remainder is 9. "
  "0 assumes every term is a multiple of 12 and misses the first three; 3 stops at 1! + 2!, forgetting that 3! = 6 is not a multiple of 12; 1 counts 1! alone.",
  "4! = 24 से आगे हर क्रमगुणित में 4! शामिल है, इसलिए वह 12 का गुणज है। केवल 1! + 2! + 3! = 1 + 2 + 6 = 9 बचता है, और 9, 12 से छोटा है, अतः शेषफल 9 है। "
  "0 मान लेता है कि हर पद 12 का गुणज है और पहले तीन पद भूल जाता है; 3, 1! + 2! पर रुक जाता है, यह भूलकर कि 3! = 6, 12 का गुणज नहीं है; 1 केवल 1! गिनता है।",
  "qa-nt-factorial-sum-mod-12", lambda: str(sum(math.factorial(k) for k in range(1, 51)) % 12))

def _nt2():
    pairs = [(x, y) for x in range(1, 100) for y in range(1, 100) if x * x - y * y == 45]
    assert sum(1 for x in range(-99, 100) for y in range(-99, 100) if x * x - y * y == 45) == 12   # the '12' distractor
    return str(len(pairs))
N(QA, "Number Theory", "hard",
  "How many pairs of positive integers (x, y) satisfy x² - y² = 45?",
  "धनात्मक पूर्णांकों के कितने युग्म (x, y) समीकरण x² - y² = 45 को संतुष्ट करते हैं?",
  ["2", "3", "6", "12"], 1,
  "x² - y² = (x - y)(x + y) = 45, where x + y is larger than x - y and both are positive. The factor pairs of 45 are 1 × 45, 3 × 15 and 5 × 9, giving (x, y) = (23, 22), (9, 6) and (7, 2): three pairs. "
  "6 counts each of the six divisors of 45 as if it gave a pair, including the orders in which x - y would exceed x + y; 12 also lets x and y be negative; 2 misses the pair that comes from 1 × 45.",
  "x² - y² = (x - y)(x + y) = 45, जहाँ x + y, x - y से बड़ा है और दोनों धनात्मक हैं। 45 के गुणनखंड-युग्म 1 × 45, 3 × 15 और 5 × 9 हैं, जिनसे (x, y) = (23, 22), (9, 6) और (7, 2) मिलते हैं: तीन युग्म। "
  "6, 45 के छहों भाजकों को ऐसे गिनता है मानो हर एक से एक युग्म बनता हो, उन क्रमों सहित जिनमें x - y, x + y से बड़ा हो जाता; 12, x और y को ऋणात्मक भी होने देता है; 2, 1 × 45 से बनने वाला युग्म छोड़ देता है।",
  "qa-nt-difference-of-squares-45", _nt2)

N(QA, "Number Theory", "medium",
  "What is the smallest positive number that leaves remainders of 4, 6 and 13 when divided by 6, 8 and 15 respectively?",
  "वह सबसे छोटी धनात्मक संख्या कौन-सी है जो 6, 8 और 15 से भाग देने पर क्रमशः 4, 6 और 13 शेषफल छोड़ती है?",
  ["118", "122", "238", "358"], 0,
  "Each remainder is 2 less than its divisor (6 - 4 = 8 - 6 = 15 - 13 = 2), so the number plus 2 is divisible by 6, 8 and 15, that is by their LCM, 120. The smallest such number is 120 - 2 = 118. "
  "238 (= 240 - 2) and 358 (= 360 - 2) also leave these remainders but are not the smallest; 122 adds the 2 instead of subtracting it.",
  "हर शेषफल अपने भाजक से 2 कम है (6 - 4 = 8 - 6 = 15 - 13 = 2), इसलिए संख्या में 2 जोड़ने पर वह 6, 8 और 15 से, यानी उनके LCM 120 से, विभाज्य होगी। ऐसी सबसे छोटी संख्या 120 - 2 = 118 है। "
  "238 (= 240 - 2) और 358 (= 360 - 2) भी ये शेषफल छोड़ती हैं पर सबसे छोटी नहीं हैं; 122, 2 घटाने के बजाय जोड़ देता है।",
  "qa-nt-remainders-two-short", lambda: str(next(n for n in range(1, 1000) if n % 6 == 4 and n % 8 == 6 and n % 15 == 13)))

def _nt4():
    odd = [n for n in range(1, 501) if ndiv(n) % 2]
    return _two(len(odd) == 22, all(n % 2 for n in odd))
S2(QA, "Number Theory", "medium",
   "Consider the integers from 1 to 500, both included. Which of the following statements is/are correct?",
   "1 से 500 तक के पूर्णांकों पर विचार कीजिए, दोनों सम्मिलित। निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
   ["Exactly 22 of them have an odd number of positive divisors.",
    "Every one of them that has an odd number of positive divisors is itself an odd number."],
   ["उनमें से ठीक 22 के धनात्मक भाजकों की संख्या विषम है।",
    "उनमें से जिस भी संख्या के धनात्मक भाजकों की संख्या विषम है, वह स्वयं एक विषम संख्या है।"], 0,
   "Only I is correct. Divisors come in pairs d and n/d, and one is left unpaired only when d = n/d, that is when n is a perfect square. So the numbers with an odd count of divisors are the squares "
   "1², 2², ..., 22² = 484 (23² = 529 is too big): exactly 22. II confuses an odd number of divisors with an odd number: 4, a square, has the three divisors 1, 2 and 4 but is even.",
   "केवल I सही है। भाजक जोड़ियों d और n/d में आते हैं, और कोई भाजक तभी अकेला बचता है जब d = n/d, यानी जब n पूर्ण वर्ग हो। अतः विषम संख्या में भाजकों वाली संख्याएँ वर्ग "
   "1², 2², ..., 22² = 484 हैं (23² = 529 बहुत बड़ा है): ठीक 22। II भाजकों की विषम संख्या को विषम संख्या से भ्रमित करता है: 4 एक वर्ग है, उसके तीन भाजक 1, 2 और 4 हैं, पर वह सम है।",
   "qa-nt-odd-number-of-divisors", roman=True, check=_nt4, craft="inference")

def _nt5():
    divs = [d for d in range(1, 361) if 360 % d == 0]
    assert sum(divs) == 1170 and len([d for d in divs if d % 2]) == 6
    return str(sum(d for d in divs if d % 2))
N(QA, "Number Theory", "hard",
  "What is the sum of all the odd divisors of 360?",
  "360 के सभी विषम भाजकों का योग क्या है?",
  ["6", "45", "78", "1170"], 2,
  "360 = 2³ × 3² × 5. An odd divisor can take no factor of 2, so the odd divisors are the divisors of 3² × 5 = 45: 1, 3, 5, 9, 15 and 45. Their sum is (1 + 3 + 9)(1 + 5) = 13 × 6 = 78. "
  "6 is how many odd divisors there are; 45 is the largest of them; 1170 is the sum of all the divisors of 360, odd and even.",
  "360 = 2³ × 3² × 5। विषम भाजक में 2 का कोई गुणनखंड नहीं हो सकता, इसलिए विषम भाजक 3² × 5 = 45 के भाजक हैं: 1, 3, 5, 9, 15 और 45। इनका योग (1 + 3 + 9)(1 + 5) = 13 × 6 = 78 है। "
  "6 विषम भाजकों की संख्या है; 45 उनमें सबसे बड़ा है; 1170, 360 के सभी भाजकों, सम और विषम, का योग है।",
  "qa-nt-sum-of-odd-divisors-360", _nt5)

N(QA, "Number Theory", "easy",
  "A number leaves a remainder of 36 when divided by 136. What remainder will it leave when divided by 17?",
  "कोई संख्या 136 से भाग देने पर 36 शेषफल छोड़ती है। 17 से भाग देने पर वह कितना शेषफल छोड़ेगी?",
  ["2", "8", "19", "36"], 0,
  "The number is 136k + 36 for some whole number k. Since 136 = 17 × 8, the part 136k is a multiple of 17, so the remainder comes from 36 alone: 36 = 17 × 2 + 2, remainder 2. "
  "36 keeps the old remainder, which is larger than 17; 19 subtracts 17 only once; 8 is the quotient 136 ÷ 17, not a remainder.",
  "संख्या किसी पूर्ण संख्या k के लिए 136k + 36 है। चूँकि 136 = 17 × 8, भाग 136k, 17 का गुणज है, इसलिए शेषफल केवल 36 से आता है: 36 = 17 × 2 + 2, शेषफल 2। "
  "36 पुराना शेषफल ही रखता है, जो 17 से बड़ा है; 19 केवल एक बार 17 घटाता है; 8 भागफल 136 ÷ 17 है, शेषफल नहीं।",
  "qa-nt-remainder-136-then-17", lambda: _only((136 * k + 36) % 17 for k in range(200)))

def _nt7():
    sols = [n for n in range(10, 100) if n // 10 + n % 10 == 9 and n - (10 * (n % 10) + n // 10) == 27]
    return _only(sols)
N(QA, "Number Theory", "easy",
  "The digits of a two-digit number add up to 9. When the digits are reversed, the number decreases by 27. What is the number?",
  "दो अंकों की एक संख्या के अंकों का योग 9 है। अंकों को उलटने पर संख्या 27 घट जाती है। संख्या क्या है?",
  ["36", "45", "54", "63"], 3,
  "Write the number as 10a + b. Reversed, it is 10b + a, and the fall is 9(a - b) = 27, so a - b = 3. With a + b = 9, a = 6 and b = 3: the number is 63, and 63 - 36 = 27. "
  "36 is the reversed number, which would increase by 27; 54 and 45 have digits adding up to 9 but change by only 9 when reversed.",
  "संख्या को 10a + b लिखिए। उलटने पर वह 10b + a है, और कमी 9(a - b) = 27 है, अतः a - b = 3। a + b = 9 के साथ a = 6 और b = 3: संख्या 63 है, और 63 - 36 = 27। "
  "36 उलटी संख्या है, जो 27 बढ़ जाती; 54 और 45 के अंकों का योग 9 है, पर उलटने पर वे केवल 9 बदलती हैं।",
  "qa-nt-digits-reversed-27", _nt7)

N(QA, "Number Theory", "medium",
  "Which one of the following numbers is the largest?",
  "निम्नलिखित संख्याओं में से कौन-सी सबसे बड़ी है?",
  ["6²⁰", "5²⁵", "3⁴⁰", "2⁶⁰"], 2,
  "The exponents 20, 25, 40 and 60 are all multiples of 5, so write each number as a fifth power: 6²⁰ = (6⁴)⁵ = 1296⁵, 5²⁵ = (5⁵)⁵ = 3125⁵, 3⁴⁰ = (3⁸)⁵ = 6561⁵ and 2⁶⁰ = (2¹²)⁵ = 4096⁵. "
  "The largest base inside gives the largest number: 3⁴⁰. 2⁶⁰ has the biggest exponent and 6²⁰ the biggest base, which is why each looks largest at first sight.",
  "घातांक 20, 25, 40 और 60 सभी 5 के गुणज हैं, इसलिए हर संख्या को पाँचवीं घात के रूप में लिखिए: 6²⁰ = (6⁴)⁵ = 1296⁵, 5²⁵ = (5⁵)⁵ = 3125⁵, 3⁴⁰ = (3⁸)⁵ = 6561⁵ और 2⁶⁰ = (2¹²)⁵ = 4096⁵। "
  "भीतर का सबसे बड़ा आधार सबसे बड़ी संख्या देता है: 3⁴⁰। 2⁶⁰ का घातांक सबसे बड़ा है और 6²⁰ का आधार सबसे बड़ा, इसीलिए पहली नज़र में दोनों सबसे बड़ी लगती हैं।",
  "qa-nt-largest-of-four-powers",
  lambda: max([("6²⁰", 6 ** 20), ("5²⁵", 5 ** 25), ("3⁴⁰", 3 ** 40), ("2⁶⁰", 2 ** 60)], key=lambda t: t[1])[0])

# ---------------------------------------------------------------- Speed-Distance-Time (4)
N(QA, "Speed-Distance-Time", "easy",
  "A train 150 m long passes a pole in 15 seconds and a platform in 25 seconds. How long is the platform?",
  "150 मीटर लंबी एक रेलगाड़ी एक खंभे को 15 सेकंड में और एक प्लेटफ़ॉर्म को 25 सेकंड में पार करती है। प्लेटफ़ॉर्म कितना लंबा है?",
  ["100 m", "150 m", "250 m", "375 m"], 0,
  "Passing a pole, the train covers its own length: 150 m in 15 s, so its speed is 10 m/s. Passing the platform it covers its own length and the platform's: 10 × 25 = 250 m, so the platform is 250 - 150 = 100 m. "
  "250 m forgets to take away the train's own length; 150 m is the train itself; 375 m scales the train's length by 25/10, as if the times measured the platform alone.",
  "खंभा पार करते समय रेलगाड़ी अपनी लंबाई तय करती है: 15 सेकंड में 150 मीटर, अतः उसकी चाल 10 मीटर/सेकंड है। प्लेटफ़ॉर्म पार करते समय वह अपनी और प्लेटफ़ॉर्म की लंबाई तय करती है: 10 × 25 = 250 मीटर, अतः प्लेटफ़ॉर्म 250 - 150 = 100 मीटर है। "
  "250 मीटर रेलगाड़ी की अपनी लंबाई घटाना भूल जाता है; 150 मीटर स्वयं रेलगाड़ी है; 375 मीटर रेलगाड़ी की लंबाई को 25/10 से गुणा करता है, मानो समय केवल प्लेटफ़ॉर्म को मापते हों।",
  "qa-sdt-pole-and-platform", lambda: f"{F(150, 15) * 25 - 150} m",
  opts_hi=["100 मीटर", "150 मीटर", "250 मीटर", "375 मीटर"])

N(QA, "Speed-Distance-Time", "medium",
  "Two cyclists start at the same time from two towns 60 km apart and ride towards each other at 12 km/h and 18 km/h. At that moment a bird starts from the first cyclist and flies back and forth between them at "
  "40 km/h until they meet. How far does the bird fly in all?",
  "दो साइकिल सवार एक ही समय पर 60 किमी दूर स्थित दो कस्बों से चलते हैं और 12 किमी/घंटा तथा 18 किमी/घंटा की चाल से एक-दूसरे की ओर बढ़ते हैं। उसी क्षण एक पक्षी पहले सवार के पास से उड़ता है और उनके मिलने तक "
  "40 किमी/घंटा की चाल से उनके बीच आगे-पीछे उड़ता रहता है। पक्षी कुल कितनी दूरी उड़ता है?",
  ["24 km", "36 km", "60 km", "80 km"], 3,
  "There is no need to add up the bird's zigzags. The cyclists close the gap at 12 + 18 = 30 km/h, so they meet after 60/30 = 2 hours, and the bird, flying all that time at 40 km/h, covers 80 km. "
  "24 km and 36 km are the distances the two cyclists ride in those 2 hours; 60 km is the gap between the towns.",
  "पक्षी के आगे-पीछे के टुकड़ों को जोड़ने की ज़रूरत नहीं। सवार 12 + 18 = 30 किमी/घंटा से दूरी घटाते हैं, इसलिए 60/30 = 2 घंटे में मिलते हैं, और पक्षी पूरे समय 40 किमी/घंटा से उड़कर 80 किमी तय करता है। "
  "24 किमी और 36 किमी वे दूरियाँ हैं जो दोनों सवार उन 2 घंटों में तय करते हैं; 60 किमी कस्बों के बीच की दूरी है।",
  "qa-sdt-bird-between-cyclists", lambda: f"{40 * F(60, 12 + 18)} km",
  opts_hi=["24 किमी", "36 किमी", "60 किमी", "80 किमी"])

def _sdt3():
    e = F(15 * 2 - 20 * 1, 20 - 15)              # 20(1 + e) = 15(2 + e)
    assert 20 * (1 + e) == 15 * (2 + e)
    return str(20 * (1 + e))
N(QA, "Speed-Distance-Time", "hard",
  "A boy walks up an escalator that is moving upwards. Taking one step a second, he reaches the top in 20 seconds; taking two steps a second, he reaches the top in 15 seconds. "
  "How many steps of the escalator are visible from the bottom to the top?",
  "एक लड़का ऊपर की ओर चलती एस्केलेटर पर चढ़ता है। एक सेकंड में एक सीढ़ी चढ़ते हुए वह 20 सेकंड में ऊपर पहुँचता है; एक सेकंड में दो सीढ़ियाँ चढ़ते हुए 15 सेकंड में। "
  "नीचे से ऊपर तक एस्केलेटर की कितनी सीढ़ियाँ दिखाई देती हैं?",
  ["30", "40", "60", "120"], 2,
  "Let the escalator carry e steps a second. The visible steps are covered by the boy's own steps plus the escalator's: 20 × 1 + 20e on the slow climb and 15 × 2 + 15e on the fast one. "
  "So 20 + 20e = 30 + 15e, giving e = 2 and 20 + 40 = 60 steps. 30 counts only the boy's steps on the fast climb and 40 only the escalator's on the slow one; 120 adds the two climbs together.",
  "मान लीजिए एस्केलेटर एक सेकंड में e सीढ़ियाँ ले जाती है। दिखाई देने वाली सीढ़ियाँ लड़के की अपनी सीढ़ियों और एस्केलेटर की सीढ़ियों से मिलकर तय होती हैं: धीमी चढ़ाई में 20 × 1 + 20e और तेज़ चढ़ाई में 15 × 2 + 15e। "
  "अतः 20 + 20e = 30 + 15e, जिससे e = 2 और 20 + 40 = 60 सीढ़ियाँ। 30 तेज़ चढ़ाई में केवल लड़के की सीढ़ियाँ गिनता है और 40 धीमी चढ़ाई में केवल एस्केलेटर की; 120 दोनों चढ़ाइयों को जोड़ देता है।",
  "qa-sdt-escalator-steps", _sdt3)

N(QA, "Speed-Distance-Time", "medium",
  "Excluding stoppages, a bus runs at 54 km/h; including stoppages, its average speed is 45 km/h. For how many minutes in each hour does the bus stop?",
  "ठहराव को छोड़कर एक बस 54 किमी/घंटा की चाल से चलती है; ठहराव सहित उसकी औसत चाल 45 किमी/घंटा है। बस हर घंटे कितने मिनट रुकती है?",
  ["9", "10", "12", "15"], 1,
  "In each hour the bus covers 45 km instead of 54 km, so it loses the time it would need for 9 km at its running speed: 9/54 of an hour, or 10 minutes. "
  "9 reads the 9 km/h lost as minutes; 12 divides the loss by 45 instead of 54; 15 assumes the bus moves for 45 minutes because its average speed is 45.",
  "हर घंटे बस 54 किमी के बजाय 45 किमी तय करती है, इसलिए वह उतना समय खोती है जितना उसे अपनी चलने की चाल से 9 किमी तय करने में लगता: घंटे का 9/54 भाग, यानी 10 मिनट। "
  "9 खोए गए 9 किमी/घंटा को मिनट मान लेता है; 12 कमी को 54 के बजाय 45 से भाग देता है; 15 मान लेता है कि बस 45 मिनट चलती है क्योंकि उसकी औसत चाल 45 है।",
  "qa-sdt-bus-stoppage-minutes", lambda: str(F(54 - 45, 54) * 60))

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    xs = [x for x in range(1, 5000) if (5 * x - 1600) % 3 == 0 and 4 * x - 2 * ((5 * x - 1600) // 3) == 1600]
    assert len(xs) == 1 and (5 * xs[0] - 1600) // 3 * 2 == 4 * xs[0] - 1600   # expenditures 3y : 2y
    return f"₹{5 * xs[0]:,}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The monthly incomes of A and B are in the ratio 5 : 4, and their monthly expenditures in the ratio 3 : 2. If each of them saves ₹1,600 a month, what is A's monthly income?",
  "A और B की मासिक आय 5 : 4 के अनुपात में है, और उनका मासिक व्यय 3 : 2 के अनुपात में। यदि दोनों में से प्रत्येक हर महीने ₹1,600 बचाता है, तो A की मासिक आय क्या है?",
  ["₹2,400", "₹3,200", "₹4,000", "₹8,000"], 2,
  "Let the incomes be 5x and 4x and the expenditures 3y and 2y. Then 5x - 3y = 1600 and 4x - 2y = 1600. Multiplying the second by 3/2 gives 6x - 3y = 2400; subtracting the first leaves x = 800, and then y = 800. "
  "A earns ₹4,000 and spends ₹2,400; B earns ₹3,200 and spends ₹1,600; each saves ₹1,600. ₹2,400 is A's spending and ₹3,200 B's income; ₹8,000 treats the ₹1,600 saving as one part of the 5 : 4 ratio.",
  "आय 5x और 4x तथा व्यय 3y और 2y मानिए। तब 5x - 3y = 1600 और 4x - 2y = 1600। दूसरे को 3/2 से गुणा करने पर 6x - 3y = 2400; इसमें से पहला घटाने पर x = 800, और फिर y = 800। "
  "A ₹4,000 कमाता और ₹2,400 ख़र्च करता है; B ₹3,200 कमाता और ₹1,600 ख़र्च करता है; दोनों ₹1,600 बचाते हैं। ₹2,400, A का व्यय है और ₹3,200, B की आय; ₹8,000, ₹1,600 की बचत को 5 : 4 अनुपात का एक भाग मान लेता है।",
  "qa-rm-incomes-and-expenditures", _rm1)

N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A batsman's average after 16 innings is 36 runs. How many runs must he score in his 17th innings to raise his average by 2 runs?",
  "16 पारियों के बाद एक बल्लेबाज़ का औसत 36 रन है। अपना औसत 2 रन बढ़ाने के लिए उसे 17वीं पारी में कितने रन बनाने होंगे?",
  ["38", "68", "70", "72"], 2,
  "After 16 innings he has 16 × 36 = 576 runs; an average of 38 over 17 innings needs 17 × 38 = 646. He must score 646 - 576 = 70: the new average, 38, plus 2 more for each of the 16 earlier innings. "
  "38 is only the new average; 68 adds 2 per earlier innings to the old average instead of the new one; 72 adds 2 for all 17 innings.",
  "16 पारियों के बाद उसके 16 × 36 = 576 रन हैं; 17 पारियों में 38 का औसत चाहिए तो 17 × 38 = 646 रन। उसे 646 - 576 = 70 रन बनाने होंगे: नया औसत 38, और पहले की 16 पारियों में से हर एक के लिए 2 और। "
  "38 केवल नया औसत है; 68 पहले की हर पारी के 2 रन नए के बजाय पुराने औसत में जोड़ता है; 72 सभी 17 पारियों के लिए 2 जोड़ता है।",
  "qa-rm-batting-average-up-by-2", lambda: str(17 * 38 - 16 * 36))

def _rm3():
    shares = [(a, b, cc) for a in range(1, 1561) for b in [F(2 * a, 3)] for cc in [F(2 * a, 4)] if a + b + cc == 1560]
    assert len(shares) == 1 and shares[0][1:] == (480, 360)
    return f"₹{shares[0][0]}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "₹1,560 is divided among A, B and C so that twice A's share, three times B's share and four times C's share are all equal. What is A's share?",
  "₹1,560 को A, B और C में इस प्रकार बाँटा जाता है कि A के हिस्से का दोगुना, B के हिस्से का तीन गुना और C के हिस्से का चार गुना, तीनों बराबर हों। A का हिस्सा क्या है?",
  ["₹360", "₹480", "₹520", "₹720"], 3,
  "If 2A = 3B = 4C = k, then A = k/2, B = k/3 and C = k/4, so A : B : C = 1/2 : 1/3 : 1/4 = 6 : 4 : 3. The 13 parts make ₹1,560, so one part is ₹120 and A gets 6 × 120 = ₹720. "
  "₹480 and ₹360 are B's and C's shares; ₹520 splits the money equally.",
  "यदि 2A = 3B = 4C = k, तो A = k/2, B = k/3 और C = k/4, अतः A : B : C = 1/2 : 1/3 : 1/4 = 6 : 4 : 3। 13 भाग ₹1,560 हैं, इसलिए एक भाग ₹120 है और A को 6 × 120 = ₹720 मिलते हैं। "
  "₹480 और ₹360, B और C के हिस्से हैं; ₹520 धन को बराबर बाँट देता है।",
  "qa-rm-twice-thrice-four-times", _rm3)

def _rm4():
    milk, water = F(60 * 2, 3), F(60, 3)
    return f"{2 * milk - water} litres"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A 60-litre mixture contains milk and water in the ratio 2 : 1. How much water must be added to it to make the ratio of milk to water 1 : 2?",
  "60 लीटर के एक मिश्रण में दूध और पानी 2 : 1 के अनुपात में हैं। दूध और पानी का अनुपात 1 : 2 करने के लिए उसमें कितना पानी मिलाना होगा?",
  ["40 litres", "60 litres", "80 litres", "120 litres"], 1,
  "The mixture holds 40 litres of milk and 20 of water. Adding water leaves the milk at 40 litres, so for a ratio of 1 : 2 the water must reach 80 litres: 60 litres must be added. "
  "80 litres is the water needed in all, not the amount to add; 40 litres is the milk; 120 litres doubles the whole mixture.",
  "मिश्रण में 40 लीटर दूध और 20 लीटर पानी है। पानी मिलाने से दूध 40 लीटर ही रहता है, इसलिए 1 : 2 के अनुपात के लिए पानी 80 लीटर होना चाहिए: 60 लीटर मिलाना होगा। "
  "80 लीटर कुल आवश्यक पानी है, मिलाई जाने वाली मात्रा नहीं; 40 लीटर दूध है; 120 लीटर पूरे मिश्रण को दोगुना कर देता है।",
  "qa-rm-water-to-reverse-ratio", _rm4,
  opts_hi=["40 लीटर", "60 लीटर", "80 लीटर", "120 लीटर"])

def _rm5():
    a, b, want = F(3, 4), F(5, 8), F(2, 3)
    r = (want - b) / (a - want)
    assert (F(2) - F(5, 3)) / (F(3) - F(2)) == F(1, 3)     # the '1 : 3' slip: alligating the ratios themselves
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "Vessel A holds milk and water in the ratio 3 : 1, and vessel B holds them in the ratio 5 : 3. In what ratio should the contents of A and B be mixed to get a mixture in which milk and water are in the ratio 2 : 1?",
  "पात्र A में दूध और पानी 3 : 1 के अनुपात में हैं, और पात्र B में 5 : 3 के अनुपात में। A और B की सामग्री को किस अनुपात में मिलाया जाए कि मिश्रण में दूध और पानी 2 : 1 के अनुपात में हों?",
  ["1 : 2", "1 : 3", "2 : 1", "3 : 5"], 0,
  "Work with the fraction of milk: 3/4 in A, 5/8 in B, and 2/3 wanted. By alligation, A : B = (2/3 - 5/8) : (3/4 - 2/3) = 1/24 : 1/12 = 1 : 2. Check: 1 litre of A and 2 of B hold 3/4 + 5/4 = 2 litres of milk in 3, which is 2 : 1. "
  "2 : 1 is the answer the wrong way round; 1 : 3 comes from alligating the ratios 3, 5/3 and 2 as if they were fractions of milk; 3 : 5 simply sets the milk parts of the two vessels against each other.",
  "दूध के अंश से काम कीजिए: A में 3/4, B में 5/8, और चाहिए 2/3। एलिगेशन से A : B = (2/3 - 5/8) : (3/4 - 2/3) = 1/24 : 1/12 = 1 : 2। जाँच: A का 1 लीटर और B के 2 लीटर में 3/4 + 5/4 = 2 लीटर दूध है, 3 लीटर में, यानी 2 : 1। "
  "2 : 1 उत्तर को उलट देता है; 1 : 3 अनुपातों 3, 5/3 और 2 पर ऐसे एलिगेशन करता है मानो वे दूध के अंश हों; 3 : 5 दोनों पात्रों के दूध के भागों को ही आमने-सामने रख देता है।",
  "qa-rm-two-vessels-to-two-to-one", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
N(QA, "Percentage & Profit-Loss", "medium",
  "The price of sugar rises by 25%. By what percentage must a family cut its consumption of sugar so that its spending on sugar does not change?",
  "चीनी का मूल्य 25% बढ़ जाता है। एक परिवार को चीनी की खपत कितने प्रतिशत घटानी होगी ताकि चीनी पर उसका ख़र्च न बदले?",
  ["20%", "25%", "75%", "80%"], 0,
  "Spending = price × quantity. If the price becomes 5/4 of what it was, the quantity must become 4/5 of what it was to keep the product the same: a cut of 1/5, or 20%. "
  "25% copies the price rise, but a 25% cut at a price 25% higher leaves spending at 125% × 75% = 93.75%; 80% is the new level of consumption, not the cut; 75% is simply 100 - 25.",
  "ख़र्च = मूल्य × मात्रा। यदि मूल्य पहले का 5/4 हो जाए, तो गुणनफल वही रखने के लिए मात्रा पहले की 4/5 होनी चाहिए: 1/5, यानी 20% की कटौती। "
  "25% मूल्य वृद्धि की ही नक़ल करता है, पर 25% ऊँचे मूल्य पर 25% कटौती से ख़र्च 125% × 75% = 93.75% रह जाता है; 80% खपत का नया स्तर है, कटौती नहीं; 75% केवल 100 - 25 है।",
  "qa-pp-price-up-consumption-down", lambda: f"{(1 - 1 / F(125, 100)) * 100}%")

def _pp2():
    cp = F(4860) / (F(12, 10) * F(9, 10))
    assert cp.denominator == 1 and F(4860) / F(9, 10) == 5400 and F(4860) * F(12, 10) == 5832
    return f"₹{int(cp):,}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A sells a bicycle to B at a profit of 20%, and B sells it to C at a loss of 10%. If C pays ₹4,860 for it, how much did A pay for the bicycle?",
  "A एक साइकिल B को 20% लाभ पर बेचता है, और B उसे C को 10% हानि पर बेचता है। यदि C उसके लिए ₹4,860 देता है, तो A ने साइकिल के लिए कितना दिया था?",
  ["₹4,500", "₹4,860", "₹5,400", "₹5,832"], 0,
  "If A paid P, B paid 1.2P, and C paid 0.9 × 1.2P = 1.08P = ₹4,860, so P = 4,860/1.08 = ₹4,500. "
  "₹5,400 is what B paid (4,860/0.9); ₹4,860 is C's price; ₹5,832 multiplies C's price by 1.2 instead of working back.",
  "यदि A ने P दिया, तो B ने 1.2P दिया, और C ने 0.9 × 1.2P = 1.08P = ₹4,860 दिया, अतः P = 4,860/1.08 = ₹4,500। "
  "₹5,400 वह है जो B ने दिया (4,860/0.9); ₹4,860, C का मूल्य है; ₹5,832, पीछे की ओर गणना करने के बजाय C के मूल्य को 1.2 से गुणा कर देता है।",
  "qa-pp-chain-of-two-sales", _pp2)

def _pp3():
    before = F(100) - F(80)                          # income 100, expenditure 80
    after = F(100) * F(12, 10) - F(80) * F(125, 100)
    change = (after - before) / before * 100
    return {-5: "They fall by 5%", 0: "They stay the same", 5: "They rise by 5%", 20: "They rise by 20%"}.get(change, "?")
N(QA, "Percentage & Profit-Loss", "hard",
  "A man saves 20% of his income. His income then rises by 20% and his expenditure by 25%. What happens to his savings?",
  "एक व्यक्ति अपनी आय का 20% बचाता है। फिर उसकी आय 20% और उसका व्यय 25% बढ़ जाता है। उसकी बचत का क्या होता है?",
  ["They fall by 5%", "They stay the same", "They rise by 5%", "They rise by 20%"], 1,
  "Take his income as 100: he spends 80 and saves 20. Afterwards he earns 120 and spends 80 × 1.25 = 100, so he still saves 20 -- no change. The two rates apply to different bases: 25% of 80 is the same amount as 20% of 100. "
  "'Fall by 5%' subtracts one rate from the other (20 - 25); 'rise by 20%' assumes savings move with income; a 5% rise has no basis at all.",
  "उसकी आय 100 मानिए: वह 80 ख़र्च करता और 20 बचाता है। बाद में वह 120 कमाता है और 80 × 1.25 = 100 ख़र्च करता है, इसलिए वह अब भी 20 बचाता है -- कोई बदलाव नहीं। दोनों दरें अलग-अलग आधारों पर लगती हैं: 80 का 25% उतनी ही राशि है जितनी 100 का 20%। "
  "'5% घटती है' एक दर में से दूसरी घटा देता है (20 - 25); '20% बढ़ती है' मान लेता है कि बचत आय के साथ चलती है; 5% की वृद्धि का कोई आधार ही नहीं।",
  "qa-pp-savings-unchanged", _pp3,
  opts_hi=["वह 5% घटती है", "वह उतनी ही रहती है", "वह 5% बढ़ती है", "वह 20% बढ़ती है"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    r = round(F(192, 24) ** F(1, 3))                # r³ = 8
    assert r ** 3 == 8
    a = F(24, r ** 2)
    return str(a * r ** 9)
N(QA, "Sequences & Series", "medium",
  "In a geometric progression the 3rd term is 24 and the 6th term is 192. What is the 10th term?",
  "एक गुणोत्तर श्रेणी का तीसरा पद 24 और छठा पद 192 है। उसका दसवाँ पद क्या है?",
  ["1536", "3072", "6144", "12288"], 1,
  "From the 3rd term to the 6th the common ratio is applied three times: r³ = 192/24 = 8, so r = 2, and the first term is 24/2² = 6. The 10th term is 6 × 2⁹ = 3072. "
  "1536 and 6144 are the 9th and 11th terms, from counting the powers of 2 one short or one over; 12288 is the 12th.",
  "तीसरे पद से छठे पद तक सार्व अनुपात तीन बार लगता है: r³ = 192/24 = 8, अतः r = 2, और पहला पद 24/2² = 6 है। दसवाँ पद 6 × 2⁹ = 3072 है। "
  "1536 और 6144 नौवें और ग्यारहवें पद हैं, जो 2 की घातें एक कम या एक अधिक गिनने से आते हैं; 12288 बारहवाँ पद है।",
  "qa-ss-gp-from-third-and-sixth", _ss1)

def _ss2():
    s = [4, 6, 12, 30, 96, 315, 1260]
    fits = [i for i in range(len(s))
            if all(F(s[k + 1], s[k]) == F(3, 2) + F(k, 2) for k in range(len(s) - 1) if k != i and k + 1 != i)]
    return _only(s[i] for i in fits)
N(QA, "Sequences & Series", "hard",
  "One number in the series 4, 6, 12, 30, 96, 315, 1260 is wrong. Which one is it?",
  "श्रेणी 4, 6, 12, 30, 96, 315, 1260 में एक संख्या ग़लत है। वह कौन-सी है?",
  ["30", "96", "315", "1260"], 1,
  "The multipliers rise by 0.5 at each step: 4 × 1.5 = 6, 6 × 2 = 12, 12 × 2.5 = 30, 30 × 3 = 90, 90 × 3.5 = 315 and 315 × 4 = 1260. The fifth term should be 90: with 96, both 30 → 96 and 96 → 315 break the pattern, while every other step fits. "
  "315 looks out of place because 3.5 is not a whole number, but it is exactly 90 × 3.5; 30 and 1260 fit their neighbours on both sides.",
  "गुणक हर चरण पर 0.5 बढ़ते हैं: 4 × 1.5 = 6, 6 × 2 = 12, 12 × 2.5 = 30, 30 × 3 = 90, 90 × 3.5 = 315 और 315 × 4 = 1260। पाँचवाँ पद 90 होना चाहिए: 96 के साथ 30 → 96 और 96 → 315 दोनों क्रम तोड़ते हैं, जबकि बाक़ी हर चरण ठीक बैठता है। "
  "315 अटपटा लगता है क्योंकि 3.5 पूर्ण संख्या नहीं है, पर वह ठीक 90 × 3.5 है; 30 और 1260 अपने दोनों ओर के पदों से मेल खाते हैं।",
  "qa-ss-wrong-term-rising-multipliers", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    routes = sum(1 for m in product("EN", repeat=7) if m.count("E") == 4)
    assert routes == math.comb(7, 3) and 2 ** 7 == 128 and math.factorial(7) == 5040 and math.comb(8, 4) == 70
    return str(routes)
N(QA, "Permutation & Combination", "hard",
  "A town's streets form a grid of square blocks, 4 blocks from west to east and 3 blocks from south to north. Walking only east or north along the streets, in how many different ways can a person go "
  "from the south-west corner of the grid to its north-east corner?",
  "एक कस्बे की सड़कें वर्गाकार खंडों का एक जाल बनाती हैं, पश्चिम से पूर्व 4 खंड और दक्षिण से उत्तर 3 खंड। सड़कों पर केवल पूर्व या उत्तर की ओर चलते हुए कोई व्यक्ति जाल के दक्षिण-पश्चिमी कोने से "
  "उत्तर-पूर्वी कोने तक कितने अलग-अलग तरीकों से जा सकता है?",
  ["35", "70", "128", "5040"], 0,
  "Every such route has 7 moves, 4 of them east and 3 north, and a route is fixed by choosing which 3 of the 7 moves go north: C(7, 3) = 35. "
  "128 = 2⁷ lets each move go either way, ignoring that exactly 4 must go east; 5040 = 7! treats the 7 moves as all different; 70 = C(8, 4) is the count for a grid 4 blocks by 4.",
  "हर ऐसे रास्ते में 7 चालें हैं, 4 पूर्व की ओर और 3 उत्तर की ओर, और रास्ता यह चुनने से तय होता है कि 7 में से कौन-सी 3 चालें उत्तर की ओर हों: C(7, 3) = 35। "
  "128 = 2⁷ हर चाल को किसी भी ओर जाने देता है, यह भूलकर कि ठीक 4 पूर्व की ओर होनी चाहिए; 5040 = 7! सातों चालों को अलग-अलग मानता है; 70 = C(8, 4), 4 × 4 खंडों वाले जाल की गिनती है।",
  "qa-pc-grid-routes-4-by-3", _pc1)

N(QA, "Permutation & Combination", "medium",
  "In how many ways can 3 different prizes be given to 5 students, if a student may receive more than one prize?",
  "3 अलग-अलग पुरस्कार 5 विद्यार्थियों को कितने तरीकों से दिए जा सकते हैं, यदि एक विद्यार्थी एक से अधिक पुरस्कार पा सकता है?",
  ["15", "60", "125", "243"], 2,
  "Each of the 3 prizes can go to any of the 5 students, independently of the others: 5 × 5 × 5 = 125. "
  "60 = 5 × 4 × 3 would hold if no student could get two prizes; 243 = 3⁵ reverses the roles, as if each student chose a prize; 15 = 5 × 3 only counts student-prize pairs.",
  "3 में से हर पुरस्कार 5 में से किसी भी विद्यार्थी को, दूसरों से स्वतंत्र रूप से, जा सकता है: 5 × 5 × 5 = 125। "
  "60 = 5 × 4 × 3 तब सही होता जब कोई विद्यार्थी दो पुरस्कार न पा सकता; 243 = 3⁵ भूमिकाएँ उलट देता है, मानो हर विद्यार्थी एक पुरस्कार चुनता हो; 15 = 5 × 3 केवल विद्यार्थी-पुरस्कार जोड़ियाँ गिनता है।",
  "qa-pc-prizes-with-repeats", lambda: str(len(list(product(range(5), repeat=3)))))

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    foot0 = math.isqrt(25 ** 2 - 24 ** 2)
    foot1 = math.isqrt(25 ** 2 - 20 ** 2)
    assert foot0 ** 2 == 49 and foot1 ** 2 == 225
    return f"{foot1 - foot0} m"
N(QA, "Geometry & Mensuration", "medium",
  "A ladder 25 m long leans against a vertical wall with its top 24 m above the ground. If the top slides 4 m down the wall, how far does the foot of the ladder move away from the wall?",
  "25 मीटर लंबी एक सीढ़ी एक ऊर्ध्वाधर दीवार से इस प्रकार टिकी है कि उसका ऊपरी सिरा ज़मीन से 24 मीटर ऊँचा है। यदि ऊपरी सिरा दीवार पर 4 मीटर नीचे खिसक जाए, तो सीढ़ी का निचला सिरा दीवार से कितना और दूर खिसकेगा?",
  ["4 m", "8 m", "15 m", "20 m"], 1,
  "At first the foot is √(25² - 24²) = √49 = 7 m from the wall. With the top at 20 m, the foot is √(25² - 20²) = √225 = 15 m away, so it has moved 15 - 7 = 8 m. "
  "4 m assumes the foot moves as far as the top; 15 m is the foot's new distance from the wall, not the change; 20 m is the new height of the top.",
  "शुरू में निचला सिरा दीवार से √(25² - 24²) = √49 = 7 मीटर दूर है। ऊपरी सिरा 20 मीटर पर होने पर निचला सिरा √(25² - 20²) = √225 = 15 मीटर दूर है, अतः वह 15 - 7 = 8 मीटर खिसका है। "
  "4 मीटर मान लेता है कि निचला सिरा उतना ही खिसकता है जितना ऊपरी; 15 मीटर दीवार से निचले सिरे की नई दूरी है, बदलाव नहीं; 20 मीटर ऊपरी सिरे की नई ऊँचाई है।",
  "qa-gm-ladder-slides-down", _gm1,
  opts_hi=["4 मीटर", "8 मीटर", "15 मीटर", "20 मीटर"])

def _gm2():
    a, b, h = 7, 24, 25
    assert a * a + b * b == h * h
    s = F(a + b + h, 2)
    area = F(a * b, 2)
    return f"{area / s} cm"
N(QA, "Geometry & Mensuration", "hard",
  "The sides of a triangle are 7 cm, 24 cm and 25 cm. What is the radius of the circle that touches all three of its sides?",
  "एक त्रिभुज की भुजाएँ 7 सेमी, 24 सेमी और 25 सेमी हैं। उसकी तीनों भुजाओं को स्पर्श करने वाले वृत्त की त्रिज्या क्या है?",
  ["3 cm", "3.5 cm", "6 cm", "12.5 cm"], 0,
  "7² + 24² = 49 + 576 = 625 = 25², so the triangle is right-angled, with area ½ × 7 × 24 = 84 cm². The radius of the inscribed circle is area ÷ semi-perimeter = 84 ÷ 28 = 3 cm "
  "(for a right triangle it is also (7 + 24 - 25)/2 = 3). 12.5 cm is the radius of the circle through the corners, half the hypotenuse; 6 cm is the diameter of the inscribed circle; 3.5 cm is half the shortest side.",
  "7² + 24² = 49 + 576 = 625 = 25², इसलिए त्रिभुज समकोण है, जिसका क्षेत्रफल ½ × 7 × 24 = 84 वर्ग सेमी है। अंतःवृत्त की त्रिज्या = क्षेत्रफल ÷ अर्धपरिमाप = 84 ÷ 28 = 3 सेमी "
  "(समकोण त्रिभुज में यह (7 + 24 - 25)/2 = 3 भी है)। 12.5 सेमी शीर्षों से होकर जाने वाले वृत्त की त्रिज्या है, कर्ण का आधा; 6 सेमी अंतःवृत्त का व्यास है; 3.5 सेमी सबसे छोटी भुजा का आधा है।",
  "qa-gm-incircle-7-24-25", _gm2,
  opts_hi=["3 सेमी", "3.5 सेमी", "6 सेमी", "12.5 सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    man = F(18, 12)                                 # one man's work in woman-units
    days = F(18 * 14) / (8 * man + 16)
    assert F(12 * 14, 8 + 16) == 7 and F(18 * 14, 8 + 16) == F(21, 2)
    return str(days)
N(QA, "Time & Work", "medium",
  "12 men or 18 women can finish a piece of work in 14 days. In how many days will 8 men and 16 women together finish it?",
  "12 पुरुष या 18 महिलाएँ एक काम को 14 दिनों में पूरा कर सकते हैं। 8 पुरुष और 16 महिलाएँ मिलकर उसे कितने दिनों में पूरा करेंगे?",
  ["7", "9", "10.5", "14"], 1,
  "12 men do as much as 18 women, so 1 man = 1.5 women and 8 men = 12 women; 8 men and 16 women are thus worth 28 women. The work is 18 × 14 = 252 woman-days, so 28 women need 252 ÷ 28 = 9 days. "
  "7 treats every woman as a man (24 men for 168 man-days); 10.5 treats every man as a woman (24 women for 252 woman-days); 14 is the original time.",
  "12 पुरुष उतना काम करते हैं जितना 18 महिलाएँ, इसलिए 1 पुरुष = 1.5 महिला और 8 पुरुष = 12 महिलाएँ; अतः 8 पुरुष और 16 महिलाएँ 28 महिलाओं के बराबर हैं। काम 18 × 14 = 252 महिला-दिन है, इसलिए 28 महिलाओं को 252 ÷ 28 = 9 दिन लगेंगे। "
  "7 हर महिला को पुरुष मान लेता है (168 पुरुष-दिन के लिए 24 पुरुष); 10.5 हर पुरुष को महिला मान लेता है (252 महिला-दिन के लिए 24 महिलाएँ); 14 मूल समय है।",
  "qa-tw-men-and-women-equivalence", _tw1)

def _tw2():
    done, day = F(0), 0
    while done < 1:
        day += 1
        done += F(1, 6) if day % 2 else F(1, 12)
    assert done == 1
    return str(day)
N(QA, "Time & Work", "hard",
  "A can finish a job in 6 days and B in 12 days. They work on alternate days, A on the first day, B on the second, and so on. In how many days will the job be finished?",
  "A किसी काम को 6 दिनों में और B 12 दिनों में पूरा कर सकता है। वे बारी-बारी से एक-एक दिन काम करते हैं, पहले दिन A, दूसरे दिन B, और इसी प्रकार आगे। काम कितने दिनों में पूरा होगा?",
  ["4", "7½", "8", "12"], 2,
  "In each pair of days A does 1/6 and B 1/12, together 1/4. After 6 days, three pairs, 3/4 is done; on day 7 A adds 1/6, making 11/12; the last 1/12 is exactly one day of B's work, so the job ends with day 8. "
  "4 days is the time if both worked every day; 7½ gives day 8 to A, forgetting that it is B's turn; 12 is B's time working alone.",
  "हर दो दिनों में A, 1/6 और B, 1/12 काम करता है, मिलकर 1/4। 6 दिनों, यानी तीन जोड़ियों, के बाद 3/4 काम हो जाता है; सातवें दिन A, 1/6 जोड़कर इसे 11/12 कर देता है; शेष 1/12 ठीक B का एक दिन का काम है, इसलिए काम आठवें दिन पूरा होता है। "
  "4 दिन तब लगते जब दोनों हर दिन काम करते; 7½, आठवाँ दिन A को दे देता है, यह भूलकर कि वह B की बारी है; 12, B का अकेले काम करने का समय है।",
  "qa-tw-alternate-days", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    sizes = {25 + 20 - 10 + neither for neither in range(0, 10)}
    return "Cannot be determined" if len(sizes) > 1 else str(sizes.pop())
N(QA, "Puzzle Hybrid", "medium",
  "In a class, 25 students play cricket, 20 play football and 10 play both games. How many students are there in the class?",
  "एक कक्षा में 25 विद्यार्थी क्रिकेट खेलते हैं, 20 फ़ुटबॉल खेलते हैं और 10 दोनों खेल खेलते हैं। कक्षा में कितने विद्यार्थी हैं?",
  ["35", "45", "55", "Cannot be determined"], 3,
  "The data give the number who play at least one of the games: 25 + 20 - 10 = 35. They say nothing about students who play neither, so the class may have 35 students or more, and its size cannot be determined. "
  "35 is the trap answer, true only if every student played one of the games; 45 forgets to take away the 10 counted twice; 55 adds them instead.",
  "आँकड़े यह बताते हैं कि कम से कम एक खेल खेलने वाले कितने हैं: 25 + 20 - 10 = 35। वे उन विद्यार्थियों के बारे में कुछ नहीं कहते जो कोई भी खेल नहीं खेलते, इसलिए कक्षा में 35 या उससे अधिक विद्यार्थी हो सकते हैं, और उसका आकार निर्धारित नहीं किया जा सकता। "
  "35 जाल वाला उत्तर है, जो तभी सही होता जब हर विद्यार्थी कोई एक खेल खेलता; 45, दो बार गिने गए 10 को घटाना भूल जाता है; 55 उन्हें घटाने के बजाय जोड़ देता है।",
  "qa-ph-class-size-not-given", _ph1,
  opts_hi=["35", "45", "55", "निर्धारित नहीं किया जा सकता"])

def _ph2():
    def sure(n):                                    # 10 black, 8 white, 6 blue
        return all(k >= 2 for k in range(0, 11) for w in range(0, 9) for b in range(0, 7) if k + w + b == n)
    return str(next(n for n in range(1, 25) if sure(n)))
N(QA, "Puzzle Hybrid", "hard",
  "A drawer holds 10 black, 8 white and 6 blue socks, all mixed up. In the dark, what is the smallest number of socks one must take out to be sure of having two black socks?",
  "एक दराज़ में 10 काले, 8 सफ़ेद और 6 नीले मोज़े आपस में मिले हुए हैं। अँधेरे में, दो काले मोज़े निश्चित रूप से पाने के लिए कम से कम कितने मोज़े निकालने होंगे?",
  ["4", "14", "15", "16"], 3,
  "Plan for the worst luck: all 8 white and all 6 blue socks could come out first, 14 socks with no black one among them. The next two are then certain to be black, so 16 socks are needed. "
  "4 is enough for a pair of the same colour, not for a black pair; 14 might still contain no black sock at all; 15 makes sure of only one black sock.",
  "सबसे बुरी स्थिति मानिए: पहले सभी 8 सफ़ेद और सभी 6 नीले मोज़े निकल सकते हैं, 14 मोज़े जिनमें एक भी काला नहीं। उसके बाद के दो मोज़े निश्चित रूप से काले होंगे, अतः 16 मोज़े चाहिए। "
  "4 एक ही रंग की जोड़ी के लिए पर्याप्त है, काली जोड़ी के लिए नहीं; 14 में अब भी एक भी काला मोज़ा न हो, ऐसा हो सकता है; 15 केवल एक काला मोज़ा निश्चित करता है।",
  "qa-ph-two-black-socks-in-the-dark", _ph2)

def _ph3():
    sols = [(p, q) for p in range(1, 50) for q in range(1, 50) if 3 * p + 4 * q == 46 and 5 * p + 2 * q == 58]
    assert sols == [(10, 4)]
    return f"₹{sum(sols[0])}"
N(QA, "Puzzle Hybrid", "medium",
  "3 pens and 4 pencils cost ₹46, and 5 pens and 2 pencils cost ₹58. What do one pen and one pencil cost together?",
  "3 पेन और 4 पेंसिल का मूल्य ₹46 है, और 5 पेन और 2 पेंसिल का ₹58। एक पेन और एक पेंसिल का कुल मूल्य क्या है?",
  ["₹6", "₹10", "₹13", "₹14"], 3,
  "Doubling the second purchase gives 10 pens + 4 pencils = ₹116; taking away the first leaves 7 pens = ₹70, so a pen costs ₹10, and then 4 pencils cost 46 - 30 = ₹16, so a pencil costs ₹4. Together, ₹14. "
  "₹10 is the pen alone; ₹6 is the difference between a pen and a pencil; ₹13 divides the sum of the two purchases, 8 pens + 6 pencils = ₹104, by 8 as if both counts were 8.",
  "दूसरी ख़रीद को दोगुना करने पर 10 पेन + 4 पेंसिल = ₹116; इसमें से पहली घटाने पर 7 पेन = ₹70, अतः एक पेन ₹10 का है, और फिर 4 पेंसिल 46 - 30 = ₹16 की, यानी एक पेंसिल ₹4 की। दोनों मिलकर ₹14। "
  "₹10 केवल पेन है; ₹6 पेन और पेंसिल का अंतर है; ₹13 दोनों ख़रीदों के योग, 8 पेन + 6 पेंसिल = ₹104, को 8 से भाग देता है, मानो दोनों गिनतियाँ 8 हों।",
  "qa-ph-pens-and-pencils", _ph3)

def _ph4():
    sols = [a for a in range(1, 63) for b in [63 - a] if a > b and a == 2 * (b - (a - b))]
    return _only(sols)
N(QA, "Puzzle Hybrid", "hard",
  "A is now twice as old as B was when A was as old as B is now. The sum of their present ages is 63 years. What is A's present age in years?",
  "A की वर्तमान आयु उस समय की B की आयु की दोगुनी है जब A की आयु उतनी थी जितनी अब B की है। दोनों की वर्तमान आयु का योग 63 वर्ष है। A की वर्तमान आयु कितने वर्ष है?",
  ["18", "27", "36", "42"], 2,
  "Let A be a and B be b years old now, with a > b. A was b years old a - b years ago, when B was b - (a - b) = 2b - a. So a = 2(2b - a), that is 3a = 4b, and with a + b = 63, b = 27 and a = 36. "
  "Check: nine years ago A was 27 and B was 18, and 36 is twice 18. 42 takes A as simply twice B's present age; 27 is B's present age; 18 is B's age at that earlier time.",
  "मान लीजिए अभी A की आयु a और B की b वर्ष है, जहाँ a > b। A की आयु b वर्ष, a - b वर्ष पहले थी, जब B की आयु b - (a - b) = 2b - a थी। अतः a = 2(2b - a), यानी 3a = 4b, और a + b = 63 के साथ b = 27 और a = 36। "
  "जाँच: नौ वर्ष पहले A 27 और B 18 वर्ष का था, और 36, 18 का दोगुना है। 42, A को सीधे B की वर्तमान आयु का दोगुना मान लेता है; 27, B की वर्तमान आयु है; 18 उस पहले के समय में B की आयु है।",
  "qa-ph-twice-as-old-as-b-was", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    ys = [F(k, 2) for k in range(-20, 21)]
    s1 = {(12 - 3 * y) / 2 + y for y in ys}
    s2 = {(24 - 6 * y) / 4 + y for y in ys}
    both = {(12 - 3 * y) / 2 + y for y in ys if 4 * ((12 - 3 * y) / 2) + 6 * y == 24}
    alone = (len(s1) == 1, len(s2) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(both) == 1 else "d"
DS(QA, "medium",
   "What is the value of x + y?",
   "x + y का मान क्या है?",
   "2x + 3y = 12", "2x + 3y = 12",
   "4x + 6y = 24", "4x + 6y = 24",
   3,
   "Statement I is one equation in two unknowns: x = 0 and y = 4 give x + y = 4, while x = 6 and y = 0 give 6 -- not sufficient. Statement II is Statement I multiplied by 2, so it adds no information, "
   "and even together the two leave x + y open. The trap is to count two equations and conclude that two unknowns can be found.",
   "कथन I दो अज्ञात राशियों वाला एक समीकरण है: x = 0 और y = 4 से x + y = 4 मिलता है, जबकि x = 6 और y = 0 से 6 -- पर्याप्त नहीं। कथन II, कथन I को 2 से गुणा करने पर बनता है, इसलिए वह कोई नई जानकारी नहीं देता, "
   "और दोनों साथ लेकर भी x + y अनिर्धारित रहता है। जाल यह है कि दो समीकरण गिनकर मान लिया जाए कि दोनों अज्ञात निकल आएँगे।",
   "qa-ds-same-equation-twice", _ds1)

def _ds2():
    vals = [F(k, 2) for k in range(-12, 13)]
    pts = [(x, y) for x in vals for y in vals]
    ans = lambda ps: {x > y for x, y in ps}
    s1 = ans([(x, y) for x, y in pts if x * x > y * y])
    s2 = ans([(x, y) for x, y in pts if x + y > 0])
    both = ans([(x, y) for x, y in pts if x * x > y * y and x + y > 0])
    alone = (len(s1) == 1, len(s2) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(both) == 1 else "d"
DS(QA, "hard",
   "Is x greater than y? (x and y are real numbers.)",
   "क्या x, y से बड़ा है? (x और y वास्तविक संख्याएँ हैं।)",
   "x² > y²", "x² > y²",
   "x + y > 0", "x + y > 0",
   2,
   "Statement I alone: x = 3, y = 1 gives yes, but x = -3, y = 1 also satisfies x² > y² and gives no -- not sufficient. Statement II alone: x = 2, y = 1 gives yes and x = 1, y = 2 gives no. "
   "Together: x² - y² = (x - y)(x + y) is positive and x + y is positive, so x - y must be positive, that is x > y -- sufficient. Each statement alone fails; both together answer the question.",
   "कथन I अकेला: x = 3, y = 1 से उत्तर हाँ है, पर x = -3, y = 1 भी x² > y² को संतुष्ट करते हैं और उत्तर नहीं देते -- पर्याप्त नहीं। कथन II अकेला: x = 2, y = 1 से हाँ और x = 1, y = 2 से नहीं। "
   "दोनों साथ: x² - y² = (x - y)(x + y) धनात्मक है और x + y धनात्मक है, इसलिए x - y धनात्मक होना चाहिए, यानी x > y -- पर्याप्त। कोई भी कथन अकेला काफ़ी नहीं; दोनों साथ मिलकर प्रश्न का उत्तर देते हैं।",
   "qa-ds-is-x-greater-than-y", _ds2)
