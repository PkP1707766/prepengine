# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 9 -- Logical Reasoning (20 items: 17 in the Reasoning slots, 3 in the data-sufficiency block).

Layout C, the 2026 shape: the heavier Reasoning section. Exam-level mix (1 easy / 10 medium / 9 hard), with none of
the shapes of Levels 1-3 or Simulators 1-8: a bridge called safe because the alternative is alarming, an astrologer's
hits counted without the misses, a survey question that assumes its answer, what a chess club's rules make certain, a
faster road that empties hotels, what to ask of a tree-planting drive, two phones that condemn a brand; a relay
team's order of legs, four friends with their pets and cities, a quiz's answer key read back from three scores; a
grandmother written in symbols; a substitution code checked for consistency, a word reversed in halves; an arrow seen
in a mirror on the north wall; a block enlarged and then painted; squares, rectangles and circles, kettles and imported
goods; and in the data-sufficiency block a place in a queue after people leave, three boxes in three colours, and
pens that may or may not be red. Arrangement, relation, code, direction, cube, syllogism and quiz keys are found by
checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

def _venn(n):
    """Every way n classes can overlap: each of the 2^n - 1 regions of the diagram is empty or not."""
    regions = [r for r in product((0, 1), repeat=n) if any(r)]
    for present in product((0, 1), repeat=len(regions)):
        yield {r for r, p in zip(regions, present) if p}

# 1 -- a bridge called safe because the alternative is alarming
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'This bridge cannot be unsafe. If it were, the thousands of people who cross it every day would be in danger, and the city could not cope with closing it.' Which one of the following best describes the flaw in this argument?",
  "'यह पुल असुरक्षित नहीं हो सकता। यदि होता, तो रोज़ इसे पार करने वाले हज़ारों लोग ख़तरे में होते, और शहर इसे बंद करने का बोझ नहीं उठा सकता।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It concludes that a claim is false because its being true would have unwelcome results.",
   "It relies on the opinion of the people who cross the bridge instead of that of engineers.",
   "It assumes that the city has already inspected the bridge and found it to be sound.",
   "It confuses the number of people who cross the bridge with the weight the bridge can bear."],
  ["यह किसी दावे को इसलिए झूठा मान लेता है कि उसके सच होने के परिणाम अप्रिय होंगे।",
   "यह इंजीनियरों के बजाय पुल पार करने वाले लोगों की राय पर निर्भर करता है।",
   "यह मान लेता है कि शहर पुल का पहले ही निरीक्षण कर चुका है और उसे ठीक पाया है।",
   "यह पुल पार करने वाले लोगों की संख्या को उस भार से भ्रमित करता है जो पुल सह सकता है।"],
  0,
  "Whether the bridge is safe is a question of its condition. The argument instead points to how bad things would be if it were unsafe -- danger to commuters, a city unable to cope -- and treats that as a reason to believe it is safe. How unwelcome a fact would be is no evidence that it is false. "
  "The argument cites no one's opinion, mentions no inspection, and does not discuss the bridge's load at all.",
  "पुल सुरक्षित है या नहीं, यह उसकी दशा का प्रश्न है। तर्क इसके बजाय यह बताता है कि यदि पुल असुरक्षित होता तो स्थिति कितनी बुरी होती -- यात्रियों को ख़तरा, शहर पर बोझ -- और उसे पुल के सुरक्षित होने का कारण मान लेता है। कोई तथ्य कितना अप्रिय होगा, यह उसके झूठे होने का प्रमाण नहीं। "
  "तर्क किसी की राय उद्धृत नहीं करता, किसी निरीक्षण का उल्लेख नहीं करता, और पुल के भार पर कुछ नहीं कहता।",
  "lr-sc-a-bridge-called-safe-because-the-alternative-is-alarming", pos=3)

# 2 -- an astrologer's hits counted without the misses
T(LR, "Statement-Conclusion/Assumption", "hard",
  "An astrologer made 100 specific predictions last year. A magazine lists the 14 that came true and concludes that the astrologer can foresee events. Which one of the following, if true, most seriously weakens the magazine's conclusion?",
  "एक ज्योतिषी ने पिछले वर्ष 100 विशिष्ट भविष्यवाणियाँ कीं। एक पत्रिका उनमें से सच निकलीं 14 की सूची देकर निष्कर्ष निकालती है कि ज्योतिषी घटनाओं का पूर्वानुमान कर सकता है। निम्नलिखित में से कौन-सा, यदि सत्य हो, पत्रिका के निष्कर्ष को सबसे गंभीर रूप से कमज़ोर करता है?",
  ["About as many of the predictions would have come true if they had been mere guesses.",
   "The magazine did not say which of the 14 correct predictions was the most important one.",
   "Many of the magazine's readers had heard of the astrologer before the article appeared.",
   "Some of the 14 predictions that came true were about events in countries far away."],
  ["यदि भविष्यवाणियाँ केवल अनुमान होतीं, तब भी लगभग उतनी ही सच निकलतीं।",
   "पत्रिका ने यह नहीं बताया कि 14 सही भविष्यवाणियों में सबसे महत्त्वपूर्ण कौन-सी थी।",
   "पत्रिका के बहुत-से पाठकों ने लेख छपने से पहले ही ज्योतिषी के बारे में सुना था।",
   "सच निकलीं 14 भविष्यवाणियों में से कुछ दूर के देशों की घटनाओं के बारे में थीं।"],
  0,
  "The magazine counts the 14 hits and ignores the 86 misses. If guessing would have produced about as many hits, the 14 show no special power at all -- which strikes at the conclusion directly. "
  "Which hit mattered most, what readers knew beforehand, and where the events happened say nothing about whether the hits beat chance.",
  "पत्रिका 14 सफलताएँ गिनती है और 86 विफलताओं की अनदेखी करती है। यदि अनुमान से भी लगभग उतनी ही सफलताएँ मिलतीं, तो 14 कोई विशेष शक्ति नहीं दिखातीं -- जो सीधे निष्कर्ष पर चोट करता है। "
  "कौन-सी सफलता सबसे महत्त्वपूर्ण थी, पाठक पहले क्या जानते थे, और घटनाएँ कहाँ हुईं -- इनसे यह पता नहीं चलता कि सफलताएँ संयोग से अधिक थीं या नहीं।",
  "lr-sc-an-astrologer-s-hits-counted-without-the-misses", pos=0)

