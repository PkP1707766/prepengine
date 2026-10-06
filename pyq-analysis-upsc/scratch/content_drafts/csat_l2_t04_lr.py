# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 4 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Same mix as Tests 1-3 with new traps: an argument strengthened by a comparison group, a library notice, a
correlation read as a cause, a square table with corner and middle seats, a three-way logic grid, a round table
where some face outwards, a grandfather through a son, a family whose men must be counted though one member's sex is never stated,
legs that cancel, two walkers going opposite ways, letters shifted one place further each time, a product written
backwards, a die seen twice, two 'some' statements, and a theft where only one statement is true; in the
data-sufficiency block, a day fixed either way, a chain of heights, and a share that settles the question.
Difficulty 3 easy / 10 medium / 5 hard. Arrangement, code, die, syllogism and truth-teller keys are found by
checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

ASSUMPT = "Which of the following assumptions is/are implicit in the statement?"
ASSUMPT_HI = "निम्नलिखित में से कौन-सी/से पूर्वधारणा/एँ कथन में अंतर्निहित है/हैं?"

# 1 -- an argument strengthened by a comparison group
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Argument: Some schools in a district moved their start time from 7:30 to 8:30 in the morning, and in the following year they reported better attendance. Starting school later therefore improves attendance.\n\n"
  "Which one of the following, if true, most strengthens the argument?",
  "तर्क: एक ज़िले के कुछ विद्यालयों ने अपना प्रारंभ समय सुबह 7:30 से बदलकर 8:30 कर दिया, और अगले वर्ष उनमें उपस्थिति बेहतर रही। अतः विद्यालय देर से शुरू करने से उपस्थिति सुधरती है।\n\n"
  "निम्नलिखित में से कौन-सा, यदि सत्य हो, तो तर्क को सबसे अधिक मज़बूत करता है?",
  ["That year, attendance did not change at the district's schools that kept the 7:30 start.",
   "The later start meant that teachers at those schools also began their work an hour later.",
   "Attendance at the schools that moved had already been rising in the years before the change.",
   "Some of the schools that moved their start time have no buses for their students."],
  ["उसी वर्ष, 7:30 का समय रखने वाले ज़िले के विद्यालयों में उपस्थिति नहीं बदली।",
   "देर से शुरुआत के कारण उन विद्यालयों के शिक्षकों ने भी अपना काम एक घंटा देर से शुरू किया।",
   "समय बदलने वाले विद्यालयों में बदलाव से पहले के वर्षों में ही उपस्थिति बढ़ रही थी।",
   "प्रारंभ समय बदलने वाले कुछ विद्यालयों के पास विद्यार्थियों के लिए बसें नहीं हैं।"], 0,
  "The argument credits the later start with the better attendance. The strongest support compares like with like: schools in the same district and the same year that kept the 7:30 start saw no change, "
  "which points to the timing as the cause. A rise already under way before the change would weaken the argument; when the teachers began work, and whether some schools lack buses, say nothing about why attendance rose.",
  "तर्क बेहतर उपस्थिति का श्रेय देर से शुरुआत को देता है। सबसे प्रबल समर्थन समान की समान से तुलना करता है: उसी ज़िले और उसी वर्ष में जिन विद्यालयों ने 7:30 का समय रखा उनमें कोई बदलाव नहीं हुआ, "
  "जो समय को ही कारण के रूप में इंगित करता है। बदलाव से पहले से चल रही वृद्धि तर्क को कमज़ोर करती; शिक्षकों ने कब काम शुरू किया, और कुछ विद्यालयों के पास बसें हैं या नहीं, इससे यह पता नहीं चलता कि उपस्थिति क्यों बढ़ी।",
  "lr-sc-later-start-comparison-group", pos=3)

# 2 -- a library notice
S2(LR, "Statement-Conclusion/Assumption", "easy",
   "Statement: A notice at the entrance of a library reads, 'Bags are not allowed beyond this point.'\n\n" + ASSUMPT,
   "कथन: एक पुस्तकालय के प्रवेश द्वार पर लगी सूचना में लिखा है, 'इस स्थान से आगे थैले ले जाने की अनुमति नहीं है।'\n\n" + ASSUMPT_HI,
   ["Bags could be used to take books out of the library without having them issued.",
    "Every reader who comes to the library carries a bag."],
   ["थैलों का उपयोग पुस्तकों को बिना जारी कराए पुस्तकालय से बाहर ले जाने में किया जा सकता है।",
    "पुस्तकालय में आने वाला हर पाठक थैला लेकर आता है।"], 0,
   "Only I is implicit: the rule makes sense only if bags carried into the reading area could cause trouble, most obviously by letting books leave unrecorded. "
   "II is not assumed: the notice is addressed to readers who do bring bags, and it works whether or not every reader carries one.",
   "केवल I अंतर्निहित है: नियम तभी अर्थपूर्ण है जब पढ़ने वाले क्षेत्र में ले जाए गए थैले कोई समस्या पैदा कर सकें, सबसे स्पष्ट रूप से पुस्तकों को बिना दर्ज हुए बाहर ले जाने में। "
   "II पूर्वधारणा नहीं है: सूचना उन पाठकों के लिए है जो थैले लाते हैं, और वह इस बात से स्वतंत्र काम करती है कि हर पाठक थैला लाता है या नहीं।",
   "lr-sc-library-notice-on-bags", roman=True)

