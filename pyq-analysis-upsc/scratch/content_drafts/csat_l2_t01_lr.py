# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 1 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Mix (playbook J.1): statement-conclusion/assumption 3, seating and ranking 3, blood relations 2, directions 2,
coding 2, cube (described in words, no figure) 1, syllogism 1, truth-teller 1, data sufficiency 3.
Difficulty 3 easy / 10 medium / 5 hard. Every arrangement, code, cube count, syllogism and truth-teller
key is found by checking every case in code, which also proves that each puzzle has exactly one answer."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _two(one_follows, two_follows):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one_follows, two_follows)]]

CONC = "Which of the following conclusions follow(s) from the statement?"
CONC_HI = "निम्नलिखित में से कौन-सा/से निष्कर्ष कथन से निकलता/निकलते है/हैं?"

# 1 -- conclusion: contrapositive versus converse
def _sc1():
    one = two = True
    for riya, other in product(product((0, 1), repeat=2), repeat=2):
        if any(a and not s for a, s in (riya, other)) or riya[1]:
            continue                                  # premise: above 90 -> scholarship; Riya got none
        one &= not riya[0]
        two &= all(a for a, s in (riya, other) if s)
    return _two(one, two)
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: Every student who scored above 90 in the test was given a scholarship. Riya was not given a scholarship.\n\n" + CONC,
   "कथन: परीक्षा में 90 से अधिक अंक पाने वाले हर विद्यार्थी को छात्रवृत्ति दी गई। रिया को छात्रवृत्ति नहीं दी गई।\n\n" + CONC_HI,
   ["Riya did not score above 90 in the test.", "Every student who was given a scholarship scored above 90."],
   ["रिया ने परीक्षा में 90 से अधिक अंक नहीं पाए।", "छात्रवृत्ति पाने वाले हर विद्यार्थी ने 90 से अधिक अंक पाए।"], 0,
   "Only I follows. If Riya had scored above 90, the rule would have given her a scholarship; she did not get one, so she did not score above 90 -- the contrapositive of the rule. "
   "II reverses the rule: the statement says who must get a scholarship, not that nobody else can; students with lower marks may have got one on other grounds.",
   "केवल I निकलता है। यदि रिया के 90 से अधिक अंक होते, तो नियम के अनुसार उसे छात्रवृत्ति मिलती; उसे नहीं मिली, इसलिए उसके 90 से अधिक अंक नहीं थे -- यह नियम का प्रतिधनात्मक (contrapositive) रूप है। "
   "II नियम को उलट देता है: कथन बताता है कि किसे छात्रवृत्ति अवश्य मिलेगी, यह नहीं कि किसी और को नहीं मिल सकती; कम अंक वाले विद्यार्थियों को अन्य आधारों पर मिली हो सकती है।",
   "lr-sc-scholarship-contrapositive", roman=True, check=_sc1)

# 2 -- linear seating
def _sa1():
    sols = []
    for row in permutations("PQRSTU"):
        pos = {p: i for i, p in enumerate(row)}
        if pos["R"] != 2 or pos["P"] != 3 or pos["S"] not in (0, 5):
            continue
        if pos["Q"] - pos["T"] != 1 or abs(pos["U"] - pos["S"]) != 1 or pos["Q"] in (0, 5):
            continue
        sols.append(row)
    assert len(sols) == 1, sols
    return sols[0][4]
