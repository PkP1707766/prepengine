# -*- coding: utf-8 -*-
"""Level 3 Tests 1 and 3: replace the drafts that the whole-bank overlap scan (l3_tools/overlap_scan.py, 2026-10-24)
found repeating facts already tested elsewhere in the UPSC bank. The module sources (gs_l3_t1_*.py, gs_l3_t3_e.py) are
edited in place so they stay the source of truth, and this script writes fix_l3_t1_t3_repeats.sql, which rewrites the
draft rows in place (write_updates), keeping each row's topic, type, difficulty and answer letter.

  l3-t1-pol-part-xiii-trade-301-304   repeated fed-trade-commerce-301-304 (L2)      -> Jindal Stainless (2016) on taxes
  l3-t1-his-ina-red-fort-trial        repeated modern-ina-azad-hind (L2)            -> Sister Nivedita and Vivekananda
  l3-t1-his-rin-ratings-revolt-1946   repeated modern-vellore-barrackpore-rin-...   -> the Hindu Mela
  l3-t1-env-arctic-amplification-...  repeated env-arctic-amplification (L2)        -> ice cores
  l3-t1-eco-critical-mineral-mission  repeated en-critical-minerals (L2)            -> twelve industrial smart cities
  l3-t1-sci-green-ammonia-carrier     statement 1 restated env-hydrogen-colours     -> ammonia 'cracking' (same row id)
  l3-t3-eco-schemes-dajgua-...        pair 3 restated gov-poshan-mission-shakti-... -> Swachh Bharat Mission (Grameen)
"""
import contextlib, importlib, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "l3_tools"))
from swap_block import swap as _swap

def swap(mod, cg, new):
    # Idempotent: skip when the old concept id is gone (the swap was applied on an earlier run).
    if '"' + cg + '"' not in io.open(os.path.join(HERE, mod), encoding="utf-8").read():
        print("already swapped", cg); return
    _swap(mod, cg, new)

swap("gs_l3_t1_a.py", "l3-t1-pol-part-xiii-trade-301-304", '''
S("Federalism & Special Provisions", "medium", "With reference to the Supreme Court's nine-judge decision in Jindal Stainless Ltd. v. State of Haryana (2016), consider the following statements:",
  "जिंदल स्टेनलेस लिमिटेड बनाम हरियाणा राज्य (2016) में सर्वोच्च न्यायालय के नौ न्यायाधीशों के निर्णय के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It held that a non-discriminatory tax is not, by itself, a restriction on the freedom of trade guaranteed by Article 301.",
   "It held that every State tax on goods entering from another State needs the President's previous sanction.",
   "After the judgment, the States lost all power to levy an entry tax on goods."],
  ["इसने माना कि भेदभाव-रहित कर अपने-आप में अनुच्छेद 301 द्वारा प्रत्याभूत व्यापार की स्वतंत्रता पर प्रतिबंध नहीं है।",
   "इसने माना कि दूसरे राज्य से आने वाली वस्तुओं पर हर राज्य-कर के लिए राष्ट्रपति की पूर्व मंज़ूरी चाहिए।",
   "इस निर्णय के बाद राज्यों ने वस्तुओं पर प्रवेश-कर लगाने की सारी शक्ति खो दी।"],
  C3, 0,
  "Only statement 1 is correct. States had long levied entry taxes on goods brought in from other States, and traders argued that these hit the freedom of trade in Article 301 unless they were 'compensatory' or cleared under Article 304(b). The nine-judge bench rejected the compensatory-tax test and held that taxes are not, as such, restrictions on trade; only a tax that discriminates against goods from other States, in favour of local goods, offends Article 304(a). "
  "Statements 2 and 3 are wrong: a non-discriminatory entry tax needed no presidential sanction, so the States kept the power, and the cases on whether particular levies were discriminatory went back to regular benches. Entry taxes were later subsumed into the GST in 2017.",
  "केवल कथन 1 सही है। राज्य लंबे समय से दूसरे राज्यों से लाई गई वस्तुओं पर प्रवेश-कर लगाते रहे थे, और व्यापारियों का तर्क था कि जब तक वे 'प्रतिपूरक' न हों या अनुच्छेद 304(ख) के अंतर्गत स्वीकृत न हों, वे अनुच्छेद 301 की व्यापार-स्वतंत्रता पर चोट करते हैं। नौ न्यायाधीशों की पीठ ने प्रतिपूरक-कर की कसौटी ख़ारिज की और माना कि कर अपने-आप में व्यापार पर प्रतिबंध नहीं हैं; केवल वही कर अनुच्छेद 304(क) का उल्लंघन करता है जो स्थानीय वस्तुओं के पक्ष में दूसरे राज्यों की वस्तुओं से भेदभाव करे। "
  "कथन 2 और 3 ग़लत हैं: भेदभाव-रहित प्रवेश-कर के लिए राष्ट्रपति की मंज़ूरी आवश्यक नहीं थी, इसलिए राज्यों की शक्ति बनी रही, और कोई विशेष कर भेदभावपूर्ण है या नहीं, इसके मामले सामान्य पीठों को लौटाए गए। बाद में 2017 में प्रवेश-कर GST में समाहित हो गए।",
  f"{SC}: Jindal Stainless Ltd. v. State of Haryana (2016); {COI}, Articles 301 and 304.",
  "l3-t1-pol-jindal-stainless-entry-tax", craft="precision")
''')

