# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 3 -- Logical Reasoning (9 items: 7 in the Reasoning slots, 2 in the data-sufficiency block).

The half paper's share of Level 2's Reasoning mix, rotated across the three minis (this one has two data-sufficiency
items, a syllogism and a truth-teller item, and one arrangement item), at the foundation level (3 easy / 5 medium /
1 hard). None of the shapes of Level 2, Mini 1 or Mini 2 is reused: which way a person facing you points with the right
arm; 'some kites are red, all red things are bright'; a father's sister's husband found through a grandparent; the one
clue that fixes a row; a code that moves each letter by its place in the word; the question to put to two guards, one
truthful and one lying; the point on which two speakers disagree; and, in the data-sufficiency block, the floor of a
building fixed by a prime number and the person in the middle seat. The rows are written in the order they take on
the paper; direction, syllogism, arrangement, code, truth-teller and data-sufficiency keys are found by checking every
case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _two(one, two):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 3 -- which way a person facing you points with the right arm
def _point():
    compass = ["North", "East", "South", "West"]
    asha = "South"
    bina = compass[(compass.index(asha) + 2) % 4]          # facing each other
    right = compass[(compass.index(bina) + 1) % 4]          # a quarter-turn clockwise from where one faces
    assert bina == "North" and compass[(compass.index(asha) + 1) % 4] == "West"
    return right
N(LR, "Direction & Distance", "easy",
  "Asha and Bina stand facing each other. Asha faces south. Bina stretches out the right arm and points sideways. In which direction is Bina pointing?",
  "आशा और बीना एक-दूसरे के आमने-सामने खड़ी हैं। आशा का मुख दक्षिण की ओर है। बीना अपना दायाँ हाथ फैलाकर बगल की ओर इशारा करती है। बीना किस दिशा में इशारा कर रही है?",
  ["North", "East", "South", "West"], 1,
  "Asha faces south, so Bina, who faces Asha, faces north. For a person facing north, the right hand is towards the east, so Bina points east. "
  "West would be Asha's right, not Bina's: two people facing each other have their right hands on opposite sides. North and south are the directions the two face, not sideways.",
  "आशा का मुख दक्षिण की ओर है, इसलिए आशा के सामने खड़ी बीना का मुख उत्तर की ओर है। उत्तर की ओर मुख वाले व्यक्ति का दायाँ हाथ पूर्व की ओर होता है, इसलिए बीना पूर्व की ओर इशारा करती है। "
  "पश्चिम आशा का दायाँ होगा, बीना का नहीं: आमने-सामने खड़े दो लोगों के दाएँ हाथ विपरीत ओर होते हैं। उत्तर और दक्षिण वे दिशाएँ हैं जिनकी ओर दोनों के मुख हैं, बगल की नहीं।",
  "lr-dd-which-way-a-person-facing-you-points", _point,
  opts_hi=["उत्तर", "पूर्व", "दक्षिण", "पश्चिम"])

# 9 -- 'some kites are red; all red things are bright'
def _syl():
    regions = list(product((0, 1), repeat=3))                # (kite, red, bright)
    follow = [True, True]
    for mask in range(1, 1 << 8):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not any(k and r for k, r, b in full):              # some kites are red
            continue
        if any(r and not b for k, r, b in full):              # all red things are bright
            continue
        follow[0] &= any(k and b for k, r, b in full)         # I. some kites are bright
        follow[1] &= any(b and k for k, r, b in full)         # II. some bright things are kites
    return _two(*follow)
S2(LR, "Syllogism", "easy",
   "Statements: Some kites are red. All red things are bright.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ पतंगें लाल हैं। सभी लाल वस्तुएँ चमकीली हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some kites are bright.", "Some bright things are kites."],
   ["कुछ पतंगें चमकीली हैं।", "कुछ चमकीली वस्तुएँ पतंगें हैं।"], 2,
   "The kites that are red are bright, because every red thing is bright -- so some kites are bright, and I follows. Those same red kites are bright things that are kites, so II follows as well; it says the same thing turned round. Both follow.",
   "जो पतंगें लाल हैं वे चमकीली हैं, क्योंकि हर लाल वस्तु चमकीली है -- इसलिए कुछ पतंगें चमकीली हैं, और I निकलता है। वही लाल पतंगें ऐसी चमकीली वस्तुएँ हैं जो पतंगें हैं, इसलिए II भी निकलता है; वह उसी बात को उलटकर कहता है। दोनों निकलते हैं।",
   "lr-sy-some-kites-are-red", roman=True, check=_syl)

