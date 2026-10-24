# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 1 -- Logical Reasoning (15 items: 12 in the Reasoning slots, 3 in the data-sufficiency block).

Layout A, the 2023/2024 shape: a lighter Reasoning section. Exam-level mix (2 easy / 6 medium / 7 hard), with none of
the shapes of Levels 1-3: a source vouched for by itself, four cards and a rule; ranks in two subjects, six lockers in
two rows, men and women alternating in a row; what a relation does not fix about ages; a distance on a map; a code
that cannot be read back in one way, a sentence written backwards; a cube folded from a staircase net; a complementary
pair of conclusions; a contest in which only the winner lies; and in the data-sufficiency block students who study
two languages, a letter's number found two ways, and a car ruled out by a parking pass. Arrangement, relation, code,
cube, syllogism and truth-teller keys are found by checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a source vouched for by itself
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'This encyclopaedia can be trusted, because its articles are accurate; and we know its articles are accurate because the encyclopaedia itself states that every article is carefully checked.' Which one of the following best describes the flaw in this argument?",
  "'इस विश्वकोश पर भरोसा किया जा सकता है, क्योंकि इसके लेख सटीक हैं; और हम जानते हैं कि इसके लेख सटीक हैं क्योंकि विश्वकोश स्वयं कहता है कि हर लेख की सावधानी से जाँच की जाती है।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It relies on the source's own claim about itself to show that the source is reliable.",
   "It dismisses the encyclopaedia because of the character of the people who wrote it.",
   "It concludes that every article is accurate because most of the articles it checked were.",
   "It treats the encyclopaedia's great popularity with readers as proof of its accuracy."],
  ["यह स्रोत को विश्वसनीय दिखाने के लिए उसी के अपने बारे में किए दावे पर निर्भर है।",
   "यह विश्वकोश को उसके लेखकों के चरित्र के कारण ख़ारिज कर देता है।",
   "यह इस आधार पर कि जाँचे गए अधिकांश लेख सटीक थे, यह निष्कर्ष निकाल लेता है कि हर लेख सटीक है।",
   "यह पाठकों में विश्वकोश की भारी लोकप्रियता को उसकी सटीकता का प्रमाण मान लेता है।"],
  0,
  "The only evidence offered for the encyclopaedia's accuracy is what the encyclopaedia says about itself, and that statement is believable only if the encyclopaedia is already trusted. The argument goes round in a circle: it assumes the reliability it sets out to prove. "
  "It does not attack the writers -- it defends the book; it draws on no sample of checked articles; and it says nothing about popularity.",
  "विश्वकोश की सटीकता का एकमात्र प्रमाण वह है जो विश्वकोश अपने बारे में कहता है, और वह कथन तभी विश्वसनीय है जब विश्वकोश पर पहले से भरोसा हो। तर्क एक चक्र में घूमता है: वह वही विश्वसनीयता मान लेता है जिसे सिद्ध करने निकला है। "
  "वह लेखकों पर हमला नहीं करता -- वह पुस्तक का बचाव करता है; वह जाँचे गए लेखों का कोई नमूना नहीं लेता; और लोकप्रियता के बारे में कुछ नहीं कहता।",
  "lr-sc-a-source-vouched-for-by-itself", pos=0)

# 2 -- four cards and a rule
def _sc2():
    shown = {"E": "letter", "K": "letter", "4": "number", "7": "number"}
    vowel, even = lambda ch: ch in "AEIOU", lambda n: n % 2 == 0
    def breaks(letter, number):
        return vowel(letter) and not even(number)
    must = []
    for face, kind in shown.items():
        hidden = range(10) if kind == "letter" else "AEIKOUZ"
        if any(breaks(face, h) if kind == "letter" else breaks(h, int(face)) for h in hidden):
            must.append(face)
    assert must == ["E", "7"]
    return "E and 7"
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Each of four cards has a letter on one side and a number on the other. They lie on a table showing E, K, 4 and 7. Someone claims: 'If a card has a vowel on one side, it has an even number on the other side.' Which cards must be turned over to find out whether the claim is true for these four cards?",
  "चार कार्डों में से हर एक के एक ओर एक अक्षर और दूसरी ओर एक संख्या है। वे मेज़ पर E, K, 4 और 7 दिखाते हुए रखे हैं। कोई दावा करता है: 'यदि किसी कार्ड के एक ओर स्वर है, तो उसकी दूसरी ओर सम संख्या है।' इन चार कार्डों के लिए दावा सत्य है या नहीं, यह जानने के लिए किन कार्डों को पलटना आवश्यक है?",
  ["E and 7", "E only", "E and 4", "E, 4 and 7"], ["E और 7", "केवल E", "E और 4", "E, 4 और 7"],
  0,
  "The claim can be broken only by a card with a vowel on one side and an odd number on the other. E might have an odd number behind it, so it must be turned. 7 might have a vowel behind it, so it must be turned too. "
  "K is a consonant, and the claim says nothing about consonants; 4 is even, and an even number may have a vowel or a consonant behind it without breaking the claim. Turning 4 is the common mistake: the claim does not say that only vowels go with even numbers.",
  "दावा केवल ऐसे कार्ड से टूट सकता है जिसके एक ओर स्वर और दूसरी ओर विषम संख्या हो। E के पीछे विषम संख्या हो सकती है, इसलिए उसे पलटना आवश्यक है। 7 के पीछे स्वर हो सकता है, इसलिए उसे भी पलटना आवश्यक है। "
  "K व्यंजन है, और दावा व्यंजनों के बारे में कुछ नहीं कहता; 4 सम है, और सम संख्या के पीछे स्वर या व्यंजन कुछ भी हो, दावा नहीं टूटता। 4 को पलटना आम भूल है: दावा यह नहीं कहता कि सम संख्याओं के साथ केवल स्वर ही होते हैं।",
  "lr-sc-four-cards-and-a-rule", pos=3, check=_sc2)