swap("gs_l3_t1_b.py", "l3-t1-his-ina-red-fort-trial", '''
M("Modern", "easy",
  "Sister Nivedita, the Irish-born educationist who opened a school for girls in Calcutta and wrote on Indian art and nationalism, was a disciple of:",
  "आयरलैंड में जन्मी शिक्षाविद् भगिनी निवेदिता, जिन्होंने कलकत्ता में लड़कियों का विद्यालय खोला और भारतीय कला तथा राष्ट्रवाद पर लिखा, किनकी शिष्या थीं?",
  ["Ramakrishna Paramahamsa", "Dayananda Saraswati", "Annie Besant", "Swami Vivekananda"],
  ["रामकृष्ण परमहंस", "दयानंद सरस्वती", "एनी बेसेंट", "स्वामी विवेकानंद"],
  3,
  "Margaret Noble met Vivekananda in London in 1895, came to India in 1898 and was given the name Nivedita, 'the dedicated', when he initiated her; she opened a girls' school in Bagbazar, nursed the sick during the plague of 1899, encouraged scientists such as J.C. Bose and artists of the Bengal school, and became an influential voice of nationalism during the Swadeshi years. "
  "Ramakrishna was Vivekananda's own teacher, who died in 1886; Dayananda founded the Arya Samaj; and Annie Besant led the Theosophical Society and the Home Rule movement.",
  "मार्गरेट नोबल 1895 में लंदन में विवेकानंद से मिलीं, 1898 में भारत आईं और जब उन्होंने उन्हें दीक्षा दी तो उन्हें 'समर्पित' अर्थ वाला नाम निवेदिता मिला; उन्होंने बागबाज़ार में लड़कियों का विद्यालय खोला, 1899 के प्लेग में बीमारों की सेवा की, जे.सी. बोस जैसे वैज्ञानिकों और बंगाल शैली के कलाकारों को प्रोत्साहित किया, और स्वदेशी वर्षों में राष्ट्रवाद की प्रभावशाली आवाज़ बनीं। "
  "रामकृष्ण विवेकानंद के अपने गुरु थे, जिनकी 1886 में मृत्यु हुई; दयानंद ने आर्य समाज की स्थापना की; और एनी बेसेंट ने थियोसोफ़िकल सोसाइटी और होम रूल आंदोलन का नेतृत्व किया।",
  MOD + "; Ramakrishna Mission.",
  "l3-t1-his-sister-nivedita", pos=3, craft="recall")
''')