# 3 -- a correlation read as a cause
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Argument: A survey of the members of a gym found that those who exercise every day are, on average, healthier than those who exercise once a week. Exercising every day therefore makes people healthier.\n\n"
  "Which one of the following points out a flaw in the argument?",
  "तर्क: एक जिम के सदस्यों के सर्वेक्षण में पाया गया कि जो हर दिन व्यायाम करते हैं, वे औसतन उनसे अधिक स्वस्थ हैं जो सप्ताह में एक बार व्यायाम करते हैं। अतः हर दिन व्यायाम करना लोगों को अधिक स्वस्थ बनाता है।\n\n"
  "निम्नलिखित में से कौन-सा तर्क की एक त्रुटि बताता है?",
  ["It ignores that healthier people may be better able to exercise daily.",
   "It relies on the opinions of gym trainers rather than on facts about members.",
   "It compares people who exercise with people who never exercise at all.",
   "It assumes that exercising once a week has no effect on health whatsoever."],
  ["यह अनदेखा करता है कि अधिक स्वस्थ लोग ही शायद रोज़ व्यायाम कर पाते हैं।",
   "यह सदस्यों के तथ्यों के बजाय जिम प्रशिक्षकों की राय पर निर्भर है।",
   "यह व्यायाम करने वालों की तुलना कभी व्यायाम न करने वालों से करता है।",
   "यह मान लेता है कि सप्ताह में एक बार व्यायाम का स्वास्थ्य पर कोई असर नहीं होता।"], 0,
  "The argument moves from 'daily exercisers are healthier' to 'daily exercise makes people healthier' without ruling out the reverse: being healthier may be what lets people exercise every day. "
  "The other options misdescribe the argument: it rests on a survey of members, not on trainers' opinions; it compares daily with weekly exercisers, not with people who never exercise; and it claims nothing about weekly exercise having no effect.",
  "तर्क 'रोज़ व्यायाम करने वाले अधिक स्वस्थ हैं' से 'रोज़ व्यायाम लोगों को अधिक स्वस्थ बनाता है' पर पहुँच जाता है, उलटी संभावना को ख़ारिज किए बिना: हो सकता है अधिक स्वस्थ होना ही लोगों को रोज़ व्यायाम करने देता हो। "
  "बाक़ी विकल्प तर्क का ग़लत वर्णन करते हैं: वह सदस्यों के सर्वेक्षण पर टिका है, प्रशिक्षकों की राय पर नहीं; वह रोज़ और साप्ताहिक व्यायाम करने वालों की तुलना करता है, कभी व्यायाम न करने वालों से नहीं; और वह साप्ताहिक व्यायाम के बेअसर होने का कोई दावा नहीं करता।",
  "lr-sc-correlation-read-as-cause", pos=1)

# 4 -- a square table with corner and middle seats
def _sa1():
    # Seats 0-7 clockwise; even seats are corners, odd seats the middles of the sides. Everyone faces the centre,
    # so a person's left is the next seat clockwise (+1) and the right the next anticlockwise (-1). P fixed at seat 0.
    sols = []
    for rest in permutations("QRSTUVW"):
        s = dict(zip(rest, range(1, 8)))
        s["P"] = 0
        if any(s[x] % 2 for x in "PQRS") or s["S"] != 4 or s["R"] != 2 or s["T"] != 1:
            continue
        if s["W"] != (s["T"] + 4) % 8 or s["U"] != (s["P"] - 1) % 8:
            continue
        sols.append(s)
    assert len(sols) == 1, sols
    s = sols[0]
    return next(p for p, seat in s.items() if seat == (s["V"] + 4) % 8)