# 3 -- a survey question that assumes its answer
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A town survey asks residents: 'How much more should the council spend on repairing the dangerous potholes on Station Road?' Which one of the following best describes the problem with this question?",
  "एक कस्बे का सर्वेक्षण निवासियों से पूछता है: 'स्टेशन रोड के ख़तरनाक गड्ढों की मरम्मत पर परिषद को कितना अधिक ख़र्च करना चाहिए?' निम्नलिखित में से कौन-सा इस प्रश्न की समस्या का सबसे अच्छा वर्णन करता है?",
  ["It takes for granted that the potholes are dangerous and that more should be spent.",
   "It asks about only one road, although the town has many other roads that need repairing.",
   "It asks residents about money, a matter on which ordinary people can have no opinion.",
   "It uses the word 'council', which some of the residents who answer may not understand."],
  ["यह मान लेता है कि गड्ढे ख़तरनाक हैं और उन पर अधिक ख़र्च होना चाहिए।",
   "यह केवल एक सड़क के बारे में पूछता है, यद्यपि कस्बे की कई और सड़कों को मरम्मत चाहिए।",
   "यह निवासियों से पैसे के बारे में पूछता है, ऐसा विषय जिस पर आम लोगों की कोई राय नहीं हो सकती।",
   "यह 'परिषद' शब्द का प्रयोग करता है, जिसे उत्तर देने वाले कुछ निवासी शायद न समझें।"],
  0,
  "The question is loaded: whatever figure a resident gives, the answer accepts that the potholes are dangerous and that more money should go to them. Someone who thinks the potholes are minor, or that no more should be spent, has no way to say so. "
  "Asking about one road is a choice of topic, not a fault in the wording; residents can hold views on spending; and 'council' is an ordinary word.",
  "प्रश्न पहले से झुका हुआ है: निवासी जो भी राशि बताए, उत्तर यह स्वीकार कर लेता है कि गड्ढे ख़तरनाक हैं और उन पर अधिक पैसा जाना चाहिए। जो मानता है कि गड्ढे मामूली हैं, या कि और ख़र्च नहीं होना चाहिए, उसके पास यह कहने का कोई रास्ता नहीं। "
  "एक सड़क के बारे में पूछना विषय का चुनाव है, शब्दों की त्रुटि नहीं; निवासी ख़र्च पर राय रख सकते हैं; और 'परिषद' एक सामान्य शब्द है।",
  "lr-sc-a-survey-question-that-assumes-its-answer", pos=2)

# 4 -- what a chess club's rules make certain
def _sc4():
    # worlds: Ravi's club membership and class; the rules restrict which combinations are possible
    worlds = [(club, cls) for club in (True, False) for cls in ("9", "10", "other")
              if (not club or cls in ("9", "10")) and cls != "10"]      # club members are in 9 or 10; band members are not in 10
    must = {
        "If Ravi is in the chess club, Ravi is in Class 9.": all(cls == "9" for club, cls in worlds if club),
        "Ravi is in Class 9.": all(cls == "9" for club, cls in worlds),
        "Ravi is not in the chess club.": all(not club for club, cls in worlds),
        "No member of the chess club is in the school band.": False,     # a Class 9 member may well play in the band
    }
    assert [k for k, v in must.items() if v] == ["If Ravi is in the chess club, Ravi is in Class 9."]
    return "If Ravi is in the chess club, Ravi is in Class 9."
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Every member of the school chess club is in Class 9 or Class 10. No Class 10 student is in the school band. Ravi is in the school band. Which one of the following must be true?",
  "विद्यालय के शतरंज क्लब का हर सदस्य कक्षा 9 या कक्षा 10 में है। कक्षा 10 का कोई विद्यार्थी विद्यालय के बैंड में नहीं है। रवि विद्यालय के बैंड में है। निम्नलिखित में से कौन-सा अवश्य सत्य है?",
  ["If Ravi is in the chess club, Ravi is in Class 9.",
   "Ravi is in Class 9.",
   "Ravi is not in the chess club.",
   "No member of the chess club is in the school band."],
  ["यदि रवि शतरंज क्लब में है, तो रवि कक्षा 9 में है।",
   "रवि कक्षा 9 में है।",
   "रवि शतरंज क्लब में नहीं है।",
   "शतरंज क्लब का कोई सदस्य विद्यालय के बैंड में नहीं है।"],
  0,
  "Ravi is in the band, so Ravi is not in Class 10. If Ravi is also in the chess club, Ravi must be in Class 9 or 10 -- and so in Class 9. That conditional must be true. "
  "But nothing says Ravi is in the chess club, so 'Ravi is in Class 9' need not hold (Ravi could be in another class); nothing rules Ravi out of the club either; and Class 9 members of the club may well play in the band.",
  "रवि बैंड में है, इसलिए रवि कक्षा 10 में नहीं है। यदि रवि शतरंज क्लब में भी है, तो उसे कक्षा 9 या 10 में होना चाहिए -- यानी कक्षा 9 में। यह शर्त वाला कथन अवश्य सत्य है। "
  "पर कहीं नहीं कहा गया कि रवि शतरंज क्लब में है, इसलिए 'रवि कक्षा 9 में है' आवश्यक नहीं (रवि किसी और कक्षा में हो सकता है); कुछ भी रवि को क्लब से बाहर नहीं करता; और क्लब के कक्षा 9 के सदस्य बैंड में हो सकते हैं।",
  "lr-sc-what-a-chess-club-s-rules-make-certain", pos=3, check=_sc4)

