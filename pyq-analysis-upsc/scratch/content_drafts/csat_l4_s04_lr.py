# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 4 -- Logical Reasoning (15 items: 12 in the Reasoning slots, 3 in the data-sufficiency block).

Layout A again, the lighter 2023/2024 Reasoning section. Exam-level mix (1 easy / 6 medium / 8 hard), with none of
the shapes of Levels 1-3 or Simulators 1-3: a claim saved by redefining its terms, a coin that is thought to be due
for tails, an argument that denies its own condition, a safe load found by splitting the difference; how women,
mothers and doctors are related as classes; a mother's only grandchild; a code that shifts the two halves of the
alphabet in opposite directions; a walk that goes backwards; a cube with its corners sliced off; a round table of
seven chairs with one left empty, four classes on four weekdays; a speaker who alternates truth and lies; and in the
data-sufficiency block the bottom face of a die, an islander who gives another away, and a row counted two ways.
Arrangement, relation, code, direction and truth-teller keys are found by checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a claim saved by redefining its terms
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Mohan: 'No good teacher ever loses patience with a student.' Sunita: 'But Mrs Rao, whom everyone calls the best teacher in our school, lost her patience with a student yesterday.' Mohan: 'Then she was never a good teacher after all.' Which one of the following best describes the flaw in Mohan's reasoning?",
  "मोहन: 'कोई भी अच्छा शिक्षक कभी किसी विद्यार्थी पर धैर्य नहीं खोता।' सुनीता: 'पर श्रीमती राव, जिन्हें सब हमारे विद्यालय की सबसे अच्छी शिक्षिका कहते हैं, कल एक विद्यार्थी पर धैर्य खो बैठीं।' मोहन: 'तब वे कभी अच्छी शिक्षिका थीं ही नहीं।' निम्नलिखित में से कौन-सा मोहन के तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["He protects his claim by refusing to let any example count against it.",
   "He attacks Sunita's motives for raising the example instead of answering her point.",
   "He draws a general rule about all teachers from what happened in one classroom.",
   "He assumes that any teacher who stays patient must also be a good teacher."],
  ["वह किसी भी उदाहरण को अपने दावे के विरुद्ध न गिनने देकर दावे को बचाता है।",
   "वह सुनीता की बात का उत्तर देने के बजाय उदाहरण देने के उसके इरादों पर हमला करता है।",
   "वह एक कक्षा में हुई घटना से सभी शिक्षकों के बारे में एक सामान्य नियम बना लेता है।",
   "वह मान लेता है कि जो भी शिक्षक धैर्य रखता है वह अच्छा शिक्षक भी होगा।"],
  0,
  "A good teacher who loses patience is exactly the kind of case that could test Mohan's claim. When Sunita offers one, Mohan decides that the teacher cannot have been good -- so no example could ever count against him, and his claim has quietly become true by definition rather than by evidence. "
  "He says nothing about Sunita's motives; it is Sunita, not Mohan, who brings a single case, which is a fair way to test a rule that says 'no'; and he never claims that patience is enough to make a teacher good.",
  "धैर्य खोने वाला अच्छा शिक्षक ठीक वैसा उदाहरण है जो मोहन के दावे को परख सकता है। जब सुनीता ऐसा उदाहरण देती है, मोहन तय कर लेता है कि वह शिक्षिका अच्छी रही ही नहीं होगी -- इसलिए कोई भी उदाहरण कभी उसके विरुद्ध नहीं गिना जा सकता, और उसका दावा चुपचाप प्रमाण से नहीं बल्कि परिभाषा से सत्य बन गया है। "
  "वह सुनीता के इरादों के बारे में कुछ नहीं कहता; एक उदाहरण मोहन नहीं, सुनीता देती है, जो 'कोई नहीं' कहने वाले नियम को परखने का उचित तरीक़ा है; और वह कभी यह दावा नहीं करता कि धैर्य अकेले किसी शिक्षक को अच्छा बना देता है।",
  "lr-sc-a-claim-saved-by-redefining-its-terms", pos=1)

# 2 -- a coin that is thought to be due for tails
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'A fair coin has come up heads in each of its last five tosses, so the next toss is more likely to come up tails.' Which one of the following best describes the flaw in this reasoning?",
  "'एक निष्पक्ष सिक्का अपनी पिछली पाँचों उछालों में चित आया है, इसलिए अगली उछाल में पट आने की संभावना अधिक है।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It treats the coin's past tosses as if they could change the chance of the next one.",
   "It takes the coin to be fair without first testing it over a large number of tosses.",
   "It draws a conclusion about every coin from what happened with a single coin.",
   "It assumes that what is true of each toss must be true of the five tosses together."],
  ["यह सिक्के की पिछली उछालों को ऐसे लेता है मानो वे अगली उछाल की संभावना बदल सकती हों।",
   "यह बहुत-सी उछालों में जाँचे बिना ही सिक्के को निष्पक्ष मान लेता है।",
   "यह एक ही सिक्के के साथ हुई घटना से हर सिक्के के बारे में निष्कर्ष निकाल लेता है।",
   "यह मान लेता है कि जो हर उछाल के लिए सत्य है वह पाँचों उछालों के लिए मिलाकर भी सत्य होगा।"],
  0,
  "Each toss of a fair coin is independent: the coin has no memory, so heads and tails stay equally likely on the sixth toss whatever came before. Five heads in a row was unlikely before it happened (1 in 32), but once it has happened it says nothing about the next toss. "
  "The argument states that the coin is fair, so it does not take that on trust as a flaw; it generalises to no other coin; and it does not reason from the parts to the whole.",
  "निष्पक्ष सिक्के की हर उछाल स्वतंत्र है: सिक्के की कोई स्मृति नहीं होती, इसलिए पहले चाहे जो हुआ हो, छठी उछाल में चित और पट समान रूप से संभावित रहते हैं। लगातार पाँच चित होना घटित होने से पहले असंभावित था (32 में 1), पर घटित हो जाने के बाद वह अगली उछाल के बारे में कुछ नहीं कहता। "
  "तर्क स्वयं कहता है कि सिक्का निष्पक्ष है, इसलिए उसे बिना जाँचे मानना त्रुटि नहीं; वह किसी अन्य सिक्के पर सामान्यीकरण नहीं करता; और वह अंशों से पूर्ण की ओर तर्क नहीं करता।",
  "lr-sc-a-coin-thought-to-be-due-for-tails", pos=2)