N(LR, "Seating Arrangement", "hard",
  "Eight people sit around a square table, all facing the centre: P, Q, R and S at the four corners, and T, U, V and W at the middles of the four sides. P sits opposite S. R sits second to the left of P, "
  "and T sits between P and R. W sits opposite T. U sits to the immediate right of P. Who sits opposite V?",
  "आठ लोग एक वर्गाकार मेज़ के चारों ओर केंद्र की ओर मुँह करके बैठे हैं: P, Q, R और S चारों कोनों पर, और T, U, V और W चारों भुजाओं के मध्य में। P, S के सामने बैठा है। R, P के बाएँ से दूसरे स्थान पर है, "
  "और T, P और R के बीच बैठा है। W, T के सामने बैठा है। U, P के ठीक दाएँ बैठा है। V के सामने कौन बैठा है?",
  ["T", "U", "V", "W"], 1,
  "For people facing the centre, left is clockwise and right anticlockwise. Put P at a corner; S takes the opposite corner. Second to P's left is the next corner clockwise, so R sits there, "
  "and T, between P and R, takes the middle seat between them; W, opposite T, sits between S and the fourth corner. U is at P's immediate right, the middle seat on P's other side. "
  "Q takes the last corner and V the last middle seat, between R and S -- directly opposite U. Taking left as anticlockwise puts R at the wrong corner.",
  "केंद्र की ओर मुँह किए लोगों के लिए बायाँ दक्षिणावर्त है और दायाँ वामावर्त। P को एक कोने पर रखिए; S सामने वाला कोना लेता है। P के बाएँ से दूसरा स्थान दक्षिणावर्त अगला कोना है, इसलिए R वहाँ बैठता है, "
  "और P और R के बीच वाला T उनके बीच की मध्य सीट लेता है; T के सामने वाला W, S और चौथे कोने के बीच बैठता है। U, P के ठीक दाएँ, P की दूसरी ओर की मध्य सीट पर है। "
  "Q अंतिम कोना और V अंतिम मध्य सीट लेता है, R और S के बीच -- ठीक U के सामने। बाएँ को वामावर्त मानने से R ग़लत कोने पर पहुँच जाता है।",
  "lr-sa-square-table-corners-and-sides", _sa1)

# 5 -- a three-way logic grid
def _sa2():
    names = ["Anil", "Bina", "Chetan"]
    sols = []
    for cities in permutations(["Pune", "Kochi", "Jaipur"]):
        city = dict(zip(names, cities))
        for jobs in permutations(["Doctor", "Lawyer", "Teacher"]):
            job = dict(zip(names, jobs))
            doctor = next(n for n in names if job[n] == "Doctor")
            if city[doctor] != "Kochi" or job["Anil"] == "Lawyer" or city["Anil"] == "Jaipur":
                continue
            if city["Bina"] != "Pune" or job["Chetan"] == "Teacher":
                continue
            sols.append((city, job))
    assert len(sols) == 1, sols
    return sols[0][1]["Bina"]
N(LR, "Seating Arrangement", "medium",
  "Three friends -- Anil, Bina and Chetan -- live in three different cities, Pune, Kochi and Jaipur, and work as a doctor, a lawyer and a teacher, one job each. The doctor lives in Kochi. "
  "Anil is not the lawyer and does not live in Jaipur. Bina lives in Pune. Chetan is not the teacher. What does Bina do?",
  "तीन मित्र -- अनिल, बीना और चेतन -- तीन अलग-अलग शहरों, पुणे, कोच्चि और जयपुर, में रहते हैं, और डॉक्टर, वकील और शिक्षक के रूप में काम करते हैं, हर एक का एक काम। डॉक्टर कोच्चि में रहता है। "
  "अनिल वकील नहीं है और जयपुर में नहीं रहता। बीना पुणे में रहती है। चेतन शिक्षक नहीं है। बीना क्या काम करती है?",
  ["Doctor", "Lawyer", "Teacher", "Cannot be determined"], 2,
  "Bina lives in Pune, and Anil does not live in Jaipur, so Anil lives in Kochi and Chetan in Jaipur. The doctor lives in Kochi, so Anil is the doctor. Chetan is not the teacher, so Chetan is the lawyer, "
  "and Bina is the teacher. 'Cannot be determined' gives up too early: every clue is needed, but together they fix the whole grid.",
  "बीना पुणे में रहती है, और अनिल जयपुर में नहीं रहता, इसलिए अनिल कोच्चि में और चेतन जयपुर में रहता है। डॉक्टर कोच्चि में रहता है, इसलिए अनिल डॉक्टर है। चेतन शिक्षक नहीं है, इसलिए चेतन वकील है, "
  "और बीना शिक्षक है। 'निर्धारित नहीं किया जा सकता' बहुत जल्दी हार मान लेता है: हर सूत्र ज़रूरी है, पर मिलकर वे पूरी तालिका तय कर देते हैं।",
  "lr-sa-three-friends-cities-and-jobs", _sa2,
  opts_hi=["डॉक्टर", "वकील", "शिक्षक", "निर्धारित नहीं किया जा सकता"])

