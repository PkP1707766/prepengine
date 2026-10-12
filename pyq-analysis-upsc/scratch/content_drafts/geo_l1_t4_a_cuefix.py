# -*- coding: utf-8 -*-
"""Level 1 Test 4, part A -- cue fixes found by the whole-paper scan (l1_check.py 4 geo_l1_t4 l1-geo-), applied to
geo_l1_t4_a.py before insertion:
- l1-geo-temperate-evergreen-deciduous-taiga: statement 2 placed temperate forests between the Tropics, which the
  word 'temperate' and the heat-zones item (part B) gave away. It now tests the tree species instead (teak, sal and
  sandalwood belong to the tropical deciduous forests). Level 2 already uses the 'shed leaves in the dry season' trap.
- l1-geo-water-vapour-dust-nuclei: statement 3 (vapour increases towards the poles) was contradicted by statement 1
  of the same item. It now tests whether water vapour absorbs insolation.
Keys are unchanged (Only one; Only two)."""
import io, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_l1_t4_a.py")
s = io.open(P, encoding="utf-8").read()
REPS = [
    ('"Temperate deciduous forests are found mainly in the belt between the Tropic of Cancer and the Tropic of Capricorn."',
     '"Temperate deciduous forests, as in north-eastern USA and western Europe, consist mainly of teak, sal and sandalwood."'),
    ('"शीतोष्ण पर्णपाती वन मुख्यतः कर्क रेखा और मकर रेखा के बीच की पट्टी में मिलते हैं।"',
     '"उत्तर-पूर्वी अमेरिका और पश्चिमी यूरोप जैसे क्षेत्रों के शीतोष्ण पर्णपाती वनों में मुख्यतः सागौन, साल और चंदन के वृक्ष होते हैं।"'),
    ("Statement 2 is wrong: temperate deciduous forests lie towards higher latitudes -- in north-eastern USA, China, New Zealand, Chile and the coastal regions of western Europe -- with oak, ash and beech, and animals such as deer, foxes and wolves. ",
     "Statement 2 is wrong: teak, sal and sandalwood are trees of the tropical deciduous (monsoon) forests, as in India; the temperate deciduous forests, further towards the poles in north-eastern USA, China, New Zealand, Chile and the coastal regions of western Europe, have oak, ash and beech, and animals such as deer, foxes and wolves. "),
    ("कथन 2 गलत है: शीतोष्ण पर्णपाती वन ऊँचे अक्षांशों की ओर हैं -- उत्तर-पूर्वी अमेरिका, चीन, न्यूज़ीलैंड, चिली और पश्चिमी यूरोप के तटीय क्षेत्रों में -- जिनमें बलूत, ऐश और बीच वृक्ष, तथा हिरण, लोमड़ी और भेड़िये जैसे जंतु हैं। ",
     "कथन 2 गलत है: सागौन, साल और चंदन उष्णकटिबंधीय पर्णपाती (मानसूनी) वनों के वृक्ष हैं, जैसे भारत में; ध्रुवों की ओर उत्तर-पूर्वी अमेरिका, चीन, न्यूज़ीलैंड, चिली और पश्चिमी यूरोप के तटीय क्षेत्रों में स्थित शीतोष्ण पर्णपाती वनों में बलूत, ऐश और बीच वृक्ष, तथा हिरण, लोमड़ी और भेड़िये जैसे जंतु हैं। "),
    ('"The water vapour content of the air increases from the Equator towards the poles."',
     '"Water vapour lets all incoming solar radiation pass through, and traps only the heat radiated by the Earth."'),
    ('"हवा में जलवाष्प की मात्रा विषुवत रेखा से ध्रुवों की ओर बढ़ती है।"',
     '"जलवाष्प आने वाले सभी सौर विकिरण को आर-पार जाने देती है, और केवल पृथ्वी द्वारा विकिरित ऊष्मा को रोकती है।"'),
    ("Statements 1 and 2 are correct. Water vapour, though a small and variable part of the air, absorbs part of the insolation and preserves the heat radiated by the Earth, and is the source of all clouds and precipitation; ",
     "Statements 1 and 2 are correct. Water vapour, though a small and variable part of the air, is the source of all clouds and precipitation; "),
    ("Statement 3 is wrong: water vapour decreases from the Equator towards the poles, as it also does with altitude, because colder air can hold less of it.",
     "Statement 3 is wrong: water vapour absorbs part of the insolation as well as preserving the heat radiated by the Earth, acting like a blanket that keeps the Earth from becoming too hot or too cold; its share falls from the Equator towards the poles and with altitude, because colder air can hold less of it."),
    ("कथन 1 और 2 सही हैं। जलवाष्प, यद्यपि हवा का एक छोटा और परिवर्तनशील भाग है, सूर्यातप का एक भाग सोखती है और पृथ्वी से विकिरित ऊष्मा को रोके रखती है, और सारे बादलों तथा वर्षण का स्रोत है; ",
     "कथन 1 और 2 सही हैं। जलवाष्प, यद्यपि हवा का एक छोटा और परिवर्तनशील भाग है, सारे बादलों तथा वर्षण का स्रोत है; "),
    ("कथन 3 गलत है: जलवाष्प विषुवत रेखा से ध्रुवों की ओर घटती है, जैसे ऊँचाई के साथ भी घटती है, क्योंकि ठंडी हवा उसे कम धारण कर सकती है।",
     "कथन 3 गलत है: जलवाष्प पृथ्वी से विकिरित ऊष्मा को रोके रखने के साथ-साथ सूर्यातप का एक भाग भी सोखती है, और कंबल की तरह पृथ्वी को न बहुत गर्म होने देती है न बहुत ठंडी; इसका अनुपात विषुवत रेखा से ध्रुवों की ओर और ऊँचाई के साथ घटता है, क्योंकि ठंडी हवा उसे कम धारण कर सकती है।"),
]
for a, b in REPS:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("geo_l1_t4_a.py: 2 items re-worded")