# 15 -- a father's sister's husband found through a grandparent
_KEY_BR = "Father's sister's husband"
def _br():
    children_of_b = {"son": "F", "daughter": "C"}            # B's only son is A's father F; B's only daughter is C
    husband = {"C": "D"}
    father_of_a = children_of_b["son"]
    sister_of_father = children_of_b["daughter"]              # F and C are both B's children
    assert husband[sister_of_father] == "D" and father_of_a == "F"
    return _KEY_BR
T(LR, "Blood Relation", "medium",
  "A's father is the only son of B. C is the only daughter of B, and D is the husband of C. How is D related to A?",
  "A के पिता, B के इकलौते पुत्र हैं। C, B की इकलौती पुत्री है, और D, C का पति है। D का A से क्या संबंध है?",
  ["Mother's sister's husband", "Father's brother", "Mother's brother", _KEY_BR],
  ["मौसा", "चाचा", "मामा", "फूफा"], 3,
  "A's father and C are both children of B, so C is the sister of A's father -- A's father's sister. D, C's husband, is therefore A's father's sister's husband. "
  "He is not on the mother's side at all, so neither the mother's sister's husband nor the mother's brother fits; and he is not the father's brother, since B's only son is A's father himself.",
  "A के पिता और C दोनों B की संतानें हैं, इसलिए C, A के पिता की बहन -- A की बुआ -- है। अतः C का पति D, A का फूफा है। "
  "वह माँ की ओर से बिल्कुल नहीं है, इसलिए न मौसा ठीक बैठता है न मामा; और वह चाचा भी नहीं है, क्योंकि B का इकलौता पुत्र स्वयं A का पिता है।",
  "lr-br-a-father-s-sister-s-husband", pos=3, check=_br)

# 18 -- the one clue that fixes a row
_KEY_SA = "R sits next to S."
def _sa():
    sols = []
    for p in permutations("PQRST"):                          # index 0 is the left end; all face north
        d = {x: i for i, x in enumerate(p)}
        if d["P"] == 0 and d["Q"] - d["R"] == 1 and abs(d["S"] - d["P"]) > 1:
            sols.append(d)
    assert len(sols) == 4
    clue = {_KEY_SA: lambda d: abs(d["R"] - d["S"]) == 1,
            "T sits next to P.": lambda d: abs(d["T"] - d["P"]) == 1,
            "S sits at the right end.": lambda d: d["S"] == 4,
            "Q sits in the middle seat.": lambda d: d["Q"] == 2}
    fixes = [k for k, f in clue.items() if sum(1 for d in sols if f(d)) == 1]
    assert fixes == [_KEY_SA] and all(sum(1 for d in sols if f(d)) == 2 for k, f in clue.items() if k != _KEY_SA)
    return fixes[0]
T(LR, "Seating Arrangement", "hard",
  "Five friends -- P, Q, R, S and T -- sit in a row, all facing north. P sits at the left end. Q sits immediately to the right of R. S does not sit next to P. "
  "Which one of the following, if it were also known, would fix the seat of every one of the five friends?",
  "पाँच मित्र -- P, Q, R, S और T -- एक पंक्ति में उत्तर की ओर मुख करके बैठे हैं। P बाएँ सिरे पर है। Q, R के ठीक दाईं ओर है। S, P के बगल में नहीं है। "
  "निम्नलिखित में से कौन-सी बात, यदि वह भी ज्ञात हो, तो पाँचों मित्रों में से हर एक का स्थान तय कर देगी?",
  ["T sits next to P.", _KEY_SA, "S sits at the right end.", "Q sits in the middle seat."],
  ["T, P के बगल में है।", "R, S के बगल में है।", "S दाएँ सिरे पर है।", "Q बीच की सीट पर है।"], 1,
  "The three conditions allow exactly four rows (left to right): P R Q S T, P R Q T S, P T R Q S and P T S R Q. Only the last has R next to S, so that clue fixes every seat. "
  "Each of the others leaves two rows: T next to P allows P T R Q S and P T S R Q; S at the right end allows P R Q T S and P T R Q S; Q in the middle allows P R Q S T and P R Q T S.",
  "तीनों शर्तें ठीक चार पंक्तियाँ बनने देती हैं (बाएँ से दाएँ): P R Q S T, P R Q T S, P T R Q S और P T S R Q। केवल अंतिम में R, S के बगल में है, इसलिए यह बात हर स्थान तय कर देती है। "
  "बाक़ी में से हर एक दो पंक्तियाँ छोड़ देती है: T का P के बगल में होना P T R Q S और P T S R Q दोनों में सही है; S का दाएँ सिरे पर होना P R Q T S और P T R Q S में; Q का बीच में होना P R Q S T और P R Q T S में।",
  "lr-sa-the-one-clue-that-fixes-a-row", pos=1, check=_sa)