# 3 -- ranks in two subjects
def _sa1():
    sols = []
    for m in permutations(range(1, 6)):
        M = dict(zip("PQRST", m))
        if (M["P"], M["Q"], M["T"]) != (1, 4, 5):
            continue
        for s in permutations(range(1, 6)):
            S = dict(zip("PQRST", s))
            if (S["P"], S["T"]) == (4, 2) and S["R"] == M["R"] and M["S"] < M["Q"] and S["S"] < S["Q"]:
                sols.append({k: M[k] + S[k] for k in M})
    assert len(sols) == 1
    order = sorted(sols[0], key=sols[0].get)
    assert [sols[0][k] for k in order] == [3, 5, 6, 7, 9]
    return order[1]
N(LR, "Seating Arrangement", "hard",
  "Five students, P, Q, R, S and T, were ranked 1 to 5 in Mathematics and again in Science, with no ties (1 is the best rank). P was first in Mathematics but fourth in Science. Q was fourth in Mathematics. T was last in Mathematics but second in Science. R had the same rank in both subjects, and S was ranked above Q in both. "
  "If the students are placed in order by the sum of their two ranks, the lowest sum first, who comes second?",
  "पाँच विद्यार्थियों, P, Q, R, S और T, को गणित में और फिर विज्ञान में 1 से 5 तक रैंक दी गई, बिना किसी बराबरी के (1 सबसे अच्छी रैंक है)। P गणित में पहला पर विज्ञान में चौथा था। Q गणित में चौथा था। T गणित में अंतिम पर विज्ञान में दूसरा था। R की दोनों विषयों में एक ही रैंक थी, और S दोनों में Q से ऊपर था। "
  "यदि विद्यार्थियों को उनकी दोनों रैंकों के योग के क्रम में रखा जाए, सबसे कम योग पहले, तो दूसरे स्थान पर कौन आता है?",
  ["P", "R", "S", "T"], 0,
  "In Mathematics P, Q and T hold ranks 1, 4 and 5, so R and S share 2 and 3. In Science P and T hold 4 and 2, so Q, R and S share 1, 3 and 5. R has the same rank in both, and the only rank open to R in both lists is 3; so R is third in both, and S is second in Mathematics. In Science S is above Q, so S is first and Q fifth. "
  "The sums are S 2 + 1 = 3, P 1 + 4 = 5, R 3 + 3 = 6, T 5 + 2 = 7 and Q 4 + 5 = 9. S comes first and P second. S is the answer to who comes first; R and T come third and fourth.",
  "गणित में P, Q और T की रैंक 1, 4 और 5 हैं, इसलिए R और S, 2 और 3 बाँटते हैं। विज्ञान में P और T की रैंक 4 और 2 हैं, इसलिए Q, R और S, 1, 3 और 5 बाँटते हैं। R की दोनों में एक ही रैंक है, और दोनों सूचियों में R के लिए खुली एकमात्र रैंक 3 है; इसलिए R दोनों में तीसरा है, और S गणित में दूसरा। विज्ञान में S, Q से ऊपर है, इसलिए S पहला और Q पाँचवाँ। "
  "योग हैं S 2 + 1 = 3, P 1 + 4 = 5, R 3 + 3 = 6, T 5 + 2 = 7 और Q 4 + 5 = 9। S पहले और P दूसरे स्थान पर है। S 'पहले कौन' का उत्तर है; R और T तीसरे और चौथे हैं।",
  "lr-sa-ranks-in-two-subjects", _sa1)