swap("gs_l3_t1_b.py", "l3-t1-his-rin-ratings-revolt-1946", '''
S("Modern", "easy", "Consider the following statements about the Hindu Mela:",
  "हिंदू मेले के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was started in Calcutta in 1867, with the support of the Tagore family, to foster national pride and Indian crafts and industry.",
   "As a boy, Rabindranath Tagore recited a patriotic poem of his own at one of its gatherings."],
  ["इसे 1867 में कलकत्ता में, टैगोर परिवार के सहयोग से, राष्ट्रीय गौरव और भारतीय शिल्प तथा उद्योग को बढ़ावा देने के लिए शुरू किया गया।",
   "बालक के रूप में रवींद्रनाथ टैगोर ने इसके एक आयोजन में अपनी एक देशभक्ति कविता का पाठ किया।"],
  T2, 2,
  "Both statements are correct. The Hindu Mela, organised by Nabagopal Mitra with Dwijendranath and Ganendranath Tagore among its patrons, held annual gatherings with exhibitions of Indian crafts, wrestling and patriotic songs, and urged self-help in industry and education decades before the Swadeshi movement; in 1875 the fourteen-year-old Rabindranath recited a poem there, one of his first public appearances. "
  "Historians treat it as an early sign of the cultural nationalism that later shaped the Indian Association and the Congress in Bengal.",
  "दोनों कथन सही हैं। नवगोपाल मित्र द्वारा आयोजित हिंदू मेला, जिसके संरक्षकों में द्विजेंद्रनाथ और गणेंद्रनाथ टैगोर थे, भारतीय शिल्पों की प्रदर्शनियों, कुश्ती और देशभक्ति गीतों के साथ वार्षिक आयोजन करता था, और स्वदेशी आंदोलन से दशकों पहले उद्योग और शिक्षा में आत्मनिर्भरता का आग्रह करता था; 1875 में चौदह वर्षीय रवींद्रनाथ ने वहाँ एक कविता पढ़ी, जो उनकी पहली सार्वजनिक उपस्थितियों में से एक थी। "
  "इतिहासकार इसे उस सांस्कृतिक राष्ट्रवाद का आरंभिक संकेत मानते हैं जिसने बाद में बंगाल में इंडियन एसोसिएशन और कांग्रेस को आकार दिया।",
  MOD + ".",
  "l3-t1-his-hindu-mela-1867", craft="recall")
''')