# 3 -- an argument that denies its own condition
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'If a student practises every day, she will pass the examination. Meera does not practise every day. So Meera will not pass the examination.' Which one of the following arguments has the same flaw?",
  "'यदि कोई विद्यार्थी हर दिन अभ्यास करती है, तो वह परीक्षा में उत्तीर्ण होगी। मीरा हर दिन अभ्यास नहीं करती। इसलिए मीरा परीक्षा में उत्तीर्ण नहीं होगी।' निम्नलिखित में से किस तर्क में वही त्रुटि है?",
  ["If a shop is in the main market, it is crowded. This shop is not in the main market, so it is not crowded.",
   "If a fruit is a mango, it tastes sweet. This fruit tastes sweet, so this fruit must be a mango.",
   "If it rains at night, the ground is wet in the morning. The ground is dry this morning, so it did not rain.",
   "If a train is more than an hour late, the passengers complain. Today's train is two hours late, so they will complain."],
  ["यदि कोई दुकान मुख्य बाज़ार में है, तो उसमें भीड़ रहती है। यह दुकान मुख्य बाज़ार में नहीं है, इसलिए इसमें भीड़ नहीं रहती।",
   "यदि कोई फल आम है, तो वह मीठा होता है। यह फल मीठा है, इसलिए यह फल अवश्य आम है।",
   "यदि रात में वर्षा होती है, तो सुबह ज़मीन गीली रहती है। आज सुबह ज़मीन सूखी है, इसलिए वर्षा नहीं हुई।",
   "यदि कोई रेलगाड़ी एक घंटे से अधिक देर से है, तो यात्री शिकायत करते हैं। आज की रेलगाड़ी दो घंटे देर से है, इसलिए वे शिकायत करेंगे।"],
  0,
  "The original argument denies the condition ('does not practise every day') and concludes that the result will not follow -- but daily practice was offered as one way to pass, not the only way. The shop argument makes exactly this move: a shop outside the main market may still be crowded. "
  "The mango argument has a different flaw, reasoning back from the result to the condition (other fruits are sweet too). The wet-ground and late-train arguments are both valid: one rules the condition out because the result did not happen, the other applies the rule to a case that meets it.",
  "मूल तर्क शर्त को नकारता है ('हर दिन अभ्यास नहीं करती') और निष्कर्ष निकालता है कि परिणाम नहीं होगा -- पर दैनिक अभ्यास उत्तीर्ण होने का एक रास्ता बताया गया था, एकमात्र नहीं। दुकान वाला तर्क ठीक यही करता है: मुख्य बाज़ार के बाहर की दुकान में भी भीड़ हो सकती है। "
  "आम वाले तर्क में अलग त्रुटि है, जो परिणाम से उलटकर शर्त तक तर्क करता है (और फल भी मीठे होते हैं)। गीली ज़मीन और देर से चल रही रेलगाड़ी वाले दोनों तर्क वैध हैं: एक परिणाम न होने से शर्त को ख़ारिज करता है, दूसरा नियम को ऐसी स्थिति पर लागू करता है जो उसे पूरा करती है।",
  "lr-sc-an-argument-that-denies-its-own-condition", pos=3)