# 4 -- six lockers in two rows
def _sa2():
    pos = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2)}      # top row 1-3, bottom row 4-6
    sols = []
    for p in permutations(range(1, 7)):
        r = {k: pos[v] for k, v in zip("ABCDEF", p)}
        if (r["A"][0] == 0 and r["D"] == (1, r["A"][1]) and r["A"][1] != 0 and r["B"][0] == 1 and r["B"][1] != 1
                and r["C"][0] == 0 and abs(r["C"][1] - r["A"][1]) == 1 and r["F"][1] != 1
                and r["E"][0] == 1 and abs(r["E"][1] - r["B"][1]) == 1):
            sols.append(r)
    assert len(sols) == 1
    r = sols[0]
    return next(k for k, v in r.items() if v == (0, r["B"][1]))
N(LR, "Seating Arrangement", "medium",
  "Six lockers stand in two rows of three, one row on top of the other, and each of six people, A, B, C, D, E and F, has one locker. A's locker is in the top row, but not at its left end, and D's is directly below A's. C's locker is in the top row next to A's. B's locker is at one end of the bottom row, and E's is next to B's. F's locker is not in the middle column. Whose locker is directly above B's?",
  "छह लॉकर तीन-तीन की दो पंक्तियों में, एक पंक्ति दूसरी के ऊपर, खड़े हैं, और छह लोगों, A, B, C, D, E और F, में से हर एक का एक लॉकर है। A का लॉकर ऊपरी पंक्ति में है, पर उसके बाएँ छोर पर नहीं, और D का लॉकर ठीक A के नीचे है। C का लॉकर ऊपरी पंक्ति में A के बग़ल में है। B का लॉकर निचली पंक्ति के एक छोर पर है, और E का लॉकर B के बग़ल में है। F का लॉकर बीच वाले स्तंभ में नहीं है। B के लॉकर के ठीक ऊपर किसका लॉकर है?",
  ["C", "D", "E", "F"], 3,
  "B is at one end of the bottom row and E beside B, so B and E take two of the bottom places, and D takes the place below A. If A were in the middle column, D would be in the bottom middle, leaving no place beside B for E; so A is at the right end of the top row, D below A, and C in the top middle. "
  "Then B is at the left end of the bottom row and E in the bottom middle. F takes the last place, the top left, which is not in the middle column -- directly above B. C is above E, and D is in the bottom row.",
  "B निचली पंक्ति के एक छोर पर है और E, B के बग़ल में, इसलिए B और E नीचे के दो स्थान लेते हैं, और D, A के नीचे का स्थान। यदि A बीच वाले स्तंभ में होता, तो D नीचे बीच में होता, जिससे B के बग़ल में E के लिए कोई स्थान न बचता; इसलिए A ऊपरी पंक्ति के दाएँ छोर पर है, D उसके नीचे, और C ऊपर बीच में। "
  "तब B निचली पंक्ति के बाएँ छोर पर और E नीचे बीच में है। F अंतिम स्थान, ऊपर बाएँ, लेता है, जो बीच वाले स्तंभ में नहीं है -- ठीक B के ऊपर। C, E के ऊपर है, और D निचली पंक्ति में है।",
  "lr-sa-six-lockers-in-two-rows", _sa2)

# 5 -- men and women alternating in a row
def _sa3():
    rows = []
    for w in permutations("PQR"):
        for m in permutations("ABC"):
            row = [w[0], m[0], w[1], m[1], w[2], m[2]]
            i = {x: row.index(x) for x in row}
            if i["A"] == 5 and abs(i["Q"] - i["B"]) == 1 and abs(i["R"] - i["C"]) == 1 and abs(i["R"] - i["B"]) == 1:
                rows.append(row)
    third = {row[2] for row in rows}
    assert len(rows) == 2 and len(third) == 1
    return third.pop()
