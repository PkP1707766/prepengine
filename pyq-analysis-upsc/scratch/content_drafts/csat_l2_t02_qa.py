# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 2 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Same mix as Test 1 (playbook B.7), with none of Test 1's question shapes: last digits, squares and cubes,
equal remainders, a Chinese-remainder pair, trailing zeros, the smallest number with ten divisors (every
distractor also has ten), half-and-half average speed, crossing trains, a head-start race, mixture by equal
volumes, a mean of overlapping groups, shares in chained fractions, a profit-and-loss pair, an election,
sets, coins by ratio, a balance with weights on both pans, and a calendar.
Difficulty 3 easy / 19 medium / 12 hard; every key is worked out in code by check()."""
import math, datetime as dt
from fractions import Fraction as F
from itertools import combinations, product
import csat_common as c
from csat_common import N, S2, DS, QA

def ndiv(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)

# 1
N(QA, "Number Theory", "medium",
  "What is the units digit of 7⁹⁵ × 3⁵⁸?",
  "7⁹⁵ × 3⁵⁸ का इकाई अंक क्या है?",
  ["1", "3", "7", "9"], 2,
  "Units digits of powers of 7 repeat in the cycle 7, 9, 3, 1; 95 = 4 × 23 + 3, so 7⁹⁵ ends in 3. Powers of 3 repeat as 3, 9, 7, 1; 58 = 4 × 14 + 2, so 3⁵⁸ ends in 9. "
  "The product ends in the units digit of 3 × 9 = 27, that is 7. 3 and 9 are the units digits of the two powers taken alone; 1 is the end of a full cycle.",
  "7 की घातों के इकाई अंक 7, 9, 3, 1 के चक्र में दोहराते हैं; 95 = 4 × 23 + 3, इसलिए 7⁹⁵ का इकाई अंक 3 है। 3 की घातें 3, 9, 7, 1 में दोहराती हैं; 58 = 4 × 14 + 2, इसलिए 3⁵⁸ का इकाई अंक 9 है। "
  "गुणनफल का इकाई अंक 3 × 9 = 27 का इकाई अंक, यानी 7, है। 3 और 9 दोनों घातों के अलग-अलग इकाई अंक हैं; 1 पूरे चक्र का अंत है।",
  "qa-nt-units-digit-7-95-3-58", lambda: str((pow(7, 95, 10) * pow(3, 58, 10)) % 10))

# 2
def _nt2():
    sq = {k * k for k in range(1, 32) if k * k <= 1000}
    cu = {k ** 3 for k in range(1, 11) if k ** 3 <= 1000}
    return str(1000 - len(sq | cu))
N(QA, "Number Theory", "hard",
  "How many of the integers from 1 to 1000, both included, are neither perfect squares nor perfect cubes?",
  "1 से 1000 तक के पूर्णांकों में से, दोनों सम्मिलित, कितने न तो पूर्ण वर्ग हैं और न ही पूर्ण घन?",
  ["962", "965", "969", "990"], 0,
  "Squares up to 1000: 1² to 31², 31 of them. Cubes: 1³ to 10³, 10 of them. Numbers that are both are sixth powers: 1, 64 and 729, 3 of them. "
  "So 31 + 10 - 3 = 38 numbers are squares or cubes, and 1000 - 38 = 962 are neither. 965 subtracts the 3 sixth powers twice; 969 leaves out the cubes; 990 leaves out the squares.",
  "1000 तक के वर्ग: 1² से 31², कुल 31। घन: 1³ से 10³, कुल 10। जो दोनों हैं वे छठी घातें हैं: 1, 64 और 729, कुल 3। "
  "अतः 31 + 10 - 3 = 38 संख्याएँ वर्ग या घन हैं, और 1000 - 38 = 962 दोनों में से कुछ नहीं हैं। 965 तीन छठी घातों को दो बार घटाता है; 969 घनों को छोड़ देता है; 990 वर्गों को छोड़ देता है।",
  "qa-nt-neither-square-nor-cube", _nt2)

# 3
def _nt3():
    m = 147 // 3
    return f"{(m - 2) * (m + 2):,}".replace(",", "")
N(QA, "Number Theory", "medium",
  "The sum of three consecutive odd numbers is 147. What is the product of the smallest and the largest of them?",
  "तीन क्रमागत विषम संख्याओं का योग 147 है। उनमें से सबसे छोटी और सबसे बड़ी संख्या का गुणनफल क्या है?",
  ["2209", "2303", "2397", "2401"], 2,
  "Three consecutive odd numbers are m - 2, m and m + 2, with sum 3m = 147, so m = 49 and the numbers are 47, 49 and 51. The product asked for is 47 × 51 = 2397 (= 49² - 4). "
  "2401 is the square of the middle number; 2303 = 47 × 49 uses the middle number; 2209 = 47².",
  "तीन क्रमागत विषम संख्याएँ m - 2, m और m + 2 हैं, जिनका योग 3m = 147, अतः m = 49 और संख्याएँ 47, 49 और 51 हैं। माँगा गया गुणनफल 47 × 51 = 2397 (= 49² - 4) है। "
  "2401 बीच वाली संख्या का वर्ग है; 2303 = 47 × 49 बीच वाली संख्या लेता है; 2209 = 47²।",
  "qa-nt-three-consecutive-odd", _nt3)

# 4
def _nt4():
    nums = (1305, 4665, 6905)
    best = max(d for d in range(1, 7000) if len({x % d for x in nums}) == 1)
    return str(best)
N(QA, "Number Theory", "hard",
  "What is the largest number that divides 1305, 4665 and 6905 and leaves the same remainder in each case?",
  "वह सबसे बड़ी संख्या कौन-सी है जो 1305, 4665 और 6905 को भाग देकर हर बार समान शेषफल छोड़ती है?",
  ["140", "280", "560", "1120"], 3,
  "If all three leave the same remainder, the divisor divides every difference: 4665 - 1305 = 3360, 6905 - 4665 = 2240 and 6905 - 1305 = 5600. "
  "Their HCF is 1120 (each is a multiple of 2⁵ × 5 × 7 = 1120: 3, 2 and 5 times), and dividing by 1120 leaves 185 every time. 140, 280 and 560 also divide all three differences, but the question asks for the largest.",
  "यदि तीनों समान शेषफल छोड़ती हैं, तो भाजक हर अंतर को विभाजित करता है: 4665 - 1305 = 3360, 6905 - 4665 = 2240 और 6905 - 1305 = 5600। "
  "इनका HCF 1120 है (हर एक 2⁵ × 5 × 7 = 1120 का गुणज है: 3, 2 और 5 गुना), और 1120 से भाग देने पर हर बार 185 बचता है। 140, 280 और 560 भी तीनों अंतरों को विभाजित करते हैं, पर प्रश्न सबसे बड़ी संख्या पूछता है।",
  "qa-nt-same-remainder-largest-divisor", _nt4)

# 5
N(QA, "Speed-Distance-Time", "medium",
  "A man covers the first half of a journey at 30 km/h and the second half at 60 km/h. What is his average speed for the whole journey?",
  "एक व्यक्ति यात्रा का पहला आधा भाग 30 किमी/घंटा और दूसरा आधा भाग 60 किमी/घंटा की चाल से तय करता है। पूरी यात्रा में उसकी औसत चाल क्या है?",
  ["40 km/h", "42 km/h", "45 km/h", "50 km/h"], 0,
  "For equal distances the average speed is 2ab/(a + b) = 2 × 30 × 60 / 90 = 40 km/h: over 60 km, for example, he takes 1 h for the first 30 km and 0.5 h for the next, 60 km in 1.5 h. "
  "45 km/h is the plain average of the two speeds, which would hold only if he spent equal times, not equal distances, at each speed.",
  "बराबर दूरियों के लिए औसत चाल 2ab/(a + b) = 2 × 30 × 60 / 90 = 40 किमी/घंटा है: उदाहरण के लिए 60 किमी में वह पहले 30 किमी में 1 घंटा और अगले में 0.5 घंटा लेता है, यानी 1.5 घंटे में 60 किमी। "
  "45 किमी/घंटा दोनों चालों का साधारण औसत है, जो तभी सही होता जब वह हर चाल पर बराबर दूरी के बजाय बराबर समय बिताता।",
  "qa-sdt-half-and-half-average", lambda: f"{int(F(2 * 30 * 60, 90))} km/h",
  opts_hi=["40 किमी/घंटा", "42 किमी/घंटा", "45 किमी/घंटा", "50 किमी/घंटा"])

# 6
N(QA, "Number Theory", "hard",
  "How many zeros are there at the end of 100!, the product 1 × 2 × 3 × ... × 100?",
  "100!, यानी गुणनफल 1 × 2 × 3 × ... × 100, के अंत में कितने शून्य हैं?",
  ["20", "24", "25", "28"], 1,
  "Each trailing zero needs a factor 10 = 2 × 5, and factors of 2 are plentiful, so count the 5s. Multiples of 5 up to 100 give 20; multiples of 25 (25, 50, 75, 100) give one extra 5 each, 4 more. Total 24. "
  "20 forgets the second 5 in multiples of 25; 25 counts 100 as giving a third 5 (100 = 2² × 5²); 28 also counts the multiples of 25 twice over.",
  "हर अंतिम शून्य के लिए 10 = 2 × 5 का एक गुणनखंड चाहिए, और 2 के गुणनखंड बहुत हैं, इसलिए 5 गिनिए। 100 तक 5 के गुणज 20 देते हैं; 25 के गुणज (25, 50, 75, 100) हर एक एक अतिरिक्त 5 देते हैं, 4 और। कुल 24। "
  "20, 25 के गुणजों में दूसरा 5 भूल जाता है; 25, 100 से तीसरा 5 मानता है (100 = 2² × 5²); 28, 25 के गुणजों को फिर से दोहरा गिनता है।",
  "qa-nt-trailing-zeros-100-factorial", lambda: str(len(str(math.factorial(100))) - len(str(math.factorial(100)).rstrip("0"))))

# 7
def _nt5():
    return str(next(x for x in range(1, 1000) if x % 5 == 3 and x % 7 == 4) % 35)
N(QA, "Number Theory", "medium",
  "A number leaves a remainder of 3 when divided by 5 and a remainder of 4 when divided by 7. What remainder does it leave when divided by 35?",
  "कोई संख्या 5 से भाग देने पर 3 और 7 से भाग देने पर 4 शेषफल छोड़ती है। 35 से भाग देने पर वह कितना शेषफल छोड़ेगी?",
  ["18", "23", "28", "33"], 0,
  "Numbers leaving remainder 4 on division by 7 are 4, 11, 18, 25, 32; of these only 18 also leaves remainder 3 on division by 5. Since 5 and 7 are co-prime, every such number is 18 more than a multiple of 35, so the remainder is 18. "
  "Each distractor meets one condition only: 23, 28 and 33 all leave 3 on division by 5, but leave 2, 0 and 5 on division by 7.",
  "7 से भाग देने पर 4 शेषफल देने वाली संख्याएँ 4, 11, 18, 25, 32 हैं; इनमें केवल 18 ही 5 से भाग देने पर 3 शेषफल भी देती है। चूँकि 5 और 7 सहअभाज्य हैं, ऐसी हर संख्या 35 के किसी गुणज से 18 अधिक होती है, अतः शेषफल 18 है। "
  "हर ग़लत विकल्प केवल एक शर्त पूरी करता है: 23, 28 और 33 सभी 5 से भाग देने पर 3 छोड़ते हैं, पर 7 से भाग देने पर 2, 0 और 5 छोड़ते हैं।",
  "qa-nt-remainders-5-and-7", _nt5)

# 8 -- statement-based: HCF 12, sum 60
def _nt6():
    pairs = [(x, 60 - x) for x in range(1, 30) if math.gcd(x, 60 - x) == 12]
    one = len(pairs) == 2
    two = len({a * b for a, b in pairs}) == 1
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Number Theory", "medium",
   "The sum of two natural numbers is 60 and their HCF is 12. Which of the following statements is/are correct?",
   "दो प्राकृत संख्याओं का योग 60 और उनका HCF 12 है। निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
   ["There are exactly two such pairs of numbers.", "The product of the two numbers is the same for every such pair."],
   ["ऐसी संख्याओं की ठीक दो जोड़ियाँ हैं।", "ऐसी हर जोड़ी के लिए दोनों संख्याओं का गुणनफल समान है।"], 0,
   "Only I is correct. Write the numbers as 12a and 12b with a and b co-prime: then a + b = 5, giving (1, 4) and (2, 3), so the pairs are 12 and 48, and 24 and 36 -- exactly two. "
   "Their products differ, 576 and 864. The trap is the rule 'product = HCF × LCM', which fixes the product only when the LCM is fixed; here the LCMs, 48 and 72, differ.",
   "केवल I सही है। संख्याओं को 12a और 12b लिखिए, जहाँ a और b सहअभाज्य हैं: तब a + b = 5, जिससे (1, 4) और (2, 3) मिलते हैं, अतः जोड़ियाँ 12 और 48, तथा 24 और 36 हैं -- ठीक दो। "
   "उनके गुणनफल अलग हैं, 576 और 864। जाल 'गुणनफल = HCF × LCM' का नियम है, जो गुणनफल को तभी तय करता है जब LCM तय हो; यहाँ LCM, 48 और 72, अलग-अलग हैं।",
   "qa-nt-hcf-12-sum-60", roman=True, check=_nt6, craft="inference")

# 9 -- trains crossing
def _sdt2():
    s_sum, s_diff = F(300, 10), F(300, 30)
    fast = (s_sum + s_diff) / 2
    return f"{int(fast * F(18, 5))} km/h"
N(QA, "Speed-Distance-Time", "hard",
  "Two trains, 120 m and 180 m long, run on parallel tracks. Running in opposite directions they cross each other completely in 10 seconds; running in the same direction, the faster one takes 30 seconds to cross the slower one. What is the speed of the faster train?",
  "120 मी और 180 मी लंबी दो रेलगाड़ियाँ समांतर पटरियों पर चलती हैं। विपरीत दिशाओं में चलते हुए वे एक-दूसरे को 10 सेकंड में पूरी तरह पार करती हैं; एक ही दिशा में चलते हुए तेज़ गाड़ी धीमी गाड़ी को 30 सेकंड में पार करती है। तेज़ गाड़ी की चाल क्या है?",
  ["36 km/h", "54 km/h", "72 km/h", "108 km/h"], 2,
  "Crossing means covering both lengths, 300 m. Opposite directions: sum of speeds = 300/10 = 30 m/s; same direction: difference = 300/30 = 10 m/s. So the faster train runs at (30 + 10)/2 = 20 m/s = 72 km/h, the slower at 10 m/s = 36 km/h. "
  "36 km/h is the slower train; 108 km/h is the sum of the speeds; 54 km/h averages the two crossing speeds 30 and 10 m/s wrongly as 15 m/s.",
  "पार करने का अर्थ दोनों लंबाइयाँ, 300 मी, तय करना है। विपरीत दिशाएँ: चालों का योग = 300/10 = 30 मी/से; एक ही दिशा: अंतर = 300/30 = 10 मी/से। अतः तेज़ गाड़ी (30 + 10)/2 = 20 मी/से = 72 किमी/घंटा और धीमी 10 मी/से = 36 किमी/घंटा से चलती है। "
  "36 किमी/घंटा धीमी गाड़ी है; 108 किमी/घंटा चालों का योग है; 54 किमी/घंटा 30 और 10 मी/से को ग़लत ढंग से 15 मी/से मान लेता है।",
  "qa-sdt-two-trains-cross", _sdt2, opts_hi=["36 किमी/घंटा", "54 किमी/घंटा", "72 किमी/घंटा", "108 किमी/घंटा"])

# 10 -- mixture of equal volumes
def _rm1():
    m = (F(3, 5) + F(7, 10)) / 2
    r = m / (1 - m)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Two vessels contain milk and water in the ratios 3 : 2 and 7 : 3. If equal quantities are taken from the two vessels and mixed, what is the ratio of milk to water in the mixture?",
  "दो बर्तनों में दूध और पानी 3 : 2 और 7 : 3 के अनुपात में हैं। यदि दोनों बर्तनों से बराबर मात्रा लेकर मिलाई जाए, तो मिश्रण में दूध और पानी का अनुपात क्या होगा?",
  ["5 : 3", "13 : 7", "2 : 1", "21 : 6"], 1,
  "Milk is 3/5 = 0.6 of the first vessel and 7/10 = 0.7 of the second. Equal quantities give milk at (0.6 + 0.7)/2 = 0.65, water 0.35, so the ratio is 13 : 7. "
  "2 : 1 (= 10 : 5) adds the ratio terms (3 + 7 : 2 + 3), which is wrong because the two ratios have different totals; 21 : 6 multiplies them; 5 : 3 is close but has no basis.",
  "पहले बर्तन में दूध 3/5 = 0.6 और दूसरे में 7/10 = 0.7 है। बराबर मात्राएँ लेने पर दूध (0.6 + 0.7)/2 = 0.65 और पानी 0.35 होगा, अतः अनुपात 13 : 7 है। "
  "2 : 1 (= 10 : 5) अनुपात के पदों को जोड़ता है (3 + 7 : 2 + 3), जो ग़लत है क्योंकि दोनों अनुपातों के कुल अलग हैं; 21 : 6 उन्हें गुणा करता है; 5 : 3 पास है पर उसका कोई आधार नहीं।",
  "qa-rm-equal-volumes-mixture", _rm1)

# 11 -- late and early
def _sdt3():
    d = F(15, 60) / (F(1, 4) - F(1, 5))
    return f"{d:g} km" if d.denominator == 1 else f"{float(d):g} km"
N(QA, "Speed-Distance-Time", "medium",
  "Walking from home to school at 4 km/h, Ravi reaches 5 minutes late. Walking at 5 km/h, he reaches 10 minutes early. How far is the school from his home?",
  "घर से विद्यालय तक 4 किमी/घंटा की चाल से चलने पर रवि 5 मिनट देर से पहुँचता है। 5 किमी/घंटा की चाल से चलने पर वह 10 मिनट पहले पहुँचता है। विद्यालय उसके घर से कितनी दूर है?",
  ["4 km", "5 km", "6 km", "7.5 km"], 1,
  "The two walks differ by 5 + 10 = 15 minutes = 1/4 hour. With distance d, d/4 - d/5 = 1/4, so d/20 = 1/4 and d = 5 km: 75 minutes at 4 km/h and 60 minutes at 5 km/h. "
  "Using only the 5 or the 10 minutes, instead of their sum, gives a shorter distance.",
  "दोनों बार के समय में 5 + 10 = 15 मिनट = 1/4 घंटे का अंतर है। दूरी d हो तो d/4 - d/5 = 1/4, अतः d/20 = 1/4 और d = 5 किमी: 4 किमी/घंटा पर 75 मिनट और 5 किमी/घंटा पर 60 मिनट। "
  "योग के बजाय केवल 5 या केवल 10 मिनट लेने से कम दूरी आती है।",
  "qa-sdt-late-and-early", _sdt3, opts_hi=["4 किमी", "5 किमी", "6 किमी", "7.5 किमी"])

# 12 -- mean of overlapping groups
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "The average of 11 numbers is 50. The average of the first six of them is 49, and the average of the last six is 52. What is the sixth number?",
  "11 संख्याओं का औसत 50 है। उनमें से पहली छह का औसत 49 और अंतिम छह का औसत 52 है। छठी संख्या क्या है?",
  ["49", "50", "52", "56"], 3,
  "The first six and the last six together cover all 11 numbers with the sixth counted twice: 6 × 49 + 6 × 52 = 294 + 312 = 606, against a total of 11 × 50 = 550. "
  "The excess, 606 - 550 = 56, is the sixth number. 49, 50 and 52 are the three averages in the question, picked by solvers who guess that the overlap is 'typical'.",
  "पहली छह और अंतिम छह मिलकर सभी 11 संख्याओं को ढकती हैं, जिनमें छठी संख्या दो बार गिनी गई है: 6 × 49 + 6 × 52 = 294 + 312 = 606, जबकि कुल 11 × 50 = 550 है। "
  "अधिकता, 606 - 550 = 56, ही छठी संख्या है। 49, 50 और 52 प्रश्न के तीनों औसत हैं, जिन्हें वे चुनते हैं जो अनुमान लगाते हैं कि बीच वाली संख्या 'सामान्य' होगी।",
  "qa-rm-overlapping-averages", lambda: str(6 * 49 + 6 * 52 - 11 * 50))

# 13 -- race with a head start
def _sdt4():
    t_a = F(1000, 8)
    return f"{(F(960) / (t_a + 35)):g} m/s"
N(QA, "Speed-Distance-Time", "hard",
  "In a 1 km race, A gives B a start of 40 m and still beats him by 35 seconds. If A runs at 8 m/s, what is B's speed?",
  "1 किमी की दौड़ में A, B को 40 मी की बढ़त देता है और फिर भी उसे 35 सेकंड से हरा देता है। यदि A की चाल 8 मी/से है, तो B की चाल क्या है?",
  ["6 m/s", "6.25 m/s", "6.5 m/s", "7 m/s"], 0,
  "A runs 1000 m in 1000/8 = 125 s. B, starting 40 m ahead, runs only 960 m and finishes 35 s after A, in 160 s, so B's speed is 960/160 = 6 m/s. "
  "6.25 m/s forgets the start and divides 1000 m by 160 s; 6.5 m/s adds the start instead (1040/160); 7 m/s has no basis.",
  "A 1000 मी, 1000/8 = 125 सेकंड में दौड़ता है। 40 मी आगे से शुरू करने वाला B केवल 960 मी दौड़ता है और A से 35 सेकंड बाद, 160 सेकंड में, पहुँचता है, अतः B की चाल 960/160 = 6 मी/से है। "
  "6.25 मी/से बढ़त भूलकर 1000 मी को 160 सेकंड से भाग देता है; 6.5 मी/से बढ़त को घटाने के बजाय जोड़ता है (1040/160); 7 मी/से का कोई आधार नहीं।",
  "qa-sdt-race-head-start", _sdt4, opts_hi=["6 मी/से", "6.25 मी/से", "6.5 मी/से", "7 मी/से"])

# 14 -- chained fractions of shares
def _rm2():
    k = 6800 // 17
    return f"₹{12 * k:,}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "₹6,800 is divided among A, B and C so that A gets two-thirds of what B gets, and B gets one-fourth of what C gets. What is C's share?",
  "₹6,800 को A, B और C में इस प्रकार बाँटा जाता है कि A को B के हिस्से का दो-तिहाई मिलता है, और B को C के हिस्से का एक-चौथाई। C का हिस्सा कितना है?",
  ["₹800", "₹1,200", "₹2,000", "₹4,800"], 3,
  "Take C = 12k; then B = C/4 = 3k and A = 2B/3 = 2k. The total 2k + 3k + 12k = 17k = 6,800 gives k = 400, so C gets ₹4,800, B ₹1,200 and A ₹800. "
  "₹800 and ₹1,200 are A's and B's shares; ₹2,000 is the two together.",
  "C = 12k लीजिए; तब B = C/4 = 3k और A = 2B/3 = 2k। कुल 2k + 3k + 12k = 17k = 6,800 से k = 400, अतः C को ₹4,800, B को ₹1,200 और A को ₹800 मिलते हैं। "
  "₹800 और ₹1,200, A और B के हिस्से हैं; ₹2,000 दोनों का योग है।",
  "qa-rm-chained-fraction-shares", _rm2)

# 15 -- two articles at the same price
def _pp1():
    cp = F(990) / F(11, 10) + F(990) / F(9, 10)
    diff = 2 * 990 - cp
    return "Loss of ₹20" if diff == -20 else str(diff)
N(QA, "Percentage & Profit-Loss", "medium",
  "A shopkeeper sells two articles for ₹990 each. On one he makes a profit of 10% and on the other a loss of 10%. What is his net result on the two?",
  "एक दुकानदार दो वस्तुएँ ₹990-₹990 में बेचता है। एक पर उसे 10% लाभ होता है और दूसरी पर 10% हानि। दोनों को मिलाकर उसका कुल परिणाम क्या है?",
  ["Loss of ₹20", "Loss of ₹99", "No profit, no loss", "Profit of ₹20"], 0,
  "The cost prices are 990/1.1 = ₹900 and 990/0.9 = ₹1,100, together ₹2,000, against sales of ₹1,980: a loss of ₹20, or 1%. "
  "'No profit, no loss' assumes the 10% gain and 10% loss cancel, but they are percentages of different cost prices; ₹99 takes 10% of ₹990.",
  "क्रय मूल्य 990/1.1 = ₹900 और 990/0.9 = ₹1,100 हैं, कुल ₹2,000, जबकि बिक्री ₹1,980 की है: ₹20 की हानि, यानी 1%। "
  "'न लाभ, न हानि' मानता है कि 10% लाभ और 10% हानि एक-दूसरे को काट देते हैं, पर ये अलग-अलग क्रय मूल्यों के प्रतिशत हैं; ₹99, ₹990 का 10% लेता है।",
  "qa-pp-same-price-profit-loss", _pp1,
  opts_hi=["₹20 की हानि", "₹99 की हानि", "न लाभ, न हानि", "₹20 का लाभ"])

# 16 -- election
def _pp2():
    valid = F(168) / (F(52, 100) - F(48, 100))
    cast = valid + 120
    return f"{int(cast / F(9, 10)):,}"
N(QA, "Percentage & Profit-Loss", "hard",
  "In an election between two candidates, 10% of the voters on the list did not vote, and 120 of the votes cast were invalid. The winner got 52% of the valid votes and won by 168 votes. How many voters were on the list?",
  "दो उम्मीदवारों के बीच एक चुनाव में सूची के 10% मतदाताओं ने मत नहीं डाला, और डाले गए मतों में से 120 अमान्य थे। विजेता को मान्य मतों का 52% मिला और वह 168 मतों से जीता। सूची में कितने मतदाता थे?",
  ["4,320", "4,620", "4,667", "4,800"], 3,
  "The margin is 52% - 48% = 4% of the valid votes, so the valid votes number 168/0.04 = 4,200. Adding the 120 invalid ones, 4,320 votes were cast, which is 90% of the list: 4,320/0.9 = 4,800. "
  "4,320 stops at the votes cast; 4,667 divides the valid votes by 0.9 and forgets the invalid ones; 4,620 adds 10% to 4,200 instead of dividing by 0.9.",
  "अंतर मान्य मतों का 52% - 48% = 4% है, अतः मान्य मत 168/0.04 = 4,200 हैं। 120 अमान्य जोड़ने पर 4,320 मत डाले गए, जो सूची का 90% है: 4,320/0.9 = 4,800। "
  "4,320 डाले गए मतों पर रुक जाता है; 4,667 मान्य मतों को 0.9 से भाग देकर अमान्य मत भूल जाता है; 4,620, 0.9 से भाग देने के बजाय 4,200 में 10% जोड़ देता है।",
  "qa-pp-election-voters-on-list", _pp2)

# 17 -- easy series
N(QA, "Sequences & Series", "easy",
  "What is the next number in the series 2, 6, 12, 20, 30, ... ?",
  "श्रेणी 2, 6, 12, 20, 30, ... में अगली संख्या क्या है?",
  ["38", "40", "42", "56"], 2,
  "The terms are 1 × 2, 2 × 3, 3 × 4, 4 × 5, 5 × 6, so the next is 6 × 7 = 42; equally, the differences 4, 6, 8, 10 grow by 2, so the next difference is 12. "
  "40 repeats the last difference, 10; 56 = 7 × 8 skips a term; 38 adds 8.",
  "पद 1 × 2, 2 × 3, 3 × 4, 4 × 5, 5 × 6 हैं, इसलिए अगला 6 × 7 = 42 है; इसी तरह अंतर 4, 6, 8, 10, 2-2 बढ़ते हैं, इसलिए अगला अंतर 12 है। "
  "40 अंतिम अंतर 10 को दोहराता है; 56 = 7 × 8 एक पद छोड़ देता है; 38, 8 जोड़ता है।",
  "qa-ss-n-times-n-plus-1-series", lambda: str(6 * 7))

# 18 -- cost with list price
N(QA, "Percentage & Profit-Loss", "medium",
  "A trader buys goods at 20% below the list price and sells them at 10% above the list price. What is his profit percentage?",
  "एक व्यापारी सूची मूल्य से 20% कम पर माल ख़रीदता है और सूची मूल्य से 10% अधिक पर बेचता है। उसका लाभ प्रतिशत क्या है?",
  ["25%", "30%", "32.5%", "37.5%"], 3,
  "With a list price of 100, he pays 80 and sells for 110, a profit of 30 on a cost of 80: 30/80 = 37.5%. "
  "30% adds the two percentages; it measures the profit against the list price rather than against what the trader paid.",
  "सूची मूल्य 100 लें तो वह 80 देता है और 110 में बेचता है, 80 की लागत पर 30 का लाभ: 30/80 = 37.5%। "
  "30% दोनों प्रतिशत जोड़ देता है; यह लाभ को व्यापारी की लागत के बजाय सूची मूल्य के सापेक्ष मापता है।",
  "qa-pp-buy-below-sell-above-list", lambda: f"{float(F(110 - 80, 80) * 100):g}%")

# 19 -- sum of an AP
def _ss2():
    a, t10 = 7, 43
    d = F(t10 - a, 9)
    return str(int(F(20, 2) * (2 * a + 19 * d)))
N(QA, "Sequences & Series", "medium",
  "The first term of an arithmetic progression is 7 and its tenth term is 43. What is the sum of its first 20 terms?",
  "किसी समांतर श्रेढ़ी का पहला पद 7 और दसवाँ पद 43 है। उसके पहले 20 पदों का योग क्या है?",
  ["817", "824", "860", "900"], 3,
  "From the 1st to the 10th term there are 9 steps, so the common difference is (43 - 7)/9 = 4. The 20th term is 7 + 19 × 4 = 83, and the sum is 20 × (7 + 83)/2 = 900. "
  "824 divides by 10 steps instead of 9 (d = 3.6); 860 is 20 times the 10th term; 817 sums only 19 terms.",
  "पहले से दसवें पद तक 9 चरण हैं, इसलिए सार्व अंतर (43 - 7)/9 = 4 है। 20वाँ पद 7 + 19 × 4 = 83 है, और योग 20 × (7 + 83)/2 = 900 है। "
  "824, 9 के बजाय 10 चरणों से भाग देता है (d = 3.6); 860 दसवें पद का 20 गुना है; 817 केवल 19 पदों का योग है।",
  "qa-ss-ap-sum-20-terms", _ss2)

# 20 -- committee with at least one woman
N(QA, "Permutation & Combination", "medium",
  "In how many ways can a committee of 4 be chosen from 5 men and 4 women if it must include at least one woman?",
  "5 पुरुषों और 4 महिलाओं में से 4 सदस्यों की एक समिति कितने तरीकों से चुनी जा सकती है, यदि उसमें कम से कम एक महिला होनी अनिवार्य है?",
  ["111", "121", "125", "126"], 1,
  "All committees of 4 from 9 people: C(9, 4) = 126. Those with no woman are all-men committees: C(5, 4) = 5. So 126 - 5 = 121 have at least one woman. "
  "126 ignores the condition; 125 removes the single all-woman committee, the opposite case; 111 removes C(6, 4) = 15 for no reason.",
  "9 लोगों में से 4 की सभी समितियाँ: C(9, 4) = 126। जिनमें कोई महिला नहीं, वे केवल पुरुषों वाली समितियाँ हैं: C(5, 4) = 5। अतः 126 - 5 = 121 में कम से कम एक महिला है। "
  "126 शर्त को अनदेखा करता है; 125 केवल महिलाओं वाली एक समिति को हटाता है, जो उलटी स्थिति है; 111 अकारण C(6, 4) = 15 घटा देता है।",
  "qa-pc-committee-at-least-one-woman", lambda: str(math.comb(9, 4) - math.comb(5, 4)))

# 21 -- dice probability
def _pc2():
    primes = {2, 3, 5, 7, 11}
    fav = sum(1 for a, b in product(range(1, 7), repeat=2) if a + b in primes)
    f = F(fav, 36)
    return f"{f.numerator}/{f.denominator}"
N(QA, "Permutation & Combination", "medium",
  "Two fair dice are thrown together. What is the probability that the sum of the numbers shown is a prime number?",
  "दो निष्पक्ष पासे एक साथ फेंके जाते हैं। दिखाई देने वाली संख्याओं का योग अभाज्य संख्या होने की प्रायिकता क्या है?",
  ["1/3", "5/12", "1/2", "7/12"], 1,
  "Of the 36 equally likely outcomes, the prime sums 2, 3, 5, 7 and 11 occur 1, 2, 4, 6 and 2 times: 15 outcomes, so the probability is 15/36 = 5/12. "
  "1/2 treats the 11 possible sums (2 to 12) as equally likely; 1/3 forgets the sum 11; 7/12 counts the complement.",
  "36 समान संभावित परिणामों में अभाज्य योग 2, 3, 5, 7 और 11 क्रमशः 1, 2, 4, 6 और 2 बार आते हैं: 15 परिणाम, अतः प्रायिकता 15/36 = 5/12 है। "
  "1/2, 11 संभावित योगों (2 से 12) को समान संभावित मान लेता है; 1/3 योग 11 को भूल जाता है; 7/12 पूरक गिनता है।",
  "qa-pc-two-dice-prime-sum", _pc2)

# 22 -- easy geometry: square wire to circle
N(QA, "Geometry & Mensuration", "easy",
  "A wire bent into the shape of a square encloses an area of 121 cm². If the same wire is bent into a circle, what area will it enclose? (Take π = 22/7.)",
  "वर्ग के आकार में मोड़े गए एक तार से घिरा क्षेत्रफल 121 वर्ग सेमी है। यदि उसी तार को वृत्त के आकार में मोड़ा जाए, तो वह कितना क्षेत्रफल घेरेगा? (π = 22/7 लीजिए।)",
  ["154 cm²", "176 cm²", "196 cm²", "616 cm²"], 0,
  "The square's side is 11 cm, so the wire is 44 cm long. As a circle, 2πr = 44 gives r = 7 cm, and the area is (22/7) × 7² = 154 cm² -- more than the square's 121, as a circle always encloses the most area for its perimeter. "
  "616 cm² takes 14 cm as the radius instead of the diameter; 196 cm² is 14²; 176 cm² has no basis.",
  "वर्ग की भुजा 11 सेमी है, इसलिए तार 44 सेमी लंबा है। वृत्त के रूप में 2πr = 44 से r = 7 सेमी, और क्षेत्रफल (22/7) × 7² = 154 वर्ग सेमी -- वर्ग के 121 से अधिक, क्योंकि किसी परिधि के लिए वृत्त सदा सबसे अधिक क्षेत्रफल घेरता है। "
  "616 वर्ग सेमी, 14 सेमी को व्यास के बजाय त्रिज्या मान लेता है; 196 वर्ग सेमी, 14² है; 176 वर्ग सेमी का कोई आधार नहीं।",
  "qa-gm-square-wire-to-circle", lambda: f"{int(F(22, 7) * F(44 * 7, 44) ** 2)} cm²",
  opts_hi=["154 वर्ग सेमी", "176 वर्ग सेमी", "196 वर्ग सेमी", "616 वर्ग सेमी"])

# 23 -- diagonals of a polygon
N(QA, "Geometry & Mensuration", "medium",
  "How many diagonals does a polygon with 12 sides have?",
  "12 भुजाओं वाले बहुभुज के कितने विकर्ण होते हैं?",
  ["48", "54", "60", "66"], 1,
  "Any two of the 12 vertices give a line segment, C(12, 2) = 66, but 12 of those segments are sides, so there are 66 - 12 = 54 diagonals; equivalently 12 × (12 - 3)/2. "
  "66 forgets to remove the sides; 60 removes only half of them; 48 subtracts the sides a second time.",
  "12 शीर्षों में से कोई दो एक रेखाखंड देते हैं, C(12, 2) = 66, पर इनमें से 12 रेखाखंड भुजाएँ हैं, इसलिए विकर्ण 66 - 12 = 54 हैं; इसी तरह 12 × (12 - 3)/2। "
  "66 भुजाओं को हटाना भूल जाता है; 60 उनमें से केवल आधी हटाता है; 48 भुजाओं को दूसरी बार घटा देता है।",
  "qa-gm-diagonals-12-gon", lambda: str(math.comb(12, 2) - 12))

# 24 -- men join midway
def _tw1():
    work = 12 * 15
    left = work - 12 * 5
    return str(5 + left // 15)
N(QA, "Time & Work", "medium",
  "12 workers can finish a job in 15 days. After they have worked for 5 days, 3 more workers join them. In how many days in all is the job finished?",
  "12 श्रमिक एक काम 15 दिनों में पूरा कर सकते हैं। 5 दिन काम करने के बाद उनके साथ 3 और श्रमिक जुड़ जाते हैं। काम कुल कितने दिनों में पूरा होता है?",
  ["8", "13", "15", "20"], 1,
  "The job is 12 × 15 = 180 worker-days. In 5 days, 60 are done, leaving 120 for 15 workers: 8 more days, so 13 days in all. "
  "8 is only the time after the new workers join; 15 is the original time, ignoring them; 20 adds the original 15 days to the first 5.",
  "काम 12 × 15 = 180 श्रमिक-दिन का है। 5 दिनों में 60 पूरे होते हैं, और 15 श्रमिकों के लिए 120 बचते हैं: 8 और दिन, यानी कुल 13 दिन। "
  "8 केवल नए श्रमिकों के जुड़ने के बाद का समय है; 15 मूल समय है, जो उन्हें अनदेखा करता है; 20 पहले 5 दिनों में मूल 15 दिन जोड़ देता है।",
  "qa-tw-workers-join-midway", _tw1)

# 25 -- outlet rate
def _tw2():
    out = 1 / (F(1, 20) + F(1, 30) - F(1, 15))
    return f"{int(out)} minutes"
N(QA, "Time & Work", "hard",
  "Two inlet pipes can fill a tank in 20 minutes and 30 minutes respectively. With both inlets and an outlet pipe open together, the empty tank fills in 15 minutes. In how many minutes can the outlet alone empty the full tank?",
  "दो भरने वाले पाइप एक टंकी को क्रमशः 20 मिनट और 30 मिनट में भर सकते हैं। दोनों पाइप और एक निकास पाइप एक साथ खुले हों तो ख़ाली टंकी 15 मिनट में भरती है। निकास पाइप अकेला भरी टंकी को कितने मिनट में ख़ाली कर सकता है?",
  ["12 minutes", "30 minutes", "50 minutes", "60 minutes"], 3,
  "The inlets fill 1/20 + 1/30 = 1/12 of the tank a minute; with the outlet open the net rate is 1/15. So the outlet empties 1/12 - 1/15 = 1/60 a minute, and needs 60 minutes for a full tank. "
  "12 minutes is how long the two inlets alone would take; 50 adds the two filling times; 30 has no basis.",
  "भरने वाले पाइप प्रति मिनट टंकी का 1/20 + 1/30 = 1/12 भाग भरते हैं; निकास खुला होने पर शुद्ध दर 1/15 है। अतः निकास प्रति मिनट 1/12 - 1/15 = 1/60 भाग ख़ाली करता है, और भरी टंकी के लिए 60 मिनट चाहिए। "
  "12 मिनट वह समय है जो दोनों भरने वाले पाइप अकेले लेते; 50 दोनों भरने के समयों को जोड़ता है; 30 का कोई आधार नहीं।",
  "qa-tw-outlet-rate", _tw2, opts_hi=["12 मिनट", "30 मिनट", "50 मिनट", "60 मिनट"])

# 26 -- sets: exactly one
N(QA, "Puzzle Hybrid", "medium",
  "Each of the 30 students in a class likes at least one of tea and coffee. 18 of them like tea and 20 like coffee. How many students like exactly one of the two drinks?",
  "एक कक्षा के 30 विद्यार्थियों में से हर एक को चाय और कॉफ़ी में से कम से कम एक पसंद है। उनमें से 18 को चाय और 20 को कॉफ़ी पसंद है। कितने विद्यार्थियों को दोनों में से ठीक एक पेय पसंद है?",
  ["8", "10", "12", "22"], 3,
  "Since everyone likes at least one, the overlap is 18 + 20 - 30 = 8 students who like both. Exactly one drink: tea only 18 - 8 = 10 and coffee only 20 - 8 = 12, together 22 (or 30 - 8). "
  "8 is the number who like both; 10 and 12 are each 'only' group on its own.",
  "चूँकि हर एक को कम से कम एक पसंद है, उभयनिष्ठ भाग 18 + 20 - 30 = 8 विद्यार्थी हैं जिन्हें दोनों पसंद हैं। ठीक एक पेय: केवल चाय 18 - 8 = 10 और केवल कॉफ़ी 20 - 8 = 12, कुल 22 (या 30 - 8)। "
  "8 दोनों पसंद करने वालों की संख्या है; 10 और 12 'केवल' वाले दोनों समूह अलग-अलग हैं।",
  "qa-ph-tea-coffee-exactly-one", lambda: str(30 - (18 + 20 - 30)))

# 27 -- easy coins by ratio
def _ph2():
    for n in range(1, 50):
        if 5 * n + 2 * 2 * n + 1 * 3 * n == 120:
            return str(2 * n)
N(QA, "Puzzle Hybrid", "easy",
  "A bag contains ₹5, ₹2 and ₹1 coins in the ratio 1 : 2 : 3 by number. If the coins are worth ₹120 in all, how many ₹2 coins are there?",
  "एक थैले में ₹5, ₹2 और ₹1 के सिक्के संख्या में 1 : 2 : 3 के अनुपात में हैं। यदि सिक्कों का कुल मूल्य ₹120 है, तो ₹2 के कितने सिक्के हैं?",
  ["10", "20", "30", "40"], 1,
  "One 'set' of the ratio -- one ₹5, two ₹2 and three ₹1 coins -- is worth 5 + 4 + 3 = ₹12. ₹120 is 10 such sets, so there are 10 coins of ₹5, 20 of ₹2 and 30 of ₹1. "
  "10 and 30 are the counts of the other two coins; 40 has no basis.",
  "अनुपात का एक 'समूह' -- ₹5 का एक, ₹2 के दो और ₹1 के तीन सिक्के -- 5 + 4 + 3 = ₹12 का है। ₹120 ऐसे 10 समूह हैं, इसलिए ₹5 के 10, ₹2 के 20 और ₹1 के 30 सिक्के हैं। "
  "10 और 30 दूसरे दो सिक्कों की संख्याएँ हैं; 40 का कोई आधार नहीं।",
  "qa-ph-coins-by-ratio", _ph2)

# 28 -- smallest number with ten divisors
N(QA, "Number Theory", "hard",
  "What is the smallest positive integer that has exactly 10 positive divisors?",
  "वह सबसे छोटा धनात्मक पूर्णांक कौन-सा है जिसके ठीक 10 धनात्मक भाजक हैं?",
  ["48", "80", "162", "512"], 0,
  "A number p^a × q^b × ... has (a + 1)(b + 1) ... divisors. 10 = 10 or 2 × 5, so the number is p⁹ or p⁴ × q. The smallest choices are 2⁹ = 512 and 2⁴ × 3 = 48, so the answer is 48. "
  "Every distractor also has exactly 10 divisors -- 80 = 2⁴ × 5, 162 = 2 × 3⁴, 512 = 2⁹ -- so the question turns on 'smallest': the higher power must go on the smaller prime.",
  "संख्या p^a × q^b × ... के (a + 1)(b + 1) ... भाजक होते हैं। 10 = 10 या 2 × 5, इसलिए संख्या p⁹ या p⁴ × q है। सबसे छोटे विकल्प 2⁹ = 512 और 2⁴ × 3 = 48 हैं, अतः उत्तर 48 है। "
  "हर ग़लत विकल्प के भी ठीक 10 भाजक हैं -- 80 = 2⁴ × 5, 162 = 2 × 3⁴, 512 = 2⁹ -- इसलिए प्रश्न 'सबसे छोटा' पर टिका है: बड़ी घात छोटे अभाज्य पर होनी चाहिए।",
  "qa-nt-smallest-with-ten-divisors",
  lambda: (lambda xs: (str(min(xs)) if all(ndiv(x) == 10 for x in (48, 80, 162, 512)) else "?"))([n for n in range(1, 600) if ndiv(n) == 10]))

# 29 -- ratio of ages
def _rm3():
    for x in range(1, 50):
        if F(7 * x + 10, 2 * x + 10) == F(9, 4):
            return str(7 * x)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The present ages of a father and his son are in the ratio 7 : 2. After 10 years, they will be in the ratio 9 : 4. What is the father's present age?",
  "एक पिता और उसके पुत्र की वर्तमान आयु 7 : 2 के अनुपात में है। 10 वर्ष बाद यह अनुपात 9 : 4 होगा। पिता की वर्तमान आयु क्या है?",
  ["10", "20", "35", "45"], 2,
  "Let the ages be 7x and 2x. Then (7x + 10)/(2x + 10) = 9/4 gives 28x + 40 = 18x + 90, so x = 5: the father is 35 and the son 10; in 10 years they will be 45 and 20, in the ratio 9 : 4. "
  "10 and 20 are the son's ages now and later; 45 is the father's age after 10 years.",
  "आयु 7x और 2x मानिए। तब (7x + 10)/(2x + 10) = 9/4 से 28x + 40 = 18x + 90, अतः x = 5: पिता 35 और पुत्र 10 वर्ष का है; 10 वर्ष बाद वे 45 और 20 के होंगे, अनुपात 9 : 4। "
  "10 और 20 पुत्र की अभी की और बाद की आयु हैं; 45, 10 वर्ष बाद पिता की आयु है।",
  "qa-rm-father-son-ratio", _rm3)

# 30 -- weights on both pans
def _ph3():
    from itertools import combinations as comb
    for k in range(1, 7):
        for ws in comb(range(1, 41), k):
            reach = {0}
            for w in ws:
                reach = {r + s for r in reach for s in (-w, 0, w)}
            if all(v in reach for v in range(1, 41)):
                return str(k)
N(QA, "Puzzle Hybrid", "hard",
  "A shopkeeper wants to weigh every whole number of kilograms from 1 kg to 40 kg on a two-pan balance, and may place weights on either pan. What is the smallest number of weights he needs?",
  "एक दुकानदार दो पलड़ों वाले तराज़ू पर 1 किग्रा से 40 किग्रा तक हर पूरे किलोग्राम को तौलना चाहता है, और बाट किसी भी पलड़े पर रख सकता है। उसे कम से कम कितने बाट चाहिए?",
  ["4", "5", "6", "8"], 0,
  "With weights allowed on both pans, each weight can be added, subtracted (put with the goods) or left out. Weights of 1, 3, 9 and 27 kg reach every value up to 1 + 3 + 9 + 27 = 40 -- for example 2 = 3 - 1 and 5 = 9 - 3 - 1 -- "
  "while three weights can produce at most (3³ - 1)/2 = 13 positive values. So 4 weights suffice and fewer cannot. 6 is the answer for weights on one pan only (1, 2, 4, 8, 16, 32).",
  "जब बाट दोनों पलड़ों पर रखे जा सकते हैं, तो हर बाट जोड़ा, घटाया (माल के साथ रखकर) या छोड़ा जा सकता है। 1, 3, 9 और 27 किग्रा के बाट 1 + 3 + 9 + 27 = 40 तक हर मान बना लेते हैं -- जैसे 2 = 3 - 1 और 5 = 9 - 3 - 1 -- "
  "जबकि तीन बाट अधिकतम (3³ - 1)/2 = 13 धनात्मक मान बना सकते हैं। अतः 4 बाट पर्याप्त हैं और इससे कम नहीं। 6 तब का उत्तर है जब बाट केवल एक पलड़े पर रखे जाएँ (1, 2, 4, 8, 16, 32)।",
  "qa-ph-weights-both-pans-1-to-40", _ph3)

# 31 -- calendar
def _ph4():
    assert dt.date(2027, 1, 26).strftime("%A") == "Tuesday"
    return dt.date(2027, 8, 15).strftime("%A")
N(QA, "Puzzle Hybrid", "medium",
  "If 26 January 2027 falls on a Tuesday, on which day of the week will 15 August 2027 fall?",
  "यदि 26 जनवरी 2027 को मंगलवार है, तो 15 अगस्त 2027 को सप्ताह का कौन-सा दिन होगा?",
  ["Thursday", "Friday", "Saturday", "Sunday"], 3,
  "From 26 January to 15 August 2027: 5 more days in January, then 28 (February, 2027 is not a leap year), 31, 30, 31, 30 and 31, and 15 in August, 201 days in all. "
  "201 = 7 × 28 + 5, so the day moves 5 places on from Tuesday, to Sunday. Counting February as 29 days gives Monday; counting 26 January itself as one of the days gives Monday as well.",
  "26 जनवरी से 15 अगस्त 2027 तक: जनवरी के 5 और दिन, फिर 28 (फ़रवरी, 2027 लीप वर्ष नहीं है), 31, 30, 31, 30 और 31, और अगस्त के 15, कुल 201 दिन। "
  "201 = 7 × 28 + 5, इसलिए दिन मंगलवार से 5 स्थान आगे, यानी रविवार, होगा। फ़रवरी को 29 दिन का गिनने पर सोमवार आता है; 26 जनवरी को भी एक दिन गिनने पर भी सोमवार आता है।",
  "qa-ph-26-january-to-15-august", _ph4,
  opts_hi=["गुरुवार", "शुक्रवार", "शनिवार", "रविवार"])

# 32 -- alligation with profit
def _rm4():
    cp = F(5610, 100) / F(11, 10)
    r = (55 - cp) / (cp - 40)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A grocer mixes rice costing ₹40 a kg with rice costing ₹55 a kg and sells the mixture at ₹56.10 a kg, making a profit of 10%. In what ratio did he mix the cheaper and the dearer rice?",
  "एक पंसारी ₹40 प्रति किग्रा वाले चावल को ₹55 प्रति किग्रा वाले चावल के साथ मिलाता है और मिश्रण को ₹56.10 प्रति किग्रा पर बेचकर 10% लाभ कमाता है। उसने सस्ते और महँगे चावल को किस अनुपात में मिलाया?",
  ["3 : 11", "1 : 3", "4 : 11", "11 : 4"], 2,
  "First remove the profit: the mixture costs 56.10/1.1 = ₹51 a kg. By alligation, cheaper : dearer = (55 - 51) : (51 - 40) = 4 : 11. "
  "11 : 4 is the same ratio the wrong way round; using the selling price ₹56.10 as if it were the cost gives no sensible mixture, since it is above both prices.",
  "पहले लाभ हटाइए: मिश्रण की लागत 56.10/1.1 = ₹51 प्रति किग्रा है। एलिगेशन से सस्ता : महँगा = (55 - 51) : (51 - 40) = 4 : 11। "
  "11 : 4 वही अनुपात उलटा है; विक्रय मूल्य ₹56.10 को लागत मानने से कोई अर्थपूर्ण मिश्रण नहीं बनता, क्योंकि वह दोनों मूल्यों से अधिक है।",
  "qa-rm-rice-alligation-profit", _rm4)

# ---- the data-sufficiency block's two Quant items
def _ds1():
    xs = range(1, 5001)
    s1 = [n for n in xs if any(n == (2 * k) ** 2 for k in range(1, 40))]
    s2 = [n for n in xs if n % 8 == 0]
    ok = lambda ns: len({n % 4 == 0 for n in ns}) == 1
    return "b" if ok(s1) and ok(s2) else "a" if ok(s1) or ok(s2) else "c"
DS(QA, "medium",
   "Is the positive integer n divisible by 4?",
   "क्या धनात्मक पूर्णांक n, 4 से विभाज्य है?",
   "n is the square of an even integer.", "n किसी सम पूर्णांक का वर्ग है।",
   "n is a multiple of 8.", "n, 8 का गुणज है।",
   1,
   "Statement I: if n = (2k)², then n = 4k², which is divisible by 4 -- sufficient. Statement II: every multiple of 8 is a multiple of 4 -- also sufficient. "
   "Each statement alone answers the question (yes). The trap is to look for a case where the statements must be combined.",
   "कथन I: यदि n = (2k)², तो n = 4k², जो 4 से विभाज्य है -- पर्याप्त। कथन II: 8 का हर गुणज 4 का गुणज है -- यह भी पर्याप्त। "
   "हर कथन अकेला प्रश्न का उत्तर (हाँ) देता है। जाल यह है कि ऐसी स्थिति खोजी जाए जिसमें कथनों को मिलाना ज़रूरी हो।",
   "qa-ds-divisible-by-4", _ds1)

def _ds2():
    # Sides are any positive real numbers, so sample them finely instead of using whole numbers only:
    # with whole numbers, Statement II would look sufficient (6 x 8 is the only whole-number case).
    ls = [k / 100 for k in range(1, 1400)]
    s1 = {round(l * (14 - l), 6) for l in ls if 14 - l > 0}
    s2 = {round(l * (100 - l * l) ** 0.5, 6) for l in ls if l < 10}
    both = {round(l * (14 - l), 6) for l in ls if abs(l * l + (14 - l) ** 2 - 100) < 1e-9}
    alone = (len(s1) == 1, len(s2) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(both) == 1 else "d"
DS(QA, "hard",
   "What is the area of a rectangle?",
   "एक आयत का क्षेत्रफल क्या है?",
   "Its perimeter is 28 cm.", "उसका परिमाप 28 सेमी है।",
   "Its diagonal is 10 cm.", "उसका विकर्ण 10 सेमी है।",
   2,
   "Statement I alone gives length + breadth = 14, which allows 13 × 1, 10 × 4, 8 × 6 and so on, with different areas. Statement II alone gives length² + breadth² = 100, which also allows many rectangles. "
   "Together: (l + b)² = l² + b² + 2lb, so 196 = 100 + 2lb and the area lb = 48 cm² (the rectangle is 8 cm by 6 cm). Both are needed, and together they suffice without finding the sides.",
   "कथन I अकेला लंबाई + चौड़ाई = 14 देता है, जो 13 × 1, 10 × 4, 8 × 6 आदि अलग-अलग क्षेत्रफल वाले आयत होने देता है। कथन II अकेला लंबाई² + चौड़ाई² = 100 देता है, जो भी कई आयत होने देता है। "
   "दोनों साथ: (l + b)² = l² + b² + 2lb, इसलिए 196 = 100 + 2lb और क्षेत्रफल lb = 48 वर्ग सेमी (आयत 8 सेमी × 6 सेमी है)। दोनों आवश्यक हैं, और साथ मिलकर भुजाएँ निकाले बिना भी पर्याप्त हैं।",
   "qa-ds-rectangle-area", _ds2)