# 4 -- a safe load found by splitting the difference
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Two engineers inspect an old bridge. One says it can safely carry lorries of up to 40 tonnes; the other says it cannot safely carry more than 10 tonnes. To be fair to both, the town council decides to allow lorries of up to 25 tonnes. Which one of the following best describes the flaw in the council's reasoning?",
  "दो अभियंता एक पुराने पुल की जाँच करते हैं। एक कहता है कि वह 40 टन तक के ट्रक सुरक्षित रूप से ढो सकता है; दूसरा कहता है कि वह 10 टन से अधिक सुरक्षित रूप से नहीं ढो सकता। दोनों के साथ न्याय करने के लिए नगर परिषद 25 टन तक के ट्रकों की अनुमति देने का निर्णय लेती है। निम्नलिखित में से कौन-सा परिषद के तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It assumes that the truth must lie halfway between two opposing claims.",
   "It rejects the advice of both engineers merely because the two of them disagree.",
   "It trusts the more experienced of the two engineers without giving any reason.",
   "It treats the bridge's safe record in the past as proof that it will stay safe."],
  ["यह मान लेती है कि सत्य दो विरोधी दावों के ठीक बीच में ही होगा।",
   "यह दोनों अभियंताओं की सलाह केवल इसलिए ठुकरा देती है कि दोनों असहमत हैं।",
   "यह बिना कोई कारण बताए दोनों में से अधिक अनुभवी अभियंता पर भरोसा कर लेती है।",
   "यह पुल के अतीत के सुरक्षित रिकॉर्ड को इस बात का प्रमाण मान लेती है कि वह सुरक्षित रहेगा।"],
  0,
  "Being fair to two people is not the same as being right about a bridge. The safe load is a fact about the bridge, and it need not lie midway between the two estimates: if the cautious engineer is right, 25 tonnes is two and a half times the safe load. The council should find out which estimate is correct, or keep to the lower one while it does. "
  "It does not reject both engineers -- it uses both figures; it prefers neither of them; and it says nothing about the bridge's past record.",
  "दो लोगों के साथ न्याय करना और किसी पुल के बारे में सही होना एक बात नहीं है। सुरक्षित भार पुल के बारे में एक तथ्य है, और उसका दोनों अनुमानों के बीच में होना आवश्यक नहीं: यदि सतर्क अभियंता सही है, तो 25 टन सुरक्षित भार का ढाई गुना है। परिषद को पता लगाना चाहिए कि कौन-सा अनुमान सही है, या तब तक निचले अनुमान पर टिके रहना चाहिए। "
  "वह दोनों अभियंताओं को ठुकराती नहीं -- वह दोनों के आँकड़ों का उपयोग करती है; वह किसी को वरीयता नहीं देती; और पुल के अतीत के रिकॉर्ड के बारे में कुछ नहीं कहती।",
  "lr-sc-a-safe-load-found-by-splitting-the-difference", pos=0)

# 5 -- how women, mothers and doctors are related
T(LR, "Syllogism", "easy",
  "Which one of the following best describes how the classes 'women', 'mothers' and 'doctors' are related?",
  "निम्नलिखित में से कौन-सा सबसे अच्छा वर्णन करता है कि 'महिलाएँ', 'माताएँ' और 'डॉक्टर' वर्ग आपस में कैसे संबंधित हैं?",
  ["Mothers lie wholly within women, and doctors overlap both of them.",
   "Women lie wholly within mothers, and doctors overlap both of them.",
   "Mothers lie wholly within women, and doctors lie wholly within mothers.",
   "The three classes overlap, but none of them lies wholly within another."],
  ["माताएँ पूरी तरह महिलाओं के भीतर हैं, और डॉक्टर दोनों से आंशिक रूप से मिलते हैं।",
   "महिलाएँ पूरी तरह माताओं के भीतर हैं, और डॉक्टर दोनों से आंशिक रूप से मिलते हैं।",
   "माताएँ पूरी तरह महिलाओं के भीतर हैं, और डॉक्टर पूरी तरह माताओं के भीतर हैं।",
   "तीनों वर्ग आपस में मिलते हैं, पर उनमें से कोई दूसरे के पूरी तरह भीतर नहीं है।"],
  0,
  "Every mother is a woman, but not every woman is a mother, so mothers lie wholly within women. Some doctors are women, some of them mothers, and some doctors are men, who are neither -- so doctors overlap both classes without lying inside either. "
  "Women do not lie within mothers; doctors are not all mothers; and mothers do lie wholly within women.",
  "हर माता महिला है, पर हर महिला माता नहीं, इसलिए माताएँ पूरी तरह महिलाओं के भीतर हैं। कुछ डॉक्टर महिलाएँ हैं, उनमें से कुछ माताएँ, और कुछ डॉक्टर पुरुष हैं, जो दोनों में से कुछ नहीं -- इसलिए डॉक्टर दोनों वर्गों से आंशिक रूप से मिलते हैं, किसी के भीतर हुए बिना। "
  "महिलाएँ माताओं के भीतर नहीं हैं; सभी डॉक्टर माताएँ नहीं हैं; और माताएँ सचमुच पूरी तरह महिलाओं के भीतर हैं।",
  "lr-sy-women-mothers-and-doctors", pos=1)

# 6 -- a mother's only grandchild
def _br6():
    # Neha's daughter D is the only grandchild of the man's mother M, so one of D's parents is M's child.
    # D's parents are Neha and her husband; M's children are the man and perhaps his siblings.
    cases = []
    for neha_is in ("the man's wife", "the man's sister", "the wife of the man's brother"):
        man_children = ["D"] if neha_is == "the man's wife" else []      # any other child would be another grandchild
        cases.append({"wife": neha_is == "the man's wife", "sister": neha_is == "the man's sister",
                      "his_daughter": "D" in man_children, "no_son": True})
    must = [k for k in ("wife", "sister", "his_daughter", "no_son") if all(cs[k] for cs in cases)]
    assert must == ["no_son"]
    return "The man has no son."