N(LR, "Seating Arrangement", "medium",
  "Three men, A, B and C, and three women, P, Q and R, sit in a row of six seats facing the same way. Men and women sit in alternate seats, and a woman sits at the left end. A sits at the right end. Q sits next to B, and R sits next to both B and C. Who sits in the third seat from the left?",
  "तीन पुरुष, A, B और C, और तीन महिलाएँ, P, Q और R, एक ही दिशा में मुँह किए छह सीटों की एक पंक्ति में बैठे हैं। पुरुष और महिलाएँ बारी-बारी की सीटों पर बैठे हैं, और बाएँ छोर पर एक महिला बैठी है। A दाएँ छोर पर बैठा है। Q, B के बग़ल में बैठी है, और R, B और C दोनों के बग़ल में बैठी है। बाएँ से तीसरी सीट पर कौन बैठा है?",
  ["P", "Q", "R", "C"], 2,
  "Women take seats 1, 3 and 5 and men seats 2, 4 and 6, with A in seat 6. R must sit between B and C, so R is in seat 3, between the men in seats 2 and 4 (seat 5 has A on one side). Q must sit next to B: if B is in seat 2, Q is in seat 1 and P in seat 5; if B is in seat 4, Q is in seat 5 and P in seat 1. "
  "So the row is either Q B R C P A or P C R B Q A. The arrangement is not fixed, but in both R is third from the left.",
  "महिलाएँ सीटें 1, 3 और 5 और पुरुष 2, 4 और 6 लेते हैं, A सीट 6 पर। R को B और C के बीच बैठना है, इसलिए R सीट 3 पर है, सीट 2 और 4 के पुरुषों के बीच (सीट 5 के एक ओर A है)। Q को B के बग़ल में बैठना है: यदि B सीट 2 पर है, तो Q सीट 1 पर और P सीट 5 पर; यदि B सीट 4 पर है, तो Q सीट 5 पर और P सीट 1 पर। "
  "अतः पंक्ति या तो Q B R C P A है या P C R B Q A। व्यवस्था तय नहीं है, पर दोनों में R बाएँ से तीसरी है।",
  "lr-sa-men-and-women-alternating-in-a-row", _sa3)

# 6 -- what a relation does not fix about ages
def _br1():
    # one family, years of birth: each parent at least 15 and at most 45 years older than each child
    fam = {"father's mother": 1960, "father": 1976, "father's younger brother": 2002, "mother": 1955, "person": 1999}
    ok = lambda par, ch: 15 <= fam[ch] - fam[par] <= 45
    assert ok("father's mother", "father") and ok("father's mother", "father's younger brother")
    assert ok("father", "person") and ok("mother", "person") and fam["father's younger brother"] > fam["father"]
    one = fam["father's younger brother"] > fam["person"]          # the uncle is younger than the person
    two = fam["father's mother"] > fam["mother"]                    # the grandmother is younger than the mother
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Blood Relation", "hard",
   "Which of the following is/are possible?",
   "निम्नलिखित में से कौन-सा/से संभव है/हैं?",
   ["A person's father's younger brother is younger than the person.",
    "A person's father's mother is younger than the person's mother."],
   ["किसी व्यक्ति का चाचा (पिता का छोटा भाई) उस व्यक्ति से छोटा है।",
    "किसी व्यक्ति की दादी (पिता की माँ) उस व्यक्ति की माँ से छोटी है।"],
   2,
   "Both are possible. 1: the father may be the eldest of a large family and his youngest brother born many years later -- for example a father born in 1976 with a brother born in 2002, and a child born in 1999. "
   "2: a person's mother may be much older than the father; if she was born in 1955, the father in 1976 and his mother in 1960, then the father's mother is five years younger than the person's mother. A relation fixes who descends from whom, not how far apart in age two people on different branches are.",
   "दोनों संभव हैं। 1: पिता किसी बड़े परिवार में सबसे बड़ा हो सकता है और उसका सबसे छोटा भाई बहुत वर्षों बाद जन्मा हो -- उदाहरण के लिए 1976 में जन्मे पिता, 2002 में जन्मा भाई, और 1999 में जन्मी संतान। "
   "2: किसी व्यक्ति की माँ पिता से बहुत बड़ी हो सकती है; यदि माँ 1955 में, पिता 1976 में और पिता की माँ 1960 में जन्मी, तो दादी उस व्यक्ति की माँ से पाँच वर्ष छोटी है। संबंध यह तय करता है कि कौन किसका वंशज है, यह नहीं कि अलग-अलग शाखाओं के दो लोगों की आयु में कितना अंतर है।",
   "lr-br-what-a-relation-does-not-fix-about-ages", check=_br1)

# 7 -- a distance on a map
def _dd1():
    km_per_cm = 250000 / 100000
    return f"{(6 ** 2 + 8 ** 2) ** 0.5 * km_per_cm:g} km"
