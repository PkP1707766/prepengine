# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 8 -- Logical Reasoning (17 items: 14 in the Reasoning slots, 3 in the data-sufficiency block).

Layout B, the 2025 shape. Exam-level mix (1 easy / 8 medium / 8 hard), with none of the shapes of Levels 1-7:
advice dismissed because of the adviser's own habit, a remedy called safe because it is natural, an argument matched
by its pattern (one of two, and not the other), a risk halved from two in ten thousand, a fossil dated to the year,
a pattern among districts applied to each woman in them; drums, flutes and bamboo; the son of a daughter of a maternal
grandfather; a code that reads a word down its columns; the left bank of a river that flows north; a slab one cube
thick; six trains on six platforms, a queue that changes four times; three witnesses who each tell one truth and one
lie; and in the data-sufficiency block a weight on both pans, an uncle found two ways, and the 20th letter of a pattern
that repeats. Relation, code, direction, cube, arrangement and witness keys are found by checking every case."""
from itertools import combinations, permutations, product
import random
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- advice dismissed because of the adviser's own habit
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'The health minister tells us to give up sugary drinks, yet the minister drinks three colas a day. So the advice can safely be ignored.' Which one of the following best describes the flaw in this argument?",
  "'स्वास्थ्य मंत्री हमें मीठे पेय छोड़ने को कहते हैं, फिर भी मंत्री स्वयं दिन में तीन कोला पीते हैं। इसलिए इस सलाह की बेझिझक अनदेखी की जा सकती है।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It rejects the advice because of the adviser's habits, which do not show whether the advice is sound.",
   "It assumes that a health minister must know more about health than any of the people being advised.",
   "It generalises from the habits of a single minister to the habits of everyone who holds public office.",
   "It treats the minister's fondness for colas as the cause of the advice that the minister has given."],
  ["यह सलाह को सलाहकार की अपनी आदतों के कारण ठुकराता है, जिनसे यह पता नहीं चलता कि सलाह ठीक है या नहीं।",
   "यह मान लेता है कि स्वास्थ्य मंत्री को स्वास्थ्य के बारे में सलाह पाने वाले हर व्यक्ति से अधिक जानकारी होनी चाहिए।",
   "यह एक मंत्री की आदतों से सार्वजनिक पद पर बैठे हर व्यक्ति की आदतों के बारे में सामान्य निष्कर्ष निकालता है।",
   "यह मंत्री के कोला-प्रेम को मंत्री द्वारा दी गई सलाह का कारण मान लेता है।"],
  0,
  "Whether sugary drinks are harmful depends on the evidence about sugary drinks, not on whether the person giving the advice follows it. A hypocrite can give sound advice. "
  "The argument makes no claim about how much the minister knows; it draws no conclusion about other office-holders; and it does not say the cola habit caused the advice.",
  "मीठे पेय हानिकारक हैं या नहीं, यह मीठे पेयों के बारे में प्रमाण पर निर्भर है, इस पर नहीं कि सलाह देने वाला स्वयं उसका पालन करता है या नहीं। पाखंडी भी ठीक सलाह दे सकता है। "
  "तर्क मंत्री की जानकारी के बारे में कोई दावा नहीं करता; वह दूसरे पदधारियों के बारे में कोई निष्कर्ष नहीं निकालता; और वह यह नहीं कहता कि कोला की आदत सलाह का कारण बनी।",
  "lr-sc-advice-dismissed-because-of-the-adviser-s-habit")

# 2 -- a remedy called safe because it is natural
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'This hair oil is made only from natural herbs, so it cannot do anyone any harm.' Which one of the following is an assumption on which this argument depends?",
  "'यह केश तेल केवल प्राकृतिक जड़ी-बूटियों से बना है, इसलिए यह किसी को कोई हानि नहीं पहुँचा सकता।' निम्नलिखित में से कौन-सी पूर्वधारणा है जिस पर यह तर्क निर्भर करता है?",
  ["Nothing that comes wholly from nature can be harmful.",
   "Hair oils made from chemicals always do some harm to their users.",
   "Natural herbs cost less to grow than chemicals cost to make in factories.",
   "Most buyers of hair oil would rather use natural products than man-made ones."],
  ["जो कुछ पूरी तरह प्रकृति से आता है, वह हानिकारक नहीं हो सकता।",
   "रसायनों से बने केश तेल अपने उपयोगकर्ताओं को सदा कुछ हानि पहुँचाते हैं।",
   "प्राकृतिक जड़ी-बूटियाँ उगाना कारख़ानों में रसायन बनाने से सस्ता पड़ता है।",
   "केश तेल के अधिकांश ख़रीदार मानव-निर्मित के बजाय प्राकृतिक उत्पाद पसंद करेंगे।"],
  0,
  "The argument moves from 'natural' straight to 'harmless'. That step holds only if whatever comes wholly from nature is harmless -- an assumption that is false, since many plants are poisonous or cause allergies. "
  "It says nothing about oils made from chemicals, so it need not assume they always harm; and costs and buyers' tastes have no bearing on whether the oil is safe.",
  "तर्क 'प्राकृतिक' से सीधे 'हानिरहित' पर पहुँच जाता है। यह क़दम तभी टिकता है जब जो कुछ पूरी तरह प्रकृति से आता है वह हानिरहित हो -- यह पूर्वधारणा ग़लत है, क्योंकि बहुत-से पौधे विषैले होते हैं या एलर्जी करते हैं। "
  "तर्क रसायनों से बने तेलों के बारे में कुछ नहीं कहता, इसलिए उसे यह मानने की आवश्यकता नहीं कि वे सदा हानि पहुँचाते हैं; और लागत तथा ख़रीदारों की पसंद का तेल के सुरक्षित होने से कोई संबंध नहीं।",
  "lr-sc-a-remedy-called-safe-because-it-is-natural")

# 3 -- an argument matched by its pattern
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'Either the fuse has blown or the bulb has failed. The bulb has not failed. So the fuse has blown.' Which one of the following arguments is most similar in its pattern of reasoning to the argument above?",
  "'या तो फ़्यूज़ उड़ गया है या बल्ब ख़राब हो गया है। बल्ब ख़राब नहीं हुआ है। इसलिए फ़्यूज़ उड़ गया है।' निम्नलिखित में से कौन-सा तर्क अपनी तर्क-पद्धति में ऊपर के तर्क के सबसे समान है?",
  ["Either the train is late or my watch is fast. My watch is not fast. So the train is late.",
   "Either the train is late or my watch is fast. The train is late. So my watch is not fast.",
   "If the train is late, then my watch is fast. My watch is not fast. So the train is not late.",
   "Every train on this line runs late in the monsoon. This is the monsoon. So this train is late."],
  ["या तो रेलगाड़ी देर से है या मेरी घड़ी आगे है। मेरी घड़ी आगे नहीं है। इसलिए रेलगाड़ी देर से है।",
   "या तो रेलगाड़ी देर से है या मेरी घड़ी आगे है। रेलगाड़ी देर से है। इसलिए मेरी घड़ी आगे नहीं है।",
   "यदि रेलगाड़ी देर से है, तो मेरी घड़ी आगे है। मेरी घड़ी आगे नहीं है। इसलिए रेलगाड़ी देर से नहीं है।",
   "इस लाइन की हर रेलगाड़ी मानसून में देर से चलती है। अभी मानसून है। इसलिए यह रेलगाड़ी देर से है।"],
  0,
  "The original has the form 'A or B; not B; so A'. The argument about the late train and the fast watch has exactly that form. "
  "The argument that infers 'my watch is not fast' runs 'A or B; A; so not B', which is a different (and invalid) pattern, since both could be true at once; the 'if ... then' argument starts from a condition, not from two alternatives; and the monsoon argument applies a general rule to one case.",
  "मूल तर्क का रूप है 'A या B; B नहीं; इसलिए A'। देर से चलती रेलगाड़ी और आगे चलती घड़ी वाले तर्क का ठीक यही रूप है। "
  "'मेरी घड़ी आगे नहीं है' निकालने वाला तर्क 'A या B; A; इसलिए B नहीं' है, जो एक भिन्न (और अमान्य) पद्धति है, क्योंकि दोनों एक साथ सच हो सकते हैं; 'यदि ... तो' वाला तर्क दो विकल्पों से नहीं, एक शर्त से शुरू होता है; और मानसून वाला तर्क एक सामान्य नियम को एक स्थिति पर लागू करता है।",
  "lr-sc-an-argument-matched-by-its-pattern")

# 4 -- a risk halved from two in ten thousand
T(LR, "Statement-Conclusion/Assumption", "hard",
  "A newspaper headline reads: 'New medicine halves the risk of a rare illness!' In the trial behind it, 2 in every 10,000 people who did not take the medicine got the illness, against 1 in every 10,000 who took it. Which one of the following conclusions is best supported by these figures?",
  "एक समाचार-पत्र का शीर्षक है: 'नई दवा एक दुर्लभ बीमारी का जोखिम आधा कर देती है!' इसके पीछे के परीक्षण में दवा न लेने वाले हर 10,000 लोगों में से 2 को बीमारी हुई, जबकि दवा लेने वाले हर 10,000 में से 1 को। इन आँकड़ों से निम्नलिखित में से कौन-सा निष्कर्ष सबसे अच्छी तरह समर्थित है?",
  ["Taking the medicine spares about 1 person in every 10,000 from the illness.",
   "Taking the medicine spares about half of all the people who take it from the illness.",
   "The headline is false, because the risk fell by only 1 in 10,000 and not by half.",
   "The medicine is not worth taking for anyone, since the illness it guards against is rare."],
  ["दवा लेने से हर 10,000 में से लगभग 1 व्यक्ति बीमारी से बचता है।",
   "दवा लेने से उसे लेने वाले सभी लोगों में से लगभग आधे बीमारी से बच जाते हैं।",
   "शीर्षक ग़लत है, क्योंकि जोखिम आधा नहीं, केवल 10,000 में 1 घटा।",
   "यह दवा किसी के लिए भी लेने योग्य नहीं, क्योंकि जिस बीमारी से यह बचाती है वह दुर्लभ है।"],
  0,
  "The risk falls from 2 in 10,000 to 1 in 10,000: halved in relative terms, but in absolute terms only 1 person in 10,000 is spared. "
  "'Half of all the people who take it' confuses halving the risk with sparing half the people -- most would never have fallen ill anyway. The headline is not false: from 2 to 1 is indeed half. And whether the medicine is worth taking depends on things the figures do not give, such as its cost and side effects.",
  "जोखिम 10,000 में 2 से घटकर 10,000 में 1 होता है: सापेक्ष रूप से आधा, पर निरपेक्ष रूप से 10,000 में केवल 1 व्यक्ति बचता है। "
  "'लेने वाले सभी लोगों में से आधे' जोखिम आधा होने को आधे लोगों के बचने से भ्रमित करता है -- अधिकांश वैसे भी कभी बीमार न पड़ते। शीर्षक ग़लत नहीं: 2 से 1 सचमुच आधा है। और दवा लेने योग्य है या नहीं, यह उन बातों पर निर्भर है जो आँकड़े नहीं बताते, जैसे उसकी लागत और दुष्प्रभाव।",
  "lr-sc-a-risk-halved-from-two-in-ten-thousand")

# 5 -- a fossil dated to the year
T(LR, "Statement-Conclusion/Assumption", "easy",
  "A museum guide tells visitors: 'This fossil is 65 million and 3 years old. When I started working here three years ago, I was told it was 65 million years old.' Which one of the following best describes the error in the guide's statement?",
  "एक संग्रहालय का गाइड दर्शकों से कहता है: 'यह जीवाश्म 6 करोड़ 50 लाख और 3 वर्ष पुराना है। जब मैंने तीन वर्ष पहले यहाँ काम शुरू किया था, तब मुझे बताया गया था कि यह 6 करोड़ 50 लाख वर्ष पुराना है।' निम्नलिखित में से कौन-सा गाइड के कथन की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It adds an exact figure to a rough estimate, claiming a precision it never had.",
   "It assumes that a fossil goes on growing older after it has been dug out of the rock.",
   "It relies on what one person was told instead of on any record kept by the museum.",
   "It confuses the age of the fossil with the length of time the museum has displayed it."],
  ["यह मोटे अनुमान में सटीक संख्या जोड़कर ऐसी सटीकता का दावा करता है जो उसमें कभी नहीं थी।",
   "यह मान लेता है कि चट्टान से निकाले जाने के बाद भी जीवाश्म और पुराना होता जाता है।",
   "यह संग्रहालय के किसी अभिलेख के बजाय उस पर निर्भर करता है जो एक व्यक्ति को बताया गया था।",
   "यह जीवाश्म की आयु को उस अवधि से भ्रमित करता है जितने समय से संग्रहालय उसे प्रदर्शित कर रहा है।"],
  0,
  "'65 million years' is a round estimate, uncertain by far more than three years; adding 3 to it gives an air of exactness the original figure never had. "
  "The fossil does grow older with time, so that is not the error; the trouble is not whose word it is but the false precision; and the guide does not mix up the fossil's age with how long it has been on display.",
  "'6 करोड़ 50 लाख वर्ष' एक गोल अनुमान है, जिसकी अनिश्चितता तीन वर्षों से कहीं अधिक है; उसमें 3 जोड़ना ऐसी सटीकता का आभास देता है जो मूल संख्या में कभी नहीं थी। "
  "जीवाश्म समय के साथ सचमुच पुराना होता है, इसलिए वह त्रुटि नहीं; कठिनाई यह नहीं कि बात किसकी है, बल्कि झूठी सटीकता है; और गाइड जीवाश्म की आयु को प्रदर्शन की अवधि से नहीं मिलाता।",
  "lr-sc-a-fossil-dated-to-the-year")

# 6 -- a pattern among districts applied to each woman in them
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'Districts in which a larger share of women can read and write have, on average, fewer children per woman. So in any district, a woman who can read and write will have fewer children than a woman who cannot.' Which one of the following best describes the flaw in this reasoning?",
  "'जिन ज़िलों में पढ़-लिख सकने वाली महिलाओं का अनुपात अधिक है, वहाँ औसतन प्रति महिला बच्चे कम हैं। इसलिए किसी भी ज़िले में, पढ़-लिख सकने वाली महिला के बच्चे न पढ़-लिख सकने वाली महिला से कम होंगे।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It applies a pattern found among whole districts to every woman within a district.",
   "It assumes that being able to read is the only reason why families have fewer children.",
   "It treats the average number of children in a district as if it were the largest number there.",
   "It uses figures about women in order to reach a conclusion about the men in those districts."],
  ["यह पूरे ज़िलों के बीच पाए गए पैटर्न को किसी ज़िले की हर महिला पर लागू कर देता है।",
   "यह मान लेता है कि पढ़ पाना ही वह अकेला कारण है जिससे परिवारों में बच्चे कम होते हैं।",
   "यह किसी ज़िले में बच्चों की औसत संख्या को ऐसे लेता है मानो वह वहाँ की सबसे बड़ी संख्या हो।",
   "यह महिलाओं के आँकड़ों से उन ज़िलों के पुरुषों के बारे में निष्कर्ष निकालता है।"],
  0,
  "The evidence compares districts as wholes; it says nothing about how individual women within a district compare, still less that every literate woman will have fewer children than every woman who is not. A pattern among groups need not hold for each member of them. "
  "The argument makes no claim that literacy is the only cause; it does not mistake an average for a maximum; and its conclusion is about women, not men.",
  "प्रमाण पूरे ज़िलों की तुलना करता है; वह यह नहीं बताता कि किसी ज़िले के भीतर अलग-अलग महिलाओं की तुलना कैसी है, यह तो बिल्कुल नहीं कि हर साक्षर महिला के बच्चे हर निरक्षर महिला से कम होंगे। समूहों के बीच का पैटर्न उनके हर सदस्य पर लागू हो, यह आवश्यक नहीं। "
  "तर्क यह दावा नहीं करता कि साक्षरता ही अकेला कारण है; वह औसत को अधिकतम नहीं समझता; और उसका निष्कर्ष महिलाओं के बारे में है, पुरुषों के नहीं।",
  "lr-sc-a-pattern-among-districts-applied-to-each-woman")

# 7 -- drums, flutes and bamboo
def _sy7():
    # classes drums (D), flutes (F), bamboo things (B): each of the seven regions is empty or not
    regions = [r for r in product((0, 1), repeat=3) if any(r)]     # (in D, in F, in B)
    one = two = True
    for present in product((0, 1), repeat=len(regions)):
        filled = {r for r, p in zip(regions, present) if p}
        if any(d and f for d, f, b in filled):                       # no drum is a flute
            continue
        if not any(f and b for d, f, b in filled):                   # some flutes are made of bamboo
            continue
        one &= any(b and not d for d, f, b in filled)
        two &= any(d and not b for d, f, b in filled)
    return c.T2R[{(True, True): 2, (True, False): 0, (False, True): 1, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "medium",
   "Statements: No drum is a flute. Some flutes are made of bamboo.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कोई ढोल बाँसुरी नहीं है। कुछ बाँसुरियाँ बाँस से बनी हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some things made of bamboo are not drums.", "Some drums are not made of bamboo."],
   ["बाँस से बनी कुछ वस्तुएँ ढोल नहीं हैं।", "कुछ ढोल बाँस से नहीं बने हैं।"],
   0,
   "Only I follows. The bamboo flutes are things made of bamboo, and since no drum is a flute, none of them is a drum. "
   "II does not follow: the statements say nothing about what drums are made of -- every drum might be made of bamboo without breaking either statement. II looks like I turned round, but 'some A are not B' cannot be reversed.",
   "केवल I निकलता है। बाँस की बाँसुरियाँ बाँस से बनी वस्तुएँ हैं, और चूँकि कोई ढोल बाँसुरी नहीं है, उनमें से कोई ढोल नहीं है। "
   "II नहीं निकलता: कथन यह नहीं बताते कि ढोल किससे बने हैं -- हर ढोल बाँस का हो सकता है और कोई कथन नहीं टूटता। II, I को उलटकर पढ़ने जैसा लगता है, पर 'कुछ A, B नहीं हैं' को उलटा नहीं जा सकता।",
   "lr-sy-drums-flutes-and-bamboo", roman=True, check=_sy7)

# 8 -- the son of a daughter of a maternal grandfather
def _br8():
    # Neha's mother M and her sisters are the daughters of M's father G; Neha's maternal uncle U is G's son.
    family = {"G": {"children": ["M", "A1", "A2", "U"]}}
    daughters = [d for d in family["G"]["children"] if d != "U"]
    rel = {"M": "Brother", "A1": "Cousin", "A2": "Cousin"}       # a son of each daughter, as seen by Neha (M's child)
    found = {rel[d] for d in daughters}
    assert found == {"Brother", "Cousin"}
    return "Brother or cousin"
T(LR, "Blood Relation", "hard",
  "Pointing to a boy, Neha says, 'He is the son of a daughter of the father of my maternal uncle.' How is the boy related to Neha?",
  "एक लड़के की ओर इशारा करते हुए नेहा कहती है, 'वह मेरे मामा के पिता की एक बेटी का बेटा है।' वह लड़का नेहा का क्या लगता है?",
  ["Brother or cousin", "Brother only", "Cousin only, through her mother's sister", "Nephew"],
  ["भाई या मौसेरा भाई", "केवल भाई", "केवल मौसेरा भाई, उसकी मौसी के द्वारा", "भतीजा या भांजा"],
  0,
  "The father of Neha's maternal uncle is her mother's father. A daughter of his is either Neha's mother herself or one of her mother's sisters, and the words do not say which. The boy is that daughter's son: Neha's brother if the daughter is her mother, her cousin if the daughter is her aunt. "
  "'Brother only' and 'cousin only' each pick one reading without warrant; a nephew would be the son of Neha's own brother or sister.",
  "नेहा के मामा के पिता उसकी माँ के पिता (नाना) हैं। उनकी बेटी या तो स्वयं नेहा की माँ है या उसकी माँ की कोई बहन (मौसी), और शब्द यह नहीं बताते कि कौन। लड़का उसी बेटी का बेटा है: बेटी माँ हो तो नेहा का भाई, मौसी हो तो मौसेरा भाई। "
  "'केवल भाई' और 'केवल मौसेरा भाई' बिना आधार के एक अर्थ चुन लेते हैं; भतीजा या भांजा नेहा के अपने भाई या बहन का बेटा होता।",
  "lr-br-the-son-of-a-daughter-of-a-maternal-grandfather", check=_br8)

# 9 -- a code that reads a word down its columns
def _code(word):
    rows = [word[i:i + 3] for i in range(0, len(word), 3)]
    return "".join(r[k] for k in range(3) for r in rows if k < len(r))
def _cd9():
    assert _code("GARDEN") == "GDAERN"
    return _code("PLANET")
T(LR, "Coding-Decoding", "medium",
  "In a code, a word is written in rows of three letters, one row below another, and then read column by column from top to bottom, starting with the left-hand column. In this code GARDEN is written as GDAERN. How is PLANET written in the same code?",
  "एक कूट में किसी शब्द को तीन-तीन अक्षरों की पंक्तियों में, एक पंक्ति के नीचे दूसरी, लिखा जाता है और फिर बाएँ स्तंभ से शुरू करके स्तंभ-दर-स्तंभ ऊपर से नीचे पढ़ा जाता है। इस कूट में GARDEN को GDAERN लिखा जाता है। उसी कूट में PLANET कैसे लिखा जाएगा?",
  ["PNLEAT", "PLNAET", "PNELAT", "TENALP"],
  ["PNLEAT", "PLNAET", "PNELAT", "TENALP"],
  0,
  "GARDEN in rows of three is GAR above DEN; reading down the columns gives G-D, A-E, R-N: GDAERN, which confirms the rule. PLANET gives PLA above NET, and the columns read P-N, L-E, A-T: PNLEAT. "
  "PLNAET reads in pairs along the rows instead of down the columns; PNELAT takes the second row's letters in the wrong order; TENALP simply reverses the word.",
  "GARDEN को तीन-तीन की पंक्तियों में लिखें तो GAR के नीचे DEN; स्तंभों को नीचे की ओर पढ़ने पर G-D, A-E, R-N: GDAERN, जिससे नियम की पुष्टि होती है। PLANET से PLA के नीचे NET बनता है, और स्तंभ P-N, L-E, A-T पढ़े जाते हैं: PNLEAT। "
  "PLNAET स्तंभों के बजाय पंक्तियों के साथ जोड़ों में पढ़ता है; PNELAT दूसरी पंक्ति के अक्षर ग़लत क्रम में लेता है; TENALP शब्द को केवल उलट देता है।",
  "lr-cd-a-code-that-reads-a-word-down-its-columns", check=_cd9)

# 10 -- the left bank of a river that flows north
def _dd10():
    vec = {"north": (0, 1), "south": (0, -1), "east": (1, 0), "west": (-1, 0)}
    left_of = lambda d: (-d[1], d[0])                     # turning 90° anticlockwise
    flow = vec["north"]
    bank = left_of(flow)                                  # the left bank lies on this side of the river
    facing = vec["south"]                                 # facing upstream
    to_river = (-bank[0], -bank[1])                       # from the bank, the river lies the other way
    side = "On his left" if to_river == left_of(facing) else "On his right" if to_river == (-left_of(facing)[0], -left_of(facing)[1]) else "?"
    assert bank == vec["west"]
    return side
T(LR, "Direction & Distance", "medium",
  "A river flows from south to north. Ravi stands on its left bank -- the bank on the left of a person who faces downstream -- and turns to face upstream. On which side of Ravi is the river?",
  "एक नदी दक्षिण से उत्तर की ओर बहती है। रवि उसके बाएँ तट पर खड़ा है -- वह तट जो धारा की दिशा में मुँह किए व्यक्ति के बाईं ओर होता है -- और प्रवाह के विपरीत दिशा में मुँह कर लेता है। नदी रवि की किस ओर है?",
  ["On his left", "On his right", "In front of him", "Behind him"],
  ["उसके बाईं ओर", "उसके दाईं ओर", "उसके सामने", "उसके पीछे"],
  0,
  "Facing downstream means facing north, and a person facing north has the west on their left, so the left bank is the west bank and the river lies to the east of Ravi. Facing upstream, Ravi faces south, and for someone facing south the east is on the left. So the river is on his left. "
  "The trap is to assume that a 'left bank' keeps the river on one's right whichever way one faces; the river runs alongside him, so it is neither in front nor behind.",
  "धारा की दिशा में मुँह करने का अर्थ उत्तर की ओर मुँह करना है, और उत्तर की ओर मुँह किए व्यक्ति के बाईं ओर पश्चिम होता है, इसलिए बायाँ तट पश्चिमी तट है और नदी रवि के पूर्व में है। प्रवाह के विपरीत मुँह करने पर रवि दक्षिण की ओर देखता है, और दक्षिण की ओर देखने वाले के बाईं ओर पूर्व होता है। अतः नदी उसके बाईं ओर है। "
  "जाल यह मानना है कि 'बायाँ तट' होने से नदी हर दिशा में दाईं ओर रहती है; नदी उसके साथ-साथ बहती है, इसलिए न सामने है न पीछे।",
  "lr-dd-the-left-bank-of-a-river-that-flows-north", check=_dd10)

# 11 -- a slab one cube thick
def _cp11():
    L, W, H = 4, 4, 1
    count = {}
    for x, y, z in product(range(L), range(W), range(H)):
        faces = (x == 0) + (x == L - 1) + (y == 0) + (y == W - 1) + (z == 0) + (z == H - 1)
        count[faces] = count.get(faces, 0) + 1
    assert count == {4: 4, 3: 8, 2: 4}
    return str(count[3])
N(LR, "Cube Painting", "hard",
  "A slab measuring 4 cm × 4 cm × 1 cm is painted on all its faces and then cut into 1 cm cubes. How many of the small cubes have exactly three faces painted?",
  "4 सेमी × 4 सेमी × 1 सेमी माप की एक पट्टी को उसके सभी फलकों पर रंगा जाता है और फिर 1 सेमी के घनों में काटा जाता है। कितने छोटे घनों के ठीक तीन फलक रंगे हैं?",
  ["0", "4", "8", "12"], 2,
  "The slab is only one cube thick, so every small cube has paint on its top and its bottom. Add the sides on the slab's edge: the 4 corner cubes have two side faces painted (4 in all), the 8 cubes along the edges between the corners have one (3 in all), and the 4 in the middle have none (2 in all). So 8 cubes have exactly three faces painted. "
  "4 applies the rule for a large cube, where only the corners have three painted faces -- here the corners have four; 12 counts the corners as well; 0 forgets the painted bottom.",
  "पट्टी केवल एक घन मोटी है, इसलिए हर छोटे घन के ऊपर और नीचे रंग है। अब पट्टी के किनारे की भुजाएँ जोड़ें: 4 कोने वाले घनों के दो पार्श्व फलक रंगे हैं (कुल 4), कोनों के बीच किनारों पर के 8 घनों का एक (कुल 3), और बीच के 4 घनों का कोई नहीं (कुल 2)। अतः 8 घनों के ठीक तीन फलक रंगे हैं। "
  "4 बड़े घन का नियम लगाता है, जिसमें केवल कोनों के तीन फलक रंगे होते हैं -- यहाँ कोनों के चार हैं; 12 कोनों को भी गिनता है; 0 रंगे हुए निचले फलक को भूल जाता है।",
  "lr-cp-a-slab-one-cube-thick", _cp11)

# 12 -- six trains on six platforms
TRAINS = "ABCDEF"   # Ajmer, Bareilly, Cuttack, Dehradun, Erode, Firozpur
CLUES12 = [
    lambda q: q["D"] in (1, 6),
    lambda q: q["C"] == q["B"] + 1,
    lambda q: abs(q["A"] - q["F"]) == 3,
    lambda q: q["B"] % 2 == 0,
    lambda q: q["A"] > q["F"],
    lambda q: q["E"] > q["B"],
]
def _sa12():
    fits = [dict(zip(TRAINS, p)) for p in permutations(range(1, 7)) if all(f(dict(zip(TRAINS, p))) for f in CLUES12)]
    assert len(fits) == 1
    for i in range(len(CLUES12)):                         # every clue is needed
        rest = CLUES12[:i] + CLUES12[i + 1:]
        assert sum(1 for p in permutations(range(1, 7)) if all(f(dict(zip(TRAINS, p))) for f in rest)) > 1
    q = fits[0]
    assert "".join(sorted(TRAINS, key=q.get)) == "FBCAED"
    return str(abs(q["D"] - q["B"]) - 1)
N(LR, "Seating Arrangement", "hard",
  "Six trains -- to Ajmer, Bareilly, Cuttack, Dehradun, Erode and Firozpur -- stand at the six platforms of a station, numbered 1 to 6 from west to east, one train to a platform.\n"
  "- The Dehradun train is at platform 1 or platform 6.\n"
  "- The Cuttack train is at the platform immediately east of the Bareilly train.\n"
  "- Exactly two platforms lie between the Ajmer train and the Firozpur train, and the Ajmer train is east of the Firozpur train.\n"
  "- The Bareilly train is at an even-numbered platform.\n"
  "- The Erode train is east of the Bareilly train.\n"
  "How many platforms lie between the Bareilly train and the Dehradun train?",
  "छह रेलगाड़ियाँ -- अजमेर, बरेली, कटक, देहरादून, इरोड और फ़िरोज़पुर की -- एक स्टेशन के छह प्लेटफ़ॉर्मों पर खड़ी हैं, जो पश्चिम से पूर्व 1 से 6 तक क्रमांकित हैं, हर प्लेटफ़ॉर्म पर एक रेलगाड़ी।\n"
  "- देहरादून की रेलगाड़ी प्लेटफ़ॉर्म 1 या प्लेटफ़ॉर्म 6 पर है।\n"
  "- कटक की रेलगाड़ी बरेली की रेलगाड़ी के ठीक पूर्व वाले प्लेटफ़ॉर्म पर है।\n"
  "- अजमेर और फ़िरोज़पुर की रेलगाड़ियों के बीच ठीक दो प्लेटफ़ॉर्म हैं, और अजमेर की रेलगाड़ी फ़िरोज़पुर की रेलगाड़ी के पूर्व में है।\n"
  "- बरेली की रेलगाड़ी सम-संख्या वाले प्लेटफ़ॉर्म पर है।\n"
  "- इरोड की रेलगाड़ी बरेली की रेलगाड़ी के पूर्व में है।\n"
  "बरेली और देहरादून की रेलगाड़ियों के बीच कितने प्लेटफ़ॉर्म हैं?",
  ["1", "2", "3", "4"], 2,
  "Ajmer and Firozpur stand three platforms apart with Ajmer to the east: (1, 4), (2, 5) or (3, 6) for Firozpur and Ajmer. Bareilly is at 2 or 4 with Cuttack just east, at 3 or 5. "
  "If Bareilly-Cuttack were at 4-5, Erode (east of Bareilly) would need 6 and Dehradun 1, leaving 2 and 3 for Ajmer and Firozpur, which are not three apart -- impossible. So Bareilly is at 2 and Cuttack at 3. Then (2, 5) and (3, 6) are blocked, so Firozpur and Ajmer are at 1 and 4; Dehradun takes 6 and Erode 5. "
  "The order is Firozpur, Bareilly, Cuttack, Ajmer, Erode, Dehradun, and between Bareilly (2) and Dehradun (6) lie platforms 3, 4 and 5: three.",
  "अजमेर और फ़िरोज़पुर तीन प्लेटफ़ॉर्म की दूरी पर हैं और अजमेर पूर्व में है: फ़िरोज़पुर और अजमेर के लिए (1, 4), (2, 5) या (3, 6)। बरेली 2 या 4 पर है और कटक ठीक पूर्व में, 3 या 5 पर। "
  "यदि बरेली-कटक 4-5 पर होते, तो इरोड (बरेली के पूर्व) को 6 और देहरादून को 1 चाहिए होता, जिससे अजमेर और फ़िरोज़पुर के लिए 2 और 3 बचते, जो तीन की दूरी पर नहीं -- असंभव। इसलिए बरेली 2 पर और कटक 3 पर है। तब (2, 5) और (3, 6) रुक जाते हैं, इसलिए फ़िरोज़पुर और अजमेर 1 और 4 पर हैं; देहरादून 6 लेता है और इरोड 5। "
  "क्रम है फ़िरोज़पुर, बरेली, कटक, अजमेर, इरोड, देहरादून, और बरेली (2) तथा देहरादून (6) के बीच प्लेटफ़ॉर्म 3, 4 और 5 हैं: तीन।",
  "lr-sa-six-trains-on-six-platforms", _sa12)

# 13 -- a queue that changes four times
def _sa13():
    q = list("PQRST")
    q.pop(0)                                   # the person at the front is served and leaves
    i = q.index("S"); q.insert(i - 2, q.pop(i))  # S moves two places forward
    q.append("U")                              # U joins at the back
    q[1], q[2] = q[2], q[1]                    # the person now second lets the one behind go ahead
    assert q == list("SRQTU")
    return q[2]
T(LR, "Seating Arrangement", "medium",
  "Five people stand in a queue in the order P, Q, R, S, T, with P at the front. Then, one after another: the person at the front is served and leaves; S moves two places forward; U joins at the back; and the person who is now second lets the person just behind go ahead. Who is now third in the queue?",
  "पाँच लोग P, Q, R, S, T के क्रम में एक पंक्ति में खड़े हैं, P सबसे आगे है। फिर एक के बाद एक: सबसे आगे वाले का काम होता है और वह चला जाता है; S दो स्थान आगे बढ़ता है; U पीछे जुड़ता है; और जो अब दूसरे स्थान पर है, वह अपने ठीक पीछे वाले को आगे जाने देता है। अब पंक्ति में तीसरे स्थान पर कौन है?",
  ["Q", "R", "S", "T"], ["Q", "R", "S", "T"],
  0,
  "After P leaves the queue is Q, R, S, T. S moves two places forward, past R and Q: S, Q, R, T. U joins at the back: S, Q, R, T, U. Q, now second, lets R go ahead: S, R, Q, T, U. Q is third. "
  "R is third only if the last swap is forgotten; S, if S moves just one place forward; T, if the person served is not removed.",
  "P के जाने के बाद पंक्ति Q, R, S, T है। S, R और Q को पार करके दो स्थान आगे बढ़ता है: S, Q, R, T। U पीछे जुड़ता है: S, Q, R, T, U। अब दूसरे स्थान पर Q, R को आगे जाने देता है: S, R, Q, T, U। Q तीसरे स्थान पर है। "
  "R तीसरा तभी होता जब अंतिम अदला-बदली भुला दी जाए; S, यदि S केवल एक स्थान आगे बढ़े; T, यदि जिसका काम हुआ उसे हटाया न जाए।",
  "lr-sa-a-queue-that-changes-four-times", check=_sa13)

# 14 -- three witnesses who each tell one truth and one lie
def _tl14():
    did = lambda x, t: t == x
    witnesses = [
        (lambda t: not did("Q", t), lambda t: did("S", t)),
        (lambda t: not did("P", t), lambda t: did("Q", t)),
        (lambda t: did("P", t), lambda t: not did("Q", t)),
    ]
    fits = [t for t in "PQRS" if all(a(t) != b(t) for a, b in witnesses)]
    assert fits == ["R"]
    return fits[0]
T(LR, "Truth-Liar", "hard",
  "Cash has gone missing from a shop, and exactly one of P, Q, R and S took it. Three witnesses each make two statements, and each witness makes exactly one true statement and one false one.\n"
  "Witness 1: 'Q did not take it.' 'S took it.'\n"
  "Witness 2: 'P did not take it.' 'Q took it.'\n"
  "Witness 3: 'P took it.' 'Q did not take it.'\n"
  "Who took the cash?",
  "एक दुकान से नक़दी ग़ायब हो गई है, और P, Q, R और S में से ठीक एक ने उसे लिया। तीन गवाहों में से हर एक दो कथन देता है, और हर गवाह का ठीक एक कथन सच और एक झूठ है।\n"
  "गवाह 1: 'Q ने नहीं लिया।' 'S ने लिया।'\n"
  "गवाह 2: 'P ने नहीं लिया।' 'Q ने लिया।'\n"
  "गवाह 3: 'P ने लिया।' 'Q ने नहीं लिया।'\n"
  "नक़दी किसने ली?",
  ["R", "P", "Q", "S"], ["R", "P", "Q", "S"],
  0,
  "Test each suspect. If P took it, Witness 2's statements are both false. If Q took it, Witness 1's are both false. If S took it, Witness 1's are both true. If R took it, Witness 1 is right that Q did not and wrong about S; Witness 2 is right about P and wrong about Q; Witness 3 is wrong about P and right about Q -- one truth and one lie each. So R took it, though no witness names R. "
  "P, Q and S each leave some witness with two true or two false statements.",
  "हर संदिग्ध को जाँचें। यदि P ने लिया, तो गवाह 2 के दोनों कथन झूठे हैं। यदि Q ने लिया, तो गवाह 1 के दोनों झूठे हैं। यदि S ने लिया, तो गवाह 1 के दोनों सच हैं। यदि R ने लिया, तो गवाह 1 का यह कहना सही है कि Q ने नहीं लिया और S के बारे में ग़लत; गवाह 2, P के बारे में सही और Q के बारे में ग़लत; गवाह 3, P के बारे में ग़लत और Q के बारे में सही -- हर एक का एक सच और एक झूठ। अतः R ने लिया, यद्यपि कोई गवाह R का नाम नहीं लेता। "
  "P, Q और S में से हर एक किसी गवाह के दोनों कथन सच या दोनों झूठ कर देता है।",
  "lr-tl-three-witnesses-who-each-tell-one-truth-and-one-lie", check=_tl14)

# ---- the data-sufficiency block's three Reasoning items
def _ds15():
    rng = random.Random(15)
    s1, s2, both = set(), set(), set()
    for _ in range(4000):
        r, b, g = (rng.randint(1, 20) for _ in range(3))
        i1, i2 = r + g > b + g, r > g > b
        if i1: s1.add(r > b)
        if i2: s2.add(r > b)
        if i1 and i2: both.add(r > b)
    assert s1 == s2 == {True}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "There are three boxes: red, blue and green. Is the red box heavier than the blue box?",
   "तीन डिब्बे हैं: लाल, नीला और हरा। क्या लाल डिब्बा नीले डिब्बे से भारी है?",
   "The red and green boxes together are heavier than the blue and green boxes together.", "लाल और हरा डिब्बा मिलकर नीले और हरे डिब्बे से मिलकर भारी हैं।",
   "The red box is heavier than the green box, and the green box is heavier than the blue box.", "लाल डिब्बा हरे से भारी है, और हरा डिब्बा नीले से भारी है।",
   1,
   "Statement I alone: the green box is on both sides, so taking it away from both leaves the red box heavier than the blue -- yes. Statement II alone: red is heavier than green, which is heavier than blue, so red is heavier than blue -- yes. Either statement alone answers the question.",
   "कथन I अकेले: हरा डिब्बा दोनों ओर है, इसलिए दोनों ओर से उसे हटाने पर लाल डिब्बा नीले से भारी बचता है -- हाँ। कथन II अकेले: लाल, हरे से भारी है, जो नीले से भारी है, इसलिए लाल, नीले से भारी है -- हाँ। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-weight-on-both-pans", _ds15)

def _ds16():
    # Who can Ravi (a man) be to Sita under each statement?
    s1 = {"uncle"}                                             # brother of Sita's mother: her maternal uncle
    s2 = {"father", "uncle"}                                   # a son of Sita's grandfather: her father, or her father's or mother's brother
    both = s1 & s2
    return _ds({x == "uncle" for x in s1}, {x == "uncle" for x in s2}, {x == "uncle" for x in both})
DS(LR, "medium",
   "Ravi is a man. Is Ravi an uncle of Sita?",
   "रवि एक पुरुष है। क्या रवि, सीता का अंकल (चाचा, ताऊ, मामा, मौसा या फूफा) है?",
   "Ravi is the brother of Sita's mother.", "रवि, सीता की माँ का भाई है।",
   "Ravi's father is Sita's grandfather.", "रवि के पिता, सीता के दादा/नाना हैं।",
   0,
   "Statement I alone: the brother of Sita's mother is her maternal uncle -- yes. Statement II alone: a son of Sita's grandfather may be Sita's own father, or her father's or mother's brother, so the answer could be yes or no. One statement alone is enough, but not the other.",
   "कथन I अकेले: सीता की माँ का भाई उसका मामा है -- हाँ। कथन II अकेले: सीता के दादा/नाना का बेटा स्वयं सीता का पिता हो सकता है, या उसके पिता या माँ का भाई, इसलिए उत्तर हाँ या नहीं, दोनों हो सकता है। एक कथन अकेले पर्याप्त है, पर दूसरा नहीं।",
   "lr-ds-an-uncle-found-two-ways", _ds16)

def _ds17():
    letters = "KXY"
    def twentieth(period, fixed):
        # every pattern with this period that fits the fixed letters: the set of possible 20th letters
        out = set()
        for pat in product(letters, repeat=period):
            if all(pat[(p - 1) % period] == ch for p, ch in fixed.items()):
                out.add(pat[(20 - 1) % period])
        return out
    known = {2: "K", 8: "K", 14: "K"}
    s1 = twentieth(6, {})
    s2 = set().union(*(twentieth(p, known) for p in range(1, 8)))
    both = twentieth(6, known)
    assert len(s1) > 1 and len(s2) > 1 and both == {"K"}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "A long row of letters follows a pattern that repeats. What is the 20th letter of the row?",
   "अक्षरों की एक लंबी पंक्ति एक दोहराने वाले पैटर्न पर चलती है। पंक्ति का 20वाँ अक्षर क्या है?",
   "The pattern repeats every 6 letters.", "पैटर्न हर 6 अक्षरों के बाद दोहराता है।",
   "The 2nd, 8th and 14th letters are all K.", "दूसरा, आठवाँ और चौदहवाँ अक्षर, तीनों K हैं।",
   2,
   "Statement I alone gives the length of the pattern but none of its letters. Statement II alone gives three letters but not the length: a pattern of 6 would put K 20th too, but with a 7-letter pattern, for instance, the K's at places 2, 8 and 14 fix only three of its letters, and the 20th letter falls on one that is still free. "
   "Together: with a 6-letter pattern the 20th letter stands where the 2nd, 8th and 14th do (20 = 2 + 3 × 6), so it is K. Both statements are needed.",
   "कथन I अकेले पैटर्न की लंबाई बताता है पर उसका कोई अक्षर नहीं। कथन II अकेले तीन अक्षर बताता है पर लंबाई नहीं: 6 का पैटर्न 20वें स्थान पर भी K रखता, पर, उदाहरण के लिए, 7 अक्षरों के पैटर्न में स्थान 2, 8 और 14 के K उसके केवल तीन अक्षर तय करते हैं, और 20वाँ अक्षर किसी ऐसे अक्षर पर पड़ता है जो अभी अनिर्धारित है। "
   "दोनों मिलकर: 6 अक्षरों के पैटर्न में 20वाँ अक्षर उसी स्थान पर पड़ता है जहाँ दूसरा, आठवाँ और चौदहवाँ (20 = 2 + 3 × 6), इसलिए वह K है। दोनों कथन आवश्यक हैं।",
   "lr-ds-the-20th-letter-of-a-pattern-that-repeats", _ds17)
