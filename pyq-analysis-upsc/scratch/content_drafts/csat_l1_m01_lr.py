# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 1 -- Logical Reasoning (9 items: 8 in the Reasoning slots, 1 in the data-sufficiency block).

The half paper's share of Level 2's Reasoning mix, at the foundation level (3 easy / 5 medium / 1 hard), with none of
Level 2's 126 Reasoning shapes: the assumption a Sunday opening of a health centre depends on, a rise in reported thefts
explained;
a bench on which one statement must be true while the others only could be; 'her mother's husband is my father's only
son-in-law'; a signpost knocked round at a crossroads; a code that swaps each pair of letters; 'some teachers are
singers, no singer is lazy'; a reply nobody heard on an island of truth-tellers and liars; and, in the data-sufficiency
block, a club whose members are all doctors. The rows are written in the order they take on the paper; arrangement,
code, truth-teller and data-sufficiency keys are found by checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _two(one, two):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 3 -- the assumption a Sunday opening depends on
_KEY_HC = "Some daily-wage workers would visit the centre on a Sunday morning if it were open."
T(LR, "Statement-Conclusion/Assumption", "easy",
  "A district official argues: 'The primary health centre should also open on Sunday mornings, because many daily-wage workers cannot come on a weekday without losing a day's pay.' "
  "Which one of the following is an assumption on which the argument depends?",
  "एक ज़िला अधिकारी का तर्क है: 'प्राथमिक स्वास्थ्य केंद्र को रविवार सुबह भी खुलना चाहिए, क्योंकि बहुत से दिहाड़ी मज़दूर एक दिन की मज़दूरी गँवाए बिना किसी कार्यदिवस पर नहीं आ सकते।' "
  "निम्नलिखित में से कौन-सी वह पूर्वधारणा है जिस पर यह तर्क निर्भर करता है?",
  [_KEY_HC,
   "Most of the patients of the health centre are daily-wage workers.",
   "Daily-wage workers fall ill more often than other people in the district do.",
   "The centre's present weekday hours are too short for the patients who come on weekdays."],
  ["कुछ दिहाड़ी मज़दूर रविवार सुबह केंद्र आएँगे, यदि वह खुला हो।",
   "स्वास्थ्य केंद्र के अधिकांश रोगी दिहाड़ी मज़दूर हैं।",
   "दिहाड़ी मज़दूर ज़िले के दूसरे लोगों की तुलना में अधिक बार बीमार पड़ते हैं।",
   "केंद्र के मौजूदा कार्यदिवस के घंटे उन रोगियों के लिए बहुत कम हैं जो कार्यदिवसों पर आते हैं।"], 0,
  "The argument offers Sunday opening as the remedy for workers who cannot come on weekdays. That works only if at least some of them would in fact come on a Sunday morning: if none would, opening on Sundays would not help them, and the argument fails. "
  "It does not need most of the centre's patients to be daily-wage workers -- 'many' who cannot come on weekdays is enough; it does not need such workers to fall ill more often; and the length of the weekday hours concerns the people who already come on weekdays, not the workers the argument is about.",
  "तर्क रविवार को खोलने को उन मज़दूरों के लिए उपाय बताता है जो कार्यदिवसों पर नहीं आ सकते। यह तभी काम करता है जब उनमें से कम से कम कुछ वास्तव में रविवार सुबह आएँ: यदि कोई न आए, तो रविवार को खोलने से उन्हें कोई लाभ नहीं, और तर्क टूट जाता है। "
  "उसके लिए यह आवश्यक नहीं कि केंद्र के अधिकांश रोगी दिहाड़ी मज़दूर हों -- कार्यदिवस पर न आ सकने वाले 'बहुत से' मज़दूर काफ़ी हैं; यह भी आवश्यक नहीं कि ऐसे मज़दूर अधिक बार बीमार पड़ें; और कार्यदिवस के घंटों की लंबाई उन लोगों से जुड़ी है जो पहले से कार्यदिवसों पर आते हैं, उन मज़दूरों से नहीं जिनकी बात तर्क करता है।",
  "lr-sc-the-assumption-a-sunday-opening-depends-on", pos=0)

# 9 -- a signpost knocked round at a crossroads
def _sign():
    compass = ["North", "East", "South", "West"]
    turn = (compass.index("South") - compass.index("East")) % 4      # the whole post turned by this many quarter-turns clockwise
    assert turn == 1
    return compass[(compass.index("North") + turn) % 4]