T(LR, "Seating Arrangement", "medium",
  "Six friends P, Q, R, S, T and U sit in a row, all facing north. R is third from the left end, and P sits to the immediate right of R. S sits at one of the ends, and U sits next to S. "
  "T sits to the immediate left of Q, and Q is not at either end. Who sits second from the right end?",
  "छह मित्र P, Q, R, S, T और U एक पंक्ति में उत्तर की ओर मुँह करके बैठे हैं। R बाएँ छोर से तीसरा है, और P, R के ठीक दाएँ बैठा है। S किसी एक छोर पर बैठा है, और U, S के बगल में बैठा है। "
  "T, Q के ठीक बाएँ बैठा है, और Q किसी भी छोर पर नहीं है। दाएँ छोर से दूसरा कौन बैठा है?",
  ["U", "P", "Q", "T"], ["U", "P", "Q", "T"], 0,
  "R and P take the 3rd and 4th seats. The pair 'T, Q' must fill two neighbouring free seats with T on the left: seats 1-2 or seats 5-6. Seats 5-6 would put Q at the right end, which is not allowed, "
  "so T and Q take seats 1 and 2. S must then take an end, and the left end is taken, so S is in seat 6 with U beside it in seat 5. The row is T Q R P U S, and U is second from the right. "
  "P is second from the right only if one forgets that U must sit next to S.",
  "R और P तीसरे और चौथे स्थान पर हैं। 'T, Q' की जोड़ी को दो पास-पास के ख़ाली स्थान लेने हैं, T बाईं ओर: स्थान 1-2 या 5-6। स्थान 5-6 पर Q दाएँ छोर पर होगा, जिसकी अनुमति नहीं है, "
  "इसलिए T और Q स्थान 1 और 2 पर हैं। तब S को एक छोर लेना है और बायाँ छोर भर चुका है, इसलिए S स्थान 6 पर और उसके बगल में U स्थान 5 पर है। पंक्ति T Q R P U S है, और दाएँ से दूसरा U है। "
  "P दाएँ से दूसरा तभी लगेगा जब यह भुला दिया जाए कि U को S के बगल में बैठना है।",
  "lr-sa-six-in-a-row", check=_sa1)

# 3 -- easy conclusion: neither follows
S2(LR, "Statement-Conclusion/Assumption", "easy",
   "Statement: Ravi always carries an umbrella when he goes out.\n\n" + CONC,
   "कथन: रवि बाहर जाते समय सदा छाता साथ रखता है।\n\n" + CONC_HI,
   ["It rains every day in the town where Ravi lives.", "Ravi does not own a raincoat."],
   ["रवि जिस नगर में रहता है वहाँ हर दिन वर्षा होती है।", "रवि के पास बरसाती (रेनकोट) नहीं है।"], 3,
   "Neither follows. Carrying an umbrella every time shows a habit or caution, not daily rain: people carry umbrellas against the sun or a chance of rain. "
   "Nor does it say anything about a raincoat: he may own one and still prefer an umbrella. Both conclusions read more into the statement than it says.",
   "कोई भी नहीं निकलता। हर बार छाता रखना आदत या सावधानी दिखाता है, हर दिन वर्षा नहीं: लोग धूप से या वर्षा की संभावना से बचने के लिए भी छाता रखते हैं। "
   "न ही कथन बरसाती के बारे में कुछ कहता है: उसके पास बरसाती हो सकती है, फिर भी वह छाता पसंद करता हो। दोनों निष्कर्ष कथन से अधिक पढ़ लेते हैं।",
   "lr-sc-umbrella-neither", roman=True)

# 4 -- coded blood relation
T(LR, "Blood Relation", "hard",
  "In a code, 'A + B' means A is the father of B, 'A - B' means A is the wife of B, and 'A × B' means A is the brother of B. If P × Q - R + S, how is P related to S?",
  "एक कूट में 'A + B' का अर्थ है A, B का पिता है; 'A - B' का अर्थ है A, B की पत्नी है; और 'A × B' का अर्थ है A, B का भाई है। यदि P × Q - R + S, तो P का S से क्या संबंध है?",
  ["Maternal uncle", "Paternal uncle", "Brother", "Father"], ["मामा", "चाचा", "भाई", "पिता"], 0,
  "Read the chain from the right: R + S means R is the father of S; Q - R means Q is R's wife, so Q is S's mother; P × Q means P is Q's brother. "
  "P is the brother of S's mother, that is S's maternal uncle. 'Paternal uncle' would need P to be the father's brother -- the trap of attaching P to R instead of Q.",
  "शृंखला को दाईं ओर से पढ़िए: R + S का अर्थ है R, S का पिता है; Q - R का अर्थ है Q, R की पत्नी है, इसलिए Q, S की माता है; P × Q का अर्थ है P, Q का भाई है। "
  "P, S की माता का भाई, यानी S का मामा, है। 'चाचा' के लिए P को पिता का भाई होना चाहिए -- यही जाल है, P को Q के बजाय R से जोड़ देना।",
  "lr-br-coded-maternal-uncle")

