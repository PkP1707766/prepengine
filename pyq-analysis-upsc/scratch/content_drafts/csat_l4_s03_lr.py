# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 3 -- Logical Reasoning (20 items: 17 in the Reasoning slots, 3 in the data-sufficiency block).

Layout C, the 2026 shape: the heaviest Reasoning section of the three layouts. Exam-level mix (3 easy / 10 medium /
7 hard), with none of the shapes of Levels 1-3 or Simulators 1-2: a remedy proved by its popularity, a proposal
turned into a straw man, no proof of harm taken for proof of safety, what a higher average guarantees; scores with a
tie, four couples, a family of three generations in a row, a race read from its passes; cousins counted on one side,
a wife's brother's son; the far corner of a park, three towns on one road; vowels written as numbers, letters times
their places; a cube drilled through its faces; 'more than half' twice; two islanders who give the same answer; and in
the data-sufficiency block a floor found two ways, a left end fixed by a compass point, and wet ground that does not
prove rain. Arrangement, relation, code, cube, syllogism and truth-teller keys are found by checking every case."""
from itertools import permutations, product
import math
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a remedy proved by its popularity
T(LR, "Statement-Conclusion/Assumption", "easy",
  "'Millions of people take this herbal tonic every day, so it must be good for health.' Which one of the following best describes the flaw in this argument?",
  "'लाखों लोग रोज़ यह जड़ी-बूटी वाला टॉनिक लेते हैं, इसलिए यह स्वास्थ्य के लिए अच्छा ही होगा।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It takes the number of people who use the tonic as proof that it works.",
   "It attacks the people who doubt the tonic instead of answering their doubts.",
   "It assumes that whatever is natural must also be safe for every person.",
   "It argues in a circle, using its own conclusion as one of its premises."],
  ["यह टॉनिक लेने वालों की संख्या को उसके असर का प्रमाण मान लेता है।",
   "यह टॉनिक पर संदेह करने वालों के संदेहों का उत्तर देने के बजाय उन पर हमला करता है।",
   "यह मान लेता है कि जो कुछ प्राकृतिक है वह हर व्यक्ति के लिए सुरक्षित भी होगा।",
   "यह चक्राकार तर्क करता है, अपने ही निष्कर्ष को अपने आधार-वाक्यों में से एक बनाकर।"],
  0,
  "The only reason given is that many people take the tonic, but how many people do something says nothing about whether it works: popular remedies can be useless, and effective ones little used. "
  "The argument attacks no doubters, says nothing about the tonic being natural, and does not assume its conclusion.",
  "दिया गया एकमात्र कारण यह है कि बहुत-से लोग टॉनिक लेते हैं, पर कितने लोग कुछ करते हैं, इससे यह पता नहीं चलता कि वह काम करता है: लोकप्रिय उपचार व्यर्थ हो सकते हैं, और प्रभावी उपचार कम प्रयुक्त। "
  "तर्क किसी संदेह करने वाले पर हमला नहीं करता, टॉनिक के प्राकृतिक होने के बारे में कुछ नहीं कहता, और अपना निष्कर्ष मान नहीं लेता।",
  "lr-sc-a-remedy-proved-by-its-popularity", pos=3)

# 2 -- a proposal turned into a straw man
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'Mr Sen proposes cutting the defence budget by 5 per cent. Clearly he wants to leave the country defenceless.' Which one of the following best describes the flaw in this argument?",
  "'श्री सेन रक्षा बजट में 5 प्रतिशत कटौती का प्रस्ताव करते हैं। स्पष्ट है कि वे देश को असुरक्षित छोड़ देना चाहते हैं।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It replaces the actual proposal with an extreme version that is easy to attack.",
   "It rejects the proposal because of Mr Sen's personal character and past conduct.",
   "It assumes that a small cut must be followed by a chain of ever larger cuts.",
   "It relies on the opinions of defence experts whom it does not even trouble to name."],
  ["यह वास्तविक प्रस्ताव की जगह उसका ऐसा अतिवादी रूप रखता है जिस पर हमला आसान है।",
   "यह प्रस्ताव को श्री सेन के निजी चरित्र और पिछले आचरण के कारण अस्वीकार करता है।",
   "यह मान लेता है कि एक छोटी कटौती के बाद लगातार बड़ी होती कटौतियों की कड़ी आएगी।",
   "यह रक्षा विशेषज्ञों की राय पर टिका है जिनके नाम बताने का कष्ट भी वह नहीं उठाता।"],
  0,
  "A 5 per cent cut is a modest change; the argument attacks a far more extreme position -- leaving the country defenceless -- that Mr Sen never took. This is the straw-man error. "
  "It says nothing about his character; it does not predict a chain of further cuts, but simply misstates what he wants; and it cites no experts.",
  "5 प्रतिशत की कटौती एक साधारण बदलाव है; तर्क एक कहीं अधिक अतिवादी स्थिति पर हमला करता है -- देश को असुरक्षित छोड़ना -- जो श्री सेन ने कभी नहीं ली। यह 'पुतले पर वार' (स्ट्रॉ-मैन) की भूल है। "
  "वह उनके चरित्र के बारे में कुछ नहीं कहता; वह आगे की कटौतियों की कड़ी की भविष्यवाणी नहीं करता, बस यह ग़लत बताता है कि वे क्या चाहते हैं; और किसी विशेषज्ञ का हवाला नहीं देता।",
  "lr-sc-a-proposal-turned-into-a-straw-man", pos=0)

# 3 -- no proof of harm taken for proof of safety
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'No study has ever shown that this food additive is harmful, so it must be safe.' Which one of the following best describes the flaw in this argument?",
  "'किसी अध्ययन ने कभी नहीं दिखाया कि यह खाद्य योज्य हानिकारक है, इसलिए यह सुरक्षित ही होगा।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It reaches a general conclusion about all additives from a single study of one of them.",
   "It assumes that what is true of this additive must be true of every other additive.",
   "It attacks the scientists who have studied the additive instead of their findings.",
   "It treats the absence of proof of harm as though it were proof of safety."],
  ["यह किसी एक योज्य के एक अकेले अध्ययन से सभी योज्यों के बारे में सामान्य निष्कर्ष निकालता है।",
   "यह मान लेता है कि जो इस योज्य के बारे में सत्य है वह हर दूसरे योज्य के बारे में सत्य होगा।",
   "यह योज्य का अध्ययन करने वाले वैज्ञानिकों पर उनके निष्कर्षों के बजाय हमला करता है।",
   "यह हानि के प्रमाण के अभाव को ऐसे लेता है मानो वह सुरक्षा का प्रमाण हो।"],
  3,
  "That no study has shown harm may only mean that the right studies have not been done, or were too small to detect it. The argument treats a lack of evidence against the additive as evidence for it -- the error of arguing from ignorance. "
  "It draws on no single study, makes no claim about other additives, and attacks no scientists.",
  "यह कि किसी अध्ययन ने हानि नहीं दिखाई, इसका अर्थ केवल यह हो सकता है कि सही अध्ययन हुए ही नहीं, या वे हानि पकड़ने के लिए बहुत छोटे थे। तर्क योज्य के विरुद्ध प्रमाण की कमी को उसके पक्ष का प्रमाण मान लेता है -- अज्ञान से तर्क करने की भूल। "
  "वह किसी अकेले अध्ययन पर नहीं टिका, दूसरे योज्यों के बारे में कोई दावा नहीं करता, और किसी वैज्ञानिक पर हमला नहीं करता।",
  "lr-sc-no-proof-of-harm-taken-for-proof-of-safety", pos=3)

# 4 -- what a higher average guarantees
def _sc4():
    one = two = True
    vals = range(1, 7)
    for a in product(vals, repeat=3):
        for b in product(vals, repeat=3):
            if sum(a) / 3 > sum(b) / 3:
                one = one and max(a) > min(b)
                two = two and max(a) >= max(b)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Statement-Conclusion/Assumption", "hard",
   "Statement: The average monthly income of the households in village A is higher than that of the households in village B.\n\nWhich of the following conclusions follow(s) from the statement?",
   "कथन: गाँव A के परिवारों की औसत मासिक आय गाँव B के परिवारों से अधिक है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथन से निकलता/निकलते है/हैं?",
   ["At least one household in A earns more than at least one household in B.",
    "The richest household of the two villages is in A."],
   ["A का कम से कम एक परिवार B के कम से कम एक परिवार से अधिक कमाता है।",
    "दोनों गाँवों का सबसे धनी परिवार A में है।"],
   0,
   "Only I follows. The richest household in A earns at least A's average, which is above B's average, which in turn is at least what the poorest household in B earns; so A's richest earns more than B's poorest (I). "
   "II does not follow: B could contain the single richest household while most of its households are poor enough to pull its average below A's.",
   "केवल I निकलता है। A का सबसे धनी परिवार कम से कम A के औसत जितना कमाता है, जो B के औसत से अधिक है, जो स्वयं कम से कम उतना है जितना B का सबसे निर्धन परिवार कमाता है; इसलिए A का सबसे धनी परिवार B के सबसे निर्धन से अधिक कमाता है (I)। "
   "II नहीं निकलता: B में अकेला सबसे धनी परिवार हो सकता है, जबकि उसके अधिकांश परिवार इतने निर्धन हों कि उसका औसत A से नीचे आ जाए।",
   "lr-sc-what-a-higher-average-guarantees", roman=True, check=_sc4)

# 5 -- scores with a tie
def _sa1():
    counts = set()
    for s in product(range(1, 11), repeat=5):
        a = dict(zip("ABCDE", s))
        if a["B"] < a["A"] < a["C"] and a["D"] == a["B"] and all(a["E"] < a[x] for x in "ABC") and a["E"] != a["D"]:
            counts.add(len(set(s)))
    assert counts == {4}
    return "4"
N(LR, "Seating Arrangement", "medium",
  "In a test, A scored more than B but less than C. D scored exactly the same as B. E scored less than each of A, B and C, and not the same as D. How many different scores did the five students get between them?",
  "एक परीक्षा में A ने B से अधिक पर C से कम अंक पाए। D ने ठीक B जितने अंक पाए। E ने A, B और C में से हर एक से कम अंक पाए, और D के बराबर नहीं। पाँचों विद्यार्थियों ने मिलकर कितने अलग-अलग अंक पाए?",
  ["2", "3", "4", "5"], 2,
  "From the top: C is above A, and A above B. D has the same score as B. E is below B -- and so below D too -- and not equal to D. The order is C, A, then B and D together, then E: four different scores. "
  "5 forgets that B and D share a score; 3 treats E as tied with B and D, which the last clue rules out; 2 has no basis.",
  "ऊपर से: C, A से ऊपर है, और A, B से ऊपर। D के अंक B जितने हैं। E, B से नीचे है -- और इसलिए D से भी -- और D के बराबर नहीं। क्रम है C, A, फिर B और D साथ, फिर E: चार अलग-अलग अंक। "
  "5 भूल जाता है कि B और D के अंक एक हैं; 3, E को B और D के बराबर मान लेता है, जिसे अंतिम संकेत नकारता है; 2 का कोई आधार नहीं।",
  "lr-sa-scores-with-a-tie", _sa1)

# 6 -- four couples
def _sa2():
    sols = []
    for w in permutations("PQRS"):
        m = dict(zip("ABCD", w))
        if (m["A"] not in ("P", "Q", "S") and (m["B"] == "Q" or m["C"] == "Q") and m["C"] != "S" and m["D"] != "S" and m["B"] != "P"):
            sols.append(m)
    assert sols == [{"A": "R", "B": "S", "C": "Q", "D": "P"}]
    return sols[0]["C"]
N(LR, "Seating Arrangement", "medium",
  "Four men, A, B, C and D, are married to four women, P, Q, R and S, one each. A is married to none of P, Q and S. Q is married to B or to C. S is not married to C or to D. B is not married to P. To whom is C married?",
  "चार पुरुष, A, B, C और D, चार महिलाओं, P, Q, R और S, से विवाहित हैं, हर एक एक से। A का विवाह P, Q और S में से किसी से नहीं हुआ है। Q का विवाह B या C से हुआ है। S का विवाह न C से हुआ है न D से। B का विवाह P से नहीं हुआ है। C का विवाह किससे हुआ है?",
  ["P", "Q", "R", "S"], 1,
  "A is married to none of P, Q and S, so A is married to R. S is not married to C or D, and not to A, so S is married to B. Q is married to B or C; B is taken, so Q is married to C. That leaves D married to P, which fits the clue that B is not married to P. So C is married to Q.",
  "A का विवाह P, Q और S में से किसी से नहीं हुआ, इसलिए A का विवाह R से हुआ है। S का विवाह न C से हुआ है न D से, और A से भी नहीं, इसलिए S का विवाह B से हुआ है। Q का विवाह B या C से हुआ है; B का विवाह हो चुका, इसलिए Q का विवाह C से हुआ है। इससे D का विवाह P से बचता है, जो इस संकेत से मेल खाता है कि B का विवाह P से नहीं हुआ। अतः C का विवाह Q से हुआ है।",
  "lr-sa-four-couples", _sa2)

# 7 -- a family of three generations in a row
def _sa3():
    names = ["GF", "F", "M", "S", "D"]
    sols = []
    for p in permutations(range(1, 6)):
        a = dict(zip(names, p))
        if (abs(a["F"] - a["M"]) == 1 and a["M"] == 3 and a["GF"] == 5 and abs(a["GF"] - a["F"]) != 1
                and abs(a["S"] - a["D"]) != 1 and a["D"] < a["S"]):
            sols.append(a)
    assert sols == [{"GF": 5, "F": 2, "M": 3, "S": 4, "D": 1}]
    between = [k for k, v in sols[0].items() if sols[0]["M"] < v < sols[0]["GF"]]
    assert between == ["S"]
    return "The son"
T(LR, "Seating Arrangement", "hard",
  "Five members of a family -- a grandfather, his son, the son's wife, and their son and daughter -- sit in a row of five seats, all facing the same way. The son's wife sits in the middle seat, next to her husband. The grandfather sits at the right end, but not next to his son. The two children do not sit next to each other, and the daughter sits somewhere to the left of her brother. Who sits between the children's mother and the grandfather?",
  "एक परिवार के पाँच सदस्य -- एक दादा, उनका बेटा, बेटे की पत्नी, और उनका बेटा और बेटी -- एक ही दिशा में मुँह किए पाँच सीटों की एक पंक्ति में बैठे हैं। बेटे की पत्नी बीच की सीट पर, अपने पति के बग़ल में बैठी है। दादा दाएँ छोर पर बैठे हैं, पर अपने बेटे के बग़ल में नहीं। दोनों बच्चे एक-दूसरे के बग़ल में नहीं बैठे, और बेटी अपने भाई से कहीं बाईं ओर बैठी है। बच्चों की माँ और दादा के बीच कौन बैठा है?",
  ["The son", "The father", "The daughter", "No one sits between them"],
  ["बेटा", "पिता", "बेटी", "उनके बीच कोई नहीं बैठा"],
  0,
  "Number the seats 1 to 5 from the left. The mother is in seat 3 and the grandfather in seat 5. The father sits next to the mother, in seat 2 or 4, but not next to the grandfather, so he is in seat 2. That leaves seats 1 and 4 for the children, who are then not side by side, with the daughter to the left: daughter in 1, son in 4. "
  "So the row is daughter, father, mother, son, grandfather, and the son sits between the mother and the grandfather. The father sits on the mother's other side; the daughter is at the far left.",
  "सीटों को बाएँ से 1 से 5 तक गिनिए। माँ सीट 3 पर और दादा सीट 5 पर हैं। पिता माँ के बग़ल में, सीट 2 या 4 पर, बैठते हैं, पर दादा के बग़ल में नहीं, इसलिए वे सीट 2 पर हैं। इससे सीटें 1 और 4 बच्चों के लिए बचती हैं, जो तब अगल-बग़ल नहीं हैं, बेटी बाईं ओर: बेटी 1 पर, बेटा 4 पर। "
  "अतः पंक्ति है बेटी, पिता, माँ, बेटा, दादा, और बेटा माँ और दादा के बीच बैठा है। पिता माँ की दूसरी ओर बैठे हैं; बेटी सबसे बाईं ओर है।",
  "lr-sa-a-family-of-three-generations-in-a-row", pos=2, check=_sa3)

# 8 -- a race read from its passes
def _sa4():
    order = list("PQRS")
    for passer, passed in (("R", "Q"), ("S", "Q"), ("S", "R"), ("Q", "R")):
        i, j = order.index(passer), order.index(passed)
        assert i == j + 1
        order[i], order[j] = order[j], order[i]
    assert order == list("PSQR")
    return order[2]
N(LR, "Seating Arrangement", "medium",
  "Four runners started a race in the order P, Q, R, S, with P in front. During the race R passed Q, then S passed Q, then S passed R, and finally Q passed R; there was no other passing. Who finished third?",
  "चार धावकों ने दौड़ P, Q, R, S के क्रम में शुरू की, P सबसे आगे। दौड़ के दौरान R ने Q को पार किया, फिर S ने Q को, फिर S ने R को, और अंत में Q ने R को; और कोई आगे-पीछे नहीं हुआ। तीसरे स्थान पर कौन रहा?",
  ["P", "Q", "R", "S"], 1,
  "Follow each pass, which swaps two neighbouring runners. P Q R S becomes P R Q S (R passes Q), then P R S Q (S passes Q), then P S R Q (S passes R), and finally P S Q R (Q passes R). So the finishing order is P, S, Q, R, and Q is third. S is second and R last.",
  "हर बार पार करने को देखिए, जो दो पास-पास के धावकों की अदला-बदली करता है। P Q R S बनता है P R Q S (R, Q को पार करता है), फिर P R S Q (S, Q को), फिर P S R Q (S, R को), और अंत में P S Q R (Q, R को)। अतः समाप्ति का क्रम P, S, Q, R है, और Q तीसरा है। S दूसरा और R अंतिम है।",
  "lr-sa-a-race-read-from-its-passes", _sa4)

# 9 -- cousins counted on one side
def _br1():
    rams_brothers_children = [2, 2]
    return str(sum(rams_brothers_children))
N(LR, "Blood Relation", "easy",
  "Ram has two brothers and no sisters. Each of his brothers has two children, and Ram himself has three children. How many first cousins does Ram's daughter have on her father's side?",
  "राम के दो भाई हैं और कोई बहन नहीं। उसके हर भाई के दो बच्चे हैं, और स्वयं राम के तीन बच्चे हैं। राम की बेटी के पिता की ओर से कितने चचेरे भाई-बहन हैं?",
  ["2", "3", "4", "6"], 2,
  "Her first cousins on her father's side are the children of her father's brothers and sisters. Ram has two brothers with two children each and no sisters, so she has 4 such cousins. Ram's own three children are her brothers and sisters, not her cousins; 6 adds two of them in, and 2 counts only one uncle's children.",
  "उसके पिता की ओर से चचेरे भाई-बहन उसके पिता के भाई-बहनों के बच्चे हैं। राम के दो भाई हैं जिनके दो-दो बच्चे हैं, और कोई बहन नहीं, इसलिए उसके ऐसे 4 चचेरे भाई-बहन हैं। राम के अपने तीन बच्चे उसके भाई-बहन हैं, चचेरे भाई-बहन नहीं; 6 उनमें से दो को जोड़ देता है, और 2 केवल एक चाचा के बच्चे गिनता है।",
  "lr-br-cousins-counted-on-one-side", _br1)

# 10 -- a wife's brother's son
def _br2():
    sister_of = {"Bimal": "Arun's wife"}
    father_of = {"Chetan": "Bimal"}
    assert sister_of[father_of["Chetan"]] == "Arun's wife"
    return "He is Chetan's father's sister's husband."
T(LR, "Blood Relation", "medium",
  "Arun's wife's brother is Bimal, and Bimal's son is Chetan. How is Arun related to Chetan?",
  "अरुण की पत्नी का भाई बिमल है, और बिमल का बेटा चेतन है। अरुण का चेतन से क्या संबंध है?",
  ["He is Chetan's mother's brother.", "He is Chetan's father's brother.", "He is Chetan's grandfather on his father's side.",
   "He is Chetan's father's sister's husband."],
  ["वह चेतन की माँ का भाई (मामा) है।", "वह चेतन के पिता का भाई (चाचा या ताऊ) है।", "वह चेतन के पिता की ओर से उसका दादा है।",
   "वह चेतन के पिता की बहन का पति (फूफा) है।"],
  3,
  "Chetan's father is Bimal, and Bimal's sister is Arun's wife; so Arun is married to Chetan's father's sister -- he is her husband. "
  "He is not Chetan's mother's brother, for nothing is said of Chetan's mother; not his father's brother, for Arun is Bimal's sister's husband, not his brother; and he is of Chetan's father's generation, not his grandfather's.",
  "चेतन के पिता बिमल हैं, और बिमल की बहन अरुण की पत्नी है; इसलिए अरुण का विवाह चेतन के पिता की बहन (बुआ) से हुआ है -- वह उसके पति (फूफा) हैं। "
  "वह चेतन की माँ के भाई नहीं, क्योंकि चेतन की माँ के बारे में कुछ नहीं कहा गया; न उसके पिता के भाई, क्योंकि अरुण बिमल की बहन के पति हैं, उनके भाई नहीं; और वह चेतन के पिता की पीढ़ी के हैं, दादा की नहीं।",
  "lr-br-a-wife-s-brother-s-son", pos=3, check=_br2)

# 11 -- the far corner of a park
def _dd1():
    return f"{int(math.hypot(300, 400))} m"
N(LR, "Direction & Distance", "medium",
  "From a corner of a rectangular park measuring 300 m by 400 m, a man walks the whole length of a 300 m side and then the whole length of the adjoining 400 m side. How far is he then, in a straight line, from where he set out?",
  "300 मीटर × 400 मीटर माप वाले एक आयताकार पार्क के एक कोने से एक व्यक्ति पूरी 300 मीटर वाली भुजा और फिर उससे जुड़ी पूरी 400 मीटर वाली भुजा चलता है। तब वह जहाँ से चला था वहाँ से सीधी रेखा में कितनी दूर है?",
  ["100 m", "300 m", "500 m", "700 m"], 2,
  "Walking one 300 m side and then the adjoining 400 m side takes him to the corner diagonally opposite the start. The diagonal is √(300² + 400²) = 500 m. 700 m is the distance walked, not the straight-line distance; 100 m and 300 m have no basis.",
  "एक 300 मीटर भुजा और फिर उससे जुड़ी 400 मीटर भुजा पर चलना उसे आरंभ के ठीक सामने वाले (विकर्णतः विपरीत) कोने तक ले जाता है। विकर्ण √(300² + 400²) = 500 मीटर है। 700 मीटर चली गई दूरी है, सीधी दूरी नहीं; 100 मीटर और 300 मीटर का कोई आधार नहीं।",
  "lr-dd-the-far-corner-of-a-park", _dd1,
  opts_hi=["100 मीटर", "300 मीटर", "500 मीटर", "700 मीटर"])

# 12 -- three towns on one road
def _dd2():
    ds = {abs(q + s * 15 - (q + t * 10)) for q in (0,) for s in (1, -1) for t in (1, -1)}
    assert ds == {5, 25}
    return "Either 5 km or 25 km"
T(LR, "Direction & Distance", "hard",
  "Towns P, Q and R stand on the same straight road. Q is 10 km from P and 15 km from R. How far is P from R?",
  "नगर P, Q और R एक ही सीधी सड़क पर हैं। Q, P से 10 किमी और R से 15 किमी दूर है। P, R से कितनी दूर है?",
  ["Either 5 km or 25 km", "25 km, and no other distance", "5 km, and no other distance",
   "It cannot be found, since the directions of the towns are not given"],
  ["या तो 5 किमी या 25 किमी", "25 किमी, और कोई दूसरी दूरी नहीं", "5 किमी, और कोई दूसरी दूरी नहीं",
   "यह ज्ञात नहीं किया जा सकता, क्योंकि नगरों की दिशाएँ नहीं दी गईं"],
  0,
  "If Q lies between P and R, the distance is 10 + 15 = 25 km; if P and R lie on the same side of Q, it is 15 - 10 = 5 km. Both arrangements fit the facts, so the distance is either 5 km or 25 km. "
  "Each single answer assumes one arrangement; and the possibilities are not unlimited, since the towns are on one straight road -- only two distances can arise.",
  "यदि Q, P और R के बीच है, तो दूरी 10 + 15 = 25 किमी है; यदि P और R, Q की एक ही ओर हैं, तो 15 - 10 = 5 किमी। दोनों व्यवस्थाएँ तथ्यों से मेल खाती हैं, इसलिए दूरी या तो 5 किमी है या 25 किमी। "
  "हर अकेला उत्तर एक ही व्यवस्था मान लेता है; और संभावनाएँ असीमित नहीं, क्योंकि नगर एक सीधी सड़क पर हैं -- केवल दो दूरियाँ संभव हैं।",
  "lr-dd-three-towns-on-one-road", pos=0, check=_dd2)

# 13 -- vowels written as numbers
def _cd1():
    code = lambda w: "".join(str("AEIOU".index(ch) + 1) if ch in "AEIOU" else ch for ch in w)
    assert code("MOTHER") == "M4TH2R"
    return code("TEACHER")
T(LR, "Coding-Decoding", "easy",
  "In a certain code, each vowel in a word is replaced by its place among the vowels (A = 1, E = 2, I = 3, O = 4, U = 5), and the consonants are left as they are; MOTHER is written as M4TH2R. How is TEACHER written in that code?",
  "एक विशेष कूट में शब्द के हर स्वर को स्वरों में उसके स्थान (A = 1, E = 2, I = 3, O = 4, U = 5) से बदला जाता है, और व्यंजन जैसे हैं वैसे रहते हैं; MOTHER को M4TH2R लिखा जाता है। उस कूट में TEACHER को कैसे लिखा जाएगा?",
  ["T12CH2R", "T21CH2R", "T21CH1R", "T2ACH2R"], ["T12CH2R", "T21CH2R", "T21CH1R", "T2ACH2R"],
  1,
  "T stays, E becomes 2, A becomes 1, C and H stay, E becomes 2 and R stays: T21CH2R. T12CH2R swaps the two vowels; T21CH1R codes the second E as an A; T2ACH2R leaves the A uncoded.",
  "T वैसा ही रहता है, E बनता है 2, A बनता है 1, C और H वैसे ही रहते हैं, E बनता है 2 और R वैसा ही: T21CH2R। T12CH2R दोनों स्वरों की अदला-बदली कर देता है; T21CH1R दूसरे E को A मानकर लिखता है; T2ACH2R, A को बिना बदले छोड़ देता है।",
  "lr-cd-vowels-written-as-numbers", pos=1, check=_cd1)

# 14 -- letters times their places
def _cd2():
    code = lambda w: "-".join(str((i + 1) * (ord(ch) - 64)) for i, ch in enumerate(w))
    assert code("ABC") == "1-4-9"
    return code("CAB")
T(LR, "Coding-Decoding", "medium",
  "In a certain code, each letter of a word is replaced by the product of its place in the word and its place in the alphabet; ABC is written as 1-4-9. How is CAB written in that code?",
  "एक विशेष कूट में शब्द के हर अक्षर को शब्द में उसके स्थान और वर्णमाला में उसके स्थान के गुणनफल से बदला जाता है; ABC को 1-4-9 लिखा जाता है। उस कूट में CAB को कैसे लिखा जाएगा?",
  ["3-2-6", "1-4-9", "3-1-2", "9-2-3"], ["3-2-6", "1-4-9", "3-1-2", "9-2-3"],
  0,
  "C is 3rd in the alphabet and 1st in the word: 3 × 1 = 3. A is 1st in the alphabet and 2nd in the word: 1 × 2 = 2. B is 2nd and 3rd: 2 × 3 = 6. So CAB is 3-2-6. "
  "1-4-9 is the code of ABC, unchanged; 3-1-2 gives only the alphabet places; 9-2-3 multiplies C by its alphabet place twice.",
  "C वर्णमाला में तीसरा और शब्द में पहला है: 3 × 1 = 3। A वर्णमाला में पहला और शब्द में दूसरा है: 1 × 2 = 2। B दूसरा और तीसरा है: 2 × 3 = 6। अतः CAB = 3-2-6। "
  "1-4-9, ABC का कूट है, बिना बदले; 3-1-2 केवल वर्णमाला के स्थान देता है; 9-2-3, C को उसके वर्णमाला स्थान से दो बार गुणा करता है।",
  "lr-cd-letters-times-their-places", pos=3, check=_cd2)

# 15 -- a cube drilled through its faces
def _cp1():
    cells = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
    left = [cc for cc in cells if sum(v == 1 for v in cc) < 2]       # a tunnel removes every cube on a central line
    return str(len(left))
N(LR, "Cube Painting", "hard",
  "A large cube is made of 27 small cubes. Three square tunnels, each the width of one small cube, are cut straight through it from the centre of each face to the centre of the opposite face, removing every small cube that lies in their way. How many small cubes are left?",
  "एक बड़ा घन 27 छोटे घनों से बना है। उसमें तीन वर्गाकार सुरंगें, हर एक एक छोटे घन की चौड़ाई की, हर फलक के केंद्र से सामने वाले फलक के केंद्र तक सीधी काटी जाती हैं, जिनके रास्ते में आने वाला हर छोटा घन हटा दिया जाता है। कितने छोटे घन बचते हैं?",
  ["18", "19", "20", "21"], 2,
  "Each tunnel removes the three cubes in a line through the centre, but all three tunnels pass through the central cube. So the cubes removed are the centre and the six cubes at the centres of the faces: 7 in all, leaving 27 - 7 = 20 -- the 8 corner cubes and the 12 edge cubes. "
  "18 subtracts 3 cubes for each tunnel, counting the centre three times; 19 counts it twice; 21 leaves out one face-centre cube.",
  "हर सुरंग केंद्र से होकर जाती रेखा के तीन घन हटाती है, पर तीनों सुरंगें केंद्र वाले घन से गुज़रती हैं। इसलिए हटाए गए घन हैं केंद्र और फलकों के केंद्रों पर के छह घन: कुल 7, जिससे 27 - 7 = 20 बचते हैं -- 8 कोने वाले और 12 किनारे वाले घन। "
  "18 हर सुरंग के लिए 3 घन घटाता है, केंद्र को तीन बार गिनकर; 19 उसे दो बार गिनता है; 21 फलक-केंद्र का एक घन छोड़ देता है।",
  "lr-cp-a-cube-drilled-through-its-faces", _cp1)

# 16 -- 'more than half' twice
def _sy1():
    one = two = True
    for n in range(1, 8):
        for flags in product(product((0, 1), repeat=2), repeat=n):         # (teacher, singer) for each member
            if sum(t for t, s in flags) * 2 > n and sum(s for t, s in flags) * 2 > n:
                one = one and any(t and s for t, s in flags)
                two = two and all(t or s for t, s in flags)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "hard",
   "Statements: More than half of the members of a club are teachers. More than half of the members of the club are singers.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: एक क्लब के आधे से अधिक सदस्य शिक्षक हैं। उसी क्लब के आधे से अधिक सदस्य गायक हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some members of the club are both teachers and singers.",
    "Every member of the club is either a teacher or a singer."],
   ["क्लब के कुछ सदस्य शिक्षक और गायक दोनों हैं।",
    "क्लब का हर सदस्य या तो शिक्षक है या गायक।"],
   0,
   "Only I follows. If no member were both, the teachers and the singers would be separate groups, together more than the whole club -- impossible; so some members are both. "
   "II does not follow: with ten members, six teachers and six singers can overlap in four, leaving two members who are neither.",
   "केवल I निकलता है। यदि कोई सदस्य दोनों न होता, तो शिक्षक और गायक अलग-अलग समूह होते, जो मिलकर पूरे क्लब से अधिक होते -- असंभव; इसलिए कुछ सदस्य दोनों हैं। "
   "II नहीं निकलता: दस सदस्यों में छह शिक्षक और छह गायक चार में साझा हो सकते हैं, जिससे दो सदस्य ऐसे बचते हैं जो दोनों में से कुछ नहीं।",
   "lr-sy-more-than-half-twice", roman=True, check=_sy1)

# 17 -- two islanders who give the same answer
def _tl1():
    kinds = []
    for a, b in product((True, False), repeat=2):          # True = always tells the truth
        truth = a or b                                      # 'Is at least one of you a truth-teller?'
        says = lambda honest: truth if honest else not truth
        if says(a) and says(b):                             # both answer 'Yes'
            kinds.append((a, b))
    assert sorted(kinds) == [(False, False), (True, True)]
    return "They are of the same kind, but which kind cannot be told."
T(LR, "Truth-Liar", "hard",
  "On an island every person either always tells the truth or always lies. A visitor asks two islanders, A and B, 'Is at least one of you a truth-teller?' Each of them answers 'Yes.' What can the visitor conclude?",
  "एक द्वीप पर हर व्यक्ति या तो हमेशा सच बोलता है या हमेशा झूठ। एक आगंतुक दो द्वीपवासियों, A और B, से पूछता है, 'क्या तुममें से कम से कम एक सच बोलने वाला है?' दोनों उत्तर देते हैं 'हाँ।' आगंतुक क्या निष्कर्ष निकाल सकता है?",
  ["Both of them tell the truth, since a liar could never have answered 'Yes'.",
   "They are of the same kind, but which kind cannot be told.",
   "Exactly one of them tells the truth, and the other is lying about it.",
   "Both of them are liars, since the question invites a false reply."],
  ["दोनों सच बोलते हैं, क्योंकि कोई झूठा कभी 'हाँ' उत्तर नहीं दे सकता था।",
   "दोनों एक ही प्रकार के हैं, पर कौन-से, यह नहीं बताया जा सकता।",
   "उनमें से ठीक एक सच बोलता है, और दूसरा इस बारे में झूठ बोल रहा है।",
   "दोनों झूठे हैं, क्योंकि प्रश्न ही झूठे उत्तर को न्योता देता है।"],
  1,
  "If exactly one were a truth-teller, the honest answer would be 'Yes' -- so the truth-teller says 'Yes' but the liar says 'No'; they would not agree. If both tell the truth, both say 'Yes'. If both are liars, the honest answer is 'No', so both say 'Yes'. "
  "So their agreement shows only that they are of the same kind: both truthful or both liars, and the question cannot tell which. Each of 'both tell the truth' and 'both are liars' picks one of two possibilities.",
  "यदि ठीक एक सच बोलने वाला होता, तो सच्चा उत्तर 'हाँ' होता -- इसलिए सच बोलने वाला 'हाँ' कहता पर झूठा 'नहीं'; वे सहमत न होते। यदि दोनों सच बोलते हैं, तो दोनों 'हाँ' कहते हैं। यदि दोनों झूठे हैं, तो सच्चा उत्तर 'नहीं' है, इसलिए दोनों 'हाँ' कहते हैं। "
  "अतः उनकी सहमति केवल यह दिखाती है कि वे एक ही प्रकार के हैं: दोनों सच्चे या दोनों झूठे, और प्रश्न से यह पता नहीं चलता कि कौन-से। 'दोनों सच बोलते हैं' और 'दोनों झूठे हैं' दो संभावनाओं में से केवल एक चुनते हैं।",
  "lr-tl-two-islanders-who-give-the-same-answer", pos=1, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    s1 = {f for f in range(1, 6) if f == 3 + 1}          # I: directly above the middle (third) floor
    s2 = {f for f in range(1, 6) if 5 - f == 1}          # II: exactly one floor above hers
    assert s1 == s2 == {4}
    return _ds(s1, s2, s1 & s2)
DS(LR, "medium",
   "A building has five floors, numbered 1 to 5 from the bottom. On which floor does Neha live?",
   "एक भवन में पाँच मंज़िलें हैं, नीचे से 1 से 5 तक क्रमांकित। नेहा किस मंज़िल पर रहती है?",
   "She lives on the floor directly above the middle floor.", "वह बीच वाली मंज़िल के ठीक ऊपर वाली मंज़िल पर रहती है।",
   "Exactly one floor of the building is above hers.", "भवन की ठीक एक मंज़िल उसकी मंज़िल के ऊपर है।",
   1,
   "Statement I: the middle of five floors is the 3rd, so she lives on the 4th -- sufficient. Statement II: only the 5th floor is above hers, so she lives on the 4th -- sufficient. Either statement alone answers the question.",
   "कथन I: पाँच मंज़िलों में बीच वाली तीसरी है, इसलिए वह चौथी पर रहती है -- पर्याप्त। कथन II: उसकी मंज़िल के ऊपर केवल पाँचवीं मंज़िल है, इसलिए वह चौथी पर रहती है -- पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-floor-found-two-ways", _ds1)

def _ds2():
    rows = [r for r in permutations("PQRST")]
    s1 = {r.index("P") < r.index("Q") for r in rows if r[0] == "P"}               # I: P at the west end, i.e. the left end
    s2 = {r.index("P") < r.index("Q") for r in rows if abs(r.index("Q") - r.index("R")) == 1}
    assert s1 == {True} and s2 == {True, False}
    return _ds(s1, s2, s1)
DS(LR, "easy",
   "Five people, P, Q, R, S and T, stand in a row, all facing north. Is P somewhere to the left of Q?",
   "पाँच लोग, P, Q, R, S और T, एक पंक्ति में उत्तर की ओर मुँह करके खड़े हैं। क्या P, Q से कहीं बाईं ओर है?",
   "P stands at the western end of the row.", "P पंक्ति के पश्चिमी छोर पर खड़ा है।",
   "Q stands next to R.", "Q, R के बग़ल में खड़ा है।",
   0,
   "Statement I: facing north, a person's left is the west, so the western end of the row is its left end; P is at the left end, so P is to the left of everyone else, Q included -- sufficient. Statement II says nothing about where P is -- not sufficient. One statement alone answers the question.",
   "कथन I: उत्तर की ओर मुँह होने पर व्यक्ति के बाईं ओर पश्चिम होता है, इसलिए पंक्ति का पश्चिमी छोर उसका बायाँ छोर है; P बाएँ छोर पर है, इसलिए वह Q सहित सबसे बाईं ओर है -- पर्याप्त। कथन II, P की स्थिति के बारे में कुछ नहीं कहता -- पर्याप्त नहीं। एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-left-end-fixed-by-a-compass-point", _ds2)

def _ds3():
    worlds = [(rain, canal) for rain in (True, False) for canal in (True, False)]
    # wet ground on Wednesday morning is given in I; II says wet ground means rain the day before unless the canal overflowed
    s1 = {rain for rain, canal in worlds}                                   # I alone: the ground was wet -- cause unknown
    s2 = {rain for rain, canal in worlds}                                   # II alone: no observation of the ground
    both = {rain for rain, canal in worlds if rain or canal}                # wet ground: rain, or an overflow, or both
    assert both == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Did it rain in the village on Tuesday?",
   "क्या मंगलवार को गाँव में बारिश हुई?",
   "The ground in the village was wet on Wednesday morning.", "बुधवार सुबह गाँव की ज़मीन गीली थी।",
   "The village ground is wet on a morning only if it rained the day before or the canal overflowed during the night.",
   "गाँव की ज़मीन किसी सुबह तभी गीली होती है जब पिछले दिन बारिश हुई हो या रात में नहर उफन गई हो।",
   3,
   "Statement I gives the wet ground but not its cause. Statement II gives the possible causes but no observation. Together they show that it rained on Tuesday or the canal overflowed on Tuesday night -- or both -- but not which. So even together they do not answer the question.",
   "कथन I गीली ज़मीन बताता है पर उसका कारण नहीं। कथन II संभावित कारण बताता है पर कोई अवलोकन नहीं। दोनों साथ दिखाते हैं कि मंगलवार को बारिश हुई या मंगलवार रात नहर उफनी -- या दोनों -- पर यह नहीं कि कौन-सा। अतः दोनों साथ भी प्रश्न का उत्तर नहीं देते।",
   "lr-ds-wet-ground-that-does-not-prove-rain", _ds3)
