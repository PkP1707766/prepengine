# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 5 -- Logical Reasoning (17 items: 14 in the Reasoning slots, 3 in the data-sufficiency block).

Layout B, the 2025 shape. Exam-level mix (1 easy / 8 medium / 8 hard), with none of the shapes of Levels 1-3 or
Simulators 1-4: a date defended by its age, a cricketer's word on cement, the assumptions behind a rule on price
labels, what to do after a midday meal makes children ill, what would show that green tea protects the heart, what a
household survey guarantees; bottles that are green; a husband's brother's wife; a code that sends each letter to
twice its place; the two houses farthest apart; a cube with only its edges painted; a hexagonal table with
opposite seats, six friends in six coaches; one truth-teller among three friends; and in the data-sufficiency block the
runner who came second, a light that goes on with the fan, and the colour opposite red. Arrangement, relation,
code, cube and truth-teller keys are found by checking every case."""
from itertools import combinations, permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- a date defended by its age
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'The village fair has been held in the first week of March for more than a hundred years, so the first week of March must be the best time to hold it.' Which one of the following best describes the flaw in this reasoning?",
  "'गाँव का मेला सौ से अधिक वर्षों से मार्च के पहले सप्ताह में लगता आया है, इसलिए मार्च का पहला सप्ताह ही उसे लगाने का सबसे अच्छा समय होगा।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It treats the age of a custom as if that alone proved the custom to be the best choice.",
   "It assumes that the people who come to the fair would never accept any change of date.",
   "It judges the fair by the opinions of a few visitors rather than those of everyone.",
   "It confuses the cause of the fair's popularity with one of the effects of that popularity."],
  ["यह किसी प्रथा के पुरानेपन को ही उसके सबसे अच्छा होने का प्रमाण मान लेता है।",
   "यह मान लेता है कि मेले में आने वाले लोग तारीख़ का कोई भी बदलाव कभी स्वीकार नहीं करेंगे।",
   "यह मेले को सबकी नहीं, कुछ आगंतुकों की राय के आधार पर आँकता है।",
   "यह मेले की लोकप्रियता के कारण को उस लोकप्रियता के किसी प्रभाव से भ्रमित कर देता है।"],
  0,
  "That something has long been done shows only that it has been done. The date may once have suited conditions -- a harvest, the roads, the weather of an earlier time -- that no longer hold, and a better date may never have been tried. Age alone is not evidence of being best. "
  "The argument says nothing about whether visitors would accept a change; it cites no visitors' opinions at all; and it makes no claim about what causes the fair's popularity.",
  "किसी काम का लंबे समय से होते आना केवल यह दिखाता है कि वह होता आया है। हो सकता है वह तारीख़ कभी ऐसी परिस्थितियों -- फ़सल, सड़कों, पहले के समय के मौसम -- के अनुकूल रही हो जो अब नहीं हैं, और कोई बेहतर तारीख़ कभी आज़माई ही न गई हो। केवल पुरानापन सबसे अच्छा होने का प्रमाण नहीं है। "
  "तर्क इस बारे में कुछ नहीं कहता कि आगंतुक बदलाव स्वीकार करेंगे या नहीं; वह आगंतुकों की कोई राय उद्धृत नहीं करता; और वह मेले की लोकप्रियता के कारण के बारे में कोई दावा नहीं करता।",
  "lr-sc-a-date-defended-by-its-age", pos=0)

# 2 -- a cricketer's word on cement
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A famous cricketer appears in an advertisement saying that a certain brand of cement is the strongest in the country. A viewer says, 'He is one of the greatest players of our time, so this must be the best cement.' Which one of the following best describes the flaw in the viewer's reasoning?",
  "एक प्रसिद्ध क्रिकेटर एक विज्ञापन में कहता है कि सीमेंट का एक ब्रांड देश में सबसे मज़बूत है। एक दर्शक कहता है, 'वह हमारे समय के सबसे महान खिलाड़ियों में से एक है, इसलिए यही सबसे अच्छा सीमेंट होगा।' निम्नलिखित में से कौन-सा दर्शक के तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It treats excellence in one field as if it gave expert knowledge in an unrelated one.",
   "It rejects the claim only because the person making it is being paid to advertise the cement.",
   "It concludes that all brands of cement are equally strong because none of them has been tested.",
   "It assumes that a cement used by many builders must be stronger than any other cement."],
  ["यह एक क्षेत्र की उत्कृष्टता को किसी असंबंधित क्षेत्र के विशेषज्ञ ज्ञान जैसा मान लेता है।",
   "यह दावे को केवल इसलिए ठुकरा देता है कि दावा करने वाले को सीमेंट के विज्ञापन के पैसे मिल रहे हैं।",
   "यह इस आधार पर कि किसी की जाँच नहीं हुई, निष्कर्ष निकालता है कि सीमेंट के सभी ब्रांड बराबर मज़बूत हैं।",
   "यह मान लेता है कि कई निर्माताओं द्वारा उपयोग किया जाने वाला सीमेंट किसी भी अन्य सीमेंट से मज़बूत होगा।"],
  0,
  "Being a great cricketer gives no special knowledge of how strong cement is. The viewer accepts the claim because of who made it, though the speaker's authority lies in a field that has nothing to do with the claim; what would count is evidence from tests of the cement. "
  "The viewer accepts the claim rather than rejecting it; draws no conclusion that all brands are equal; and says nothing about how many builders use the cement.",
  "महान क्रिकेटर होना सीमेंट की मज़बूती का कोई विशेष ज्ञान नहीं देता। दर्शक दावे को इसलिए स्वीकार करता है कि उसे किसने किया, जबकि वक्ता का अधिकार ऐसे क्षेत्र में है जिसका दावे से कोई संबंध नहीं; जो मायने रखता वह सीमेंट की जाँच से मिला प्रमाण होता। "
  "दर्शक दावे को ठुकराता नहीं, स्वीकार करता है; वह यह निष्कर्ष नहीं निकालता कि सभी ब्रांड बराबर हैं; और यह नहीं कहता कि कितने निर्माता उस सीमेंट का उपयोग करते हैं।",
  "lr-sc-a-cricketer-s-word-on-cement", pos=3)

# 3 -- the assumptions behind a rule on price labels
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: A city corporation orders that, from 1 June, every shop selling food in the city must display its prices clearly in both Hindi and English.\n\nWhich of the following assumptions is/are implicit in the statement?",
   "कथन: एक नगर निगम आदेश देता है कि 1 जून से शहर में खाद्य पदार्थ बेचने वाली हर दुकान को अपने मूल्य हिंदी और अंग्रेज़ी दोनों में स्पष्ट रूप से प्रदर्शित करने होंगे।\n\nनिम्नलिखित में से कौन-सी पूर्वधारणा/एँ कथन में निहित है/हैं?",
   ["Customers find it useful to be able to read the prices before they buy.",
    "Every customer in the city can read both Hindi and English."],
   ["ग्राहकों के लिए ख़रीदने से पहले मूल्य पढ़ पाना उपयोगी है।",
    "शहर का हर ग्राहक हिंदी और अंग्रेज़ी दोनों पढ़ सकता है।"],
   0,
   "Only I is implicit. An order to display prices clearly makes sense only if being able to read them before buying is of use to customers. "
   "II is not assumed; the order points the other way. Requiring both languages makes sense precisely because some customers read one language but not the other; if everyone read both, one would do.",
   "केवल I निहित है। मूल्य स्पष्ट रूप से प्रदर्शित करने का आदेश तभी समझ में आता है जब ख़रीदने से पहले उन्हें पढ़ पाना ग्राहकों के लिए उपयोगी हो। "
   "II पूर्वधारणा नहीं है; आदेश उलटी ओर संकेत करता है। दोनों भाषाओं की अनिवार्यता इसीलिए समझ में आती है कि कुछ ग्राहक एक भाषा पढ़ते हैं पर दूसरी नहीं; यदि सब दोनों पढ़ते, तो एक ही पर्याप्त होती।",
   "lr-sc-the-assumptions-behind-a-rule-on-price-labels", roman=True)

# 4 -- what to do after a midday meal makes children ill
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: Several children at a government school fell ill after eating the midday meal served there.\n\nWhich of the following courses of action follow(s) for pursuing?",
   "कथन: एक सरकारी विद्यालय में वहाँ परोसा गया मध्याह्न भोजन खाने के बाद कई बच्चे बीमार पड़ गए।\n\nनिम्नलिखित में से कौन-सी कार्यवाही/याँ अपनाने योग्य है/हैं?",
   ["Samples of the food should be tested, and the school's kitchen and the supplier inspected.",
    "The midday meal scheme should be stopped in every school of the State."],
   ["भोजन के नमूनों की जाँच हो, और विद्यालय की रसोई तथा आपूर्तिकर्ता का निरीक्षण किया जाए।",
    "राज्य के हर विद्यालय में मध्याह्न भोजन योजना बंद कर दी जाए।"],
   0,
   "Only I follows. Testing the food and inspecting the kitchen and supplier deals directly with the problem: it finds the cause and lets it be put right. "
   "II does not follow. One school's bad meal is no reason to deprive children in every school of a meal many of them depend on; a course of action should be in proportion to the problem.",
   "केवल I अपनाने योग्य है। भोजन की जाँच और रसोई तथा आपूर्तिकर्ता का निरीक्षण समस्या से सीधे निपटता है: वह कारण खोजता है और उसे ठीक करने देता है। "
   "II नहीं। एक विद्यालय का ख़राब भोजन हर विद्यालय के बच्चों को उस भोजन से वंचित करने का कारण नहीं, जिस पर उनमें से कई निर्भर हैं; कार्यवाही समस्या के अनुपात में होनी चाहिए।",
   "lr-sc-after-a-midday-meal-makes-children-ill", roman=True)

# 5 -- what would show that green tea protects the heart
T(LR, "Statement-Conclusion/Assumption", "hard",
  "In a survey of 10,000 adults, those who drank green tea every day had fewer heart attacks over ten years than those who did not. A tea company concludes that drinking green tea protects the heart. Which one of the following, if true, would most strengthen the company's conclusion?",
  "10,000 वयस्कों के एक सर्वेक्षण में, जो लोग प्रतिदिन ग्रीन टी पीते थे उन्हें दस वर्षों में न पीने वालों की तुलना में कम दिल के दौरे पड़े। एक चाय कंपनी निष्कर्ष निकालती है कि ग्रीन टी पीना दिल की रक्षा करता है। निम्नलिखित में से कौन-सा, यदि सत्य हो, कंपनी के निष्कर्ष को सबसे अधिक मज़बूत करेगा?",
  ["Among people alike in diet, exercise and smoking, the daily tea drinkers still had fewer heart attacks.",
   "The daily green tea drinkers in the survey were, on average, younger and more active than the people who did not drink it.",
   "The survey was paid for by a group of companies that sell green tea in many countries, including the company in question.",
   "Green tea is drunk far more often in some regions of the country than in others, as the survey itself went on to find."],
  ["आहार, व्यायाम और धूम्रपान में समान लोगों में भी प्रतिदिन चाय पीने वालों को कम दिल के दौरे पड़े।",
   "सर्वेक्षण में प्रतिदिन ग्रीन टी पीने वाले, औसतन, उसे न पीने वालों से कम आयु के और अधिक सक्रिय थे।",
   "सर्वेक्षण का ख़र्च ऐसी कंपनियों के एक समूह ने उठाया जो इस कंपनी सहित कई देशों में ग्रीन टी बेचती हैं।",
   "जैसा सर्वेक्षण ने आगे पाया, देश के कुछ क्षेत्रों में ग्रीन टी दूसरों की तुलना में कहीं अधिक पी जाती है।"],
  0,
  "The survey shows only that tea drinkers had fewer heart attacks. The worry is that they differed in other ways that protect the heart. If the difference remains among people who are alike in diet, exercise and smoking, those other explanations are ruled out and the tea itself becomes the likelier cause. "
  "Younger, more active tea drinkers would offer exactly such another explanation, weakening the conclusion; who paid for the survey bears on trust in it, not on whether tea protects the heart; and where tea is drunk is beside the point.",
  "सर्वेक्षण केवल यह दिखाता है कि चाय पीने वालों को कम दिल के दौरे पड़े। चिंता यह है कि वे अन्य ऐसे तरीक़ों से अलग थे जो दिल की रक्षा करते हैं। यदि आहार, व्यायाम और धूम्रपान में समान लोगों में भी अंतर बना रहे, तो वे अन्य व्याख्याएँ ख़ारिज हो जाती हैं और स्वयं चाय अधिक संभावित कारण बनती है। "
  "कम आयु के, अधिक सक्रिय चाय पीने वाले ठीक ऐसी ही एक अन्य व्याख्या देते, जो निष्कर्ष को कमज़ोर करती; सर्वेक्षण का ख़र्च किसने उठाया यह उस पर भरोसे से जुड़ा है, इससे नहीं कि चाय दिल की रक्षा करती है या नहीं; और चाय कहाँ पी जाती है, यह अप्रासंगिक है।",
  "lr-sc-what-would-show-that-green-tea-protects-the-heart", pos=1)

# 6 -- what a household survey guarantees
def _sc6():
    types = list(product((True, False), repeat=3))                    # (car, bicycle, television)
    worlds = []
    for k in range(1, 9):
        for present in combinations(types, k):
            if all((not car or bike) for car, bike, tv in present) \
               and any(bike and not tv for car, bike, tv in present) \
               and all(tv or not car for car, bike, tv in present):
                worlds.append(present)
    opts = {"Some households that own a bicycle do not own a car.":
                lambda w: any(b and not c_ for c_, b, t in w),
            "Every household that owns a bicycle also owns a car.":
                lambda w: all(c_ for c_, b, t in w if b),
            "Some households that own a car do not own a television.":
                lambda w: any(c_ and not t for c_, b, t in w),
            "Every household that owns a television also owns a car.":
                lambda w: all(c_ for c_, b, t in w if t)}
    must = [o for o, f in opts.items() if all(f(w) for w in worlds)]
    assert must == ["Some households that own a bicycle do not own a car."]
    return must[0]
T(LR, "Statement-Conclusion/Assumption", "hard",
  "A survey of a town found that every household that owns a car also owns a bicycle; that some households that own a bicycle do not own a television; and that no household without a television owns a car. Which one of the following must be true?",
  "एक नगर के सर्वेक्षण में पाया गया कि कार रखने वाला हर परिवार साइकिल भी रखता है; कि साइकिल रखने वाले कुछ परिवार टेलीविज़न नहीं रखते; और कि टेलीविज़न न रखने वाला कोई भी परिवार कार नहीं रखता। निम्नलिखित में से कौन-सा अवश्य सत्य है?",
  ["Some households that own a bicycle do not own a car.",
   "Every household that owns a bicycle also owns a car.",
   "Some households that own a car do not own a television.",
   "Every household that owns a television also owns a car."],
  ["साइकिल रखने वाले कुछ परिवार कार नहीं रखते।",
   "साइकिल रखने वाला हर परिवार कार भी रखता है।",
   "कार रखने वाले कुछ परिवार टेलीविज़न नहीं रखते।",
   "टेलीविज़न रखने वाला हर परिवार कार भी रखता है।"],
  0,
  "Take the households that own a bicycle but no television; the survey says there are some. No household without a television owns a car, so none of these owns a car. So some households that own a bicycle do not own a car. "
  "That same fact rules out 'every household with a bicycle owns a car'; 'some car owners have no television' contradicts the third finding, which means every car owner has a television; and the third finding does not run backwards -- a television does not bring a car with it.",
  "उन परिवारों को लीजिए जिनके पास साइकिल है पर टेलीविज़न नहीं; सर्वेक्षण कहता है कि ऐसे कुछ हैं। टेलीविज़न न रखने वाला कोई परिवार कार नहीं रखता, इसलिए इनमें से किसी के पास कार नहीं। अतः साइकिल रखने वाले कुछ परिवार कार नहीं रखते। "
  "यही तथ्य 'साइकिल रखने वाला हर परिवार कार रखता है' को ख़ारिज करता है; 'कुछ कार वालों के पास टेलीविज़न नहीं' तीसरी खोज का खंडन करता है, जिसका अर्थ है कि हर कार वाले के पास टेलीविज़न है; और तीसरी खोज उलटी नहीं चलती -- टेलीविज़न अपने साथ कार नहीं लाता।",
  "lr-sc-what-a-household-survey-guarantees", pos=1, check=_sc6)

# 7 -- bottles that are green
def _sy7():
    # Every way the classes 'bottles' (B), 'green things' (G) and 'recyclable things' (R) can overlap: each of the
    # seven regions of a three-set diagram is empty or not; the statements keep those with some B in G, and G inside R.
    regions = [r for r in product((0, 1), repeat=3) if any(r)]     # (in B, in G, in R)
    one = two = True
    for present in product((0, 1), repeat=len(regions)):
        filled = {r for r, p in zip(regions, present) if p}
        if not any(b and g for b, g, rr in filled):                  # some bottles are green
            continue
        if any(g and not rr for b, g, rr in filled):                 # all green things are recyclable
            continue
        one &= any(b and rr for b, g, rr in filled)
        two &= any(rr and b for b, g, rr in filled)
    return c.T2R[{(True, True): 2, (True, False): 0, (False, True): 1, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "easy",
   "Statements: Some bottles are green. All green things are recyclable.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ बोतलें हरी हैं। सभी हरी वस्तुएँ पुनर्चक्रण योग्य हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some bottles are recyclable.", "Some recyclable things are bottles."],
   ["कुछ बोतलें पुनर्चक्रण योग्य हैं।", "कुछ पुनर्चक्रण योग्य वस्तुएँ बोतलें हैं।"],
   2,
   "Both follow. The green bottles are green things, and all green things are recyclable, so those bottles are recyclable (I). And if some bottles are recyclable, then some recyclable things are bottles -- the same fact read the other way round (II).",
   "दोनों निकलते हैं। हरी बोतलें हरी वस्तुएँ हैं, और सभी हरी वस्तुएँ पुनर्चक्रण योग्य हैं, इसलिए वे बोतलें पुनर्चक्रण योग्य हैं (I)। और यदि कुछ बोतलें पुनर्चक्रण योग्य हैं, तो कुछ पुनर्चक्रण योग्य वस्तुएँ बोतलें हैं -- वही तथ्य उलटी ओर से पढ़ा गया (II)।",
   "lr-sy-bottles-that-are-green", roman=True, check=_sy7)

# 8 -- a husband's brother's wife
def _br8():
    father = {"son": "Asha's husband"}
    brother = {"Asha's husband": "his brother"}
    wife = {"his brother": "Rina"}
    rina = wife[brother[father["son"]]]
    assert rina == "Rina"
    return "She is the wife of his father's brother."
T(LR, "Blood Relation", "medium",
  "Rina is the wife of the brother of Asha's husband. How is Rina related to Asha's son?",
  "रीना, आशा के पति के भाई की पत्नी है। रीना, आशा के बेटे की क्या लगती है?",
  ["She is the wife of his mother's brother.", "She is his mother's sister.",
   "She is his father's sister.", "She is the wife of his father's brother."],
  ["वह उसकी माँ के भाई की पत्नी, यानी उसकी मामी, है।", "वह उसकी माँ की बहन (मौसी) है।",
   "वह उसके पिता की बहन (बुआ) है।", "वह उसके पिता के भाई की पत्नी (चाची या ताई) है।"],
  3,
  "Asha's husband is the son's father, so the brother of Asha's husband is the son's father's brother, and Rina, his wife, is the wife of the son's father's brother -- his chachi or tai. "
  "The mother's brother and the mother's sister are on Asha's side of the family, not her husband's; and Rina married into the father's family rather than being born in it, so she is not his father's sister.",
  "आशा का पति उस बेटे का पिता है, इसलिए आशा के पति का भाई बेटे के पिता का भाई है, और रीना, उसकी पत्नी, बेटे के पिता के भाई की पत्नी है -- उसकी चाची या ताई। "
  "मामा और मौसी आशा के परिवार की ओर हैं, उसके पति के नहीं; और रीना पिता के परिवार में ब्याह कर आई है, उसमें जन्मी नहीं, इसलिए वह बुआ नहीं है।",
  "lr-br-a-husband-s-brother-s-wife", check=_br8)

# 9 -- a code that sends each letter to twice its place
def _cd9():
    enc = lambda w: "".join(chr(64 + ((2 * (ord(ch) - 64) - 1) % 26) + 1) for ch in w)
    assert enc("M") == "Z" and enc("N") == "B"
    return enc("CAKE")
T(LR, "Coding-Decoding", "medium",
  "In a code, the letter in position n of the alphabet (A = 1, B = 2, ..., Z = 26) is replaced by the letter in position 2n, counting on from A again after Z -- so M (13) becomes Z (26), and N (14) becomes B (28 - 26 = 2). How is CAKE written in this code?",
  "एक कूट में वर्णमाला के n-वें स्थान का अक्षर (A = 1, B = 2, ..., Z = 26) 2n-वें स्थान के अक्षर से बदला जाता है, Z के बाद फिर A से गिनते हुए -- इसलिए M (13), Z (26) बन जाता है, और N (14), B (28 - 26 = 2)। इस कूट में CAKE कैसे लिखा जाता है?",
  ["FBVJ", "DBLF", "FBUJ", "ECMG"], ["FBVJ", "DBLF", "FBUJ", "ECMG"],
  0,
  "C is 3rd, so it becomes the 6th letter, F; A (1) becomes B (2); K (11) becomes V (22); and E (5) becomes J (10). CAKE is written FBVJ. "
  "DBLF moves each letter on by one place; ECMG moves each on by two; FBUJ slips on K, sending it to the 21st letter instead of the 22nd.",
  "C तीसरा है, इसलिए वह छठा अक्षर F बनता है; A (1), B (2) बनता है; K (11), V (22) बनता है; और E (5), J (10) बनता है। CAKE, FBVJ लिखा जाता है। "
  "DBLF हर अक्षर को एक स्थान आगे ले जाता है; ECMG दो स्थान; FBUJ, K पर चूकता है, उसे 22वें के बजाय 21वें अक्षर पर भेजता है।",
  "lr-cd-a-code-that-sends-each-letter-to-twice-its-place", pos=0, check=_cd9)

# 10 -- the two houses farthest apart
def _dd10():
    pos = {"Q": (0, 0)}
    pos["P"] = (-2, 0)                           # 2 km due west of Q
    pos["R"] = (0, 2)                            # 2 km due north of Q
    pos["S"] = (2, 2)                            # 2 km due east of R
    d = {frozenset(p): (pos[p[0]][0] - pos[p[1]][0]) ** 2 + (pos[p[0]][1] - pos[p[1]][1]) ** 2 for p in combinations("PQRS", 2)}
    far = max(d, key=d.get)
    assert far == frozenset("PS") and sorted(d.values()).count(max(d.values())) == 1
    return "P and S"
T(LR, "Direction & Distance", "medium",
  "P's house is 2 km due west of Q's house. R's house is 2 km due north of Q's house, and S's house is 2 km due east of R's house. Which two of the four houses are farthest apart?",
  "P का घर, Q के घर से 2 किमी ठीक पश्चिम में है। R का घर, Q के घर से 2 किमी ठीक उत्तर में है, और S का घर, R के घर से 2 किमी ठीक पूर्व में है। चारों में से कौन-से दो घर एक-दूसरे से सबसे दूर हैं?",
  ["P and R", "P and S", "Q and S", "Q and R"], ["P और R", "P और S", "Q और S", "Q और R"],
  1,
  "Put Q at the centre. P is 2 km west, R is 2 km north and S is 2 km north and 2 km east of Q. P and S are then 4 km apart east to west and 2 km north to south: √(4² + 2²) = √20, about 4.5 km. "
  "P and R and Q and S are each √(2² + 2²) = √8, about 2.8 km apart; Q and R are just 2 km apart.",
  "Q को केंद्र में रखिए। P, 2 किमी पश्चिम में है, R, 2 किमी उत्तर में और S, Q से 2 किमी उत्तर और 2 किमी पूर्व में। तब P और S पूर्व-पश्चिम में 4 किमी और उत्तर-दक्षिण में 2 किमी दूर हैं: √(4² + 2²) = √20, लगभग 4.5 किमी। "
  "P और R तथा Q और S, हर जोड़ा √(2² + 2²) = √8, लगभग 2.8 किमी दूर है; Q और R केवल 2 किमी दूर हैं।",
  "lr-dd-the-two-houses-farthest-apart", pos=1, check=_dd10)

# 11 -- a cube with only its edges painted
def _cp11():
    cells = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
    on_edge = lambda p: sum(v in (0, 2) for v in p) >= 2         # two coordinates at the outside: on an edge line
    painted = [p for p in cells if on_edge(p)]
    assert sum(1 for p in cells if sum(v in (0, 2) for v in p) == 3) == 8 and len(painted) == 20
    return str(len(painted))
N(LR, "Cube Painting", "hard",
  "Only the twelve edges of a wooden cube are painted, as thin lines; the rest of its faces are left bare. The cube is then cut into 27 equal smaller cubes. How many of the small cubes have some paint on them?",
  "लकड़ी के एक घन के केवल बारह किनारे पतली रेखाओं के रूप में रँगे जाते हैं; उसके फलकों का बाक़ी भाग बिना रंग के छोड़ा जाता है। फिर घन को 27 बराबर छोटे घनों में काटा जाता है। कितने छोटे घनों पर कुछ रंग है?",
  ["8", "20", "24", "26"], 1,
  "A small cube gets paint only if it lies along an edge of the big cube. That means the 8 corner cubes, each on three edges, and the 12 cubes in the middle of the edges, one to each edge. The 6 cubes at the centres of the faces touch no edge, since the painted lines run round the borders of each face, and the cube at the very centre is hidden. So 8 + 12 = 20. "
  "26 counts every cube on the surface, as if the faces had been painted; 8 counts only the corners; 24 has no basis.",
  "किसी छोटे घन पर रंग तभी आता है जब वह बड़े घन के किसी किनारे के साथ हो। यानी 8 कोने वाले घन, हर एक तीन किनारों पर, और किनारों के बीच के 12 घन, हर किनारे पर एक। फलकों के केंद्र वाले 6 घन किसी किनारे को नहीं छूते, क्योंकि रँगी रेखाएँ हर फलक की सीमा के चारों ओर चलती हैं, और ठीक केंद्र वाला घन छिपा है। अतः 8 + 12 = 20। "
  "26 सतह के हर घन को गिनता है, मानो फलक रँगे गए हों; 8 केवल कोनों को गिनता है; 24 का कोई आधार नहीं।",
  "lr-cp-a-cube-with-only-its-edges-painted", _cp11)

# 12 -- a hexagonal table with opposite seats
def _sa12():
    sols = []
    for perm in permutations("ABCDEF"):
        if perm[0] != "A":
            continue
        at = {x: i for i, x in enumerate(perm)}
        left = lambda x: perm[(at[x] + 1) % 6]                # facing the centre, the left-hand neighbour is clockwise
        right = lambda x: perm[(at[x] - 1) % 6]
        opp = lambda x: perm[(at[x] + 3) % 6]
        nb = lambda x, y: (at[x] - at[y]) % 6 in (1, 5)
        if opp("A") == "D" and left("A") == "B" and not nb("E", "A") and opp("F") == "E":
            sols.append((perm, left, right, opp, nb))
    assert len(sols) == 1
    perm, left, right, opp, nb = sols[0]
    facts = [left("D") == "C", right("B") == "E", opp("C") == "F", nb("C", "A")]
    assert facts == [True, False, False, False]
    return "C sits to D's immediate left."
T(LR, "Seating Arrangement", "hard",
  "Six people -- A, B, C, D, E and F -- sit at a hexagonal table, one on each side, all facing the centre, so that each person sits directly opposite one other. A sits opposite D. B sits to A's immediate left. E does not sit next to A, and F sits opposite E. Which one of the following is correct?",
  "छह लोग -- A, B, C, D, E और F -- एक षट्भुजाकार मेज़ पर, हर भुजा पर एक, सभी केंद्र की ओर मुख करके बैठे हैं, ऐसे कि हर व्यक्ति किसी एक के ठीक सामने बैठा है। A, D के सामने बैठा है। B, A के ठीक बाईं ओर बैठा है। E, A के बगल में नहीं बैठा, और F, E के सामने बैठा है। निम्नलिखित में से कौन-सा सही है?",
  ["C sits to D's immediate left.", "E sits to B's immediate right.", "F sits opposite C.", "C sits next to A."],
  ["C, D के ठीक बाईं ओर बैठा है।", "E, B के ठीक दाईं ओर बैठा है।", "F, C के सामने बैठा है।", "C, A के बगल में बैठा है।"],
  0,
  "Go round the table from A towards A's left: A, then B, then one seat, then D (opposite A), then one more seat, then the seat at A's right. E is not next to A, so E takes one of the two seats beside D. The seat opposite the one between D and A's right is B's, so E there would leave no seat opposite E for F. Hence E sits between B and D, F sits opposite E at A's right, and C takes the seat between D and F. "
  "Facing the centre, C is then at D's immediate left. B's immediate right is A, not E; F sits opposite E, not C; and A's neighbours are B and F, not C.",
  "A से A के बाईं ओर मेज़ पर घूमिए: A, फिर B, फिर एक सीट, फिर D (A के सामने), फिर एक और सीट, फिर A के दाईं ओर की सीट। E, A के बगल में नहीं है, इसलिए E, D के पास की दो सीटों में से एक लेता है। D और A के दाईं ओर की सीट के बीच वाली सीट के सामने B की सीट है, इसलिए E वहाँ हो तो F के लिए E के सामने कोई सीट न बचे। अतः E, B और D के बीच बैठता है, F, E के सामने A के दाईं ओर, और C, D और F के बीच की सीट लेता है। "
  "केंद्र की ओर मुख होने पर C तब D के ठीक बाईं ओर है। B के ठीक दाईं ओर A है, E नहीं; F, E के सामने बैठा है, C के नहीं; और A के पड़ोसी B और F हैं, C नहीं।",
  "lr-sa-a-hexagonal-table-with-opposite-seats", pos=0, check=_sa12)

# 13 -- six friends in six coaches
def _sa13():
    names = ["Arun", "Bina", "Chand", "Dev", "Esha", "Farah"]
    sols = []
    for p in permutations(range(1, 7)):
        w = dict(zip(names, p))
        if (w["Chand"] == 4 and w["Farah"] == w["Chand"] - 1 and abs(w["Arun"] - w["Esha"]) == 3
                and w["Esha"] < w["Arun"] and w["Bina"] > w["Dev"]):
            sols.append(w)
    assert len(sols) == 1
    w = sols[0]
    facts = [w["Arun"] == 5, w["Bina"] == 2, w["Dev"] == 6, w["Esha"] == 3]
    assert facts == [True, False, False, False]
    return "Arun is in coach 5."
T(LR, "Seating Arrangement", "hard",
  "Six friends -- Arun, Bina, Chand, Dev, Esha and Farah -- travel in a train, one in each of six coaches numbered 1 to 6 from the engine. Chand is in coach 4, and Farah is in the coach just in front of Chand's, nearer the engine. Exactly two coaches lie between Arun's and Esha's, and Esha is nearer the engine than Arun. Bina is farther from the engine than Dev. Which one of the following is correct?",
  "छह मित्र -- अरुण, बीना, चाँद, देव, ईशा और फ़राह -- एक रेलगाड़ी में यात्रा करते हैं, इंजन से 1 से 6 तक क्रमांकित छह डिब्बों में से हर एक में एक। चाँद डिब्बा 4 में है, और फ़राह, चाँद के डिब्बे के ठीक आगे वाले डिब्बे में है, इंजन के निकट। अरुण और ईशा के डिब्बों के बीच ठीक दो डिब्बे हैं, और ईशा, अरुण से इंजन के अधिक निकट है। बीना, देव से इंजन से अधिक दूर है। निम्नलिखित में से कौन-सा सही है?",
  ["Arun is in coach 5.", "Bina is in coach 2.", "Dev is in coach 6.", "Esha is in coach 3."],
  ["अरुण डिब्बा 5 में है।", "बीना डिब्बा 2 में है।", "देव डिब्बा 6 में है।", "ईशा डिब्बा 3 में है।"],
  0,
  "Chand is in 4 and Farah in 3. Esha and Arun are three coaches apart with Esha nearer the engine: 1 and 4, 2 and 5, or 3 and 6. Coaches 4 and 3 are taken, which rules out the first and third pairs, so Esha is in 2 and Arun in 5. That leaves coaches 1 and 6 for Bina and Dev, and Bina is the farther from the engine: Dev in 1, Bina in 6. "
  "So Arun is in coach 5. Bina is in 6, not 2; Dev is in 1, not 6; and Esha is in 2, not 3 -- the other three options describe a seating that Farah's place rules out.",
  "चाँद 4 में है और फ़राह 3 में। ईशा और अरुण तीन डिब्बे दूर हैं और ईशा इंजन के निकट है: 1 और 4, 2 और 5, या 3 और 6। डिब्बे 4 और 3 भरे हैं, जिससे पहली और तीसरी जोड़ी ख़ारिज होती हैं, इसलिए ईशा 2 में है और अरुण 5 में। बीना और देव के लिए डिब्बे 1 और 6 बचते हैं, और बीना इंजन से अधिक दूर है: देव 1 में, बीना 6 में। "
  "अतः अरुण डिब्बा 5 में है। बीना 6 में है, 2 में नहीं; देव 1 में है, 6 में नहीं; और ईशा 2 में है, 3 में नहीं -- बाक़ी तीन विकल्प ऐसी व्यवस्था बताते हैं जिसे फ़राह का स्थान ख़ारिज कर देता है।",
  "lr-sa-six-friends-in-six-coaches", pos=3, check=_sa13)

# 14 -- one truth-teller among three friends
def _tl14():
    fits = []
    for teller in "ABC":
        truth = {x: x == teller for x in "ABC"}
        said = {"A": teller == "A",                 # A: 'I am the truth-teller.'
                "B": not truth["A"],                # B: 'A is lying.'
                "C": teller == "B"}                 # C: 'B is the truth-teller.'
        if all(said[x] == truth[x] for x in "ABC"):
            fits.append(teller)
    assert fits == ["A"]
    return "A is the truth-teller."
T(LR, "Truth-Liar", "hard",
  "Of three friends, A, B and C, exactly one always tells the truth and the other two always lie. A says, 'I am the truth-teller.' B says, 'A is lying.' C says, 'B is the truth-teller.' Which one of the following is correct?",
  "तीन मित्रों, A, B और C, में से ठीक एक हमेशा सच बोलता है और बाक़ी दो हमेशा झूठ। A कहता है, 'सच बोलने वाला मैं हूँ।' B कहता है, 'A झूठ बोल रहा है।' C कहता है, 'सच बोलने वाला B है।' निम्नलिखित में से कौन-सा सही है?",
  ["B is the truth-teller.", "C is the truth-teller.", "A is the truth-teller.", "Who tells the truth cannot be decided."],
  ["सच बोलने वाला B है।", "सच बोलने वाला C है।", "सच बोलने वाला A है।", "सच कौन बोलता है, यह तय नहीं किया जा सकता।"],
  2,
  "Try each friend as the truth-teller. If B were, then C's statement 'B is the truth-teller' would be true -- but C would be a liar, so that fails. If C were, C's own statement would make B the truth-teller as well, and there is only one -- that fails too. If A is the truth-teller, A's statement is true; B's 'A is lying' is false, as a liar's must be; and C's 'B is the truth-teller' is false, as it must be. Everything fits, so A is the truth-teller. "
  "A's own claim proves nothing on its own, since a liar could say the same; it is B's and C's statements that decide it.",
  "हर मित्र को सच बोलने वाला मानकर देखिए। यदि B होता, तो C का कथन 'सच बोलने वाला B है' सत्य होता -- पर C झूठा होता, इसलिए यह विफल है। यदि C होता, तो C का अपना कथन B को भी सच बोलने वाला बना देता, जबकि ऐसा केवल एक है -- यह भी विफल। यदि A सच बोलने वाला है, तो A का कथन सत्य है; B का 'A झूठ बोल रहा है' असत्य है, जैसा झूठे का होना चाहिए; और C का 'सच बोलने वाला B है' असत्य है, जैसा होना चाहिए। सब ठीक बैठता है, इसलिए A सच बोलने वाला है। "
  "A का अपना दावा अकेले कुछ सिद्ध नहीं करता, क्योंकि झूठा भी यही कह सकता है; B और C के कथन ही इसे तय करते हैं।",
  "lr-tl-one-truth-teller-among-three-friends", pos=0, check=_tl14)

# ---- the data-sufficiency block's three Reasoning items
def _ds17():
    orders = list(permutations("PQRS"))
    ok1 = lambda o: o.index("R") < o.index("P") < o.index("Q")
    ok2 = lambda o: o[3] == "S"
    s1 = {o[1] for o in orders if ok1(o)}
    s2 = {o[1] for o in orders if ok2(o)}
    both = {o[1] for o in orders if ok1(o) and ok2(o)}
    assert both == {"P"}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Four runners, P, Q, R and S, ran a race in which there were no ties. Who finished second?",
   "चार धावकों, P, Q, R और S, ने एक दौड़ लगाई जिसमें कोई बराबरी नहीं हुई। दूसरे स्थान पर कौन रहा?",
   "P finished ahead of Q but behind R.", "P, Q से आगे पर R से पीछे रहा।",
   "S finished last.", "S अंतिम रहा।",
   2,
   "Statement I alone fixes R ahead of P ahead of Q, but S could come anywhere, so the runner in second place could be S, R or P. Statement II alone says nothing about the other three. Together the order is R, P, Q, S, and P finished second. Both statements are needed.",
   "कथन I अकेले R को P से और P को Q से आगे रखता है, पर S कहीं भी आ सकता है, इसलिए दूसरे स्थान पर S, R या P हो सकता है। कथन II अकेले बाक़ी तीन के बारे में कुछ नहीं कहता। दोनों मिलकर क्रम R, P, Q, S है, और P दूसरे स्थान पर रहा। दोनों कथन आवश्यक हैं।",
   "lr-ds-the-runner-who-came-second", _ds17)

def _ds15():
    worlds = list(product((True, False), repeat=2))           # (fan on, light on)
    ok1 = lambda f, l: (not f) or l                           # whenever the fan is on, the light is on
    ok2 = lambda f, l: not f                                  # the fan is off
    s1 = {l for f, l in worlds if ok1(f, l)}
    s2 = {l for f, l in worlds if ok2(f, l)}
    both = {l for f, l in worlds if ok1(f, l) and ok2(f, l)}
    assert both == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Is the light in the hall on?",
   "क्या हॉल की बत्ती जल रही है?",
   "Whenever the fan in the hall is on, the light in the hall is on too.", "जब भी हॉल का पंखा चलता है, हॉल की बत्ती भी जलती है।",
   "The fan in the hall is off.", "हॉल का पंखा बंद है।",
   3,
   "Statement I says only what happens when the fan is on. Statement II says the fan is off, and then Statement I says nothing at all: the light may be on or off. Even together the statements do not answer the question. The trap is to read I as 'the light is on only when the fan is on' and conclude that the light is off.",
   "कथन I केवल यह बताता है कि पंखा चलने पर क्या होता है। कथन II कहता है कि पंखा बंद है, और तब कथन I कुछ भी नहीं कहता: बत्ती जल भी सकती है और बुझी भी हो सकती है। दोनों कथन साथ मिलकर भी प्रश्न का उत्तर नहीं देते। जाल यह है कि I को 'बत्ती केवल तभी जलती है जब पंखा चलता है' पढ़कर निष्कर्ष निकाल लिया जाए कि बत्ती बुझी है।",
   "lr-ds-a-light-that-goes-on-with-the-fan", _ds15)

def _ds16():
    colours = ["red", "blue", "green", "yellow", "white", "black"]
    def pairings(xs):
        if not xs:
            yield []
            return
        a = xs[0]
        for b in xs[1:]:
            rest = [x for x in xs if x not in (a, b)]
            for p in pairings(rest):
                yield [(a, b)] + p
    def opp(pr, x):
        return next(b if a == x else a for a, b in pr if x in (a, b))
    cubes = list(pairings(colours))
    ok1 = lambda pr: opp(pr, "blue") not in ("red", "green", "yellow")   # blue touches red, green and yellow
    ok2 = lambda pr: opp(pr, "white") == "yellow"
    s1 = {opp(pr, "red") for pr in cubes if ok1(pr)}
    s2 = {opp(pr, "red") for pr in cubes if ok2(pr)}
    both = {opp(pr, "red") for pr in cubes if ok1(pr) and ok2(pr)}
    assert both == {"green"}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "The six faces of a cube are painted red, blue, green, yellow, white and black, one colour to each face. Which colour is on the face opposite the red face?",
   "एक घन के छह फलक लाल, नीले, हरे, पीले, सफ़ेद और काले रंग से रँगे हैं, हर फलक पर एक रंग। लाल फलक के सामने वाले फलक पर कौन-सा रंग है?",
   "The blue face shares an edge with the red, the green and the yellow faces.", "नीला फलक लाल, हरे और पीले फलकों से एक-एक किनारा साझा करता है।",
   "The white face is opposite the yellow face.", "सफ़ेद फलक पीले फलक के सामने है।",
   2,
   "Statement I alone: blue is next to red, green and yellow, so the face opposite blue is white or black -- and red's opposite is still open. Statement II alone pairs white with yellow and says nothing about red. Together: white is opposite yellow, so blue, which cannot be opposite red, green or yellow, must be opposite black. The only pair left is red and green. Both statements are needed.",
   "कथन I अकेले: नीला, लाल, हरे और पीले के बगल में है, इसलिए नीले के सामने सफ़ेद या काला है -- और लाल के सामने वाला फलक अब भी खुला है। कथन II अकेले सफ़ेद को पीले से जोड़ता है और लाल के बारे में कुछ नहीं कहता। दोनों मिलकर: सफ़ेद, पीले के सामने है, इसलिए नीला, जो लाल, हरे या पीले के सामने नहीं हो सकता, काले के सामने होगा। बचा हुआ एकमात्र जोड़ा लाल और हरा है। दोनों कथन आवश्यक हैं।",
   "lr-ds-the-colour-opposite-red", _ds16)