# 6 -- a round table where some face outwards
def _sa3():
    # Seats 0-5 clockwise. Facing the centre: left = clockwise (+1), right = anticlockwise (-1); facing out it is the reverse.
    left = lambda seat, inward: (seat + 1) % 6 if inward else (seat - 1) % 6
    right = lambda seat, inward: (seat - 1) % 6 if inward else (seat + 1) % 6
    sols = []
    for rest in permutations("BCDEF"):
        s = dict(zip(rest, range(1, 6)))
        s["A"] = 0
        for faces in product((True, False), repeat=6):
            inward = {p: faces[s[p]] for p in s}
            if not inward["A"] or any(faces[i] == faces[(i + 1) % 6] for i in range(6)):
                continue
            if s["C"] != left(left(s["A"], inward["A"]), inward["A"]) or s["B"] != right(s["C"], inward["C"]):
                continue
            if s["E"] != (s["B"] + 3) % 6 or s["F"] != right(s["A"], inward["A"]):
                continue
            sols.append((s, inward))
    assert len(sols) == 1, sols
    s, inward = sols[0]
    target = left(s["B"], inward["B"])
    return next(p for p, seat in s.items() if seat == target)
N(LR, "Seating Arrangement", "hard",
  "Six people, A, B, C, D, E and F, sit around a round table. Some face the centre and the others face outwards, and no two people sitting next to each other face the same way. A faces the centre. "
  "C sits second to the left of A, and B sits to the immediate right of C. E sits opposite B, and F sits to the immediate right of A. Who sits to the immediate left of B?",
  "छह लोग, A, B, C, D, E और F, एक गोल मेज़ के चारों ओर बैठे हैं। कुछ का मुँह केंद्र की ओर है और बाक़ियों का बाहर की ओर, और बगल में बैठे कोई भी दो व्यक्ति एक ही ओर मुँह नहीं किए हैं। A का मुँह केंद्र की ओर है। "
  "C, A के बाएँ से दूसरे स्थान पर है, और B, C के ठीक दाएँ बैठा है। E, B के सामने बैठा है, और F, A के ठीक दाएँ बैठा है। B के ठीक बाएँ कौन बैठा है?",
  ["A", "C", "D", "E"], 0,
  "Since neighbours face opposite ways, the seats alternate: A and every second seat from A face the centre, the seats in between face outwards. Facing the centre, left is clockwise; facing outwards, it is anticlockwise. "
  "C is two seats clockwise from A and so faces the centre too; B, to C's right, is the seat back towards A, between them, and faces outwards. E is opposite B, F is just anticlockwise of A, and D takes the last seat. "
  "Because B faces outwards, B's left is the seat towards A: A. C is the answer only if B is taken to face the centre.",
  "पड़ोसी उलटी दिशाओं में मुँह किए हैं, इसलिए सीटें बारी-बारी से बदलती हैं: A और A से हर दूसरी सीट केंद्र की ओर, और बीच की सीटें बाहर की ओर। केंद्र की ओर मुँह होने पर बायाँ दक्षिणावर्त है; बाहर की ओर होने पर वामावर्त। "
  "C, A से दो सीट दक्षिणावर्त है और इसलिए वह भी केंद्र की ओर है; C के दाएँ वाला B, A की ओर लौटती सीट पर, उन दोनों के बीच है और बाहर की ओर मुँह किए है। E, B के सामने है, F, A के ठीक वामावर्त है, और D अंतिम सीट लेता है। "
  "चूँकि B का मुँह बाहर की ओर है, B का बायाँ A की ओर वाली सीट है: A। C तभी उत्तर होता जब B को केंद्र की ओर मुँह किए माना जाए।",
  "lr-sa-round-table-some-face-out", _sa3)

# 7 -- a grandfather through a son
T(LR, "Blood Relation", "easy",
  "P is the father of Q, and Q is the sister of R. R is the husband of S, and T is the son of R and S. How is P related to T?",
  "P, Q का पिता है, और Q, R की बहन है। R, S का पति है, और T, R और S का बेटा है। P, T का क्या लगता है?",
  ["Grandfather", "Father", "Uncle", "Father-in-law"], ["दादा", "पिता", "चाचा", "ससुर"], 0,
  "Q and R are brother and sister, so P, Q's father, is R's father too. T is the son of R and S, so P is T's father's father: T's grandfather (दादा). "
  "'Father' stops a generation short; 'father-in-law' is P's relation to S; an uncle would be R's brother.",
  "Q और R भाई-बहन हैं, इसलिए Q के पिता P, R के भी पिता हैं। T, R और S का बेटा है, इसलिए P, T के पिता के पिता हैं: T के दादा। "
  "'पिता' एक पीढ़ी पहले रुक जाता है; 'ससुर' P का S से संबंध है; चाचा R का भाई होता।",
  "lr-br-grandfather-through-a-son", pos=3)

# 8 -- count the men: one member's sex has to be worked out
def _br2():
    six = "PQRSTU"
    known = {"Q": "M", "P": "F", "S": "F", "U": "F", "T": "M"}       # husband, mother, daughter-in-law, sister, son
    # S is P's daughter-in-law, so she is married to a son of P; with two married couples in the family he is one of the six.
    husbands = [x for x in six if x not in ("S", "Q", "T") and known.get(x) != "F"]   # not P's husband, not S's own son, not a woman
    assert husbands == ["R"]
    sexes = dict(known, R="M")
    return str(sum(1 for x in six if sexes[x] == "M"))