# 5 -- ranking
N(LR, "Seating Arrangement", "easy",
  "In a class of 40 students, Asha is 12th from the top. Bina is 5 ranks below Asha. What is Bina's rank from the bottom?",
  "40 विद्यार्थियों की एक कक्षा में आशा ऊपर से 12वें स्थान पर है। बीना, आशा से 5 स्थान नीचे है। नीचे से बीना का स्थान क्या है?",
  ["23", "24", "25", "29"], 1,
  "Bina is 12 + 5 = 17th from the top. Counting from the bottom, rank = total - rank from top + 1 = 40 - 17 + 1 = 24. "
  "23 forgets the '+ 1'; 25 adds it twice; 29 = 40 - 12 + 1 is Asha's rank from the bottom.",
  "बीना ऊपर से 12 + 5 = 17वें स्थान पर है। नीचे से गिनने पर स्थान = कुल - ऊपर से स्थान + 1 = 40 - 17 + 1 = 24। "
  "23 में '+ 1' भूल गए हैं; 25 उसे दो बार जोड़ता है; 29 = 40 - 12 + 1, आशा का नीचे से स्थान है।",
  "lr-sa-rank-from-bottom", lambda: str(40 - (12 + 5) + 1))

# 6 -- directions
def _dd1():
    x, y = 0, 0
    y += 6; x += 8; y -= 12
    dist = (x * x + y * y) ** 0.5
    return f"{dist:g} km to the south-east" if x > 0 and y < 0 else "?"
T(LR, "Direction & Distance", "medium",
  "Starting from a point O, a man walks 6 km north, turns right and walks 8 km, then turns right again and walks 12 km. How far is he from O, and in which direction?",
  "एक व्यक्ति बिंदु O से चलकर 6 किमी उत्तर की ओर जाता है, दाएँ मुड़कर 8 किमी चलता है, फिर दोबारा दाएँ मुड़कर 12 किमी चलता है। वह O से कितनी दूर और किस दिशा में है?",
  ["10 km to the south-east", "10 km to the north-east", "14 km to the south-east", "26 km to the south"],
  ["दक्षिण-पूर्व में 10 किमी", "उत्तर-पूर्व में 10 किमी", "दक्षिण-पूर्व में 14 किमी", "दक्षिण में 26 किमी"], 0,
  "Facing north, a right turn faces east, and a second right turn faces south. He ends 8 km east of O and 12 - 6 = 6 km south of it, so he is √(8² + 6²) = 10 km away, to the south-east. "
  "North-east forgets that the 12 km south overshoots the 6 km north; 14 km adds 8 and 6 instead of using the right triangle; 26 km is the total distance walked.",
  "उत्तर की ओर मुँह होने पर दाएँ मुड़ने से मुँह पूर्व की ओर, और दोबारा दाएँ मुड़ने से दक्षिण की ओर हो जाता है। अंत में वह O से 8 किमी पूर्व और 12 - 6 = 6 किमी दक्षिण में है, इसलिए दूरी √(8² + 6²) = 10 किमी, दक्षिण-पूर्व में। "
  "उत्तर-पूर्व यह भूल जाता है कि दक्षिण के 12 किमी उत्तर के 6 किमी से आगे निकल जाते हैं; 14 किमी समकोण त्रिभुज के बजाय 8 और 6 जोड़ देता है; 26 किमी कुल चली गई दूरी है।",
  "lr-dd-north-right-right", check=_dd1)

# 7 -- syllogism
def _sy1():
    regions = list(product((0, 1), repeat=4))           # (poet, dreamer, teacher, lazy)
    one = two = True
    for mask in range(1, 1 << 16):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(p and not d for p, d, t, l in full):            # all poets are dreamers
            continue
        if not any(d and t for p, d, t, l in full):            # some dreamers are teachers
            continue
        if any(t and l for p, d, t, l in full):                # no teacher is lazy
            continue
        one &= any(p and t for p, d, t, l in full)
        two &= any(d and not l for p, d, t, l in full)
    return _two(one, two)
S2(LR, "Syllogism", "medium",
   "Statements: All poets are dreamers. Some dreamers are teachers. No teacher is lazy.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी कवि स्वप्नदर्शी हैं। कुछ स्वप्नदर्शी शिक्षक हैं। कोई भी शिक्षक आलसी नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some poets are teachers.", "Some dreamers are not lazy."],
   ["कुछ कवि शिक्षक हैं।", "कुछ स्वप्नदर्शी आलसी नहीं हैं।"], 1,
   "Only II follows. The dreamers who are teachers cannot be lazy, because no teacher is lazy, so at least some dreamers are not lazy. "
   "I does not follow: the poets lie inside the dreamers, but the dreamers who teach may all be non-poets, so a diagram with no poet-teacher satisfies every statement.",
   "केवल II निकलता है। जो स्वप्नदर्शी शिक्षक हैं वे आलसी नहीं हो सकते, क्योंकि कोई शिक्षक आलसी नहीं है; अतः कम से कम कुछ स्वप्नदर्शी आलसी नहीं हैं। "
   "I नहीं निकलता: कवि स्वप्नदर्शियों के भीतर हैं, पर पढ़ाने वाले स्वप्नदर्शी सब के सब ग़ैर-कवि हो सकते हैं, इसलिए ऐसा आरेख जिसमें कोई कवि-शिक्षक न हो, सभी कथनों को संतुष्ट करता है।",
   "lr-sy-poets-dreamers-teachers", roman=True, check=_sy1)