T(LR, "Blood Relation", "hard",
  "Pointing to a man, Neha said, 'His mother's only grandchild is my daughter.' Which one of the following must be true?",
  "एक व्यक्ति की ओर संकेत करते हुए नेहा ने कहा, 'इसकी माँ की एकमात्र पोती/नातिन मेरी बेटी है।' निम्नलिखित में से कौन-सा अवश्य सत्य है?",
  ["The man has no son.", "Neha is the man's wife.", "Neha is the man's sister.", "Neha's daughter is the man's daughter."],
  ["उस व्यक्ति का कोई बेटा नहीं है।", "नेहा उस व्यक्ति की पत्नी है।", "नेहा उस व्यक्ति की बहन है।", "नेहा की बेटी उस व्यक्ति की बेटी है।"],
  0,
  "Neha's daughter is a grandchild of the man's mother, so one of her parents is a child of that mother. That parent may be the man himself (Neha is then his wife), Neha (she is then his sister), or a brother of the man (Neha is then his sister-in-law). So none of 'wife', 'sister' or 'his daughter' must hold. "
  "But in every case the man can have no child other than Neha's daughter, since any child of his would be another grandchild of his mother. So he has no son.",
  "नेहा की बेटी उस व्यक्ति की माँ की पोती/नातिन है, इसलिए उसके माता-पिता में से एक उस माँ की संतान है। वह व्यक्ति स्वयं हो सकता है (तब नेहा उसकी पत्नी है), नेहा हो सकती है (तब वह उसकी बहन है), या उस व्यक्ति का कोई भाई (तब नेहा उसकी भाभी है)। अतः 'पत्नी', 'बहन' या 'उसकी बेटी' में से कोई अवश्य सत्य नहीं। "
  "पर हर स्थिति में उस व्यक्ति की नेहा की बेटी के अलावा कोई संतान नहीं हो सकती, क्योंकि उसकी कोई भी संतान उसकी माँ का एक और पोता या पोती होती। अतः उसका कोई बेटा नहीं है।",
  "lr-br-a-mother-s-only-grandchild", pos=3, check=_br6)

# 7 -- a code that shifts the two halves of the alphabet in opposite directions
def _cd7():
    def enc(word, fwd_first_half=True):
        out = ""
        for ch in word:
            n = ord(ch) - 65
            step = 2 if (n <= 12) == fwd_first_half else -2
            out += chr(65 + (n + step) % 26)
        return out
    assert enc("SMILE", False) == "UKGJC"
    return enc("SMILE")
T(LR, "Coding-Decoding", "medium",
  "In a code, each letter from A to M is replaced by the letter two places after it in the alphabet, and each letter from N to Z by the letter two places before it. How is SMILE written in this code?",
  "एक कूट में A से M तक का हर अक्षर वर्णमाला में अपने से दो स्थान आगे वाले अक्षर से, और N से Z तक का हर अक्षर अपने से दो स्थान पीछे वाले अक्षर से बदला जाता है। इस कूट में SMILE कैसे लिखा जाता है?",
  ["QOKNG", "UOKNG", "QKGJC", "UKGJC"], ["QOKNG", "UOKNG", "QKGJC", "UKGJC"],
  0,
  "S is in the second half, so it moves back two places to Q. M, I, L and E are all in the first half (M is its last letter), so each moves forward two: M to O, I to K, L to N, E to G. SMILE becomes QOKNG. "
  "UOKNG moves every letter forward; QKGJC moves every letter back; UKGJC applies the rule the wrong way round.",
  "S दूसरे आधे में है, इसलिए वह दो स्थान पीछे Q पर जाता है। M, I, L और E सभी पहले आधे में हैं (M उसका अंतिम अक्षर है), इसलिए हर एक दो स्थान आगे जाता है: M से O, I से K, L से N, E से G। SMILE बन जाता है QOKNG। "
  "UOKNG हर अक्षर को आगे ले जाता है; QKGJC हर अक्षर को पीछे; UKGJC नियम को उलटा लागू करता है।",
  "lr-cd-the-two-halves-of-the-alphabet-shifted-opposite-ways", pos=2, check=_cd7)

# 8 -- a walk that goes backwards
def _dd8():
    x = y = 0
    hx, hy = 1, 0                                # facing east
    x, y = x + 8 * hx, y + 8 * hy                # 8 m forward
    x, y = x - 3 * hx, y - 3 * hy                # 3 m backwards, still facing east
    hx, hy = -hy, hx                             # a left turn from east faces north
    x, y = x + 12 * hx, y + 12 * hy
    assert (x, y) == (5, 12) and x * x + y * y == 13 ** 2
    return "13 m, to the north-east"