N(LR, "Direction & Distance", "medium",
  "A map has a scale of 1 : 250,000. On it, town B is 6 cm due east of town A, and town C is 8 cm due north of town B. What is the actual straight-line distance between towns A and C?",
  "एक मानचित्र का पैमाना 1 : 250,000 है। उस पर नगर B, नगर A से 6 सेमी ठीक पूर्व में है, और नगर C, नगर B से 8 सेमी ठीक उत्तर में। नगर A और C के बीच वास्तविक सीधी दूरी क्या है?",
  ["20 km", "25 km", "35 km", "250 km"], 1,
  "On the map A, B and C form a right angle at B, so A to C is √(6² + 8²) = 10 cm. At 1 : 250,000, 1 cm stands for 250,000 cm = 2.5 km, so 10 cm is 25 km. "
  "35 km follows the two legs (14 cm) instead of the straight line; 250 km reads 1 cm as 25 km; 20 km reads it as 2 km.",
  "मानचित्र पर A, B और C, B पर समकोण बनाते हैं, इसलिए A से C, √(6² + 8²) = 10 सेमी है। 1 : 250,000 पर 1 सेमी, 250,000 सेमी = 2.5 किमी दर्शाता है, इसलिए 10 सेमी = 25 किमी। "
  "35 किमी सीधी रेखा के बजाय दोनों भुजाओं (14 सेमी) पर चलता है; 250 किमी, 1 सेमी को 25 किमी पढ़ लेता है; 20 किमी उसे 2 किमी।",
  "lr-dd-a-distance-on-a-map", _dd1,
  opts_hi=["20 किमी", "25 किमी", "35 किमी", "250 किमी"])

# 8 -- a code that cannot be read back in one way
def _cd1():
    def ways(s):
        if not s:
            return [""]
        out = []
        for k in (1, 2):
            if len(s) >= k and s[0] != "0" and 1 <= int(s[:k]) <= 26:
                out += [chr(64 + int(s[:k])) + rest for rest in ways(s[k:])]
        return out
    code = lambda w: "".join(str(ord(ch) - 64) for ch in w)
    assert code("CAB") == "312"
    found = ways("1225")
    assert sorted(found) == ["ABBE", "ABY", "AVE", "LBE", "LY"] and all(code(w) == "1225" for w in found)
    return str(len(found))
N(LR, "Coding-Decoding", "hard",
  "In a certain code, each letter of a word is replaced by its position in the alphabet (A = 1, B = 2, ..., Z = 26), and the numbers are written together without gaps; for example, CAB is written as 312. How many different strings of letters would be written as 1225 in this code?",
  "एक विशेष कूट में किसी शब्द के हर अक्षर को वर्णमाला में उसके स्थान (A = 1, B = 2, ..., Z = 26) से बदला जाता है, और संख्याएँ बिना अंतराल के साथ-साथ लिखी जाती हैं; उदाहरण के लिए, CAB को 312 लिखा जाता है। इस कूट में अक्षरों की कितनी अलग-अलग लड़ियाँ 1225 लिखी जाएँगी?",
  ["4", "5", "6", "8"], 1,
  "1225 can be cut into numbers from 1 to 26 in five ways: 1-2-2-5 (ABBE), 1-2-25 (ABY), 1-22-5 (AVE), 12-2-5 (LBE) and 12-25 (LY). Cuts such as 122-5 fail, because 122 is not a letter. "
  "So five strings give the same code -- which is why such a code cannot always be read back. 4 misses one of the splits; 6 and 8 count splits that use a number above 26.",
  "1225 को 1 से 26 तक की संख्याओं में पाँच तरीक़ों से तोड़ा जा सकता है: 1-2-2-5 (ABBE), 1-2-25 (ABY), 1-22-5 (AVE), 12-2-5 (LBE) और 12-25 (LY)। 122-5 जैसे विभाजन विफल होते हैं, क्योंकि 122 कोई अक्षर नहीं। "
  "अतः पाँच लड़ियाँ एक ही कूट देती हैं -- इसीलिए ऐसा कूट हमेशा वापस नहीं पढ़ा जा सकता। 4 एक विभाजन चूक जाता है; 6 और 8 ऐसे विभाजन गिनते हैं जिनमें 26 से बड़ी संख्या आती है।",
  "lr-cd-a-code-that-cannot-be-read-back-in-one-way", _cd1)

# 9 -- a sentence written backwards
def _cd2():
    code = lambda s: s[::-1]
    assert code("COME HOME NOW") == "WON EMOH EMOC"
    return code("GO TO WORK")