# 23 -- a code that moves each letter by its place in the word
def _code():
    ex = {"COAL": "DQDP", "FISH": "GKVL"}
    shift = lambda w, ks: "".join(chr((ord(ch) - 65 + k) % 26 + 65) for ch, k in zip(w, ks))
    fits = [ks for ks in product(range(26), repeat=4) if all(shift(w, ks) == v for w, v in ex.items())]
    assert fits == [(1, 2, 3, 4)]
    return shift("BIRD", fits[0])
T(LR, "Coding-Decoding", "medium",
  "In a certain code, COAL is written as DQDP and FISH is written as GKVL. How will BIRD be written in that code?",
  "एक निश्चित कूट भाषा में COAL को DQDP और FISH को GKVL लिखा जाता है। उसी कूट भाषा में BIRD को कैसे लिखा जाएगा?",
  ["CKUH", "CJSE", "CKUG", "DKUH"], ["CKUH", "CJSE", "CKUG", "DKUH"], 0,
  "Each letter moves forward by its place in the word: the first by 1, the second by 2, the third by 3 and the fourth by 4 (C → D, O → Q, A → D, L → P; F → G, I → K, S → V, H → L). "
  "So B → C, I → K, R → U and D → H: CKUH. CJSE moves every letter by 1; CKUG moves the last letter by 3 instead of 4; DKUH moves the first letter by 2 instead of 1.",
  "हर अक्षर शब्द में अपने स्थान जितना आगे बढ़ता है: पहला 1, दूसरा 2, तीसरा 3 और चौथा 4 (C → D, O → Q, A → D, L → P; F → G, I → K, S → V, H → L)। "
  "अतः B → C, I → K, R → U और D → H: CKUH। CJSE हर अक्षर को 1 बढ़ाता है; CKUG अंतिम अक्षर को 4 के बजाय 3 बढ़ाता है; DKUH पहले अक्षर को 1 के बजाय 2 बढ़ाता है।",
  "lr-cd-each-letter-moved-by-its-place", pos=0, check=_code)

# 32 -- the question to put to two guards
_KEY_TL = "Ask, 'Which door would the other guard say leads to freedom?', and take the other door."
def _guards():
    def answer(guard, question, safe):
        """The door a guard points to. guard is 'T' (always truthful) or 'L' (always lies); doors are 0 and 1."""
        other = "L" if guard == "T" else "T"
        lie = lambda d: 1 - d
        if question == "which":
            return safe if guard == "T" else lie(safe)
        if question == "you-would-say":
            said = safe if guard == "T" else lie(safe)              # what the guard would say
            return said if guard == "T" else lie(said)              # a liar misreports it
        if question == "other-would-say":
            said = answer(other, "which", safe)
            return said if guard == "T" else lie(said)
    sure = {}
    for q, take_other in (("which", False), ("you-would-say", True), ("other-would-say", True)):
        sure[q] = all((1 - answer(g, q, s) if take_other else answer(g, q, s)) == s for g in "TL" for s in (0, 1))
    # 'Are you the truthful guard?' -- both say yes, so taking that guard's own door is right only if it happens to be safe
    sure["are-you"] = all(own == s for own in (0, 1) for s in (0, 1))
    assert sure == {"which": False, "you-would-say": False, "other-would-say": True, "are-you": False}
    return _KEY_TL
