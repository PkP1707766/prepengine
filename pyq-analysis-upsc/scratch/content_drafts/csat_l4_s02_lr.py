# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 2 -- Logical Reasoning (17 items: 14 in the Reasoning slots, 3 in the data-sufficiency block).

Layout B, the 2025 shape. Exam-level mix (2 easy / 9 medium / 6 hard), with none of the shapes of Levels 1-3 or
Simulator 1: a study dismissed because of its author, a slippery slope from calculators, a chain of two conditions run
backwards; balls of three colours in three boxes, four meetings in two rooms, a knockout draw read back from its
results; a mother's brother across two families, a man placed by a woman's daughter's father; two legs on compass
bearings; letters in odd places first, a code that counts vowels and consonants; the small cubes seen from a corner;
'only a few'; a row of people who each call the one on their left a liar; and in the data-sufficiency block a son
found from two facts, a distance fixed by one statement, and a seat opposite that two clues leave open. Arrangement,
relation, code, cube, syllogism and truth-teller keys are found by checking every case."""
from itertools import permutations, product
from collections import Counter
import math
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a study dismissed because of its author
T(LR, "Statement-Conclusion/Assumption", "easy",
  "'Dr Rao's study showing that the new drug lowers blood pressure should be ignored, because she is known to be rude to her colleagues.' Which one of the following best describes the flaw in this argument?",
  "'डॉ. राव के उस अध्ययन की अनदेखी करनी चाहिए जो दिखाता है कि नई दवा रक्तचाप घटाती है, क्योंकि वे अपने सहकर्मियों के साथ रूखे व्यवहार के लिए जानी जाती हैं।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It rejects a finding because of the character of the person who reported it.",
   "It assumes that a drug which lowers blood pressure must be safe for every patient.",
   "It generalises about all of Dr Rao's colleagues from her behaviour towards a few.",
   "It treats the drug's popularity among doctors as proof that it works."],
  ["यह किसी निष्कर्ष को उसे प्रस्तुत करने वाले व्यक्ति के चरित्र के कारण अस्वीकार करता है।",
   "यह मान लेता है कि रक्तचाप घटाने वाली दवा हर रोगी के लिए सुरक्षित होगी।",
   "यह कुछ सहकर्मियों के साथ डॉ. राव के व्यवहार से उनके सभी सहकर्मियों के बारे में सामान्यीकरण करता है।",
   "यह डॉक्टरों में दवा की लोकप्रियता को उसके असर का प्रमाण मान लेता है।"],
  0,
  "Whether the study is sound depends on its data and methods, not on how its author treats her colleagues. The argument attacks the person instead of the finding -- the error of arguing against the person. "
  "It makes no claim about safety, draws no conclusion about Dr Rao's colleagues, and says nothing about the drug's popularity.",
  "अध्ययन ठोस है या नहीं, यह उसके आँकड़ों और विधियों पर निर्भर है, इस पर नहीं कि उसकी लेखिका सहकर्मियों से कैसा व्यवहार करती हैं। तर्क निष्कर्ष के बजाय व्यक्ति पर हमला करता है -- व्यक्ति के विरुद्ध तर्क करने की भूल। "
  "वह सुरक्षा के बारे में कोई दावा नहीं करता, डॉ. राव के सहकर्मियों के बारे में कोई निष्कर्ष नहीं निकालता, और दवा की लोकप्रियता के बारे में कुछ नहीं कहता।",
  "lr-sc-a-study-dismissed-because-of-its-author", pos=1)

# 2 -- a slippery slope from calculators
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'If we allow pupils to use calculators in examinations, they will stop learning to do sums by hand; soon no one will understand how numbers work, and within a generation the country will have no engineers.' Which one of the following best describes the flaw in this argument?",
  "'यदि हम विद्यार्थियों को परीक्षाओं में कैलकुलेटर प्रयोग करने दें, तो वे हाथ से गणना करना सीखना छोड़ देंगे; जल्दी ही कोई नहीं समझेगा कि संख्याएँ कैसे काम करती हैं, और एक पीढ़ी के भीतर देश में कोई इंजीनियर नहीं रहेगा।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It rejects the use of calculators because the people who favour them are not experts.",
   "It assumes that what is true of one examination must be true of every examination.",
   "It contradicts itself by both allowing and forbidding calculators in the same examination.",
   "It strings together a chain of consequences, each assumed to follow, with no evidence."],
  ["यह कैलकुलेटर के प्रयोग को इसलिए अस्वीकार करता है कि उसके समर्थक विशेषज्ञ नहीं हैं।",
   "यह मान लेता है कि जो एक परीक्षा के बारे में सत्य है, वह हर परीक्षा के बारे में सत्य होगा।",
   "यह एक ही परीक्षा में कैलकुलेटर की अनुमति देकर और उसे रोककर स्वयं का खंडन करता है।",
   "यह परिणामों की ऐसी कड़ी जोड़ता है जिसका हर क़दम बिना प्रमाण के निश्चित मान लिया गया है।"],
  3,
  "Each step -- calculators, then no hand arithmetic, then no understanding of numbers, then no engineers -- is presented as though it must follow from the one before, but no step is supported, and each could be checked or stopped. This is the slippery-slope error. "
  "The argument says nothing about who favours calculators, compares no examinations, and does not contradict itself.",
  "हर क़दम -- कैलकुलेटर, फिर हाथ से गणना नहीं, फिर संख्याओं की समझ नहीं, फिर इंजीनियर नहीं -- ऐसे प्रस्तुत किया गया है मानो उसे पिछले से निकलना ही हो, पर किसी क़दम का समर्थन नहीं किया गया, और हर एक को जाँचा या रोका जा सकता है। यह फिसलन-ढलान की भूल है। "
  "तर्क यह नहीं कहता कि कैलकुलेटर के समर्थक कौन हैं, किसी परीक्षा की तुलना नहीं करता, और स्वयं का खंडन नहीं करता।",
  "lr-sc-a-slippery-slope-from-calculators", pos=3)

# 3 -- a chain of two conditions run backwards
def _sc3():
    worlds = [(rain, post, hall) for rain in (True, False) for post in (True, False) for hall in (True, False)
              if (not rain or post) and (not post or hall) and not hall]
    one = all(not r for r, p, h in worlds)
    two = all(not p for r, p, h in worlds)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Statement-Conclusion/Assumption", "hard",
   "Statements: If it rains on Friday, the match will be postponed. If the match is postponed, the hall will be booked for Saturday. The hall has not been booked for Saturday.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: यदि शुक्रवार को बारिश होती है, तो मैच स्थगित होगा। यदि मैच स्थगित होता है, तो शनिवार के लिए हॉल बुक किया जाएगा। शनिवार के लिए हॉल बुक नहीं किया गया है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["It did not rain on Friday.", "The match was not postponed."],
   ["शुक्रवार को बारिश नहीं हुई।", "मैच स्थगित नहीं हुआ।"],
   2,
   "Both follow. Run the chain backwards: had the match been postponed, the hall would have been booked; it was not booked, so the match was not postponed (II). And had it rained, the match would have been postponed; it was not postponed, so it did not rain (I). "
   "The trap is to stop after the first step, or to think that a statement denied at the end of a chain says nothing about its beginning.",
   "दोनों निकलते हैं। कड़ी को उलटा चलाइए: यदि मैच स्थगित होता, तो हॉल बुक होता; वह बुक नहीं हुआ, इसलिए मैच स्थगित नहीं हुआ (II)। और यदि बारिश होती, तो मैच स्थगित होता; वह स्थगित नहीं हुआ, इसलिए बारिश नहीं हुई (I)। "
   "जाल यह है कि पहले क़दम के बाद रुक जाया जाए, या यह सोचा जाए कि कड़ी के अंत में नकारा गया कथन उसके आरंभ के बारे में कुछ नहीं कहता।",
   "lr-sc-a-chain-of-two-conditions-run-backwards", roman=True, check=_sc3)

# 4 -- balls of three colours in three boxes
def _sa1():
    sols = []
    for x in product(range(4), repeat=3):                   # (red, blue, green) in box X
        for y in product(range(4), repeat=3):
            z = tuple(3 - x[i] - y[i] for i in range(3))
            if min(z) < 0 or sum(x) != 3 or sum(y) != 3 or sum(z) != 3 or 3 in x + y + z:
                continue
            if x[0] == 2 and y[2] == 0 and z[1] == 1:
                sols.append((x, y, z))
    assert sols == [((2, 0, 1), (1, 2, 0), (0, 1, 2))]
    return str(sols[0][1][0])
N(LR, "Seating Arrangement", "medium",
  "Nine balls -- three red, three blue and three green -- are put into three boxes, X, Y and Z, three balls in each box, and no box holds three balls of the same colour. X holds exactly two red balls. Y holds no green ball. Z holds exactly one blue ball. How many red balls are in Y?",
  "नौ गेंदें -- तीन लाल, तीन नीली और तीन हरी -- तीन बक्सों, X, Y और Z, में डाली जाती हैं, हर बक्से में तीन गेंदें, और किसी बक्से में एक ही रंग की तीनों गेंदें नहीं हैं। X में ठीक दो लाल गेंदें हैं। Y में कोई हरी गेंद नहीं है। Z में ठीक एक नीली गेंद है। Y में कितनी लाल गेंदें हैं?",
  ["0", "1", "2", "3"], 1,
  "Y has no green ball, so its three balls are red and blue, and it cannot hold three of either -- so it has red and blue in some mix of 1 and 2. X has two red balls, leaving only one red ball for Y and Z together, so Y has at most one red. Hence Y has 1 red and 2 blue. "
  "Then Z has 1 blue (as given) and no red left over -- the last red ball is in Y -- so Z has 2 green, and X's third ball is the remaining green. The full sharing is X: 2 red, 1 green; Y: 1 red, 2 blue; Z: 1 blue, 2 green.",
  "Y में कोई हरी गेंद नहीं, इसलिए उसकी तीनों गेंदें लाल और नीली हैं, और उसमें किसी एक रंग की तीनों नहीं हो सकतीं -- इसलिए उसमें लाल और नीली 1 और 2 के किसी मेल में हैं। X में दो लाल गेंदें हैं, जिससे Y और Z दोनों के लिए मिलाकर केवल एक लाल बचती है, इसलिए Y में अधिक से अधिक एक लाल है। अतः Y में 1 लाल और 2 नीली हैं। "
  "तब Z में 1 नीली है (जैसा दिया गया) और कोई लाल नहीं बचती -- अंतिम लाल गेंद Y में है -- इसलिए Z में 2 हरी हैं, और X की तीसरी गेंद बची हुई हरी है। पूरा बँटवारा: X: 2 लाल, 1 हरी; Y: 1 लाल, 2 नीली; Z: 1 नीली, 2 हरी।",
  "lr-sa-balls-of-three-colours-in-three-boxes", _sa1)

# 5 -- four meetings in two rooms
def _sa2():
    cells = [(r, s) for r in (1, 2) for s in "MA"]          # room, morning / afternoon
    sols = []
    for p in permutations(cells):
        a = dict(zip("PQRS", p))
        if (a["P"][1] != a["Q"][1] and a["R"][0] == 1 and a["S"][1] == "A" and a["Q"][0] == 2 and a["P"][1] == "M"):
            sols.append(a)
    assert len(sols) == 1
    return next(k for k, v in sols[0].items() if v == (1, "A"))
N(LR, "Seating Arrangement", "medium",
  "Four meetings, P, Q, R and S, are held in two rooms, 1 and 2, one in each room in the morning and one in each room in the afternoon. P and Q are not held at the same time. R is in room 1. S is in the afternoon, and P is in the morning. Q is in room 2. Which meeting is held in room 1 in the afternoon?",
  "चार बैठकें, P, Q, R और S, दो कमरों, 1 और 2, में होती हैं, हर कमरे में एक सुबह और एक दोपहर बाद। P और Q एक ही समय नहीं होतीं। R कमरा 1 में है। S दोपहर बाद है, और P सुबह। Q कमरा 2 में है। कमरा 1 में दोपहर बाद कौन-सी बैठक होती है?",
  ["P", "Q", "R", "S"], 3,
  "P is in the morning, and since P and Q are not at the same time, Q is in the afternoon -- in room 2, as given. S is also in the afternoon, so S takes the other afternoon place, room 1. That leaves the two morning places for P and R, with R in room 1 and P in room 2. "
  "So room 1 has R in the morning and S in the afternoon; room 2 has P in the morning and Q in the afternoon.",
  "P सुबह है, और चूँकि P और Q एक समय नहीं होतीं, Q दोपहर बाद है -- कमरा 2 में, जैसा दिया गया। S भी दोपहर बाद है, इसलिए S दोपहर बाद का दूसरा स्थान, कमरा 1, लेती है। इससे सुबह के दोनों स्थान P और R के लिए बचते हैं, R कमरा 1 में और P कमरा 2 में। "
  "अतः कमरा 1 में सुबह R और दोपहर बाद S है; कमरा 2 में सुबह P और दोपहर बाद Q।",
  "lr-sa-four-meetings-in-two-rooms", _sa2)

# 6 -- a knockout draw read back from its results
def _sa3():
    champs = set()
    for w in product((0, 1), repeat=7):
        r1 = [("A", "B")[w[0]], ("C", "D")[w[1]], ("E", "F")[w[2]], ("G", "H")[w[3]]]
        sf = [(r1[0], r1[1])[w[4]], (r1[2], r1[3])[w[5]]]
        champ = sf[w[6]]
        games = [("A", "B", r1[0]), ("C", "D", r1[1]), ("E", "F", r1[2]), ("G", "H", r1[3]),
                 (r1[0], r1[1], sf[0]), (r1[2], r1[3], sf[1]), (sf[0], sf[1], champ)]
        wins = Counter(g[2] for g in games)
        lost_to = {(x if win == y else y): win for x, y, win in games}
        if lost_to.get("A") == champ and "D" in sf and wins["H"] == 1 and wins["E"] == 0:
            champs.add(champ)
    assert len(champs) == 1
    return champs.pop()
N(LR, "Seating Arrangement", "hard",
  "Eight players take part in a knockout tournament. In the first round A plays B, C plays D, E plays F and G plays H. The winner of A-B then plays the winner of C-D, the winner of E-F plays the winner of G-H, and the two winners meet in the final. A lost to the player who won the tournament. D reached the final. H won exactly one match, and E did not win any. Who won the tournament?",
  "आठ खिलाड़ी एक नॉकआउट प्रतियोगिता में भाग लेते हैं। पहले दौर में A का मैच B से, C का D से, E का F से और G का H से होता है। फिर A-B का विजेता C-D के विजेता से खेलता है, E-F का विजेता G-H के विजेता से, और दोनों विजेता फ़ाइनल में मिलते हैं। A उस खिलाड़ी से हारा जिसने प्रतियोगिता जीती। D फ़ाइनल में पहुँचा। H ने ठीक एक मैच जीता, और E ने कोई मैच नहीं जीता। प्रतियोगिता किसने जीती?",
  ["A", "C", "D", "F"], 2,
  "D reached the final, so D won the C-D match and the semi-final against the A-B winner. H won exactly one match: H beat G and then lost the semi-final. E won nothing, so F beat E -- and F, beating H in the semi-final, is the other finalist. The final is D against F. "
  "A lost to the champion. A cannot have met F (they are in different halves until the final, which A did not reach), so A lost to D -- and if A lost to D, A must have beaten B and lost the semi-final. So D is the champion. F lost the final; A and C lost to D on the way.",
  "D फ़ाइनल में पहुँचा, इसलिए D ने C-D मैच और A-B के विजेता के विरुद्ध सेमीफ़ाइनल जीता। H ने ठीक एक मैच जीता: H ने G को हराया और फिर सेमीफ़ाइनल हारा। E ने कुछ नहीं जीता, इसलिए F ने E को हराया -- और F, सेमीफ़ाइनल में H को हराकर, दूसरा फ़ाइनलिस्ट है। फ़ाइनल D और F के बीच है। "
  "A विजेता से हारा। A, F से नहीं मिल सकता था (फ़ाइनल तक वे अलग-अलग हिस्सों में हैं, और A फ़ाइनल में नहीं पहुँचा), इसलिए A, D से हारा -- और यदि A, D से हारा, तो A ने B को हराया होगा और सेमीफ़ाइनल हारा होगा। अतः D विजेता है। F फ़ाइनल हारा; A और C रास्ते में D से हारे।",
  "lr-sa-a-knockout-draw-read-back-from-its-results", _sa3)

# 7 -- a mother's brother across two families
def _br1():
    sister_of = {"Meena": "Ravi"}                  # Meena is Ravi's sister
    husband_of = {"Meena": "Sunil"}                # Meena is married to Sunil, Arun's brother
    boy_mother, boy_father = "Meena", husband_of["Meena"]
    assert sister_of[boy_mother] == "Ravi" and boy_father == "Sunil"
    return "His mother's brother"
T(LR, "Blood Relation", "medium",
  "Ravi's sister Meena is married to Arun's brother Sunil, and they have a son. How is Ravi related to Meena's son?",
  "रवि की बहन मीना का विवाह अरुण के भाई सुनील से हुआ है, और उनका एक बेटा है। रवि का मीना के बेटे से क्या संबंध है?",
  ["His father's brother", "His mother's brother", "His grandfather", "His cousin"],
  ["उसके पिता का भाई (चाचा या ताऊ)", "उसकी माँ का भाई (मामा)", "उसके दादा", "उसका चचेरा भाई"],
  1,
  "The boy's mother is Meena and his father Sunil. Ravi is Meena's brother, so Ravi is the boy's mother's brother. The father's brother is Arun, the trap in the question; Ravi is of the boy's parents' generation, not his grandfather's, and not a cousin.",
  "लड़के की माँ मीना और पिता सुनील हैं। रवि, मीना का भाई है, इसलिए रवि लड़के की माँ का भाई (मामा) है। पिता का भाई अरुण है, जो प्रश्न का जाल है; रवि लड़के के माता-पिता की पीढ़ी का है, दादा की नहीं, और चचेरा भाई भी नहीं।",
  "lr-br-a-mother-s-brother-across-two-families", pos=1, check=_br1)

# 8 -- a man placed by a woman's daughter's father
def _br2():
    daughters_father = "Kavita's husband"
    father_of = {"Kavita's husband": "F"}          # the husband's father
    only_brother_of = {"the man": "F"}             # the man's only brother is F
    assert only_brother_of["the man"] == father_of[daughters_father]
    return "He is his father's brother."
T(LR, "Blood Relation", "hard",
  "Pointing to a man, Kavita says, 'His only brother is the father of my daughter's father.' How is the man related to Kavita's husband?",
  "एक व्यक्ति की ओर इशारा करते हुए कविता कहती है, 'उसका इकलौता भाई मेरी बेटी के पिता का पिता है।' उस व्यक्ति का कविता के पति से क्या संबंध है?",
  ["He is his father, the man named in the statement.", "He is his brother.", "He is his grandfather.", "He is his father's brother."],
  ["वह उसका पिता है, जिसका कथन में उल्लेख है।", "वह उसका भाई है।", "वह उसका दादा है।", "वह उसके पिता का भाई है।"],
  3,
  "Kavita's daughter's father is Kavita's husband, and his father is the husband's father. The man's only brother is that person, so the man is the brother of the husband's father -- his father's brother. "
  "'His father' takes the man to be the person named in the statement rather than that person's brother; 'his brother' and 'his grandfather' put him in the wrong generation.",
  "कविता की बेटी का पिता कविता का पति है, और उसका पिता पति का पिता है। उस व्यक्ति का इकलौता भाई वही है, इसलिए वह व्यक्ति पति के पिता का भाई है -- यानी पति का चाचा या ताऊ। "
  "'उसका पिता' उस व्यक्ति को कथन में बताया गया व्यक्ति मान लेता है, न कि उसका भाई; 'उसका भाई' और 'उसका दादा' उसे ग़लत पीढ़ी में रखते हैं।",
  "lr-br-a-man-placed-by-a-woman-s-daughter-s-father", pos=3, check=_br2)

# 9 -- two legs on compass bearings
def _dd1():
    x = y = 0.0
    for bearing, dist in ((60, 10), (300, 10)):         # bearings measured clockwise from north
        x += dist * math.sin(math.radians(bearing))
        y += dist * math.cos(math.radians(bearing))
    assert abs(x) < 1e-9 and abs(y - 10) < 1e-9
    return "10 km due north"
N(LR, "Direction & Distance", "medium",
  "A boat sails 10 km on a bearing of 060° (60° clockwise from north) and then 10 km on a bearing of 300°. Where is it now from its starting point?",
  "एक नाव 060° के दिक्-कोण (उत्तर से 60° दक्षिणावर्त) पर 10 किमी और फिर 300° के दिक्-कोण पर 10 किमी चलती है। अब वह अपने आरंभ बिंदु से कहाँ है?",
  ["10 km due north", "20 km due north", "10√3 km due north", "10 km due east"], 0,
  "A bearing of 060° points 60° east of north, and 300° points 60° west of north. Each leg carries the boat 10 × cos 60° = 5 km north, while their east and west parts, 10 × sin 60° each, cancel. So the boat ends 5 + 5 = 10 km due north of where it started. "
  "20 km adds the two legs as if both pointed north; 10√3 km takes the sine for the northward part; 'due east' ignores the second leg's turn to the west.",
  "060° का दिक्-कोण उत्तर से 60° पूर्व की ओर है, और 300° उत्तर से 60° पश्चिम की ओर। हर हिस्सा नाव को 10 × cos 60° = 5 किमी उत्तर ले जाता है, जबकि उनके पूर्व और पश्चिम भाग, हर एक 10 × sin 60°, कट जाते हैं। अतः नाव आरंभ से 5 + 5 = 10 किमी ठीक उत्तर में पहुँचती है। "
  "20 किमी दोनों हिस्सों को ऐसे जोड़ता है मानो दोनों उत्तर की ओर हों; 10√3 किमी उत्तर वाले भाग के लिए sin ले लेता है; 'ठीक पूर्व' दूसरे हिस्से के पश्चिम की ओर मुड़ने को अनदेखा करता है।",
  "lr-dd-two-legs-on-compass-bearings", _dd1,
  opts_hi=["10 किमी ठीक उत्तर", "20 किमी ठीक उत्तर", "10√3 किमी ठीक उत्तर", "10 किमी ठीक पूर्व"])

# 10 -- letters in odd places first
def _cd1():
    code = lambda w: w[0::2] + w[1::2]
    assert code("PLANET") == "PAELNT"
    return code("GARDEN")
T(LR, "Coding-Decoding", "medium",
  "In a certain code, a word is written by taking its letters in the 1st, 3rd, 5th, ... places first and then those in the 2nd, 4th, 6th, ... places, each group in its original order; PLANET is written as PAELNT. How is GARDEN written in that code?",
  "एक विशेष कूट में कोई शब्द ऐसे लिखा जाता है कि पहले उसके पहले, तीसरे, पाँचवें, ... स्थानों के अक्षर लिए जाएँ और फिर दूसरे, चौथे, छठे, ... स्थानों के, हर समूह अपने मूल क्रम में; PLANET को PAELNT लिखा जाता है। उस कूट में GARDEN को कैसे लिखा जाएगा?",
  ["GREADN", "GRAEDN", "ADNGRE", "GERDAN"], ["GREADN", "GRAEDN", "ADNGRE", "GERDAN"],
  0,
  "GARDEN has G, R and E in the odd places and A, D and N in the even places, so it is written GREADN. "
  "ADNGRE puts the even-place letters first; GRAEDN mixes the two groups; GERDAN swaps two letters of the word instead of regrouping them.",
  "GARDEN में विषम स्थानों पर G, R और E हैं और सम स्थानों पर A, D और N, इसलिए उसे GREADN लिखा जाता है। "
  "ADNGRE सम स्थानों के अक्षर पहले रखता है; GRAEDN दोनों समूहों को मिला देता है; GERDAN अक्षरों को समूहों में रखने के बजाय शब्द के दो अक्षरों की अदला-बदली करता है।",
  "lr-cd-letters-in-odd-places-first", pos=0, check=_cd1)

# 11 -- a code that counts vowels and consonants
def _cd2():
    code = lambda w: f"{sum(ch in 'AEIOU' for ch in w)}{sum(ch not in 'AEIOU' for ch in w)}"
    assert code("TABLE") == "23"
    return code("COMPUTER")
N(LR, "Coding-Decoding", "easy",
  "In a certain code, a word is written as the number of its vowels followed by the number of its consonants; TABLE is written as 23. How is COMPUTER written in that code?",
  "एक विशेष कूट में कोई शब्द उसके स्वरों की संख्या और उसके बाद व्यंजनों की संख्या के रूप में लिखा जाता है; TABLE को 23 लिखा जाता है। उस कूट में COMPUTER को कैसे लिखा जाएगा?",
  ["26", "35", "44", "53"], 1,
  "COMPUTER has three vowels (O, U and E) and five consonants (C, M, P, T and R), so it is written 35. 53 puts the consonants first; 26 and 44 miscount the vowels.",
  "COMPUTER में तीन स्वर (O, U और E) और पाँच व्यंजन (C, M, P, T और R) हैं, इसलिए उसे 35 लिखा जाता है। 53 व्यंजन पहले रखता है; 26 और 44 स्वर ग़लत गिनते हैं।",
  "lr-cd-a-code-that-counts-vowels-and-consonants", _cd2)

# 12 -- the small cubes seen from a corner
def _cp1():
    seen = sum(1 for x, y, z in product(range(3), repeat=3) if 2 in (x, y, z))   # on one of the three faces in view
    assert 27 - 8 == seen
    return str(seen)
N(LR, "Cube Painting", "medium",
  "A large cube is built from 27 identical small cubes. It is looked at from a point from which exactly three of its faces can be seen. How many of the small cubes can be seen, at least in part?",
  "एक बड़ा घन 27 एक जैसे छोटे घनों से बना है। उसे ऐसे बिंदु से देखा जाता है जहाँ से उसके ठीक तीन फलक दिखते हैं। कितने छोटे घन, कम से कम आंशिक रूप से, दिखाई देते हैं?",
  ["19", "20", "26", "27"], 0,
  "The hidden cubes are those touching none of the three visible faces: they form the 2 × 2 × 2 block in the far corner, 8 cubes. So 27 - 8 = 19 can be seen. (Counting directly: the three faces show 9 + 9 + 9 = 27 squares, but the 3 cubes on each shared edge are counted twice and the corner cube three times, giving 27 - 9 + 1 = 19.) "
  "26 leaves out only the centre cube, which applies when the cube can be seen from all sides; 27 counts every cube; 20 has no basis.",
  "छिपे हुए घन वे हैं जो तीनों दिखने वाले फलकों में से किसी को नहीं छूते: वे दूर के कोने में 2 × 2 × 2 का खंड बनाते हैं, 8 घन। अतः 27 - 8 = 19 दिखाई देते हैं। (सीधे गिनें तो: तीन फलक 9 + 9 + 9 = 27 वर्ग दिखाते हैं, पर हर साझा किनारे के 3 घन दो बार गिने जाते हैं और कोने का घन तीन बार, जिससे 27 - 9 + 1 = 19।) "
  "26 केवल केंद्र वाले घन को छोड़ता है, जो तब लागू होता है जब घन सब ओर से देखा जा सके; 27 हर घन गिनता है; 20 का कोई आधार नहीं।",
  "lr-cp-the-small-cubes-seen-from-a-corner", _cp1)

# 13 -- 'only a few'
def _sy1():
    regions = list(product((0, 1), repeat=3))          # (car, electric, quiet)
    one = two = True
    for mask in range(1, 1 << 8):
        world = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not (any(c_ and e for c_, e, q in world) and any(c_ and not e for c_, e, q in world)): continue   # only a few cars are electric
        if any(e and not q for c_, e, q in world): continue                                                  # all electric vehicles are quiet
        one = one and any(c_ and not e for c_, e, q in world)
        two = two and any(c_ and q for c_, e, q in world)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "hard",
   "Statements: Only a few cars are electric. All electric vehicles are quiet.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: केवल कुछ ही कारें इलेक्ट्रिक हैं। सभी इलेक्ट्रिक वाहन शांत होते हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some cars are not electric.", "Some cars are quiet."],
   ["कुछ कारें इलेक्ट्रिक नहीं हैं।", "कुछ कारें शांत हैं।"],
   2,
   "Both follow. 'Only a few cars are electric' says two things: some cars are electric, and the rest -- at least some -- are not; so I follows. The cars that are electric are electric vehicles, and all of these are quiet, so some cars are quiet (II). "
   "The trap is to read 'only a few' as 'some' alone, which would lose I, or as 'none', which would lose II.",
   "दोनों निकलते हैं। 'केवल कुछ ही कारें इलेक्ट्रिक हैं' दो बातें कहता है: कुछ कारें इलेक्ट्रिक हैं, और बाक़ी -- कम से कम कुछ -- नहीं हैं; इसलिए I निकलता है। जो कारें इलेक्ट्रिक हैं वे इलेक्ट्रिक वाहन हैं, और ये सभी शांत हैं, इसलिए कुछ कारें शांत हैं (II)। "
   "जाल 'केवल कुछ ही' को अकेले 'कुछ' पढ़ना है, जिससे I छूट जाता, या 'कोई नहीं' पढ़ना, जिससे II छूट जाता।",
   "lr-sy-only-a-few", roman=True, check=_sy1)

# 14 -- a row of people who each call the one on their left a liar
def _tl1():
    rows = [t for t in product((True, False), repeat=5) if t[0] and all(t[i] == (not t[i - 1]) for i in range(1, 5))]
    assert rows == [(True, False, True, False, True)]
    return str(5 - sum(rows[0]))
N(LR, "Truth-Liar", "hard",
  "Five people stand in a row, each either always telling the truth or always lying. Each of the four people to the right of the first says, 'The person on my left is a liar.' The person at the left end always tells the truth. How many of the five are liars?",
  "पाँच लोग एक पंक्ति में खड़े हैं, हर एक या तो हमेशा सच बोलता है या हमेशा झूठ। पहले व्यक्ति के दाईं ओर के चारों में से हर एक कहता है, 'मेरे बाईं ओर वाला व्यक्ति झूठा है।' बाएँ छोर वाला व्यक्ति हमेशा सच बोलता है। पाँचों में से कितने झूठे हैं?",
  ["1", "2", "3", "4"], 1,
  "The first person tells the truth, so the second, who calls the first a liar, is lying. The third calls the second a liar, which is true, so the third tells the truth; the fourth then lies and the fifth tells the truth. The row runs truth, lie, truth, lie, truth: two liars. "
  "3 and 4 assume that everyone who makes the accusation is lying; 1 stops after the second person.",
  "पहला व्यक्ति सच बोलता है, इसलिए दूसरा, जो पहले को झूठा कहता है, झूठ बोल रहा है। तीसरा दूसरे को झूठा कहता है, जो सच है, इसलिए तीसरा सच बोलता है; तब चौथा झूठ बोलता है और पाँचवाँ सच। पंक्ति सच, झूठ, सच, झूठ, सच है: दो झूठे। "
  "3 और 4 मान लेते हैं कि आरोप लगाने वाला हर व्यक्ति झूठ बोल रहा है; 1 दूसरे व्यक्ति के बाद रुक जाता है।",
  "lr-tl-a-row-of-people-who-each-call-the-one-on-their-left-a-liar", _tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    worlds = [(parent, boy) for parent in (True, False) for boy in (True, False)]
    s1 = {p and b for p, b in worlds if p}
    s2 = {p and b for p, b in worlds if b}
    both = {p and b for p, b in worlds if p and b}
    assert both == {True}
    return _ds(s1, s2, both)
DS(LR, "easy",
   "Is X the son of Y?",
   "क्या X, Y का बेटा है?",
   "Y is one of X's parents.", "Y, X के माता-पिता में से एक है।",
   "X is a boy.", "X एक लड़का है।",
   2,
   "Statement I makes X a child of Y but does not say whether X is a son or a daughter; Statement II says X is a boy but nothing about Y. Together, X is Y's child and a boy -- Y's son. Both are needed.",
   "कथन I, X को Y की संतान बताता है पर यह नहीं कहता कि X बेटा है या बेटी; कथन II कहता है कि X लड़का है पर Y के बारे में कुछ नहीं। दोनों साथ: X, Y की संतान है और लड़का है -- Y का बेटा। दोनों आवश्यक हैं।",
   "lr-ds-a-son-found-from-two-facts", _ds1)

def _ds2():
    s1 = {math.hypot(3, 4)}                                                      # I: X 3 km north of Y, Z 4 km east of Y
    s2 = {round(math.hypot(4 * math.cos(a), x - 4 * math.sin(a)), 3) for a in (0, 1, 2) for x in (1, 3, 5)}   # II: Z 4 km from Y
    assert s1 == {5.0} and len(s2) > 1
    return _ds(s1, s2, s1)
DS(LR, "medium",
   "How far is town X from town Z, in a straight line?",
   "नगर X, नगर Z से सीधी रेखा में कितनी दूर है?",
   "X is 3 km due north of town Y, and Z is 4 km due east of Y.", "X, नगर Y से 3 किमी ठीक उत्तर में है, और Z, Y से 4 किमी ठीक पूर्व में।",
   "Z is 4 km from Y.", "Z, Y से 4 किमी दूर है।",
   0,
   "Statement I: X, Y and Z form a right angle at Y with arms of 3 km and 4 km, so X is √(3² + 4²) = 5 km from Z -- sufficient. Statement II gives one distance from Y but says nothing about where X is or in which direction Z lies -- not sufficient. One statement alone answers the question.",
   "कथन I: X, Y और Z, Y पर 3 किमी और 4 किमी भुजाओं वाला समकोण बनाते हैं, इसलिए X, Z से √(3² + 4²) = 5 किमी दूर है -- पर्याप्त। कथन II, Y से एक दूरी देता है पर यह कुछ नहीं कहता कि X कहाँ है या Z किस दिशा में है -- पर्याप्त नहीं। एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-distance-fixed-by-one-statement", _ds2)

def _ds3():
    def opposite(cond):
        out = set()
        for p in permutations(range(6)):                     # seats 0-5 round the table; A in seat 0
            a = dict(zip("ABCDEF", p))
            if a["A"] == 0 and cond(a):
                out.add(next(k for k, v in a.items() if v == 3))
        return out
    I = lambda a: a["B"] == 1
    II = lambda a: {a["D"], a["E"]} == {(a["C"] + 1) % 6, (a["C"] - 1) % 6}
    s1, s2, both = opposite(I), opposite(II), opposite(lambda a: I(a) and II(a))
    assert both == {"C", "D", "E"}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Six people, A, B, C, D, E and F, sit around a round table facing its centre. Who sits directly opposite A?",
   "छह लोग, A, B, C, D, E और F, एक गोल मेज़ के चारों ओर केंद्र की ओर मुँह करके बैठे हैं। A के ठीक सामने कौन बैठा है?",
   "B sits immediately to the left of A.", "B, A के ठीक बाईं ओर बैठा है।",
   "C sits between D and E, next to both.", "C, D और E के बीच, दोनों के बग़ल में बैठा है।",
   3,
   "With A and B fixed side by side, four seats remain, the one opposite A among them. Statement I leaves C, D, E or F free to take it. Statement II keeps D, C and E together in a block of three, but the block can sit in the four free seats in two places and either way round, so C, D or E may still be opposite A. "
   "Even together the statements do not settle who sits opposite A.",
   "A और B को अगल-बग़ल तय करने पर चार सीटें बचती हैं, जिनमें A के सामने वाली भी है। कथन I के अनुसार C, D, E या F में से कोई भी उसे ले सकता है। कथन II, D, C और E को तीन के एक खंड में साथ रखता है, पर यह खंड चार ख़ाली सीटों में दो जगह और दोनों ओर से बैठ सकता है, इसलिए C, D या E में से कोई भी A के सामने हो सकता है। "
   "दोनों कथन साथ मिलकर भी यह तय नहीं करते कि A के सामने कौन बैठा है।",
   "lr-ds-a-seat-opposite-that-two-clues-leave-open", _ds3)