T(LR, "Coding-Decoding", "easy",
  "In a certain code, COME HOME NOW is written as WON EMOH EMOC. How is GO TO WORK written in that code?",
  "एक विशेष कूट में COME HOME NOW को WON EMOH EMOC लिखा जाता है। उस कूट में GO TO WORK को कैसे लिखा जाएगा?",
  ["KROW OT OG", "OG OT KROW", "WORK TO GO", "KROW TO GO"], ["KROW OT OG", "OG OT KROW", "WORK TO GO", "KROW TO GO"],
  0,
  "The whole sentence is written backwards, letter by letter: the order of the words is reversed and so is each word (NOW becomes WON and comes first). GO TO WORK therefore becomes KROW OT OG. "
  "OG OT KROW reverses each word but keeps their order; WORK TO GO reverses the order of the words but not the words themselves; KROW TO GO reverses only the last word.",
  "पूरा वाक्य अक्षर-दर-अक्षर उलटा लिखा जाता है: शब्दों का क्रम भी उलटता है और हर शब्द भी (NOW, WON बनकर पहले आता है)। इसलिए GO TO WORK बनता है KROW OT OG। "
  "OG OT KROW हर शब्द को उलटता है पर उनका क्रम रखता है; WORK TO GO शब्दों का क्रम उलटता है पर स्वयं शब्दों को नहीं; KROW TO GO केवल अंतिम शब्द को उलटता है।",
  "lr-cd-a-sentence-written-backwards", pos=0, check=_cd2)

# 10 -- a cube folded from a staircase net
def _cp1():
    net = {(0, 0): 1, (1, 0): 2, (1, 1): 3, (2, 1): 4, (2, 2): 5, (3, 2): 6}       # (column, row), rows counted downwards
    roll = {"E": ("bottom", "east", "top", "west"), "W": ("bottom", "west", "top", "east"),
            "S": ("bottom", "south", "top", "north"), "N": ("bottom", "north", "top", "south")}
    step = {"E": (1, 0), "W": (-1, 0), "S": (0, 1), "N": (0, -1)}
    face, seen = {}, set()
    def dfs(xy, o):
        seen.add(xy)
        face[o["bottom"]] = net[xy]
        for d, (dx, dy) in step.items():
            nxt = (xy[0] + dx, xy[1] + dy)
            if nxt in net and nxt not in seen:
                a, b, cc, e = roll[d]
                o2 = dict(o)
                o2[a], o2[b], o2[cc], o2[e] = o[b], o[cc], o[e], o[a]
                dfs(nxt, o2)
    dfs((0, 0), {k: k for k in ("bottom", "top", "north", "south", "east", "west")})
    assert len(face) == 6
    opp = {face["bottom"]: face["top"], face["top"]: face["bottom"], face["north"]: face["south"],
           face["south"]: face["north"], face["east"]: face["west"], face["west"]: face["east"]}
    assert opp[2] == 5 and opp[3] == 6
    return str(opp[1])
N(LR, "Cube Painting", "medium",
  "A cube is folded from a flat sheet of six squares numbered 1 to 6. Square 2 is to the right of square 1; square 3 is directly below square 2; square 4 is to the right of square 3; square 5 is directly below square 4; and square 6 is to the right of square 5, forming a staircase. When the sheet is folded into a cube, which number is on the face opposite 1?",
  "छह वर्गों वाली एक समतल शीट से, जिन पर 1 से 6 तक संख्याएँ हैं, एक घन मोड़ा जाता है। वर्ग 2, वर्ग 1 के दाईं ओर है; वर्ग 3, वर्ग 2 के ठीक नीचे है; वर्ग 4, वर्ग 3 के दाईं ओर है; वर्ग 5, वर्ग 4 के ठीक नीचे है; और वर्ग 6, वर्ग 5 के दाईं ओर है, जिससे एक सीढ़ी बनती है। शीट को घन में मोड़ने पर 1 के सामने वाले फलक पर कौन-सी संख्या है?",
  ["3", "4", "5", "6"], 1,
  "Imagine the cube resting on square 1 and rolling along the net: onto 2 (tipping right), down onto 3, right onto 4, down onto 5 and right onto 6. Each square becomes the face that touches it. Rolling right then down then right brings the face that started on top to the bottom exactly when the cube reaches square 4, so 1 and 4 are opposite. "
  "The same rolling pairs 2 with 5 and 3 with 6: in a staircase net each square is opposite the square three places further along. 3, 5 and 6 are all faces next to 1 on the cube; 6 is opposite 3.",
  "कल्पना कीजिए कि घन वर्ग 1 पर रखा है और जाल पर लुढ़कता है: 2 पर (दाईं ओर पलटकर), नीचे 3 पर, दाईं ओर 4 पर, नीचे 5 पर और दाईं ओर 6 पर। हर वर्ग वह फलक बनता है जो उसे छूता है। दाएँ, फिर नीचे, फिर दाएँ लुढ़कने से जो फलक आरंभ में ऊपर था वह ठीक तब नीचे आता है जब घन वर्ग 4 पर पहुँचता है, इसलिए 1 और 4 आमने-सामने हैं। "
  "इसी लुढ़कन से 2 का जोड़ा 5 के साथ और 3 का 6 के साथ बनता है: सीढ़ीनुमा जाल में हर वर्ग अपने से तीन स्थान आगे वाले वर्ग के सामने होता है। 3, 5 और 6 घन पर सभी 1 के पास वाले फलक हैं; 6, 3 के सामने है।",
  "lr-cp-a-cube-folded-from-a-staircase-net", _cp1)

