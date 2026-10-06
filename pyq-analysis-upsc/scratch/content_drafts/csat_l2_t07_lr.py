# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 7 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Same mix as Tests 1-6 with new traps: an average that rises when a member leaves (what it forces about the member
and the club), an average read as if every household had gained, an argument that treats a necessary condition as a
sufficient one (and the valid arguments that look like it), a row in which some people face north and some south, a
queue counted from both ends, seven parking slots with one empty, a maternal uncle's wife, 'my son's father's
brother's sister', a spiral walk, a walk with right and left turns, a coded inequality that mixes strict and weak
signs, a cipher that moves each letter to the next letter of its own kind, the cubes of a 4 × 4 × 4 block that carry
both colours, three conclusions from a mango-fruit-stone chain, and three statements about the number of liars; in
the data-sufficiency block, handshakes, the nearer of two places and a father's age.
Difficulty 3 easy / 10 medium / 5 hard. Arrangement, code, cube, syllogism and truth-teller keys are found by
checking every case."""
import math
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, SC, DS, LR

def _two(one, two):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

CONC = "Which of the following conclusions follow(s) from the statement?"
CONC_HI = "निम्नलिखित में से कौन-सा/से निष्कर्ष कथन से निकलता/निकलते है/हैं?"

# 1 -- an average that rises when a member leaves
def _sc1():
    known = [(n, x) for n in range(2, 200) for x in range(1, 150) if 40 * n - x == 41 * (n - 1)]
    # n members averaged 40, so their ages sum to 40 n; the n - 1 who remain average 41; the one who left was x = 41 - n
    assert known == [(n, 41 - n) for n in range(2, 41)], known
    assert all(x < 40 for n, x in known) and all(n < 41 for n, x in known)      # I and II hold in every case (ages are at least 1)
    return _two(True, True)
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: When one member left a club, the average age of the remaining members rose from 40 years to 41 years.\n\n" + CONC,
   "कथन: जब एक सदस्य ने क्लब छोड़ा, तो शेष सदस्यों की औसत आयु 40 वर्ष से बढ़कर 41 वर्ष हो गई।\n\n" + CONC_HI,
   ["The member who left was younger than 40 years.", "The club had fewer than 41 members before the member left."],
   ["क्लब छोड़ने वाला सदस्य 40 वर्ष से कम आयु का था।", "सदस्य के क्लब छोड़ने से पहले क्लब में 41 से कम सदस्य थे।"], 2,
   "Let the club have n members, so their ages add up to 40n. After a member of age x leaves, the other n - 1 members average 41, so their ages add up to 41(n - 1). "
   "Hence x = 40n - 41(n - 1) = 41 - n. I: the remaining members must be at least one person, so n is at least 2 and x = 41 - n is less than 40 -- the member who left was younger than 40, as must be the case, since removing someone below the average raises the average. "
   "II: an age cannot be zero or negative, so 41 - n is greater than 0, which gives n less than 41: the club had fewer than 41 members. Both follow.",
   "मान लीजिए क्लब में n सदस्य हैं, इसलिए उनकी आयुओं का योग 40n है। आयु x वाले सदस्य के जाने के बाद शेष n - 1 सदस्यों की औसत आयु 41 है, इसलिए उनकी आयुओं का योग 41(n - 1) है। "
   "अतः x = 40n - 41(n - 1) = 41 - n। I: शेष सदस्यों में कम से कम एक व्यक्ति होना चाहिए, इसलिए n कम से कम 2 है और x = 41 - n, 40 से कम है -- जाने वाला सदस्य 40 वर्ष से छोटा था, जैसा होना ही था, क्योंकि औसत से कम वाले को हटाने पर औसत बढ़ता है। "
   "II: आयु शून्य या ऋणात्मक नहीं हो सकती, इसलिए 41 - n शून्य से बड़ा है, यानी n < 41: क्लब में 41 से कम सदस्य थे। दोनों निकलते हैं।",
   "lr-sc-an-average-that-rises-when-a-member-leaves", roman=True, check=_sc1)

# 2 -- a few large incomes carry the average
_KEY2 = "A few very rich households account for most of the rise, while most households' incomes have hardly changed."
def _sc2():
    n = 10
    before = [30000] * n
    carried = [30000] * (n - 1) + [30000 + 60000]                       # one household carries the whole rise in the average
    assert sum(carried) / n == 36000 and sum(a > b for a, b in zip(carried, before)) / n < 0.9    # 'almost every household' fails
    spread = [36000] * n                                                   # the same average with every household up
    assert sum(spread) / n == 36000 and all(a > b for a, b in zip(spread, before))
    return _KEY2
T(LR, "Statement-Conclusion/Assumption", "hard",
  "The average monthly income of households in a town rose from ₹30,000 to ₹36,000 over five years. The mayor concludes: 'Almost every household in the town now has a higher income in rupees than it had five years ago.' "
  "Which one of the following, if true, most weakens the mayor's conclusion?",
  "एक कस्बे में परिवारों की औसत मासिक आय पाँच वर्षों में ₹30,000 से बढ़कर ₹36,000 हो गई। महापौर निष्कर्ष निकालते हैं: 'कस्बे के लगभग हर परिवार की आय अब रुपयों में पाँच वर्ष पहले की आय से अधिक है।' "
  "निम्नलिखित में से कौन-सा कथन, यदि सत्य हो, महापौर के निष्कर्ष को सबसे अधिक कमज़ोर करता है?",
  [_KEY2,
   "The cost of living in the town has risen by about 20 per cent over the same five years, as it has in the rest of the State.",
   "The income of the middle household, the median, has also risen from ₹27,000 to ₹33,000 over the same five years.",
   "Several new schools and hospitals have opened in the town during the last five years, some of them run by the State."],
  ["वृद्धि का अधिकांश भाग कुछ बहुत अमीर परिवारों से आया है, जबकि अधिकतर परिवारों की आय में बहुत कम बदलाव आया है।",
   "इन्हीं पाँच वर्षों में कस्बे में रहन-सहन का ख़र्च लगभग 20 प्रतिशत बढ़ा है, जैसा राज्य के बाक़ी हिस्सों में भी हुआ है।",
   "इन्हीं पाँच वर्षों में बीच के परिवार की आय, यानी माध्यिका, भी ₹27,000 से बढ़कर ₹33,000 हो गई है।",
   "पिछले पाँच वर्षों में कस्बे में कई नए विद्यालय और अस्पताल खुले हैं, जिनमें से कुछ राज्य द्वारा चलाए जाते हैं।"], 0,
  "The mayor moves from a rise in the average to a rise for almost every household, but an average can rise because of a few very large incomes. If a few very rich households account for most of the rise while most incomes have hardly changed, "
  "the conclusion fails even though the average is exactly as stated -- this weakens it directly. A rise in the cost of living changes what an income buys, not whether a household's income in rupees went up, so it leaves the conclusion untouched. "
  "A median that has also risen supports the conclusion, and new schools and hospitals say nothing about incomes.",
  "महापौर औसत में वृद्धि से लगभग हर परिवार की वृद्धि तक पहुँच जाते हैं, पर औसत कुछ बहुत बड़ी आयों के कारण भी बढ़ सकता है। यदि कुछ बहुत अमीर परिवार वृद्धि के अधिकांश के लिए उत्तरदायी हों और अधिकतर परिवारों की आय में बहुत कम बदलाव आया हो, "
  "तो औसत ठीक वैसा रहते हुए भी निष्कर्ष टूट जाता है -- यह उसे सीधे कमज़ोर करता है। रहन-सहन का ख़र्च बढ़ना यह बदलता है कि आय से क्या ख़रीदा जा सकता है, यह नहीं कि परिवार की आय रुपयों में बढ़ी या नहीं, इसलिए निष्कर्ष अछूता रहता है। "
  "माध्यिका का भी बढ़ना निष्कर्ष का समर्थन करता है, और नए विद्यालय व अस्पताल आय के बारे में कुछ नहीं कहते।",
  "lr-sc-a-few-large-incomes-carry-the-average", pos=0, check=_sc2)

# 3 -- a necessary condition taken as a sufficient one
_KEY3 = "Only candidates who clear the written test are called for the interview. Mohan cleared the written test. Therefore, Mohan was called for the interview."
def _sc3():
    def valid(rule, fact, concl):
        """rule = (antecedent, consequent) read as 'antecedent -> consequent'; fact and concl are literals (variable, truth value)."""
        for a, b in product((True, False), repeat=2):                      # a: the first variable, b: the second
            env = {"A": a, "B": b}
            holds = lambda lit: env[lit[0]] == lit[1]
            if ((not holds(rule[0])) or holds(rule[1])) and holds(fact) and not holds(concl):
                return False
        return True
    # A = 'cleared the test' (signed by the assistant), B = 'called for interview' (bounced); 'Only A are B' is B -> A
    stem = (("B", True), ("A", True)), ("A", True), ("B", True)           # only signed cheques bounced; this one is signed; so it bounced
    assert not valid(*stem)
    options = {
        "called, so cleared": ((("B", True), ("A", True)), ("B", True), ("A", True)),
        "did not clear, so not called": ((("B", True), ("A", True)), ("A", False), ("B", False)),
        "cleared, so called": ((("B", True), ("A", True)), ("A", True), ("B", True)),
        "all, not called, so did not clear": ((("A", True), ("B", True)), ("B", False), ("A", False)),
    }
    bad = [k for k, v in options.items() if not valid(*v)]
    assert bad == ["cleared, so called"] and options["cleared, so called"] == stem
    return _KEY3
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Consider the argument: 'Only cheques signed by the manager's assistant bounced last month. This cheque was signed by the manager's assistant. Therefore, this cheque bounced last month.' "
  "Which one of the following arguments is flawed in the same way?",
  "निम्नलिखित तर्क पर विचार कीजिए: 'पिछले महीने केवल वही चेक बाउंस हुए जिन पर प्रबंधक के सहायक के हस्ताक्षर थे। इस चेक पर प्रबंधक के सहायक के हस्ताक्षर हैं। अतः यह चेक पिछले महीने बाउंस हुआ।' "
  "निम्नलिखित में से कौन-सा तर्क उसी प्रकार से त्रुटिपूर्ण है?",
  ["Only candidates who clear the written test are called for the interview. Mohan was called for the interview. Therefore, Mohan cleared the written test.",
   "Only candidates who clear the written test are called for the interview. Mohan did not clear the written test. Therefore, Mohan was not called for the interview.",
   "All candidates who clear the written test are called for the interview. Mohan was not called for the interview. Therefore, Mohan did not clear the written test.",
   _KEY3],
  ["केवल वही उम्मीदवार साक्षात्कार के लिए बुलाए जाते हैं जो लिखित परीक्षा पास करते हैं। मोहन साक्षात्कार के लिए बुलाया गया। अतः मोहन ने लिखित परीक्षा पास की।",
   "केवल वही उम्मीदवार साक्षात्कार के लिए बुलाए जाते हैं जो लिखित परीक्षा पास करते हैं। मोहन ने लिखित परीक्षा पास नहीं की। अतः मोहन साक्षात्कार के लिए नहीं बुलाया गया।",
   "लिखित परीक्षा पास करने वाले सभी उम्मीदवार साक्षात्कार के लिए बुलाए जाते हैं। मोहन साक्षात्कार के लिए नहीं बुलाया गया। अतः मोहन ने लिखित परीक्षा पास नहीं की।",
   "केवल वही उम्मीदवार साक्षात्कार के लिए बुलाए जाते हैं जो लिखित परीक्षा पास करते हैं। मोहन ने लिखित परीक्षा पास की। अतः मोहन साक्षात्कार के लिए बुलाया गया।"], 3,
  "The argument in the stem says that only cheques signed by the assistant bounced, and then reasons from 'signed by the assistant' to 'bounced': it treats a condition that bouncing requires as if it were enough to make a cheque bounce. "
  "The argument that goes from clearing the written test to being called for the interview does exactly this: clearing the test is required for a call, but nothing says that it is enough. "
  "The arguments that go from the call back to the test, or from failing the test to not being called, use the requirement the right way round, and so does the argument that goes from not being called to not having cleared the test when every candidate who clears is called.",
  "स्टेम का तर्क कहता है कि केवल सहायक के हस्ताक्षर वाले चेक बाउंस हुए, और फिर 'सहायक के हस्ताक्षर' से 'बाउंस' निकाल लेता है: वह उस शर्त को, जो बाउंस होने के लिए ज़रूरी है, चेक को बाउंस कराने के लिए काफ़ी मान लेता है। "
  "लिखित परीक्षा पास करने से साक्षात्कार के लिए बुलाए जाने तक पहुँचने वाला तर्क ठीक यही करता है: परीक्षा पास करना बुलावे के लिए ज़रूरी है, पर कहीं नहीं कहा गया कि वह काफ़ी है। "
  "जो तर्क बुलावे से परीक्षा की ओर, या परीक्षा में असफल होने से न बुलाए जाने की ओर, जाते हैं वे ज़रूरी शर्त को सही दिशा में लगाते हैं, और वैसा ही वह तर्क भी जो, जब परीक्षा पास करने वाला हर उम्मीदवार बुलाया जाता हो, न बुलाए जाने से परीक्षा पास न करने की ओर जाता है।",
  "lr-sc-a-necessary-condition-taken-as-enough", pos=3, check=_sc3)

# 4 -- a row in which some face north and some face south
def _sa1():
    def solutions(north):
        dirn = lambda w, side: (1 if side == "right" else -1) * (1 if w in north else -1)    # +1 = towards the east
        out = []
        for perm in permutations("ABCDEF"):
            pos = {p: i for i, p in enumerate(perm)}
            if (pos["F"] - pos["A"] == dirn("A", "right") and pos["A"] - pos["E"] == 3 * dirn("E", "left")
                    and pos["C"] - pos["B"] == dirn("B", "right") and pos["B"] - pos["D"] == 3 * dirn("D", "left")):
                out.append("".join(perm))
        return out
    sols = solutions(set("ACE"))
    assert sols == ["AFDECB"], sols
    assert solutions(set("ABCDEF")) == [] and solutions(set()) == []      # if everyone faced the same way, no arrangement would fit
    return sols[0][2]
T(LR, "Seating Arrangement", "hard",
  "Six people -- A, B, C, D, E and F -- stand in a line from west to east. A, C and E face north; B, D and F face south. Each statement below is read from the position, and in the facing direction, of the person named at its start. "
  "From A's position, F is immediately to the right. From E's position, A is third to the left. From B's position, C is immediately to the right. From D's position, B is third to the left. "
  "Who stands third from the west end?",
  "छह व्यक्ति -- A, B, C, D, E और F -- पश्चिम से पूर्व की ओर एक पंक्ति में खड़े हैं। A, C और E उत्तर की ओर मुँह किए हैं; B, D और F दक्षिण की ओर। नीचे दिया हर कथन उस व्यक्ति की स्थिति और उसके मुँह की दिशा से पढ़ा जाए जिसका नाम उसके आरंभ में है। "
  "A की स्थिति से, F ठीक दाईं ओर है। E की स्थिति से, A बाईं ओर तीसरा है। B की स्थिति से, C ठीक दाईं ओर है। D की स्थिति से, B बाईं ओर तीसरा है। "
  "पश्चिमी छोर से तीसरे स्थान पर कौन खड़ा है?",
  ["C", "D", "E", "F"], ["C", "D", "E", "F"], 1,
  "A person facing north has the east on the right and the west on the left; a person facing south has the west on the right and the east on the left. "
  "A faces north and F is immediately on A's right, so F is immediately east of A: A F. E faces north and A is third on E's left, so A is three places west of E: A F _ E with a gap in the third place. "
  "B faces south, so C, immediately on B's right, is immediately west of B: C B. D faces south, so B, third on D's left, is three places east of D: D _ C B with a gap in the second place. "
  "Each block fills four of the six places, so each can start in the first, second or third place; of the nine pairs of starting places only one keeps all six people apart: the first block in places 1 to 4 and the second in places 3 to 6. "
  "The gap in the first block is place 3 and D stands there, and the gap in the second block is place 4 and E stands there: the line is A F D E C B, so D stands third from the west. "
  "If everyone faced the same way, no arrangement would fit the four statements.",
  "उत्तर की ओर मुँह किए व्यक्ति के दाएँ पूर्व और बाएँ पश्चिम होता है; दक्षिण की ओर मुँह किए व्यक्ति के दाएँ पश्चिम और बाएँ पूर्व। "
  "A उत्तर की ओर मुँह किए है और F, A के ठीक दाएँ है, इसलिए F, A के ठीक पूर्व में है: A F। E उत्तर की ओर मुँह किए है और A, E के बाईं ओर तीसरा है, इसलिए A, E से तीन स्थान पश्चिम में है: A F _ E, तीसरे स्थान पर एक ख़ाली जगह के साथ। "
  "B दक्षिण की ओर मुँह किए है, इसलिए B के ठीक दाएँ C, B के ठीक पश्चिम में है: C B। D दक्षिण की ओर मुँह किए है, इसलिए D के बाईं ओर तीसरा B, D से तीन स्थान पूर्व में है: D _ C B, दूसरे स्थान पर एक ख़ाली जगह के साथ। "
  "हर खंड छह में से चार स्थान घेरता है, इसलिए हर खंड पहले, दूसरे या तीसरे स्थान से शुरू हो सकता है; शुरुआती स्थानों की नौ जोड़ियों में से केवल एक छहों व्यक्तियों को अलग रखती है: पहला खंड स्थान 1 से 4 में और दूसरा स्थान 3 से 6 में। "
  "पहले खंड की ख़ाली जगह स्थान 3 है और वहाँ D खड़ा है, और दूसरे खंड की ख़ाली जगह स्थान 4 है और वहाँ E खड़ा है: पंक्ति A F D E C B है, इसलिए D पश्चिम से तीसरे स्थान पर है। "
  "यदि सब एक ही ओर मुँह किए होते, तो चारों कथनों के अनुरूप कोई व्यवस्था नहीं बनती।",
  "lr-sa-a-row-facing-two-ways", pos=1, check=_sa1)

# 5 -- a queue counted from both ends
def _sa2():
    totals = [n for n in range(14, 80) if n - (7 + 5 + 1) + 1 == 9]        # Bala is 7 + 5 + 1 = 13th from the front and 9th from the back
    assert totals == [21], totals
    return str(totals[0])
N(LR, "Seating Arrangement", "easy",
  "In a queue, Anil is 7th from the front and Bala stands behind Anil, with 5 people between them. If Bala is 9th from the back, how many people are in the queue?",
  "एक कतार में अनिल आगे से 7वाँ है और बाला अनिल के पीछे खड़ा है, दोनों के बीच 5 व्यक्ति हैं। यदि बाला पीछे से 9वाँ है, तो कतार में कितने व्यक्ति हैं?",
  ["19", "20", "21", "22"], 2,
  "Anil is 7th from the front, and the 5 people between Anil and Bala take places 8 to 12, so Bala is 13th from the front. Bala is also 9th from the back, so the queue has 13 + 9 - 1 = 21 people -- Bala is counted in both numbers, so one is taken away. "
  "Another way: 7 people up to Anil, 5 between, and 9 from Bala to the back, 7 + 5 + 9 = 21. 22 counts Bala twice.",
  "अनिल आगे से 7वाँ है, और अनिल व बाला के बीच के 5 व्यक्ति स्थान 8 से 12 घेरते हैं, इसलिए बाला आगे से 13वाँ है। बाला पीछे से 9वाँ भी है, इसलिए कतार में 13 + 9 - 1 = 21 व्यक्ति हैं -- बाला दोनों संख्याओं में गिना गया है, इसलिए एक घटाया जाता है। "
  "दूसरा तरीक़ा: अनिल तक 7 व्यक्ति, बीच में 5, और बाला से पीछे तक 9, यानी 7 + 5 + 9 = 21। 22 में बाला दो बार गिना गया है।",
  "lr-sa-a-queue-counted-from-both-ends", _sa2)

# 6 -- seven parking slots, one empty
def _sa3():
    cars = ["red", "blue", "green", "white", "black", "grey"]
    sols = []
    for empty in range(1, 8):
        rest = [s for s in range(1, 8) if s != empty]
        for perm in permutations(cars):
            p = dict(zip(perm, rest))
            if (abs(p["grey"] - p["green"]) == 3 and abs(p["green"] - p["blue"]) == 3 and p["green"] < p["black"] < p["red"]
                    and abs(p["white"] - p["blue"]) == 1):
                sols.append((empty, p))
    assert len(sols) == 1, sols
    return str(sols[0][0])
T(LR, "Seating Arrangement", "hard",
  "Seven parking slots, numbered 1 to 7 from left to right, stand in a row. Six cars -- red, blue, green, white, black and grey -- are parked in six of the slots, and one slot is empty. "
  "'Two slots between' two cars means that exactly two slots, empty or occupied, lie between them. The grey car and the green car have two slots between them, and so do the green car and the blue car. "
  "The green car is to the left of the black car, which is to the left of the red car. The white car and the blue car are in neighbouring slots. Which slot is empty?",
  "सात पार्किंग स्थान, बाईं से दाईं ओर 1 से 7 तक क्रमांकित, एक पंक्ति में हैं। छह कारें -- लाल, नीली, हरी, सफ़ेद, काली और स्लेटी -- छह स्थानों में खड़ी हैं और एक स्थान ख़ाली है। "
  "दो कारों के 'बीच में दो स्थान' होने का अर्थ है कि उनके बीच ठीक दो स्थान, ख़ाली हों या भरे, हैं। स्लेटी और हरी कार के बीच दो स्थान हैं, और हरी और नीली कार के बीच भी। "
  "हरी कार काली कार के बाईं ओर है, जो लाल कार के बाईं ओर है। सफ़ेद और नीली कार पास-पास के स्थानों में हैं। कौन-सा स्थान ख़ाली है?",
  ["2", "3", "5", "6"], ["2", "3", "5", "6"], 1,
  "Two slots between two cars means that their slot numbers differ by 3. The grey car and the blue car are each 3 slots from the green car and are different cars, so one is 3 slots to the left of green and the other 3 slots to the right; "
  "that is possible only if green is in slot 4, with one of grey and blue in slot 1 and the other in slot 7. Black and red are to the right of green, so they take two of slots 5, 6 and 7, and slot 7 is held by grey or blue: black is in slot 5 and red in slot 6. "
  "The white car must be next to the blue car. If blue were in slot 7, its only neighbour, slot 6, would belong to red, so blue is in slot 1, grey in slot 7, and white in slot 2. "
  "The slots taken are 1, 2, 4, 5, 6 and 7, so slot 3 is empty.",
  "दो कारों के बीच दो स्थान होने का अर्थ है कि उनके स्थान-क्रमांकों का अंतर 3 है। स्लेटी और नीली कार हरी कार से 3-3 स्थान दूर हैं और अलग-अलग कारें हैं, इसलिए एक हरी से 3 स्थान बाएँ और दूसरी 3 स्थान दाएँ है; "
  "यह तभी संभव है जब हरी कार स्थान 4 में हो, और स्लेटी व नीली में से एक स्थान 1 में तथा दूसरी स्थान 7 में। काली और लाल कार हरी के दाईं ओर हैं, इसलिए वे स्थान 5, 6 और 7 में से दो लेती हैं, और स्थान 7 स्लेटी या नीली के पास है: काली स्थान 5 में और लाल स्थान 6 में। "
  "सफ़ेद कार नीली कार के पास होनी चाहिए। यदि नीली स्थान 7 में होती, तो उसका एकमात्र पड़ोसी, स्थान 6, लाल कार का होता, इसलिए नीली स्थान 1 में है, स्लेटी स्थान 7 में, और सफ़ेद स्थान 2 में। "
  "भरे स्थान 1, 2, 4, 5, 6 और 7 हैं, इसलिए स्थान 3 ख़ाली है।",
  "lr-sa-seven-parking-slots-one-empty", pos=1, check=_sa3)

# 7 -- a maternal uncle's wife
T(LR, "Blood Relation", "easy",
  "Pointing to a woman, Rohit says, 'Her husband is the only son of my mother's mother.' How is the woman related to Rohit?",
  "एक महिला की ओर इशारा करते हुए रोहित कहता है, 'इसका पति मेरी माँ की माँ का इकलौता बेटा है।' वह महिला रोहित की क्या लगती है?",
  ["His maternal uncle's wife",
   "His mother's sister, whether older or younger than his mother",
   "His brother's wife, that is, his sister-in-law",
   "His mother's mother, that is, his maternal grandmother"],
  ["उसके मामा की पत्नी, यानी मामी",
   "उसकी माँ की बहन, यानी मौसी, चाहे वह माँ से बड़ी हो या छोटी",
   "उसके भाई की पत्नी, यानी भाभी",
   "उसकी माँ की माँ, यानी नानी"], 0,
  "Rohit's mother's mother is his maternal grandmother, and her only son is Rohit's mother's brother, his maternal uncle (मामा). The woman is that man's wife, so she is the wife of Rohit's maternal uncle (मामी). "
  "A mother's sister (मौसी) is a daughter of the maternal grandmother, not the wife of her son; a brother's wife would be a sister-in-law (भाभी); and the maternal grandmother is the woman's mother-in-law, not the woman herself.",
  "रोहित की माँ की माँ उसकी नानी है, और उनका इकलौता बेटा रोहित की माँ का भाई, यानी उसका मामा, है। वह महिला उसी पुरुष की पत्नी है, इसलिए वह रोहित के मामा की पत्नी, यानी मामी, है। "
  "माँ की बहन (मौसी) नानी की बेटी होती है, उनके बेटे की पत्नी नहीं; भाई की पत्नी भाभी कहलाती; और नानी इस महिला की सास है, स्वयं यह महिला नहीं।",
  "lr-br-a-maternal-uncle-s-wife", pos=0)

# 8 -- my son's father's brother's sister
T(LR, "Blood Relation", "medium",
  "Looking at a girl, a man says, 'Her mother is the sister of my son's father's brother.' How is the man related to the girl?",
  "एक लड़की को देखकर एक पुरुष कहता है, 'इसकी माँ मेरे बेटे के पिता के भाई की बहन है।' वह पुरुष उस लड़की का क्या लगता है?",
  ["Father", "Paternal uncle", "Elder brother", "Maternal uncle"], ["पिता", "चाचा", "बड़ा भाई", "मामा"], 3,
  "The man's son's father is the man himself, so 'my son's father's brother' is the man's own brother, and the sister of that brother is the man's sister. "
  "The girl's mother is therefore the man's sister, which makes the man the brother of the girl's mother, her maternal uncle (मामा). A father would be the husband of her mother; a paternal uncle would be her father's brother; an elder brother would be a child of her own parents.",
  "पुरुष के बेटे का पिता वह स्वयं है, इसलिए 'मेरे बेटे के पिता का भाई' उसका अपना भाई है, और उस भाई की बहन उसकी अपनी बहन है। "
  "अतः लड़की की माँ पुरुष की बहन है, यानी पुरुष लड़की की माँ का भाई, उसका मामा, है। पिता लड़की की माँ का पति होता; चाचा उसके पिता का भाई होता; बड़ा भाई उसके अपने माता-पिता की संतान होता।",
  "lr-br-my-son-s-father-s-brother-s-sister", pos=3)

# 9 -- a spiral walk
def _dd1():
    step = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    x = y = 0
    for d, k in zip("NESWNE", range(1, 7)):
        x, y = x + step[d][0] * k, y + step[d][1] * k
    assert (x, y) == (4, 3) and x * x + y * y == 25 and abs(x) + abs(y) == 7
    return "5 km"
N(LR, "Direction & Distance", "easy",
  "A man starts from a point and walks 1 km north, then 2 km east, then 3 km south, then 4 km west, then 5 km north and finally 6 km east. How far is he from the starting point?",
  "एक आदमी एक बिंदु से चलना शुरू करता है और 1 किमी उत्तर, फिर 2 किमी पूर्व, फिर 3 किमी दक्षिण, फिर 4 किमी पश्चिम, फिर 5 किमी उत्तर और अंत में 6 किमी पूर्व चलता है। वह आरंभ बिंदु से कितनी दूर है?",
  ["5 km", "7 km", "9 km", "11 km"], 0,
  "Count east and north as positive. North-south: +1 - 3 + 5 = 3, so he is 3 km north of the start. East-west: +2 - 4 + 6 = 4, so he is 4 km east of the start. "
  "His distance is √(3² + 4²) = 5 km. 7 km adds the two components instead of using the right triangle.",
  "पूर्व और उत्तर को धनात्मक मानिए। उत्तर-दक्षिण: +1 - 3 + 5 = 3, इसलिए वह आरंभ बिंदु से 3 किमी उत्तर में है। पूर्व-पश्चिम: +2 - 4 + 6 = 4, इसलिए वह आरंभ बिंदु से 4 किमी पूर्व में है। "
  "उसकी दूरी √(3² + 4²) = 5 किमी है। 7 किमी दोनों घटकों को जोड़ देता है, समकोण त्रिभुज का प्रयोग नहीं करता।",
  "lr-dd-a-spiral-walk", opts_hi=["5 किमी", "7 किमी", "9 किमी", "11 किमी"], check=_dd1)

# 10 -- a walk with right and left turns
def _dd2():
    pos, head = (0, 0), (1, 0)                                    # he starts facing east
    right = lambda h: (h[1], -h[0])
    left = lambda h: (-h[1], h[0])
    for turn, k in ((None, 9), (right, 5), (right, 15), (left, 3)):
        if turn:
            head = turn(head)
        pos = (pos[0] + head[0] * k, pos[1] + head[1] * k)
    assert pos == (-6, -8) and pos[0] ** 2 + pos[1] ** 2 == 100 and abs(pos[0]) + abs(pos[1]) == 14
    return "10 km"
N(LR, "Direction & Distance", "medium",
  "A man walks 9 km east from his house. He turns right and walks 5 km, turns right again and walks 15 km, and then turns left and walks 3 km. How far is he now from his house?",
  "एक आदमी अपने घर से 9 किमी पूर्व की ओर चलता है। वह दाएँ मुड़कर 5 किमी चलता है, फिर दाएँ मुड़कर 15 किमी चलता है, और फिर बाएँ मुड़कर 3 किमी चलता है। अब वह अपने घर से कितनी दूर है?",
  ["6 km", "8 km", "10 km", "14 km"], 2,
  "Walking east, a right turn points him south; walking south, a right turn points him west; walking west, a left turn points him south. So the legs are 9 km east, 5 km south, 15 km west and 3 km south. "
  "East-west: 9 - 15 = 6 km west of the house. North-south: 5 + 3 = 8 km south of the house. His distance is √(6² + 8²) = 10 km. 14 km adds the two components instead of using the right triangle; 6 km and 8 km are single components.",
  "पूर्व की ओर चलते हुए दाएँ मुड़ने पर वह दक्षिण की ओर हो जाता है; दक्षिण की ओर चलते हुए दाएँ मुड़ने पर पश्चिम की ओर; पश्चिम की ओर चलते हुए बाएँ मुड़ने पर दक्षिण की ओर। इसलिए चरण हैं: 9 किमी पूर्व, 5 किमी दक्षिण, 15 किमी पश्चिम और 3 किमी दक्षिण। "
  "पूर्व-पश्चिम: 9 - 15 = घर से 6 किमी पश्चिम में। उत्तर-दक्षिण: 5 + 3 = घर से 8 किमी दक्षिण में। उसकी दूरी √(6² + 8²) = 10 किमी है। 14 किमी दोनों घटकों को जोड़ देता है, समकोण त्रिभुज का प्रयोग नहीं करता; 6 किमी और 8 किमी अकेले घटक हैं।",
  "lr-dd-a-walk-with-right-and-left-turns", opts_hi=["6 किमी", "8 किमी", "10 किमी", "14 किमी"], check=_dd2)

# 11 -- a coded inequality that mixes strict and weak signs
def _cd1():
    follows, seen = [True, True], 0
    for vals in product(range(6), repeat=5):
        v = dict(zip("MNOPQ", vals))
        if not (v["M"] > v["N"] >= v["O"] == v["P"] < v["Q"]):
            continue
        seen += 1
        follows[0] &= v["M"] > v["P"]
        follows[1] &= v["N"] > v["P"]
    assert seen and follows == [True, False]
    return _two(*follows)
S2(LR, "Coding-Decoding", "medium",
   "In a certain code, 'A # B' means 'A is greater than B'; 'A @ B' means 'A is greater than or equal to B'; 'A $ B' means 'A is equal to B'; and 'A & B' means 'A is less than B'.\n\n"
   "Statement: M # N @ O $ P & Q\n\n" + CONC,
   "एक निश्चित कूट में 'A # B' का अर्थ है 'A, B से बड़ा है'; 'A @ B' का अर्थ है 'A, B से बड़ा या उसके बराबर है'; 'A $ B' का अर्थ है 'A, B के बराबर है'; और 'A & B' का अर्थ है 'A, B से छोटा है'।\n\n"
   "कथन: M # N @ O $ P & Q\n\n" + CONC_HI,
   ["M # P", "N # P"], ["M # P", "N # P"], 0,
   "Decoding the statement gives M > N ≥ O = P < Q. I: M > N ≥ O and O = P, so M > P, which is M # P -- it follows. "
   "II: N ≥ O = P gives only N ≥ P, so 'N is greater than P' (N # P) need not hold: N could be equal to P. Only I follows.",
   "कथन को खोलने पर M > N ≥ O = P < Q मिलता है। I: M > N ≥ O और O = P, इसलिए M > P, यानी M # P -- यह निकलता है। "
   "II: N ≥ O = P से केवल N ≥ P मिलता है, इसलिए 'N, P से बड़ा है' (N # P) अनिवार्य नहीं: N, P के बराबर हो सकता है। केवल I निकलता है।",
   "lr-cd-a-coded-inequality-strict-and-weak", roman=True, check=_cd1)

# 12 -- each letter moves to the next letter of its own kind
def _cd2():
    V = "AEIOU"
    nxt = lambda ch: next(chr((ord(ch) - 65 + k) % 26 + 65) for k in range(1, 27)
                          if (chr((ord(ch) - 65 + k) % 26 + 65) in V) == (ch in V))
    rule = lambda w: "".join(nxt(ch) for ch in w)
    ex = {"BAKE": "CELI", "DOZEN": "FUBIP"}
    assert all(rule(w) == v for w, v in ex.items())
    # every letter of the query appears in an example, so the code of each letter is shown and the query is fixed
    letter = {a: b for w, v in ex.items() for a, b in zip(w, v)}
    assert all(ch in letter for ch in "BANKED") and "".join(letter[ch] for ch in "BANKED") == rule("BANKED") == "CEPLIF"
    # rules that shift consonants by a and vowels by b do not fit; neither does a shift that depends only on the place
    shift = lambda w, a, b: "".join(chr((ord(ch) - 65 + (b if ch in V else a)) % 26 + 65) for ch in w)
    assert not any(all(shift(w, a, b) == v for w, v in ex.items()) for a in range(26) for b in range(26))
    assert (ord("C") - ord("B")) % 26 != (ord("F") - ord("D")) % 26
    # the other options come from natural misreadings
    assert "".join(chr(ord(ch) + 1) for ch in "BANKED") == "CBOLFE"
    assert "".join(ch if ch in V else nxt(ch) for ch in "BANKED") == "CAPLEF"
    assert "".join(nxt(ch) if ch in V else chr(ord(ch) + 1) for ch in "BANKED") == "CEOLIE"
    return rule("BANKED")
N(LR, "Coding-Decoding", "hard",
  "In a certain code, BAKE is written as CELI and DOZEN as FUBIP. How is BANKED written in that code?",
  "एक निश्चित कूट में BAKE को CELI और DOZEN को FUBIP लिखा जाता है। उसी कूट में BANKED को कैसे लिखा जाएगा?",
  ["CAPLEF", "CBOLFE", "CEOLIE", "CEPLIF"], 3,
  "In BAKE → CELI and DOZEN → FUBIP, every consonant is replaced by the next consonant in the alphabet and every vowel by the next vowel: B → C, K → L, D → F (E is a vowel, so it is skipped), N → P (O is a vowel), "
  "Z → B (the alphabet starts again, and A is a vowel); A → E, E → I, O → U. For BANKED: B → C, A → E, N → P, K → L, E → I, D → F, which gives CEPLIF. "
  "CAPLEF changes only the consonants; CBOLFE moves every letter one place forward; CEOLIE moves the vowels to the next vowel but each consonant by one place, so it misses N → P and D → F.",
  "BAKE → CELI और DOZEN → FUBIP में हर व्यंजन अगले व्यंजन से और हर स्वर अगले स्वर से बदला गया है: B → C, K → L, D → F (E स्वर है, इसलिए छूट जाता है), N → P (O स्वर है), "
  "Z → B (वर्णमाला फिर से शुरू होती है, और A स्वर है); A → E, E → I, O → U। BANKED के लिए: B → C, A → E, N → P, K → L, E → I, D → F, जिससे CEPLIF बनता है। "
  "CAPLEF केवल व्यंजनों को बदलता है; CBOLFE हर अक्षर को एक स्थान आगे ले जाता है; CEOLIE स्वरों को अगले स्वर पर ले जाता है पर हर व्यंजन को केवल एक स्थान, इसलिए N → P और D → F चूक जाता है।",
  "lr-cd-the-next-letter-of-its-own-kind", check=_cd2)

# 13 -- the cubes of a 4 x 4 x 4 block that carry both colours
def _cp1():
    n = 4
    cubes = list(product(range(n), repeat=3))
    red = lambda x, y, z: z in (0, n - 1)
    blue = lambda x, y, z: x in (0, n - 1) or y in (0, n - 1)
    both = [q for q in cubes if red(*q) and blue(*q)]
    faces = lambda q: sum(v in (0, n - 1) for v in q)                    # painted faces of a small cube
    corners = [q for q in cubes if faces(q) == 3]
    two_faces = [q for q in both if faces(q) == 2]
    any_red = [q for q in cubes if red(*q)]
    assert (len(corners), len(two_faces), len(both), len(any_red)) == (8, 16, 24, 32)
    return str(len(both))
N(LR, "Cube Painting", "medium",
  "A solid cube of side 4 cm has its top and bottom faces painted red and its four side faces painted blue. It is then cut into 64 cubes of side 1 cm. How many of the small cubes have both red and blue paint on them?",
  "4 सेमी भुजा वाले एक ठोस घन के ऊपर और नीचे के फलक लाल रँगे गए हैं और चारों बग़ल के फलक नीले। फिर उसे 1 सेमी भुजा वाले 64 घनों में काटा जाता है। कितने छोटे घनों पर लाल और नीले दोनों रंग हैं?",
  ["8", "16", "24", "32"], 2,
  "A small cube carries red only if it lies in the top or the bottom layer, and carries blue only if it is on one of the four side faces, that is, on the outer ring of its layer. "
  "Both colours therefore belong to the ring cubes of the top and bottom layers. A layer has 4 × 4 = 16 cubes, of which the inner 2 × 2 = 4 touch no side face, leaving a ring of 12; the two layers give 12 + 12 = 24. "
  "8 counts only the corner cubes; 16 counts only the cubes with exactly two painted faces, leaving out the corners; 32 counts every cube with any red on it, including those with red alone.",
  "छोटे घन पर लाल रंग तभी है जब वह सबसे ऊपरी या सबसे निचली परत में हो, और नीला रंग तभी जब वह चार बग़ल के फलकों में से किसी पर हो, यानी अपनी परत के बाहरी घेरे में। "
  "इसलिए दोनों रंग ऊपरी और निचली परत के घेरे वाले घनों पर हैं। एक परत में 4 × 4 = 16 घन हैं, जिनमें भीतरी 2 × 2 = 4 किसी बग़ल के फलक को नहीं छूते, इसलिए घेरे में 12 बचते हैं; दोनों परतें 12 + 12 = 24 देती हैं। "
  "8 केवल कोने वाले घनों को गिनता है; 16 केवल उन घनों को जिनके ठीक दो फलक रँगे हैं, कोनों को छोड़कर; 32 हर उस घन को गिनता है जिस पर कुछ भी लाल है, केवल लाल वाले भी।",
  "lr-cp-both-colours-on-a-small-cube", _cp1)

# 14 -- mangoes, fruits, stones
def _sy1():
    regions = list(product((0, 1), repeat=4))                           # (mango, fruit, stone, red)
    follow = [True] * 3
    for mask in range(1, 1 << 16):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(m and not f for m, f, s, r in full):                    # all mangoes are fruits
            continue
        if any(f and s for m, f, s, r in full):                        # no fruit is a stone
            continue
        if not any(s and r for m, f, s, r in full):                    # some stones are red
            continue
        follow[0] &= not any(m and s for m, f, s, r in full)           # 1. no mango is a stone
        follow[1] &= any(r and not f for m, f, s, r in full)           # 2. some red things are not fruits
        follow[2] &= any(r and m for m, f, s, r in full)               # 3. some red things are mangoes
    assert follow == [True, True, False], follow
    return "1 and 2 only"
SC(LR, "Syllogism", "medium",
   "Statements: All mangoes are fruits. No fruit is a stone. Some stones are red.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी आम फल हैं। कोई भी फल पत्थर नहीं है। कुछ पत्थर लाल हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["No mango is a stone.", "Some red things are not fruits.", "Some red things are mangoes."],
   ["कोई भी आम पत्थर नहीं है।", "कुछ लाल वस्तुएँ फल नहीं हैं।", "कुछ लाल वस्तुएँ आम हैं।"],
   ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 1,
   "1 follows: every mango is a fruit and no fruit is a stone, so no mango is a stone. 2 follows: some stones are red, and no stone is a fruit (turn 'no fruit is a stone' round), so those red stones are red things that are not fruits. "
   "3 does not follow: the only red things the statements speak of are stones, and no mango is a stone; nothing links a red thing to a mango, so the conclusion is not forced. The conclusions that follow are 1 and 2.",
   "1 निकलता है: हर आम फल है और कोई फल पत्थर नहीं है, इसलिए कोई आम पत्थर नहीं है। 2 निकलता है: कुछ पत्थर लाल हैं, और कोई पत्थर फल नहीं है ('कोई फल पत्थर नहीं है' को पलटिए), इसलिए वे लाल पत्थर ऐसी लाल वस्तुएँ हैं जो फल नहीं हैं। "
   "3 नहीं निकलता: कथन जिन लाल वस्तुओं की बात करते हैं वे केवल पत्थर हैं, और कोई आम पत्थर नहीं है; किसी लाल वस्तु को आम से जोड़ने वाला कुछ नहीं है, इसलिए निष्कर्ष अनिवार्य नहीं। जो निष्कर्ष निकलते हैं वे 1 और 2 हैं।",
   "lr-sy-mangoes-fruits-and-stones", check=_sy1)

# 15 -- three statements about the number of liars
def _tl1():
    sols = []
    for roles in product("TL", repeat=3):
        r = dict(zip("ABC", roles))
        liars = sum(v == "L" for v in r.values())
        said = {"A": liars == 3, "B": liars == 1, "C": liars == 2}
        if all(said[p] == (r[p] == "T") for p in "ABC"):
            sols.append(r)
    assert len(sols) == 1, sols
    return next(p for p, role in sols[0].items() if role == "T")
T(LR, "Truth-Liar", "medium",
  "Each of three people -- A, B and C -- either always tells the truth or always lies. A says, 'All three of us are liars.' B says, 'Exactly one of us is a liar.' C says, 'Exactly two of us are liars.' Who tells the truth?",
  "तीन व्यक्तियों -- A, B और C -- में से प्रत्येक या तो हमेशा सच बोलता है या हमेशा झूठ। A कहता है, 'हम तीनों झूठे हैं।' B कहता है, 'हममें से ठीक एक झूठा है।' C कहता है, 'हममें से ठीक दो झूठे हैं।' सच कौन बोलता है?",
  ["A", "B", "C", "No one"], ["A", "B", "C", "कोई नहीं"], 2,
  "Suppose A tells the truth: then all three are liars, A included -- a contradiction, so A lies, and 'all three are liars' is false. B and C cannot both be truthful, since 'exactly one liar' and 'exactly two liars' cannot both be true. "
  "Suppose B tells the truth: exactly one of the three lies. A already lies, so C must tell the truth -- but C's 'exactly two of us are liars' would then be false, a contradiction. So B lies, and that leaves C: A and B are the two liars, exactly as C says, "
  "and B's 'exactly one of us is a liar' is false, as it must be. C tells the truth.",
  "मान लीजिए A सच बोलता है: तब तीनों झूठे हैं, A सहित -- एक विरोधाभास, इसलिए A झूठ बोलता है, और 'तीनों झूठे हैं' असत्य है। B और C दोनों सच नहीं बोल सकते, क्योंकि 'ठीक एक झूठा' और 'ठीक दो झूठे' दोनों सत्य नहीं हो सकते। "
  "मान लीजिए B सच बोलता है: तीनों में ठीक एक झूठ बोलता है। A पहले से झूठा है, इसलिए C को सच बोलना होगा -- पर तब C का 'हममें से ठीक दो झूठे हैं' असत्य होगा, एक विरोधाभास। इसलिए B झूठ बोलता है, और C बचता है: A और B दो झूठे हैं, ठीक वैसे ही जैसा C कहता है, "
  "और B का 'हममें से ठीक एक झूठा है' असत्य है, जैसा होना ही चाहिए। C सच बोलता है।",
  "lr-tl-statements-about-the-number-of-liars", pos=3, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    worlds = range(2, 41)
    s1 = [n for n in worlds if n * (n - 1) // 2 == 45]
    s2 = [n for n in worlds if n > 6]
    both = [n for n in s1 if n > 6]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "How many members does the committee have?",
   "समिति में कितने सदस्य हैं?",
   "Every two members of the committee shook hands exactly once, and there were 45 handshakes in all.",
   "समिति के हर दो सदस्यों ने आपस में ठीक एक बार हाथ मिलाया, और कुल 45 बार हाथ मिलाया गया।",
   "The committee has more than 6 members.", "समिति में 6 से अधिक सदस्य हैं।",
   0,
   "Statement I alone: with n members and every pair shaking hands once, the number of handshakes is n(n - 1) ÷ 2; setting this equal to 45 gives n = 10 (10 × 9 ÷ 2 = 45), the only positive solution -- sufficient. "
   "Statement II alone gives only a lower limit: 7, 8, 9 and more members all remain possible. So I alone is enough, and II alone is not.",
   "कथन I अकेला: n सदस्यों में हर जोड़ी के एक बार हाथ मिलाने पर हाथ मिलाने की संख्या n(n - 1) ÷ 2 होती है; इसे 45 के बराबर रखने पर n = 10 मिलता है (10 × 9 ÷ 2 = 45), जो एकमात्र धनात्मक हल है -- पर्याप्त। "
   "कथन II अकेला केवल निचली सीमा देता है: 7, 8, 9 और अधिक सदस्य सभी संभव रहते हैं। अतः I अकेला पर्याप्त है, और II अकेला नहीं।",
   "lr-ds-handshakes-and-members", _ds1)

def _ds2():
    pt = lambda r, a: (r * math.cos(math.radians(a)), r * math.sin(math.radians(a)))
    nearer = lambda market, school: "market" if math.hypot(*market) < math.hypot(*school) else "school"
    angles = range(0, 360, 15)
    out = lambda m, b: (m[0] + 5 * math.cos(math.radians(b)), m[1] + 5 * math.sin(math.radians(b)))   # the school, 5 km from the market
    s1 = [nearer(pt(3, a), pt(r, b)) for a in angles for r in range(1, 10) for b in angles]          # I: the market is 3 km out; the school is anywhere
    s2 = [nearer(pt(r, a), out(pt(r, a), b)) for r in range(1, 10) for a in angles for b in angles]  # II: the school is 5 km from the market, which is anywhere
    both = [nearer(pt(3, a), out(pt(3, a), b)) for a in angles for b in angles]
    d = [math.hypot(*out(pt(3, a), b)) for a in angles for b in angles]
    assert min(d) < 3 < max(d) and 2 - 1e-9 <= min(d) and max(d) <= 8 + 1e-9
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Which is nearer to the railway station: the market or the school?",
   "रेलवे स्टेशन के अधिक निकट कौन है: बाज़ार या विद्यालय?",
   "The market is 3 km from the station.", "बाज़ार स्टेशन से 3 किमी दूर है।",
   "The school is 5 km from the market.", "विद्यालय बाज़ार से 5 किमी दूर है।",
   3,
   "Statement I alone fixes the market's distance from the station but says nothing about the school. Statement II alone relates the school to the market and says nothing about the station. "
   "Together, the school's distance from the station depends on the direction in which it lies from the market: straight back past the station it is 5 - 3 = 2 km away, straight on the far side it is 3 + 5 = 8 km away, and between these it can be anywhere from 2 km to 8 km. "
   "It can therefore be nearer to the station than the market (less than 3 km) or farther (more than 3 km). The question cannot be answered even with both statements.",
   "कथन I अकेला बाज़ार की स्टेशन से दूरी तय करता है पर विद्यालय के बारे में कुछ नहीं कहता। कथन II अकेला विद्यालय को बाज़ार से जोड़ता है और स्टेशन के बारे में कुछ नहीं कहता। "
   "दोनों साथ: विद्यालय की स्टेशन से दूरी इस पर निर्भर है कि वह बाज़ार से किस दिशा में है: स्टेशन के पार सीधा पीछे की ओर वह 5 - 3 = 2 किमी दूर है, दूसरी ओर सीधा आगे की ओर 3 + 5 = 8 किमी दूर, और इनके बीच कहीं भी 2 किमी से 8 किमी के बीच। "
   "इसलिए वह स्टेशन के बाज़ार से अधिक निकट (3 किमी से कम) भी हो सकता है और अधिक दूर (3 किमी से अधिक) भी। दोनों कथनों के साथ भी प्रश्न का उत्तर नहीं दिया जा सकता।",
   "lr-ds-the-nearer-of-two-places", _ds2)

def _ds3():
    ages = [(f, s) for s in range(1, 70) for f in range(s + 15, 120)]        # the father is at least 15 years older
    s1 = [f for f, s in ages if f == 4 * s]
    s2 = [f for f, s in ages if f + s + 10 == 70]
    both = [f for f, s in ages if f == 4 * s and f + s + 10 == 70]
    assert both == [48]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "What is the present age of the father?",
   "पिता की वर्तमान आयु क्या है?",
   "The father is four times as old as his son.", "पिता अपने बेटे से चार गुना बड़ा है।",
   "Five years from now, the sum of the ages of the father and the son will be 70 years.", "पाँच वर्ष बाद पिता और बेटे की आयुओं का योग 70 वर्ष होगा।",
   2,
   "Statement I alone gives only a ratio: father 40 and son 10, or father 48 and son 12, both fit -- not sufficient. Statement II alone gives the sum of the present ages, 70 - 10 = 60, which many pairs satisfy -- not sufficient. "
   "Together, F = 4S and F + S = 60 give 5S = 60, so the son is 12 and the father 48. Both statements are needed.",
   "कथन I अकेला केवल एक अनुपात देता है: पिता 40 और बेटा 10, या पिता 48 और बेटा 12, दोनों ठीक बैठते हैं -- पर्याप्त नहीं। कथन II अकेला वर्तमान आयुओं का योग, 70 - 10 = 60, देता है, जिसे कई जोड़ियाँ पूरा करती हैं -- पर्याप्त नहीं। "
   "दोनों साथ: F = 4S और F + S = 60 से 5S = 60, इसलिए बेटा 12 वर्ष का और पिता 48 वर्ष का है। दोनों कथन ज़रूरी हैं।",
   "lr-ds-a-father-and-son-s-ages", _ds3)