T(LR, "Truth-Liar", "medium",
  "A room has two doors: one leads to freedom and the other to a trap. Each door has a guard. One guard always tells the truth and the other always lies, but you do not know which is which. "
  "You may ask one question of one guard. Which one of the following is sure to lead you to freedom?",
  "एक कमरे में दो दरवाज़े हैं: एक मुक्ति की ओर ले जाता है और दूसरा जाल की ओर। हर दरवाज़े पर एक पहरेदार है। एक पहरेदार सदा सच बोलता है और दूसरा सदा झूठ, पर आप नहीं जानते कि कौन कौन है। "
  "आप एक पहरेदार से एक प्रश्न पूछ सकते हैं। निम्नलिखित में से कौन-सा आपको निश्चित रूप से मुक्ति तक ले जाएगा?",
  ["Ask, 'Which door leads to freedom?', and take the door that the guard points to.",
   "Ask, 'Are you the guard who always tells the truth?', and if the answer is yes, take the door that this guard stands at.",
   "Ask, 'Which door would you say leads to freedom?', and take the other door.",
   _KEY_TL],
  ["पूछिए, 'कौन-सा दरवाज़ा मुक्ति की ओर ले जाता है?', और पहरेदार जिस दरवाज़े की ओर इशारा करे उसे लीजिए।",
   "पूछिए, 'क्या आप वह पहरेदार हैं जो सदा सच बोलता है?', और उत्तर हाँ हो, तो जिस दरवाज़े पर यह पहरेदार खड़ा है उसे लीजिए।",
   "पूछिए, 'आप किस दरवाज़े को मुक्ति वाला बताएँगे?', और दूसरा दरवाज़ा लीजिए।",
   "पूछिए, 'दूसरा पहरेदार किस दरवाज़े को मुक्ति वाला बताएगा?', और दूसरा दरवाज़ा लीजिए।"], 3,
  "Asked what the other guard would say, the truthful guard reports the liar's false answer truthfully, and the liar turns the truthful guard's right answer into a false one. Either way you are shown the trap, so taking the other door is always safe. "
  "Asking 'Which door leads to freedom?' works only if you happen to ask the truthful guard. Both guards answer 'yes' to 'Are you the truthful guard?', so that tells you nothing. "
  "Asked 'Which door would you say leads to freedom?', both guards point to the right door -- the liar misreports even the lie that would have been told -- so taking the other door leads into the trap.",
  "जब पूछा जाए कि दूसरा पहरेदार क्या कहेगा, तो सच्चा पहरेदार झूठे का ग़लत उत्तर सच्चाई से बता देता है, और झूठा, सच्चे के सही उत्तर को ग़लत बना देता है। दोनों ही स्थितियों में आपको जाल वाला दरवाज़ा दिखाया जाता है, इसलिए दूसरा दरवाज़ा लेना सदा सुरक्षित है। "
  "'कौन-सा दरवाज़ा मुक्ति की ओर ले जाता है?' पूछना तभी काम करता है जब संयोग से आप सच्चे पहरेदार से पूछें। 'क्या आप सच्चे पहरेदार हैं?' का उत्तर दोनों 'हाँ' देते हैं, इसलिए उससे कुछ पता नहीं चलता। "
  "'आप किस दरवाज़े को मुक्ति वाला बताएँगे?' पूछने पर दोनों पहरेदार सही दरवाज़े की ओर इशारा करते हैं -- झूठा अपने ही झूठ के बारे में झूठ बोलता है -- इसलिए दूसरा दरवाज़ा लेना जाल में ले जाता है।",
  "lr-tl-the-question-for-two-guards", pos=3, check=_guards)

# ---- the data-sufficiency block's two Reasoning items
def _ds1():
    floors = range(1, 11)
    isprime = lambda n: n > 1 and all(n % d for d in range(2, n))
    s1 = [f for f in floors if isprime(f) and f > 5]
    s2 = [f for f in floors if f % 2 == 1]
    both = [f for f in s1 if f in s2]
    assert s1 == [7]
    return _ds(s1, s2, both)
DS(LR, "easy",
   "The floors of a ten-storey building are numbered 1 to 10. On which floor does Asha live?",
   "दस मंज़िला इमारत की मंज़िलें 1 से 10 तक क्रमांकित हैं। आशा किस मंज़िल पर रहती है?",
   "The number of Asha's floor is a prime number greater than 5.",
   "आशा की मंज़िल की संख्या 5 से बड़ी एक अभाज्य संख्या है।",
   "Asha lives on an odd-numbered floor.",
   "आशा एक विषम संख्या वाली मंज़िल पर रहती है।",
   0,
   "Statement I: the only prime between 6 and 10 is 7, so Asha lives on the 7th floor -- sufficient. Statement II allows floors 1, 3, 5, 7 and 9 -- not sufficient. Statement I alone answers the question, but II alone does not.",
   "कथन I: 6 और 10 के बीच केवल 7 अभाज्य है, इसलिए आशा सातवीं मंज़िल पर रहती है -- पर्याप्त। कथन II मंज़िल 1, 3, 5, 7 और 9 होने देता है -- पर्याप्त नहीं। कथन I अकेले प्रश्न का उत्तर देता है, पर II अकेले नहीं।",
   "lr-ds-a-floor-fixed-by-a-prime", check=_ds1)