# 11 -- a complementary pair of conclusions
def _sy1():
    regions = list(product((0, 1), repeat=3))          # (farmer, potter, weaver)
    one = two = True
    for mask in range(1, 1 << 8):
        world = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not any(p and q for p, q, e in world): continue          # some farmers are potters
        if any(q and e for p, q, e in world): continue              # no potter is a weaver
        one = one and any(p and e for p, q, e in world)
        two = two and not any(p and e for p, q, e in world)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "hard",
   "Statements: Some farmers are potters. No potter is a weaver.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ किसान कुम्हार हैं। कोई भी कुम्हार बुनकर नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some farmers are weavers.", "No farmer is a weaver."],
   ["कुछ किसान बुनकर हैं।", "कोई भी किसान बुनकर नहीं है।"],
   3,
   "Neither follows. The statements say that some farmers are potters and that those potters are not weavers, but they say nothing about the farmers who are not potters: some of them may be weavers, or none may be. So I need not be true and II need not be true. "
   "Exactly one of the two must be true, since they contradict each other -- but that does not make either one follow from the statements, and the code offers no 'either' choice.",
   "कोई भी नहीं निकलता। कथन कहते हैं कि कुछ किसान कुम्हार हैं और वे कुम्हार बुनकर नहीं हैं, पर उन किसानों के बारे में कुछ नहीं कहते जो कुम्हार नहीं हैं: उनमें से कुछ बुनकर हो सकते हैं, या कोई भी नहीं। इसलिए I का सत्य होना आवश्यक नहीं और II का भी नहीं। "
   "दोनों में से ठीक एक सत्य होना ही चाहिए, क्योंकि वे एक-दूसरे का खंडन करते हैं -- पर इससे दोनों में से कोई भी कथनों से निकलता नहीं, और कूट में 'या तो' का कोई विकल्प नहीं है।",
   "lr-sy-a-complementary-pair-of-conclusions", roman=True, check=_sy1)

# 12 -- a contest in which only the winner lies
def _tl1():
    says = {"A": lambda w, lies: w != "A", "B": lambda w, lies: w != "C",
            "C": lambda w, lies: w == "D", "D": lambda w, lies: lies["C"]}
    winners = []
    for w in "ABCD":
        lies = {p: p == w for p in "ABCD"}
        if all(says[p](w, lies) != lies[p] for p in "ABCD"):
            winners.append(w)
    assert winners == ["D"]
    return winners[0]
N(LR, "Truth-Liar", "hard",
  "Exactly one of four contestants, A, B, C and D, won a quiz. The winner lies and the other three tell the truth. A says, 'I did not win.' B says, 'C did not win.' C says, 'D won.' D says, 'C is lying.' Who won?",
  "चार प्रतियोगियों, A, B, C और D, में से ठीक एक ने एक प्रश्नोत्तरी जीती। विजेता झूठ बोलता है और बाक़ी तीन सच। A कहता है, 'मैं नहीं जीता।' B कहता है, 'C नहीं जीता।' C कहता है, 'D जीता।' D कहता है, 'C झूठ बोल रहा है।' कौन जीता?",
  ["A", "B", "C", "D"], 3,
  "Test each possible winner. If A won, A's 'I did not win' is a lie, as it should be, but C, telling the truth, says D won -- a contradiction. If B won, B's lie would mean C won -- a contradiction. If C won, B's true statement 'C did not win' would be false -- a contradiction. "
  "If D won, D's 'C is lying' is a lie, so C tells the truth, and C's 'D won' is indeed true; A and B are also telling the truth. Only D works. D's statement looks like an accusation, but it is the winner's lie.",
  "हर संभावित विजेता को जाँचिए। यदि A जीता, तो A का 'मैं नहीं जीता' झूठ है, जैसा होना चाहिए, पर सच बोलने वाला C कहता है कि D जीता -- विरोधाभास। यदि B जीता, तो B का झूठ यह अर्थ देता कि C जीता -- विरोधाभास। यदि C जीता, तो B का सच्चा कथन 'C नहीं जीता' ग़लत होता -- विरोधाभास। "
  "यदि D जीता, तो D का 'C झूठ बोल रहा है' झूठ है, इसलिए C सच बोलता है, और C का 'D जीता' वास्तव में सच है; A और B भी सच बोल रहे हैं। केवल D ठीक बैठता है। D का कथन आरोप जैसा लगता है, पर वह विजेता का झूठ है।",
  "lr-tl-a-contest-in-which-only-the-winner-lies", _tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    s1 = {b for b in range(0, 41) if 25 + 20 - b <= 40 and b <= 20}                # I alone: any overlap from 5 to 20
    s2 = {b for b in range(0, 41)}                                                  # II alone: no numbers
    both = {b for b in s1 if 25 + 20 - b == 40}
    assert min(s1) == 5 and both == {5}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "How many of the students in a class study both French and German?",
   "एक कक्षा के कितने विद्यार्थी फ़्रेंच और जर्मन दोनों पढ़ते हैं?",
   "Of the 40 students in the class, 25 study French and 20 study German.", "कक्षा के 40 विद्यार्थियों में से 25 फ़्रेंच पढ़ते हैं और 20 जर्मन।",
   "Every student in the class studies at least one of the two languages.", "कक्षा का हर विद्यार्थी दोनों में से कम से कम एक भाषा पढ़ता है।",
   2,
   "Statement I alone allows anything from 5 to 20 students studying both, depending on how many study neither. Statement II alone gives no numbers. Together, nobody studies neither, so 25 + 20 - (both) = 40 and exactly 5 study both. Both statements are needed.",
   "कथन I अकेला 5 से 20 तक किसी भी संख्या की अनुमति देता है, इस पर निर्भर कि कितने कोई भी भाषा नहीं पढ़ते। कथन II अकेला कोई संख्या नहीं देता। दोनों साथ: कोई भी ऐसा नहीं जो दोनों में से कुछ न पढ़ता हो, इसलिए 25 + 20 - (दोनों) = 40 और ठीक 5 दोनों पढ़ते हैं। दोनों कथन आवश्यक हैं।",
   "lr-ds-students-who-study-two-languages", _ds1)