N(LR, "Blood Relation", "hard",
  "A family has six members, P, Q, R, S, T and U, among whom there are two married couples. Q is the husband of P, and P is the mother of R. S is the daughter-in-law of P, and T is the son of S. "
  "U is the sister of R and is unmarried. How many male members does the family have?",
  "एक परिवार में छह सदस्य हैं, P, Q, R, S, T और U, जिनमें दो विवाहित दंपती हैं। Q, P का पति है, और P, R की माँ है। S, P की बहू है, और T, S का बेटा है। "
  "U, R की बहन है और अविवाहित है। परिवार में कितने पुरुष सदस्य हैं?",
  ["2", "3", "4", "Cannot be determined"], 1,
  "Q is a husband and T a son, so they are men; P is a mother, S a daughter-in-law and U a sister, so they are women. That leaves R. S is the daughter-in-law of P, so she is married to a son of P, "
  "and since the family's second couple must be among the six, her husband is one of them. He cannot be Q (P's husband), T (S's own son) or U (a woman), so he is R, and R is a man. "
  "The men are Q, R and T: three. 2 leaves R out because no statement calls R a man; 'cannot be determined' stops at the same point; 4 counts one of the women as well.",
  "Q पति है और T बेटा, इसलिए वे पुरुष हैं; P माँ है, S बहू और U बहन, इसलिए वे महिलाएँ हैं। बचता है R। S, P की बहू है, इसलिए उसका विवाह P के किसी बेटे से हुआ है, "
  "और चूँकि परिवार का दूसरा दंपती इन्हीं छह में है, उसका पति इन्हीं में से एक है। वह Q (P का पति), T (S का अपना बेटा) या U (महिला) नहीं हो सकता, इसलिए वह R है, और R पुरुष है। "
  "पुरुष Q, R और T हैं: तीन। 2, R को छोड़ देता है क्योंकि कोई कथन R को पुरुष नहीं कहता; 'निर्धारित नहीं किया जा सकता' उसी बिंदु पर रुक जाता है; 4 किसी एक महिला को भी गिन लेता है।",
  "lr-br-count-the-men", _br2,
  opts_hi=["2", "3", "4", "निर्धारित नहीं किया जा सकता"])

# 9 -- legs that cancel
def _dd1():
    x = 8 - 3
    y = -5 + 5
    assert y == 0 and 5 + 8 + 5 + 3 == 21 and 8 + 3 == 11
    return f"{abs(x)} km {'east' if x > 0 else 'west'}"
N(LR, "Direction & Distance", "easy",
  "Starting from his house, Arjun walks 5 km south, then 8 km east, then 5 km north and finally 3 km west. How far is he now from his house, and in which direction?",
  "अपने घर से चलकर अर्जुन 5 किमी दक्षिण, फिर 8 किमी पूर्व, फिर 5 किमी उत्तर और अंत में 3 किमी पश्चिम चलता है। अब वह अपने घर से कितनी दूर और किस दिशा में है?",
  ["5 km east", "5 km west", "11 km east", "21 km east"], 0,
  "The 5 km south and the 5 km north cancel. East-west, he goes 8 km east and comes back 3 km, so he ends 5 km east of his house. "
  "21 km adds up all the legs; 11 km adds the 3 km instead of taking it away; 5 km west gets the direction the wrong way round.",
  "5 किमी दक्षिण और 5 किमी उत्तर एक-दूसरे को काट देते हैं। पूर्व-पश्चिम में वह 8 किमी पूर्व जाता है और 3 किमी लौटता है, इसलिए वह घर से 5 किमी पूर्व में पहुँचता है। "
  "21 किमी सभी हिस्सों को जोड़ देता है; 11 किमी, 3 किमी को घटाने के बजाय जोड़ता है; 5 किमी पश्चिम दिशा उलट देता है।",
  "lr-dd-legs-that-cancel", _dd1,
  opts_hi=["5 किमी पूर्व", "5 किमी पश्चिम", "11 किमी पूर्व", "21 किमी पूर्व"])

# 10 -- two walkers going opposite ways
def _dd2():
    a, b = (4, 3), (-4, -3)
    d2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    root = round(d2 ** 0.5)
    assert root * root == d2
    return f"{root} km"