swap("gs_l3_t1_c.py", "l3-t1-env-arctic-amplification-albedo", '''
M("Climate Science & Mitigation", "medium",
  "Ice cores drilled from the Antarctic and Greenland ice sheets are especially valuable to climate scientists mainly because:",
  "अंटार्कटिक और ग्रीनलैंड की हिम-चादरों से निकाले गए बर्फ़ के कोर (आइस कोर) जलवायु वैज्ञानिकों के लिए विशेष रूप से मूल्यवान क्यों हैं?",
  ["they hold microbes from past ages whose decay rates are used to date volcanic eruptions on other continents",
   "they record the eleven-year sunspot cycle through changes in the thickness of each winter's snow layer",
   "bubbles in them preserve samples of past air, showing greenhouse-gas levels over many millennia",
   "their temperature at depth shows directly how warm the oceans were at each period of the past"],
  ["उनमें पिछले युगों के सूक्ष्मजीव होते हैं जिनकी क्षय-दर से दूसरे महाद्वीपों के ज्वालामुखी विस्फोटों की तिथि तय होती है",
   "वे हर सर्दी की हिम-परत की मोटाई में परिवर्तन के माध्यम से ग्यारह-वर्षीय सौर-कलंक चक्र को दर्ज करते हैं",
   "उनके बुलबुलों में पिछली हवा के नमूने बचे रहते हैं, जो हज़ारों वर्षों के ग्रीनहाउस-गैस स्तर दिखाते हैं",
   "गहराई पर उनका तापमान सीधे बताता है कि अतीत के हर काल में महासागर कितने गर्म थे"],
  2,
  "As snow piles up and is compressed into ice, it seals in small pockets of the atmosphere of the time, so analysing the bubbles gives carbon dioxide and methane levels going back about 800,000 years in Antarctic cores; the ratio of oxygen or hydrogen isotopes in the ice itself shows past temperatures, and layers of ash and dust mark eruptions and dry, windy periods. "
  "These records show that carbon dioxide and temperature rose and fell together through the ice-age cycles, and that today's level -- above 420 parts per million -- is far higher than anything in that span, which is why ice cores are central evidence in assessments of human-caused warming.",
  "जब बर्फ़ जमा होकर दबती हुई हिम बनती है, तो वह उस समय के वायुमंडल की छोटी जेबों को बंद कर लेती है, इसलिए बुलबुलों के विश्लेषण से अंटार्कटिक कोरों में लगभग 8,00,000 वर्ष पीछे तक के कार्बन डाइऑक्साइड और मीथेन स्तर मिलते हैं; स्वयं बर्फ़ में ऑक्सीजन या हाइड्रोजन समस्थानिकों का अनुपात पिछले तापमान बताता है, और राख तथा धूल की परतें विस्फोटों और शुष्क, आँधी वाले कालों को चिह्नित करती हैं। "
  "ये अभिलेख दिखाते हैं कि हिमयुग-चक्रों में कार्बन डाइऑक्साइड और तापमान साथ-साथ चढ़ते-उतरते रहे, और आज का स्तर -- 420 भाग प्रति दस लाख से ऊपर -- उस पूरी अवधि के किसी भी स्तर से कहीं ऊँचा है, इसीलिए मानव-जनित तापन के आकलनों में आइस कोर केंद्रीय साक्ष्य हैं।",
  IPCC + " (paleoclimate assessment); National Centre for Polar and Ocean Research.",
  "l3-t1-env-ice-cores-past-air", pos=2, craft="inference")
''')

swap("gs_l3_t1_e.py", "l3-t1-eco-critical-mineral-mission", '''
S("Industry, Infrastructure, Energy & Services", "medium", "Consider the following statements about the industrial smart cities approved in 2024:",
  "2024 में स्वीकृत औद्योगिक स्मार्ट शहरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Twelve of them were approved under the National Industrial Corridor Development Programme.",
   "They are planned as 'plug-and-play' sites, with land and infrastructure ready before investors arrive.",
   "They are located only in coastal States, so that their output can be exported easily."],
  ["इनमें से बारह को राष्ट्रीय औद्योगिक गलियारा विकास कार्यक्रम के अंतर्गत स्वीकृति दी गई।",
   "इन्हें 'प्लग-एंड-प्ले' स्थलों के रूप में नियोजित किया गया है, जहाँ निवेशकों के आने से पहले भूमि और बुनियादी ढाँचा तैयार रहे।",
   "ये केवल तटीय राज्यों में स्थित हैं, ताकि इनका उत्पादन आसानी से निर्यात हो सके।"],
  C3, 1,
  "Statements 1 and 2 are correct. In August 2024 the Union Cabinet approved twelve greenfield industrial cities along the industrial corridors, developed by the National Industrial Corridor Development and Implementation Trust with the States, which provide the land; the aim is to cut the time and uncertainty of land acquisition and approvals by offering developed plots, utilities and connectivity in advance. "
  "Statement 3 is wrong: the sites are spread across ten States, many of them inland -- among them Agra and Prayagraj in Uttar Pradesh, Gaya in Bihar, Jodhpur-Pali in Rajasthan, Zaheerabad in Telangana and Khurpia in Uttarakhand -- because the corridors follow freight routes and dedicated freight corridors as much as the coast.",
  "कथन 1 और 2 सही हैं। अगस्त 2024 में केंद्रीय मंत्रिमंडल ने औद्योगिक गलियारों के साथ बारह ग्रीनफ़ील्ड औद्योगिक शहरों को स्वीकृति दी, जिन्हें राष्ट्रीय औद्योगिक गलियारा विकास और कार्यान्वयन ट्रस्ट राज्यों के साथ विकसित करता है, और राज्य भूमि देते हैं; उद्देश्य पहले से विकसित भूखंड, उपयोगिताएँ और संपर्क देकर भूमि-अधिग्रहण और स्वीकृतियों का समय और अनिश्चितता घटाना है। "
  "कथन 3 ग़लत है: ये स्थल दस राज्यों में फैले हैं, उनमें से कई अंतर्देशीय -- जैसे उत्तर प्रदेश में आगरा और प्रयागराज, बिहार में गया, राजस्थान में जोधपुर-पाली, तेलंगाना में ज़हीराबाद और उत्तराखंड में खुरपिया -- क्योंकि गलियारे तट के साथ-साथ माल-मार्गों और समर्पित माल गलियारों का भी अनुसरण करते हैं।",
  "Department for Promotion of Industry and Internal Trade: National Industrial Corridor Development Programme (Cabinet decision, August 2024).",
  "l3-t1-eco-industrial-smart-cities-2024", craft="linkage")
''')