# 8 -- coding by reversal and shift
def _code(w):
    return "".join(chr((ord(ch) - 65 + 1) % 26 + 65) for ch in w[::-1])
assert _code("MOBILE") == "FMJCPN"
T(LR, "Coding-Decoding", "medium",
  "In a certain code, MOBILE is written as FMJCPN. How is TABLET written in that code?",
  "एक निश्चित कूट में MOBILE को FMJCPN लिखा जाता है। उसी कूट में TABLET को कैसे लिखा जाएगा?",
  ["UFMCBU", "UBCMFU", "SDKAZS", "UFMCBV"], ["UFMCBU", "UBCMFU", "SDKAZS", "UFMCBV"], 0,
  "The code reverses the word and then moves every letter one place forward: MOBILE reversed is ELIBOM, and E->F, L->M, I->J, B->C, O->P, M->N gives FMJCPN. "
  "TABLET reversed is TELBAT, which becomes UFMCBU. UBCMFU shifts without reversing; SDKAZS reverses but shifts backwards; UFMCBV changes the last letter twice.",
  "कूट शब्द को उलटता है और फिर हर अक्षर को एक स्थान आगे बढ़ाता है: MOBILE उलटने पर ELIBOM, और E->F, L->M, I->J, B->C, O->P, M->N से FMJCPN बनता है। "
  "TABLET उलटने पर TELBAT, जो UFMCBU बन जाता है। UBCMFU उलटे बिना आगे बढ़ाता है; SDKAZS उलटता है पर पीछे की ओर खिसकाता है; UFMCBV अंतिम अक्षर को दो बार बदल देता है।",
  "lr-cd-reverse-and-shift", check=lambda: _code("TABLET"))

# 9 -- circular seating, facing the centre
def _sa2():
    # Seats 0-5 numbered clockwise, A fixed at seat 0 (a rotation of the table is the same seating).
    # For someone facing the centre, the right-hand neighbour is the anticlockwise one.
    right = lambda i: (i - 1) % 6
    left = lambda i: (i + 1) % 6
    sols = []
    for rest in permutations(range(1, 6)):
        seat = dict(zip("ABCDEF", (0,) + rest))
        if (seat["D"] - seat["A"]) % 6 != 3 or seat["B"] != right(seat["A"]):
            continue
        if seat["C"] != left(left(seat["B"])) or seat["F"] in (left(seat["C"]), right(seat["C"])):
            continue
        sols.append(seat)
    assert len(sols) == 1, sols
    at = {v: k for k, v in sols[0].items()}
    return at[left(sols[0]["D"])]
T(LR, "Seating Arrangement", "hard",
  "Six persons A, B, C, D, E and F sit around a circular table, all facing the centre. A sits opposite D. B sits to the immediate right of A. C sits second to the left of B. F does not sit next to C. "
  "Who sits to the immediate left of D?",
  "छह व्यक्ति A, B, C, D, E और F एक वृत्ताकार मेज़ के चारों ओर केंद्र की ओर मुँह करके बैठे हैं। A, D के ठीक सामने बैठा है। B, A के ठीक दाएँ बैठा है। C, B के बाएँ से दूसरे स्थान पर बैठा है। F, C के बगल में नहीं बैठा है। "
  "D के ठीक बाएँ कौन बैठा है?",
  ["F", "E", "B", "C"], ["F", "E", "B", "C"], 0,
  "Place A anywhere; D is directly opposite. For people facing the centre, one's right is the anticlockwise neighbour, so B is the anticlockwise neighbour of A. Second to the left of B means two seats clockwise from B, "
  "which is the seat just clockwise of A, so C sits beside A. The two seats left are both next to D; F cannot sit beside C, so F takes the one away from C and E the one between C and D. "
  "Going clockwise: A, C, E, D, F, B. D's left is the clockwise neighbour, F. E is D's right-hand neighbour -- the trap of reading left and right as if looking at the table from outside.",
  "A को कहीं भी रखिए; D ठीक सामने है। केंद्र की ओर मुँह किए व्यक्ति का दायाँ, वामावर्त (anticlockwise) पड़ोसी होता है, इसलिए B, A का वामावर्त पड़ोसी है। B के बाएँ से दूसरा यानी B से दो स्थान दक्षिणावर्त, "
  "जो A के ठीक दक्षिणावर्त वाला स्थान है, इसलिए C, A के बगल में है। बचे दोनों स्थान D के बगल में हैं; F, C के बगल में नहीं बैठ सकता, इसलिए F, C से दूर वाला स्थान लेता है और E, C और D के बीच वाला। "
  "दक्षिणावर्त क्रम: A, C, E, D, F, B। D का बायाँ उसका दक्षिणावर्त पड़ोसी, F, है। E, D का दाएँ वाला पड़ोसी है -- जाल यह है कि बाएँ-दाएँ को बाहर से मेज़ देखकर पढ़ा जाए।",
  "lr-sa-circle-facing-centre", check=_sa2)