N(LR, "Direction & Distance", "medium",
  "Two friends start from the same point. One walks 3 km north and then 4 km east; the other walks 4 km west and then 3 km south. How far apart are they now?",
  "दो मित्र एक ही स्थान से चलते हैं। एक 3 किमी उत्तर और फिर 4 किमी पूर्व चलता है; दूसरा 4 किमी पश्चिम और फिर 3 किमी दक्षिण चलता है। अब वे एक-दूसरे से कितनी दूर हैं?",
  ["5 km", "7 km", "10 km", "14 km"], 2,
  "From the starting point, the first friend ends 4 km east and 3 km north, and the second 4 km west and 3 km south -- exactly opposite each other, each 5 km away (a 3-4-5 triangle). "
  "So they are 5 + 5 = 10 km apart. 5 km is each one's distance from the start; 7 km and 14 km add up the legs instead of measuring straight-line distances.",
  "आरंभ स्थान से पहला मित्र 4 किमी पूर्व और 3 किमी उत्तर पहुँचता है, और दूसरा 4 किमी पश्चिम और 3 किमी दक्षिण -- ठीक एक-दूसरे के विपरीत, हर एक 5 किमी दूर (3-4-5 त्रिभुज)। "
  "अतः वे 5 + 5 = 10 किमी दूर हैं। 5 किमी हर एक की आरंभ स्थान से दूरी है; 7 किमी और 14 किमी सीधी दूरी मापने के बजाय हिस्सों को जोड़ देते हैं।",
  "lr-dd-two-walkers-opposite-ways", _dd2,
  opts_hi=["5 किमी", "7 किमी", "10 किमी", "14 किमी"])

# 11 -- each letter moved one place further
def _cd1():
    # The examples have three letters and so fix the shifts for positions 1-3 only; the question is asked about a
    # three-letter word, so no shift has to be guessed beyond what the examples show.
    shift = lambda w: "".join(chr((ord(ch) - 65 + i + 1) % 26 + 65) for i, ch in enumerate(w))
    assert shift("CAT") == "DCW" and shift("DOG") == "EQJ"
    assert shift("HEN") == "IGQ" and "".join(chr(ord(ch) + 1) for ch in "HEN") == "IFO"
    assert "".join(chr(ord(ch) + i) for i, ch in enumerate("HEN")) == "HFP"
    assert "".join(chr(ord(ch) - i - 1) for i, ch in enumerate("HEN")) == "GCK"
    return shift("HEN")
N(LR, "Coding-Decoding", "medium",
  "In a certain code, CAT is written as DCW and DOG as EQJ. How is HEN written in that code?",
  "एक निश्चित कूट में CAT को DCW और DOG को EQJ लिखा जाता है। उसी कूट में HEN को कैसे लिखा जाएगा?",
  ["GCK", "HFP", "IFO", "IGQ"], 3,
  "Compare letter by letter: C → D (+1), A → C (+2), T → W (+3), and D → E, O → Q, G → J in the same way: the first letter moves one place, the second two and the third three. "
  "HEN becomes H + 1 = I, E + 2 = G, N + 3 = Q: IGQ. IFO moves every letter by one place; HFP starts the steps at +0; GCK moves the letters backwards instead of forwards.",
  "अक्षर-दर-अक्षर तुलना कीजिए: C → D (+1), A → C (+2), T → W (+3), और इसी तरह D → E, O → Q, G → J: पहला अक्षर एक स्थान, दूसरा दो और तीसरा तीन स्थान खिसकता है। "
  "HEN बनता है H + 1 = I, E + 2 = G, N + 3 = Q: IGQ। IFO हर अक्षर को एक ही स्थान खिसकाता है; HFP कदमों को +0 से शुरू करता है; GCK अक्षरों को आगे के बजाय पीछे ले जाता है।",
  "lr-cd-each-letter-one-place-further", _cd1)

# 12 -- a product written backwards
def _cd2():
    code = lambda a, b: str(a * b)[::-1]
    assert code(6, 4) == "42" and code(7, 3) == "12"
    return code(8, 9)
N(LR, "Coding-Decoding", "medium",
  "In a certain code, 6 × 4 is written as 42 and 7 × 3 as 12. How is 8 × 9 written in that code?",
  "एक निश्चित कूट में 6 × 4 को 42 और 7 × 3 को 12 लिखा जाता है। उसी कूट में 8 × 9 को कैसे लिखा जाएगा?",
  ["17", "27", "72", "98"], 1,
  "6 × 4 = 24 and 7 × 3 = 21, and the code writes each product with its digits reversed: 42 and 12. 8 × 9 = 72, so the code is 27. "
  "72 is the product itself; 17 adds the two numbers; 98 reverses the two numbers instead of their product.",
  "6 × 4 = 24 और 7 × 3 = 21, और कूट हर गुणनफल को उसके अंक उलटकर लिखता है: 42 और 12। 8 × 9 = 72, इसलिए कूट 27 है। "
  "72 स्वयं गुणनफल है; 17 दोनों संख्याओं को जोड़ता है; 98 गुणनफल के बजाय दोनों संख्याओं को उलट देता है।",
  "lr-cd-product-written-backwards", _cd2)