T(LR, "Direction & Distance", "medium",
  "Facing east, Priya walks 8 m forward. Without turning round, she then walks 3 m backwards. Next she turns to her left and walks 12 m. How far is she now from where she started, and in which general direction?",
  "पूर्व की ओर मुख करके प्रिया 8 मीटर आगे चलती है। फिर बिना मुड़े वह 3 मीटर पीछे की ओर चलती है। इसके बाद वह अपनी बाईं ओर मुड़कर 12 मीटर चलती है। अब वह अपने आरंभ स्थान से कितनी दूर है, और मोटे तौर पर किस दिशा में?",
  ["13 m, to the north-east", "13 m, to the south-east", "23 m, to the north-east", "17 m, to the north-east"],
  ["13 मीटर, उत्तर-पूर्व में", "13 मीटर, दक्षिण-पूर्व में", "23 मीटर, उत्तर-पूर्व में", "17 मीटर, उत्तर-पूर्व में"],
  0,
  "Walking backwards without turning takes her 3 m west, so after two legs she is 8 - 3 = 5 m east of the start and still facing east. A left turn from east faces north, so she ends 5 m east and 12 m north of the start: √(5² + 12²) = 13 m, to the north-east. "
  "South-east comes from treating the backward walk as a turn to face west, which would make her left point south; 23 m adds up every leg walked; 17 m adds the 5 m and the 12 m.",
  "बिना मुड़े पीछे चलना उसे 3 मीटर पश्चिम ले जाता है, इसलिए दो चरणों के बाद वह आरंभ से 8 - 3 = 5 मीटर पूर्व में है और अब भी पूर्व की ओर मुख किए है। पूर्व से बाईं ओर मुड़ने पर मुख उत्तर की ओर होता है, इसलिए वह आरंभ से 5 मीटर पूर्व और 12 मीटर उत्तर में पहुँचती है: √(5² + 12²) = 13 मीटर, उत्तर-पूर्व में। "
  "दक्षिण-पूर्व पीछे चलने को पश्चिम की ओर मुड़ना मान लेने से आता है, जिससे उसकी बाईं ओर दक्षिण हो जाती; 23 मीटर चले गए हर चरण को जोड़ता है; 17 मीटर 5 और 12 मीटर को जोड़ता है।",
  "lr-dd-a-walk-that-goes-backwards", pos=0, check=_dd8)

# 9 -- a cube with its corners sliced off
def _cp9():
    V = 8 * 3                                    # each corner becomes a small triangle with three corners of its own
    F_ = 6 + 8                                   # the six old faces, plus a triangle at each corner
    E = 12 + 8 * 3                               # the twelve old edges, shortened, plus three edges round each triangle
    assert V - E + F_ == 2                       # Euler's formula for a solid without holes
    return str(E)
N(LR, "Cube Painting", "medium",
  "Each of the eight corners of a solid cube is sliced off with a small flat cut, so that every corner is replaced by a small triangular face and no two cuts meet. How many edges does the new solid have?",
  "एक ठोस घन के आठों कोनों में से हर एक को एक छोटे समतल कट से काट दिया जाता है, जिससे हर कोने की जगह एक छोटा त्रिभुजाकार फलक बन जाता है और कोई दो कट आपस में नहीं मिलते। नए ठोस के कितने किनारे (कोर) हैं?",
  ["20", "24", "30", "36"], 3,
  "The cube's 12 edges all remain, only shorter. Each cut adds a triangle, and a triangle has 3 edges of its own, so the 8 cuts add 8 × 3 = 24 edges. In all 12 + 24 = 36. "
  "As a check, the new solid has 24 corners (3 for each triangle) and 6 + 8 = 14 faces, and 24 - 36 + 14 = 2, as Euler's formula requires. 24 counts only the new edges; 20 adds the 8 cuts to the 12 old edges; 30 has no basis.",
  "घन के सभी 12 किनारे बने रहते हैं, केवल छोटे हो जाते हैं। हर कट एक त्रिभुज जोड़ता है, और त्रिभुज के अपने 3 किनारे होते हैं, इसलिए 8 कट 8 × 3 = 24 किनारे जोड़ते हैं। कुल 12 + 24 = 36। "
  "जाँच के लिए, नए ठोस के 24 शीर्ष (हर त्रिभुज के 3) और 6 + 8 = 14 फलक हैं, और 24 - 36 + 14 = 2, जैसा ऑयलर का सूत्र माँगता है। 24 केवल नए किनारे गिनता है; 20, 12 पुराने किनारों में 8 कट जोड़ता है; 30 का कोई आधार नहीं।",
  "lr-cp-a-cube-with-its-corners-sliced-off", _cp9)

# 10 -- a round table of seven chairs with one left empty
def _sa10():
    sols = []
    for perm in permutations(list("PQRSTU") + ["_"]):
        if perm[0] != "P":                       # fix P's chair: seatings that differ by a rotation are the same
            continue
        at = {x: i for i, x in enumerate(perm)}
        left = lambda x, k=1: perm[(at[x] + k) % 7]       # facing the centre, the left-hand neighbour is clockwise
        right = lambda x, k=1: perm[(at[x] - k) % 7]
        nb = lambda x, y: (at[x] - at[y]) % 7 in (1, 6)
        if left("P") == "_" and right("P", 2) == "Q" and nb("T", "_") and not nb("R", "Q") and not nb("S", "P"):
            sols.append(perm)
    assert len(sols) == 1
    at = {x: i for i, x in enumerate(sols[0])}
    nb = lambda x, y: (at[x] - at[y]) % 7 in (1, 6)
    pairs = [("R", "T"), ("P", "T"), ("S", "U"), ("Q", "R")]
    assert [nb(*p) for p in pairs] == [True, False, False, False]
    return "R and T"