# 10 -- cube painted on five faces
def _cp1():
    n = 4
    painted = lambda x, y, z: x in (0, n - 1) or y in (0, n - 1) or z == n - 1    # every face but the bottom (z = 0)
    return str(sum(1 for x in range(n) for y in range(n) for z in range(n) if not painted(x, y, z)))
N(LR, "Cube Painting", "hard",
  "A wooden cube of side 4 cm is painted on all its faces except the bottom face, and is then cut into 64 cubes of side 1 cm. How many of the small cubes have no paint on any face?",
  "4 सेमी भुजा वाले लकड़ी के एक घन के निचले फलक को छोड़कर सभी फलकों को रंगा जाता है, और फिर उसे 1 सेमी भुजा वाले 64 घनों में काटा जाता है। कितने छोटे घनों के किसी भी फलक पर रंग नहीं है?",
  ["8", "12", "16", "24"], 1,
  "A small cube is unpainted if it is away from the four side faces and the top. Away from the sides means one of the middle 2 × 2 columns; away from the top means one of the lower 3 layers, "
  "including the bottom layer, whose bottom face was left bare. That gives 2 × 2 × 3 = 12. 8 is the usual (n - 2)³ for a cube painted all over; 16 counts the whole bottom layer; 24 adds the two.",
  "छोटा घन तब बिना रंग का है जब वह चारों पार्श्व फलकों और ऊपरी फलक से दूर हो। पार्श्व फलकों से दूर यानी बीच के 2 × 2 स्तंभों में से एक; ऊपर से दूर यानी नीचे की 3 परतों में से एक, "
  "जिसमें सबसे निचली परत भी है, क्योंकि उसका निचला फलक रंगा नहीं गया। इस तरह 2 × 2 × 3 = 12। 8 पूरे रंगे घन का सामान्य (n - 2)³ है; 16 पूरी निचली परत गिनता है; 24 दोनों जोड़ता है।",
  "lr-cp-five-faces-painted", _cp1)

# 11 -- assumptions: both implicit
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: An advertisement says, 'Learn to speak English with confidence in 30 days -- join our evening classes.'\n\n"
   "Which of the following assumptions is/are implicit in the statement?",
   "कथन: एक विज्ञापन कहता है, '30 दिनों में आत्मविश्वास के साथ अंग्रेज़ी बोलना सीखिए -- हमारी सायंकालीन कक्षाओं में शामिल होइए।'\n\n"
   "निम्नलिखित में से कौन-सी/से पूर्वधारणा/एँ कथन में अंतर्निहित है/हैं?",
   ["Some people want to speak English with more confidence.", "Some of those people are able to attend classes in the evening."],
   ["कुछ लोग अधिक आत्मविश्वास के साथ अंग्रेज़ी बोलना चाहते हैं।", "उनमें से कुछ लोग शाम को कक्षाओं में आ सकते हैं।"], 2,
   "Both are implicit. An advertiser offers a course only if it believes someone wants it (I), and fixes the classes in the evening only if it believes enough of its customers can come then (II). "
   "Neither assumption claims that everyone wants the course or that 30 days is enough, which would be stronger claims than the advertisement needs.",
   "दोनों अंतर्निहित हैं। विज्ञापनदाता कोई पाठ्यक्रम तभी देता है जब उसे विश्वास हो कि किसी को उसकी ज़रूरत है (I), और कक्षाएँ शाम को तभी रखता है जब उसे लगे कि उसके पर्याप्त ग्राहक उस समय आ सकते हैं (II)। "
   "कोई भी पूर्वधारणा यह दावा नहीं करती कि हर व्यक्ति पाठ्यक्रम चाहता है या 30 दिन पर्याप्त हैं; ये विज्ञापन की ज़रूरत से बड़े दावे होते।",
   "lr-sc-advertisement-assumptions", roman=True)