# 13 -- a die seen twice
def _cp1():
    faces = [1, 2, 3, 4, 5, 6]
    def pairings(items):
        if not items:
            yield []
            return
        first, rest = items[0], items[1:]
        for i, other in enumerate(rest):
            for more in pairings(rest[:i] + rest[i + 1:]):
                yield [(first, other)] + more
    views = [{1, 2, 3}, {1, 4, 5}]
    opposite_one = set()
    for pairs in pairings(faces):
        opp = {a: b for a, b in pairs} | {b: a for a, b in pairs}
        if all(opp[f] not in v for v in views for f in v):
            opposite_one.add(opp[1])
    assert len(opposite_one) == 1
    return str(opposite_one.pop())
N(LR, "Cube Painting", "medium",
  "The six faces of a cube are numbered 1 to 6. In one view of the cube, the faces numbered 1, 2 and 3 can be seen; in another view, the faces numbered 1, 4 and 5. Which number is on the face opposite 1?",
  "एक घन के छह फलकों पर 1 से 6 तक संख्याएँ लिखी हैं। घन के एक दृश्य में 1, 2 और 3 संख्या वाले फलक दिखते हैं; दूसरे दृश्य में 1, 4 और 5 वाले। 1 के सामने वाले फलक पर कौन-सी संख्या है?",
  ["2", "3", "5", "6"], 3,
  "Faces that can be seen together meet at a corner, so none of them is opposite another. The two views put 2, 3, 4 and 5 beside 1, which leaves 6 as the only face never seen with 1: 6 is opposite 1. "
  "Each of 2, 3 and 5 appears next to 1 in a view, so none of them can be opposite it.",
  "एक साथ दिखने वाले फलक एक कोने पर मिलते हैं, इसलिए उनमें से कोई दूसरे के सामने नहीं होता। दोनों दृश्य 2, 3, 4 और 5 को 1 के बगल में दिखाते हैं, जिससे 6 ही ऐसा फलक बचता है जो कभी 1 के साथ नहीं दिखता: 6, 1 के सामने है। "
  "2, 3 और 5 में से हर एक किसी दृश्य में 1 के बगल में दिखता है, इसलिए उनमें से कोई उसके सामने नहीं हो सकता।",
  "lr-cp-die-seen-twice", _cp1)

# 14 -- two 'some' statements
def _sy1():
    regions = list(product((0, 1), repeat=3))        # (doctor, writer, singer)
    one = two = True
    for mask in range(1, 1 << 8):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not any(d and w for d, w, s in full) or not any(w and s for d, w, s in full):
            continue
        one &= any(d and s for d, w, s in full)
        two &= not any(d and s for d, w, s in full)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "medium",
   "Statements: Some doctors are writers. Some writers are singers.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ डॉक्टर लेखक हैं। कुछ लेखक गायक हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some doctors are singers.", "No doctor is a singer."],
   ["कुछ डॉक्टर गायक हैं।", "कोई भी डॉक्टर गायक नहीं है।"], 3,
   "Neither follows. The doctors who are writers and the writers who are singers may be different people, so I need not be true; but they may also be the same people, so II need not be true either. "
   "Two 'some' statements linked only through writers fix nothing about doctors and singers. I and II cannot both be false, yet neither one follows from the statements.",
   "कोई भी नहीं निकलता। जो डॉक्टर लेखक हैं और जो लेखक गायक हैं, वे अलग-अलग लोग हो सकते हैं, इसलिए I का सत्य होना ज़रूरी नहीं; पर वे वही लोग भी हो सकते हैं, इसलिए II का सत्य होना भी ज़रूरी नहीं। "
   "केवल लेखकों के माध्यम से जुड़े दो 'कुछ' वाले कथन डॉक्टरों और गायकों के बारे में कुछ तय नहीं करते। I और II दोनों असत्य नहीं हो सकते, फिर भी कथनों से उनमें से कोई नहीं निकलता।",
   "lr-sy-two-some-statements", roman=True, check=_sy1)

# 15 -- only one statement is true
def _tl1():
    fits = []
    for g in "ABC":
        true = [g == "B", g != "B", g != "C"]        # A: 'B did it'; B: 'I did not'; C: 'I did not'
        if sum(true) == 1:
            fits.append(g)
    return fits[0] if len(fits) == 1 else "Cannot be determined"