T(LR, "Seating Arrangement", "hard",
  "Six people -- P, Q, R, S, T and U -- sit at a round table with seven chairs, all facing the centre, so that one chair is empty. The empty chair is to P's immediate left. Q sits second to P's right. T sits next to the empty chair. R does not sit next to Q, and S does not sit next to P. Which one of the following pairs sit next to each other?",
  "छह लोग -- P, Q, R, S, T और U -- सात कुर्सियों वाली एक गोल मेज़ पर, सभी केंद्र की ओर मुख करके, ऐसे बैठे हैं कि एक कुर्सी ख़ाली है। ख़ाली कुर्सी P के ठीक बाईं ओर है। Q, P के दाईं ओर दूसरे स्थान पर बैठा है। T ख़ाली कुर्सी के बगल में बैठा है। R, Q के बगल में नहीं बैठा, और S, P के बगल में नहीं बैठा। निम्नलिखित में से कौन-सा जोड़ा एक-दूसरे के बगल में बैठा है?",
  ["R and T", "P and T", "S and U", "Q and R"], ["R और T", "P और T", "S और U", "Q और R"],
  0,
  "Go round the table from P towards P's left: first the empty chair, then the chair beyond it. T must sit next to the empty chair, whose other neighbour is P, so T takes the chair beyond it. Going the other way from P, the chair at P's right is followed by Q's. That leaves the chair between Q and P and the two chairs between T and Q for R, S and U. "
  "R must not be next to Q, so R takes the chair next to T. S must not be next to P, so S takes the chair between R and Q, and U the chair between Q and P. "
  "So R and T are neighbours. P and T are not, as the empty chair lies between them; S and U are separated by Q; and R is kept away from Q by the clue itself.",
  "P से P के बाईं ओर मेज़ पर घूमिए: पहले ख़ाली कुर्सी, फिर उसके आगे की कुर्सी। T को ख़ाली कुर्सी के बगल में बैठना है, जिसका दूसरा पड़ोसी P है, इसलिए T उसके आगे वाली कुर्सी लेता है। P से दूसरी ओर जाने पर, P के दाईं ओर वाली कुर्सी के बाद Q की कुर्सी है। इससे Q और P के बीच की कुर्सी और T और Q के बीच की दो कुर्सियाँ R, S और U के लिए बचती हैं। "
  "R को Q के बगल में नहीं होना है, इसलिए R, T के बगल वाली कुर्सी लेता है। S को P के बगल में नहीं होना है, इसलिए S, R और Q के बीच की कुर्सी लेता है, और U, Q और P के बीच की। "
  "अतः R और T पड़ोसी हैं। P और T नहीं, क्योंकि उनके बीच ख़ाली कुर्सी है; S और U को Q अलग करता है; और R को Q से स्वयं संकेत ही दूर रखता है।",
  "lr-sa-a-round-table-of-seven-chairs-one-left-empty", pos=2, check=_sa10)