# 5 -- a faster road that empties hotels
T(LR, "Statement-Conclusion/Assumption", "hard",
  "After a new expressway halved the travel time between a large city and a small hill town, the number of hotel nights booked in the hill town fell, even though more people visited the town than before. Which one of the following, if true, best explains this?",
  "एक नए एक्सप्रेसवे द्वारा एक बड़े शहर और एक छोटे पहाड़ी कस्बे के बीच यात्रा का समय आधा कर देने के बाद, पहाड़ी कस्बे में होटलों में ठहरने की रातों की संख्या घट गई, यद्यपि पहले से अधिक लोग कस्बे में आए। निम्नलिखित में से कौन-सा, यदि सत्य हो, इसकी सबसे अच्छी व्याख्या करता है?",
  ["Many visitors who once had to stay overnight can now go back to the city the same day.",
   "The expressway was built mainly to carry goods traffic rather than tourists to the hills.",
   "Hotel rooms in the hill town have always cost less than hotel rooms in the large city.",
   "The number of people visiting the hill town rose steadily after the expressway opened."],
  ["बहुत-से आगंतुक, जिन्हें पहले रात रुकना पड़ता था, अब उसी दिन शहर लौट सकते हैं।",
   "एक्सप्रेसवे मुख्यतः पहाड़ों तक पर्यटकों के बजाय माल ढोने के लिए बनाया गया था।",
   "पहाड़ी कस्बे के होटल के कमरे सदा बड़े शहर के होटल के कमरों से सस्ते रहे हैं।",
   "एक्सप्रेसवे खुलने के बाद पहाड़ी कस्बे में आने वालों की संख्या लगातार बढ़ी।"],
  0,
  "More visitors but fewer hotel nights means each visitor, on average, stays fewer nights. A trip short enough to finish in a day removes the need to stay over -- which reconciles the two facts. "
  "Carrying goods says nothing about why visitors stopped staying; cheaper rooms would, if anything, encourage stays; and the rise in visitors is part of the puzzle, not its explanation.",
  "अधिक आगंतुक पर कम होटल-रातें का अर्थ है कि औसतन हर आगंतुक कम रातें रुकता है। एक दिन में पूरी हो जाने लायक़ छोटी यात्रा रुकने की आवश्यकता हटा देती है -- जिससे दोनों तथ्य मेल खा जाते हैं। "
  "माल ढोने से यह पता नहीं चलता कि आगंतुकों ने रुकना क्यों छोड़ा; सस्ते कमरे तो रुकने को बढ़ावा देते; और आगंतुकों की बढ़त पहेली का भाग है, उसकी व्याख्या नहीं।",
  "lr-sc-a-faster-road-that-empties-hotels", pos=0)

# 6 -- what to ask of a tree-planting drive
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A district plans to plant one lakh saplings this monsoon in order to increase its forest cover. Which one of the following would it be most important to know in judging whether the plan will achieve its aim?",
  "एक ज़िला अपना वन-आवरण बढ़ाने के लिए इस मानसून में एक लाख पौधे लगाने की योजना बनाता है। योजना अपना उद्देश्य पूरा करेगी या नहीं, यह आँकने के लिए निम्नलिखित में से क्या जानना सबसे महत्त्वपूर्ण होगा?",
  ["What share of saplings from the district's past drives survived to become trees",
   "How many people from the district are expected to volunteer to plant the saplings",
   "Whether the planting will be done on a public holiday so that schools can take part",
   "How many saplings the neighbouring districts are planning to plant this monsoon"],
  ["ज़िले के पिछले अभियानों के पौधों का कितना भाग जीवित रहकर पेड़ बना",
   "ज़िले के कितने लोग पौधे लगाने के लिए स्वयंसेवा करेंगे, ऐसी अपेक्षा है",
   "क्या पौधे सार्वजनिक अवकाश पर लगाए जाएँगे ताकि विद्यालय भाग ले सकें",
   "पड़ोसी ज़िले इस मानसून में कितने पौधे लगाने की योजना बना रहे हैं"],
  0,
  "Forest cover grows only if saplings survive and grow into trees; planting a lakh achieves nothing if most of them die. The record of past drives is the best guide to how many will survive. "
  "The number of volunteers and the choice of day affect how the planting is done, not whether the trees survive; what neighbouring districts plant does not change this district's cover.",
  "वन-आवरण तभी बढ़ता है जब पौधे जीवित रहकर पेड़ बनें; यदि अधिकांश मर जाएँ तो एक लाख लगाने से कुछ नहीं होता। पिछले अभियानों का रिकॉर्ड यह जानने का सबसे अच्छा आधार है कि कितने बचेंगे। "
  "स्वयंसेवकों की संख्या और दिन का चुनाव रोपाई के ढंग को प्रभावित करते हैं, पेड़ों के बचने को नहीं; पड़ोसी ज़िले क्या लगाते हैं, इससे इस ज़िले का आवरण नहीं बदलता।",
  "lr-sc-what-to-ask-of-a-tree-planting-drive", pos=3)

# 7 -- two phones that condemn a brand
T(LR, "Statement-Conclusion/Assumption", "medium",
  "'I have bought two phones of this brand, and both stopped working within a month. So every phone this company makes is badly built.' Which one of the following best describes the flaw in this reasoning?",
  "'मैंने इस ब्रांड के दो फ़ोन ख़रीदे, और दोनों एक महीने के भीतर बंद हो गए। इसलिए यह कंपनी जो भी फ़ोन बनाती है, वह ख़राब बना है।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It draws a conclusion about all the company's phones from just two of them.",
   "It assumes that a phone which works for a month will go on working for years.",
   "It relies on claims made in the advertisements of a rival phone company.",
   "It treats the price of a phone as if it were a reliable sign of its quality."],
  ["यह केवल दो फ़ोनों से कंपनी के सभी फ़ोनों के बारे में निष्कर्ष निकालता है।",
   "यह मान लेता है कि एक महीना चलने वाला फ़ोन बरसों चलता रहेगा।",
   "यह किसी प्रतिद्वंद्वी फ़ोन कंपनी के विज्ञापनों के दावों पर निर्भर करता है।",
   "यह फ़ोन के मूल्य को उसकी गुणवत्ता का विश्वसनीय संकेत मान लेता है।"],
  0,
  "Two phones out of the many a company makes are far too few to show that every one is badly built; the speaker may simply have been unlucky. The conclusion outruns the evidence. "
  "The argument makes no claim about phones lasting years, cites no advertisements, and says nothing about price.",
  "किसी कंपनी के बनाए अनगिनत फ़ोनों में से दो बहुत कम हैं यह दिखाने के लिए कि हर एक ख़राब बना है; हो सकता है बोलने वाला बस अभागा रहा हो। निष्कर्ष प्रमाण से बहुत आगे निकल जाता है। "
  "तर्क फ़ोनों के बरसों चलने के बारे में कोई दावा नहीं करता, किसी विज्ञापन का हवाला नहीं देता, और मूल्य पर कुछ नहीं कहता।",
  "lr-sc-two-phones-that-condemn-a-brand", pos=2)

