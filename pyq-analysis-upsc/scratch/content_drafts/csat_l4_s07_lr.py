# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 7 -- Logical Reasoning (15 items: 12 in the Reasoning slots, 3 in the data-sufficiency block).

Layout A, the lighter 2023/2024 Reasoning section. Exam-level mix (8 medium / 7 hard), with none of the shapes of
Levels 1-3 or Simulators 1-6: a question answered with a different one, marks asked for on the grounds of effort, the
assumption a plan for more litter bins needs, two arguments about a ban on cars; five flags on a pole, the order of a
bus's stops; a son's wife's mother-in-law; the first and last letters multiplied, each letter ranked within its word;
a walk that begins towards the evening sun; poets who are not engineers; the cubes that touch a cube's centre; and in
the data-sufficiency block a town to the north-east, a code given by its rule or by an example, and a brother who may
or may not be the eldest. Arrangement, relation, code, direction and syllogism keys are found by checking every
case."""
from itertools import combinations, permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a question answered with a different one
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Asked why a new district hospital is two years behind schedule, a minister replies: 'The previous government did not build a single hospital in this district in ten years.' Which one of the following best describes the flaw in the reply?",
  "यह पूछे जाने पर कि एक नया ज़िला अस्पताल दो वर्ष पीछे क्यों है, एक मंत्री उत्तर देता है: 'पिछली सरकार ने दस वर्षों में इस ज़िले में एक भी अस्पताल नहीं बनाया।' निम्नलिखित में से कौन-सा उत्तर की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It answers a different question from the one that was asked.",
   "It assumes that a hospital two years late will never be finished at all.",
   "It treats the views of most voters as proof of what is true.",
   "It draws a conclusion about every district from what happened in one."],
  ["यह पूछे गए प्रश्न के बजाय किसी दूसरे प्रश्न का उत्तर देता है।",
   "यह मान लेता है कि दो वर्ष पीछे चल रहा अस्पताल कभी पूरा ही नहीं होगा।",
   "यह अधिकांश मतदाताओं के विचारों को सत्य का प्रमाण मान लेता है।",
   "यह एक ज़िले में हुई घटना से हर ज़िले के बारे में निष्कर्ष निकाल लेता है।"],
  0,
  "The question was why this hospital is late. The reply says nothing about the delay; it turns attention to what an earlier government failed to do, which may be true but does not explain or excuse the present delay. "
  "It makes no claim that the hospital will never be finished, appeals to no opinion of voters, and draws no conclusion about other districts.",
  "प्रश्न यह था कि यह अस्पताल पीछे क्यों है। उत्तर देरी के बारे में कुछ नहीं कहता; वह ध्यान इस ओर मोड़ देता है कि पिछली सरकार ने क्या नहीं किया, जो सत्य हो सकता है पर वर्तमान देरी को न समझाता है न उचित ठहराता है। "
  "वह यह दावा नहीं करता कि अस्पताल कभी पूरा नहीं होगा, मतदाताओं की किसी राय का सहारा नहीं लेता, और अन्य ज़िलों के बारे में कोई निष्कर्ष नहीं निकालता।",
  "lr-sc-a-question-answered-with-a-different-one", pos=0)

# 2 -- marks asked for on the grounds of effort
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A student writes to an examiner: 'I studied for twelve hours a day for this examination, and I will be heartbroken if I fail. Please raise my marks.' Which one of the following best describes the weakness of this appeal?",
  "एक विद्यार्थी परीक्षक को लिखता है: 'मैंने इस परीक्षा के लिए रोज़ बारह घंटे पढ़ाई की, और यदि मैं अनुत्तीर्ण हुआ तो मेरा दिल टूट जाएगा। कृपया मेरे अंक बढ़ा दीजिए।' निम्नलिखित में से कौन-सा इस अनुरोध की कमज़ोरी का सबसे अच्छा वर्णन करता है?",
  ["It assumes that other students did not study as hard as the writer did.",
   "It wrongly claims that the examiner made a mistake in adding up the marks.",
   "It argues that the examination was unfair to all the students who took it.",
   "It rests on effort and feelings, which do not bear on what the answers deserve."],
  ["यह मान लेता है कि अन्य विद्यार्थियों ने लिखने वाले जितनी मेहनत नहीं की।",
   "यह ग़लत दावा करता है कि परीक्षक ने अंक जोड़ने में भूल की।",
   "यह तर्क देता है कि परीक्षा उसमें बैठे सभी विद्यार्थियों के साथ अनुचित थी।",
   "यह मेहनत और भावनाओं पर टिका है, जिनका उत्तरों की योग्यता से कोई संबंध नहीं।"],
  0,
  "Marks are meant to reflect the quality of the answers written. How long the student studied and how the student would feel about failing may be real, but neither shows that any answer deserved more marks; the appeal asks for a reward on grounds that have nothing to do with the work being judged. "
  "It makes no comparison with other students, claims no error in totalling, and raises no complaint about the examination itself.",
  "अंक लिखे गए उत्तरों की गुणवत्ता दर्शाने के लिए होते हैं। विद्यार्थी ने कितनी देर पढ़ाई की और अनुत्तीर्ण होने पर उसे कैसा लगेगा, ये वास्तविक हो सकते हैं, पर दोनों में से कोई यह नहीं दिखाता कि किसी उत्तर को अधिक अंक मिलने चाहिए थे; अनुरोध ऐसे आधारों पर पुरस्कार माँगता है जिनका आँके जा रहे काम से कोई संबंध नहीं। "
  "वह अन्य विद्यार्थियों से कोई तुलना नहीं करता, जोड़ में कोई भूल का दावा नहीं करता, और स्वयं परीक्षा के बारे में कोई शिकायत नहीं उठाता।",
  "lr-sc-marks-asked-for-on-the-grounds-of-effort", pos=3)

# 3 -- the assumption a plan for more litter bins needs
T(LR, "Statement-Conclusion/Assumption", "hard",
  "A town plans to reduce litter in its main market by doubling the number of litter bins along the streets. Which one of the following is an assumption on which the plan depends?",
  "एक नगर अपने मुख्य बाज़ार में कूड़ा घटाने के लिए सड़कों के किनारे कूड़ेदानों की संख्या दोगुनी करने की योजना बनाता है। निम्नलिखित में से कौन-सी वह पूर्वधारणा है जिस पर योजना निर्भर है?",
  ["Most people in the market would never drop litter in any circumstances at all.",
   "At least some of the litter is dropped because no bin is close enough at hand.",
   "Doubling the bins will remove every piece of litter from the market for good.",
   "The town's present bins are too small to hold the litter that is put into them."],
  ["बाज़ार के अधिकांश लोग किसी भी परिस्थिति में कभी कूड़ा नहीं फेंकेंगे।",
   "कुछ कूड़ा इसलिए फेंका जाता है कि कोई कूड़ेदान पास नहीं होता।",
   "कूड़ेदान दोगुने करने से बाज़ार से कूड़े का हर टुकड़ा हमेशा के लिए हट जाएगा।",
   "नगर के वर्तमान कूड़ेदान उनमें डाले जाने वाले कूड़े के लिए बहुत छोटे हैं।"],
  1,
  "More bins can reduce litter only if some people now drop litter because a bin is not near enough; if no one's behaviour depended on how close a bin is, adding bins would change nothing. Deny this and the plan collapses -- which marks it as an assumption the plan needs. "
  "The plan does not need most people never to litter, does not promise to remove all litter, and is about the number of bins, not their size.",
  "अधिक कूड़ेदान कूड़ा तभी घटा सकते हैं जब कुछ लोग अभी इसलिए कूड़ा फेंकते हों कि कूड़ेदान पर्याप्त पास नहीं; यदि किसी का व्यवहार कूड़ेदान की निकटता पर निर्भर न हो, तो कूड़ेदान जोड़ने से कुछ नहीं बदलेगा। इसे नकारिए और योजना गिर जाती है -- जो इसे योजना की आवश्यक पूर्वधारणा बनाता है। "
  "योजना को यह आवश्यक नहीं कि अधिकांश लोग कभी कूड़ा न फेंकें, वह सारा कूड़ा हटाने का वचन नहीं देती, और वह कूड़ेदानों की संख्या के बारे में है, उनके आकार के बारे में नहीं।",
  "lr-sc-the-assumption-a-plan-for-more-litter-bins-needs", pos=1)

# 4 -- two arguments about a ban on cars
S2(LR, "Statement-Conclusion/Assumption", "hard",
   "Statement: Should private cars be banned from a city's roads on days when air pollution reaches dangerous levels?\n\nArguments:\nI. Yes. On such days a ban would sharply cut emissions at the time when people's health is most at risk.\nII. No. Many people have no other way to reach work, hospitals or schools, and a ban without enough buses would leave them stranded.\n\nWhich of the arguments is/are strong?",
   "कथन: क्या उन दिनों शहर की सड़कों पर निजी कारों पर प्रतिबंध लगाया जाना चाहिए जब वायु प्रदूषण ख़तरनाक स्तर पर पहुँच जाए?\n\nतर्क:\nI. हाँ। ऐसे दिनों में प्रतिबंध उस समय उत्सर्जन को तेज़ी से घटाएगा जब लोगों का स्वास्थ्य सबसे अधिक जोखिम में होता है।\nII. नहीं। बहुत-से लोगों के पास काम, अस्पताल या विद्यालय पहुँचने का कोई और साधन नहीं, और पर्याप्त बसों के बिना प्रतिबंध उन्हें फँसा देगा।\n\nकौन-सा/से तर्क मज़बूत है/हैं?",
   ["Argument I", "Argument II"], ["तर्क I", "तर्क II"],
   2,
   "Both are strong. I gives a direct and important reason for the ban: it would cut emissions exactly when the harm to health is greatest. II gives a direct and important reason against it: people who depend on cars for essential journeys would be left without a way to make them. "
   "Each bears squarely on the question and points to a real consequence; neither is trivial or beside the point.",
   "दोनों मज़बूत हैं। I प्रतिबंध के पक्ष में सीधा और महत्त्वपूर्ण कारण देता है: वह उत्सर्जन ठीक तब घटाएगा जब स्वास्थ्य को हानि सबसे अधिक है। II उसके विरुद्ध सीधा और महत्त्वपूर्ण कारण देता है: आवश्यक यात्राओं के लिए कारों पर निर्भर लोग उन्हें करने के साधन से वंचित हो जाएँगे। "
   "दोनों प्रश्न से सीधे जुड़े हैं और एक वास्तविक परिणाम की ओर संकेत करते हैं; कोई भी तुच्छ या असंबद्ध नहीं।",
   "lr-sc-two-arguments-about-a-ban-on-cars", roman=True)

# 5 -- five flags on a pole
def _sa5():
    cols = ["red", "blue", "green", "yellow", "white"]
    sols = []
    for p in permutations(range(1, 6)):
        w = dict(zip(cols, p))                                 # 1 = top
        if w["yellow"] == w["green"] + 1 and abs(w["blue"] - w["red"]) == 2 and w["blue"] == 5:
            sols.append(w)
    assert len(sols) == 1
    w = sols[0]
    facts = [w["white"] == w["blue"] - 1, w["red"] == 1, w["yellow"] == w["red"] + 1, w["green"] == 3]
    assert facts == [True, False, False, False]
    return "The white flag is directly above the blue one."
T(LR, "Seating Arrangement", "medium",
  "Five flags -- red, blue, green, yellow and white -- hang one above another on a pole. The green flag is directly above the yellow one. Exactly one flag hangs between the blue flag and the red one. The blue flag is at the bottom. Which one of the following is correct?",
  "पाँच झंडे -- लाल, नीला, हरा, पीला और सफ़ेद -- एक खंभे पर एक के ऊपर एक लटके हैं। हरा झंडा पीले के ठीक ऊपर है। नीले और लाल झंडे के बीच ठीक एक झंडा है। नीला झंडा सबसे नीचे है। निम्नलिखित में से कौन-सा सही है?",
  ["The white flag is directly above the blue one.", "The red flag is at the top.",
   "The yellow flag is directly below the red one.", "The green flag is in the middle."],
  ["सफ़ेद झंडा नीले के ठीक ऊपर है।", "लाल झंडा सबसे ऊपर है।",
   "पीला झंडा लाल झंडे के ठीक नीचे है।", "हरा झंडा बीच में है।"],
  0,
  "Blue is 5th from the top, so red, with one flag between, is 3rd. Green and yellow must be next to each other with green above, and the only two neighbouring places left are the 1st and 2nd: green 1st, yellow 2nd. White takes the 4th place, directly above blue. "
  "Red is 3rd, not at the top; yellow is above red, not below it; and green is at the top, not in the middle.",
  "नीला ऊपर से 5वाँ है, इसलिए लाल, बीच में एक झंडे के साथ, तीसरा है। हरा और पीला पड़ोसी होने चाहिए और हरा ऊपर, और बचे हुए एकमात्र पड़ोसी स्थान पहला और दूसरा हैं: हरा पहला, पीला दूसरा। सफ़ेद चौथा स्थान लेता है, नीले के ठीक ऊपर। "
  "लाल तीसरा है, सबसे ऊपर नहीं; पीला लाल के ऊपर है, नीचे नहीं; और हरा सबसे ऊपर है, बीच में नहीं।",
  "lr-sa-five-flags-on-a-pole", pos=3, check=_sa5)

# 6 -- the order of a bus's stops
def _sa6():
    sols = []
    for p in permutations(range(1, 7)):
        w = dict(zip("PQRSTU", p))
        if w["R"] == w["P"] + 1 and w["S"] - w["Q"] == 3 and w["S"] < w["U"] and w["U"] - w["S"] != 1:
            sols.append(w)
    assert len(sols) == 1
    w = sols[0]
    facts = [w["T"] == 5, w["P"] == 1, w["R"] == 4, w["U"] == 5]
    assert facts == [True, False, False, False]
    return "T is the fifth stop."
T(LR, "Seating Arrangement", "hard",
  "After leaving its depot, a bus stops at six places, P, Q, R, S, T and U, one after another in some order. It stops at R immediately after P. It stops at Q before S, with exactly two other stops between them. It stops at S before U, but not immediately before. Which one of the following is correct?",
  "अपने डिपो से निकलने के बाद एक बस किसी क्रम में एक के बाद एक छह स्थानों, P, Q, R, S, T और U, पर रुकती है। वह P के ठीक बाद R पर रुकती है। वह S से पहले Q पर रुकती है, और उनके बीच ठीक दो अन्य पड़ाव हैं। वह U से पहले S पर रुकती है, पर ठीक पहले नहीं। निम्नलिखित में से कौन-सा सही है?",
  ["T is the fifth stop.", "P is the first stop.", "R is the fourth stop.", "U is the fifth stop."],
  ["T पाँचवाँ पड़ाव है।", "P पहला पड़ाव है।", "R चौथा पड़ाव है।", "U पाँचवाँ पड़ाव है।"],
  0,
  "Q and S are three places apart: 1st and 4th, 2nd and 5th, or 3rd and 6th. U comes after S with at least one stop between, which is possible only if S is 4th and U 6th -- so Q is 1st. P and R must be next to each other in that order, and of the places left (2nd, 3rd and 5th) only the 2nd and 3rd are neighbours: P 2nd, R 3rd. T takes the 5th place. "
  "So T is the fifth stop. P is 2nd, not 1st; R is 3rd, not 4th; and U is 6th, not 5th.",
  "Q और S तीन स्थान दूर हैं: पहला और चौथा, दूसरा और पाँचवाँ, या तीसरा और छठा। U, S के बाद आता है और बीच में कम से कम एक पड़ाव है, जो तभी संभव है जब S चौथा और U छठा हो -- इसलिए Q पहला है। P और R उसी क्रम में पड़ोसी होने चाहिए, और बचे स्थानों (दूसरा, तीसरा और पाँचवाँ) में केवल दूसरा और तीसरा पड़ोसी हैं: P दूसरा, R तीसरा। T पाँचवाँ स्थान लेता है। "
  "अतः T पाँचवाँ पड़ाव है। P दूसरा है, पहला नहीं; R तीसरा है, चौथा नहीं; और U छठा है, पाँचवाँ नहीं।",
  "lr-sa-the-order-of-a-bus-s-stops", pos=0, check=_sa6)

# 7 -- a son's wife's mother-in-law
def _br7():
    mother = {"son": "Ravi's wife"}                  # the son's mother is Ravi's wife
    mother_in_law = lambda daughter_in_law_of: mother[daughter_in_law_of]
    assert mother_in_law("son") == "Ravi's wife"
    return "His wife"
T(LR, "Blood Relation", "medium",
  "Pointing to a woman, Ravi says, 'She is my son's wife's mother-in-law.' Ravi has only one son. How is the woman related to Ravi?",
  "एक महिला की ओर संकेत करते हुए रवि कहता है, 'यह मेरे बेटे की पत्नी की सास है।' रवि का केवल एक बेटा है। वह महिला रवि की क्या लगती है?",
  ["His mother", "His wife", "His sister", "His daughter-in-law"], ["उसकी माँ", "उसकी पत्नी", "उसकी बहन", "उसकी पुत्रवधू (बहू)"],
  1,
  "A woman's mother-in-law is her husband's mother. Ravi's son's wife's husband is Ravi's son, and the son's mother is Ravi's wife. So the woman is Ravi's wife. "
  "His mother would be the son's grandmother; his sister would be the son's aunt; and his daughter-in-law is the son's wife herself, not her mother-in-law.",
  "किसी स्त्री की सास उसके पति की माँ होती है। रवि के बेटे की पत्नी का पति रवि का बेटा है, और बेटे की माँ रवि की पत्नी है। अतः वह महिला रवि की पत्नी है। "
  "उसकी माँ बेटे की दादी होती; उसकी बहन बेटे की बुआ होती; और उसकी बहू स्वयं बेटे की पत्नी है, उसकी सास नहीं।",
  "lr-br-a-son-s-wife-s-mother-in-law", pos=1, check=_br7)

# 8 -- the first and last letters multiplied
def _cd8():
    val = lambda w: (ord(w[0]) - 64) * (ord(w[-1]) - 64)
    assert val("CAT") == 60
    return str(val("PEN"))
N(LR, "Coding-Decoding", "medium",
  "In a code, the value of a word is the product of the positions in the alphabet of its first and last letters, so that CAT is 3 × 20 = 60. What is the value of PEN?",
  "एक कूट में किसी शब्द का मान उसके पहले और अंतिम अक्षरों के वर्णमाला-स्थानों का गुणनफल है, ताकि CAT = 3 × 20 = 60 हो। PEN का मान क्या है?",
  ["30", "196", "210", "224"], 3,
  "P is the 16th letter and N the 14th, so PEN is 16 × 14 = 224. The middle letter plays no part. "
  "30 adds the two positions instead of multiplying them; 210 takes P as the 15th letter; 196 squares N's position.",
  "P, 16वाँ अक्षर है और N, 14वाँ, इसलिए PEN = 16 × 14 = 224। बीच का अक्षर कोई भूमिका नहीं निभाता। "
  "30 दोनों स्थानों को गुणा करने के बजाय जोड़ता है; 210, P को 15वाँ अक्षर मानता है; 196, N के स्थान का वर्ग करता है।",
  "lr-cd-the-first-and-last-letters-multiplied", _cd8)

# 9 -- each letter ranked within its word
def _cd9():
    def code(w):
        order = sorted(w)
        return "".join(str(order.index(ch) + 1) for ch in w)
    assert code("CAB") == "312"
    return code("LEMON")
T(LR, "Coding-Decoding", "hard",
  "In a code, each letter of a word is replaced by its place when the letters of that word are arranged in alphabetical order, so that CAB, whose letters in order are A, B, C, becomes 312. How is LEMON written in this code?",
  "एक कूट में किसी शब्द का हर अक्षर उस स्थान से बदला जाता है जो उसे उस शब्द के अक्षरों को वर्णानुक्रम में रखने पर मिलता है, ताकि CAB, जिसके अक्षर क्रम में A, B, C हैं, 312 बन जाए। इस कूट में LEMON कैसे लिखा जाता है?",
  ["12345", "21354", "21345", "31254"], ["12345", "21354", "21345", "31254"],
  1,
  "The letters of LEMON in alphabetical order are E, L, M, N, O, so E is 1st, L 2nd, M 3rd, N 4th and O 5th. Reading LEMON letter by letter: L 2, E 1, M 3, O 5, N 4 -- 21354. "
  "12345 writes the ranks in alphabetical order rather than in the order of the word; 21345 swaps O and N; 31254 has no basis.",
  "LEMON के अक्षर वर्णानुक्रम में E, L, M, N, O हैं, इसलिए E पहला, L दूसरा, M तीसरा, N चौथा और O पाँचवाँ है। LEMON को अक्षर-दर-अक्षर पढ़ने पर: L 2, E 1, M 3, O 5, N 4 -- 21354। "
  "12345 स्थानों को शब्द के क्रम के बजाय वर्णानुक्रम में लिखता है; 21345, O और N को बदल देता है; 31254 का कोई आधार नहीं।",
  "lr-cd-each-letter-ranked-within-its-word", pos=1, check=_cd9)

# 10 -- a walk that begins towards the evening sun
def _dd10():
    x = y = 0
    hx, hy = -1, 0                                 # the evening sun is in the west
    x, y = x + 10 * hx, y + 10 * hy
    hx, hy = -hy, hx                               # a left turn
    x, y = x + 5 * hx, y + 5 * hy
    hx, hy = -hy, hx
    x, y = x + 10 * hx, y + 10 * hy
    assert (x, y) == (0, -5)
    return "South"
T(LR, "Direction & Distance", "medium",
  "One evening Mohan walks 10 m straight towards the setting sun. He then turns to his left and walks 5 m, and turns to his left again and walks 10 m. In which direction is he now from where he started?",
  "एक शाम मोहन डूबते सूरज की ओर सीधे 10 मीटर चलता है। फिर वह अपनी बाईं ओर मुड़कर 5 मीटर चलता है, और फिर बाईं ओर मुड़कर 10 मीटर चलता है। अब वह अपने आरंभ स्थान से किस दिशा में है?",
  ["South", "North", "East", "West"], ["दक्षिण", "उत्तर", "पूर्व", "पश्चिम"],
  0,
  "The setting sun is in the west, so Mohan first walks 10 m west. A left turn from west faces south, so he walks 5 m south; another left turn faces east, and the 10 m east cancels the first 10 m west. He ends 5 m due south of his start. "
  "North would follow from right turns instead of left; west and east forget that the two 10 m legs cancel.",
  "डूबता सूरज पश्चिम में होता है, इसलिए मोहन पहले 10 मीटर पश्चिम चलता है। पश्चिम से बाईं ओर मुड़ने पर मुख दक्षिण होता है, इसलिए वह 5 मीटर दक्षिण चलता है; फिर बाईं ओर मुड़ने पर मुख पूर्व होता है, और 10 मीटर पूर्व पहले के 10 मीटर पश्चिम को काट देता है। वह अपने आरंभ से 5 मीटर ठीक दक्षिण में पहुँचता है। "
  "उत्तर बाएँ के बजाय दाएँ मुड़ने से आता; पश्चिम और पूर्व यह भूल जाते हैं कि 10-10 मीटर के दोनों चरण एक-दूसरे को काट देते हैं।",
  "lr-dd-a-walk-that-begins-towards-the-evening-sun", pos=0, check=_dd10)

# 11 -- poets who are not engineers
def _sy11():
    regions = [r for r in product((0, 1), repeat=4) if any(r)]    # (engineer, musician, lazy, poet)
    one = two = True
    for present in product((0, 1), repeat=len(regions)):
        f = {r for r, p in zip(regions, present) if p}
        if any(e and not m for e, m, l, p in f):            # all engineers are musicians
            continue
        if any(m and l for e, m, l, p in f):                # no musician is lazy
            continue
        if not any(l and p for e, m, l, p in f):            # some poets are lazy
            continue
        one &= any(p and not e for e, m, l, p in f)
        two &= any(e and p for e, m, l, p in f)
    return c.T2R[{(True, True): 2, (True, False): 0, (False, True): 1, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "hard",
   "Statements: All engineers are musicians. No musician is lazy. Some poets are lazy.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी इंजीनियर संगीतकार हैं। कोई भी संगीतकार आलसी नहीं है। कुछ कवि आलसी हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some poets are not engineers.", "Some engineers are poets."],
   ["कुछ कवि इंजीनियर नहीं हैं।", "कुछ इंजीनियर कवि हैं।"],
   0,
   "Only I follows. The lazy poets cannot be musicians, since no musician is lazy, and so they cannot be engineers, since every engineer is a musician: those poets are not engineers (I). "
   "II does not follow: nothing links engineers to poets at all, and the statements are equally true if no engineer writes poetry.",
   "केवल I निकलता है। आलसी कवि संगीतकार नहीं हो सकते, क्योंकि कोई संगीतकार आलसी नहीं, और इसलिए वे इंजीनियर नहीं हो सकते, क्योंकि हर इंजीनियर संगीतकार है: वे कवि इंजीनियर नहीं हैं (I)। "
   "II नहीं निकलता: इंजीनियरों को कवियों से कुछ भी नहीं जोड़ता, और यदि कोई इंजीनियर कविता न लिखे तो भी कथन उतने ही सत्य हैं।",
   "lr-sy-poets-who-are-not-engineers", roman=True, check=_sy11)

# 12 -- the cubes that touch a cube's centre
def _cp12():
    centre = (1, 1, 1)
    touching = [p for p in product(range(3), repeat=3) if sum(abs(a - b) for a, b in zip(p, centre)) == 1]
    return str(len(touching))
N(LR, "Cube Painting", "medium",
  "A large cube is built from 27 small cubes, three along each edge. How many of the small cubes share a whole face with the small cube at the very centre?",
  "एक बड़ा घन 27 छोटे घनों से बना है, हर किनारे पर तीन। कितने छोटे घन ठीक केंद्र वाले छोटे घन के साथ पूरा एक फलक साझा करते हैं?",
  ["4", "6", "8", "26"], 1,
  "The centre cube has six faces, and each of them is pressed against one other small cube -- the one at the centre of a face of the large cube. So 6 small cubes share a face with it. "
  "26 counts every other small cube, though the edge and corner cubes touch the centre only along an edge or at a point, or not at all; 8 is the number of corners; 4 has no basis.",
  "केंद्र वाले घन के छह फलक हैं, और हर एक किसी दूसरे छोटे घन से सटा है -- बड़े घन के किसी फलक के केंद्र वाले से। इसलिए 6 छोटे घन उसके साथ एक फलक साझा करते हैं। "
  "26 हर दूसरे छोटे घन को गिनता है, यद्यपि किनारे और कोने के घन केंद्र को केवल एक किनारे या बिंदु पर छूते हैं, या बिल्कुल नहीं; 8 कोनों की संख्या है; 4 का कोई आधार नहीं।",
  "lr-cp-the-cubes-that-touch-a-cube-s-centre", _cp12)

# ---- the data-sufficiency block's three Reasoning items
def _ds13():
    grid = range(-6, 7)
    s1 = {(cx, cy + 5) == (5, 5) for cx in grid for cy in grid}       # I alone: B = C + (0, 5), C anywhere
    s2 = {(bx, by) == (5, 5) for bx in grid for by in grid}           # II alone: C = A + (5, 0), B anywhere
    both = {(5 + 0, 0 + 5) == (5, 5)}                                 # both: B = A + (5, 0) + (0, 5)
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Is town B exactly north-east of town A?",
   "क्या नगर B, नगर A से ठीक उत्तर-पूर्व में है?",
   "B is 5 km due north of town C.", "B, नगर C से 5 किमी ठीक उत्तर में है।",
   "C is 5 km due east of A.", "C, A से 5 किमी ठीक पूर्व में है।",
   2,
   "Statement I alone places B relative to C, but C could be anywhere. Statement II alone places C but says nothing about B. Together, B is 5 km east and 5 km north of A -- equal distances east and north, which is exactly north-east. Both statements are needed.",
   "कथन I अकेले B को C के सापेक्ष रखता है, पर C कहीं भी हो सकता है। कथन II अकेले C को रखता है पर B के बारे में कुछ नहीं कहता। दोनों मिलकर: B, A से 5 किमी पूर्व और 5 किमी उत्तर में है -- पूर्व और उत्तर में बराबर दूरी, जो ठीक उत्तर-पूर्व है। दोनों कथन आवश्यक हैं।",
   "lr-ds-a-town-exactly-north-east", _ds13)

def _ds14():
    reverse = lambda w: w[::-1]
    only_n = lambda w: w[::-1] if w.startswith("N") else w             # another rule that fits the example
    assert reverse("NIGHT") == only_n("NIGHT") == "THGIN"
    s1 = {reverse("LIGHT")}
    s2 = {r("LIGHT") for r in (reverse, only_n)}
    both = s1
    assert s1 == {"THGIL"} and len(s2) > 1
    return _ds(s1, s2, both)
DS(LR, "hard",
   "In a certain code, how is the word LIGHT written?",
   "एक विशेष कूट में शब्द LIGHT कैसे लिखा जाता है?",
   "In the code, every word is written with its letters in reverse order.", "कूट में हर शब्द अपने अक्षरों को उलटे क्रम में रखकर लिखा जाता है।",
   "In the code, NIGHT is written as THGIN.", "कूट में NIGHT को THGIN लिखा जाता है।",
   0,
   "Statement I gives the rule, so LIGHT is written THGIL. Statement II gives only one example: reversing every word fits it, but so do other rules -- for instance, one that reverses only words beginning with N and leaves the rest alone -- so it does not fix the code for LIGHT. One statement alone is enough, but not the other.",
   "कथन I नियम देता है, इसलिए LIGHT को THGIL लिखा जाता है। कथन II केवल एक उदाहरण देता है: हर शब्द को उलटना उस पर ठीक बैठता है, पर अन्य नियम भी -- उदाहरण के लिए, ऐसा नियम जो केवल N से शुरू होने वाले शब्दों को उलटे और बाक़ी को वैसा ही छोड़ दे -- इसलिए वह LIGHT का कूट तय नहीं करता। एक कथन अकेले पर्याप्त है, पर दूसरा नहीं।",
   "lr-ds-a-code-given-by-its-rule-or-by-an-example", _ds14)

def _ds15():
    places = range(1, 5)                          # Mohan's place by age among four brothers, 1 = eldest
    s1 = {p == 1 for p in places if p < 4}        # older than at least one brother
    s2 = {p == 1 for p in places if p != 4}       # not the youngest
    both = {p == 1 for p in places if p < 4 and p != 4}
    assert both == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Is Mohan the eldest of four brothers?",
   "क्या मोहन चार भाइयों में सबसे बड़ा है?",
   "Mohan is older than at least one of his brothers.", "मोहन अपने कम से कम एक भाई से बड़ा है।",
   "Mohan is not the youngest of the four.", "मोहन चारों में सबसे छोटा नहीं है।",
   3,
   "Both statements say the same thing: Mohan is not the youngest. That leaves him eldest, second or third. Even together they cannot settle whether he is the eldest. The trap is to read 'older than at least one' as 'older than all'.",
   "दोनों कथन एक ही बात कहते हैं: मोहन सबसे छोटा नहीं है। इससे वह सबसे बड़ा, दूसरा या तीसरा रह जाता है। दोनों मिलकर भी तय नहीं कर सकते कि वह सबसे बड़ा है या नहीं। जाल 'कम से कम एक से बड़ा' को 'सबसे बड़ा' पढ़ लेना है।",
   "lr-ds-a-brother-who-may-or-may-not-be-the-eldest", _ds15)