# 12 -- truth-tellers and liars
def _tl1():
    sols = []
    for p, q, r in product((True, False), repeat=3):     # True = always tells the truth
        says = {"P": not q, "Q": (not p) and (not r), "R": q}
        if says["P"] == p and says["Q"] == q and says["R"] == r:
            sols.append((p, q, r))
    assert len(sols) == 1, sols
    p, q, r = sols[0]
    names = [n for n, t in zip("PQR", (p, q, r)) if t]
    return {("P",): "P only", ("R",): "R only", ("P", "R"): "P and R", ("Q",): "Q only"}[tuple(names)]
T(LR, "Truth-Liar", "hard",
  "Each of P, Q and R either always tells the truth or always lies. P says, 'Q is a liar.' Q says, 'P and R are both liars.' R says, 'Q tells the truth.' Who tells the truth?",
  "P, Q और R में से हर एक या तो सदा सच बोलता है या सदा झूठ। P कहता है, 'Q झूठा है।' Q कहता है, 'P और R दोनों झूठे हैं।' R कहता है, 'Q सच बोलता है।' कौन सच बोलता है?",
  ["P only", "R only", "P and R", "Q only"], ["केवल P", "केवल R", "P और R", "केवल Q"], 0,
  "Suppose Q tells the truth. Then P and R are both liars, but R's statement 'Q tells the truth' would then be true, which a liar cannot say -- a contradiction. So Q lies. "
  "Then P's statement 'Q is a liar' is true, so P tells the truth, and R's statement 'Q tells the truth' is false, so R lies. Check Q: 'P and R are both liars' is false, as a liar's statement must be. Only P tells the truth.",
  "मान लीजिए Q सच बोलता है। तब P और R दोनों झूठे हैं, पर तब R का कथन 'Q सच बोलता है' सच होगा, जो झूठा नहीं कह सकता -- विरोधाभास। अतः Q झूठ बोलता है। "
  "तब P का कथन 'Q झूठा है' सच है, इसलिए P सच बोलता है, और R का कथन 'Q सच बोलता है' झूठा है, इसलिए R झूठ बोलता है। Q की जाँच: 'P और R दोनों झूठे हैं' झूठा है, जैसा झूठे का कथन होना चाहिए। केवल P सच बोलता है।",
  "lr-tl-three-statements", check=_tl1)

# 13 -- easy blood relation
T(LR, "Blood Relation", "easy",
  "Pointing to a man in a photograph, Meena said, 'His mother is the only daughter of my mother.' How is Meena related to the man?",
  "एक फ़ोटो में एक पुरुष की ओर इशारा करते हुए मीना ने कहा, 'इसकी माँ मेरी माँ की इकलौती बेटी है।' मीना का उस पुरुष से क्या संबंध है?",
  ["Mother", "Sister", "Aunt", "Grandmother"], ["माँ", "बहन", "मौसी", "नानी"], 0,
  "Meena is a daughter of her own mother, so 'the only daughter of my mother' is Meena herself. The man's mother is therefore Meena: she is his mother. "
  "'Aunt' would need the only daughter to be someone other than Meena, which 'only' rules out; 'Grandmother' would be Meena's mother.",
  "मीना अपनी माँ की बेटी है, इसलिए 'मेरी माँ की इकलौती बेटी' स्वयं मीना है। अतः उस पुरुष की माँ मीना है: वह उसकी माँ है। "
  "'मौसी' के लिए इकलौती बेटी मीना के अलावा कोई और होनी चाहिए, जिसे 'इकलौती' शब्द नकारता है; 'नानी' मीना की माँ होगी।",
  "lr-br-only-daughter-of-my-mother")

# 14 -- shadows in the morning
def _dd2():
    # Morning: the sun is in the east, so shadows point west.
    face = {"north": (0, 1), "south": (0, -1), "east": (1, 0), "west": (-1, 0)}
    right_of = {"north": "east", "east": "south", "south": "west", "west": "north"}
    arun = next(f for f in face if right_of[f] == "west")
    bala = {"north": "south", "south": "north", "east": "west", "west": "east"}[arun]
    return bala.capitalize()
