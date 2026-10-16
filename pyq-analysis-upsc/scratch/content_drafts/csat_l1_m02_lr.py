# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 2 -- Logical Reasoning (9 items: 8 in the Reasoning slots, 1 in the data-sufficiency block).

The half paper's share of Level 2's Reasoning mix, rotated across the three minis (this one has two arrangement items and
a cube item, and no syllogism or truth-teller item), at the foundation level (3 easy / 5 medium / 1 hard). None of
Level 2's Reasoning shapes or Mini 1's is reused: the flaw in a website's poll of its own readers, the strongest case
against widening a road; who sits where in a car, counting the seatings a row allows; 'her mother's mother is my
daughter'; the shortest walk between two corners of a street grid; a code that numbers the vowels; the fewest colours for
a cube's faces; and, in the data-sufficiency block, a family whose sons and daughters count their brothers and sisters.
The rows are written in the order they take on the paper; arrangement, grid, code, cube and data-sufficiency keys are
found by checking every case."""
from itertools import permutations, product
from csat_common import N, T, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 3 -- the flaw in a website's poll of its own readers
_KEY_POLL = "Those who answered were readers of a news website who chose to reply, unlike the country's adults as a whole."
T(LR, "Statement-Conclusion/Assumption", "easy",
  "A news website asked its readers, 'Do you read a newspaper every day?' Of the 5,000 readers who answered, 80 per cent said yes. The website concluded that about 80 per cent of the country's adults read a newspaper every day. "
  "Which one of the following points out the main flaw in this conclusion?",
  "एक समाचार वेबसाइट ने अपने पाठकों से पूछा, 'क्या आप प्रतिदिन समाचार-पत्र पढ़ते हैं?' उत्तर देने वाले 5,000 पाठकों में से 80 प्रतिशत ने हाँ कहा। वेबसाइट ने निष्कर्ष निकाला कि देश के लगभग 80 प्रतिशत वयस्क प्रतिदिन समाचार-पत्र पढ़ते हैं। "
  "निम्नलिखित में से कौन-सा इस निष्कर्ष की मुख्य त्रुटि बताता है?",
  ["A sample of 5,000 people is far too small to say anything about the habits of any large group of people.",
   _KEY_POLL,
   "Some readers who answered 'yes' may read a newspaper only on weekdays, or may have misremembered how often they read one.",
   "The website did not ask its readers how many minutes a day they spend reading the newspaper."],
  ["5,000 लोगों का नमूना किसी भी बड़े समूह की आदतों के बारे में कुछ कहने के लिए बहुत छोटा है।",
   "उत्तर देने वाले एक समाचार वेबसाइट के वे पाठक थे जिन्होंने स्वयं उत्तर देना चुना, जो देश के सभी वयस्कों जैसे नहीं हैं।",
   "'हाँ' कहने वाले कुछ पाठक शायद केवल कार्यदिवसों पर समाचार-पत्र पढ़ते हों, या उन्हें ठीक याद न हो कि वे कितनी बार पढ़ते हैं।",
   "वेबसाइट ने अपने पाठकों से यह नहीं पूछा कि वे प्रतिदिन कितने मिनट समाचार-पत्र पढ़ते हैं।"], 1,
  "The people who answered were readers of a news website, and only those who chose to reply. Such people are more likely than most adults to read news every day, so they are not a fair picture of the country's adults -- that is the main flaw. "
  "5,000 is not too small a number for a well-chosen sample; the trouble is who was asked, not how many. A few readers who misremember would change the figure a little, not the reasoning; and the minutes spent reading have nothing to do with whether people read every day.",
  "उत्तर देने वाले एक समाचार वेबसाइट के पाठक थे, और वे भी केवल वे जिन्होंने उत्तर देना चुना। ऐसे लोग अधिकतर वयस्कों की तुलना में प्रतिदिन समाचार पढ़ने की अधिक संभावना रखते हैं, इसलिए वे देश के वयस्कों का उचित चित्र नहीं हैं -- यही मुख्य त्रुटि है। "
  "ठीक से चुने गए नमूने के लिए 5,000 बहुत छोटी संख्या नहीं है; समस्या यह है कि किससे पूछा गया, यह नहीं कि कितनों से। कुछ पाठकों की ग़लत याद आँकड़े को थोड़ा बदलेगी, तर्क को नहीं; और पढ़ने में लगे मिनटों का इससे कोई संबंध नहीं कि लोग प्रतिदिन पढ़ते हैं या नहीं।",
  "lr-sc-a-website-s-poll-of-its-own-readers", pos=1)

# 9 -- the shortest walk between two corners of a street grid
_KEY_GRID = "800 m, to the south-east"
def _grid():
    asha, bala = (3, 7), (8, 4)            # (street, avenue): streets numbered west to east, avenues south to north
    east, north = bala[0] - asha[0], bala[1] - asha[1]
    assert (east, north) == (5, -3)
    walk = 100 * (abs(east) + abs(north))
    straight = round(100 * (east ** 2 + north ** 2) ** 0.5)
    assert walk == 800 and straight == 583
    return f"{walk} m, to the {'south' if north < 0 else 'north'}-{'east' if east > 0 else 'west'}"
T(LR, "Direction & Distance", "medium",
  "In a town, the streets run north-south and are numbered 1st, 2nd, 3rd ... from west to east; the avenues run east-west and are numbered 1st, 2nd, 3rd ... from south to north. Every block is 100 m long. "
  "Asha lives at the corner of 3rd Street and 7th Avenue, and Bala at the corner of 8th Street and 4th Avenue. Walking only along the streets and avenues, how far is the shortest walk from Asha's home to Bala's, "
  "and in which direction does Bala's home lie from Asha's?",
  "एक कस्बे में गलियाँ उत्तर-दक्षिण दिशा में चलती हैं और पश्चिम से पूर्व की ओर गली 1, गली 2, गली 3 ... क्रमांकित हैं; मार्ग पूर्व-पश्चिम दिशा में चलते हैं और दक्षिण से उत्तर की ओर मार्ग 1, मार्ग 2, मार्ग 3 ... क्रमांकित हैं। हर खंड 100 मी लंबा है। "
  "आशा गली 3 और मार्ग 7 के कोने पर रहती है, और बाला गली 8 और मार्ग 4 के कोने पर। केवल गलियों और मार्गों पर चलते हुए आशा के घर से बाला के घर तक सबसे छोटा पैदल रास्ता कितना लंबा है, "
  "और बाला का घर आशा के घर से किस दिशा में है?",
  ["800 m, to the north-east", "583 m, to the south-east", "1,500 m, to the south-east", _KEY_GRID],
  ["800 मी, उत्तर-पूर्व में", "583 मी, दक्षिण-पूर्व में", "1,500 मी, दक्षिण-पूर्व में", "800 मी, दक्षिण-पूर्व में"], 3,
  "Bala's street, 8th, is 5 streets east of Asha's 3rd; Bala's avenue, 4th, is 3 avenues south of Asha's 7th, because avenues are numbered from south to north. The shortest walk along the grid is 5 + 3 = 8 blocks, or 800 m, "
  "and Bala's home lies to the south-east. North-east reads the avenues as numbered from north to south; 583 m is the straight-line distance, which cannot be walked along the streets; 1,500 m adds the street and avenue numbers (8 + 7) instead of their differences.",
  "बाला की गली 8, आशा की गली 3 से 5 गली पूर्व में है; बाला का मार्ग 4, आशा के मार्ग 7 से 3 मार्ग दक्षिण में है, क्योंकि मार्ग दक्षिण से उत्तर की ओर क्रमांकित हैं। ग्रिड पर सबसे छोटा रास्ता 5 + 3 = 8 खंड, यानी 800 मी है, "
  "और बाला का घर दक्षिण-पूर्व में है। उत्तर-पूर्व, मार्गों को उत्तर से दक्षिण की ओर क्रमांकित मान लेता है; 583 मी सीधी रेखा की दूरी है, जिस पर गलियों से होकर नहीं चला जा सकता; 1,500 मी गली और मार्ग की संख्याओं को (8 + 7) जोड़ता है, उनके अंतर नहीं लेता।",
  "lr-dd-the-shortest-walk-on-a-street-grid", pos=3, check=_grid)

# 15 -- 'her mother's mother is my daughter'
_KEY_BR = "Great-grandfather"
def _br():
    parent = {"Meena": "M", "M": "G", "G": "Ravi"}        # Meena's mother M, M's mother G, and G is Ravi's daughter
    chain, p = [], "Meena"
    while p in parent:
        p = parent[p]
        chain.append(p)
    assert chain.index("Ravi") == 2                        # three generations up: a great-grandparent, and Ravi is a man
    return _KEY_BR
T(LR, "Blood Relation", "medium",
  "Ravi, a man, says, 'Meena's mother's mother is my daughter.' How is Ravi related to Meena?",
  "रवि, जो एक पुरुष है, कहता है, 'मीना की माँ की माँ मेरी बेटी है।' रवि का मीना से क्या संबंध है?",
  [_KEY_BR, "Maternal grandfather", "Great-grandson", "Father-in-law"],
  ["परनाना", "नाना", "परनाती", "ससुर"], 0,
  "Meena's mother's mother is Meena's grandmother, and she is Ravi's daughter. Ravi is therefore the father of Meena's grandmother: one generation above a grandparent, Meena's great-grandfather (on her mother's side). "
  "Maternal grandfather stops a generation short -- that is the father of Meena's mother. Great-grandson runs the relation the wrong way, and father-in-law would need a marriage that the statement does not mention.",
  "मीना की माँ की माँ, मीना की नानी है, और वह रवि की बेटी है। अतः रवि मीना की नानी के पिता हैं: नाना-नानी से एक पीढ़ी ऊपर, यानी मीना के परनाना (माँ की ओर से)। "
  "नाना एक पीढ़ी पहले रुक जाता है -- वे मीना की माँ के पिता होते हैं। परनाती संबंध को उलटी दिशा में ले जाता है, और ससुर के लिए किसी ऐसे विवाह की आवश्यकता होगी जिसका कथन में उल्लेख नहीं है।",
  "lr-br-her-mother-s-mother-is-my-daughter", pos=3, check=_br)

# 18 -- counting the seatings a row allows
def _count():
    rows = [p for p in permutations("PQRST")
            if abs(p.index("P") - p.index("Q")) == 1 and p.index("R") not in (0, 4)]
    adjacent = sum(1 for p in permutations("PQRST") if abs(p.index("P") - p.index("Q")) == 1)
    assert adjacent == 48 and adjacent - len(rows) == 24
    return str(len(rows))
N(LR, "Seating Arrangement", "hard",
  "In how many different ways can five friends -- P, Q, R, S and T -- sit in a row of five chairs, if P and Q must sit next to each other and R must not sit on either of the two end chairs?",
  "पाँच मित्र -- P, Q, R, S और T -- पाँच कुर्सियों की एक पंक्ति में कितने अलग-अलग प्रकार से बैठ सकते हैं, यदि P और Q को एक-दूसरे के बगल में बैठना है और R को दोनों सिरों की कुर्सियों में से किसी पर नहीं बैठना है?",
  ["12", "24", "36", "48"], 1,
  "Treat P and Q as one block: the block, R, S and T can be arranged in 4! = 24 ways, and P and Q can swap within the block, so 48 seatings keep P and Q together. "
  "In 12 of these R takes the left-end chair (the other three units in 3! = 6 orders, times 2 for P and Q), and in another 12 R takes the right-end chair. That leaves 48 - 24 = 24 seatings. "
  "48 ignores the rule about R; 36 removes only one end; 12 forgets that P and Q can change places.",
  "P और Q को एक खंड मानिए: खंड, R, S और T को 4! = 24 प्रकार से रखा जा सकता है, और खंड के भीतर P और Q जगह बदल सकते हैं, इसलिए 48 व्यवस्थाओं में P और Q साथ रहते हैं। "
  "इनमें से 12 में R बाएँ सिरे की कुर्सी पर है (बाक़ी तीन इकाइयाँ 3! = 6 क्रमों में, P और Q के लिए 2 से गुणा), और अन्य 12 में दाएँ सिरे की कुर्सी पर। बचती हैं 48 - 24 = 24 व्यवस्थाएँ। "
  "48, R वाले नियम की अनदेखी करता है; 36 केवल एक सिरा घटाता है; 12 यह भूल जाता है कि P और Q जगह बदल सकते हैं।",
  "lr-sa-counting-the-seatings-a-row-allows", _count)

# 23 -- a code that numbers the vowels
def _code():
    ex = {"PAINT": "P13NT", "HOUSE": "H45S2"}
    rule = {}
    for w, v in ex.items():
        for a, b in zip(w, v):
            if a != b:
                assert rule.setdefault(a, b) == b
            else:
                assert a not in "AEIOU"
    assert rule == {"A": "1", "I": "3", "O": "4", "U": "5", "E": "2"}
    return "".join(rule.get(ch, ch) for ch in "QUIET")
T(LR, "Coding-Decoding", "easy",
  "In a certain code, PAINT is written as P13NT and HOUSE is written as H45S2. How will QUIET be written in that code?",
  "एक निश्चित कूट भाषा में PAINT को P13NT और HOUSE को H45S2 लिखा जाता है। उसी कूट भाषा में QUIET को कैसे लिखा जाएगा?",
  ["Q523T", "Q532T", "Q352T", "Q5I2T"], ["Q523T", "Q532T", "Q352T", "Q5I2T"], 1,
  "The consonants stay as they are and each vowel becomes a number: from PAINT, A = 1 and I = 3; from HOUSE, O = 4, U = 5 and E = 2 -- the vowels numbered in the order A, E, I, O, U. "
  "QUIET has the vowels U, I and E in that order, so it becomes Q-5-3-2-T, that is, Q532T. Q523T swaps the codes for I and E, Q352T swaps those for U and I, and Q5I2T leaves the I uncoded.",
  "व्यंजन वैसे ही रहते हैं और हर स्वर एक संख्या बन जाता है: PAINT से A = 1 और I = 3; HOUSE से O = 4, U = 5 और E = 2 -- यानी स्वर A, E, I, O, U के क्रम में क्रमांकित हैं। "
  "QUIET में स्वर इसी क्रम में U, I और E हैं, इसलिए वह Q-5-3-2-T, यानी Q532T बनता है। Q523T, I और E के कूट आपस में बदल देता है, Q352T, U और I के, और Q5I2T, I को कूट में नहीं बदलता।",
  "lr-cd-a-code-that-numbers-the-vowels", pos=1, check=_code)

# 31 -- who sits where in a car
_KEY_CAR = "Chetan"
def _car():
    seats = ["front-right", "front-left", "back-right", "back-left"]      # front-right is the driver's seat in an Indian car
    behind = {"back-right": "front-right", "back-left": "front-left"}
    diag = {"front-right": "back-left", "back-left": "front-right", "front-left": "back-right", "back-right": "front-left"}
    sols = []
    for order in permutations(["Anu", "Bela", "Chetan", "Dev"]):
        s = dict(zip(seats, order))
        where = {v: k for k, v in s.items()}
        if (where["Chetan"] == "front-right" and not where["Anu"].startswith("front")
                and behind.get(where["Dev"]) == where["Chetan"]):
            sols.append(s[diag[where["Anu"]]])
    assert sols == [_KEY_CAR]
    return sols[0]
T(LR, "Seating Arrangement", "medium",
  "Four friends -- Anu, Bela, Chetan and Dev -- travel in a car that has two seats in front and two at the back. As in Indian cars, the driver's seat is on the front right. Chetan is the driver. "
  "Anu is not in a front seat. Dev sits directly behind Chetan. Who sits diagonally opposite Anu?",
  "चार मित्र -- अनु, बेला, चेतन और देव -- एक कार में यात्रा कर रहे हैं जिसमें दो सीटें आगे और दो पीछे हैं। भारतीय कारों की तरह चालक की सीट आगे दाईं ओर है। चेतन चालक है। "
  "अनु आगे की किसी सीट पर नहीं है। देव ठीक चेतन के पीछे है। अनु के ठीक तिरछे सामने (विकर्ण पर) कौन है?",
  ["Bela", _KEY_CAR, "Dev", "Cannot be determined"],
  ["बेला", "चेतन", "देव", "निर्धारित नहीं किया जा सकता"], 1,
  "Chetan, the driver, is in the front-right seat. Dev sits directly behind Chetan, in the back-right seat. Anu is not in front, so Anu takes the back-left seat, and Bela the front-left. "
  "The seat diagonally opposite the back-left is the front-right, which is Chetan's. Bela is directly in front of Anu, not diagonally opposite; Dev is beside Anu; and the seating is fully fixed, so the answer can be determined.",
  "चालक चेतन आगे दाईं सीट पर है। देव ठीक चेतन के पीछे, पीछे की दाईं सीट पर है। अनु आगे नहीं है, इसलिए अनु पीछे की बाईं सीट पर है, और बेला आगे की बाईं सीट पर। "
  "पीछे की बाईं सीट के विकर्ण पर आगे की दाईं सीट है, जो चेतन की है। बेला अनु के ठीक आगे है, विकर्ण पर नहीं; देव अनु के बगल में है; और बैठने की व्यवस्था पूरी तरह तय है, इसलिए उत्तर निर्धारित किया जा सकता है।",
  "lr-sa-who-sits-where-in-a-car", pos=1, check=_car)

# 36 -- the strongest case against widening a road
_KEY_ROAD = "In other cities, widened roads soon filled up again, as the extra space drew more people to drive on them."
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A city plans to end the traffic jams on its busiest road by widening it from four lanes to six. Which one of the following, if true, most seriously weakens the case for the plan?",
  "एक शहर अपनी सबसे व्यस्त सड़क को चार लेन से छह लेन चौड़ा करके उस पर लगने वाले जाम समाप्त करने की योजना बनाता है। निम्नलिखित में से कौन-सा, यदि सत्य हो, इस योजना के पक्ष को सबसे गंभीर रूप से कमज़ोर करता है?",
  [_KEY_ROAD,
   "Widening the road will take two years, during which the traffic on it will move even more slowly than now.",
   "Most of the vehicles on the road at peak hours are cars carrying only one or two people each.",
   "The city's other main roads are also crowded at peak hours, though not as badly as this one, according to a recent survey."],
  ["दूसरे शहरों में चौड़ी की गई सड़कें जल्द ही फिर भर गईं, क्योंकि अतिरिक्त जगह ने अधिक लोगों को उन पर गाड़ी चलाने के लिए खींचा।",
   "सड़क को चौड़ा करने में दो वर्ष लगेंगे, जिनके दौरान उस पर यातायात अभी से भी धीमा चलेगा।",
   "व्यस्त घंटों में सड़क पर चलने वाले अधिकांश वाहन ऐसी कारें हैं जिनमें केवल एक या दो लोग होते हैं।",
   "एक हाल के सर्वेक्षण के अनुसार शहर की दूसरी मुख्य सड़कें भी व्यस्त घंटों में भीड़भाड़ वाली रहती हैं, हालाँकि इस सड़क जितनी नहीं।"], 0,
  "The plan assumes that more lanes will carry the same traffic more freely. If, elsewhere, widened roads soon filled up again because the extra space drew more drivers, the jams are likely to return -- this strikes at the plan's very aim. "
  "Two years of slower traffic during the work is a temporary cost, not a reason the plan would fail; cars carrying one or two people say nothing about whether more lanes will help; and crowding on other roads does not touch this road's plan.",
  "योजना मानती है कि अधिक लेन वही यातायात अधिक सुगमता से ले जाएँगी। यदि दूसरी जगहों पर चौड़ी की गई सड़कें जल्द फिर भर गईं क्योंकि अतिरिक्त जगह ने अधिक चालकों को खींचा, तो जाम लौटने की संभावना है -- यह योजना के मूल उद्देश्य पर ही चोट करता है। "
  "काम के दौरान दो वर्ष का धीमा यातायात एक अस्थायी क़ीमत है, योजना के विफल होने का कारण नहीं; एक या दो लोगों वाली कारें यह कुछ नहीं बतातीं कि अधिक लेन से लाभ होगा या नहीं; और दूसरी सड़कों की भीड़ इस सड़क की योजना को नहीं छूती।",
  "lr-sc-the-case-against-widening-a-road", pos=0)

# 39 -- the fewest colours for a cube's faces
def _colours():
    opp = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}             # faces 0-5 in opposite pairs; every other pair shares an edge
    ok = lambda col: all(col[a] != col[b] for a in range(6) for b in range(6) if a < b and opp[a] != b)
    least = next(k for k in range(1, 7) if any(ok(col) for col in product(range(k), repeat=6)))
    return str(least)
N(LR, "Cube Painting", "easy",
  "What is the least number of colours needed to paint the six faces of a cube so that no two faces that share an edge have the same colour?",
  "किसी घन के छह फलकों को रंगने के लिए कम से कम कितने रंगों की आवश्यकता है, ताकि एक किनारा साझा करने वाले किन्हीं दो फलकों का रंग एक न हो?",
  ["2", "3", "4", "6"], 1,
  "Each face shares an edge with four others and is opposite just one. Three faces that meet at a corner all touch one another, so at least 3 colours are needed; and 3 are enough, because each pair of opposite faces, which never touch, can share a colour. "
  "2 colours would force two faces at a corner to match; 4 or 6 colours work but are more than needed.",
  "हर फलक चार अन्य फलकों से एक किनारा साझा करता है और केवल एक के सामने होता है। किसी कोने पर मिलने वाले तीन फलक एक-दूसरे को छूते हैं, इसलिए कम से कम 3 रंग चाहिए; और 3 पर्याप्त हैं, क्योंकि आमने-सामने के फलकों का हर जोड़ा, जो कभी नहीं छूता, एक ही रंग ले सकता है। "
  "2 रंगों से किसी कोने के दो फलक एक रंग के हो जाएँगे; 4 या 6 रंग चलते हैं पर आवश्यकता से अधिक हैं।",
  "lr-cp-the-fewest-colours-for-a-cube-s-faces", _colours)

# ---- the data-sufficiency block's Reasoning item
def _ds1():
    worlds = [(b, g) for b in range(0, 30) for g in range(0, 30)]           # b sons, g daughters
    i = lambda b, g: g >= 1 and b == g - 1                                   # each daughter: as many brothers as sisters
    ii = lambda b, g: b >= 1 and g == 2 * (b - 1)                            # each son: twice as many sisters as brothers
    s1 = [b + g for b, g in worlds if i(b, g)]
    s2 = [b + g for b, g in worlds if ii(b, g)]
    both = [b + g for b, g in worlds if i(b, g) and ii(b, g)]
    assert both == [7]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "How many children do Mr and Mrs Rao have?",
   "श्री और श्रीमती राव की कितनी संतानें हैं?",
   "Each of their daughters has as many brothers as sisters.",
   "उनकी हर बेटी के जितने भाई हैं, उतनी ही बहनें हैं।",
   "Each of their sons has twice as many sisters as brothers.",
   "उनके हर बेटे की बहनें उसके भाइयों की दुगुनी हैं।",
   2,
   "Let there be s sons and d daughters. Statement I: a daughter has s brothers and d - 1 sisters, so s = d - 1 -- this fits 1 son and 2 daughters, 2 sons and 3 daughters, and so on: not sufficient. "
   "Statement II: a son has d sisters and s - 1 brothers, so d = 2(s - 1) -- this too fits many families: not sufficient. Together, d = 2(d - 2), so d = 4 and s = 3: seven children. Both statements together answer the question; neither does alone.",
   "मान लीजिए s बेटे और d बेटियाँ हैं। कथन I: एक बेटी के s भाई और d - 1 बहनें हैं, अतः s = d - 1 -- यह 1 बेटे और 2 बेटियों, 2 बेटों और 3 बेटियों आदि सबमें बैठता है: पर्याप्त नहीं। "
   "कथन II: एक बेटे की d बहनें और s - 1 भाई हैं, अतः d = 2(s - 1) -- यह भी अनेक परिवारों में बैठता है: पर्याप्त नहीं। दोनों साथ: d = 2(d - 2), अतः d = 4 और s = 3: सात संतानें। दोनों कथन साथ मिलकर उत्तर देते हैं; कोई भी अकेले नहीं।",
   "lr-ds-sons-and-daughters-count-their-siblings", check=_ds1)
