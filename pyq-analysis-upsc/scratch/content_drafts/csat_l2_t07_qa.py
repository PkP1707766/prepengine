# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 7 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Same mix as Tests 1-6 (playbook B.7) with none of their question shapes: the number that cannot be a square, the
least a with a² divisible by 18, three consecutive squares that add up to 365, multiples of 7 but not of 5, a
repeating decimal as a fraction, the smallest four-digit multiple of three numbers, three surds compared, x³ + 1/x³;
buses that overtake and meet a walker, equal times at two speeds, the return speed that makes an average, two walkers
in the same direction; percentages that cancel, a ratio from a sum of squares, water in milk of a given price, pure
alcohol added to a solution, a diamond that is worth the square of its weight; two successive discounts, simple
interest from two amounts, half-yearly compounding; a series whose partial sums are given, a series that alternates
two operations; a card that is red or a king, ten people split into two teams; a semicircular fence, a cone's curved
surface; a worker 25 per cent less efficient, a job that is behind schedule; a knockout draw, three people on a
library rota, climbing stairs one or two at a time, cutting a pizza; and two data-sufficiency items. The build spreads
the topics through the paper (csat_common.interleave). Difficulty 3 easy / 19 medium / 12 hard; every key is worked
out in code by check()."""
import math
from fractions import Fraction as F
import csat_common as c
from csat_common import N, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    opts = [1764, 2025, 3136, 5153]
    non = [n for n in opts if math.isqrt(n) ** 2 != n]
    assert non == [5153] and 71 ** 2 == 5041 and 72 ** 2 == 5184
    return f"{non[0]:,}"
N(QA, "Number Theory", "easy",
  "Which one of the following numbers cannot be the square of a natural number?",
  "निम्नलिखित संख्याओं में से कौन-सी किसी प्राकृत संख्या का वर्ग नहीं हो सकती?",
  ["1,764", "2,025", "3,136", "5,153"], 3,
  "The square of a natural number can end only in 0, 1, 4, 5, 6 or 9. 5,153 ends in 3, so it cannot be a square (71² = 5,041 and 72² = 5,184). The others are squares: 1,764 = 42², 2,025 = 45² and 3,136 = 56².",
  "किसी प्राकृत संख्या के वर्ग का अंतिम अंक केवल 0, 1, 4, 5, 6 या 9 हो सकता है। 5,153 का अंतिम अंक 3 है, इसलिए वह वर्ग नहीं हो सकती (71² = 5,041 और 72² = 5,184)। बाक़ी वर्ग हैं: 1,764 = 42², 2,025 = 45² और 3,136 = 56²।",
  "qa-nt-the-number-that-is-not-a-square", _nt1)

N(QA, "Number Theory", "medium",
  "What is the smallest natural number a for which a² is divisible by 18?",
  "वह सबसे छोटी प्राकृत संख्या a कौन-सी है जिसके लिए a², 18 से विभाज्य हो?",
  ["6", "9", "12", "18"], 0,
  "18 = 2 × 3². In a² every prime appears to an even power, so a² can contain the factor 2 only if it contains 2², which needs a to be even; and a² contains 3² when a is a multiple of 3. So a must be a multiple of 6, and the smallest is 6 (6² = 36 = 18 × 2). "
  "9² = 81 is odd and so not divisible by 18; 12 and 18 also work, but they are not the smallest.",
  "18 = 2 × 3²। a² में हर अभाज्य सम घात में आता है, इसलिए a² में गुणनखंड 2 तभी हो सकता है जब उसमें 2² हो, जिसके लिए a को सम होना चाहिए; और a² में 3² तब होता है जब a, 3 का गुणज हो। अतः a, 6 का गुणज होना चाहिए, और सबसे छोटा 6 है (6² = 36 = 18 × 2)। "
  "9² = 81 विषम है और इसलिए 18 से विभाज्य नहीं; 12 और 18 भी चलते हैं, पर वे सबसे छोटे नहीं हैं।",
  "qa-nt-the-least-a-with-a-squared-divisible-by-18", lambda: str(next(a for a in range(1, 100) if a * a % 18 == 0)))

def _nt3():
    ns = [n for n in range(2, 100) if (n - 1) ** 2 + n ** 2 + (n + 1) ** 2 == 365]
    assert ns == [11] and 11 ** 2 + 12 ** 2 + 13 ** 2 == 434 and 12 ** 2 + 13 ** 2 + 14 ** 2 == 509 and 13 ** 2 + 14 ** 2 + 15 ** 2 == 590
    return str(3 * ns[0])
N(QA, "Number Theory", "medium",
  "The sum of the squares of three consecutive natural numbers is 365. What is the sum of the three numbers?",
  "तीन क्रमागत प्राकृत संख्याओं के वर्गों का योग 365 है। तीनों संख्याओं का योग क्या है?",
  ["33", "36", "39", "42"], 0,
  "Let the numbers be n - 1, n and n + 1. Their squares add up to 3n² + 2 = 365, so n² = 121 and n = 11: the numbers are 10, 11 and 12 (100 + 121 + 144 = 365), and their sum is 33. "
  "36, 39 and 42 are the sums of the next three triples -- 11, 12, 13 (squares add up to 434), 12, 13, 14 (509) and 13, 14, 15 (590) -- none of which gives 365.",
  "मान लीजिए संख्याएँ n - 1, n और n + 1 हैं। उनके वर्गों का योग 3n² + 2 = 365 है, अतः n² = 121 और n = 11: संख्याएँ 10, 11 और 12 हैं (100 + 121 + 144 = 365), और उनका योग 33 है। "
  "36, 39 और 42 अगली तीन तिकड़ियों के योग हैं -- 11, 12, 13 (वर्गों का योग 434), 12, 13, 14 (509) और 13, 14, 15 (590) -- जिनमें से कोई 365 नहीं देती।",
  "qa-nt-three-consecutive-squares-sum-365", _nt3)

N(QA, "Number Theory", "medium",
  "How many integers between 100 and 500 are divisible by 7 but not by 5?",
  "100 और 500 के बीच कितने पूर्णांक 7 से विभाज्य हैं पर 5 से नहीं?",
  ["12", "45", "57", "71"], 1,
  "The multiples of 7 between 100 and 500 run from 105 (7 × 15) to 497 (7 × 71): 71 - 15 + 1 = 57 of them. Those that are also multiples of 5, that is of 35, run from 105 to 490: 14 - 3 + 1 = 12. So 57 - 12 = 45 are divisible by 7 but not by 5. "
  "57 counts every multiple of 7; 12 counts only those that are also multiples of 5; 71 counts the multiples of 7 up to 500, including those below 100.",
  "100 और 500 के बीच 7 के गुणज 105 (7 × 15) से 497 (7 × 71) तक हैं: 71 - 15 + 1 = 57 । इनमें से जो 5 के भी गुणज हैं, यानी 35 के, वे 105 से 490 तक हैं: 14 - 3 + 1 = 12। अतः 57 - 12 = 45 संख्याएँ 7 से विभाज्य हैं पर 5 से नहीं। "
  "57, 7 का हर गुणज गिनता है; 12 केवल उन्हें गिनता है जो 5 के भी गुणज हैं; 71, 500 तक के 7 के गुणज गिनता है, 100 से छोटे भी।",
  "qa-nt-multiples-of-7-but-not-of-5", lambda: str(sum(1 for k in range(101, 500) if k % 7 == 0 and k % 5 != 0)))

def _nt5():
    x = F(36, 99)                              # 0.363636... : 100x - x = 36
    assert x == F(4, 11) and F(36, 90) == F(2, 5) and F(36, 999) == F(4, 111) and F(36, 100) == F(9, 25)
    return f"{x.numerator}/{x.denominator}"
N(QA, "Number Theory", "medium",
  "What is the value of 0.363636... (the digits 36 repeating without end) as a fraction in its lowest terms?",
  "0.363636... (अंक 36 बिना अंत के दोहराते हुए) का मान न्यूनतम रूप की भिन्न में क्या है?",
  ["4/111", "9/25", "4/11", "2/5"], 2,
  "Let x = 0.3636.... Then 100x = 36.3636..., and subtracting x gives 99x = 36, so x = 36/99 = 4/11. 9/25 = 0.36 is the decimal that stops after two places; 2/5 = 36/90 and "
  "4/111 = 36/999 put a wrong denominator under 36 -- 90 or 999 in place of 99, which has one 9 for each of the two repeating digits.",
  "मान लीजिए x = 0.3636...। तब 100x = 36.3636..., और x घटाने पर 99x = 36, अतः x = 36/99 = 4/11। 9/25 = 0.36 वह दशमलव है जो दो स्थानों के बाद रुक जाता है; 2/5 = 36/90 और "
  "4/111 = 36/999, 36 के नीचे ग़लत हर रखते हैं -- 99 की जगह 90 या 999, जबकि दोहराए जाने वाले दो अंकों के लिए हर में दो 9 आते हैं।",
  "qa-nt-a-repeating-decimal-as-a-fraction", _nt5)

N(QA, "Number Theory", "medium",
  "What is the smallest four-digit number that is exactly divisible by 12, 15 and 18?",
  "वह सबसे छोटी चार अंकों की संख्या कौन-सी है जो 12, 15 और 18 से पूर्णतः विभाज्य है?",
  ["1,080", "1,260", "1,800", "2,160"], 0,
  "LCM(12, 15, 18) = 180. The multiples of 180 are 180, 360, ..., 900, 1,080: 900 has only three digits, and 1,080 is the first multiple with four. "
  "1,260 is the next multiple, 1,800 is 180 × 10 and 2,160 is 180 × 12.",
  "12, 15 और 18 का लघुत्तम समापवर्त्य (LCM) 180 है। 180 के गुणज 180, 360, ..., 900, 1,080 हैं: 900 में केवल तीन अंक हैं, और 1,080 चार अंकों वाला पहला गुणज है। "
  "1,260 अगला गुणज है, 1,800 = 180 × 10 है और 2,160 = 180 × 12।",
  "qa-nt-the-smallest-four-digit-multiple-of-12-15-18", lambda: f"{next(n for n in range(1000, 10000) if n % 12 == 0 and n % 15 == 0 and n % 18 == 0):,}")

def _nt7():
    sixth = {"∛3": 3 ** 2, "√2": 2 ** 3, "⁶√7": 7}          # each number raised to the sixth power
    assert abs(3 ** (1 / 3) - 1.4422) < 1e-3 and abs(2 ** 0.5 - 1.4142) < 1e-3 and abs(7 ** (1 / 6) - 1.3831) < 1e-3
    return max(sixth, key=sixth.get)
N(QA, "Number Theory", "hard",
  "Which one of the following is the greatest?",
  "निम्नलिखित में से कौन-सी राशि सबसे बड़ी है?",
  ["∛3", "√2", "⁶√7", "All three are equal"], 0,
  "Raise each to the sixth power, the least common multiple of 2, 3 and 6: (√2)⁶ = 2³ = 8, (∛3)⁶ = 3² = 9 and (⁶√7)⁶ = 7. The largest sixth power belongs to ∛3, so ∛3 is the greatest "
  "(about 1.442, against √2 ≈ 1.414 and ⁶√7 ≈ 1.383).",
  "हर राशि की छठी घात लीजिए, जो 2, 3 और 6 का लघुत्तम समापवर्त्य है: (√2)⁶ = 2³ = 8, (∛3)⁶ = 3² = 9 और (⁶√7)⁶ = 7। सबसे बड़ी छठी घात ∛3 की है, इसलिए ∛3 सबसे बड़ी है "
  "(लगभग 1.442, जबकि √2 ≈ 1.414 और ⁶√7 ≈ 1.383)।",
  "qa-nt-three-surds-compared", _nt7,
  opts_hi=["∛3", "√2", "⁶√7", "तीनों बराबर हैं"])

def _nt8():
    s = [2, 3]                                  # s_n = x^n + 1/x^n with x + 1/x = 3: s_(n+1) = 3 s_n - s_(n-1)
    for _ in range(2):
        s.append(3 * s[-1] - s[-2])
    assert s[2] == 7 and s[3] == 18
    return str(s[3])
N(QA, "Number Theory", "hard",
  "If x + 1/x = 3, what is the value of x³ + 1/x³?",
  "यदि x + 1/x = 3, तो x³ + 1/x³ का मान क्या है?",
  ["3", "7", "9", "18"], 3,
  "(x + 1/x)³ = x³ + 1/x³ + 3(x + 1/x), so 27 = x³ + 1/x³ + 9 and x³ + 1/x³ = 18. 3 is the value of x + 1/x itself; 7 is x² + 1/x² (= 3² - 2); 9 is 3 × 3, which has nothing to do with the cube sum.",
  "(x + 1/x)³ = x³ + 1/x³ + 3(x + 1/x), अतः 27 = x³ + 1/x³ + 9 और x³ + 1/x³ = 18। 3 स्वयं x + 1/x का मान है; 7, x² + 1/x² (= 3² - 2) है; 9, 3 × 3 है, जिसका घनों के योग से कोई संबंध नहीं।",
  "qa-nt-cube-of-x-plus-one-over-x", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    gap = F(1)                                  # the distance between consecutive buses, in any unit
    behind, ahead = F(1, 12), F(1, 4)           # b - w and b + w
    b = (behind + ahead) / 2
    assert (ahead - behind) / 2 == F(1, 12)     # the man's speed, one gap every 12 minutes
    return str(gap / b)
N(QA, "Speed-Distance-Time", "hard",
  "A man walking at a steady pace along a road notices that a bus going the same way overtakes him every 12 minutes, while a bus coming from the opposite direction passes him every 4 minutes. "
  "If all the buses run at the same speed and leave their depots at equal intervals, at what interval, in minutes, do the buses leave a depot?",
  "सड़क पर एक समान चाल से चलता एक व्यक्ति देखता है कि उसी दिशा में जाने वाली बस उसे हर 12 मिनट में पार करती है, जबकि विपरीत दिशा से आने वाली बस उसके पास से हर 4 मिनट में गुज़रती है। "
  "यदि सभी बसें एक ही चाल से चलती हैं और अपने डिपो से बराबर अंतराल पर छूटती हैं, तो बसें डिपो से कितने मिनट के अंतराल पर छूटती हैं?",
  ["3", "6", "8", "16"], 1,
  "Let the gap between consecutive buses be d, the bus speed b and the man's speed w. A bus going the same way gains the gap d on him every 12 minutes, so d/(b - w) = 12; a bus coming the other way meets him every 4 minutes, so d/(b + w) = 4. "
  "Then b - w = d/12 and b + w = d/4, which give b = d/6: the buses leave a depot every d ÷ b = 6 minutes (and w = d/12). 8 is the average of 12 and 4, 16 is their sum and 3 their ratio -- none of them follows from the two equations.",
  "मान लीजिए क्रमागत बसों के बीच की दूरी d है, बस की चाल b और व्यक्ति की चाल w। उसी दिशा में जाने वाली बस हर 12 मिनट में उस पर दूरी d की बढ़त बनाती है, इसलिए d/(b - w) = 12; विपरीत दिशा से आने वाली बस उसे हर 4 मिनट में मिलती है, इसलिए d/(b + w) = 4। "
  "तब b - w = d/12 और b + w = d/4, जिनसे b = d/6 मिलता है: बसें डिपो से हर d ÷ b = 6 मिनट पर छूटती हैं (और w = d/12)। 8, 12 और 4 का औसत है, 16 उनका योग है और 3 उनका अनुपात -- इनमें से कोई दोनों समीकरणों से नहीं निकलता।",
  "qa-sdt-buses-that-overtake-and-meet-a-walker", _sdt1)

N(QA, "Speed-Distance-Time", "medium",
  "A car runs for the first half of its journey time at 40 km/h and for the second half of the time at 60 km/h. What is its average speed for the whole journey?",
  "एक कार अपनी यात्रा के समय के पहले आधे भाग में 40 किमी/घंटा और समय के दूसरे आधे भाग में 60 किमी/घंटा की चाल से चलती है। पूरी यात्रा में उसकी औसत चाल क्या है?",
  ["48 km/h", "50 km/h", "52 km/h", "100 km/h"], 1,
  "In equal times the distances are 40t and 60t, so the average speed is (40t + 60t) ÷ 2t = 50 km/h: when the time at each speed is the same, it is the simple average of the speeds. "
  "48 km/h is the average when the two halves of the distance, not of the time, are run at the two speeds (2 × 40 × 60 ÷ 100); 100 km/h adds the speeds; 52 km/h does not come from either rule.",
  "बराबर समयों में दूरियाँ 40t और 60t हैं, इसलिए औसत चाल (40t + 60t) ÷ 2t = 50 किमी/घंटा है: जब हर चाल पर समय बराबर हो, तो वह चालों का साधारण औसत होती है। "
  "48 किमी/घंटा तब की औसत चाल है जब समय के नहीं बल्कि दूरी के दो आधे भाग इन दो चालों से तय हों (2 × 40 × 60 ÷ 100); 100 किमी/घंटा चालों को जोड़ता है; 52 किमी/घंटा किसी भी नियम से नहीं आता।",
  "qa-sdt-equal-times-at-two-speeds", lambda: f"{F(40 + 60, 2)} km/h",
  opts_hi=["48 किमी/घंटा", "50 किमी/घंटा", "52 किमी/घंटा", "100 किमी/घंटा"])

def _sdt3():
    vs = [v for v in range(51, 400) if F(2 * 50 * v, 50 + v) == 60]
    assert vs == [75] and F(50 + 70, 2) == 60 and 50 * 72 == 60 ** 2 and F(2 * 50 * 70, 120) != 60 and F(2 * 50 * 72, 122) != 60
    return f"{vs[0]} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "A man drives from A to B at 50 km/h and returns along the same road at a speed for which his average speed for the whole round trip is 60 km/h. At what speed does he return?",
  "एक व्यक्ति A से B तक 50 किमी/घंटा की चाल से गाड़ी चलाता है और उसी सड़क से ऐसी चाल से लौटता है कि आने-जाने की पूरी यात्रा में उसकी औसत चाल 60 किमी/घंटा है। वह किस चाल से लौटता है?",
  ["60 km/h", "70 km/h", "72 km/h", "75 km/h"], 3,
  "For a round trip over the same distance d, the average speed is 2uv/(u + v): 2 × 50 × v/(50 + v) = 60, so 100v = 3000 + 60v and v = 75 km/h. Check: d/50 + d/75 = d/30 hours for 2d, an average of 60 km/h. "
  "70 km/h treats the average as the simple mean of the two speeds ((50 + 70) ÷ 2 = 60), which holds for equal times, not equal distances; 60 km/h is the average itself; "
  "72 km/h would make 60 the geometric mean of the two speeds (50 × 72 = 60²), which is not how an average speed is found.",
  "समान दूरी d की आने-जाने की यात्रा में औसत चाल 2uv/(u + v) होती है: 2 × 50 × v/(50 + v) = 60, अतः 100v = 3000 + 60v और v = 75 किमी/घंटा। जाँच: 2d के लिए d/50 + d/75 = d/30 घंटे, यानी औसत 60 किमी/घंटा। "
  "70 किमी/घंटा औसत को दोनों चालों का साधारण माध्य ((50 + 70) ÷ 2 = 60) मान लेता है, जो बराबर समय के लिए सही है, बराबर दूरियों के लिए नहीं; 60 किमी/घंटा स्वयं औसत है; "
  "72 किमी/घंटा 60 को दोनों चालों का गुणोत्तर माध्य बना देता है (50 × 72 = 60²), जबकि औसत चाल इस तरह नहीं निकलती।",
  "qa-sdt-the-return-speed-that-makes-an-average", _sdt3,
  opts_hi=["60 किमी/घंटा", "70 किमी/घंटा", "72 किमी/घंटा", "75 किमी/घंटा"])

N(QA, "Speed-Distance-Time", "easy",
  "Two persons start together from the same place and walk in the same direction at 4 km/h and 6 km/h. After how many hours will they be 10 km apart?",
  "दो व्यक्ति एक ही स्थान से एक साथ चलते हैं और एक ही दिशा में 4 किमी/घंटा और 6 किमी/घंटा की चाल से चलते हैं। कितने घंटे बाद वे एक-दूसरे से 10 किमी दूर होंगे?",
  ["1", "2.5", "5", "10"], 2,
  "The faster walker gains 6 - 4 = 2 km every hour, so the gap reaches 10 km after 10 ÷ 2 = 5 hours. 1 hour is the answer if they walked in opposite directions (10 ÷ (4 + 6)); 2.5 divides by the slower speed alone (10 ÷ 4); 10 is the distance itself.",
  "तेज़ चलने वाला हर घंटे 6 - 4 = 2 किमी की बढ़त बनाता है, इसलिए अंतर 10 ÷ 2 = 5 घंटे में 10 किमी हो जाता है। 1 घंटा तब का उत्तर है जब वे विपरीत दिशाओं में चलते (10 ÷ (4 + 6)); 2.5 केवल धीमी चाल से भाग देता है (10 ÷ 4); 10 स्वयं दूरी है।",
  "qa-sdt-two-walkers-in-the-same-direction", lambda: str(F(10, 6 - 4)))

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    c_inc = F(100)
    b_inc = c_inc * F(80, 100)
    a_inc = b_inc * F(125, 100)
    r = a_inc / c_inc
    assert F(5, 4) == F(125, 100) and F(4, 5) == F(80, 100) and F(21, 20) == 1 + F(25 - 20, 100)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A's income is 25% more than B's, and B's income is 20% less than C's. What is the ratio of A's income to C's income?",
  "A की आय B की आय से 25% अधिक है, और B की आय C की आय से 20% कम है। A की आय का C की आय से अनुपात क्या है?",
  ["4 : 5", "5 : 4", "21 : 20", "1 : 1"], 3,
  "Take C's income as 100. B's is 20% less: 80. A's is 25% more than B's: 80 × 1.25 = 100. So A : C = 1 : 1. 5 : 4 is A : B, and 4 : 5 is B : C; 21 : 20 comes from adding the percentages, +25% - 20% = +5%, which are on different bases.",
  "C की आय 100 मानिए। B की आय 20% कम है: 80। A की आय B से 25% अधिक है: 80 × 1.25 = 100। अतः A : C = 1 : 1। 5 : 4, A : B है, और 4 : 5, B : C; 21 : 20 प्रतिशतों को जोड़ने से आता है, +25% - 20% = +5%, जबकि वे अलग-अलग आधारों पर हैं।",
  "qa-rm-percentages-that-cancel", _rm1)

def _rm2():
    ks = [k for k in range(1, 100) if (3 * k) ** 2 + (5 * k) ** 2 == 1224]
    assert ks == [6]
    return str(8 * ks[0])
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Two numbers are in the ratio 3 : 5 and the sum of their squares is 1,224. What is their sum?",
  "दो संख्याएँ 3 : 5 के अनुपात में हैं और उनके वर्गों का योग 1,224 है। उनका योग क्या है?",
  ["34", "36", "48", "64"], 2,
  "Write the numbers as 3k and 5k: 9k² + 25k² = 34k² = 1,224, so k² = 36 and k = 6. The numbers are 18 and 30, and their sum is 48. "
  "34 is the coefficient of k²; 36 is k² itself; 64 = 8 × 8 takes the sum of the ratio terms, 8, as the multiplier.",
  "संख्याओं को 3k और 5k लिखिए: 9k² + 25k² = 34k² = 1,224, अतः k² = 36 और k = 6। संख्याएँ 18 और 30 हैं, और उनका योग 48 है। "
  "34, k² का गुणांक है; 36 स्वयं k² है; 64 = 8 × 8 अनुपात के पदों के योग, 8, को ही गुणक मान लेता है।",
  "qa-rm-a-ratio-and-a-sum-of-squares", _rm2)

def _rm3():
    r = F(60 - 48, 48 - 0)                      # water : milk, by alligation with water at price 0
    assert F(1, 5) == F(12, 60) and F(5, 4) == F(60, 48) and 4 * 60 == 5 * 48
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In what ratio of water to milk should water be mixed with milk costing ₹60 a litre so that the mixture is worth ₹48 a litre?",
  "₹60 प्रति लीटर वाले दूध में पानी को पानी और दूध के किस अनुपात में मिलाया जाए कि मिश्रण का मूल्य ₹48 प्रति लीटर हो?",
  ["1 : 5", "1 : 4", "5 : 4", "4 : 1"], 1,
  "Water costs nothing, so by alligation the quantities of water and milk are in the ratio (60 - 48) : (48 - 0) = 12 : 48 = 1 : 4. Check: 1 litre of water with 4 litres of milk gives 5 litres worth 4 × 60 = ₹240, which is ₹48 a litre. "
  "1 : 5 compares the water with the whole mixture; 4 : 1 is the ratio upside down; 5 : 4 is 60 : 48.",
  "पानी की कोई क़ीमत नहीं, इसलिए एलिगेशन से पानी और दूध की मात्राओं का अनुपात (60 - 48) : (48 - 0) = 12 : 48 = 1 : 4 है। जाँच: 1 लीटर पानी और 4 लीटर दूध से 5 लीटर मिश्रण बनता है जिसका मूल्य 4 × 60 = ₹240 है, यानी ₹48 प्रति लीटर। "
  "1 : 5 पानी की तुलना पूरे मिश्रण से करता है; 4 : 1 अनुपात को उलट देता है; 5 : 4 यानी 60 : 48।",
  "qa-rm-water-in-milk-of-a-given-price", _rm3)

def _rm4():
    xs = [x for x in range(1, 200) if F(12 + x, 40 + x) == F(1, 2)]
    assert xs == [16]
    return str(xs[0])
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A 40-litre solution contains 30% alcohol. How many litres of pure alcohol must be added to it to make the alcohol 50% of the new solution?",
  "40 लीटर के एक विलयन में 30% एल्कोहल है। उसमें कितने लीटर शुद्ध एल्कोहल मिलाया जाए कि नए विलयन में एल्कोहल 50% हो जाए?",
  ["8", "12", "16", "20"], 2,
  "The solution holds 30% of 40 = 12 litres of alcohol. After adding x litres of pure alcohol, (12 + x)/(40 + x) = 1/2, so 24 + 2x = 40 + x and x = 16. Check: 28 litres of alcohol in 56 litres of solution is 50%. "
  "8 is 20% of 40, the rise in percentage applied to the original quantity; 12 is the alcohol already present; 20 is 50% of 40.",
  "विलयन में 40 का 30% = 12 लीटर एल्कोहल है। x लीटर शुद्ध एल्कोहल मिलाने पर (12 + x)/(40 + x) = 1/2, अतः 24 + 2x = 40 + x और x = 16। जाँच: 56 लीटर विलयन में 28 लीटर एल्कोहल 50% है। "
  "8, 40 का 20% है, यानी प्रतिशत की वृद्धि को मूल मात्रा पर लगाना; 12 पहले से मौजूद एल्कोहल है; 20, 40 का 50% है।",
  "qa-rm-pure-alcohol-added-to-a-solution", _rm4)

def _rm5():
    whole = 4 ** 2
    pieces = 1 ** 2 + 3 ** 2
    loss = F(whole - pieces, whole) * 100
    assert F(pieces, whole) * 100 == F(125, 2) and F(2 ** 2 + 2 ** 2, whole) == F(1, 2) and F(3, 4) * 100 == 75
    return f"{float(loss):g}%"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "The value of a diamond is proportional to the square of its weight. A diamond of 4 grams breaks into two pieces of 1 gram and 3 grams. What percentage of the diamond's value is lost?",
  "किसी हीरे का मूल्य उसके भार के वर्ग के समानुपाती होता है। 4 ग्राम का एक हीरा 1 ग्राम और 3 ग्राम के दो टुकड़ों में टूट जाता है। हीरे के मूल्य का कितना प्रतिशत नष्ट हो जाता है?",
  ["37.5%", "50%", "62.5%", "75%"], 0,
  "Value is proportional to weight²: the whole diamond is worth 4² = 16 units, and the two pieces are worth 1² + 3² = 10 units. So 6 units, 6/16 = 37.5% of the value, are lost. "
  "62.5% is the value that is left; 50% is the loss if the diamond had broken into two pieces of 2 grams (8 of 16 units); 75% is the share of the weight in the larger piece.",
  "मूल्य भार² के समानुपाती है: पूरा हीरा 4² = 16 इकाई का है, और दोनों टुकड़े 1² + 3² = 10 इकाई के। अतः 6 इकाई, यानी मूल्य का 6/16 = 37.5%, नष्ट हुआ। "
  "62.5% बचा हुआ मूल्य है; 50% तब की हानि है जब हीरा 2-2 ग्राम के दो टुकड़ों में टूटता (16 में से 8 इकाई); 75% बड़े टुकड़े में भार का अंश है।",
  "qa-rm-a-diamond-worth-the-square-of-its-weight", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
N(QA, "Percentage & Profit-Loss", "medium",
  "Two successive discounts of 20% and 15% are equivalent to a single discount of:",
  "20% और 15% की दो क्रमागत छूटें किस एकल छूट के बराबर हैं?",
  ["32%", "35%", "36%", "68%"], 0,
  "After a 20% discount the price is 0.80 of the marked price, and after a further 15% it is 0.80 × 0.85 = 0.68 of it, so the single discount is 32%. 35% adds the two discounts; 36% applies 20% twice (1 - 0.8 × 0.8); 68% is the price that is left.",
  "20% छूट के बाद मूल्य अंकित मूल्य का 0.80 रह जाता है, और 15% की और छूट के बाद 0.80 × 0.85 = 0.68, इसलिए एकल छूट 32% है। 35% दोनों छूटें जोड़ देता है; 36% 20% दो बार लगाता है (1 - 0.8 × 0.8); 68% बचा हुआ मूल्य है।",
  "qa-pp-two-successive-discounts", lambda: f"{round((1 - F(80, 100) * F(85, 100)) * 100)}%")

def _pp2():
    per_year = F(1350 - 1200, 5 - 2)
    p = 1200 - 2 * per_year
    assert per_year == 50 and p + 5 * per_year == 1350
    return f"₹{int(p):,}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A sum of money amounts to ₹1,200 in 2 years and to ₹1,350 in 5 years at simple interest. What is the sum?",
  "साधारण ब्याज पर कोई धनराशि 2 वर्षों में ₹1,200 और 5 वर्षों में ₹1,350 हो जाती है। वह धनराशि क्या है?",
  ["₹1,100", "₹1,150", "₹1,200", "₹1,350"], 0,
  "The interest for the 3 years from the 2nd to the 5th is ₹1,350 - ₹1,200 = ₹150, so simple interest is ₹50 a year. The sum is the amount after 2 years less 2 years' interest: ₹1,200 - ₹100 = ₹1,100. "
  "₹1,150 takes away only one year's interest; ₹1,200 and ₹1,350 are the amounts after 2 and after 5 years.",
  "दूसरे से पाँचवें वर्ष तक के 3 वर्षों का ब्याज ₹1,350 - ₹1,200 = ₹150 है, इसलिए साधारण ब्याज ₹50 प्रति वर्ष है। मूलधन 2 वर्ष बाद की राशि में से 2 वर्षों का ब्याज घटाने पर मिलता है: ₹1,200 - ₹100 = ₹1,100। "
  "₹1,150 केवल एक वर्ष का ब्याज घटाता है; ₹1,200 और ₹1,350 क्रमशः 2 और 5 वर्ष बाद की राशियाँ हैं।",
  "qa-pp-simple-interest-from-two-amounts", _pp2)

def _pp3():
    si = F(8000) * F(10, 100)
    ci = F(8000) * (F(105, 100) ** 2 - 1)
    assert si == 800 and ci == 820
    return f"₹{int(ci - si)}"
N(QA, "Percentage & Profit-Loss", "hard",
  "What is the difference between the compound interest, compounded half-yearly, and the simple interest on ₹8,000 for 1 year at 10% per annum?",
  "₹8,000 पर 10% वार्षिक दर से 1 वर्ष का अर्धवार्षिक रूप से संयोजित चक्रवृद्धि ब्याज और साधारण ब्याज के बीच अंतर क्या है?",
  ["₹0", "₹20", "₹40", "₹820"], 1,
  "Simple interest is 10% of ₹8,000 = ₹800. Compounded half-yearly, the rate is 5% for each of 2 half-years: 8,000 × (1.05² - 1) = 8,000 × 0.1025 = ₹820. The difference is ₹20. "
  "₹0 would be the difference if the interest were compounded once a year, since over a single year compound and simple interest are equal; ₹820 is the compound interest itself; ₹40 doubles the difference.",
  "साधारण ब्याज ₹8,000 का 10% = ₹800 है। अर्धवार्षिक संयोजन में दर 2 अर्ध-वर्षों में से प्रत्येक के लिए 5% है: 8,000 × (1.05² - 1) = 8,000 × 0.1025 = ₹820। अंतर ₹20 है। "
  "₹0 तब अंतर होता यदि ब्याज साल में एक बार संयोजित होता, क्योंकि एक वर्ष में चक्रवृद्धि और साधारण ब्याज बराबर होते हैं; ₹820 स्वयं चक्रवृद्धि ब्याज है; ₹40 अंतर को दोगुना कर देता है।",
  "qa-pp-half-yearly-compounding-against-simple-interest", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    s = lambda n: 3 * n * n + 2 * n
    assert s(10) == 320 and s(9) == 261 and all(s(n) - s(n - 1) == 6 * n - 1 for n in range(2, 30))
    return str(s(10) - s(9))
N(QA, "Sequences & Series", "hard",
  "The sum of the first n terms of a sequence is 3n² + 2n. What is its 10th term?",
  "किसी अनुक्रम के पहले n पदों का योग 3n² + 2n है। उसका 10वाँ पद क्या है?",
  ["59", "62", "261", "320"], 0,
  "The 10th term is the sum of the first 10 terms less the sum of the first 9: (3 × 100 + 20) - (3 × 81 + 18) = 320 - 261 = 59. (In general the n-th term is 6n - 1.) "
  "320 is the sum of the first 10 terms and 261 the sum of the first 9; 62 comes from the wrong form 6n + 2.",
  "10वाँ पद पहले 10 पदों के योग में से पहले 9 पदों का योग घटाने पर मिलता है: (3 × 100 + 20) - (3 × 81 + 18) = 320 - 261 = 59। (सामान्यतः n-वाँ पद 6n - 1 है।) "
  "320 पहले 10 पदों का योग है और 261 पहले 9 का; 62 ग़लत रूप 6n + 2 से आता है।",
  "qa-ss-a-series-whose-partial-sums-are-given", _ss1)

def _ss2():
    t = [2]
    for i in range(6):
        t.append(t[-1] + 1 if i % 2 == 0 else t[-1] * 2)
    assert t[:6] == [2, 3, 6, 7, 14, 15]
    return str(t[6])
N(QA, "Sequences & Series", "medium",
  "What number should come next in the series 2, 3, 6, 7, 14, 15, ... ?",
  "श्रेणी 2, 3, 6, 7, 14, 15, ... में अगली संख्या कौन-सी होनी चाहिए?",
  ["15", "16", "28", "30"], 3,
  "The rule alternates between adding 1 and doubling: 2 + 1 = 3, 3 × 2 = 6, 6 + 1 = 7, 7 × 2 = 14, 14 + 1 = 15, and next 15 × 2 = 30. 15 repeats the last term; 16 adds 1 again; 28 doubles the term before the last.",
  "नियम बारी-बारी से 1 जोड़ने और दोगुना करने का है: 2 + 1 = 3, 3 × 2 = 6, 6 + 1 = 7, 7 × 2 = 14, 14 + 1 = 15, और अगला 15 × 2 = 30। 15 अंतिम पद को दोहराता है; 16 फिर 1 जोड़ता है; 28 अंतिम से पहले वाले पद को दोगुना करता है।",
  "qa-ss-a-series-that-alternates-two-operations", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
N(QA, "Permutation & Combination", "medium",
  "A card is drawn at random from a well-shuffled pack of 52 cards. What is the probability that it is a red card or a king?",
  "52 पत्तों की भली-भाँति फेंटी गई गड्डी में से एक पत्ता यादृच्छिक रूप से निकाला जाता है। उसके लाल पत्ता या बादशाह होने की प्रायिकता क्या है?",
  ["1/13", "1/2", "7/13", "15/26"], 2,
  "There are 26 red cards and 4 kings, of which 2 are red and so already counted: 26 + 4 - 2 = 28 cards, and 28/52 = 7/13. 15/26 = 30/52 counts the two red kings twice; 1/2 is the chance of a red card alone; 1/13 is the chance of a king alone.",
  "26 पत्ते लाल हैं और 4 बादशाह, जिनमें से 2 लाल हैं और इसलिए पहले ही गिने जा चुके हैं: 26 + 4 - 2 = 28 पत्ते, और 28/52 = 7/13। 15/26 = 30/52 दो लाल बादशाहों को दो बार गिनता है; 1/2 केवल लाल पत्ते की प्रायिकता है; 1/13 केवल बादशाह की।",
  "qa-pc-a-card-that-is-red-or-a-king", lambda: str(F(26 + 4 - 2, 52)))

N(QA, "Permutation & Combination", "hard",
  "In how many ways can 10 people be divided into two groups of 5 each?",
  "10 व्यक्तियों को 5-5 के दो समूहों में कितने तरीकों से बाँटा जा सकता है?",
  ["63", "126", "252", "504"], 1,
  "The first group of 5 can be chosen in C(10, 5) = 252 ways, but that counts every division twice, once for each group taken as 'the first'. So the number of divisions is 252 ÷ 2 = 126. "
  "252 treats the two groups as different (say, a red team and a blue team); 504 doubles it again; 63 halves it once too often.",
  "पहला 5 व्यक्तियों का समूह C(10, 5) = 252 तरीकों से चुना जा सकता है, पर इससे हर बँटवारा दो बार गिना जाता है, हर समूह को 'पहला' मानकर एक बार। इसलिए बँटवारों की संख्या 252 ÷ 2 = 126 है। "
  "252 दोनों समूहों को अलग-अलग मानता है (मान लीजिए लाल टीम और नीली टीम); 504 उसे फिर दोगुना कर देता है; 63 उसे एक बार अधिक आधा कर देता है।",
  "qa-pc-ten-people-split-into-two-teams", lambda: str(math.comb(10, 5) // 2))

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    arc = F(22, 7) * 14
    return f"{int(arc + 2 * 14)} m"
N(QA, "Geometry & Mensuration", "medium",
  "A semicircular plot has a radius of 14 m. What length of fence is needed to enclose it completely, including its straight edge? (Take π = 22/7.)",
  "एक अर्धवृत्ताकार भूखंड की त्रिज्या 14 मीटर है। उसे उसकी सीधी भुजा सहित पूरा घेरने के लिए कितनी लंबाई की बाड़ चाहिए? (π = 22/7 लीजिए।)",
  ["28 m", "44 m", "58 m", "72 m"], 3,
  "The curved edge is half a circle: π × 14 = 44 m. The straight edge is the diameter, 28 m. The fence needed is 44 + 28 = 72 m. 44 m is the arc alone; 58 m adds only one radius (44 + 14); 28 m is the diameter alone.",
  "वक्र किनारा आधा वृत्त है: π × 14 = 44 मीटर। सीधा किनारा व्यास, 28 मीटर, है। चाहिए बाड़ 44 + 28 = 72 मीटर है। 44 मीटर केवल चाप है; 58 मीटर केवल एक त्रिज्या जोड़ता है (44 + 14); 28 मीटर केवल व्यास है।",
  "qa-gm-fencing-a-semicircular-plot", _gm1,
  opts_hi=["28 मीटर", "44 मीटर", "58 मीटर", "72 मीटर"])

def _gm2():
    slant = math.hypot(5, 12)
    assert slant == 13
    return f"{5 * 13}π cm²"
N(QA, "Geometry & Mensuration", "hard",
  "A cone has a base radius of 5 cm and a height of 12 cm. What is the area of its curved surface?",
  "एक शंकु की आधार त्रिज्या 5 सेमी और ऊँचाई 12 सेमी है। उसके वक्र पृष्ठ का क्षेत्रफल क्या है?",
  ["60π cm²", "65π cm²", "90π cm²", "130π cm²"], 1,
  "The slant height is √(5² + 12²) = 13 cm, and the curved surface area is π × r × l = π × 5 × 13 = 65π cm². 60π uses the height 12 in place of the slant height; "
  "90π = π × 5 × (5 + 13) is the whole surface, the curved part and the base together; 130π doubles the curved area.",
  "तिर्यक ऊँचाई √(5² + 12²) = 13 सेमी है, और वक्र पृष्ठ का क्षेत्रफल π × r × l = π × 5 × 13 = 65π वर्ग सेमी है। 60π तिर्यक ऊँचाई की जगह ऊँचाई 12 लेता है; "
  "90π = π × 5 × (5 + 13) पूरा पृष्ठ है, वक्र भाग और आधार मिलाकर; 130π वक्र क्षेत्रफल को दोगुना कर देता है।",
  "qa-gm-the-curved-surface-of-a-cone", _gm2,
  opts_hi=["60π वर्ग सेमी", "65π वर्ग सेमी", "90π वर्ग सेमी", "130π वर्ग सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    a_rate = F(75, 100) * F(1, 12)
    return str(1 / a_rate)
N(QA, "Time & Work", "medium",
  "A is 25% less efficient than B. If B can finish a job in 12 days, in how many days can A finish it?",
  "A, B से 25% कम कुशल है। यदि B एक काम 12 दिनों में पूरा कर सकता है, तो A उसे कितने दिनों में पूरा कर सकता है?",
  ["9", "12", "15", "16"], 3,
  "A does 75% of what B does in a day, so A takes 12 ÷ 0.75 = 16 days. 9 days = 12 × 0.75 would make A faster than B; 12 is B's own time; 15 adds 25% of 12 days to B's time, but a smaller output per day means more time in proportion to 1/0.75, not 1.25.",
  "A एक दिन में B के काम का 75% करता है, इसलिए A को 12 ÷ 0.75 = 16 दिन लगते हैं। 9 दिन = 12 × 0.75, A को B से तेज़ बना देता; 12 स्वयं B का समय है; 15, B के समय में 12 दिनों का 25% जोड़ता है, पर प्रतिदिन कम काम का अर्थ है समय 1/0.75 के अनुपात में बढ़ना, 1.25 के नहीं।",
  "qa-tw-a-worker-25-per-cent-less-efficient", _tw1)

def _tw2():
    needed = 50 * F(60, 40)
    return str(needed - 50)
N(QA, "Time & Work", "hard",
  "A contractor undertakes to build a road in 50 days and employs 50 men. After 25 days, only 40% of the work is done. How many more men must be employed to finish the road on time?",
  "एक ठेकेदार 50 दिनों में सड़क बनाने का ज़िम्मा लेता है और 50 आदमी लगाता है। 25 दिन बाद केवल 40% काम हुआ है। सड़क समय पर पूरी करने के लिए और कितने आदमी लगाने होंगे?",
  ["20", "25", "50", "75"], 1,
  "In 25 days 50 men did 40% of the work, so 60% is left and it must be done in the remaining 25 days. The men needed are in proportion to the work to be done in the same time: 50 × 60/40 = 75 men in all, so 75 - 50 = 25 more are needed. "
  "75 is the total number of men needed, not the extra number; 50 would double the gang; 20 is the difference between 60% and 40%.",
  "25 दिनों में 50 आदमियों ने 40% काम किया, इसलिए 60% बचा है और उसे शेष 25 दिनों में करना है। उसी समय में किए जाने वाले काम के अनुपात में आदमी चाहिए: कुल 50 × 60/40 = 75 आदमी, अतः 75 - 50 = 25 और चाहिए। "
  "75 कुल आवश्यक आदमियों की संख्या है, अतिरिक्त की नहीं; 50 टोली को दोगुना कर देता; 20, 60% और 40% का अंतर है।",
  "qa-tw-a-job-that-is-behind-schedule", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (4)
N(QA, "Puzzle Hybrid", "easy",
  "In a knockout tournament 64 teams take part, and a team is out as soon as it loses a match. How many matches are played in all to decide the winner?",
  "एक नॉकआउट प्रतियोगिता में 64 टीमें भाग लेती हैं, और कोई टीम मैच हारते ही बाहर हो जाती है। विजेता तय करने के लिए कुल कितने मैच खेले जाते हैं?",
  ["32", "62", "63", "64"], 2,
  "Every match removes exactly one team, and 63 teams must be removed to leave a single winner, so 63 matches are played (32 + 16 + 8 + 4 + 2 + 1 = 63). 32 counts only the first round; 64 is the number of teams; 62 forgets the final.",
  "हर मैच ठीक एक टीम को बाहर करता है, और एक विजेता बचाने के लिए 63 टीमों को बाहर होना है, इसलिए 63 मैच खेले जाते हैं (32 + 16 + 8 + 4 + 2 + 1 = 63)। 32 केवल पहला दौर गिनता है; 64 टीमों की संख्या है; 62 फ़ाइनल भूल जाता है।",
  "qa-ph-a-knockout-draw", lambda: str(64 - 1))

def _ph2():
    from math import lcm
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    assert lcm(4, 6, 9) == 36
    return days[lcm(4, 6, 9) % 7]
N(QA, "Puzzle Hybrid", "medium",
  "Three people visit a library every 4, 6 and 9 days respectively. If all three visited it on a Monday, on which day of the week will they next visit it together?",
  "तीन व्यक्ति एक पुस्तकालय में क्रमशः हर 4, 6 और 9 दिन पर जाते हैं। यदि तीनों सोमवार को वहाँ गए थे, तो वे अगली बार एक साथ सप्ताह के किस दिन वहाँ जाएँगे?",
  ["Monday", "Tuesday", "Wednesday", "Thursday"], 1,
  "They are together again after LCM(4, 6, 9) = 36 days. 36 = 5 × 7 + 1, so the day is one day after Monday: Tuesday. Monday would come after 35 or 42 days, which are not common multiples of the three gaps; Wednesday and Thursday correspond to 37 and 38 days.",
  "वे 4, 6 और 9 के लघुत्तम समापवर्त्य (LCM), यानी 36 दिन बाद फिर साथ होते हैं। 36 = 5 × 7 + 1, इसलिए दिन सोमवार के एक दिन बाद का है: मंगलवार। सोमवार 35 या 42 दिन बाद आता, जो तीनों अंतरालों के उभयनिष्ठ गुणज नहीं हैं; बुधवार और गुरुवार 37 और 38 दिन के अनुरूप हैं।",
  "qa-ph-three-people-on-a-library-rota", _ph2,
  opts_hi=["सोमवार", "मंगलवार", "बुधवार", "गुरुवार"])

def _ph3():
    w = {1: 1, 2: 2}
    for n in range(3, 7):
        w[n] = w[n - 1] + w[n - 2]
    return str(w[6])
N(QA, "Puzzle Hybrid", "hard",
  "A person climbs a staircase of 6 steps, taking either 1 step or 2 steps at a time. In how many different ways can the staircase be climbed?",
  "एक व्यक्ति 6 सीढ़ियों की एक सीढ़ी पर एक बार में 1 या 2 सीढ़ियाँ चढ़ते हुए जाता है। पूरी सीढ़ी कितने अलग-अलग तरीकों से चढ़ी जा सकती है?",
  ["5", "8", "12", "13"], 3,
  "Let w(n) be the number of ways to climb n steps. The last move is 1 step or 2 steps, so w(n) = w(n - 1) + w(n - 2), with w(1) = 1 and w(2) = 2: w(3) = 3, w(4) = 5, w(5) = 8, w(6) = 13. "
  "5 and 8 are the numbers of ways for 4 and 5 steps; 12 = 2 × 6 has no basis.",
  "मान लीजिए n सीढ़ियाँ चढ़ने के तरीकों की संख्या w(n) है। अंतिम चाल 1 सीढ़ी या 2 सीढ़ियों की होती है, इसलिए w(n) = w(n - 1) + w(n - 2), जहाँ w(1) = 1 और w(2) = 2: w(3) = 3, w(4) = 5, w(5) = 8, w(6) = 13। "
  "5 और 8 क्रमशः 4 और 5 सीढ़ियों के तरीकों की संख्याएँ हैं; 12 = 2 × 6 का कोई आधार नहीं।",
  "qa-ph-climbing-stairs-one-or-two-at-a-time", _ph3)

def _ph4():
    pieces = 1
    for cut in range(1, 5):
        pieces += cut                              # the k-th cut crosses the k - 1 earlier cuts and adds k pieces
    assert pieces == 11 and 2 * 4 == 8 and 1 + 2 + 3 + 4 == 10
    return str(pieces)
N(QA, "Puzzle Hybrid", "hard",
  "What is the greatest number of pieces into which a round pizza can be cut with 4 straight cuts?",
  "एक गोल पिज़्ज़ा को 4 सीधे कटों से अधिक से अधिक कितने टुकड़ों में काटा जा सकता है?",
  ["8", "10", "11", "16"], 2,
  "Each new cut should cross all the earlier cuts at different points: the k-th cut then crosses k - 1 of them and adds k pieces. Starting from the 1 whole pizza, 4 cuts give 1 + 1 + 2 + 3 + 4 = 11 pieces. "
  "8 is what four cuts through the centre give (2 × 4); 16 doubles the pieces with every cut; 10 forgets to count the original pizza as one piece.",
  "हर नया कट पहले के सभी कटों को अलग-अलग बिंदुओं पर काटना चाहिए: तब k-वाँ कट उनमें से k - 1 को काटता है और k टुकड़े जोड़ता है। 1 पूरे पिज़्ज़ा से शुरू करके 4 कट 1 + 1 + 2 + 3 + 4 = 11 टुकड़े देते हैं। "
  "8 वह है जो केंद्र से होकर चार कट देते हैं (2 × 4); 16 हर कट के साथ टुकड़ों को दोगुना करता है; 10 मूल पिज़्ज़ा को एक टुकड़ा गिनना भूल जाता है।",
  "qa-ph-cutting-a-pizza-with-four-straight-cuts", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    sides = [F(k, 4) for k in range(1, 100)]
    s1 = {s * s for s in sides if 4 * s == 24}              # I: the perimeter is 24 cm
    s2 = {s * s for s in sides if 2 * s * s == 72}          # II: the diagonal is 6√2 cm, so 2 side² = 72
    both = s1 & s2
    assert s1 == {36} and s2 == {36} and both == {36}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the area of a square?",
   "एक वर्ग का क्षेत्रफल क्या है?",
   "Its perimeter is 24 cm.", "उसका परिमाप 24 सेमी है।",
   "Its diagonal is 6√2 cm.", "उसका विकर्ण 6√2 सेमी है।",
   1,
   "Statement I: the side is 24 ÷ 4 = 6 cm, so the area is 36 cm² -- sufficient. Statement II: the diagonal of a square is its side times √2, so the side is 6 cm and the area 36 cm² -- also sufficient. Either statement alone answers the question.",
   "कथन I: भुजा 24 ÷ 4 = 6 सेमी है, इसलिए क्षेत्रफल 36 वर्ग सेमी है -- पर्याप्त। कथन II: वर्ग का विकर्ण उसकी भुजा का √2 गुना होता है, इसलिए भुजा 6 सेमी और क्षेत्रफल 36 वर्ग सेमी है -- यह भी पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर दे देता है।",
   "qa-ds-the-area-of-a-square", _ds1)

def _ds2():
    marks = range(0, 101)
    s1 = {F(210 + x + y, 5) for x in marks for y in marks}               # I: three marks add up to 210; the other two are free
    s2 = {F(t + 130, 5) for t in range(0, 301)}                          # II: two marks add up to 130; the other three are free
    both = {F(210 + 130, 5)}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the average of the marks of 5 students?",
   "5 विद्यार्थियों के अंकों का औसत क्या है?",
   "The marks of three of them add up to 210.", "उनमें से तीन के अंकों का योग 210 है।",
   "The marks of the other two add up to 130.", "शेष दो के अंकों का योग 130 है।",
   2,
   "Statement I alone gives the total of only three students, and Statement II alone the total of only the other two. Together, the total of all five is 210 + 130 = 340, so the average is 340 ÷ 5 = 68. Both statements are needed.",
   "कथन I अकेला केवल तीन विद्यार्थियों का योग देता है, और कथन II अकेला केवल शेष दो का। दोनों साथ: पाँचों का कुल योग 210 + 130 = 340 है, इसलिए औसत 340 ÷ 5 = 68 है। दोनों कथन ज़रूरी हैं।",
   "qa-ds-the-average-of-five-marks", _ds2)