# Green ammonia: replace statement 1 (it restated the green-hydrogen definition tested in env-hydrogen-colours).
p = os.path.join(HERE, "gs_l3_t1_f.py")
s = io.open(p, encoding="utf-8").read()
reps = [
 ('"It is made by combining hydrogen produced by electrolysis using renewable electricity with nitrogen drawn from the air."',
  '"Where hydrogen itself is needed, ammonia can be \'cracked\' back into hydrogen and nitrogen."'),
]
reps += [
 ('"यह नवीकरणीय बिजली से विद्युत-अपघटन द्वारा बने हाइड्रोजन को हवा से ली गई नाइट्रोजन के साथ मिलाकर बनाई जाती है।"',
  '"जहाँ स्वयं हाइड्रोजन चाहिए, वहाँ अमोनिया को फिर से हाइड्रोजन और नाइट्रोजन में तोड़ा (‘क्रैक’ किया) जा सकता है।"'),
]
for a, b in reps:
    if s.count(a) == 0 and s.count(b) == 1: continue   # already applied
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
io.open(p, "w", encoding="utf-8").write(s)
print("green ammonia statement 1 replaced")

# Scheme pairs (T3): pair 3 restated the PMMVY-under-Mission-Shakti fact of gov-poshan-mission-shakti-pmjay.
p = os.path.join(HERE, "gs_l3_t3_e.py")
s = io.open(p, encoding="utf-8").read()
reps = [
 ('"Pradhan Mantri Matru Vandana Yojana : Ministry of Health and Family Welfare",', '"Swachh Bharat Mission (Grameen) : Ministry of Housing and Urban Affairs",'),
 ('"प्रधानमंत्री मातृ वंदना योजना : स्वास्थ्य और परिवार कल्याण मंत्रालय",', '"स्वच्छ भारत मिशन (ग्रामीण) : आवासन और शहरी कार्य मंत्रालय",'),
 ("The third pair is wrong: the Matru Vandana Yojana, which pays pregnant women and nursing mothers a cash incentive to make up for lost wages and encourage health care, is run by the Ministry of Women and Child Development.",
  "The third pair is wrong: the rural arm of the Swachh Bharat Mission, which built household toilets and now works on solid and liquid waste in villages, is run by the Department of Drinking Water and Sanitation in the Ministry of Jal Shakti; the Ministry of Housing and Urban Affairs runs the urban mission."),
 ("तीसरा युग्म ग़लत है: गर्भवती महिलाओं और स्तनपान कराने वाली माताओं को खोई मज़दूरी की भरपाई और स्वास्थ्य देखभाल के लिए नक़द प्रोत्साहन देने वाली मातृ वंदना योजना महिला और बाल विकास मंत्रालय चलाता है।",
  "तीसरा युग्म ग़लत है: स्वच्छ भारत मिशन की ग्रामीण शाखा, जिसने घरेलू शौचालय बनवाए और अब गाँवों में ठोस और तरल अपशिष्ट पर काम करती है, जल शक्ति मंत्रालय का पेयजल और स्वच्छता विभाग चलाता है; आवासन और शहरी कार्य मंत्रालय शहरी मिशन चलाता है।"),
 ('"Ministry of Tribal Affairs; Ministry of Social Justice and Empowerment; Ministry of Women and Child Development.",',
  '"Ministry of Tribal Affairs; Ministry of Social Justice and Empowerment; Ministry of Jal Shakti (Department of Drinking Water and Sanitation).",'),
 ('"l3-t3-eco-schemes-dajgua-sugamya-pmmvy-pmajay"', '"l3-t3-eco-schemes-dajgua-sugamya-sbmg-pmajay"'),
]
for a, b in reps:
    if s.count(a) == 0 and s.count(b) == 1: continue   # already applied
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
io.open(p, "w", encoding="utf-8").write(s)
print("scheme pair 3 replaced")