# 8 -- squares, rectangles and circles
def _sy8():
    one = two = True
    for filled in _venn(4):                          # (square, rectangle, circle, shape on the board)
        if any(s and not r for s, r, ci, b in filled):       # all squares are rectangles
            continue
        if any(r and ci for s, r, ci, b in filled):          # no rectangle is a circle
            continue
        if not any(s and b for s, r, ci, b in filled):       # some shapes on the board are squares
            continue
        one &= not any(s and ci for s, r, ci, b in filled)
        two &= any(b and r for s, r, ci, b in filled)
    return c.T2R[{(True, True): 2, (True, False): 0, (False, True): 1, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "medium",
   "Statements: All squares are rectangles. No rectangle is a circle. Some of the shapes on the board are squares.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी वर्ग आयत हैं। कोई आयत वृत्त नहीं है। बोर्ड पर की कुछ आकृतियाँ वर्ग हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["No square is a circle.", "Some of the shapes on the board are rectangles."],
   ["कोई वर्ग वृत्त नहीं है।", "बोर्ड पर की कुछ आकृतियाँ आयत हैं।"],
   2,
   "Both follow. I: every square is a rectangle and no rectangle is a circle, so no square can be a circle. "
   "II: some shapes on the board are squares, and every square is a rectangle, so those shapes are rectangles.",
   "दोनों निकलते हैं। I: हर वर्ग एक आयत है और कोई आयत वृत्त नहीं, इसलिए कोई वर्ग वृत्त नहीं हो सकता। "
   "II: बोर्ड पर की कुछ आकृतियाँ वर्ग हैं, और हर वर्ग आयत है, इसलिए वे आकृतियाँ आयत हैं।",
   "lr-sy-squares-rectangles-and-circles", roman=True, check=_sy8)

# 9 -- kettles and imported goods
def _sy9():
    one = two = True
    for filled in _venn(3):                          # (kettle, appliance, imported)
        if any(k and not a for k, a, i in filled):
            continue
        if not any(a and i for k, a, i in filled):
            continue
        one &= any(k and i for k, a, i in filled)
        two &= any(i and a for k, a, i in filled)
    return c.T2R[{(True, True): 2, (True, False): 0, (False, True): 1, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "easy",
   "Statements: All kettles are appliances. Some appliances are imported.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी केतलियाँ उपकरण हैं। कुछ उपकरण आयातित हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some kettles are imported.", "Some imported things are appliances."],
   ["कुछ केतलियाँ आयातित हैं।", "कुछ आयातित वस्तुएँ उपकरण हैं।"],
   1,
   "Only II follows: some appliances are imported, which is the same as saying some imported things are appliances. "
   "I does not follow: the imported appliances might all be fans or mixers, with not a single kettle among them.",
   "केवल II निकलता है: कुछ उपकरण आयातित हैं, जो यह कहने के समान है कि कुछ आयातित वस्तुएँ उपकरण हैं। "
   "I नहीं निकलता: हो सकता है सभी आयातित उपकरण पंखे या मिक्सर हों, और उनमें एक भी केतली न हो।",
   "lr-sy-kettles-and-imported-goods", roman=True, check=_sy9)

# 10 -- a relay team's order of legs
def _sa10():
    fits = []
    for o in permutations("PQRS"):
        pos = {x: i for i, x in enumerate(o)}
        if pos["Q"] == pos["P"] + 1 and pos["R"] not in (0, 3) and pos["S"] < pos["R"]:
            fits.append(o)
    assert fits == [tuple("SRPQ")]
    return fits[0][2]
T(LR, "Seating Arrangement", "medium",
  "Four runners, P, Q, R and S, run the four legs of a relay race, one leg each.\n"
  "- Q runs the leg immediately after P's.\n"
  "- R runs neither the first leg nor the last.\n"
  "- S runs before R.\n"
  "Who runs the third leg?",
  "चार धावक, P, Q, R और S, एक रिले दौड़ के चार चरण दौड़ते हैं, हर एक एक चरण।\n"
  "- Q, P के ठीक बाद वाला चरण दौड़ता है।\n"
  "- R न पहला चरण दौड़ता है न अंतिम।\n"
  "- S, R से पहले दौड़ता है।\n"
  "तीसरा चरण कौन दौड़ता है?",
  ["P", "Q", "R", "S"], ["P", "Q", "R", "S"],
  0,
  "R runs the second or the third leg. If R ran the third, S would run the first or the second, leaving legs 2 and 4 or legs 1 and 4 for P and Q, which are not next to each other -- impossible. So R runs the second leg, S the first (S runs before R), and P and Q take the third and fourth in that order. The order is S, R, P, Q: P runs the third leg. "
  "Q runs the fourth, R the second and S the first.",
  "R दूसरा या तीसरा चरण दौड़ता है। यदि R तीसरा दौड़ता, तो S पहला या दूसरा दौड़ता, और P तथा Q के लिए बचे चरण एक-दूसरे के बग़ल में न होते -- असंभव। इसलिए R दूसरा चरण दौड़ता है, S पहला (S, R से पहले दौड़ता है), और P तथा Q उसी क्रम में तीसरा और चौथा लेते हैं। क्रम है S, R, P, Q: तीसरा चरण P दौड़ता है। "
  "Q चौथा, R दूसरा और S पहला दौड़ता है।",
  "lr-sa-a-relay-team-s-order-of-legs", pos=1, check=_sa10)

# 11 -- four friends with their pets and cities
NAMES11, PETS11, CITIES11 = ["Anil", "Bela", "Chirag", "Divya"], ["cat", "dog", "fish", "parrot"], ["Agra", "Bhopal", "Cochin", "Delhi"]
CLUES11 = [
    lambda p, c_: all(c_[n] == "Cochin" for n in NAMES11 if p[n] == "parrot"),
    lambda p, c_: p["Bela"] == "dog",
    lambda p, c_: c_["Divya"] == "Delhi" and p["Divya"] != "cat",
    lambda p, c_: all(p[n] == "cat" for n in NAMES11 if c_[n] == "Bhopal"),
    lambda p, c_: c_["Chirag"] != "Bhopal",
]
def _sa11():
    fits = []
    for pp in permutations(PETS11):
        for cc in permutations(CITIES11):
            p, c_ = dict(zip(NAMES11, pp)), dict(zip(NAMES11, cc))
            if all(f(p, c_) for f in CLUES11):
                fits.append((p, c_))
    assert len(fits) == 1
    p, c_ = fits[0]
    assert (p["Anil"], c_["Anil"], c_["Bela"], p["Chirag"]) == ("cat", "Bhopal", "Agra", "parrot")
    return f"{p['Divya'].capitalize()}; {c_['Bela']}"
T(LR, "Seating Arrangement", "hard",
  "Four friends -- Anil, Bela, Chirag and Divya -- each keep a different pet (a cat, a dog, a fish or a parrot) and each live in a different city (Agra, Bhopal, Cochin or Delhi).\n"
  "- The friend who keeps the parrot lives in Cochin.\n"
  "- Bela keeps the dog.\n"
  "- Divya lives in Delhi and does not keep the cat.\n"
  "- The friend who lives in Bhopal keeps the cat.\n"
  "- Chirag does not live in Bhopal.\n"
  "Which pet does Divya keep, and where does Bela live?",
  "चार मित्र -- अनिल, बेला, चिराग और दिव्या -- हर एक अलग पालतू (बिल्ली, कुत्ता, मछली या तोता) रखता है और हर एक अलग शहर (आगरा, भोपाल, कोचीन या दिल्ली) में रहता है।\n"
  "- तोता रखने वाला मित्र कोचीन में रहता है।\n"
  "- बेला कुत्ता रखती है।\n"
  "- दिव्या दिल्ली में रहती है और बिल्ली नहीं रखती।\n"
  "- भोपाल में रहने वाला मित्र बिल्ली रखता है।\n"
  "- चिराग भोपाल में नहीं रहता।\n"
  "दिव्या कौन-सा पालतू रखती है, और बेला कहाँ रहती है?",
  ["Fish; Agra", "Parrot; Agra", "Fish; Cochin", "Cat; Bhopal"],
  ["मछली; आगरा", "तोता; आगरा", "मछली; कोचीन", "बिल्ली; भोपाल"],
  0,
  "Whoever lives in Bhopal keeps the cat. That cannot be Divya (Delhi), Chirag (not Bhopal) or Bela (who keeps the dog), so Anil lives in Bhopal and keeps the cat. The fish and the parrot are left for Chirag and Divya; the parrot's keeper lives in Cochin, and Divya lives in Delhi, so Divya keeps the fish and Chirag the parrot, in Cochin. Bela takes the city left over: Agra. "
  "'Parrot' for Divya ignores that the parrot's keeper lives in Cochin; Cochin is Chirag's city, not Bela's; and the cat and Bhopal belong to Anil.",
  "जो भोपाल में रहता है वह बिल्ली रखता है। वह दिव्या (दिल्ली), चिराग (भोपाल में नहीं) या बेला (जो कुत्ता रखती है) नहीं हो सकता, इसलिए अनिल भोपाल में रहता है और बिल्ली रखता है। मछली और तोता चिराग और दिव्या के लिए बचते हैं; तोते वाला कोचीन में रहता है, और दिव्या दिल्ली में रहती है, इसलिए दिव्या मछली रखती है और चिराग तोता, कोचीन में। बेला बचा हुआ शहर लेती है: आगरा। "
  "दिव्या के लिए 'तोता' इस बात की अनदेखी करता है कि तोते वाला कोचीन में रहता है; कोचीन चिराग का शहर है, बेला का नहीं; और बिल्ली तथा भोपाल अनिल के हैं।",
  "lr-sa-four-friends-with-their-pets-and-cities", pos=1, check=_sa11)

# 12 -- a quiz's answer key read back from three scores
def _sa12():
    answers = {"Asha": "TTFF", "Bina": "TFTF", "Chetan": "FTTT"}
    scores = {"Asha": 3, "Bina": 3, "Chetan": 2}
    keys = ["".join(k) for k in product("TF", repeat=4)
            if all(sum(a == b for a, b in zip(answers[n], k)) == scores[n] for n in answers)]
    assert keys == ["TTTF"]
    return " ".join(keys[0])
T(LR, "Seating Arrangement", "hard",
  "A quiz has four questions, each to be answered True (T) or False (F). Three students answered as follows, and their scores (one mark for each correct answer) are given.\n"
  "- Asha: T T F F, score 3\n"
  "- Bina: T F T F, score 3\n"
  "- Chetan: F T T T, score 2\n"
  "What is the correct answer key, from question 1 to question 4?",
  "एक प्रश्नोत्तरी में चार प्रश्न हैं, जिनमें से हर एक का उत्तर सत्य (T) या असत्य (F) देना है। तीन विद्यार्थियों ने नीचे दिए अनुसार उत्तर दिए, और उनके अंक (हर सही उत्तर का एक अंक) दिए गए हैं।\n"
  "- आशा: T T F F, अंक 3\n"
  "- बीना: T F T F, अंक 3\n"
  "- चेतन: F T T T, अंक 2\n"
  "प्रश्न 1 से प्रश्न 4 तक सही उत्तर-कुंजी क्या है?",
  ["T T T F", "T T F F", "T F T F", "F T T F"],
  ["T T T F", "T T F F", "T F T F", "F T T F"],
  0,
  "Asha and Bina agree on questions 1 and 4 and disagree on 2 and 3, so on 2 and 3 exactly one of them is right each time -- two marks between them. They have 6 marks together, so both must be right on 1 and 4: the key starts T and ends F. Chetan answered F to question 1 and T to question 4, both wrong, so his 2 marks come from questions 2 and 3: both are T. The key is T T T F (check: Asha 3, Bina 3, Chetan 2). "
  "T T F F and T F T F are Asha's and Bina's own answers, which would give them 4 marks; F T T F would give Asha only 2.",
  "आशा और बीना प्रश्न 1 और 4 पर सहमत हैं और 2 तथा 3 पर असहमत, इसलिए 2 और 3 पर हर बार उनमें से ठीक एक सही है -- दोनों के मिलाकर दो अंक। उनके मिलाकर 6 अंक हैं, इसलिए दोनों 1 और 4 पर सही होंगे: कुंजी T से शुरू होकर F पर ख़त्म होती है। चेतन ने प्रश्न 1 का F और प्रश्न 4 का T उत्तर दिया, दोनों ग़लत, इसलिए उसके 2 अंक प्रश्न 2 और 3 से हैं: दोनों T हैं। कुंजी T T T F है (जाँच: आशा 3, बीना 3, चेतन 2)। "
  "T T F F और T F T F आशा और बीना के अपने उत्तर हैं, जिनसे उन्हें 4 अंक मिलते; F T T F से आशा को केवल 2 मिलते।",
  "lr-sa-a-quiz-s-answer-key-read-back-from-three-scores", pos=3, check=_sa12)

# 13 -- a grandmother written in symbols
def _br13():
    # each symbol: (generation step from the first person down to the second, the first person's sex)
    sym = {"×": (1, "M"), "+": (1, "F"), "-": (0, "F"), "÷": (0, "M")}
    def reading(expr):
        a, op1, k, op2, t = expr.split()
        g1, s1 = sym[op1]
        g2, _ = sym[op2]
        return g1 + g2, s1                          # generations from M down to T, and M's sex
    opts = {"M + K × T": None, "M × K + T": None, "M - K × T": None, "M + K - T": None}
    found = [o for o in opts if reading(o) == (2, "F")]
    assert found == ["M + K × T"]
    return found[0]
T(LR, "Blood Relation", "hard",
  "In a code, 'P × Q' means P is the father of Q; 'P + Q' means P is the mother of Q; 'P - Q' means P is the sister of Q; and 'P ÷ Q' means P is the brother of Q. Which one of the following means that M is the grandmother of T?",
  "एक कूट में 'P × Q' का अर्थ है P, Q का पिता है; 'P + Q' का अर्थ है P, Q की माँ है; 'P - Q' का अर्थ है P, Q की बहन है; और 'P ÷ Q' का अर्थ है P, Q का भाई है। निम्नलिखित में से किसका अर्थ है कि M, T की दादी/नानी है?",
  ["M + K × T", "M × K + T", "M - K × T", "M + K - T"],
  ["M + K × T", "M × K + T", "M - K × T", "M + K - T"],
  0,
  "M + K × T reads: M is the mother of K, and K is the father of T -- so M is T's father's mother, T's grandmother. "
  "M × K + T makes M the father of T's mother, a grandfather; M - K × T makes M the sister of T's father, an aunt; and M + K - T makes M the mother of K, who is T's sister, so M is T's mother.",
  "M + K × T का अर्थ है: M, K की माँ है, और K, T का पिता है -- इसलिए M, T के पिता की माँ, यानी T की दादी है। "
  "M × K + T में M, T की माँ का पिता, यानी नाना बनता है; M - K × T में M, T के पिता की बहन, यानी बुआ; और M + K - T में M, K की माँ है, जो T की बहन है, इसलिए M, T की माँ है।",
  "lr-br-a-grandmother-written-in-symbols", pos=2, check=_br13)

# 14 -- a substitution code checked for consistency
def _cd14():
    code = dict(zip("TIGER", "QZBNX"))
    def fits(word, coded):
        m = dict(code)
        for a, b in zip(word, coded):
            if a in m and m[a] != b:
                return False
            if a not in m:
                if b in m.values():
                    return False
                m[a] = b
        return len(set(m.values())) == len(m) and all(k != v for k, v in m.items())
    opts = ["QZBXNMM", "QZBXNMK", "QZBXNZZ", "QZBNXMM"]
    ok = [o for o in opts if fits("TIGRESS", o)]
    assert ok == ["QZBXNMM"]
    return ok[0]
T(LR, "Coding-Decoding", "hard",
  "In a code, each letter is replaced by a different letter; the same letter is always replaced by the same code letter, and different letters by different code letters. If TIGER is written as QZBNX, which one of the following could be the code for TIGRESS?",
  "एक कूट में हर अक्षर को किसी दूसरे अक्षर से बदला जाता है; एक ही अक्षर को सदा एक ही कूट-अक्षर से, और अलग-अलग अक्षरों को अलग-अलग कूट-अक्षरों से। यदि TIGER को QZBNX लिखा जाता है, तो निम्नलिखित में से कौन-सा TIGRESS का कूट हो सकता है?",
  ["QZBXNMM", "QZBXNMK", "QZBXNZZ", "QZBNXMM"],
  ["QZBXNMM", "QZBXNMK", "QZBXNZZ", "QZBNXMM"],
  0,
  "From TIGER = QZBNX: T = Q, I = Z, G = B, E = N, R = X. So TIGRESS must begin Q Z B X N, and its two S's must share one code letter that is not already used for another letter. QZBXNMM does exactly that, with S = M. "
  "QZBXNMK gives the two S's different code letters; QZBXNZZ codes S as Z, which already stands for I; and QZBNXMM codes R as N and E as X, the other way round.",
  "TIGER = QZBNX से: T = Q, I = Z, G = B, E = N, R = X। इसलिए TIGRESS, Q Z B X N से शुरू होना चाहिए, और उसके दोनों S का एक ही कूट-अक्षर होना चाहिए जो पहले से किसी दूसरे अक्षर के लिए प्रयुक्त न हो। QZBXNMM ठीक यही करता है, S = M के साथ। "
  "QZBXNMK दोनों S को अलग कूट-अक्षर देता है; QZBXNZZ, S को Z लिखता है, जो पहले से I के लिए है; और QZBNXMM, R को N और E को X लिखता है, यानी उलटा।",
  "lr-cd-a-substitution-code-checked-for-consistency", pos=3, check=_cd14)

# 15 -- a word reversed in halves
def _cd15():
    enc = lambda w: w[:len(w) // 2][::-1] + w[len(w) // 2:][::-1]
    assert enc("SILVER") == "LISREV"
    return enc("MARKET")
T(LR, "Coding-Decoding", "medium",
  "In a code, a word is split into two halves, and the letters of each half are written in reverse order. In this code SILVER is written as LISREV. How is MARKET written in the same code?",
  "एक कूट में किसी शब्द को दो आधों में बाँटा जाता है, और हर आधे के अक्षर उलटे क्रम में लिखे जाते हैं। इस कूट में SILVER को LISREV लिखा जाता है। उसी कूट में MARKET कैसे लिखा जाएगा?",
  ["RAMTEK", "TEKRAM", "KETMAR", "MARTEK"],
  ["RAMTEK", "TEKRAM", "KETMAR", "MARTEK"],
  0,
  "SILVER splits into SIL and VER; reversed, they give LIS and REV: LISREV, which confirms the rule. MARKET splits into MAR and KET, which reversed give RAM and TEK: RAMTEK. "
  "TEKRAM reverses the whole word; KETMAR swaps the halves without reversing them; MARTEK reverses only the second half.",
  "SILVER, SIL और VER में बँटता है; उलटने पर LIS और REV मिलते हैं: LISREV, जिससे नियम की पुष्टि होती है। MARKET, MAR और KET में बँटता है, जो उलटने पर RAM और TEK देते हैं: RAMTEK। "
  "TEKRAM पूरे शब्द को उलट देता है; KETMAR आधों को उलटे बिना अदल-बदल देता है; MARTEK केवल दूसरे आधे को उलटता है।",
  "lr-cd-a-word-reversed-in-halves", pos=1, check=_cd15)

# 16 -- an arrow seen in a mirror on the north wall
def _dd16():
    # a plane mirror on the north wall maps a point (x, y) to (x, 2w - y): the north-south part flips, east-west stays
    reflect = lambda v: (v[0], -v[1])
    east = (1, 0)
    img = reflect(east)
    names = {(1, 0): "East", (-1, 0): "West", (0, 1): "North", (0, -1): "South"}
    return names[img]
T(LR, "Direction & Distance", "hard",
  "A large mirror hangs on the north wall of a room. Ravi stands facing the mirror and holds up a card on which an arrow points east. In which direction does the arrow in the mirror's image point?",
  "एक कमरे की उत्तरी दीवार पर एक बड़ा दर्पण टँगा है। रवि दर्पण की ओर मुँह करके खड़ा है और एक कार्ड उठाता है जिस पर बना तीर पूर्व की ओर है। दर्पण के प्रतिबिंब में तीर किस दिशा की ओर है?",
  ["East", "West", "North", "South"], ["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"],
  0,
  "A flat mirror reverses only the direction at right angles to it -- here north and south, so that Ravi's image faces south, back towards him. Directions along the mirror are unchanged: an arrow pointing east, to Ravi's right, is seen in the mirror still pointing east, to Ravi's right. "
  "West is the common slip of thinking a mirror swaps left and right; north and south would need the arrow to point towards or away from the mirror.",
  "समतल दर्पण केवल अपने लंबवत दिशा को उलटता है -- यहाँ उत्तर और दक्षिण, जिससे रवि का प्रतिबिंब दक्षिण की ओर, उसी की ओर, देखता है। दर्पण के साथ-साथ की दिशाएँ नहीं बदलतीं: पूर्व, यानी रवि के दाईं ओर, इशारा करता तीर दर्पण में भी पूर्व की ओर, रवि के दाईं ओर, दिखता है। "
  "पश्चिम वह आम भूल है कि दर्पण बाएँ-दाएँ बदल देता है; उत्तर या दक्षिण के लिए तीर को दर्पण की ओर या उससे दूर इशारा करना होता।",
  "lr-dd-an-arrow-seen-in-a-mirror-on-the-north-wall", pos=1, check=_dd16)

# 17 -- a block enlarged and then painted
def _cp17():
    cells = [(x, y, z) for x in range(4) for y in range(4) for z in range(4)]
    added = [p for p in cells if max(p) == 3]                    # the original block fills 0..2 in every direction
    painted = lambda p: any(v in (0, 3) for v in p)
    bare_added = [p for p in added if not painted(p)]
    bare_all = [p for p in cells if not painted(p)]
    assert len(added) == 37 and len(bare_all) == 8 and all(max(p) < 3 for p in bare_all)
    return str(len(bare_added))
N(LR, "Cube Painting", "medium",
  "A solid block of 27 small cubes, 3 × 3 × 3, is enlarged into a 4 × 4 × 4 block by gluing new small cubes onto three of its faces that meet at one corner. The whole 4 × 4 × 4 block is then painted on the outside. How many of the newly added small cubes have no paint on them?",
  "27 छोटे घनों से बने 3 × 3 × 3 के एक ठोस खंड को, एक कोने पर मिलने वाले उसके तीन फलकों पर नए छोटे घन चिपकाकर, 4 × 4 × 4 का खंड बनाया जाता है। फिर पूरे 4 × 4 × 4 खंड को बाहर से रंगा जाता है। नए जोड़े गए छोटे घनों में से कितनों पर कोई रंग नहीं है?",
  ["0", "1", "8", "37"], 0,
  "In a 4 × 4 × 4 block only the inner 2 × 2 × 2 core, 8 cubes, escapes the paint. Those 8 sit one layer in from every face, so they all belong to the original 3 × 3 × 3 block. Every new cube lies in the outer layer on one of the three faces where cubes were added, so every one of them is painted: none is bare. "
  "37 is the number of cubes added (64 - 27); 8 is the number of unpainted cubes in the whole block, all of them old; 1 has no basis.",
  "4 × 4 × 4 खंड में केवल भीतर का 2 × 2 × 2 भाग, यानी 8 घन, रंग से बचते हैं। ये 8 हर फलक से एक परत भीतर हैं, इसलिए सभी मूल 3 × 3 × 3 खंड के हैं। हर नया घन उन तीन फलकों में से किसी की बाहरी परत में है जहाँ घन जोड़े गए, इसलिए हर एक पर रंग है: कोई भी बिना रंग का नहीं। "
  "37 जोड़े गए घनों की संख्या है (64 - 27); 8 पूरे खंड के बिना रंग वाले घन हैं, जो सभी पुराने हैं; 1 का कोई आधार नहीं।",
  "lr-cp-a-block-enlarged-and-then-painted", _cp17)

# ---- the data-sufficiency block's three Reasoning items
def _ds18():
    # positions now, under each statement: I fixes the people ahead; II speaks only of those behind
    s1 = {5 - 2}
    s2 = {5 - k for k in range(0, 5)}                # people ahead may or may not have left
    both = s1
    assert s1 == {3} and len(s2) > 1
    return _ds(s1, s2, both)
DS(LR, "medium",
   "This morning Q was fifth in a queue. What is Q's position in the queue now?",
   "आज सुबह Q एक पंक्ति में पाँचवें स्थान पर था। अब पंक्ति में Q का स्थान क्या है?",
   "Since then, two of the people ahead of Q have left the queue, and nobody has joined it ahead of Q.", "तब से Q के आगे के दो लोग पंक्ति छोड़ चुके हैं, और Q के आगे कोई नहीं जुड़ा है।",
   "Since then, one of the people behind Q has left the queue.", "तब से Q के पीछे के एक व्यक्ति ने पंक्ति छोड़ दी है।",
   0,
   "Statement I alone: Q's position depends only on how many people are ahead. Four were ahead; two have left and none have joined, so two remain ahead and Q is third. Statement II alone speaks only of people behind Q, which does not change Q's position, and says nothing about those ahead. One statement alone is enough, but not the other.",
   "कथन I अकेले: Q का स्थान केवल इस पर निर्भर है कि आगे कितने लोग हैं। चार आगे थे; दो चले गए और कोई नहीं जुड़ा, इसलिए दो आगे बचे और Q तीसरा है। कथन II अकेले केवल Q के पीछे के लोगों की बात करता है, जिससे Q का स्थान नहीं बदलता, और आगे वालों के बारे में कुछ नहीं कहता। एक कथन अकेले पर्याप्त है, पर दूसरा नहीं।",
   "lr-ds-a-place-in-a-queue-after-people-leave", _ds18)

def _ds19():
    worlds = [dict(zip("PQR", p)) for p in permutations(["red", "green", "blue"])]
    i1 = lambda w: w["P"] != "red" and w["Q"] == "red"
    i2 = lambda w: w["R"] == "blue"
    s1 = {w["P"] for w in worlds if i1(w)}
    s2 = {w["P"] for w in worlds if i2(w)}
    both = {w["P"] for w in worlds if i1(w) and i2(w)}
    assert both == {"green"}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Three boxes, P, Q and R, are painted red, green and blue, one colour to each box. What colour is box P?",
   "तीन डिब्बे, P, Q और R, लाल, हरे और नीले रंग में रंगे हैं, हर डिब्बे का एक रंग। डिब्बा P किस रंग का है?",
   "P is not red, and Q is red.", "P लाल नहीं है, और Q लाल है।",
   "R is blue.", "R नीला है।",
   2,
   "Statement I alone leaves P green or blue. Statement II alone leaves P red or green. Together, red goes to Q and blue to R, so P is green. Both statements are needed.",
   "कथन I अकेले P को हरा या नीला छोड़ता है। कथन II अकेले P को लाल या हरा छोड़ता है। दोनों मिलकर, लाल Q को और नीला R को जाता है, इसलिए P हरा है। दोनों कथन आवश्यक हैं।",
   "lr-ds-three-boxes-in-three-colours", _ds19)

def _ds20():
    s1, s2, both = set(), set(), set()
    for filled in _venn(3):                          # (pen, red, cheap)
        if not filled:
            continue
        i1 = not any(r and not ch for p, r, ch in filled)            # all red things are cheap
        i2 = any(p and ch for p, r, ch in filled)                    # some pens are cheap
        ans = any(p and r for p, r, ch in filled)                    # are some pens red?
        if i1: s1.add(ans)
        if i2: s2.add(ans)
        if i1 and i2: both.add(ans)
    assert s1 == s2 == both == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Are some pens red?",
   "क्या कुछ पेन लाल हैं?",
   "All red things are cheap.", "सभी लाल वस्तुएँ सस्ती हैं।",
   "Some pens are cheap.", "कुछ पेन सस्ते हैं।",
   3,
   "Statement I alone says nothing about pens. Statement II alone says nothing about red things. Together they put some pens among cheap things and all red things among cheap things, but the cheap pens and the cheap red things may be quite different things: the pens could all be blue. So even together they do not settle the question.",
   "कथन I अकेले पेनों के बारे में कुछ नहीं कहता। कथन II अकेले लाल वस्तुओं के बारे में कुछ नहीं कहता। दोनों मिलकर कुछ पेनों को सस्ती वस्तुओं में और सभी लाल वस्तुओं को सस्ती वस्तुओं में रखते हैं, पर सस्ते पेन और सस्ती लाल वस्तुएँ बिल्कुल अलग हो सकती हैं: सभी पेन नीले हो सकते हैं। अतः दोनों मिलकर भी प्रश्न तय नहीं करते।",
   "lr-ds-pens-that-may-or-may-not-be-red", _ds20)