N(LR, "Direction & Distance", "easy",
  "A signpost at a crossroads has been knocked round, so that the arm marked 'East' now points towards the south. The arms are fixed to the post, so all of them have turned together. "
  "A traveller who follows the arm marked 'North' will actually go towards which direction?",
  "एक चौराहे पर लगा दिशा-सूचक खंभा घूम गया है, जिससे 'पूर्व' लिखी भुजा अब दक्षिण की ओर इशारा करती है। भुजाएँ खंभे से जुड़ी हैं, इसलिए सभी एक साथ घूमी हैं। "
  "'उत्तर' लिखी भुजा के अनुसार चलने वाला यात्री वास्तव में किस दिशा में जाएगा?",
  ["North", "East", "South", "West"], 1,
  "The arm marked 'East' should point east but points south: the whole signpost has turned 90° clockwise (east to south is a quarter-turn clockwise). Every arm has turned the same way, so the arm marked 'North', which should point north, "
  "now points a quarter-turn clockwise from north, that is, east. The traveller goes east. (By the same turn, the arm marked 'South' points west and the arm marked 'West' points north.)",
  "'पूर्व' लिखी भुजा को पूर्व की ओर होना चाहिए, पर वह दक्षिण की ओर है: पूरा खंभा दक्षिणावर्त 90° घूम गया है (पूर्व से दक्षिण दक्षिणावर्त एक चौथाई चक्कर है)। हर भुजा उतनी ही घूमी है, इसलिए 'उत्तर' लिखी भुजा, जिसे उत्तर की ओर होना चाहिए, "
  "अब उत्तर से दक्षिणावर्त एक चौथाई चक्कर आगे, यानी पूर्व की ओर है। यात्री पूर्व की ओर जाता है। (इसी घुमाव से 'दक्षिण' लिखी भुजा पश्चिम की ओर और 'पश्चिम' लिखी भुजा उत्तर की ओर है।)",
  "lr-dd-a-signpost-knocked-round", _sign,
  opts_hi=["उत्तर", "पूर्व", "दक्षिण", "पश्चिम"])

# 15 -- 'her mother's husband is the only son-in-law of my father'
_KEY_BR = "Her mother's brother"
def _br():
    # Arun's father F has children Arun (a son) and at least one daughter; his only son-in-law H is the husband of his
    # daughter -- so F has exactly one married daughter, Arun's sister S, and H is her husband. The woman's mother's
    # husband is H, and H's wife is S, so the woman's mother is S.
    wife_of = {"H": "S"}
    mother_of_woman = wife_of["H"]
    siblings_of_arun = {"S"}
    assert mother_of_woman in siblings_of_arun
    return _KEY_BR
T(LR, "Blood Relation", "medium",
  "Pointing to a woman, Arun said, 'Her mother's husband is the only son-in-law of my father.' How is Arun related to the woman?",
  "एक महिला की ओर संकेत करते हुए अरुण ने कहा, 'इसकी माँ का पति मेरे पिता का इकलौता दामाद है।' अरुण का उस महिला से क्या संबंध है?",
  [_KEY_BR, "Her father's brother", "Her father", "Her brother"],
  ["मामा", "चाचा", "पिता", "भाई"], 0,
  "A son-in-law of Arun's father is the husband of one of his daughters, and he has only one, so he is the husband of Arun's sister. The woman's mother's husband is that man, so the woman's mother is Arun's sister, "
  "and Arun is her mother's brother -- her maternal uncle. He cannot be her father, because the man in question is his father's son-in-law, not his father's son; and he is not her father's brother, since her father is Arun's brother-in-law. "
  "Nor is he her brother: her mother is his sister, not his mother.",
  "अरुण के पिता का दामाद उनकी किसी बेटी का पति होता है, और दामाद केवल एक है, इसलिए वह अरुण की बहन का पति है। महिला की माँ का पति वही व्यक्ति है, इसलिए महिला की माँ अरुण की बहन है, "
  "और अरुण उसकी माँ का भाई -- यानी उसका मामा -- है। वह उसका पिता नहीं हो सकता, क्योंकि वह व्यक्ति उसके पिता का दामाद है, बेटा नहीं; और वह उसका चाचा नहीं, क्योंकि उसका पिता अरुण का बहनोई है। "
  "वह उसका भाई भी नहीं: उसकी माँ अरुण की बहन है, माँ नहीं।",
  "lr-br-my-father-s-only-son-in-law", pos=0, check=_br)

