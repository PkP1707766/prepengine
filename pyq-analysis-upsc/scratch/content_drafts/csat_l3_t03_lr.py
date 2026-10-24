# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 3 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Level 3's harder mix (1 easy / 9 medium / 8 hard), with none of the shapes of Level 2 Tests 1-7, Level 1 Minis 1-3 or
Level 3 Tests 1-2: a government likened to a household, a dam or no water, the assumptions behind helmets for pillion
riders; four people who speak two languages each, six exams on three days, three races and their points; the
descendants of one couple, the father of an only sister's husband; three sides of a hexagonal park, two people back to
back; a code that writes letters in binary, a cipher keyed to the word PLANET; a die tipped three times; 'only
graduates can apply'; three boxes whose labels all lie; and in the data-sufficiency block a pass that does not follow,
the row of seat 47, and a holiday found two ways. Arrangement, code, cube, syllogism and truth-teller keys are found by
checking every case."""
from itertools import combinations, permutations, product
import math
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a government likened to a household
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'A household that keeps borrowing soon finds itself in trouble. A government is simply a very large household. Therefore a government should never borrow.' Which one of the following best describes the main weakness of this argument?",
  "'जो परिवार लगातार उधार लेता है, वह जल्दी ही संकट में पड़ जाता है। सरकार बस एक बहुत बड़ा परिवार है। इसलिए सरकार को कभी उधार नहीं लेना चाहिए।' निम्नलिखित में से कौन-सा इस तर्क की मुख्य कमज़ोरी का सबसे अच्छा वर्णन करता है?",
  ["It argues in a circle, quietly taking for granted in its premises the very conclusion that it states.",
   "It mistakes a mere correlation between borrowing and trouble for proof that one causes the other.",
   "It relies on the authority of experts in place of giving any reasons of its own.",
   "It rests on a likeness between a household and a government that fails where borrowing is concerned."],
  ["यह चक्राकार तर्क करता है, अपने आधार-वाक्यों में ठीक वही निष्कर्ष मान लेता है जो वह बताता है।",
   "यह उधार और संकट के बीच केवल सहसंबंध को इस बात का प्रमाण मान लेता है कि एक दूसरे का कारण है।",
   "यह अपने कोई कारण देने के बजाय विशेषज्ञों के अधिकार पर टिका है।",
   "यह परिवार और सरकार के बीच ऐसी समानता पर टिका है जो उधार के मामले में विफल हो जाती है।"],
  3,
  "The whole argument hangs on the claim that a government is like a household. In the respects that matter for borrowing it is not: a government can borrow for decades and spread the cost over generations, it can raise taxes, it usually borrows in its own currency, and its spending can raise the very incomes it taxes. "
  "So what is true of a household's borrowing need not be true of a government's. The argument does not assume its conclusion in its premises, it makes no claim about cause drawn from a correlation, and it cites no experts at all.",
  "पूरा तर्क इस दावे पर टिका है कि सरकार एक परिवार जैसी है। उधार के लिए मायने रखने वाले पहलुओं में ऐसा नहीं है: सरकार दशकों के लिए उधार ले सकती है और लागत को पीढ़ियों में फैला सकती है, कर बढ़ा सकती है, प्रायः अपनी ही मुद्रा में उधार लेती है, और उसका ख़र्च उन्हीं आयों को बढ़ा सकता है जिन पर वह कर लगाती है। "
  "इसलिए जो परिवार के उधार के बारे में सत्य है, वह सरकार के उधार के बारे में सत्य होना आवश्यक नहीं। तर्क अपने आधार-वाक्यों में निष्कर्ष नहीं मान लेता, सहसंबंध से कारण का कोई दावा नहीं करता, और किसी विशेषज्ञ का उल्लेख ही नहीं करता।",
  "lr-sc-a-government-likened-to-a-household", pos=3)

# 2 -- the assumptions behind helmets for pillion riders
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: To reduce deaths in road accidents, the government has made it compulsory for pillion riders on two-wheelers to wear helmets.\n\nWhich of the following assumptions is/are implicit in the statement?",
   "कथन: सड़क दुर्घटनाओं में मौतें घटाने के लिए सरकार ने दोपहिया वाहनों पर पीछे बैठने वालों के लिए हेलमेट पहनना अनिवार्य कर दिया है।\n\nनिम्नलिखित में से कौन-सी पूर्वधारणा/एँ कथन में अंतर्निहित है/हैं?",
   ["Many pillion riders do not wear helmets at present.",
    "Wearing a helmet reduces the risk of a fatal head injury in an accident."],
   ["अभी पीछे बैठने वाले कई लोग हेलमेट नहीं पहनते।",
    "हेलमेट पहनने से दुर्घटना में सिर की घातक चोट का जोखिम घटता है।"],
   2,
   "Both are implicit. A rule making helmets compulsory is worth making only if many pillion riders do not already wear them (I), and it can reduce deaths only if helmets actually lower the risk of fatal head injuries (II). "
   "Take away either assumption and the decision no longer serves its stated purpose.",
   "दोनों अंतर्निहित हैं। हेलमेट अनिवार्य करने का नियम तभी बनाने योग्य है जब पीछे बैठने वाले कई लोग पहले से हेलमेट न पहनते हों (I), और वह मौतें तभी घटा सकता है जब हेलमेट वास्तव में सिर की घातक चोटों का जोखिम घटाएँ (II)। "
   "इनमें से कोई भी पूर्वधारणा हटा दीजिए, तो निर्णय अपना बताया गया उद्देश्य पूरा नहीं करता।",
   "lr-sc-assumptions-behind-helmets-for-pillion-riders", roman=True)

# 3 -- a dam or no water
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'Either the city builds the new dam, or it will run out of drinking water within ten years.' Which one of the following best describes the flaw in this claim?",
  "'या तो शहर नया बाँध बनाए, या दस वर्षों के भीतर उसका पीने का पानी समाप्त हो जाएगा।' निम्नलिखित में से कौन-सा इस दावे की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It attacks the people who oppose the dam instead of answering their reasons.",
   "It ignores other ways of meeting the need, such as cutting leaks or reusing water.",
   "It predicts the city's future water needs from what happened in one unusually dry year in the past.",
   "It assumes that the dam, once begun, will be completed well within the ten years."],
  ["यह बाँध का विरोध करने वालों के कारणों का उत्तर देने के बजाय उन पर हमला करता है।",
   "यह आवश्यकता पूरी करने के दूसरे उपायों, जैसे रिसाव घटाने या पानी के पुनः उपयोग, की अनदेखी करता है।",
   "यह शहर की भविष्य की पानी की आवश्यकता का अनुमान अतीत के किसी एक असामान्य रूप से सूखे वर्ष की घटनाओं से लगाता है।",
   "यह मान लेता है कि एक बार शुरू हुआ बाँध दस वर्षों के भीतर पूरा हो जाएगा।"],
  1,
  "The claim offers only two possibilities -- the dam or a dry city -- as if nothing else could supply or save water. Other courses exist: reducing losses from leaking pipes, recycling waste water, harvesting rain, recharging groundwater or bringing water from elsewhere. Presenting two options as the only ones is a false choice. "
  "The claim attacks no one, cites no single dry year, and says nothing about how long the dam would take to build.",
  "दावा केवल दो संभावनाएँ देता है -- बाँध या सूखा शहर -- मानो पानी देने या बचाने का कोई और उपाय न हो। अन्य रास्ते हैं: रिसते पाइपों से हानि घटाना, अपशिष्ट जल का पुनर्चक्रण, वर्षा-जल संचयन, भूजल पुनर्भरण या कहीं और से पानी लाना। दो विकल्पों को एकमात्र विकल्प बताना एक झूठा चुनाव है। "
  "दावा किसी पर हमला नहीं करता, किसी एक सूखे वर्ष का उल्लेख नहीं करता, और यह कुछ नहीं कहता कि बाँध बनने में कितना समय लगेगा।",
  "lr-sc-a-dam-or-no-water", pos=1)

# 4 -- four people who speak two languages each
def _sa1():
    langs = "HTBM"
    sols = []
    for choice in product(list(combinations(langs, 2)), repeat=4):
        sp = dict(zip("ABCD", map(set, choice)))
        if any(sum(l in sp[p] for p in "ABCD") != 2 for l in langs): continue
        if not ("H" in sp["A"] and "M" not in sp["A"]): continue
        if sp["A"] & sp["B"]: continue
        if not ("T" in sp["C"] and "B" not in sp["C"]): continue
        if not (sp["D"] & sp["A"]) or "H" in sp["D"]: continue
        sols.append(sp)
    assert len(sols) == 1, sols
    who = [p for p in "ABCD" if {"T", "M"} <= sols[0][p]]
    return who[0] if who else "No one"
N(LR, "Seating Arrangement", "hard",
  "Each of four people, A, B, C and D, speaks exactly two of four languages -- Hindi, Tamil, Bengali and Marathi -- and each language is spoken by exactly two of them. A speaks Hindi but not Marathi. A and B have no language in common. C speaks Tamil but not Bengali. "
  "D shares a language with A but does not speak Hindi. Who speaks both Tamil and Marathi?",
  "चार व्यक्तियों, A, B, C और D, में से हर एक चार भाषाओं -- हिंदी, तमिल, बांग्ला और मराठी -- में से ठीक दो बोलता है, और हर भाषा उनमें से ठीक दो बोलते हैं। A हिंदी बोलता है पर मराठी नहीं। A और B की कोई भाषा साझी नहीं है। C तमिल बोलता है पर बांग्ला नहीं। "
  "D की A से एक भाषा साझी है पर D हिंदी नहीं बोलता। तमिल और मराठी दोनों कौन बोलता है?",
  ["B", "C", "D", "No one"], 0,
  "A speaks Hindi and one of Tamil or Bengali. D shares a language with A but not Hindi, so D shares A's second language. If A's second language were Tamil, D would speak Tamil too, making C (who speaks Tamil) a third Tamil speaker -- impossible. So A speaks Hindi and Bengali, and D speaks Bengali. "
  "B shares nothing with A, so B speaks the other two, Tamil and Marathi. C speaks Tamil and, not Bengali, must take Hindi (Hindi needs a second speaker, and D does not speak it); D's second language is then Marathi. So A: Hindi, Bengali; B: Tamil, Marathi; C: Hindi, Tamil; D: Bengali, Marathi -- B speaks both Tamil and Marathi.",
  "A हिंदी और तमिल या बांग्ला में से एक बोलता है। D की A से एक भाषा साझी है पर वह हिंदी नहीं, इसलिए D, A की दूसरी भाषा बोलता है। यदि A की दूसरी भाषा तमिल होती, तो D भी तमिल बोलता, जिससे C (जो तमिल बोलता है) तमिल का तीसरा वक्ता बन जाता -- असंभव। अतः A हिंदी और बांग्ला बोलता है, और D बांग्ला। "
  "B की A से कोई भाषा साझी नहीं, इसलिए B बाक़ी दो, तमिल और मराठी, बोलता है। C तमिल बोलता है और बांग्ला नहीं, इसलिए उसे हिंदी लेनी होगी (हिंदी के लिए दूसरा वक्ता चाहिए, और D उसे नहीं बोलता); तब D की दूसरी भाषा मराठी है। अतः A: हिंदी, बांग्ला; B: तमिल, मराठी; C: हिंदी, तमिल; D: बांग्ला, मराठी -- B तमिल और मराठी दोनों बोलता है।",
  "lr-sa-four-people-who-speak-two-languages-each", _sa1, opts_hi=["B", "C", "D", "कोई नहीं"])

# 5 -- six exams on three days
def _sa2():
    slots = [(d, h) for d in "MTW" for h in "ma"]
    out, n = set(), 0
    for p in permutations(slots):
        a = dict(zip("PQRSTU", p))
        if a["P"][0] == "M" and a["Q"][1] == "a" and a["R"][0] == a["S"][0] and a["T"] == ("W", "m") and a["U"][0] != "M":
            n += 1
            out.add(next(k for k, v in a.items() if v == ("W", "a")))
    assert n == 2 and len(out) == 1
    return out.pop()
N(LR, "Seating Arrangement", "medium",
  "Six exams, P, Q, R, S, T and U, are held over three days, Monday, Tuesday and Wednesday, with one exam each morning and one each afternoon. P is on Monday. Q is held in an afternoon. R and S are on the same day. T is on Wednesday morning, and U is not on Monday. Which exam is held on Wednesday afternoon?",
  "छह परीक्षाएँ, P, Q, R, S, T और U, तीन दिनों -- सोमवार, मंगलवार और बुधवार -- में होती हैं, हर सुबह एक और हर दोपहर एक। P सोमवार को है। Q दोपहर में होती है। R और S एक ही दिन हैं। T बुधवार सुबह है, और U सोमवार को नहीं है। बुधवार दोपहर कौन-सी परीक्षा होती है?",
  ["Q", "R", "S", "U"], 3,
  "R and S need a whole day together. Monday has P, and Wednesday has T in the morning, so the only free whole day is Tuesday: R and S take Tuesday's two slots, in some order. That leaves Monday's other slot and Wednesday afternoon for Q and U. U is not on Monday, so U takes Wednesday afternoon, and Q, which is in an afternoon, takes Monday afternoon (with P on Monday morning). "
  "The order of R and S on Tuesday is not fixed, but Wednesday afternoon is U's either way.",
  "R और S को एक पूरा दिन साथ चाहिए। सोमवार को P है, और बुधवार सुबह T है, इसलिए एकमात्र ख़ाली पूरा दिन मंगलवार है: R और S मंगलवार के दोनों समय किसी क्रम में लेते हैं। इससे सोमवार का दूसरा समय और बुधवार दोपहर Q और U के लिए बचते हैं। U सोमवार को नहीं है, इसलिए U बुधवार दोपहर लेती है, और Q, जो दोपहर में है, सोमवार दोपहर लेती है (P सोमवार सुबह)। "
  "मंगलवार को R और S का क्रम तय नहीं है, पर बुधवार दोपहर दोनों ही स्थितियों में U की है।",
  "lr-sa-six-exams-on-three-days", _sa2)

# 6 -- three races and their points
def _sa3():
    sols = []
    for rr in product(permutations("ABC"), repeat=3):
        pts = {x: 0 for x in "ABC"}
        for r in rr:
            for k, x in enumerate(r):
                pts[x] += 3 - k
        if (pts["A"], pts["B"], pts["C"]) == (7, 6, 5) and rr[0][0] == "A" and all(r[2] != "B" for r in rr):
            sols.append(rr)
    claims = {"C won exactly one race.": all(sum(r[0] == "C" for r in s) == 1 for s in sols),
              "C won the third race.": all(s[2][0] == "C" for s in sols),
              "A won the second race.": all(s[1][0] == "A" for s in sols),
              "B won one of the races.": all(any(r[0] == "B" for r in s) for s in sols)}
    must = [k for k, v in claims.items() if v]
    assert len(sols) == 2 and must == ["C won exactly one race."]
    return must[0]
T(LR, "Seating Arrangement", "hard",
  "Three runners, A, B and C, ran three races. In each race the winner got 3 points, the runner-up 2 and the last 1. A won the first race, and B never came last. At the end A had 7 points, B 6 and C 5. Which one of the following must be true?",
  "तीन धावकों, A, B और C, ने तीन दौड़ें लगाईं। हर दौड़ में विजेता को 3 अंक, दूसरे को 2 और अंतिम को 1 मिला। A ने पहली दौड़ जीती, और B कभी अंतिम नहीं आया। अंत में A के 7 अंक थे, B के 6 और C के 5। निम्नलिखित में से कौन-सा अनिवार्यतः सत्य है?",
  ["C won exactly one race.", "C won the third race.", "A won the second race.", "B won one of the races."],
  ["C ने ठीक एक दौड़ जीती।", "C ने तीसरी दौड़ जीती।", "A ने दूसरी दौड़ जीती।", "B ने कोई एक दौड़ जीती।"], 0,
  "B never came last, so B was first or second each time; 6 points in three races with no 1s means 2 + 2 + 2 -- B was second every time, and never won. So every race was won by A or C. A has 7 points: having won the first race (3), A needs 4 from the other two, which -- since A is never second -- means one more win (3) and one last place (1). "
  "C, with 5 points, must then have won the other race and come last twice. The races can be ordered either way after the first, so 'C won the third race' and 'A won the second race' each hold in only one of the two outcomes; B won none. C won exactly one race in both.",
  "B कभी अंतिम नहीं आया, इसलिए हर बार वह पहला या दूसरा रहा; तीन दौड़ों में बिना किसी 1 के 6 अंक का अर्थ है 2 + 2 + 2 -- B हर बार दूसरा रहा, और कभी नहीं जीता। अतः हर दौड़ A या C ने जीती। A के 7 अंक हैं: पहली दौड़ जीतकर (3), A को बाक़ी दो से 4 चाहिए, जो -- चूँकि A कभी दूसरा नहीं होता -- एक और जीत (3) और एक अंतिम स्थान (1) है। "
  "तब 5 अंकों वाले C ने दूसरी दौड़ जीती होगी और दो बार अंतिम आया होगा। पहली के बाद की दौड़ें किसी भी क्रम में हो सकती हैं, इसलिए 'C ने तीसरी दौड़ जीती' और 'A ने दूसरी दौड़ जीती' प्रत्येक दोनों में से केवल एक परिणाम में सही है; B ने कोई नहीं जीती। C ने दोनों में ठीक एक दौड़ जीती।",
  "lr-sa-three-races-and-their-points", pos=0, check=_sa3)

# 7 -- the descendants of one couple
N(LR, "Blood Relation", "medium",
  "A couple has 4 children. Each of the children has 2 children, and each of those grandchildren has 1 child. How many descendants does the couple have in all?",
  "एक दंपती की 4 संतानें हैं। हर संतान की 2 संतानें हैं, और उन पोते-पोतियों/नाती-नातिनों में से हर एक की 1 संतान है। दंपती के कुल कितने वंशज हैं?",
  ["16", "20", "24", "28"], 1,
  "There are 4 children, 4 × 2 = 8 grandchildren and 8 × 1 = 8 great-grandchildren: 4 + 8 + 8 = 20 descendants. "
  "16 leaves out the 4 children; 24 and 28 count some generation twice.",
  "4 संतानें, 4 × 2 = 8 पोते-पोतियाँ/नाती-नातिनें और 8 × 1 = 8 परपोते-परपोतियाँ: 4 + 8 + 8 = 20 वंशज। "
  "16, 4 संतानों को छोड़ देता है; 24 और 28 किसी पीढ़ी को दो बार गिनते हैं।",
  "lr-br-the-descendants-of-one-couple", lambda: str(4 + 4 * 2 + 4 * 2 * 1))

# 8 -- the father of an only sister's husband
T(LR, "Blood Relation", "hard",
  "Raj's only sister is married to Sohan. How is Sohan's father related to the only daughter of Raj's father?",
  "राज की इकलौती बहन का विवाह सोहन से हुआ है। सोहन के पिता, राज के पिता की इकलौती बेटी के क्या लगते हैं?",
  ["Father-in-law", "Father", "Uncle", "Brother-in-law"], ["ससुर", "पिता", "चाचा", "जेठ"], 0,
  "Raj's father has only one daughter, so Raj cannot be a daughter as well: Raj is a son, and his father's only daughter is Raj's only sister. She is married to Sohan, so Sohan's father is her father-in-law. "
  "'Father' would be right only for Sohan himself; 'uncle' and 'brother-in-law' put Sohan's father in the wrong relation to her.",
  "राज के पिता की केवल एक बेटी है, इसलिए राज भी बेटी नहीं हो सकता: राज बेटा है, और उसके पिता की इकलौती बेटी राज की इकलौती बहन है। उसका विवाह सोहन से हुआ है, इसलिए सोहन के पिता उसके ससुर हैं। "
  "'पिता' केवल स्वयं सोहन के लिए सही होता; 'चाचा' और 'जेठ' सोहन के पिता को उससे ग़लत संबंध में रखते हैं।",
  "lr-br-the-father-of-an-only-sister-s-husband", pos=0)

# 9 -- three sides of a hexagonal park
def _dd1():
    pts, x, y, ang = [], 0.0, 0.0, 0.0
    for _ in range(3):
        x, y = x + 10 * math.cos(math.radians(ang)), y + 10 * math.sin(math.radians(ang))
        ang += 60
    d = math.hypot(x, y)
    assert abs(d - 20) < 1e-9
    return "20 m"
N(LR, "Direction & Distance", "hard",
  "A park has the shape of a regular hexagon with sides of 10 m. A person starts at one corner and walks along three consecutive sides. How far is the person then from the starting corner, measured in a straight line?",
  "एक उद्यान 10 मीटर भुजा वाले सम षट्भुज के आकार का है। एक व्यक्ति एक कोने से चलकर लगातार तीन भुजाओं के साथ-साथ चलता है। तब वह आरंभ वाले कोने से सीधी रेखा में कितनी दूर है?",
  ["10 m", "10√3 m", "20 m", "30 m"], 2,
  "After three of the six sides the person is at the corner opposite the start. A regular hexagon is made of six equilateral triangles meeting at its centre, so opposite corners are two side-lengths apart through the centre: 2 × 10 = 20 m. "
  "30 m is the distance walked along the sides; 10√3 m is the distance after two sides (to the next-but-one corner); 10 m is the distance after one side.",
  "छह में से तीन भुजाओं के बाद व्यक्ति आरंभ के ठीक विपरीत कोने पर है। सम षट्भुज केंद्र पर मिलने वाले छह समबाहु त्रिभुजों से बना होता है, इसलिए विपरीत कोने केंद्र से होकर दो भुजाओं जितनी दूरी पर हैं: 2 × 10 = 20 मीटर। "
  "30 मीटर भुजाओं के साथ चली गई दूरी है; 10√3 मीटर दो भुजाओं के बाद (एक छोड़कर अगले कोने तक) की दूरी है; 10 मीटर एक भुजा के बाद की दूरी है।",
  "lr-dd-three-sides-of-a-hexagonal-park", _dd1,
  opts_hi=["10 मीटर", "10√3 मीटर", "20 मीटर", "30 मीटर"])

# 10 -- two people back to back
def _dd2():
    q = (-1, 0)                                # P faces east (1, 0); Q, back to back, faces west
    q = (-q[1], q[0])                          # a left turn: (x, y) -> (-y, x)
    return {(0, 1): "North", (1, 0): "East", (-1, 0): "West", (0, -1): "South"}[q]
N(LR, "Direction & Distance", "easy",
  "P and Q stand back to back. P faces east. Q then turns to the left. In which direction does Q face now?",
  "P और Q पीठ से पीठ सटाकर खड़े हैं। P का मुँह पूर्व की ओर है। फिर Q बाईं ओर मुड़ता है। अब Q का मुँह किस दिशा में है?",
  ["North", "East", "West", "South"], 3,
  "Back to back with P, who faces east, Q faces west. A left turn from west brings Q to face south. North is where a right turn from west would lead, or a left turn from east -- the slip of turning from P's direction instead of Q's; west is Q's direction before the turn.",
  "पूर्व की ओर मुँह किए P से पीठ सटाकर खड़े Q का मुँह पश्चिम की ओर है। पश्चिम से बाईं ओर मुड़ने पर Q का मुँह दक्षिण की ओर हो जाता है। उत्तर वह दिशा है जहाँ पश्चिम से दाईं ओर, या पूर्व से बाईं ओर मुड़ने पर पहुँचते -- Q के बजाय P की दिशा से मुड़ने की चूक; पश्चिम मुड़ने से पहले Q की दिशा है।",
  "lr-dd-two-people-back-to-back", _dd2, opts_hi=["उत्तर", "पूर्व", "पश्चिम", "दक्षिण"])

# 11 -- a code that writes letters in binary
def _cd1():
    code = lambda ch: bin(ord(ch) - 64)[2:]
    assert [code(x) for x in "ABCDE"] == ["1", "10", "11", "100", "101"]
    return code("G")
N(LR, "Coding-Decoding", "medium",
  "In a certain code, A is written as 1, B as 10, C as 11, D as 100 and E as 101. How is G written in that code?",
  "एक निश्चित कूट में A को 1, B को 10, C को 11, D को 100 और E को 101 लिखा जाता है। उस कूट में G को कैसे लिखा जाएगा?",
  ["111", "110", "1000", "1110"], 0,
  "Each letter is written as its place in the alphabet in the binary system, which uses only 0 and 1: 1 = 1, 2 = 10, 3 = 11, 4 = 100, 5 = 101. G is the 7th letter, and 7 = 4 + 2 + 1 = 111 in binary. "
  "110 is 6, the code for F; 1000 is 8, the code for H; 1110 is 14, the code for N.",
  "हर अक्षर को उसके वर्णमाला-स्थान के रूप में द्वि-आधारी (बाइनरी) पद्धति में लिखा जाता है, जो केवल 0 और 1 का प्रयोग करती है: 1 = 1, 2 = 10, 3 = 11, 4 = 100, 5 = 101। G सातवाँ अक्षर है, और बाइनरी में 7 = 4 + 2 + 1 = 111। "
  "110, 6 है, F का कूट; 1000, 8 है, H का कूट; 1110, 14 है, N का कूट।",
  "lr-cd-a-code-that-writes-letters-in-binary", _cd1)

# 12 -- a cipher keyed to the word PLANET
def _cd2():
    key = "PLANET"
    rest = [ch for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if ch not in key]
    cipher = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", list(key) + rest))
    assert "".join(cipher[x] for x in "ABCDEFGH") == "PLANETBC"
    return "".join(cipher[x] for x in "HIDE")
T(LR, "Coding-Decoding", "hard",
  "In a code, the letters A to Z are replaced in order by the letters of the word PLANET followed by the rest of the alphabet in its usual order, leaving out the letters already used: so A is written as P, B as L, C as A, D as N, E as E, F as T, G as B, H as C, and so on. How is the word HIDE written in this code?",
  "एक कूट में A से Z तक के अक्षर क्रम से शब्द PLANET के अक्षरों से और उसके बाद वर्णमाला के शेष अक्षरों से उनके सामान्य क्रम में बदले जाते हैं, पहले प्रयुक्त अक्षर छोड़ते हुए: इस प्रकार A को P, B को L, C को A, D को N, E को E, F को T, G को B, H को C लिखा जाता है, इत्यादि। इस कूट में शब्द HIDE को कैसे लिखा जाएगा?",
  ["CDNE", "CDAE", "DCNE", "CINE"], ["CDNE", "CDAE", "DCNE", "CINE"], 0,
  "After P, L, A, N, E, T, the code alphabet continues with the unused letters in order: B, C, D, F, G, H, .... So G becomes B, H becomes C, I becomes D, J becomes F, and so on. H is C, I is D, D is N (from PLANET) and E is E: HIDE is written CDNE. "
  "CDAE takes D as A, the code for C; DCNE swaps the codes of H and I; CINE leaves I unchanged.",
  "P, L, A, N, E, T के बाद कूट-वर्णमाला अप्रयुक्त अक्षरों से क्रम में आगे बढ़ती है: B, C, D, F, G, H, ....। अतः G, B बनता है, H, C बनता है, I, D बनता है, J, F बनता है, इत्यादि। H = C, I = D, D = N (PLANET से) और E = E: HIDE को CDNE लिखा जाता है। "
  "CDAE, D को A मानता है, जो C का कूट है; DCNE, H और I के कूट उलट देता है; CINE, I को अपरिवर्तित छोड़ देता है।",
  "lr-cd-a-cipher-keyed-to-planet", pos=2, check=_cd2)

# 13 -- a die tipped three times
def _cp1():
    top, north, south, bottom = 1, 2, 5, 6
    for _ in range(3):                         # tipping over the northern edge: the south face comes up
        top, north, bottom, south = south, top, north, bottom
    return str(top)
N(LR, "Cube Painting", "hard",
  "A standard die, on which opposite faces add up to 7, rests on a table with 1 on top and 2 facing north. It is tipped over its northern edge so that it rolls one place to the north, and this is done three times in all. Which number is then on top?",
  "एक सामान्य पासा, जिस पर आमने-सामने के फलकों का योग 7 है, मेज़ पर ऐसे रखा है कि ऊपर 1 है और उत्तर की ओर 2। उसे उसके उत्तरी किनारे पर पलटा जाता है ताकि वह उत्तर की ओर एक स्थान लुढ़क जाए, और ऐसा कुल तीन बार किया जाता है। तब ऊपर कौन-सी संख्या है?",
  ["1", "2", "5", "6"], 1,
  "At the start the top is 1, the bottom 6, the north face 2 and the south face 5. Each tip to the north brings the south face to the top, sends the top to the north, the north face to the bottom and the bottom to the south. "
  "After one tip the top is 5; after two it is 6; after three it is 2 (the face that began facing north has gone down and round to the top). 6 is the top after two tips and 5 after one; 1 would need four tips.",
  "आरंभ में ऊपर 1, नीचे 6, उत्तर की ओर 2 और दक्षिण की ओर 5 है। उत्तर की ओर हर बार पलटने से दक्षिणी फलक ऊपर आ जाता है, ऊपर वाला उत्तर की ओर, उत्तरी फलक नीचे और नीचे वाला दक्षिण की ओर चला जाता है। "
  "एक बार पलटने के बाद ऊपर 5 है; दो बार के बाद 6; तीन बार के बाद 2 (जो फलक आरंभ में उत्तर की ओर था वह नीचे जाकर घूमते हुए ऊपर आ गया)। 6 दो बार पलटने के बाद और 5 एक बार के बाद ऊपर होता है; 1 के लिए चार बार पलटना पड़ता।",
  "lr-cp-a-die-tipped-three-times", _cp1)

# 14 -- 'only graduates can apply'
def _sy1():
    regions = list(product((0, 1), repeat=3))          # (applicant, graduate, engineer)
    one = two = True
    for mask in range(1, 1 << 8):
        world = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(a and not g for a, g, e in world): continue      # only graduates can apply
        if not any(a and e for a, g, e in world): continue      # some applicants are engineers
        one = one and not any(a and not g for a, g, e in world)
        two = two and any(e and g for a, g, e in world)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "medium",
   "Statements: Only graduates can apply for the post. Some of the applicants are engineers.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: केवल स्नातक ही उस पद के लिए आवेदन कर सकते हैं। आवेदकों में से कुछ इंजीनियर हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["All the applicants are graduates.", "Some engineers are graduates."],
   ["सभी आवेदक स्नातक हैं।", "कुछ इंजीनियर स्नातक हैं।"],
   2,
   "Both follow. 'Only graduates can apply' means that nobody who is not a graduate is an applicant -- that is, every applicant is a graduate (I). Some applicants are engineers, and being applicants they are graduates, so some engineers are graduates (II). "
   "The trap is to read 'only graduates can apply' as 'all graduates are applicants', which it does not say.",
   "दोनों निकलते हैं। 'केवल स्नातक ही आवेदन कर सकते हैं' का अर्थ है कि जो स्नातक नहीं है वह आवेदक नहीं है -- यानी हर आवेदक स्नातक है (I)। कुछ आवेदक इंजीनियर हैं, और आवेदक होने के कारण वे स्नातक हैं, इसलिए कुछ इंजीनियर स्नातक हैं (II)। "
   "जाल यह है कि 'केवल स्नातक ही आवेदन कर सकते हैं' को 'सभी स्नातक आवेदक हैं' पढ़ लिया जाए, जो यह नहीं कहता।",
   "lr-sy-only-graduates-can-apply", roman=True, check=_sy1)

# 15 -- three boxes whose labels all lie
def _tl1():
    labels = ["GG", "SS", "GS"]
    answers = set()
    for contents in permutations(["GG", "SS", "GS"]):
        box = dict(zip(labels, contents))                     # label -> actual contents
        if any(lab == box[lab] for lab in labels): continue  # every label is wrong
        if "G" not in box["GS"]: continue                     # a gold coin came from the box labelled 'one of each'
        answers.add(box["SS"])
    assert answers == {"GS"}
    return "One gold coin and one silver coin"
T(LR, "Truth-Liar", "hard",
  "Three boxes are labelled 'Two gold coins', 'Two silver coins' and 'One gold, one silver'. One box holds two gold coins, one holds two silver coins and one holds one of each, but every label is wrong. A coin taken without looking from the box labelled 'One gold, one silver' turns out to be gold. What does the box labelled 'Two silver coins' contain?",
  "तीन बक्सों पर 'दो सोने के सिक्के', 'दो चाँदी के सिक्के' और 'एक सोने का, एक चाँदी का' लिखा है। एक बक्से में दो सोने के सिक्के हैं, एक में दो चाँदी के, और एक में दोनों में से एक-एक, पर हर लेबल ग़लत है। 'एक सोने का, एक चाँदी का' लिखे बक्से से बिना देखे निकाला गया सिक्का सोने का निकलता है। 'दो चाँदी के सिक्के' लिखे बक्से में क्या है?",
  ["Two gold coins", "Two silver coins", "One gold coin and one silver coin", "It cannot be determined from one coin drawn"],
  ["दो सोने के सिक्के", "दो चाँदी के सिक्के", "एक सोने का और एक चाँदी का सिक्का", "एक सिक्का निकालने से यह तय नहीं किया जा सकता"], 2,
  "The box labelled 'One gold, one silver' cannot hold one of each, since its label is wrong; it gave a gold coin, so it holds two gold coins. The box labelled 'Two silver coins' cannot hold two silver (wrong label) or two gold (already placed), so it holds one of each -- and the box labelled 'Two gold coins' holds two silver. "
  "A single draw settles everything because the labels are all known to be false. Two gold coins are in the box the coin came from, and two silver coins cannot be in the box that is labelled so.",
  "'एक सोने का, एक चाँदी का' लिखे बक्से में एक-एक नहीं हो सकते, क्योंकि उसका लेबल ग़लत है; उसमें से सोने का सिक्का निकला, इसलिए उसमें दो सोने के सिक्के हैं। 'दो चाँदी के सिक्के' लिखे बक्से में न दो चाँदी के (लेबल ग़लत) हो सकते हैं न दो सोने के (वे पहले ही रखे जा चुके), इसलिए उसमें एक-एक है -- और 'दो सोने के सिक्के' लिखे बक्से में दो चाँदी के। "
  "एक ही निकासी सब कुछ तय कर देती है क्योंकि सभी लेबल झूठे ज्ञात हैं। दो सोने के सिक्के उस बक्से में हैं जिससे सिक्का निकला, और दो चाँदी के सिक्के उस बक्से में नहीं हो सकते जिस पर यही लिखा है।",
  "lr-tl-three-boxes-whose-labels-all-lie", pos=3, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    worlds = [(studied, passed) for studied in (True, False) for passed in (True, False)]
    s1 = {p for s, p in worlds if (not s or p)}                       # I: studying implies passing; Sohan's study unknown
    s2 = {p for s, p in worlds if not s}                              # II: he did not study; the rule unknown
    both = {p for s, p in worlds if (not s or p) and not s}
    assert both == {True, False}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Did Sohan pass the examination?",
   "क्या सोहन परीक्षा में उत्तीर्ण हुआ?",
   "Everyone who studied regularly passed the examination.", "जिसने भी नियमित पढ़ाई की, वह परीक्षा में उत्तीर्ण हुआ।",
   "Sohan did not study regularly.", "सोहन ने नियमित पढ़ाई नहीं की।",
   3,
   "Statement I says that studying regularly was enough to pass, not that it was needed: people who did not study regularly may also have passed. With Statement II, Sohan is one of those who did not study regularly, and Statement I says nothing about them. "
   "So even together the statements do not tell us whether he passed. (Concluding that he failed would be denying the antecedent.)",
   "कथन I कहता है कि नियमित पढ़ाई उत्तीर्ण होने के लिए पर्याप्त थी, यह नहीं कि वह आवश्यक थी: जिन्होंने नियमित पढ़ाई नहीं की, वे भी उत्तीर्ण हुए हो सकते हैं। कथन II के साथ सोहन उनमें से है जिन्होंने नियमित पढ़ाई नहीं की, और कथन I उनके बारे में कुछ नहीं कहता। "
   "अतः दोनों साथ भी नहीं बताते कि वह उत्तीर्ण हुआ या नहीं। (यह निष्कर्ष निकालना कि वह अनुत्तीर्ण हुआ, पूर्ववर्ती के निषेध की भूल होगी।)",
   "lr-ds-a-pass-that-does-not-follow", _ds1)

def _ds2():
    s1 = {(47 - 1) // 12 + 1}
    s2 = set(range(1, 11))
    both = s1
    assert s1 == {4}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "In which row of a hall is seat number 47?",
   "एक सभागार में सीट संख्या 47 किस पंक्ति में है?",
   "Each row has 12 seats, and the seats are numbered continuously, row by row, starting from the front row.", "हर पंक्ति में 12 सीटें हैं, और सीटें आगे की पंक्ति से शुरू करके पंक्ति-दर-पंक्ति लगातार क्रमांकित हैं।",
   "The hall has 10 rows.", "सभागार में 10 पंक्तियाँ हैं।",
   0,
   "Statement I: rows 1 to 3 hold seats 1 to 36 and row 4 holds seats 37 to 48, so seat 47 is in row 4 -- sufficient. Statement II gives only the number of rows and says nothing about how the seats are numbered -- not sufficient. One statement alone answers the question.",
   "कथन I: पंक्तियाँ 1 से 3 में सीटें 1 से 36 हैं और पंक्ति 4 में सीटें 37 से 48, इसलिए सीट 47 पंक्ति 4 में है -- पर्याप्त। कथन II केवल पंक्तियों की संख्या देता है और यह कुछ नहीं कहता कि सीटें कैसे क्रमांकित हैं -- पर्याप्त नहीं। एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-the-row-of-seat-47", _ds2)

def _ds3():
    s1 = {True}            # I: today is Sunday, and every Sunday is a holiday
    s2 = {True}            # II: today is the 15th, and the 15th of this month is a holiday
    return _ds(s1, s2, s1 & s2)
DS(LR, "easy",
   "Is today a holiday?",
   "क्या आज छुट्टी है?",
   "Today is a Sunday, and every Sunday is a holiday.", "आज रविवार है, और हर रविवार छुट्टी होती है।",
   "Today is the 15th of the month, and the 15th of this month is a holiday.", "आज महीने की 15 तारीख़ है, और इस महीने की 15 तारीख़ छुट्टी है।",
   1,
   "Statement I alone shows that today is a holiday, and so does Statement II alone, each by its own route. Either statement is sufficient.",
   "कथन I अकेला दिखाता है कि आज छुट्टी है, और कथन II अकेला भी, हर एक अपने ढंग से। कोई भी एक कथन पर्याप्त है।",
   "lr-ds-a-holiday-found-two-ways", _ds3)