T(LR, "Direction & Distance", "medium",
  "One morning after sunrise, Arun and Bala stand facing each other. Arun's shadow falls exactly to his right. Which direction is Bala facing?",
  "एक सुबह सूर्योदय के बाद अरुण और बाला एक-दूसरे की ओर मुँह करके खड़े हैं। अरुण की परछाईं ठीक उसके दाईं ओर पड़ती है। बाला किस दिशा की ओर मुँह किए है?",
  ["North", "South", "East", "West"], ["उत्तर", "दक्षिण", "पूर्व", "पश्चिम"], 0,
  "In the morning the sun is in the east, so shadows fall to the west. Arun's right is west, which means he faces south. Bala faces Arun, so Bala faces north. "
  "South is Arun's own direction, the trap of answering for the wrong person; east and west mix up the sun's side with the shadow's.",
  "सुबह सूर्य पूर्व में होता है, इसलिए परछाइयाँ पश्चिम की ओर पड़ती हैं। अरुण का दायाँ पश्चिम है, यानी वह दक्षिण की ओर मुँह किए है। बाला, अरुण की ओर मुँह किए है, इसलिए वह उत्तर की ओर है। "
  "दक्षिण स्वयं अरुण की दिशा है -- गलत व्यक्ति के लिए उत्तर देने का जाल; पूर्व और पश्चिम सूर्य की दिशा और परछाईं की दिशा को उलझा देते हैं।",
  "lr-dd-morning-shadow-facing", check=_dd2)

# 15 -- number coding from sentences
def _cd2():
    msgs = {("sky", "is", "blue"): {28, 15, 61}, ("blue", "sea", "is", "deep"): {61, 72, 15, 40}, ("deep", "sky"): {40, 28}}
    words = {w for m in msgs for w in m}
    for perm in permutations([15, 28, 40, 61, 72], len(words)):
        code = dict(zip(sorted(words), perm))
        if all({code[w] for w in m} == v for m, v in msgs.items()):
            return str(code["sea"])
N(LR, "Coding-Decoding", "medium",
  "In a certain code, 'sky is blue' is written as '28 15 61', 'blue sea is deep' as '61 72 15 40', and 'deep sky' as '40 28'. What is the code for 'sea'?",
  "एक निश्चित कूट में 'sky is blue' को '28 15 61', 'blue sea is deep' को '61 72 15 40', और 'deep sky' को '40 28' लिखा जाता है। 'sea' का कूट क्या है?",
  ["15", "28", "40", "72"], 3,
  "'deep sky' is 40 28, and 'sky' also appears in 'sky is blue' (28 15 61), so sky = 28 and deep = 40. In 'blue sea is deep', 'blue' and 'is' share the codes 15 and 61 with the first sentence, "
  "and deep is 40, so the code left for 'sea' is 72. The codes of 'blue' and 'is' cannot be told apart, but the question does not need them.",
  "'deep sky' 40 28 है, और 'sky', 'sky is blue' (28 15 61) में भी है, इसलिए sky = 28 और deep = 40। 'blue sea is deep' में 'blue' और 'is' के कूट 15 और 61 पहले वाक्य से साझा हैं, "
  "और deep 40 है, इसलिए 'sea' के लिए बचा कूट 72 है। 'blue' और 'is' के कूट अलग-अलग पहचाने नहीं जा सकते, पर प्रश्न को उनकी ज़रूरत नहीं।",
  "lr-cd-sentence-number-code", _cd2)