# 18 -- a bench on which one statement must be true
_KEY_SA = "P does not sit at either end of the bench."
def _sa():
    sols = []
    for p in permutations("PQRST"):                       # index 0 is the west end; facing north, a person's right is east
        d = {x: i for i, x in enumerate(p)}
        if d["R"] in (0, 4) and d["Q"] - d["P"] == 1 and abs(d["S"] - d["R"]) > 1 and d["T"] < d["Q"]:
            sols.append(d)
    assert len(sols) == 4
    must = {
        _KEY_SA: all(d["P"] not in (0, 4) for d in sols),
        "P sits in the middle of the bench.": all(d["P"] == 2 for d in sols),
        "T sits next to R.": all(abs(d["T"] - d["R"]) == 1 for d in sols),
        "S sits at one of the two ends of the bench.": all(d["S"] in (0, 4) for d in sols),
    }
    could = {k: any(f(d) for d in sols) for k, f in (("P sits in the middle of the bench.", lambda d: d["P"] == 2),
                                                        ("T sits next to R.", lambda d: abs(d["T"] - d["R"]) == 1),
                                                        ("S sits at one of the two ends of the bench.", lambda d: d["S"] in (0, 4)))}
    assert [k for k, v in must.items() if v] == [_KEY_SA] and all(could.values())    # each distractor can happen, but need not
    return _KEY_SA
T(LR, "Seating Arrangement", "hard",
  "Five friends -- P, Q, R, S and T -- sit in a row on a bench, all facing north. R sits at one of the two ends of the bench. Q sits immediately to the right of P. S does not sit next to R. T sits somewhere to the left of Q. "
  "Which one of the following must be true?",
  "पाँच मित्र -- P, Q, R, S और T -- एक बेंच पर एक पंक्ति में उत्तर की ओर मुख करके बैठे हैं। R बेंच के दोनों सिरों में से किसी एक पर है। Q, P के ठीक दाईं ओर है। S, R के बगल में नहीं है। T, Q के बाईं ओर कहीं है। "
  "निम्नलिखित में से क्या अवश्य सत्य है?",
  [_KEY_SA, "P sits in the middle of the bench.", "T sits next to R.", "S sits at one of the two ends of the bench."],
  ["P बेंच के किसी भी सिरे पर नहीं है।", "P बेंच के ठीक बीच में है।", "T, R के बगल में है।", "S बेंच के दोनों सिरों में से किसी एक पर है।"], 0,
  "Number the seats 1 to 5 from the left. P cannot be in seat 5, since Q is on P's right; and P cannot be in seat 1, since Q would then be in seat 2 and T, who sits left of Q, would need seat 1. So P never sits at an end -- this must be true. "
  "The conditions allow exactly four arrangements (left to right): R T P Q S, R T S P Q, S T P Q R and T S P Q R. P is in the middle in three of them but not in R T S P Q; T sits next to R in the first two but not in the last two; "
  "and S is at an end in the first and third but not in the second and fourth. Each of these could be true, but none must be.",
  "सीटों को बाएँ से 1 से 5 तक गिनिए। P सीट 5 पर नहीं हो सकता, क्योंकि Q, P के दाईं ओर है; और P सीट 1 पर भी नहीं हो सकता, क्योंकि तब Q सीट 2 पर होगा और T को, जो Q के बाईं ओर है, सीट 1 चाहिए होगी। अतः P कभी किसी सिरे पर नहीं होता -- यह अवश्य सत्य है। "
  "शर्तें ठीक चार व्यवस्थाएँ बनने देती हैं (बाएँ से दाएँ): R T P Q S, R T S P Q, S T P Q R और T S P Q R। P इनमें से तीन में बीच में है पर R T S P Q में नहीं; T पहली दो में R के बगल में है पर अंतिम दो में नहीं; "
  "और S पहली और तीसरी में सिरे पर है पर दूसरी और चौथी में नहीं। इनमें से हर एक सत्य हो सकता है, पर कोई भी अवश्य सत्य नहीं।",
  "lr-sa-a-bench-what-must-be-true", pos=2, check=_sa)