# 11 -- four classes on four weekdays
def _sa11():
    names, subs = ["Anil", "Bela", "Chetan", "Disha"], ["Music", "Painting", "Chess", "Yoga"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
    sols = []
    for dp in permutations(range(4)):
        D = dict(zip(names, dp))
        for sp in permutations(subs):
            S = dict(zip(names, sp))
            X = {S[n]: D[n] for n in names}
            if (X["Chess"] == D["Bela"] + 1 and S["Chetan"] != "Music" and D["Chetan"] != 1
                    and abs(D["Bela"] - D["Disha"]) == 2 and X["Music"] < X["Painting"] and X["Yoga"] == D["Chetan"] + 1):
                sols.append((D, S))
    assert len(sols) == 1
    D, S = sols[0]
    facts = {f"{n} takes {S[n]} on {days[D[n]]}." for n in names}
    opts = ["Bela takes Painting on Tuesday.", "Anil takes Chess on Wednesday.",
            "Disha takes Painting on Thursday.", "Chetan takes Yoga on Wednesday."]
    assert [o in facts for o in opts] == [True, False, False, False]
    return opts[0]
T(LR, "Seating Arrangement", "hard",
  "Anil, Bela, Chetan and Disha each attend one class, on a different day from Monday to Thursday, and each class is in a different subject: Music, Painting, Chess or Yoga. The Chess class is on the day after Bela's class. Chetan does not take Music, and his class is not on Tuesday. Exactly one class falls between Bela's and Disha's. The Music class comes earlier in the week than the Painting class. Chetan's class is on the day before the Yoga class. Which one of the following is correct?",
  "अनिल, बेला, चेतन और दिशा में से हर एक सोमवार से गुरुवार तक के अलग-अलग दिन एक कक्षा में जाता/जाती है, और हर कक्षा अलग विषय की है: संगीत, चित्रकला, शतरंज या योग। शतरंज की कक्षा बेला की कक्षा के अगले दिन है। चेतन संगीत नहीं लेता, और उसकी कक्षा मंगलवार को नहीं है। बेला और दिशा की कक्षाओं के बीच ठीक एक कक्षा पड़ती है। संगीत की कक्षा सप्ताह में चित्रकला की कक्षा से पहले आती है। चेतन की कक्षा योग की कक्षा से एक दिन पहले है। निम्नलिखित में से कौन-सा सही है?",
  ["Bela takes Painting on Tuesday.", "Anil takes Chess on Wednesday.",
   "Disha takes Painting on Thursday.", "Chetan takes Yoga on Wednesday."],
  ["बेला मंगलवार को चित्रकला लेती है।", "अनिल बुधवार को शतरंज लेता है।",
   "दिशा गुरुवार को चित्रकला लेती है।", "चेतन बुधवार को योग लेता है।"],
  0,
  "Chetan's class is the day before Yoga and not on Tuesday, so Chetan is on Monday or Wednesday. Bela and Disha are two days apart: Monday and Wednesday, or Tuesday and Thursday. "
  "If Chetan were on Monday, Yoga would be Tuesday and Bela and Disha would need Tuesday and Thursday -- but Chess must be the day after Bela's class, which fails for Thursday and puts Chess on Wednesday if Bela is on Tuesday, leaving Bela with Yoga, Anil with Chess and Chetan with Painting on Monday, before any Music: ruled out. "
  "So Chetan is on Wednesday and Yoga on Thursday. Wednesday is Chetan's, so Bela and Disha take Tuesday and Thursday, and Chess follows Bela, so Bela is on Tuesday, Disha on Thursday with Yoga, Chetan on Wednesday with Chess, and Anil on Monday. Music comes before Painting, so Anil takes Music and Bela Painting. "
  "Anil does not take Chess, Disha takes Yoga rather than Painting, and Chetan takes Chess rather than Yoga.",
  "चेतन की कक्षा योग से एक दिन पहले है और मंगलवार को नहीं, इसलिए चेतन सोमवार या बुधवार को है। बेला और दिशा दो दिन के अंतर पर हैं: सोमवार और बुधवार, या मंगलवार और गुरुवार। "
  "यदि चेतन सोमवार को होता, तो योग मंगलवार को होता और बेला व दिशा को मंगलवार और गुरुवार चाहिए होते -- पर शतरंज बेला की कक्षा के अगले दिन होना चाहिए, जो गुरुवार के लिए असंभव है और बेला के मंगलवार को होने पर शतरंज को बुधवार पर रखता है, जिससे बेला को योग, अनिल को शतरंज और चेतन को सोमवार को चित्रकला मिलती, किसी भी संगीत से पहले: यह ख़ारिज। "
  "अतः चेतन बुधवार को है और योग गुरुवार को। बुधवार चेतन का है, इसलिए बेला और दिशा मंगलवार और गुरुवार लेती हैं, और शतरंज बेला के बाद आता है, इसलिए बेला मंगलवार को, दिशा गुरुवार को योग के साथ, चेतन बुधवार को शतरंज के साथ, और अनिल सोमवार को है। संगीत चित्रकला से पहले आता है, इसलिए अनिल संगीत लेता है और बेला चित्रकला। "
  "अनिल शतरंज नहीं लेता, दिशा चित्रकला के बजाय योग लेती है, और चेतन योग के बजाय शतरंज लेता है।",
  "lr-sa-four-classes-on-four-weekdays", pos=1, check=_sa11)

# 12 -- a speaker who alternates truth and lies
def _tl12():
    st = [lambda a: a > 30, lambda a: a == 28, lambda a: a % 2 == 0]
    ages = [a for a in range(1, 121)
            if any(all(st[i](a) == ((i % 2 == 0) == first) for i in range(3)) for first in (True, False))]
    assert ages and all(a > 30 and a % 2 == 0 for a in ages) and 32 in ages
    return "His age is an even number above 30."
T(LR, "Truth-Liar", "hard",
  "Ravi alternates between the truth and lies: whenever one of his statements is true, the next is false, and whenever one is false, the next is true. He makes three statements in a row: 'I am older than 30.' 'I am 28 years old.' 'My age is an even number.' What can be concluded about his age?",
  "रवि बारी-बारी से सच और झूठ बोलता है: जब भी उसका कोई कथन सत्य होता है, अगला असत्य होता है, और जब कोई असत्य होता है, अगला सत्य होता है। वह लगातार तीन कथन कहता है: 'मैं 30 से बड़ा हूँ।' 'मेरी आयु 28 वर्ष है।' 'मेरी आयु एक सम संख्या है।' उसकी आयु के बारे में क्या निष्कर्ष निकाला जा सकता है?",
  ["His age is an even number above 30.", "He is exactly 28 years old.",
   "His age is an odd number of 30 or less.", "Nothing can be concluded about his age."],
  ["उसकी आयु 30 से ऊपर की एक सम संख्या है।", "उसकी आयु ठीक 28 वर्ष है।",
   "उसकी आयु 30 या उससे कम की एक विषम संख्या है।", "उसकी आयु के बारे में कोई निष्कर्ष नहीं निकाला जा सकता।"],
  0,
  "The first and third statements are both true or both false, and the second is the opposite. If the second were true, he would be 28 -- but then the third, 'my age is even', would have to be false, and 28 is even. That is impossible. "
  "So the second is false and the first and third are true: he is older than 30 and his age is even (32, 34 and so on). He is not 28; an odd age of 30 or less would make the first and third false together with the second; and a conclusion can be drawn.",
  "पहला और तीसरा कथन दोनों सत्य हैं या दोनों असत्य, और दूसरा उनका उलटा। यदि दूसरा सत्य होता, तो वह 28 का होता -- पर तब तीसरा, 'मेरी आयु सम है', असत्य होना चाहिए, और 28 सम है। यह असंभव है। "
  "अतः दूसरा असत्य है और पहला व तीसरा सत्य: वह 30 से बड़ा है और उसकी आयु सम है (32, 34 आदि)। वह 28 का नहीं; 30 या कम की विषम आयु पहले और तीसरे को दूसरे के साथ ही असत्य कर देती; और निष्कर्ष निकाला जा सकता है।",
  "lr-tl-a-speaker-who-alternates-truth-and-lies", pos=3, check=_tl12)

# ---- the data-sufficiency block's three Reasoning items
def _ds13():
    faces = [1, 2, 3, 4, 5, 6]
    def pairings(xs):                            # every way to split the six faces into three opposite pairs
        if not xs:
            yield []
            return
        a = xs[0]
        for b in xs[1:]:
            rest = [x for x in xs if x not in (a, b)]
            for p in pairings(rest):
                yield [(a, b)] + p
    dice = list(pairings(faces))
    opp = lambda die, x: next(b if a == x else a for a, b in die if x in (a, b))
    std = [d for d in dice if all(a + b == 7 for a, b in d)]
    s1 = {opp(d, 3) for d in dice}                       # top shows 3, any die
    s2 = {opp(d, t) for d in std for t in faces}         # a standard die, top unknown
    both = {opp(d, 3) for d in std}
    assert both == {4}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "A die lies on a table. What number is on its bottom face?",
   "एक पासा मेज़ पर रखा है। उसके नीचे वाले फलक पर कौन-सी संख्या है?",
   "The top face shows 3.", "ऊपर वाला फलक 3 दिखाता है।",
   "The numbers on opposite faces of the die add up to 7.", "पासे के आमने-सामने के फलकों की संख्याओं का योग 7 है।",
   2,
   "Statement I alone gives the top but not which number is opposite it, since dice can be numbered in different ways. Statement II alone gives the rule for opposite faces but not the top. Together, the bottom is opposite 3, so it shows 7 - 3 = 4. Both statements are needed.",
   "कथन I अकेले ऊपर का फलक बताता है पर यह नहीं कि उसके सामने कौन-सी संख्या है, क्योंकि पासों पर संख्याएँ अलग-अलग ढंग से लिखी जा सकती हैं। कथन II अकेले आमने-सामने के फलकों का नियम बताता है पर ऊपर का फलक नहीं। दोनों मिलकर: नीचे वाला फलक 3 के सामने है, इसलिए वह 7 - 3 = 4 दिखाता है। दोनों कथन आवश्यक हैं।",
   "lr-ds-the-bottom-face-of-a-die", _ds13)