def _ds2():
    s1 = {ord("G") - 64}                                    # I: A = 1, B = 2, and so on
    s2 = {int("4-15-7".split("-")[2])}                       # II: DOG is written 4-15-7, and G is its third letter
    assert s1 == s2 == {7}
    return _ds(s1, s2, s1 & s2)
DS(LR, "easy",
   "In a certain code each letter stands for a number. What number does G stand for?",
   "एक विशेष कूट में हर अक्षर किसी संख्या का प्रतीक है। G किस संख्या का प्रतीक है?",
   "A stands for 1, B for 2, and each later letter of the alphabet for one more than the letter before it.", "A, 1 का प्रतीक है, B, 2 का, और वर्णमाला का हर अगला अक्षर अपने पिछले अक्षर से एक अधिक का।",
   "The word DOG is written as 4-15-7.", "शब्द DOG को 4-15-7 लिखा जाता है।",
   1,
   "Statement I: G is the seventh letter, so it stands for 7 -- sufficient. Statement II: G is the third letter of DOG, so it stands for 7 -- also sufficient. Either statement alone answers the question.",
   "कथन I: G सातवाँ अक्षर है, इसलिए वह 7 का प्रतीक है -- पर्याप्त। कथन II: G, DOG का तीसरा अक्षर है, इसलिए वह 7 का प्रतीक है -- यह भी पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-letter-s-number-found-two-ways", _ds2)

def _ds3():
    worlds = [(car, pass_) for car in (True, False) for pass_ in (True, False)]
    s1 = {car for car, ps in worlds if (not car or ps) and not ps}          # I: car -> pass, and Arjun has no pass
    s2 = {car for car, ps in worlds}                                         # II: most residents own cars -- nothing about Arjun
    assert s1 == {False}
    return _ds(s1, s2, s1)
DS(LR, "hard",
   "Does Arjun own a car?",
   "क्या अर्जुन के पास कार है?",
   "In Arjun's building, everyone who owns a car has been given a parking pass, and Arjun has not been given one.",
   "अर्जुन की इमारत में जिसके भी पास कार है उसे पार्किंग पास दिया गया है, और अर्जुन को पास नहीं दिया गया।",
   "Most of the people in Arjun's building own cars.", "अर्जुन की इमारत के अधिकांश लोगों के पास कार है।",
   0,
   "Statement I: if Arjun owned a car he would have a pass; he has none, so he does not own a car -- a definite 'no', and so sufficient. Statement II describes most residents but says nothing that settles Arjun's case. One statement alone answers the question.",
   "कथन I: यदि अर्जुन के पास कार होती तो उसके पास पास होता; उसके पास नहीं है, इसलिए उसके पास कार नहीं है -- एक निश्चित 'नहीं', इसलिए पर्याप्त। कथन II अधिकांश निवासियों का वर्णन करता है पर ऐसा कुछ नहीं कहता जो अर्जुन का मामला तय करे। एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-car-ruled-out-by-a-parking-pass", _ds3)
