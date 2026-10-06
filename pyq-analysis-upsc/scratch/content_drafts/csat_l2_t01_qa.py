# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 1 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Mix (playbook B.2/B.7): number theory 8, speed-distance-time 4, ratio/mixtures/averages 5, percentage and
profit 3, sequences 2, counting 2, geometry 2, time and work 2, puzzle hybrids 4, data sufficiency 2.
Difficulty 3 easy / 19 medium / 12 hard. Options are in a fixed, natural order (ascending numbers); every
wrong option is a named slip (QD1-QD4), one item's key is "insufficient data" (QD4), and every key is
worked out in code by check()."""
import math
from fractions import Fraction as F
from itertools import permutations, combinations
import csat_common as c
from csat_common import N, S2, DS, QA

KMH, KMH_HI = " km/h", " किमी/घंटा"

# 1 -- number theory: inclusion-exclusion, "but not by both"
def _nt1():
    return str(sum(1 for n in range(1, 501) if (n % 6 == 0) != (n % 15 == 0)))
N(QA, "Number Theory", "medium",
  "How many integers from 1 to 500 are divisible by 6 or by 15, but not by both?",
  "1 से 500 तक के कितने पूर्णांक 6 से या 15 से विभाज्य हैं, परंतु दोनों से नहीं?",
  ["84", "100", "116", "132"], 0,
  "Multiples of 6: 83; of 15: 33; of both, that is of their LCM 30: 16. Divisible by at least one: 83 + 33 - 16 = 100. "
  "'Not by both' removes the 16 common ones once more: 100 - 16 = 84 (67 multiples of 6 only and 17 of 15 only). "
  "100 forgets the 'not by both' condition, 116 forgets to subtract the overlap, and 132 adds it instead of subtracting.",
  "6 के गुणज: 83; 15 के: 33; दोनों के, यानी उनके ल.स. 30 के: 16। कम से कम एक से विभाज्य: 83 + 33 - 16 = 100। "
  "'दोनों से नहीं' की शर्त उभयनिष्ठ 16 संख्याओं को एक बार और हटाती है: 100 - 16 = 84 (केवल 6 के 67 और केवल 15 के 17 गुणज)। "
  "100 'दोनों से नहीं' की शर्त भूल जाता है, 116 उभयनिष्ठ को घटाना भूल जाता है, और 132 उसे घटाने के बजाय जोड़ देता है।",
  "qa-nt-6-or-15-not-both", _nt1)

# 2 -- train overtaking a walker
N(QA, "Speed-Distance-Time", "medium",
  "A train 180 m long overtakes a man walking at 6 km/h in the same direction in 12 seconds. What is the speed of the train?",
  "180 मी लंबी एक रेलगाड़ी उसी दिशा में 6 किमी/घंटा की चाल से चल रहे एक व्यक्ति को 12 सेकंड में पार कर लेती है। रेलगाड़ी की चाल क्या है?",
  ["48" + KMH, "54" + KMH, "60" + KMH, "66" + KMH], 2,
  "To pass the man the train must cover its own length, 180 m, at the relative speed: 180 / 12 = 15 m/s = 15 × 18/5 = 54 km/h. "
  "Since both move the same way, the relative speed is the train's speed minus the man's, so the train runs at 54 + 6 = 60 km/h. "
  "54 forgets the man's motion; 48 subtracts his speed instead of adding it; 66 adds it twice.",
  "व्यक्ति को पार करने के लिए रेलगाड़ी को सापेक्ष चाल से अपनी लंबाई, 180 मी, तय करनी होती है: 180 / 12 = 15 मी/से = 15 × 18/5 = 54 किमी/घंटा। "
  "दोनों एक ही दिशा में चल रहे हैं, इसलिए सापेक्ष चाल = रेलगाड़ी की चाल - व्यक्ति की चाल; अतः रेलगाड़ी की चाल 54 + 6 = 60 किमी/घंटा है। "
  "54 व्यक्ति की गति भूल जाता है; 48 उसकी चाल जोड़ने के बजाय घटा देता है; 66 उसे दो बार जोड़ देता है।",
  "qa-sdt-train-overtakes-walker", lambda: f"{int(F(180, 12) * F(18, 5) + 6)}" + KMH, opts_hi=["48" + KMH_HI, "54" + KMH_HI, "60" + KMH_HI, "66" + KMH_HI])

# 3 -- remainder of a repunit-type number
N(QA, "Number Theory", "hard",
  "N is the 100-digit number 777...7, in which the digit 7 is written 100 times. What is the remainder when N is divided by 37?",
  "N एक 100 अंकों की संख्या 777...7 है, जिसमें अंक 7 सौ बार लिखा गया है। N को 37 से भाग देने पर शेषफल क्या होगा?",
  ["0", "3", "7", "30"], 2,
  "Since 999 = 27 × 37, 1000 leaves remainder 1 on division by 37, so a number has the same remainder as the sum of its three-digit groups taken from the right. "
  "N splits into 33 groups of 777 and a leading 7. Each 777 = 21 × 37 leaves 0, so N leaves the remainder of the single 7, which is 7. "
  "0 assumes that because 777 is divisible by 37, so is any string of 7s; 3 is the remainder of only the last two digits, 77; 30 is 37 - 7.",
  "चूँकि 999 = 27 × 37, इसलिए 1000 को 37 से भाग देने पर शेषफल 1 आता है; अतः किसी संख्या का शेषफल उसके दाईं ओर से बने तीन-तीन अंकों के समूहों के योग के शेषफल जितना होता है। "
  "N में 777 के 33 समूह और आगे एक 7 है। हर 777 = 21 × 37 का शेषफल 0 है, इसलिए N का शेषफल अकेले 7 का शेषफल, यानी 7, है। "
  "0 यह मान लेता है कि 777 के 37 से विभाज्य होने के कारण 7 की कोई भी लड़ी विभाज्य होगी; 3 केवल अंतिम दो अंकों 77 का शेषफल है; 30 = 37 - 7 है।",
  "qa-nt-hundred-sevens-mod-37", lambda: str(int("7" * 100) % 37))

# 4 -- alligation of two alloys
def _rm1():
    p, q, t = F(3, 4), F(1, 4), F(5, 8)
    r = (t - q) / (p - t)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Alloy P contains copper and zinc in the ratio 3 : 1, and alloy Q contains them in the ratio 1 : 3. In what ratio must P and Q be melted together to obtain an alloy with copper and zinc in the ratio 5 : 3?",
  "मिश्रधातु P में तांबा और जस्ता 3 : 1 के अनुपात में हैं, और मिश्रधातु Q में 1 : 3 के अनुपात में। तांबे और जस्ते का अनुपात 5 : 3 वाली मिश्रधातु पाने के लिए P और Q को किस अनुपात में मिलाना होगा?",
  ["1 : 3", "1 : 1", "2 : 1", "3 : 1"], 3,
  "Work with the share of copper: P has 3/4, Q has 1/4 and the mixture must have 5/8. By alligation, P : Q = (5/8 - 1/4) : (3/4 - 5/8) = 3/8 : 1/8 = 3 : 1. "
  "Check: 3 kg of P and 1 kg of Q give 9/4 + 1/4 = 10/4 kg copper out of 4 kg, that is 5/8. "
  "1 : 3 is the same ratio written the wrong way round; 1 : 1 would give copper at exactly half; 2 : 1 gives 7/12.",
  "तांबे के अंश से गणना कीजिए: P में 3/4, Q में 1/4 और मिश्रण में 5/8 होना चाहिए। एलिगेशन से P : Q = (5/8 - 1/4) : (3/4 - 5/8) = 3/8 : 1/8 = 3 : 1। "
  "जाँच: P के 3 किग्रा और Q के 1 किग्रा में 4 किग्रा में से 9/4 + 1/4 = 10/4 किग्रा तांबा है, यानी 5/8। "
  "1 : 3 वही अनुपात उलटा लिखा गया है; 1 : 1 से तांबा ठीक आधा होगा; 2 : 1 से 7/12 होगा।",
  "qa-rm-alloy-alligation", _rm1)

# 5 -- HCF / LCM pairs
def _nt3():
    pairs = {(x, y) for x in range(13, 361) for y in range(x, 361) if math.gcd(x, y) == 12 and x * y // 12 == 360}
    return str(len(pairs))
N(QA, "Number Theory", "medium",
  "The HCF of two numbers is 12 and their LCM is 360. If neither of the numbers is 12, how many such pairs of numbers are possible?",
  "दो संख्याओं का महत्तम समापवर्तक (HCF) 12 और लघुत्तम समापवर्त्य (LCM) 360 है। यदि इनमें से कोई भी संख्या 12 नहीं है, तो ऐसी कितनी संख्या-जोड़ियाँ संभव हैं?",
  ["3", "4", "6", "8"], 0,
  "Write the numbers as 12a and 12b with a and b co-prime. Then LCM = 12ab = 360, so ab = 30. The co-prime pairs with product 30 are (1, 30), (2, 15), (3, 10) and (5, 6). "
  "(1, 30) gives the numbers 12 and 360, which the condition excludes, leaving 3 pairs: 24 and 180, 36 and 120, 60 and 72. "
  "4 keeps the excluded pair; 6 counts the three pairs in both orders; 8 does both.",
  "संख्याओं को 12a और 12b लिखिए, जहाँ a और b सहअभाज्य हैं। तब LCM = 12ab = 360, अतः ab = 30। गुणनफल 30 वाली सहअभाज्य जोड़ियाँ (1, 30), (2, 15), (3, 10) और (5, 6) हैं। "
  "(1, 30) से संख्याएँ 12 और 360 बनती हैं, जिन्हें शर्त बाहर करती है; अतः 3 जोड़ियाँ बचती हैं: 24 और 180, 36 और 120, 60 और 72। "
  "4 बाहर की गई जोड़ी को भी गिनता है; 6 तीनों जोड़ियों को दोनों क्रमों में गिनता है; 8 दोनों गलतियाँ करता है।",
  "qa-nt-hcf-12-lcm-360-pairs", _nt3)

# 6 -- circular track, opposite directions
def _sdt2():
    return str(sum(1 for t in range(1, 450) if (4 * t + 6 * t) % 600 == 0))
N(QA, "Speed-Distance-Time", "hard",
  "A and B start together from the same point on a circular track 600 m long and run in opposite directions at 4 m/s and 6 m/s respectively. How many times do they meet, not counting the start, before A completes three rounds?",
  "A और B 600 मी लंबे एक वृत्ताकार पथ के एक ही बिंदु से एक साथ चलना शुरू करते हैं और विपरीत दिशाओं में क्रमशः 4 मी/से और 6 मी/से की चाल से दौड़ते हैं। आरंभ को छोड़कर, A के तीन चक्कर पूरे करने से पहले वे कितनी बार मिलते हैं?",
  ["1", "3", "7", "8"], 2,
  "A needs 3 × 600 / 4 = 450 s for three rounds. Running towards each other they close the gap at 4 + 6 = 10 m/s, so they meet every 600 / 10 = 60 s: at 60, 120, ..., 420 s. "
  "The next meeting would be at 480 s, after A has finished, so they meet 7 times. "
  "1 uses the difference of the speeds, as if they ran the same way; 3 confuses meetings with A's rounds; 8 counts the start or rounds 7.5 up.",
  "तीन चक्करों के लिए A को 3 × 600 / 4 = 450 सेकंड चाहिए। एक-दूसरे की ओर दौड़ते हुए वे 4 + 6 = 10 मी/से से दूरी घटाते हैं, इसलिए हर 600 / 10 = 60 सेकंड में मिलते हैं: 60, 120, ..., 420 सेकंड पर। "
  "अगली भेंट 480 सेकंड पर होती, जब A समाप्त कर चुका होगा; अतः वे 7 बार मिलते हैं। "
  "1 चालों का अंतर लेता है, मानो वे एक ही दिशा में दौड़ रहे हों; 3 भेंटों को A के चक्कर समझ लेता है; 8 आरंभ को गिनता है या 7.5 को ऊपर पूर्णांकित कर देता है।",
  "qa-sdt-circular-track-opposite", _sdt2)

# 7 -- three-digit numbers with digit sum 10
N(QA, "Number Theory", "hard",
  "How many three-digit numbers have digits that add up to 10?",
  "ऐसी कितनी तीन अंकों की संख्याएँ हैं जिनके अंकों का योग 10 है?",
  ["45", "54", "55", "63"], 1,
  "Let the digits be a, b, c with a from 1 to 9. Put a = a' + 1: then a' + b + c = 9 with every value from 0 to 9, which has C(11, 2) = 55 solutions; only a' = 9 (a = 10) is not a digit, "
  "and b or c cannot exceed 9 because the total is 9, so there are 55 - 1 = 54 numbers. "
  "55 forgets to remove a = 10; 63 lets the first digit be 0; 45 counts digit sum 9 instead of 10.",
  "अंक a, b, c मानिए, जहाँ a 1 से 9 तक है। a = a' + 1 रखिए: तब a' + b + c = 9, जिसके C(11, 2) = 55 हल हैं; इनमें केवल a' = 9 (यानी a = 10) अंक नहीं है, "
  "और कुल 9 होने से b या c 9 से बड़ा नहीं हो सकता, अतः 55 - 1 = 54 संख्याएँ हैं। "
  "55 में a = 10 को हटाना भूल गए हैं; 63 पहले अंक को 0 होने देता है; 45 अंकों का योग 10 के बजाय 9 लेकर गिनता है।",
  "qa-nt-three-digit-digit-sum-10", lambda: str(sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == 10)))

# 8 -- percentage error
N(QA, "Percentage & Profit-Loss", "medium",
  "A student was asked to multiply a number by 5/3 but divided it by 5/3 instead. By what percentage was his result less than the correct answer?",
  "एक विद्यार्थी को किसी संख्या को 5/3 से गुणा करने को कहा गया, पर उसने उसे 5/3 से भाग दे दिया। उसका परिणाम सही उत्तर से कितने प्रतिशत कम था?",
  ["36%", "40%", "60%", "64%"], 3,
  "For the number x, the correct answer is 5x/3 and his result is 3x/5. The shortfall is 5x/3 - 3x/5 = 16x/15, and as a share of the correct answer it is (16x/15) / (5x/3) = 16/25 = 64%. "
  "36% is his result as a share of the correct one (9/25), the opposite question; 40% and 60% compare 3/5 with 1 instead of with 5/3.",
  "संख्या x के लिए सही उत्तर 5x/3 है और उसका परिणाम 3x/5। कमी 5x/3 - 3x/5 = 16x/15 है, और सही उत्तर के अनुपात में यह (16x/15) / (5x/3) = 16/25 = 64% है। "
  "36% उसका परिणाम सही उत्तर के अनुपात में (9/25) है, जो उलटा प्रश्न है; 40% और 60% 3/5 की तुलना 5/3 के बजाय 1 से करते हैं।",
  "qa-pp-divide-instead-of-multiply", lambda: f"{int((F(5, 3) - F(3, 5)) / F(5, 3) * 100)}%")

# 9 -- smallest number with given remainders, divisible by 7
N(QA, "Number Theory", "medium",
  "What is the smallest positive number that leaves a remainder of 5 when divided by 6, by 8 or by 12, and is exactly divisible by 7?",
  "वह सबसे छोटी धनात्मक संख्या कौन-सी है जिसे 6, 8 या 12 से भाग देने पर शेषफल 5 बचता है और जो 7 से पूर्णतः विभाज्य है?",
  ["5", "29", "53", "77"], 3,
  "A number leaving remainder 5 on division by 6, 8 and 12 is 5 more than a multiple of their LCM, 24: 5, 29, 53, 77, 101, ... "
  "The first of these divisible by 7 is 77 = 7 × 11. The other options leave the right remainders but fail the test of 7: 5 = 7 × 0 + 5, 29 = 7 × 4 + 1, 53 = 7 × 7 + 4.",
  "6, 8 और 12 से भाग देने पर शेषफल 5 देने वाली संख्या इनके LCM 24 के किसी गुणज से 5 अधिक होती है: 5, 29, 53, 77, 101, ... "
  "इनमें 7 से विभाज्य पहली संख्या 77 = 7 × 11 है। अन्य विकल्प सही शेषफल देते हैं पर 7 की कसौटी पर विफल हैं: 5 = 7 × 0 + 5, 29 = 7 × 4 + 1, 53 = 7 × 7 + 4।",
  "qa-nt-remainder-5-divisible-7", lambda: str(next(n for n in range(1, 10 ** 4) if all(n % d == 5 for d in (6, 8, 12)) and n % 7 == 0)))

# 10 -- partnership with a mid-year change
def _rm5():
    a = 60000 * 4 + 40000 * 8
    b = 40000 * 4 + 60000 * 8
    return f"₹{54000 * a // (a + b):,}"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A and B start a business with ₹60,000 and ₹40,000. After 4 months, A withdraws ₹20,000 and B puts in ₹20,000 more. Out of a profit of ₹54,000 at the end of the year, what is A's share?",
  "A और B ₹60,000 और ₹40,000 लगाकर एक व्यवसाय शुरू करते हैं। 4 महीने बाद A ₹20,000 निकाल लेता है और B ₹20,000 और लगा देता है। वर्ष के अंत में ₹54,000 के लाभ में A का हिस्सा कितना है?",
  ["₹25,200", "₹27,000", "₹28,800", "₹32,400"], 0,
  "Shares follow capital × time. A: 60,000 × 4 + 40,000 × 8 = 5,60,000; B: 40,000 × 4 + 60,000 × 8 = 6,40,000. The ratio is 7 : 8, so A gets 54,000 × 7/15 = ₹25,200. "
  "₹27,000 splits the profit equally; ₹28,800 is B's share; ₹32,400 uses the opening capitals 3 : 2 and ignores the change.",
  "हिस्से पूँजी x समय के अनुपात में होते हैं। A: 60,000 × 4 + 40,000 × 8 = 5,60,000; B: 40,000 × 4 + 60,000 × 8 = 6,40,000। अनुपात 7 : 8 है, इसलिए A को 54,000 × 7/15 = ₹25,200 मिलते हैं। "
  "₹27,000 लाभ को बराबर बाँटता है; ₹28,800 B का हिस्सा है; ₹32,400 आरंभिक पूँजी 3 : 2 लेता है और बदलाव को अनदेखा करता है।",
  "qa-rm-partnership-mid-year", _rm5)

# 11 -- sequence: each term the sum of the two before
def _ss1():
    for a in range(-50, 51):
        b = 9 - a
        seq = [a, b]
        while len(seq) < 6:
            seq.append(seq[-1] + seq[-2])
        if seq[5] == 41:
            return str(a)
N(QA, "Sequences & Series", "medium",
  "In a sequence of numbers, every term after the second is the sum of the two terms just before it. If the third term is 9 and the sixth term is 41, what is the first term?",
  "संख्याओं के एक अनुक्रम में दूसरे पद के बाद हर पद अपने ठीक पहले के दो पदों का योग है। यदि तीसरा पद 9 और छठा पद 41 है, तो पहला पद क्या है?",
  ["1", "2", "3", "4"], 1,
  "Call the first two terms a and b. Then the terms are a, b, a + b, a + 2b, 2a + 3b and 3a + 5b. So a + b = 9 and 3a + 5b = 41; "
  "putting a = 9 - b gives 27 + 2b = 41, so b = 7 and a = 2. The sequence is 2, 7, 9, 16, 25, 41.",
  "पहले दो पद a और b मानिए। तब पद a, b, a + b, a + 2b, 2a + 3b और 3a + 5b हैं। अतः a + b = 9 और 3a + 5b = 41; "
  "a = 9 - b रखने पर 27 + 2b = 41, इसलिए b = 7 और a = 2। अनुक्रम 2, 7, 9, 16, 25, 41 है।",
  "qa-ss-two-term-sum-sequence", _ss1)

# 12 -- easy: percentage less
N(QA, "Percentage & Profit-Loss", "easy",
  "P's salary is 25% more than Q's. By what percentage is Q's salary less than P's?",
  "P का वेतन Q के वेतन से 25% अधिक है। Q का वेतन P के वेतन से कितने प्रतिशत कम है?",
  ["20%", "25%", "80%", "125%"], 0,
  "If Q earns 100, P earns 125. Q is 25 less than P, and as a share of P's salary that is 25/125 = 20%. "
  "25% measures the gap against Q's salary, answering the question in the stem rather than this one; 80% and 125% are the two salaries as percentages of each other.",
  "यदि Q 100 कमाता है, तो P 125 कमाता है। Q, P से 25 कम है, और P के वेतन के अनुपात में यह 25/125 = 20% है। "
  "25% अंतर को Q के वेतन से मापता है, जो प्रश्न में दी गई बात है, यह प्रश्न नहीं; 80% और 125% दोनों वेतनों को एक-दूसरे के प्रतिशत में बताते हैं।",
  "qa-pp-more-than-less-than", lambda: f"{int(F(25, 125) * 100)}%")

# 13 -- repeated dilution
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A vessel contains 40 litres of milk. 8 litres are drawn out and replaced with water, and this is done three times in all. How much milk is left in the vessel?",
  "एक बर्तन में 40 लीटर दूध है। उसमें से 8 लीटर निकालकर उतना ही पानी डाला जाता है, और कुल मिलाकर ऐसा तीन बार किया जाता है। बर्तन में कितना दूध बचता है?",
  ["16 litres", "20.48 litres", "25.6 litres", "32 litres"], 1,
  "Each draw removes 8/40 = 1/5 of whatever is in the vessel, so after each round 4/5 of the milk remains: 40 × (4/5)^3 = 40 × 64/125 = 20.48 litres. "
  "16 litres assumes 8 litres of pure milk leave every time (40 - 24); 32 and 25.6 are the amounts after one and two rounds.",
  "हर बार निकालने पर बर्तन में जो कुछ है उसका 8/40 = 1/5 भाग निकलता है, इसलिए हर चक्र के बाद दूध का 4/5 बचता है: 40 × (4/5)^3 = 40 × 64/125 = 20.48 लीटर। "
  "16 लीटर मानता है कि हर बार 8 लीटर शुद्ध दूध निकलता है (40 - 24); 32 और 25.6 एक और दो चक्रों के बाद की मात्राएँ हैं।",
  "qa-rm-repeated-dilution", lambda: f"{float(40 * F(4, 5) ** 3):g} litres",
  opts_hi=["16 लीटर", "20.48 लीटर", "25.6 लीटर", "32 लीटर"])

# 14 -- statement-based number theory
def _nt8():
    one = all((n ** 3 - n) % 6 == 0 for n in range(1, 3001))
    two = all((n ** 5 - n) % 30 == 0 for n in range(1, 3001))
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Number Theory", "hard",
  "For every positive integer n, which of the following statements is/are correct?",
  "प्रत्येक धनात्मक पूर्णांक n के लिए, निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
  ["n³ - n is divisible by 6.", "n⁵ - n is divisible by 30."],
  ["n³ - n, 6 से विभाज्य है।", "n⁵ - n, 30 से विभाज्य है।"], 2,
  "Both are correct. n³ - n = (n - 1) n (n + 1) is a product of three consecutive integers, so it contains a multiple of 2 and a multiple of 3. "
  "For II, n⁵ - n = n(n⁴ - 1) = (n - 1) n (n + 1)(n² + 1) is divisible by 2 and 3 for the same reason, and by 5 because a fifth power leaves the same remainder on division by 5 as the number itself "
  "(check n = 0 to 4: 0, 1, 32, 243, 1024 leave 0, 1, 2, 3, 4). Being divisible by 2, 3 and 5, it is divisible by 30. The trap is to accept I and suspect that 30 is too large for II.",
  "दोनों सही हैं। n³ - n = (n - 1) n (n + 1) तीन क्रमागत पूर्णांकों का गुणनफल है, इसलिए इसमें 2 का एक गुणज और 3 का एक गुणज होता है। "
  "II के लिए n⁵ - n = n(n⁴ - 1) = (n - 1) n (n + 1)(n² + 1) इसी कारण 2 और 3 से विभाज्य है, और 5 से भी, क्योंकि किसी संख्या की पाँचवीं घात 5 से भाग देने पर वही शेषफल देती है जो स्वयं संख्या "
  "(n = 0 से 4 तक जाँचिए: 0, 1, 32, 243, 1024 के शेषफल 0, 1, 2, 3, 4 हैं)। 2, 3 और 5 से विभाज्य होने के कारण यह 30 से विभाज्य है। जाल यह है कि I मान लिया जाए और II में 30 को बहुत बड़ा समझा जाए।",
  "qa-nt-n3-n5-divisibility", roman=True, check=_nt8, craft="inference")

# 15 -- boat and stream
N(QA, "Speed-Distance-Time", "medium",
  "A boat takes 3 hours to go 24 km upstream and 2 hours to come back the same distance downstream. How long would it take to cover 24 km in still water?",
  "एक नाव धारा के विरुद्ध 24 किमी जाने में 3 घंटे और उतनी ही दूरी धारा के साथ लौटने में 2 घंटे लेती है। शांत जल में 24 किमी तय करने में उसे कितना समय लगेगा?",
  ["2 h", "2 h 24 min", "2 h 30 min", "2 h 40 min"], 1,
  "Upstream speed = 24/3 = 8 km/h and downstream speed = 24/2 = 12 km/h. The speed in still water is their average, (8 + 12)/2 = 10 km/h, so 24 km takes 2.4 h = 2 h 24 min. "
  "2 h 30 min averages the times instead of the speeds; 2 h 40 min uses 9 km/h; 2 h is the downstream time.",
  "धारा के विरुद्ध चाल = 24/3 = 8 किमी/घंटा और धारा के साथ चाल = 24/2 = 12 किमी/घंटा। शांत जल में चाल इनका औसत, (8 + 12)/2 = 10 किमी/घंटा, है, इसलिए 24 किमी में 2.4 घंटे = 2 घंटे 24 मिनट लगते हैं। "
  "2 घंटे 30 मिनट चालों के बजाय समयों का औसत लेता है; 2 घंटे 40 मिनट 9 किमी/घंटा लेता है; 2 घंटे धारा के साथ का समय है।",
  "qa-sdt-boat-still-water", lambda: (lambda h: f"{int(h)} h {int(round((h - int(h)) * 60))} min")(24 / ((8 + 12) / 2)),
  opts_hi=["2 घंटे", "2 घंटे 24 मिनट", "2 घंटे 30 मिनट", "2 घंटे 40 मिनट"])

# 16 -- digit 7 written from 1 to 300
N(QA, "Number Theory", "medium",
  "How many times is the digit 7 written when all the integers from 1 to 300 are written down?",
  "1 से 300 तक के सभी पूर्णांक लिखने पर अंक 7 कुल कितनी बार लिखा जाता है?",
  ["30", "54", "57", "60"], 3,
  "Count by place. Units place: 7, 17, ..., 297, one in every ten numbers, 30 times. Tens place: 70-79, 170-179 and 270-279, 30 times. The hundreds place never shows 7 up to 300. Total 60. "
  "Numbers such as 77 contain the digit twice and must be counted twice. 57 counts numbers that contain a 7 rather than the digits written; 54 subtracts 77, 177 and 277 twice; 30 counts the units place only.",
  "स्थान के अनुसार गिनिए। इकाई का स्थान: 7, 17, ..., 297, हर दस संख्याओं में एक, 30 बार। दहाई का स्थान: 70-79, 170-179 और 270-279, 30 बार। 300 तक सैकड़े के स्थान पर 7 नहीं आता। कुल 60। "
  "77 जैसी संख्याओं में अंक दो बार है और उसे दो बार गिनना होगा। 57 लिखे गए अंकों के बजाय 7 वाली संख्याएँ गिनता है; 54, 77, 177 और 277 को दो बार घटा देता है; 30 केवल इकाई का स्थान गिनता है।",
  "qa-nt-digit-7-one-to-300", lambda: str(sum(str(n).count("7") for n in range(1, 301))))

# 17 -- easy average
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "The average weight of 25 students in a class is 42 kg. When the teacher's weight is included, the average rises by 1 kg. What is the teacher's weight?",
  "एक कक्षा के 25 विद्यार्थियों का औसत भार 42 किग्रा है। शिक्षक का भार जोड़ने पर औसत 1 किग्रा बढ़ जाता है। शिक्षक का भार कितना है?",
  ["43 kg", "67 kg", "68 kg", "69 kg"], 2,
  "Total for the students = 25 × 42 = 1,050 kg; total for all 26 = 26 × 43 = 1,118 kg; the teacher weighs 1,118 - 1,050 = 68 kg. "
  "Equivalently, the teacher brings the new average, 43, plus 1 kg for each of the 25 students: 43 + 25 = 68. 67 adds 25 to the old average; 69 adds 26 to the new one; 43 is the new average itself.",
  "विद्यार्थियों का कुल भार = 25 × 42 = 1,050 किग्रा; सभी 26 का कुल = 26 × 43 = 1,118 किग्रा; शिक्षक का भार 1,118 - 1,050 = 68 किग्रा है। "
  "इसी प्रकार, शिक्षक नया औसत 43 और 25 विद्यार्थियों में से हर एक के लिए 1 किग्रा लाता है: 43 + 25 = 68। 67 पुराने औसत में 25 जोड़ता है; 69 नए औसत में 26 जोड़ता है; 43 स्वयं नया औसत है।",
  "qa-rm-teacher-raises-average", lambda: f"{26 * 43 - 25 * 42} kg", opts_hi=["43 किग्रा", "67 किग्रा", "68 किग्रा", "69 किग्रा"])

# 18 -- arrangements with two letters together
def _pc1():
    return str(len({p for p in permutations("ARRANGE") if "RR" in "".join(p)}))
N(QA, "Permutation & Combination", "medium",
  "In how many different ways can the letters of the word ARRANGE be arranged so that the two R's are always together?",
  "शब्द ARRANGE के अक्षरों को कितने भिन्न तरीकों से व्यवस्थित किया जा सकता है कि दोनों R सदा साथ रहें?",
  ["180", "360", "720", "1260"], 1,
  "Tie the two R's into one block. That leaves six units -- RR, A, A, N, G, E -- with A repeated, so the number of arrangements is 6!/2! = 720/2 = 360. "
  "720 forgets that the two A's are alike; 180 also divides by 2! for the R's, which are already one block; 1260 = 7!/(2! x 2!) is the count with no condition.",
  "दोनों R को एक खंड मानिए। तब छह इकाइयाँ बचती हैं -- RR, A, A, N, G, E -- जिनमें A दोहराया गया है, अतः व्यवस्थाओं की संख्या 6!/2! = 720/2 = 360 है। "
  "720 भूल जाता है कि दोनों A समान हैं; 180, R के लिए भी 2! से भाग देता है, जो पहले ही एक खंड हैं; 1260 = 7!/(2! x 2!) बिना शर्त वाली संख्या है।",
  "qa-pc-arrange-rr-together", _pc1)

# 19 -- tank with an outlet closed midway
def _tw2():
    a, b, cc = F(1, 6), F(1, 9), F(1, 12)
    done = 2 * (a + b - cc)
    h = 2 + (1 - done) / (a + b)
    return f"{int(h)} h {int((h - int(h)) * 60)} min"
N(QA, "Time & Work", "hard",
  "Pipe A can fill a tank in 6 hours and pipe B in 9 hours, while pipe C can empty the full tank in 12 hours. All three are opened when the tank is empty, and C is closed after 2 hours. How long does it take in all to fill the tank?",
  "पाइप A एक टंकी को 6 घंटे में और पाइप B 9 घंटे में भर सकता है, जबकि पाइप C भरी टंकी को 12 घंटे में ख़ाली कर सकता है। ख़ाली टंकी पर तीनों पाइप खोले जाते हैं और 2 घंटे बाद C बंद कर दिया जाता है। टंकी भरने में कुल कितना समय लगता है?",
  ["3 h 36 min", "4 h 12 min", "5 h 9 min", "5 h 40 min"], 1,
  "In one hour the three together fill 1/6 + 1/9 - 1/12 = 7/36 of the tank, so 2 hours fill 14/36. The remaining 22/36 is filled by A and B at 1/6 + 1/9 = 10/36 an hour, taking 2.2 hours. "
  "Total = 4.2 hours = 4 h 12 min. 5 h 9 min keeps C open throughout (36/7 h); 3 h 36 min ignores C altogether; 5 h 40 min lets only A carry on after 2 hours.",
  "एक घंटे में तीनों मिलकर टंकी का 1/6 + 1/9 - 1/12 = 7/36 भाग भरते हैं, इसलिए 2 घंटे में 14/36। शेष 22/36 भाग A और B 1/6 + 1/9 = 10/36 प्रति घंटे की दर से 2.2 घंटे में भरते हैं। "
  "कुल = 4.2 घंटे = 4 घंटे 12 मिनट। 5 घंटे 9 मिनट C को पूरे समय खुला मानता है (36/7 घंटे); 3 घंटे 36 मिनट C को पूरी तरह अनदेखा करता है; 5 घंटे 40 मिनट 2 घंटे बाद केवल A को चालू मानता है।",
  "qa-tw-pipes-outlet-closed", _tw2, opts_hi=["3 घंटे 36 मिनट", "4 घंटे 12 मिनट", "5 घंटे 9 मिनट", "5 घंटे 40 मिनट"])

# 20 -- triangles with collinear points
def _pc2():
    return str(math.comb(10, 3) - math.comb(4, 3))
N(QA, "Permutation & Combination", "medium",
  "There are 10 points in a plane. Four of them lie on one straight line, and no three of the others, or of the others together with any of these four, are collinear. How many triangles can be formed with vertices at these points?",
  "एक समतल में 10 बिंदु हैं। उनमें से चार एक सरल रेखा पर हैं, और शेष में से, या शेष में से किन्हीं के साथ इन चार में से किसी के मिलने पर, कोई तीन बिंदु संरेख नहीं हैं। इन बिंदुओं को शीर्ष मानकर कितने त्रिभुज बनाए जा सकते हैं?",
  ["56", "80", "114", "116"], 3,
  "Any 3 of the 10 points give C(10, 3) = 120 choices, but the C(4, 3) = 4 choices taken entirely from the line give no triangle: 120 - 4 = 116. "
  "Counted by cases: 20 with no point on the line, 60 with one, 36 with two. 80 leaves out the triangles with two vertices on the line; 56 leaves out those with one; 114 subtracts C(4, 2) = 6 instead of C(4, 3).",
  "10 बिंदुओं में से कोई 3 चुनने के C(10, 3) = 120 तरीके हैं, पर पूरी तरह रेखा से लिए गए C(4, 3) = 4 चयन त्रिभुज नहीं बनाते: 120 - 4 = 116। "
  "स्थितियों से गिनें तो: रेखा पर कोई बिंदु नहीं वाले 20, एक वाले 60, दो वाले 36। 80 रेखा पर दो शीर्ष वाले त्रिभुज छोड़ देता है; 56 एक शीर्ष वाले छोड़ देता है; 114, C(4, 3) के बजाय C(4, 2) = 6 घटाता है।",
  "qa-pc-triangles-four-collinear", _pc2)

# 21 -- easy geometry: crossing paths
N(QA, "Geometry & Mensuration", "easy",
  "A rectangular field is 60 m long and 40 m wide. Two paths, each 5 m wide, run through the middle of it, one parallel to the length and the other parallel to the width. What is the total area of the paths?",
  "एक आयताकार मैदान 60 मी लंबा और 40 मी चौड़ा है। उसके बीच से 5-5 मी चौड़े दो रास्ते जाते हैं, एक लंबाई के समांतर और दूसरा चौड़ाई के समांतर। रास्तों का कुल क्षेत्रफल कितना है?",
  ["450 m²", "475 m²", "500 m²", "525 m²"], 1,
  "The path along the length covers 60 × 5 = 300 m² and the path along the width 40 × 5 = 200 m², but the 5 × 5 = 25 m² square where they cross is counted twice, so the area is 300 + 200 - 25 = 475 m². "
  "500 m² forgets the overlap; 450 m² removes it twice; 525 m² adds it.",
  "लंबाई के साथ वाला रास्ता 60 × 5 = 300 वर्ग मी और चौड़ाई के साथ वाला 40 × 5 = 200 वर्ग मी घेरता है, पर जहाँ वे काटते हैं वह 5 × 5 = 25 वर्ग मी का वर्ग दो बार गिना गया है, इसलिए क्षेत्रफल 300 + 200 - 25 = 475 वर्ग मी है। "
  "500 वर्ग मी अतिव्यापन भूल जाता है; 450 वर्ग मी उसे दो बार घटाता है; 525 वर्ग मी उसे जोड़ देता है।",
  "qa-gm-crossing-paths", lambda: f"{60 * 5 + 40 * 5 - 25} m²", opts_hi=["450 वर्ग मी", "475 वर्ग मी", "500 वर्ग मी", "525 वर्ग मी"])

# 22 -- false weight and discount
N(QA, "Percentage & Profit-Loss", "hard",
  "A trader marks his goods 40% above the cost price and allows a discount of 15% on the marked price. He also uses a weight of 900 g in place of 1 kg. What is his overall profit, correct to one decimal place?",
  "एक व्यापारी अपने माल पर क्रय मूल्य से 40% अधिक मूल्य अंकित करता है और अंकित मूल्य पर 15% छूट देता है। वह 1 किग्रा के स्थान पर 900 ग्राम का बाट भी प्रयोग करता है। उसका कुल लाभ, एक दशमलव स्थान तक, कितना है?",
  ["19.0%", "29.0%", "30.9%", "32.2%"], 3,
  "Let 1 kg cost ₹100. The customer pays 100 × 1.40 × 0.85 = ₹119 for what he believes is 1 kg, but receives only 900 g, which cost the trader ₹90. "
  "Profit = (119 - 90)/90 = 32.2%. 19.0% ignores the false weight; 29.0% simply adds 10 percentage points for it; 30.9% multiplies by 1.1 instead of dividing by 0.9.",
  "मान लीजिए 1 किग्रा का क्रय मूल्य ₹100 है। ग्राहक जिसे 1 किग्रा समझता है उसके लिए 100 × 1.40 × 0.85 = ₹119 देता है, पर उसे केवल 900 ग्राम मिलते हैं, जिनकी लागत व्यापारी को ₹90 है। "
  "लाभ = (119 - 90)/90 = 32.2%। 19.0% झूठे बाट को अनदेखा करता है; 29.0% उसके लिए केवल 10 प्रतिशत अंक जोड़ देता है; 30.9%, 0.9 से भाग देने के बजाय 1.1 से गुणा करता है।",
  "qa-pp-markup-discount-false-weight", lambda: f"{float((F(119) - 90) / 90 * 100):.1f}%")

# 23 -- minimum number of measures
def _ph1():
    jars = (1, 5, 20, 50)
    best = [0] + [10 ** 9] * 87
    for v in range(1, 88):
        best[v] = min(best[v - j] + 1 for j in jars if j <= v)
    return str(best[87])
N(QA, "Puzzle Hybrid", "hard",
  "Measuring jars of 1 litre, 5 litres, 20 litres and 50 litres are available. Water can only be drawn from a tank with them, never poured back. What is the minimum number of times the jars must be filled to draw exactly 87 litres?",
  "1 लीटर, 5 लीटर, 20 लीटर और 50 लीटर के मापने वाले जार उपलब्ध हैं। उनसे टंकी से केवल पानी निकाला जा सकता है, वापस नहीं डाला जा सकता। ठीक 87 लीटर निकालने के लिए जारों को कम से कम कितनी बार भरना होगा?",
  ["5", "6", "7", "8"], 2,
  "Since water can only be drawn, 87 must be a sum of jar sizes. 50 + 20 + 5 + 5 + 5 + 1 + 1 = 87 uses 7 fillings, and so does 20 × 4 + 5 + 1 + 1. "
  "Six fillings cannot make 87. With 50 and 20, the other 17 litres would have to come from four jars of 5 or 1, but 5a + b = 17 with a + b = 4 has no solution; with 50 and no 20, five small jars give at most 25; "
  "without the 50, four 20s leave 7 litres for two jars, which 5s and 1s cannot make, and three 20s leave 27 for three small jars, at most 15. "
  "5 and 6 forget that the last 17 litres need five small jars; 8 is one filling more than needed.",
  "चूँकि पानी केवल निकाला जा सकता है, 87 को जारों के आकारों का योग होना चाहिए। 50 + 20 + 5 + 5 + 5 + 1 + 1 = 87 में 7 बार भरना होता है, और 20 × 4 + 5 + 1 + 1 में भी। "
  "छह बार भरकर 87 नहीं बनता। 50 और 20 लेने पर शेष 17 लीटर 5 या 1 के चार जारों से आने चाहिए, पर a + b = 4 के साथ 5a + b = 17 का कोई हल नहीं है; 50 हो और 20 न हो तो पाँच छोटे जार अधिकतम 25 देते हैं; "
  "50 के बिना चार 20 लेने पर दो जारों के लिए 7 लीटर बचते हैं, जो 5 और 1 से नहीं बनते, और तीन 20 लेने पर तीन छोटे जारों के लिए 27 बचते हैं, जबकि वे अधिकतम 15 देते हैं। "
  "5 और 6 भूल जाते हैं कि अंतिम 17 लीटर के लिए पाँच छोटे जार चाहिए; 8 आवश्यकता से एक बार अधिक है।",
  "qa-ph-minimum-measures-87", _ph1)

# 24 -- rectangles in a grid
def _gm2():
    return str(sum(1 for x1, x2 in combinations(range(5), 2) for y1, y2 in combinations(range(4), 2)))
N(QA, "Geometry & Mensuration", "hard",
  "A board is divided into a grid of 3 rows and 4 columns of equal squares. How many rectangles of all sizes, squares included, can be traced along the grid lines?",
  "एक बोर्ड बराबर वर्गों की 3 पंक्तियों और 4 स्तंभों वाले ग्रिड में बँटा है। ग्रिड की रेखाओं पर सभी आकारों के कितने आयत, वर्गों सहित, बनाए जा सकते हैं?",
  ["12", "18", "20", "60"], 3,
  "A rectangle is fixed by choosing two of the 5 vertical lines and two of the 4 horizontal lines: C(5, 2) × C(4, 2) = 10 × 6 = 60. "
  "12 counts only the unit squares; 20 counts only the squares (12 + 6 + 2); 18 chooses from the rows and columns of squares, C(4, 2) × C(3, 2), instead of from the lines.",
  "आयत 5 ऊर्ध्वाधर रेखाओं में से दो और 4 क्षैतिज रेखाओं में से दो चुनकर तय होता है: C(5, 2) × C(4, 2) = 10 × 6 = 60। "
  "12 केवल इकाई वर्ग गिनता है; 20 केवल वर्ग गिनता है (12 + 6 + 2); 18 रेखाओं के बजाय वर्गों की पंक्तियों और स्तंभों में से चुनता है, C(4, 2) × C(3, 2)।",
  "qa-gm-rectangles-3-by-4", _gm2)

# 25 -- time and work, partner leaves
N(QA, "Time & Work", "medium",
  "A can do a piece of work in 12 days and B can do it in 18 days. They work together for 4 days, after which A leaves. In how many more days will B finish the work?",
  "A किसी काम को 12 दिनों में और B उसे 18 दिनों में कर सकता है। दोनों 4 दिन साथ काम करते हैं, जिसके बाद A चला जाता है। B शेष काम कितने और दिनों में पूरा करेगा?",
  ["8", "12", "14", "18"], 0,
  "Together they do 1/12 + 1/18 = 5/36 of the work a day, so in 4 days 20/36. B alone finishes the remaining 16/36 at 1/18 a day in 16/36 × 18 = 8 days. "
  "12 is the total time, 4 + 8, not the extra days; 14 subtracts the 4 days from B's 18 as if A had done nothing; 18 is B's time for the whole job.",
  "दोनों मिलकर प्रतिदिन काम का 1/12 + 1/18 = 5/36 भाग करते हैं, इसलिए 4 दिनों में 20/36। B अकेला शेष 16/36 भाग 1/18 प्रतिदिन की दर से 16/36 × 18 = 8 दिनों में पूरा करता है। "
  "12 कुल समय (4 + 8) है, अतिरिक्त दिन नहीं; 14, B के 18 दिनों में से 4 घटाता है, मानो A ने कुछ किया ही न हो; 18 पूरे काम के लिए B का समय है।",
  "qa-tw-partner-leaves", lambda: str(int((1 - 4 * (F(1, 12) + F(1, 18))) / F(1, 18))))

# 26 -- insufficient data (QD4)
def _ph5():
    sols = [p for p in range(1, 81) if (2400 - 30 * p) % 4 == 0 and (2400 - 30 * p) // 4 > 200]
    return "The question cannot be answered due to insufficient data" if len(sols) > 1 else str(sols[0])
N(QA, "Puzzle Hybrid", "medium",
  "A courier is paid ₹30 for each parcel delivered and ₹4 for every kilometre travelled. Last week he earned ₹2,400 and travelled more than 200 km, a whole number of kilometres. How many parcels did he deliver?",
  "एक कूरियर-कर्मी को हर पार्सल पहुँचाने के ₹30 और हर किलोमीटर चलने के ₹4 मिलते हैं। पिछले सप्ताह उसने ₹2,400 कमाए और 200 किमी से अधिक, पूरे किलोमीटरों में, यात्रा की। उसने कितने पार्सल पहुँचाए?",
  ["40", "50", "52", "The question cannot be answered due to insufficient data"], 3,
  "With p parcels and k km, 30p + 4k = 2,400 with k > 200, so 30p < 1,600 and p is at most 53; also 30p must leave a multiple of 4, so p is even. "
  "Many values fit: p = 52 with k = 210, p = 50 with k = 225, p = 40 with k = 300, and so on. Each listed number is possible but none is forced, so the data do not fix the answer. "
  "The trap is to stop at the first value that works.",
  "p पार्सल और k किमी के लिए 30p + 4k = 2,400, जहाँ k > 200; अतः 30p < 1,600 और p अधिकतम 53 है; साथ ही 2,400 - 30p को 4 का गुणज होना चाहिए, इसलिए p सम है। "
  "कई मान बैठते हैं: p = 52 और k = 210, p = 50 और k = 225, p = 40 और k = 300, आदि। सूची की हर संख्या संभव है पर कोई निश्चित नहीं, इसलिए आँकड़े उत्तर तय नहीं करते। "
  "जाल यह है कि पहला बैठने वाला मान मिलते ही रुक जाया जाए।",
  "qa-ph-courier-insufficient", _ph5,
  opts_hi=["40", "50", "52", "अपर्याप्त आँकड़ों के कारण प्रश्न का उत्तर नहीं दिया जा सकता"])

# 27 -- round trip at two speeds
def _sdt3():
    d = F(5) / (F(1, 12) + F(1, 18))
    return f"{int(d)} km"
N(QA, "Speed-Distance-Time", "medium",
  "A cyclist rides from P to Q at 12 km/h and returns along the same road at 18 km/h. If the whole round trip takes 5 hours, what is the distance from P to Q?",
  "एक साइकिल सवार P से Q तक 12 किमी/घंटा की चाल से जाता है और उसी सड़क से 18 किमी/घंटा की चाल से लौटता है। यदि पूरी आने-जाने की यात्रा में 5 घंटे लगते हैं, तो P से Q की दूरी कितनी है?",
  ["36 km", "37.5 km", "45 km", "72 km"], 0,
  "With distance d, d/12 + d/18 = 5, that is 5d/36 = 5, so d = 36 km. "
  "37.5 km takes the plain average of the speeds, 15 km/h, though the cyclist spends longer at the slower speed; 72 km is the round trip, not P to Q; 45 km is 18 × 2.5, as if each leg took half the time.",
  "दूरी d हो तो d/12 + d/18 = 5, यानी 5d/36 = 5, अतः d = 36 किमी। "
  "37.5 किमी चालों का साधारण औसत 15 किमी/घंटा लेता है, जबकि सवार धीमी चाल पर अधिक समय बिताता है; 72 किमी पूरी आने-जाने की दूरी है, P से Q नहीं; 45 किमी = 18 × 2.5, मानो हर ओर आधा समय लगा हो।",
  "qa-sdt-round-trip-two-speeds", _sdt3, opts_hi=["36 किमी", "37.5 किमी", "45 किमी", "72 किमी"])

# 28 -- ways to pay with each coin used
N(QA, "Puzzle Hybrid", "medium",
  "In how many ways can a sum of ₹20 be paid using coins of ₹1, ₹2 and ₹5 only, if at least one coin of each value must be used?",
  "केवल ₹1, ₹2 और ₹5 के सिक्कों से ₹20 का भुगतान कितने तरीकों से किया जा सकता है, यदि हर मूल्य का कम से कम एक सिक्का प्रयोग करना अनिवार्य हो?",
  ["11", "12", "13", "14"], 2,
  "Count by the number of ₹5 coins, c. c = 1 leaves ₹15 for ₹1 and ₹2 coins with at least one of each: ₹2 coins from 1 to 7, 7 ways. c = 2 leaves ₹10: 1 to 4 coins of ₹2, 4 ways. "
  "c = 3 leaves ₹5: 1 or 2 coins of ₹2, 2 ways. c = 4 leaves nothing, which breaks the condition. Total 7 + 4 + 2 = 13. 12 and 14 miss or add one boundary case.",
  "₹5 के सिक्कों की संख्या c के अनुसार गिनिए। c = 1 पर ₹1 और ₹2 के सिक्कों के लिए ₹15 बचते हैं, हर एक का कम से कम एक: ₹2 के सिक्के 1 से 7, 7 तरीके। c = 2 पर ₹10: ₹2 के 1 से 4 सिक्के, 4 तरीके। "
  "c = 3 पर ₹5: ₹2 के 1 या 2 सिक्के, 2 तरीके। c = 4 पर कुछ नहीं बचता, जो शर्त तोड़ता है। कुल 7 + 4 + 2 = 13। 12 और 14 किसी एक सीमा-स्थिति को छोड़ते या जोड़ते हैं।",
  "qa-ph-coins-each-value-used", lambda: str(sum(1 for a in range(1, 21) for b in range(1, 11) for cc in range(1, 5) if a + 2 * b + 5 * cc == 20)))

# 29 -- ages in ratios
def _rm4():
    for x in range(1, 100):
        if F(3 * x + 10, 4 * x + 10) == F(5, 6):
            return f"{3 * x + 5} years"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Five years ago the ages of A and B were in the ratio 3 : 4. Five years from now they will be in the ratio 5 : 6. What is A's present age?",
  "पाँच वर्ष पहले A और B की आयु का अनुपात 3 : 4 था। पाँच वर्ष बाद यह अनुपात 5 : 6 होगा। A की वर्तमान आयु क्या है?",
  ["5 years", "15 years", "20 years", "25 years"], 2,
  "Five years ago let the ages be 3x and 4x. Ten years later they are 3x + 10 and 4x + 10, and (3x + 10)/(4x + 10) = 5/6 gives 18x + 60 = 20x + 50, so x = 5. "
  "A was 15 five years ago and is 20 now; the ages will be 25 and 30 in five years, in the ratio 5 : 6. 5 is × itself; 15 and 25 are A's ages five years ago and five years ahead.",
  "पाँच वर्ष पहले आयु 3x और 4x मानिए। दस वर्ष बाद ये 3x + 10 और 4x + 10 होंगी, और (3x + 10)/(4x + 10) = 5/6 से 18x + 60 = 20x + 50, अतः x = 5। "
  "A पाँच वर्ष पहले 15 वर्ष का था और अब 20 वर्ष का है; पाँच वर्ष बाद आयु 25 और 30 होंगी, अनुपात 5 : 6। 5 स्वयं x है; 15 और 25, A की पाँच वर्ष पहले और पाँच वर्ष बाद की आयु हैं।",
  "qa-rm-ages-two-ratios", _rm4, opts_hi=["5 वर्ष", "15 वर्ष", "20 वर्ष", "25 वर्ष"])

# 30 -- clock that gains
def _ph3():
    real = F(720) * 60 / 64
    mins = int(real)
    hh, mm = 6 + mins // 60, mins % 60
    return f"{hh - 12 if hh > 12 else hh}:{mm:02d} p.m."
N(QA, "Puzzle Hybrid", "hard",
  "A clock gains 4 minutes in every hour of correct time. It is set right at 6:00 a.m. What is the correct time when this clock shows 6:00 p.m. the same day?",
  "एक घड़ी सही समय के हर घंटे में 4 मिनट आगे हो जाती है। उसे सुबह 6:00 बजे सही मिलाया जाता है। उसी दिन जब यह घड़ी शाम 6:00 बजे दिखाती है, तब सही समय क्या होता है?",
  ["5:12 p.m.", "5:15 p.m.", "6:45 p.m.", "6:48 p.m."], 1,
  "In 60 minutes of correct time the clock moves 64 minutes. It shows 12 hours, or 720 minutes, gone, so the correct time gone is 720 × 60/64 = 675 minutes = 11 h 15 min, and the correct time is 5:15 p.m. "
  "5:12 p.m. subtracts 12 × 4 = 48 minutes, though the clock's 12 hours are fewer than 12 correct hours; 6:45 and 6:48 p.m. move the wrong way: a fast clock is ahead of the correct time.",
  "सही समय के 60 मिनट में घड़ी 64 मिनट चलती है। यह 12 घंटे, यानी 720 मिनट, बीते दिखाती है, इसलिए सही बीता समय 720 × 60/64 = 675 मिनट = 11 घंटे 15 मिनट है, और सही समय शाम 5:15 है। "
  "5:12, 12 × 4 = 48 मिनट घटाता है, जबकि घड़ी के 12 घंटे सही 12 घंटों से कम हैं; 6:45 और 6:48 उलटी दिशा में जाते हैं: तेज़ घड़ी सही समय से आगे होती है।",
  "qa-ph-fast-clock-correct-time", _ph3, opts_hi=["शाम 5:12", "शाम 5:15", "शाम 6:45", "शाम 6:48"])

# 31 -- sum of products of consecutive numbers
N(QA, "Sequences & Series", "medium",
  "What is the value of 1 × 2 + 2 × 3 + 3 × 4 + ... + 20 × 21?",
  "1 × 2 + 2 × 3 + 3 × 4 + ... + 20 × 21 का मान क्या है?",
  ["2870", "3080", "3290", "4620"], 1,
  "Each term k(k + 1) = k² + k, so the sum is (1² + ... + 20²) + (1 + ... + 20) = 2,870 + 210 = 3,080; the formula n(n + 1)(n + 2)/3 = 20 × 21 × 22/3 gives the same. "
  "2870 is the sum of the squares alone; 3290 adds the 210 twice; 4620 divides by 2 instead of 3.",
  "हर पद k(k + 1) = k² + k है, इसलिए योग = (1² + ... + 20²) + (1 + ... + 20) = 2,870 + 210 = 3,080; सूत्र n(n + 1)(n + 2)/3 = 20 × 21 × 22/3 भी यही देता है। "
  "2870 केवल वर्गों का योग है; 3290, 210 को दो बार जोड़ता है; 4620, 3 के बजाय 2 से भाग देता है।",
  "qa-ss-sum-k-times-k-plus-1", lambda: str(sum(k * (k + 1) for k in range(1, 21))))

# 32 -- divisors that are perfect squares
def _nt7():
    return str(sum(1 for d in range(1, 721) if 720 % d == 0 and math.isqrt(d) ** 2 == d))
N(QA, "Number Theory", "medium",
  "How many of the positive divisors of 720 are perfect squares?",
  "720 के धनात्मक भाजकों में से कितने पूर्ण वर्ग हैं?",
  ["6", "9", "12", "30"], 0,
  "720 = 2⁴ × 3² × 5. A square divisor uses each prime to an even power: 2 to the power 0, 2 or 4 (three choices), 3 to the power 0 or 2 (two choices), and 5 to the power 0 only. "
  "So there are 3 × 2 × 1 = 6: 1, 4, 9, 16, 36 and 144. 30 is the number of all divisors (5 × 3 × 2); 9 allows 3 to any power; 12 allows the single 5.",
  "720 = 2⁴ × 3² × 5। वर्ग भाजक में हर अभाज्य सम घात में आता है: 2 की घात 0, 2 या 4 (तीन विकल्प), 3 की घात 0 या 2 (दो विकल्प), और 5 की घात केवल 0। "
  "अतः 3 × 2 × 1 = 6 हैं: 1, 4, 9, 16, 36 और 144। 30 सभी भाजकों की संख्या है (5 × 3 × 2); 9, 3 को किसी भी घात में लेने देता है; 12, अकेले 5 को लेने देता है।",
  "qa-nt-square-divisors-720", _nt7)

# ---- the data-sufficiency block's two Quant items
def _ds1():
    one = [n for n in range(10, 100) if sum(map(int, str(n))) == 9]
    two = [n for n in range(10, 100) if n - int(str(n)[::-1]) == 27]
    both = [n for n in one if n in two]
    alone = (len(one) == 1, len(two) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(both) == 1 else "d"
DS(QA, "medium",
   "What is the two-digit number N?",
   "दो अंकों की संख्या N क्या है?",
   "The sum of the digits of N is 9.", "N के अंकों का योग 9 है।",
   "When the digits of N are reversed, the number decreases by 27.", "N के अंकों को उलटने पर संख्या 27 घट जाती है।",
   2,
   "Statement I alone allows 18, 27, 36, ..., 90. Statement II alone says 9(a - b) = 27, so the tens digit exceeds the units digit by 3: 30, 41, 52, ..., 96 -- many numbers. "
   "Together, a + b = 9 and a - b = 3 give a = 6 and b = 3, so N = 63. Both statements are needed.",
   "कथन I अकेला 18, 27, 36, ..., 90 की अनुमति देता है। कथन II अकेला कहता है 9(a - b) = 27, यानी दहाई का अंक इकाई के अंक से 3 अधिक है: 30, 41, 52, ..., 96 -- कई संख्याएँ। "
   "दोनों साथ लेने पर a + b = 9 और a - b = 3 से a = 6 और b = 3, अतः N = 63। दोनों कथन आवश्यक हैं।",
   "qa-ds-two-digit-number", _ds1)

def _ds2():
    xs = range(1, 20001)
    s1 = [x for x in xs if x % 3 == 0 and (x * x) % 2 == 0]
    s2 = [x for x in xs if any(k * (k + 1) == x for k in range(1, 142))]
    ok1 = all(x % 6 == 0 for x in s1)
    ok2 = len({x % 6 == 0 for x in s2}) == 1
    return "b" if ok1 and ok2 else "a" if ok1 or ok2 else "c"
DS(QA, "hard",
   "Is the positive integer × divisible by 6?",
   "क्या धनात्मक पूर्णांक x, 6 से विभाज्य है?",
   "x is divisible by 3, and x² is even.", "x, 3 से विभाज्य है, और x² सम है।",
   "x is the product of two consecutive integers.", "x दो क्रमागत पूर्णांकों का गुणनफल है।",
   0,
   "Statement I: x² is even only if × is even, so × is divisible by both 2 and 3, hence by 6 -- sufficient. Statement II: a product of two consecutive integers is always even but need not be a multiple of 3: "
   "2 = 1 × 2 is not divisible by 6, while 6 = 2 × 3 is. So II alone cannot answer, and I alone can. The trap is to treat 'two consecutive' like 'three consecutive', whose product is always a multiple of 6.",
   "कथन I: x² तभी सम होता है जब x सम हो, इसलिए x, 2 और 3 दोनों से, अतः 6 से विभाज्य है -- पर्याप्त। कथन II: दो क्रमागत पूर्णांकों का गुणनफल सदा सम होता है पर 3 का गुणज होना ज़रूरी नहीं: "
   "2 = 1 × 2, 6 से विभाज्य नहीं है, जबकि 6 = 2 × 3 है। अतः II अकेला उत्तर नहीं दे सकता, और I अकेला दे सकता है। जाल यह है कि 'दो क्रमागत' को 'तीन क्रमागत' जैसा मान लिया जाए, जिनका गुणनफल सदा 6 का गुणज होता है।",
   "qa-ds-divisible-by-6", _ds2)