# 23 -- a code that swaps each pair of letters
def _code():
    ex = {"FOREST": "OFERTS", "GARDEN": "AGDRNE"}
    fits = [s for s in permutations(range(6)) if all("".join(w[i] for i in s) == v for w, v in ex.items())]
    assert fits == [(1, 0, 3, 2, 5, 4)]                     # one rule of positions fits both examples: swap each pair
    shift = lambda w, k: "".join(chr((ord(ch) - 65 + k) % 26 + 65) for ch in w)
    assert not any(all(shift(w, k) == v for w, v in ex.items()) for k in range(26))     # no letter shift fits
    return "".join("CASTLE"[i] for i in fits[0])
T(LR, "Coding-Decoding", "easy",
  "In a certain code, FOREST is written as OFERTS and GARDEN is written as AGDRNE. How will CASTLE be written in that code?",
  "एक निश्चित कूट भाषा में FOREST को OFERTS और GARDEN को AGDRNE लिखा जाता है। उसी कूट भाषा में CASTLE को कैसे लिखा जाएगा?",
  ["ACTSEL", "ACSTEL", "ACTSLE", "ELTSAC"], ["ACTSEL", "ACSTEL", "ACTSLE", "ELTSAC"], 0,
  "Split each word into pairs of letters and swap the two letters of each pair: FO-RE-ST becomes OF-ER-TS, and GA-RD-EN becomes AG-DR-NE. So CA-ST-LE becomes AC-TS-EL, that is, ACTSEL. "
  "ACSTEL leaves the middle pair unswapped, ACTSLE leaves the last pair unswapped, and ELTSAC reverses the order of the pairs as well as swapping them.",
  "हर शब्द को अक्षरों के जोड़ों में बाँटिए और हर जोड़े के दोनों अक्षरों की जगह बदल दीजिए: FO-RE-ST बनता है OF-ER-TS, और GA-RD-EN बनता है AG-DR-NE। अतः CA-ST-LE बनेगा AC-TS-EL, यानी ACTSEL। "
  "ACSTEL बीच के जोड़े को नहीं बदलता, ACTSLE अंतिम जोड़े को नहीं बदलता, और ELTSAC जोड़ों को बदलने के साथ उनका क्रम भी उलट देता है।",
  "lr-cd-each-pair-of-letters-swapped", pos=1, check=_code)

# 31 -- 'some teachers are singers; no singer is lazy'
def _syl():
    regions = list(product((0, 1), repeat=3))                # (teacher, singer, lazy)
    follow = [True, True]
    for mask in range(1, 1 << 8):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not any(t and s for t, s, l in full):            # some teachers are singers
            continue
        if any(s and l for t, s, l in full):                # no singer is lazy
            continue
        follow[0] &= not any(t and l for t, s, l in full)    # I. no teacher is lazy
        follow[1] &= any(t and not l for t, s, l in full)    # II. some teachers are not lazy
    return _two(*follow)
S2(LR, "Syllogism", "medium",
   "Statements: Some teachers are singers. No singer is lazy.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ शिक्षक गायक हैं। कोई भी गायक आलसी नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["No teacher is lazy.", "Some teachers are not lazy."],
   ["कोई भी शिक्षक आलसी नहीं है।", "कुछ शिक्षक आलसी नहीं हैं।"], 1,
   "II follows: the teachers who are singers cannot be lazy, because no singer is lazy, so at least some teachers are not lazy. "
   "I does not follow: the statements say nothing about the teachers who are not singers, and some of them may well be lazy. Only II follows.",
   "II निकलता है: जो शिक्षक गायक हैं वे आलसी नहीं हो सकते, क्योंकि कोई गायक आलसी नहीं है, इसलिए कम से कम कुछ शिक्षक आलसी नहीं हैं। "
   "I नहीं निकलता: कथन उन शिक्षकों के बारे में कुछ नहीं कहते जो गायक नहीं हैं, और उनमें से कुछ आलसी हो सकते हैं। केवल II निकलता है।",
   "lr-sy-some-teachers-are-singers", roman=True, check=_syl)