N(LR, "Truth-Liar", "hard",
  "Exactly one of three suspects, A, B and C, committed a theft, and exactly one of their three statements is true. A says, 'B did it.' B says, 'I did not do it.' C says, 'I did not do it.' Who committed the theft?",
  "तीन संदिग्धों, A, B और C, में से ठीक एक ने चोरी की, और उनके तीनों कथनों में से ठीक एक सत्य है। A कहता है, 'B ने की।' B कहता है, 'मैंने नहीं की।' C कहता है, 'मैंने नहीं की।' चोरी किसने की?",
  ["A", "B", "C", "Cannot be determined"], 2,
  "Test each suspect. If A did it, B's and C's denials are both true -- two true statements. If B did it, A's accusation and C's denial are true -- two again. If C did it, only B's denial is true, which fits. "
  "So C committed the theft. Believing A's accusation points to B, which leaves two statements true.",
  "हर संदिग्ध को जाँचिए। यदि A ने की, तो B और C दोनों के इनकार सत्य हैं -- दो सत्य कथन। यदि B ने की, तो A का आरोप और C का इनकार सत्य हैं -- फिर दो। यदि C ने की, तो केवल B का इनकार सत्य है, जो शर्त पर खरा है। "
  "अतः चोरी C ने की। A के आरोप पर विश्वास करना B की ओर ले जाता है, जिससे दो कथन सत्य रह जाते हैं।",
  "lr-tl-only-one-statement-true", _tl1,
  opts_hi=["A", "B", "C", "निर्धारित नहीं किया जा सकता"])

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    s1 = [d for i, d in enumerate(days) if days[(i - 2) % 7] == "Monday"]
    s2 = [d for i, d in enumerate(days) if days[(i + 1) % 7] == "Thursday"]
    return _ds(s1, s2, [d for d in s1 if d in s2])
DS(LR, "medium",
   "On which day of the week is the meeting held?",
   "बैठक सप्ताह के किस दिन होती है?",
   "It is held two days after Monday.", "वह सोमवार के दो दिन बाद होती है।",
   "It is held on the day before Thursday.", "वह गुरुवार से एक दिन पहले होती है।",
   1,
   "Two days after Monday is Wednesday, and the day before Thursday is also Wednesday, so either statement alone fixes the day. "
   "The trap is to think that the two must be combined because each gives the day only indirectly.",
   "सोमवार के दो दिन बाद बुधवार है, और गुरुवार से एक दिन पहले भी बुधवार है, इसलिए कोई भी एक कथन अकेले दिन तय कर देता है। "
   "जाल यह सोचना है कि दोनों को मिलाना होगा, क्योंकि हर एक दिन को केवल परोक्ष रूप से बताता है।",
   "lr-ds-meeting-day-either-way", _ds1)

def _ds2():
    orders = list(permutations(["Ram", "Shyam", "Mohan"]))      # tallest first
    taller = lambda o, a, b: o.index(a) < o.index(b)
    s1 = [taller(o, "Ram", "Shyam") for o in orders if taller(o, "Ram", "Mohan")]
    s2 = [taller(o, "Ram", "Shyam") for o in orders if taller(o, "Mohan", "Shyam")]
    both = [taller(o, "Ram", "Shyam") for o in orders if taller(o, "Ram", "Mohan") and taller(o, "Mohan", "Shyam")]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Is Ram taller than Shyam?",
   "क्या राम, श्याम से लंबा है?",
   "Ram is taller than Mohan.", "राम, मोहन से लंबा है।",
   "Mohan is taller than Shyam.", "मोहन, श्याम से लंबा है।",
   2,
   "I alone says nothing about Shyam, and II alone says nothing about Ram. Together, Ram is taller than Mohan, who is taller than Shyam, so Ram is taller than Shyam. Both statements are needed.",
   "I अकेला श्याम के बारे में कुछ नहीं कहता, और II अकेला राम के बारे में कुछ नहीं। दोनों साथ: राम, मोहन से लंबा है, जो श्याम से लंबा है, इसलिए राम, श्याम से लंबा है। दोनों कथन ज़रूरी हैं।",
   "lr-ds-chain-of-heights", _ds2)

def _ds3():
    sizes = range(23, 300)
    s1 = [22 > n - 22 for n in sizes]                            # 22 boys, any class size
    s2 = [n * 55 > n * 45 for n in sizes if n * 45 % 100 == 0]   # girls 45% of a class whose size allows it
    both = [22 > n - 22 for n in sizes if n * 45 % 100 == 0 and n * 55 == 2200]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Are there more boys than girls in the class?",
   "क्या कक्षा में लड़कियों से अधिक लड़के हैं?",
   "There are 22 boys in the class.", "कक्षा में 22 लड़के हैं।",
   "Girls make up 45% of the class.", "कक्षा का 45% भाग लड़कियाँ हैं।",
   0,
   "Statement II alone settles it: if girls are 45% of the class, boys are 55%, so there are more boys. Statement I alone gives the boys but not the girls, who could number 10 or 30. "
   "So the question can be answered using II alone but not using I alone.",
   "कथन II अकेला बात तय कर देता है: यदि लड़कियाँ कक्षा का 45% हैं, तो लड़के 55% हैं, इसलिए लड़के अधिक हैं। कथन I अकेला लड़कों की संख्या देता है पर लड़कियों की नहीं, जो 10 भी हो सकती हैं और 30 भी। "
   "अतः प्रश्न का उत्तर केवल II से दिया जा सकता है, केवल I से नहीं।",
   "lr-ds-a-share-settles-it", _ds3)