def _ds14():
    def ok_I(a, b):                              # A says 'B is a liar'
        return a == (not b)
    def ok_II(a, b):                             # B says 'A and I are not of the same kind'
        return b == (a != b)
    s1 = {a for a, b in product((True, False), repeat=2) if ok_I(a, b)}
    s2 = {a for a, b in product((True, False), repeat=2) if ok_II(a, b)}
    both = {a for a, b in product((True, False), repeat=2) if ok_I(a, b) and ok_II(a, b)}
    assert s2 == {False} and s1 == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "On an island every person either always tells the truth or always lies. Is A a truth-teller?",
   "एक द्वीप पर हर व्यक्ति या तो हमेशा सच बोलता है या हमेशा झूठ। क्या A सच बोलने वाला है?",
   "A says, 'B is a liar.'", "A कहता है, 'B झूठा है।'",
   "B says, 'A and I are not of the same kind.'", "B कहता है, 'A और मैं एक ही प्रकार के नहीं हैं।'",
   0,
   "Statement II alone settles it. If B tells the truth, A and B differ, so A is a liar. If B lies, the statement is false, so A and B are alike -- and A is a liar again. Either way A is a liar. "
   "Statement I alone does not: A truthful with B a liar, and A a liar with B truthful, both fit. So the question can be answered from one statement alone but not from the other.",
   "कथन II अकेले इसे तय कर देता है। यदि B सच बोलता है, तो A और B अलग हैं, इसलिए A झूठा है। यदि B झूठ बोलता है, तो कथन असत्य है, इसलिए A और B एक जैसे हैं -- और A फिर झूठा है। दोनों ही तरह A झूठा है। "
   "कथन I अकेले नहीं: A सच्चा और B झूठा, तथा A झूठा और B सच्चा, दोनों ठीक बैठते हैं। अतः प्रश्न का उत्तर एक कथन से अकेले दिया जा सकता है पर दूसरे से नहीं।",
   "lr-ds-an-islander-who-gives-another-away", _ds14)

def _ds15():
    s1 = {7 + 9 - 1}
    s2 = {8 + 8 - 1}
    return _ds(s1, s2, s1 & s2)
DS(LR, "medium",
   "How many children are standing in a row?",
   "एक पंक्ति में कितने बच्चे खड़े हैं?",
   "Ravi is 7th from the left end of the row and 9th from the right end.", "रवि पंक्ति के बाएँ छोर से 7वाँ और दाएँ छोर से 9वाँ है।",
   "Sita is 8th from the left end of the row and 8th from the right end.", "सीता पंक्ति के बाएँ छोर से 8वीं और दाएँ छोर से 8वीं है।",
   1,
   "A child who is m-th from one end and n-th from the other has m - 1 children on one side and n - 1 on the other, so the row has m + n - 1. Statement I gives 7 + 9 - 1 = 15; Statement II gives 8 + 8 - 1 = 15. Either statement alone answers the question.",
   "जो बच्चा एक छोर से m-वाँ और दूसरे से n-वाँ है, उसके एक ओर m - 1 और दूसरी ओर n - 1 बच्चे हैं, इसलिए पंक्ति में m + n - 1 बच्चे हैं। कथन I से 7 + 9 - 1 = 15; कथन II से 8 + 8 - 1 = 15। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "lr-ds-a-row-counted-two-ways", _ds15)