# 36 -- a rise in reported thefts explained
_KEY_ST = "With better light, thefts that once went unnoticed are now seen by victims or passers-by, so more of them get reported."
T(LR, "Statement-Conclusion/Assumption", "medium",
  "After a town put up brighter street lights along its main roads, the number of thefts reported on those roads at night rose over the following year. Which one of the following, if true, best explains this?",
  "एक कस्बे ने अपनी मुख्य सड़कों पर अधिक तेज़ रोशनी वाली स्ट्रीट लाइटें लगाईं, जिसके बाद अगले वर्ष उन सड़कों पर रात में दर्ज चोरियों की संख्या बढ़ गई। निम्नलिखित में से कौन-सा, यदि सत्य हो, इसकी सबसे अच्छी व्याख्या करता है?",
  ["Most thefts in the town take place inside houses rather than on its roads, by day as well as by night.",
   _KEY_ST,
   "The new street lights cost the town a great deal more to put up than its old lights had cost it to run.",
   "Over the same year, thefts reported on the main roads during the daytime fell slightly, according to figures released by the town's police."],
  ["कस्बे में अधिकांश चोरियाँ सड़कों पर नहीं बल्कि घरों के भीतर होती हैं, दिन में भी और रात में भी।",
   "अधिक रोशनी में पहले अनदेखी रह जाने वाली चोरियाँ अब पीड़ितों या राहगीरों को दिखती हैं, इसलिए अधिक दर्ज होती हैं।",
   "नई स्ट्रीट लाइटें लगाने में कस्बे का ख़र्च पुरानी लाइटों को चलाने के ख़र्च से कहीं अधिक हुआ।",
   "कस्बे की पुलिस द्वारा जारी किए गए आँकड़ों के अनुसार, उसी वर्ष मुख्य सड़कों पर दिन के समय दर्ज होने वाली चोरियाँ थोड़ी घट गईं।"], 1,
  "The puzzle is that brighter lights, meant to deter theft, were followed by more reported thefts. The figure counts thefts that are reported, not thefts that happen. If better light lets victims and passers-by notice thefts that once went unseen, "
  "more of them are reported even if no more take place -- this explains the rise. That most thefts happen in houses does not explain a change on the roads; the cost of the lights has nothing to do with thefts; "
  "and a slight fall in daytime thefts deepens the puzzle about the night rather than explaining it.",
  "पहेली यह है कि चोरी रोकने के लिए लगाई गई तेज़ रोशनी के बाद अधिक चोरियाँ दर्ज हुईं। आँकड़ा उन चोरियों को गिनता है जो दर्ज होती हैं, उन्हें नहीं जो होती हैं। यदि बेहतर रोशनी पीड़ितों और राहगीरों को वे चोरियाँ दिखा देती है जो पहले अनदेखी रह जाती थीं, "
  "तो चोरियाँ न बढ़ने पर भी अधिक दर्ज होंगी -- यह वृद्धि की व्याख्या करता है। अधिकांश चोरियों का घरों में होना सड़कों पर आए बदलाव की व्याख्या नहीं करता; लाइटों की लागत का चोरियों से कोई संबंध नहीं; "
  "और दिन की चोरियों में थोड़ी कमी रात की पहेली को सुलझाने के बजाय और गहरा करती है।",
  "lr-sc-more-light-more-reported-thefts", pos=3)

# 39 -- a reply nobody heard on an island of truth-tellers and liars
_KEY_TL = "Q is a liar and R is a truth-teller."
def _tl():
    sols = []
    for kinds in product("TL", repeat=3):
        k = dict(zip("PQR", kinds))
        p_said_liar = False                                  # a truth-teller says 'truth-teller'; so does a liar, lying
        q_true = p_said_liar
        r_true = k["Q"] == "L"
        if (k["Q"] == "T") == q_true and (k["R"] == "T") == r_true:
            sols.append(k)
    opts = {_KEY_TL: lambda k: k["Q"] == "L" and k["R"] == "T",
            "Q is a truth-teller and R is a liar.": lambda k: k["Q"] == "T" and k["R"] == "L",
            "P is a liar.": lambda k: k["P"] == "L",
            "P and R are both truth-tellers.": lambda k: k["P"] == "T" and k["R"] == "T"}
    must = [o for o, f in opts.items() if all(f(k) for k in sols)]
    assert len(sols) == 2 and must == [_KEY_TL]
    return must[0]