def _ds2():
    rows = ["".join(p) for p in permutations("ABCDE")]
    i = lambda r: {r[0], r[4]} == {"A", "B"}
    ii = lambda r: abs(r.index("C") - r.index("A")) == 1 and abs(r.index("D") - r.index("B")) == 1
    s1 = [r[2] for r in rows if i(r)]
    s2 = [r[2] for r in rows if ii(r)]
    both = [r[2] for r in rows if i(r) and ii(r)]
    assert set(both) == {"E"}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Five friends -- A, B, C, D and E -- sit in a row of five seats. Who sits in the middle seat?",
   "पाँच मित्र -- A, B, C, D और E -- पाँच सीटों की एक पंक्ति में बैठे हैं। बीच की सीट पर कौन बैठा है?",
   "A and B sit at the two ends of the row.",
   "A और B पंक्ति के दोनों सिरों पर बैठे हैं।",
   "C sits next to A, and D sits next to B.",
   "C, A के बगल में बैठा है, और D, B के बगल में।",
   2,
   "Statement I leaves C, D and E for the three middle seats in any order -- not sufficient. Statement II alone allows many rows, for example C A E B D or A C D B E -- not sufficient. "
   "Together: with A and B at the ends, C must take the seat beside A and D the seat beside B, which leaves the middle seat for E. Both statements together answer the question; neither does alone.",
   "कथन I बीच की तीन सीटें किसी भी क्रम में C, D और E के लिए छोड़ता है -- पर्याप्त नहीं। कथन II अकेले अनेक पंक्तियाँ होने देता है, जैसे C A E B D या A C D B E -- पर्याप्त नहीं। "
   "दोनों साथ: A और B सिरों पर हों, तो C को A के बगल की सीट और D को B के बगल की सीट लेनी होगी, जिससे बीच की सीट E के लिए बचती है। दोनों कथन साथ मिलकर उत्तर देते हैं; कोई भी अकेले नहीं।",
   "lr-ds-who-sits-in-the-middle-seat", check=_ds2)

# 39 -- the point on which two speakers disagree
_KEY_SC = "Whether the library is the main reason the children's reading scores rose"
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Asha: 'The new public library has made the town's children better readers -- their reading scores rose this year.'\n"
  "Bilal: 'The scores did rise, but mainly because the schools began a daily reading hour in the same year.'\n\n"
  "On which one of the following do Asha and Bilal disagree?",
  "आशा: 'नए सार्वजनिक पुस्तकालय ने कस्बे के बच्चों को बेहतर पाठक बना दिया है -- इस वर्ष उनके पठन अंक बढ़े।'\n"
  "बिलाल: 'अंक बढ़े तो हैं, पर मुख्य रूप से इसलिए कि उसी वर्ष विद्यालयों ने प्रतिदिन एक पठन-घंटा शुरू किया।'\n\n"
  "निम्नलिखित में से किस बात पर आशा और बिलाल असहमत हैं?",
  ["Whether the children's reading scores rose this year",
   _KEY_SC,
   "Whether the schools in the town began a daily reading hour for their pupils in the same year",
   "Whether public libraries are ever worth what they cost a town"],
  ["क्या इस वर्ष बच्चों के पठन अंक बढ़े",
   "क्या बच्चों के पठन अंक बढ़ने का मुख्य कारण पुस्तकालय है",
   "क्या कस्बे के विद्यालयों ने उसी वर्ष अपने विद्यार्थियों के लिए प्रतिदिन एक पठन-घंटा शुरू किया",
   "क्या सार्वजनिक पुस्तकालय कभी उस लागत के योग्य होते हैं जो कस्बा उन पर ख़र्च करता है"], 1,
  "Both accept that the scores rose -- Bilal says 'the scores did rise'. Asha credits the library; Bilal credits the reading hour. So they disagree on whether the library is the main reason for the rise. "
  "Asha says nothing about the reading hour, so there is no disagreement over whether it began; and neither speaker discusses whether libraries are worth their cost.",
  "दोनों मानते हैं कि अंक बढ़े -- बिलाल कहता है 'अंक बढ़े तो हैं'। आशा श्रेय पुस्तकालय को देती है; बिलाल पठन-घंटे को। अतः वे इस पर असहमत हैं कि वृद्धि का मुख्य कारण पुस्तकालय है या नहीं। "
  "आशा पठन-घंटे के बारे में कुछ नहीं कहती, इसलिए उसके शुरू होने पर कोई असहमति नहीं; और कोई भी वक्ता यह चर्चा नहीं करता कि पुस्तकालय अपनी लागत के योग्य हैं या नहीं।",
  "lr-sc-the-point-two-speakers-disagree-on", pos=1)
