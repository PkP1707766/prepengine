# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 4 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Level 3's harder mix (2 easy / 7 medium / 9 hard), with none of the shapes of Level 2 Tests 1-7, Level 1 Minis 1-3 or
Level 3 Tests 1-3: a team of stars taken for a star team, a heart unit whose death rate rose, 'unless' read as 'if and
only if'; birthdays in five months, six boxes in a stack, seven students split into two groups; a mother-in-law traced
through a maternal grandfather, a woman's 'father's only son'; the way back after a walk that turns back, a leg of a
walk found from the final distance; a code that sorts letters, a digit code found from two examples; a
painted cube counted back from its unpainted cubes; 'no' with 'some'; two people who lie on different days; and in
the data-sufficiency block a speaker who cannot be telling the truth, a light coin found two ways, and a definite
'no' from two directions. Arrangement, relation, code, cube, syllogism and truth-teller keys are found by checking
every case."""
from itertools import combinations, permutations, product
import csat_common as c
from csat_common import N, T, S2, SC, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a team of stars taken for a star team
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'Every player in our team is the best in the country in his or her position. So ours must be the best team in the country.' Which one of the following best describes the flaw in this argument?",
  "'हमारी टीम का हर खिलाड़ी अपने स्थान पर देश में सर्वश्रेष्ठ है। इसलिए हमारी टीम देश की सर्वश्रेष्ठ टीम होनी चाहिए।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It assumes that what is true of each member must be true of the team as a whole.",
   "It judges all the players in the country from a small sample of players it happens to know.",
   "It treats the boasts of the team's own supporters as though they were evidence.",
   "It assumes that a team that was the best in the past must still be the best today."],
  ["यह मान लेता है कि जो हर सदस्य के बारे में सत्य है, वह पूरी टीम के बारे में भी सत्य होगा।",
   "यह देश के सभी खिलाड़ियों का आकलन उन कुछ खिलाड़ियों के छोटे नमूने से करता है जिन्हें वह जानता है।",
   "यह टीम के अपने समर्थकों की डींगों को ऐसे लेता है मानो वे प्रमाण हों।",
   "यह मान लेता है कि जो टीम अतीत में सर्वश्रेष्ठ थी, वह आज भी सर्वश्रेष्ठ ही होगी।"],
  0,
  "The argument moves from a property of each part (each player is the best in his or her position) to the same property of the whole (the team is the best). But a team's strength also depends on how its players combine -- whether they understand one another's play, whether the side is balanced, how it is led -- so a side of individual stars can lose to a better-knit team. "
  "This is the error of reasoning from the parts to the whole. The argument draws on no sample of players, cites no supporters and says nothing about the past.",
  "तर्क हर भाग के एक गुण (हर खिलाड़ी अपने स्थान पर सर्वश्रेष्ठ है) से पूरे के उसी गुण (टीम सर्वश्रेष्ठ है) पर पहुँच जाता है। पर टीम की शक्ति इस पर भी निर्भर है कि खिलाड़ी आपस में कैसे जुड़ते हैं -- क्या वे एक-दूसरे का खेल समझते हैं, क्या टीम संतुलित है, उसका नेतृत्व कैसा है -- इसलिए अलग-अलग सितारों की टीम किसी बेहतर तालमेल वाली टीम से हार सकती है। "
  "यह भागों से पूरे के बारे में तर्क करने की भूल है। तर्क खिलाड़ियों का कोई नमूना नहीं लेता, किसी समर्थक का उल्लेख नहीं करता और अतीत के बारे में कुछ नहीं कहता।",
  "lr-sc-a-team-of-stars-taken-for-a-star-team", pos=3)

# 2 -- a heart unit whose death rate rose
T(LR, "Statement-Conclusion/Assumption", "hard",
  "After a district hospital opened a specialised heart unit with the latest equipment and trained staff, the proportion of its heart patients who died went up. Which one of the following, if true, best explains this?",
  "एक ज़िला अस्पताल में नवीनतम उपकरणों और प्रशिक्षित कर्मचारियों वाली एक विशेष हृदय इकाई खुलने के बाद, उसके हृदय रोगियों में मरने वालों का अनुपात बढ़ गया। निम्नलिखित में से कौन-सा, यदि सत्य हो, इसकी सबसे अच्छी व्याख्या करता है?",
  ["Since the unit opened, doctors across the region have been sending their most serious heart cases to it.",
   "The new equipment was bought from the same firm that supplies several of the largest hospitals in the cities.",
   "Heart disease has become more common in the district over the same period, as diets and habits have changed.",
   "Several of the unit's doctors trained at some of the most highly regarded medical colleges in the country."],
  ["इकाई खुलने के बाद से क्षेत्र भर के डॉक्टर हृदय के सबसे गंभीर मरीज़ उसी के पास भेज रहे हैं।",
   "नए उपकरण उसी कंपनी से ख़रीदे गए जो शहरों के कई सबसे बड़े अस्पतालों को उपकरण देती है।",
   "इसी अवधि में ज़िले में बदलते खान-पान और आदतों के कारण हृदय रोग पहले की तुलना में कहीं अधिक आम हो गया है।",
   "इकाई के कई डॉक्टरों ने देश के कुछ सबसे प्रतिष्ठित मेडिकल कॉलेजों में प्रशिक्षण पाया है।"],
  0,
  "The puzzle is that better care seems to have produced worse results. It dissolves if the patients changed: once the unit opened, the sickest heart patients from a wide area were sent there, so the hospital's heart patients as a group became far more seriously ill. A higher share of deaths among much sicker patients is consistent with the unit doing good work, and each patient may have a better chance than before. "
  "A general rise in heart disease would raise the number of patients, not by itself the share who die; the firm that supplied the equipment explains nothing; and well-trained doctors make the puzzle sharper rather than solving it.",
  "पहेली यह है कि बेहतर देखभाल से परिणाम बदतर हुए लगते हैं। यह सुलझ जाती है यदि मरीज़ बदल गए हों: इकाई खुलने के बाद एक बड़े क्षेत्र के सबसे गंभीर हृदय रोगी वहाँ भेजे गए, इसलिए अस्पताल के हृदय रोगी समूह के रूप में कहीं अधिक गंभीर रूप से बीमार हो गए। कहीं अधिक बीमार मरीज़ों में मौतों का ऊँचा अनुपात इस बात से मेल खाता है कि इकाई अच्छा काम कर रही है, और हर मरीज़ का बचने का अवसर पहले से बेहतर हो सकता है। "
  "हृदय रोग में सामान्य वृद्धि से मरीज़ों की संख्या बढ़ेगी, अपने आप मरने वालों का अनुपात नहीं; उपकरण देने वाली कंपनी कुछ नहीं समझाती; और अच्छे प्रशिक्षित डॉक्टर पहेली को सुलझाने के बजाय और तीखा बना देते हैं।",
  "lr-sc-a-heart-unit-whose-death-rate-rose", pos=0)

# 3 -- 'unless' read as 'if and only if'
def _sc3():
    worlds = [(rain, open_) for rain in (True, False) for open_ in (True, False) if rain or open_]   # no rain -> open ground
    must = [all(r or o for r, o in worlds), all(not (r and o) for r, o in worlds), all(o or r for r, o in worlds)]
    assert must == [True, False, True]
    return "1 and 3 only"
SC(LR, "Statement-Conclusion/Assumption", "hard",
   "Statement: 'The festival will be held in the open ground unless it rains.'\n\nIf the statement is true, which of the following must also be true?",
   "कथन: 'उत्सव खुले मैदान में होगा, जब तक कि बारिश न हो।'\n\nयदि कथन सत्य है, तो निम्नलिखित में से कौन-सा/से भी अवश्य सत्य है/हैं?",
   ["If it does not rain, the festival is held in the open ground.",
    "If it rains, the festival is not held in the open ground.",
    "If the festival is not held in the open ground, it rained."],
   ["यदि बारिश नहीं होती, तो उत्सव खुले मैदान में होता है।",
    "यदि बारिश होती है, तो उत्सव खुले मैदान में नहीं होता।",
    "यदि उत्सव खुले मैदान में नहीं हुआ, तो बारिश हुई थी।"],
   ["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], 1,
   "'A unless B' means 'if not B, then A': the statement promises the open ground on any day without rain, which is 1. Statement 3 says the same thing turned round -- if the festival has moved off the open ground, the condition for the open ground must have failed, so it rained -- and so it must be true as well. "
   "Statement 2 reads 'unless' as 'if and only if'. The statement makes no promise about a rainy day: the organisers may still hold the festival in the open ground in the rain, so 2 need not be true.",
   "'A, जब तक कि B न हो' का अर्थ है 'यदि B नहीं, तो A': कथन बिना बारिश वाले किसी भी दिन खुले मैदान का वादा करता है, जो 1 है। कथन 3 यही बात उलटकर कहता है -- यदि उत्सव खुले मैदान से हट गया, तो खुले मैदान की शर्त विफल हुई होगी, यानी बारिश हुई -- इसलिए वह भी अवश्य सत्य है। "
   "कथन 2, 'जब तक कि ... न' को 'यदि और केवल यदि' पढ़ लेता है। कथन बारिश वाले दिन के बारे में कोई वादा नहीं करता: आयोजक बारिश में भी उत्सव खुले मैदान में कर सकते हैं, इसलिए 2 का सत्य होना आवश्यक नहीं।",
   "lr-sc-unless-read-as-if-and-only-if", check=_sc3)

# 4 -- birthdays in five months
def _sa1():
    months = ["Feb", "Apr", "Jul", "Sep", "Dec"]
    sols = []
    for p in permutations(months):
        a = dict(zip("PQRST", p))
        i = {k: months.index(v) for k, v in a.items()}
        if i["R"] < i["Q"] < i["T"] and a["S"] in ("Jul", "Dec") and i["S"] < i["T"] and i["P"] >= 2 and a["T"] not in ("Jul", "Dec"):
            sols.append(a)
    assert sols == [{"P": "Dec", "Q": "Apr", "R": "Feb", "S": "Jul", "T": "Sep"}]
    return next(k for k, v in sols[0].items() if v == "Jul")
N(LR, "Seating Arrangement", "medium",
  "Five friends, P, Q, R, S and T, have their birthdays in five different months of the year: February, April, July, September and December. R's birthday comes earlier in the year than Q's, and Q's earlier than T's. S was born in a month that has 31 days, and earlier in the year than T. "
  "P was born in the second half of the year, and T in a month that does not have 31 days. Whose birthday is in July?",
  "पाँच मित्रों, P, Q, R, S और T, के जन्मदिन वर्ष के पाँच अलग-अलग महीनों में हैं: फ़रवरी, अप्रैल, जुलाई, सितंबर और दिसंबर। R का जन्मदिन वर्ष में Q से पहले आता है, और Q का T से पहले। S का जन्म ऐसे महीने में हुआ जिसमें 31 दिन होते हैं, और वर्ष में T से पहले। "
  "P का जन्म वर्ष के उत्तरार्ध में हुआ, और T का ऐसे महीने में जिसमें 31 दिन नहीं होते। किसका जन्मदिन जुलाई में है?",
  ["P", "Q", "S", "T"], 2,
  "Of the five months only July and December have 31 days. T's month has fewer, so T is in February, April or September; and since R and Q both come before T, T is in September. S has a 31-day month earlier than T's, so S is in July -- and P, born in the second half of the year, takes the remaining December. R and Q take February and April, in that order. "
  "So R: February, Q: April, S: July, T: September, P: December. P is the tempting answer for anyone who forgets that S must come before T.",
  "पाँच महीनों में केवल जुलाई और दिसंबर में 31 दिन होते हैं। T के महीने में कम दिन हैं, इसलिए T फ़रवरी, अप्रैल या सितंबर में है; और चूँकि R और Q दोनों T से पहले आते हैं, T सितंबर में है। S का महीना 31 दिनों वाला है और T से पहले, इसलिए S जुलाई में है -- और P, जिसका जन्म वर्ष के उत्तरार्ध में हुआ, बचा हुआ दिसंबर लेता है। R और Q उसी क्रम में फ़रवरी और अप्रैल लेते हैं। "
  "अतः R: फ़रवरी, Q: अप्रैल, S: जुलाई, T: सितंबर, P: दिसंबर। जो यह भूल जाए कि S को T से पहले आना है, उसके लिए P लुभावना उत्तर है।",
  "lr-sa-birthdays-in-five-months", _sa1)

# 5 -- six boxes in a stack
def _sa2():
    sols = []
    for p in permutations(range(1, 7)):                  # 1 = bottom, 6 = top
        a = dict(zip("PQRSTU", p))
        if abs(a["Q"] - a["T"]) == 3 and a["R"] == a["P"] + 1 and a["P"] != 1 and a["U"] not in (1, 6) and a["Q"] < a["S"] < a["T"]:
            sols.append(a)
    below = {next(k for k, v in a.items() if v == a["P"] - 1) for a in sols}
    assert len(sols) == 2 and len(below) == 1
    return below.pop()
N(LR, "Seating Arrangement", "medium",
  "Six boxes, P, Q, R, S, T and U, are stacked one on top of another. Exactly two boxes are between Q and T. R is directly on top of P, and P is not at the bottom. U is neither at the top nor at the bottom. S is above Q but below T. Which box is directly below P?",
  "छह बक्से, P, Q, R, S, T और U, एक के ऊपर एक रखे हैं। Q और T के बीच ठीक दो बक्से हैं। R सीधे P के ऊपर है, और P सबसे नीचे नहीं है। U न सबसे ऊपर है न सबसे नीचे। S, Q से ऊपर पर T से नीचे है। P के ठीक नीचे कौन-सा बक्सा है?",
  ["Q", "R", "S", "T"], 3,
  "S is above Q and below T, so Q is the lower of the two, and counting from the bottom Q and T are at 1 and 4, 2 and 5, or 3 and 6. S must lie between them, and P and R need two adjacent free places with P not at the bottom. With Q at 2 and T at 5, the only adjacent free pair is 3-4, which S needs. With Q at 3 and T at 6, the free pairs are 1-2 (P at the bottom) and 4-5 (needed by S). "
  "So Q is at 1 and T at 4; S and U take 2 and 3 in some order, and P and R take 5 and 6, R on top. The box directly below P is T; the order of S and U is not fixed, but it does not affect the answer.",
  "S, Q से ऊपर और T से नीचे है, इसलिए दोनों में Q नीचे है, और नीचे से गिनने पर Q और T, 1 और 4, 2 और 5, या 3 और 6 पर हैं। S को उनके बीच होना है, और P और R को दो सटे हुए ख़ाली स्थान चाहिए, P सबसे नीचे न हो। Q के 2 और T के 5 पर होने पर एकमात्र सटा ख़ाली जोड़ा 3-4 है, जो S को चाहिए। Q के 3 और T के 6 पर होने पर ख़ाली जोड़े 1-2 (P सबसे नीचे) और 4-5 (S को चाहिए) हैं। "
  "अतः Q, 1 पर और T, 4 पर है; S और U किसी क्रम में 2 और 3 लेते हैं, और P और R, 5 और 6 लेते हैं, R ऊपर। P के ठीक नीचे T है; S और U का क्रम तय नहीं, पर उससे उत्तर पर कोई असर नहीं पड़ता।",
  "lr-sa-six-boxes-in-a-stack", _sa2)

# 6 -- seven students split into two groups
def _sa3():
    reds = [set(r) for r in combinations("ABCDEFG", 3)
            if ("A" in r) != ("B" in r) and ("C" in r) == ("D" in r) and not {"E", "F"} <= set(r) and "G" not in r]
    claims = {"C is in the Red group.": all("C" in r for r in reds),
              "A is in the Red group.": all("A" in r for r in reds),
              "E is in the Red group.": all("E" in r for r in reds),
              "B and F are in the same group.": all(("B" in r) == ("F" in r) for r in reds)}
    must = [k for k, v in claims.items() if v]
    assert len(reds) == 2 and must == ["C is in the Red group."]
    return must[0]
T(LR, "Seating Arrangement", "hard",
  "Seven students, A, B, C, D, E, F and G, are divided into two groups: Red, with three students, and Blue, with four. A and B are in different groups. C and D are in the same group. E and F are not both in Red. G is in Blue. Which one of the following must be true?",
  "सात विद्यार्थियों, A, B, C, D, E, F और G, को दो समूहों में बाँटा जाता है: लाल, जिसमें तीन विद्यार्थी हैं, और नीला, जिसमें चार। A और B अलग-अलग समूहों में हैं। C और D एक ही समूह में हैं। E और F दोनों लाल में नहीं हैं। G नीले में है। निम्नलिखित में से कौन-सा अवश्य सत्य है?",
  ["C is in the Red group.", "A is in the Red group.", "E is in the Red group.", "B and F are in the same group."],
  ["C लाल समूह में है।", "A लाल समूह में है।", "E लाल समूह में है।", "B और F एक ही समूह में हैं।"],
  0,
  "Red has three places and G is not in it, and Red holds exactly one of A and B. If C and D were in Blue, Red's other two members would have to come from E and F -- both of them, which is not allowed. So C and D are in Red: Red is C, D and one of A and B, and E, F and G are all in Blue. "
  "C is therefore in Red in every possible split. A may be in Red, but B may be instead; E is never in Red; and B shares a group with F only when A is the one in Red.",
  "लाल में तीन स्थान हैं और G उसमें नहीं है, और लाल में A और B में से ठीक एक है। यदि C और D नीले में होते, तो लाल के बाक़ी दो सदस्य E और F से आते -- दोनों, जो मना है। अतः C और D लाल में हैं: लाल में C, D और A या B में से एक है, और E, F और G सभी नीले में हैं। "
  "इसलिए हर संभव बँटवारे में C लाल में है। A लाल में हो सकता है, पर उसकी जगह B भी; E कभी लाल में नहीं होता; और B, F के साथ एक समूह में तभी होता है जब लाल में A हो।",
  "lr-sa-seven-students-split-into-two-groups", pos=3, check=_sa3)

# 7 -- a mother-in-law traced through a maternal grandfather
def _br1():
    sons_of_rahuls_mother = {"Rahul": True, "his brother": False}     # married?
    husbands = [s for s, married in sons_of_rahuls_mother.items() if married]
    assert husbands == ["Rahul"]
    return "Wife"
N(LR, "Blood Relation", "medium",
  "Neha's mother-in-law is the only daughter of Rahul's maternal grandfather. Rahul's only brother is unmarried. How is Neha related to Rahul?",
  "नेहा की सास राहुल के नाना की इकलौती बेटी है। राहुल का इकलौता भाई अविवाहित है। नेहा का राहुल से क्या संबंध है?",
  ["Sister-in-law", "Daughter-in-law", "Wife", "Cousin"], 2,
  "Rahul's maternal grandfather is his mother's father, and that man's only daughter is Rahul's mother. So Neha's mother-in-law is Rahul's mother, and Neha is married to one of her sons -- Rahul or his brother. The brother is unmarried, so Neha is Rahul's wife. "
  "'Sister-in-law' would need her to be the brother's wife; 'daughter-in-law' is what she is to Rahul's mother, not to Rahul; and nothing makes her a cousin.",
  "राहुल के नाना उसकी माँ के पिता हैं, और उनकी इकलौती बेटी राहुल की माँ है। अतः नेहा की सास राहुल की माँ है, और नेहा का विवाह उनके किसी बेटे से हुआ है -- राहुल या उसके भाई से। भाई अविवाहित है, इसलिए नेहा राहुल की पत्नी है। "
  "'भाभी' होने के लिए उसे भाई की पत्नी होना चाहिए; 'बहू' वह राहुल की माँ की है, राहुल की नहीं; और उसे चचेरी या ममेरी बहन बनाने वाली कोई बात नहीं।",
  "lr-br-a-mother-in-law-traced-through-a-maternal-grandfather", _br1,
  opts_hi=["भाभी", "बहू", "पत्नी", "चचेरी या ममेरी बहन"])

# 8 -- a woman's 'father's only son'
def _br2():
    out = set()
    for via in ("son", "daughter"):                  # the brother's child through whom the boy descends
        grandfather_side = "paternal" if via == "son" else "maternal"
        out.add(("sister of a grandfather", grandfather_side))
    assert {r for r, _ in out} == {"sister of a grandfather"} and len(out) == 2
    return "She is a sister of one of his grandfathers."
T(LR, "Blood Relation", "hard",
  "Pointing to a boy, Seema says, 'He is the grandson of my father's only son.' How is Seema related to the boy?",
  "एक लड़के की ओर इशारा करते हुए सीमा कहती है, 'वह मेरे पिता के इकलौते बेटे का पोता/नाती है।' सीमा का उस लड़के से क्या संबंध है?",
  ["She is a sister of one of his grandfathers.", "She is his grandmother.", "She is his father's sister.",
   "It cannot be determined, since the boy's parents are not named."],
  ["वह उसके दादा या नाना की बहन है।", "वह उसकी दादी है।", "वह उसकी बुआ है।",
   "यह तय नहीं किया जा सकता, क्योंकि लड़के के माता-पिता के नाम नहीं दिए गए।"],
  0,
  "Seema is a woman, so her father's only son is not Seema herself but her brother. The boy is her brother's grandson, which makes the brother one of the boy's grandfathers -- his paternal grandfather if the boy is the brother's son's son, his maternal grandfather if he is the brother's daughter's son. Either way Seema is the sister of one of his grandfathers. "
  "Reading 'my father's only son' as the speaker gives 'grandmother', the trap; 'father's sister' would need the boy to be her brother's son, not his grandson; and the relation is fixed even though which grandfather it runs through is not.",
  "सीमा एक स्त्री है, इसलिए उसके पिता का इकलौता बेटा स्वयं सीमा नहीं बल्कि उसका भाई है। लड़का उसके भाई का पोता या नाती है, जिससे भाई लड़के का दादा या नाना बनता है -- दादा, यदि लड़का भाई के बेटे का बेटा है; नाना, यदि वह भाई की बेटी का बेटा है। दोनों ही स्थितियों में सीमा उसके दादा या नाना की बहन है। "
  "'मेरे पिता का इकलौता बेटा' को वक्ता स्वयं मान लेने से 'दादी' उत्तर आता है, जो जाल है; 'बुआ' होने के लिए लड़के को उसके भाई का बेटा होना चाहिए, पोता नहीं; और संबंध तय है, भले ही यह तय न हो कि वह दादा के रास्ते है या नाना के।",
  "lr-br-a-woman-s-father-s-only-son", pos=3, check=_br2)

# 9 -- the way back after a walk that turns back
def _dd1():
    x = y = 0
    heading = (0, 1)                                  # north
    right = lambda h: (h[1], -h[0])
    left = lambda h: (-h[1], h[0])
    for turn, dist in ((None, 6), (right, 3), ("back", 8), (left, 6)):
        if turn == "back":
            heading = (-heading[0], -heading[1])
        elif turn:
            heading = turn(heading)
        x, y = x + heading[0] * dist, y + heading[1] * dist
    assert (x, y) == (-5, 0) and heading == (0, -1)
    return "East, 5 km"                               # the temple, at the origin, lies 5 km due east of her
N(LR, "Direction & Distance", "easy",
  "Asha leaves a temple and walks 6 km north. She turns right and walks 3 km, then turns back and walks 8 km, and then turns left and walks 6 km. In which direction must she now walk to go straight back to the temple, and how far?",
  "आशा एक मंदिर से निकलकर 6 किमी उत्तर चलती है। वह दाएँ मुड़कर 3 किमी चलती है, फिर पीछे मुड़कर 8 किमी चलती है, और फिर बाएँ मुड़कर 6 किमी चलती है। मंदिर तक सीधे लौटने के लिए अब उसे किस दिशा में और कितना चलना होगा?",
  ["West, 5 km", "East, 5 km", "South, 5 km", "East, 11 km"], 1,
  "Turning right from north faces east; turning back from east faces west; turning left from west faces south. Taking the temple as the starting point, she goes 6 km north, 3 km east, then 8 km west -- 5 km west of the temple's north-south line -- and finally 6 km south, back to the temple's east-west line. "
  "She is 5 km due west of the temple, facing south, so she must walk 5 km east to return. 'West' is her direction from the temple, not the way back; 'south' is the way she is facing; and 11 km adds the two east-west legs instead of subtracting one from the other.",
  "उत्तर से दाएँ मुड़ने पर मुँह पूर्व की ओर होता है; पूर्व से पीछे मुड़ने पर पश्चिम की ओर; पश्चिम से बाएँ मुड़ने पर दक्षिण की ओर। मंदिर को आरंभ बिंदु मानें तो वह 6 किमी उत्तर, 3 किमी पूर्व, फिर 8 किमी पश्चिम जाती है -- मंदिर की उत्तर-दक्षिण रेखा से 5 किमी पश्चिम -- और अंत में 6 किमी दक्षिण, मंदिर की पूर्व-पश्चिम रेखा पर वापस। "
  "वह मंदिर से 5 किमी ठीक पश्चिम में है, मुँह दक्षिण की ओर, इसलिए लौटने के लिए उसे 5 किमी पूर्व चलना होगा। 'पश्चिम' मंदिर से उसकी दिशा है, लौटने का रास्ता नहीं; 'दक्षिण' वह दिशा है जिधर उसका मुँह है; और 11 किमी पूर्व-पश्चिम के दोनों हिस्सों को घटाने के बजाय जोड़ देता है।",
  "lr-dd-the-way-back-after-a-walk-that-turns-back", _dd1,
  opts_hi=["पश्चिम, 5 किमी", "पूर्व, 5 किमी", "दक्षिण, 5 किमी", "पूर्व, 11 किमी"])

# 10 -- a leg of a walk found from the final distance
def _dd2():
    ys = [y for y in range(1, 50) if (5 - 8) ** 2 + (y - 2) ** 2 == 25]
    assert ys == [6]
    return f"{ys[0]} km"
N(LR, "Direction & Distance", "hard",
  "A man walks 5 km due east, then some distance due north, then 8 km due west, and finally 2 km due south. He is now 5 km from where he started. How far did he walk north?",
  "एक व्यक्ति 5 किमी ठीक पूर्व चलता है, फिर कुछ दूरी ठीक उत्तर, फिर 8 किमी ठीक पश्चिम, और अंत में 2 किमी ठीक दक्षिण। अब वह अपने आरंभ बिंदु से 5 किमी दूर है। वह उत्तर की ओर कितना चला?",
  ["2 km", "4 km", "6 km", "7 km"], 2,
  "East-west, he ends 8 - 5 = 3 km west of the start. If he walked y km north, he ends y - 2 km north of the start. Being 5 km from the start means 3² + (y - 2)² = 5², so y - 2 = 4 (the other root, -4, would need him to walk a negative distance north), and y = 6 km. "
  "4 km forgets the final 2 km south; 2 km and 7 km do not leave him 5 km from the start.",
  "पूर्व-पश्चिम में वह आरंभ से 8 - 5 = 3 किमी पश्चिम में रहता है। यदि वह y किमी उत्तर चला, तो वह आरंभ से y - 2 किमी उत्तर में रहता है। आरंभ से 5 किमी दूर होने का अर्थ है 3² + (y - 2)² = 5², अतः y - 2 = 4 (दूसरे मूल -4 के लिए उसे उत्तर की ओर ऋणात्मक दूरी चलनी पड़ती), और y = 6 किमी। "
  "4 किमी अंतिम 2 किमी दक्षिण को भूल जाता है; 2 किमी और 7 किमी उसे आरंभ से 5 किमी दूर नहीं छोड़ते।",
  "lr-dd-a-leg-of-a-walk-found-from-the-final-distance", _dd2,
  opts_hi=["2 किमी", "4 किमी", "6 किमी", "7 किमी"])

# 11 -- a code that sorts letters
def _cd1():
    code = lambda w: "".join(sorted(w))
    assert code("GARDEN") == "ADEGNR"
    same = [w for w in ("ALMOST", "GLOBE", "FLOWER", "CHEST") if code(w) == w]
    assert same == ["ALMOST"]
    return same[0]
T(LR, "Coding-Decoding", "medium",
  "In a certain code, every word is written with its letters arranged in alphabetical order; for example, GARDEN is written as ADEGNR. Which one of the following words is written in this code exactly as it is spelt?",
  "एक विशेष कूट में हर शब्द उसके अक्षरों को वर्णमाला के क्रम में रखकर लिखा जाता है; उदाहरण के लिए, GARDEN को ADEGNR लिखा जाता है। निम्नलिखित में से कौन-सा शब्द इस कूट में ठीक वैसा ही लिखा जाता है जैसी उसकी वर्तनी है?",
  ["ALMOST", "GLOBE", "FLOWER", "CHEST"], ["ALMOST", "GLOBE", "FLOWER", "CHEST"], 0,
  "A word is unchanged by the code only if its letters already stand in alphabetical order. A-L-M-O-S-T does: each letter comes later in the alphabet than the one before it. GLOBE breaks the order at O-B (it is written BEGLO), FLOWER at W-E (EFLORW) and CHEST at H-E (CEHST).",
  "कोई शब्द इस कूट में तभी अपरिवर्तित रहता है जब उसके अक्षर पहले से वर्णमाला के क्रम में हों। A-L-M-O-S-T ऐसा है: हर अक्षर वर्णमाला में अपने पिछले अक्षर के बाद आता है। GLOBE, O-B पर क्रम तोड़ता है (उसे BEGLO लिखा जाता है), FLOWER, W-E पर (EFLORW) और CHEST, H-E पर (CEHST)।",
  "lr-cd-a-code-that-sorts-letters", pos=3, check=_cd1)

# 12 -- a digit code found from two examples
def _cd2():
    code = lambda n: "".join(str(9 - int(d)) for d in reversed(n))
    assert code("3172") == "7286" and code("5431") == "8654"
    return code("2618")
N(LR, "Coding-Decoding", "hard",
  "In a certain code, 3172 is written as 7286 and 5431 is written as 8654. How is 2618 written in that code?",
  "एक विशेष कूट में 3172 को 7286 और 5431 को 8654 लिखा जाता है। उस कूट में 2618 को कैसे लिखा जाएगा?",
  ["1837", "1873", "7381", "8162"], 0,
  "In each example the digits are written in reverse order and each digit is then replaced by 9 minus itself: 3172 reversed is 2713, and 9 - 2, 9 - 7, 9 - 1 and 9 - 3 give 7286; 5431 reversed is 1345, which gives 8654. So 2618, reversed to 8162, becomes 1837. "
  "8162 stops after reversing; 7381 replaces the digits without reversing them; 1873 swaps the last two digits of the answer.",
  "हर उदाहरण में अंक उलटे क्रम में लिखे जाते हैं और फिर हर अंक को 9 में से उसे घटाकर बदला जाता है: 3172 उलटकर 2713 है, और 9 - 2, 9 - 7, 9 - 1 और 9 - 3 से 7286 मिलता है; 5431 उलटकर 1345 है, जिससे 8654 मिलता है। अतः 2618, उलटकर 8162, बन जाता है 1837। "
  "8162 उलटने के बाद रुक जाता है; 7381 अंकों को उलटे बिना बदल देता है; 1873 उत्तर के अंतिम दो अंकों की अदला-बदली कर देता है।",
  "lr-cd-a-digit-code-found-from-two-examples", _cd2)

# 13 -- a painted cube counted back from its unpainted cubes
def _cp1():
    n = next(n for n in range(3, 30) if (n - 2) ** 3 == 343)
    assert n == 9 and 6 * (n - 2) ** 2 == 294
    return str(12 * (n - 2))
N(LR, "Cube Painting", "hard",
  "A large cube is painted on all its faces and then cut into small cubes of the same size. Of these small cubes, 343 have no paint on them. How many of the small cubes have paint on exactly two faces?",
  "एक बड़े घन के सभी फलकों को रंगा जाता है और फिर उसे समान आकार के छोटे घनों में काटा जाता है। इन छोटे घनों में से 343 पर कोई रंग नहीं है। कितने छोटे घनों के ठीक दो फलक रंगे हैं?",
  ["72", "84", "96", "294"], 1,
  "If the large cube is cut into n × n × n small cubes, the unpainted ones form the inner block of (n - 2)³ cubes. (n - 2)³ = 343 gives n - 2 = 7, so n = 9. The cubes with exactly two painted faces lie along the 12 edges, leaving out the corners: 12 × (n - 2) = 12 × 7 = 84. "
  "294 = 6 × 49 counts the cubes with exactly one painted face; 96 takes 8 cubes per edge, counting a corner with each edge; 72 takes 6.",
  "यदि बड़े घन को n × n × n छोटे घनों में काटा जाए, तो बिना रंग वाले घन (n - 2)³ घनों का भीतरी खंड बनाते हैं। (n - 2)³ = 343 से n - 2 = 7, अतः n = 9। ठीक दो रंगे फलकों वाले घन 12 किनारों के साथ होते हैं, कोनों को छोड़कर: 12 × (n - 2) = 12 × 7 = 84। "
  "294 = 6 × 49 ठीक एक रंगे फलक वाले घन गिनता है; 96 हर किनारे पर 8 घन लेता है, हर किनारे के साथ एक कोना गिनकर; 72, 6 लेता है।",
  "lr-cp-a-painted-cube-counted-back-from-its-unpainted-cubes", _cp1)

# 14 -- 'no' with 'some'
def _sy1():
    regions = list(product((0, 1), repeat=3))          # (farmer, trader, moneylender)
    one = two = True
    for mask in range(1, 1 << 8):
        world = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(f and t for f, t, m in world): continue           # no farmers are traders
        if not any(t and m for f, t, m in world): continue       # some traders are moneylenders
        one = one and any(m and not f for f, t, m in world)
        two = two and any(f and not m for f, t, m in world)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "medium",
   "Statements: No farmers are traders. Some traders are moneylenders.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कोई भी किसान व्यापारी नहीं है। कुछ व्यापारी साहूकार हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some moneylenders are not farmers.", "Some farmers are not moneylenders."],
   ["कुछ साहूकार किसान नहीं हैं।", "कुछ किसान साहूकार नहीं हैं।"],
   0,
   "The traders who are moneylenders cannot be farmers, since no trader is a farmer; so at least some moneylenders are not farmers, and I follows. The statements say nothing else about farmers and moneylenders: every farmer could be a moneylender (one who is not a trader), so II does not follow. "
   "The trap is to turn I round mechanically into II, which a 'some ... are not' statement does not allow.",
   "जो व्यापारी साहूकार हैं वे किसान नहीं हो सकते, क्योंकि कोई व्यापारी किसान नहीं है; अतः कम से कम कुछ साहूकार किसान नहीं हैं, और I निकलता है। कथन किसानों और साहूकारों के बारे में और कुछ नहीं कहते: हर किसान साहूकार हो सकता है (ऐसा जो व्यापारी नहीं है), इसलिए II नहीं निकलता। "
   "जाल I को यंत्रवत उलटकर II बना लेना है, जिसकी अनुमति 'कुछ ... नहीं हैं' वाला कथन नहीं देता।",
   "lr-sy-no-with-some", roman=True, check=_sy1)

# 15 -- two people who lie on different days
def _tl1():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    lies = {"Ravi": {"Monday", "Tuesday", "Wednesday"}, "Mohan": {"Thursday", "Friday", "Saturday"}}
    def can_say(who, k):                 # 'Yesterday was one of my lying days.'
        claim = days[k - 1] in lies[who]
        return claim != (days[k] in lies[who])
    fits = [days[k] for k in range(7) if can_say("Ravi", k) and can_say("Mohan", k)]
    assert fits == ["Thursday"]
    return fits[0]
T(LR, "Truth-Liar", "hard",
  "Ravi lies on Mondays, Tuesdays and Wednesdays and tells the truth on the other days of the week. Mohan lies on Thursdays, Fridays and Saturdays and tells the truth on the other days. One day both of them say, 'Yesterday was one of my lying days.' What day is it?",
  "रवि सोमवार, मंगलवार और बुधवार को झूठ बोलता है और सप्ताह के बाक़ी दिनों में सच। मोहन गुरुवार, शुक्रवार और शनिवार को झूठ बोलता है और बाक़ी दिनों में सच। एक दिन दोनों कहते हैं, 'कल मेरे झूठ बोलने वाले दिनों में से एक था।' वह कौन-सा दिन है?",
  ["Thursday", "Monday", "Sunday", "No day of the week fits both statements"],
  ["गुरुवार", "सोमवार", "रविवार", "सप्ताह का कोई भी दिन दोनों कथनों पर ठीक नहीं बैठता"],
  0,
  "Ravi can say it truthfully only on a truth day that follows a lying day -- Thursday -- or falsely on a lying day that follows a truth day -- Monday. Mohan can say it truthfully on Sunday, after his lying Saturday, or falsely on Thursday, a lying day after his truthful Wednesday. "
  "The only day that works for both is Thursday: Ravi is telling the truth about Wednesday and Mohan is lying about it. Monday works only for Ravi and Sunday only for Mohan, so a day that fits both does exist.",
  "रवि यह बात सच के रूप में केवल ऐसे सच वाले दिन कह सकता है जो झूठ वाले दिन के बाद आए -- गुरुवार -- या झूठ के रूप में ऐसे झूठ वाले दिन जो सच वाले दिन के बाद आए -- सोमवार। मोहन इसे सच के रूप में रविवार को कह सकता है, अपने झूठ वाले शनिवार के बाद, या झूठ के रूप में गुरुवार को, जो उसके सच वाले बुधवार के बाद झूठ का दिन है। "
  "दोनों के लिए ठीक बैठने वाला एकमात्र दिन गुरुवार है: रवि बुधवार के बारे में सच कह रहा है और मोहन उसी के बारे में झूठ। सोमवार केवल रवि के लिए और रविवार केवल मोहन के लिए ठीक बैठता है, इसलिए दोनों पर ठीक बैठने वाला दिन मौजूद है।",
  "lr-tl-two-people-who-lie-on-different-days", pos=0, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    worlds = [(a, b) for a in (True, False) for b in (True, False)]       # (A truthful, B truthful)
    ok1 = lambda a, b: ((not a) and (not b)) == a                         # I: A says 'B and I both always lie'
    ok2 = lambda a, b: (not a) == b                                       # II: B says 'A always lies'
    s1 = {a for a, b in worlds if ok1(a, b)}
    s2 = {a for a, b in worlds if ok2(a, b)}
    both = {a for a, b in worlds if ok1(a, b) and ok2(a, b)}
    assert s1 == {False} and s2 == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "On an island, every person either always tells the truth or always lies. Is A a person who always tells the truth?",
   "एक द्वीप पर हर व्यक्ति या तो हमेशा सच बोलता है या हमेशा झूठ। क्या A हमेशा सच बोलने वाला व्यक्ति है?",
   "A says, 'B and I both always lie.'", "A कहता है, 'B और मैं दोनों हमेशा झूठ बोलते हैं।'",
   "B says, 'A always lies.'", "B कहता है, 'A हमेशा झूठ बोलता है।'",
   0,
   "Statement I: if A told the truth, A would be a liar, which is impossible; so A lies, and the answer is 'no' -- settled by I alone. (A's statement being false also tells us that B tells the truth.) Statement II alone allows both cases: B truthful and A a liar, or B a liar and A truthful. "
   "So one statement alone answers the question and the other does not.",
   "कथन I: यदि A सच बोलता, तो A झूठा होता, जो असंभव है; अतः A झूठ बोलता है, और उत्तर 'नहीं' है -- अकेले I से तय। (A का कथन झूठा होने से यह भी पता चलता है कि B सच बोलता है।) कथन II अकेला दोनों स्थितियों की अनुमति देता है: B सच्चा और A झूठा, या B झूठा और A सच्चा। "
   "अतः एक कथन अकेले प्रश्न का उत्तर देता है और दूसरा नहीं।",
   "lr-ds-a-speaker-who-cannot-be-telling-the-truth", _ds1)

def _ds2():
    weight = lambda fake, coin: 1 if coin == fake else 2
    s1 = {f for f in (1, 2, 3) if weight(f, 2) < weight(f, 1)}             # I: the pan with coin 2 rises
    s2 = {f for f in (1, 2, 3) if weight(f, 1) + weight(f, 3) == 4}        # II: coins 1 and 3 weigh as two genuine coins
    assert s1 == s2 == {2}
    return _ds(s1, s2, s1 & s2)
DS(LR, "easy",
   "Of three coins that look alike, exactly one is a counterfeit, which is lighter than the other two; the two genuine coins weigh the same. Which coin is the counterfeit?",
   "एक जैसे दिखने वाले तीन सिक्कों में से ठीक एक नक़ली है, जो बाक़ी दो से हल्का है; दोनों असली सिक्कों का भार समान है। नक़ली सिक्का कौन-सा है?",
   "When coin 1 is placed on one pan of a balance and coin 2 on the other, the pan with coin 2 rises.",
   "जब सिक्का 1 तराज़ू के एक पलड़े पर और सिक्का 2 दूसरे पर रखा जाता है, तो सिक्का 2 वाला पलड़ा ऊपर उठ जाता है।",
   "Coins 1 and 3 together weigh exactly as much as two genuine coins.",
   "सिक्के 1 और 3 मिलकर ठीक उतने भारी हैं जितने दो असली सिक्के।",
   1,
   "Statement I: the pan that rises holds the lighter coin, so coin 2 is lighter than coin 1 and must be the counterfeit -- sufficient. Statement II: coins 1 and 3 weigh as much as two genuine coins, so neither of them is the light one, and the counterfeit is coin 2 -- also sufficient. Either statement alone answers the question.",
   "कथन I: जो पलड़ा ऊपर उठता है उसमें हल्का सिक्का है, इसलिए सिक्का 2, सिक्का 1 से हल्का है और नक़ली होना चाहिए -- पर्याप्त। कथन II: सिक्के 1 और 3 दो असली सिक्कों जितने भारी हैं, इसलिए उनमें से कोई हल्का नहीं, और नक़ली सिक्का 2 है -- यह भी पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-light-coin-found-two-ways", _ds2)

def _ds3():
    pts = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
    R = (0, 0)
    s1 = {p[1] > q[1] for p in pts for q in pts if p[1] == R[1] and p[0] > R[0]}                 # I: P due east of R
    s2 = {p[1] > q[1] for p in pts for q in pts if q[0] == R[0] and q[1] > R[1]}                 # II: Q due north of R
    both = {p[1] > q[1] for p in pts for q in pts if p[1] == R[1] and p[0] > R[0] and q[0] == R[0] and q[1] > R[1]}
    assert both == {False}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Is town P to the north of town Q?",
   "क्या नगर P, नगर Q के उत्तर में है?",
   "P is due east of town R.", "P, नगर R के ठीक पूर्व में है।",
   "Q is due north of town R.", "Q, नगर R के ठीक उत्तर में है।",
   2,
   "Statement I places P on R's east-west line but says nothing of Q; Statement II places Q north of R but says nothing of P. Together, P lies on R's east-west line while Q lies north of that line, so P is to the south of Q (to its south-east, in fact): the answer is a definite 'no'. "
   "A definite 'no' answers the question as fully as a 'yes' would, so the two statements together are sufficient, though neither is alone.",
   "कथन I, P को R की पूर्व-पश्चिम रेखा पर रखता है पर Q के बारे में कुछ नहीं कहता; कथन II, Q को R के उत्तर में रखता है पर P के बारे में कुछ नहीं कहता। दोनों साथ: P, R की पूर्व-पश्चिम रेखा पर है जबकि Q उस रेखा के उत्तर में, इसलिए P, Q के दक्षिण में (वास्तव में दक्षिण-पूर्व में) है: उत्तर एक निश्चित 'नहीं' है। "
   "निश्चित 'नहीं' प्रश्न का उत्तर उतना ही पूरा देता है जितना 'हाँ', इसलिए दोनों कथन साथ मिलकर पर्याप्त हैं, यद्यपि अकेले कोई नहीं।",
   "lr-ds-a-definite-no-from-two-directions", _ds3)