# The rewrite SQL: load the edited modules and rewrite the affected drafts in place.
import draft_common as d
NEW = {  # new concept id -> old concept id
  "l3-t1-pol-jindal-stainless-entry-tax": "l3-t1-pol-part-xiii-trade-301-304",
  "l3-t1-his-sister-nivedita": "l3-t1-his-ina-red-fort-trial",
  "l3-t1-his-hindu-mela-1867": "l3-t1-his-rin-ratings-revolt-1946",
  "l3-t1-env-ice-cores-past-air": "l3-t1-env-arctic-amplification-albedo",
  "l3-t1-eco-industrial-smart-cities-2024": "l3-t1-eco-critical-mineral-mission",
  "l3-t1-sci-green-ammonia-carrier": "l3-t1-sci-green-ammonia-carrier",
  "l3-t3-eco-schemes-dajgua-sugamya-sbmg-pmajay": "l3-t3-eco-schemes-dajgua-sugamya-pmmvy-pmajay",
}
real_write = d.write
keep = []
for m in ["gs_l3_t1_a", "gs_l3_t1_b", "gs_l3_t1_c", "gs_l3_t1_e", "gs_l3_t1_f", "gs_l3_t3_e"]:
    d.ROWS.clear(); d.CGS.clear(); d.CELLS.clear(); d.SPREAD.clear(); d._mcq_n[0] = 0
    d.write = lambda name: None
    with contextlib.redirect_stdout(io.StringIO()):
        mod = importlib.import_module(m)
    subject = d.SUBJECT
    for r in d.ROWS:
        if r["concept_group_id"] in NEW:
            keep.append((subject, r))
d.write = real_write
assert len(keep) == len(NEW), len(keep)
# write_updates uses one SUBJECT per file, so emit one statement block per subject and join them.
stmts = []
for subject in sorted({s for s, _ in keep}):
    d.ROWS.clear(); d.SUBJECT = subject
    d.ROWS.extend(r for s, r in keep if s == subject)
    tmp = f"_fix_tmp_{abs(hash(subject))}.sql"
    with contextlib.redirect_stdout(io.StringIO()):
        d.write_updates(tmp, replaces={k: v for k, v in NEW.items()})
    body = io.open(os.path.join(HERE, tmp), encoding="utf-8").read().replace("begin;\n", "").replace("commit;\n", "")
    stmts.append(body.strip())
    os.remove(os.path.join(HERE, tmp)); os.remove(os.path.join(HERE, tmp.replace(".sql", "_cgs.json")))
io.open(os.path.join(HERE, "fix_l3_t1_t3_repeats.sql"), "w", encoding="utf-8", newline="\n").write("begin;\n" + "\n".join(stmts) + "\ncommit;\n")
print("wrote fix_l3_t1_t3_repeats.sql with", len(keep), "row rewrites")