# ---- the data-sufficiency block's three Reasoning items
def _dsl1():
    people = "PQRST"
    orders = list(permutations(people))                          # tallest first
    h = lambda o, x: len(o) - o.index(x)
    s1 = [o for o in orders if h(o, "P") > h(o, "Q") and h(o, "P") > h(o, "R") and h(o, "P") < h(o, "S")]
    s2 = [o for o in orders if h(o, "T") > h(o, "Q")]
    both = [o for o in s1 if o in s2]
    top = lambda os: {o[0] for o in os}
    alone = (len(top(s1)) == 1, len(top(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(top(both)) == 1 else "d"
DS(LR, "medium",
   "Among five friends P, Q, R, S and T, all of different heights, who is the tallest?",
   "अलग-अलग ऊँचाई वाले पाँच मित्रों P, Q, R, S और T में सबसे लंबा कौन है?",
   "P is taller than Q and R, but shorter than S.", "P, Q और R से लंबा है, पर S से छोटा है।",
   "T is taller than Q.", "T, Q से लंबा है।",
   3,
   "Statement I puts S above P, and P above Q and R, but says nothing about T, who may be taller or shorter than S. Statement II only places T above Q. "
   "Together: S > P > Q and R, and T > Q -- still T may stand above S or anywhere below it, so the tallest can be S or T. The question cannot be answered even with both. "
   "The trap is to assume that a person not mentioned in Statement I must be shorter.",
   "कथन I, S को P से ऊपर और P को Q तथा R से ऊपर रखता है, पर T के बारे में कुछ नहीं कहता, जो S से लंबा या छोटा हो सकता है। कथन II केवल T को Q से ऊपर रखता है। "
   "दोनों साथ: S > P > Q और R, तथा T > Q -- फिर भी T, S से ऊपर या उससे नीचे कहीं भी हो सकता है, इसलिए सबसे लंबा S या T हो सकता है। दोनों के साथ भी प्रश्न का उत्तर नहीं दिया जा सकता। "
   "जाल यह है कि कथन I में जिसका उल्लेख नहीं, उसे छोटा मान लिया जाए।",
   "lr-ds-tallest-of-five", _dsl1)

def _dsl2():
    import datetime as dt
    years = range(2001, 2061)
    sunday = 6
    from_i = {dt.date(y, 3, 15).weekday() for y in years if dt.date(y, 3, 1).weekday() == sunday}
    from_ii = {dt.date(y, 3, 15).weekday() for y in years if dt.date(y, 3, 29).weekday() == sunday}
    alone = (len(from_i) == 1, len(from_ii) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c"
DS(LR, "hard",
   "On what day of the week did 15 March fall in a certain year?",
   "किसी वर्ष 15 मार्च को सप्ताह का कौन-सा दिन था?",
   "1 March of that year was a Sunday.", "उस वर्ष 1 मार्च को रविवार था।",
   "29 March of that year was a Sunday.", "उस वर्ष 29 मार्च को रविवार था।",
   1,
   "15 March is exactly 14 days -- two weeks -- after 1 March and 14 days before 29 March, and leap years do not matter because February is not crossed. "
   "So either statement alone tells us that 15 March was a Sunday. The trap is to think a single date cannot fix the day without the year, or to insist on both dates.",
   "15 मार्च, 1 मार्च से ठीक 14 दिन -- दो सप्ताह -- बाद और 29 मार्च से 14 दिन पहले है, और लीप वर्ष का कोई असर नहीं, क्योंकि फ़रवरी बीच में नहीं आती। "
   "इसलिए कोई भी एक कथन अकेला बता देता है कि 15 मार्च को रविवार था। जाल यह है कि वर्ष के बिना एक तारीख़ से दिन तय न होने की बात सोची जाए, या दोनों तारीख़ों पर अड़ा जाए।",
   "lr-ds-day-of-15-march", _dsl2)

DS(LR, "medium",
   "How is Kavita related to Suresh?",
   "कविता का सुरेश से क्या संबंध है?",
   "Kavita is the daughter of Suresh's only brother.", "कविता, सुरेश के इकलौते भाई की बेटी है।",
   "Suresh's son is Kavita's cousin.", "सुरेश का बेटा कविता का कज़िन (चचेरा, ममेरा, फुफेरा या मौसेरा भाई) है।",
   0,
   "Statement I alone settles it: the daughter of Suresh's brother is Suresh's niece (his brother's daughter). Statement II alone does not: a cousin can be related through either parent, "
   "so Kavita could be the daughter of Suresh's brother or sister (his niece) or of his wife's brother or sister (his wife's niece). So one statement alone answers the question, and the other does not.",
   "कथन I अकेला उत्तर दे देता है: सुरेश के भाई की बेटी सुरेश की भतीजी है। कथन II अकेला नहीं दे पाता: चचेरा-ममेरा संबंध माता या पिता किसी की भी ओर से हो सकता है, "
   "इसलिए कविता सुरेश के भाई या बहन की बेटी (उसकी भतीजी या भांजी) या उसकी पत्नी के भाई या बहन की बेटी हो सकती है। अतः एक कथन अकेला उत्तर देता है, और दूसरा नहीं।",
   "lr-ds-kavita-suresh-relation")