T(LR, "Truth-Liar", "medium",
  "On an island, every person is either a truth-teller, who always tells the truth, or a liar, who always lies. A visitor asks P, 'Are you a truth-teller or a liar?' P replies, but the visitor does not hear the reply. "
  "Q then says, 'P said that P is a liar.' R says, 'Q is lying.' Which one of the following must be true?",
  "एक द्वीप पर हर व्यक्ति या तो सत्यवादी है, जो सदा सच बोलता है, या झूठा, जो सदा झूठ बोलता है। एक आगंतुक P से पूछता है, 'आप सत्यवादी हैं या झूठे?' P उत्तर देता है, पर आगंतुक उत्तर सुन नहीं पाता। "
  "तब Q कहता है, 'P ने कहा कि P झूठा है।' R कहता है, 'Q झूठ बोल रहा है।' निम्नलिखित में से क्या अवश्य सत्य है?",
  ["Q is a truth-teller and R is a liar.", "P is a liar.", "P and R are both truth-tellers.", _KEY_TL],
  ["Q सत्यवादी है और R झूठा है।", "P झूठा है।", "P और R दोनों सत्यवादी हैं।", "Q झूठा है और R सत्यवादी है।"], 3,
  "Nobody on the island can say 'I am a liar': a truth-teller would be lying, and a liar would be telling the truth. So whatever P is, P said 'I am a truth-teller'. Q's report that P called P a liar is therefore false, and Q is a liar. "
  "R says that Q is lying, which is true, so R is a truth-teller. P's own kind cannot be known, since both kinds give the same reply; so 'P is a liar' and 'P and R are both truth-tellers' may or may not be true, "
  "and 'Q is a truth-teller and R is a liar' is false.",
  "द्वीप पर कोई भी यह नहीं कह सकता कि 'मैं झूठा हूँ': सत्यवादी के लिए यह झूठ होगा, और झूठे के लिए सच। अतः P जो भी हो, P ने कहा 'मैं सत्यवादी हूँ'। इसलिए Q की यह बात कि P ने स्वयं को झूठा कहा, असत्य है, और Q झूठा है। "
  "R कहता है कि Q झूठ बोल रहा है, जो सत्य है, इसलिए R सत्यवादी है। P स्वयं किस प्रकार का है, यह नहीं जाना जा सकता, क्योंकि दोनों प्रकार के लोग एक ही उत्तर देते हैं; इसलिए 'P झूठा है' और 'P और R दोनों सत्यवादी हैं' सत्य हो भी सकते हैं और नहीं भी, "
  "और 'Q सत्यवादी है और R झूठा है' असत्य है।",
  "lr-tl-a-reply-nobody-heard", pos=3, check=_tl)

# ---- the data-sufficiency block's Reasoning item
def _ds1():
    # A small town stands in for the real one: five people, of whom the doctors (D) and the club's members (M) are subsets;
    # 'the club has 40 members and the town 40 doctors' becomes 'the club and the doctors are of the same size'.
    people = range(5)
    subsets = [frozenset(x for x in people if m >> x & 1) for m in range(32)]
    worlds = [(D, M) for D in subsets for M in subsets if D]
    answer = lambda D, M: D <= M
    s1 = [answer(D, M) for D, M in worlds if M <= D]
    s2 = [answer(D, M) for D, M in worlds if len(M) == len(D)]
    both = [answer(D, M) for D, M in worlds if M <= D and len(M) == len(D)]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Is every doctor in the town a member of the town's medical club?",
   "क्या कस्बे का हर डॉक्टर कस्बे के मेडिकल क्लब का सदस्य है?",
   "Every member of the club is a doctor in the town.",
   "क्लब का हर सदस्य कस्बे का डॉक्टर है।",
   "The club has 40 members, and there are 40 doctors in the town.",
   "क्लब के 40 सदस्य हैं, और कस्बे में 40 डॉक्टर हैं।",
   2,
   "Statement I says that the members are some or all of the doctors, but there may be doctors who have not joined -- not sufficient. Statement II gives equal numbers, but some members may not be doctors, leaving some doctors out -- not sufficient. "
   "Together: the 40 members are all doctors, and there are only 40 doctors, so the members are exactly the doctors, and every doctor is a member. Both statements together answer the question; neither does alone.",
   "कथन I कहता है कि सदस्य कुछ या सभी डॉक्टर हैं, पर ऐसे डॉक्टर हो सकते हैं जो क्लब में शामिल नहीं हुए -- पर्याप्त नहीं। कथन II संख्याएँ बराबर बताता है, पर कुछ सदस्य डॉक्टर न हों तो कुछ डॉक्टर बाहर रह जाएँगे -- पर्याप्त नहीं। "
   "दोनों साथ: 40 सदस्य सभी डॉक्टर हैं, और डॉक्टर केवल 40 हैं, इसलिए सदस्य ठीक-ठीक वही डॉक्टर हैं, और हर डॉक्टर सदस्य है। दोनों कथन साथ मिलकर उत्तर देते हैं; कोई भी अकेले नहीं।",
   "lr-ds-a-club-whose-members-are-all-doctors", check=_ds1)
