# -*- coding: utf-8 -*-
"""History audit rewrite, part 1: Ancient India.

The 2026-09-28 audit (docs/upsc-bank-audit-2026-09-28.md) found that many of the
earliest History rows could be answered without knowing the history:
- a planted false statement that announced itself ("without dispute among
  historians", "caused entirely by a single factor", "exclusively Buddhist");
- statements that contradicted each other, so one had to be false;
- school-level one-liners ("Who founded the Mauryan Empire?");
- the pre-2020 "A-2, B-1, C-4, D-3" code format, which UPSC has replaced with
  "How many of the pairs given above are correctly matched?".
Each row below is rewritten in place (same id), with the planted error now a
plausible, specific fact a student must actually know, and with Hindi. No row here
is in a published test.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from bilingual import options_json, rewrite_sql, combo_hi, CLOSING_HI, CONSIDER_HI
from polity_common import C3, C4, T2, P4, P3, HOW_MANY, WHICH, PAIRS

OUT = []
TALLY = {}

def _t(key):
    TALLY[key] = TALLY.get(key, 0) + 1

def S(fid, topic, diff, body, body_hi, st, st_hi, ladder, ans, expl, expl_hi, cite, cg, roman=False):
    closing = WHICH if ladder is T2 else HOW_MANY
    qd = {"statements": st, "statements_hi": st_hi, "closing": closing, "closing_hi": CLOSING_HI[closing], "fixed_option_order": True}
    if roman:
        qd["numbering"] = "roman"
    OUT.append(rewrite_sql(fid, topic=topic, typ="statement_based", diff=diff, body=body, body_hi=body_hi, qd=qd,
                           options=options_json(ladder, ans), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t(f"stmt:{len(st)}:{ladder[ans]}")

def M(fid, topic, diff, body, body_hi, opts, opts_hi, ans, expl, expl_hi, cite, cg, qd=None):
    OUT.append(rewrite_sql(fid, topic=topic, typ="mcq", diff=diff, body=body, body_hi=body_hi, qd=qd or {},
                           options=options_json(opts, ans, opts_hi), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t("mcq")

def P(fid, topic, diff, body, body_hi, pairs_en, pairs_hi, ans, expl, expl_hi, cite, cg):
    """pairs_en / pairs_hi: 'left : right' strings, split into the List-I and List-II columns
    the exam screen draws (the same shape as every existing pairs row)."""
    ladder = P4 if len(pairs_en) == 4 else P3
    assert len(pairs_en) == len(pairs_hi) and len(pairs_en) in (3, 4)
    sp = lambda xs: [tuple(y.strip() for y in x.split(" : ")) for x in xs]
    en, hi = sp(pairs_en), sp(pairs_hi)
    assert all(len(t) == 2 for t in en + hi), "every pair needs exactly one ' : '"
    qd = {"list_1": [f"{i + 1}. {a}" for i, (a, _) in enumerate(en)], "list_1_hi": [f"{i + 1}. {a}" for i, (a, _) in enumerate(hi)],
          "list_2": [b for _, b in en], "list_2_hi": [b for _, b in hi], "closing": PAIRS, "closing_hi": CLOSING_HI[PAIRS], "fixed_option_order": True}
    OUT.append(rewrite_sql(fid, topic=topic, typ="match_the_following", diff=diff, body=body, body_hi=body_hi, qd=qd,
                           options=options_json(ladder, ans), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t(f"pairs:{ladder[ans]}")

SHARMA = "R.S. Sharma, India's Ancient Past"
THEMES1 = "NCERT Class XII, Themes in Indian History Part I"
ART = "NCERT Class XI, An Introduction to Indian Art (Part I)"

# ---------------------------------------------------------------------------------------
S("0a890c67-bd87-4a92-9d77-f553ece3b9d4", "Ancient", "medium",
  "Consider the following statements regarding Pallava and Chalukya temple architecture:",
  "पल्लव और चालुक्य मंदिर स्थापत्य के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Pallavas are credited with the transition from rock-cut to structural stone temples, exemplified by the Shore Temple at Mahabalipuram.",
   "The Kailasanatha temple at Kanchipuram was built by the Pallava ruler Narasimhavarman I.",
   "At Pattadakal, the Chalukyas of Badami built temples in both the Nagara and the Dravida styles."],
  ["चट्टान काटकर बनाए गए मंदिरों से पत्थर जोड़कर बनाए गए संरचनात्मक मंदिरों की ओर बदलाव का श्रेय पल्लवों को दिया जाता है, जिसका उदाहरण महाबलीपुरम का तट मंदिर (Shore Temple) है।",
   "कांचीपुरम के कैलासनाथ मंदिर का निर्माण पल्लव शासक नरसिंहवर्मन प्रथम ने करवाया था।",
   "पट्टदकल में बादामी के चालुक्यों ने नागर और द्रविड़, दोनों शैलियों के मंदिर बनवाए।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Pallavas moved from the rock-cut rathas and mandapas of Mamallapuram to free-standing structural temples such as the Shore Temple. "
  "Statement 2 is incorrect: the Kailasanatha temple at Kanchipuram was built by Narasimhavarman II (Rajasimha) in the early 8th century; Narasimhavarman I (Mamalla) is linked with the rock-cut monuments of Mamallapuram. "
  "Statement 3 is correct: Pattadakal has Dravida temples such as the Virupaksha and Mallikarjuna alongside Nagara temples such as the Galaganatha and Kashivishvanatha, which is why the site is studied as a meeting point of the two styles.",
  "कथन 1 और 3 सही हैं। पल्लव महाबलीपुरम के चट्टान काटकर बने रथों और मंडपों से आगे बढ़कर तट मंदिर जैसे स्वतंत्र संरचनात्मक मंदिरों तक पहुँचे। "
  "कथन 2 गलत है: कांचीपुरम का कैलासनाथ मंदिर 8वीं शताब्दी के आरंभ में नरसिंहवर्मन द्वितीय (राजसिंह) ने बनवाया था; नरसिंहवर्मन प्रथम (मामल्ल) का संबंध महाबलीपुरम के चट्टान काटकर बने स्मारकों से है। "
  "कथन 3 सही है: पट्टदकल में विरूपाक्ष और मल्लिकार्जुन जैसे द्रविड़ शैली के मंदिरों के साथ गलगनाथ और काशीविश्वनाथ जैसे नागर शैली के मंदिर भी हैं, इसीलिए इस स्थल को दोनों शैलियों का संगम माना जाता है।",
  f"{ART} -- temple architecture and sculpture; UNESCO World Heritage List: Group of Monuments at Mahabalipuram (1984) and at Pattadakal (1987).",
  "ancient-pallava-chalukya-architecture")

S("a4017ff9-250d-434c-9f1e-575eaa422a1e", "Ancient", "medium",
  "Consider the following statements regarding the Later Vedic period:",
  "उत्तर वैदिक काल के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Iron came into use during this period, and the texts refer to it as 'shyama ayas' or 'krishna ayas'.",
   "The popular assemblies, the sabha and the samiti, grew in importance in this period, and women continued to attend the sabha.",
   "Coins called 'nishka' were the usual medium of everyday exchange in this period."],
  ["इस काल में लोहे का प्रयोग शुरू हुआ और ग्रंथों में इसे 'श्याम अयस' या 'कृष्ण अयस' कहा गया है।",
   "इस काल में सभा और समिति जैसी जन-सभाओं का महत्त्व बढ़ा, और स्त्रियाँ सभा में भाग लेती रहीं।",
   "इस काल में 'निष्क' नामक सिक्के रोज़मर्रा के लेन-देन का सामान्य माध्यम थे।"],
  C3, 0,
  "Only statement 1 is correct. Iron ('shyama' or 'krishna ayas', the dark metal) came into use around 1000 BCE in the Ganga-Yamuna doab, alongside the spread of settled agriculture. "
  "Statement 2 is incorrect on both counts: as royal power grew and kingdoms became territorial, the sabha and samiti lost their importance, and women were no longer permitted to attend the sabha. "
  "Statement 3 is incorrect: the Later Vedic texts mention the nishka and the shatamana, but as gold ornaments or units of value; regular coins came into use only in the age of the Buddha, with the punch-marked coins. "
  "Both traps carry a feature of another period into the Later Vedic age.",
  "केवल कथन 1 सही है। लगभग 1000 ई.पू. से गंगा-यमुना दोआब में लोहे ('श्याम' या 'कृष्ण अयस', यानी काली धातु) का प्रयोग होने लगा, और साथ ही स्थायी खेती फैली। "
  "कथन 2 दोनों ही बातों में गलत है: राजा की शक्ति बढ़ने और राज्यों के क्षेत्रीय बन जाने से सभा और समिति का महत्त्व घट गया, और स्त्रियों को सभा में बैठने की अनुमति नहीं रही। "
  "कथन 3 गलत है: उत्तर वैदिक ग्रंथों में निष्क और शतमान का उल्लेख है, पर सोने के आभूषण या मूल्य की इकाई के रूप में; नियमित सिक्के बुद्ध के युग में आहत (पंच-मार्क) सिक्कों के साथ ही चलन में आए। "
  "दोनों ही जाल किसी दूसरे काल की विशेषता को उत्तर वैदिक युग पर लागू करते हैं।",
  f"{SHARMA} -- chapter on the Later Vedic phase.",
  "ancient-later-vedic-economy-society")

S("aa715bf6-8ace-401e-b741-85b8a5f24f08", "Ancient", "medium",
  "With reference to the Arthashastra, consider the following statements:",
  "अर्थशास्त्र के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its text was discovered and first published in the early twentieth century by R. Shamasastry.",
   "It sets out a 'mandala' of states, in which the kingdom immediately next to a ruler's own is regarded as a natural friend.",
   "It is written in Prakrit, the language of Ashoka's edicts."],
  ["इसका पाठ बीसवीं सदी के आरंभ में आर. शामशास्त्री ने खोजा और पहली बार प्रकाशित किया।",
   "इसमें राज्यों के 'मंडल' का सिद्धांत दिया गया है, जिसमें किसी राजा के ठीक पड़ोसी राज्य को उसका स्वाभाविक मित्र माना गया है।",
   "यह प्राकृत भाषा में लिखा गया है, जो अशोक के अभिलेखों की भाषा है।"],
  C3, 0,
  "Only statement 1 is correct. R. Shamasastry identified a manuscript of the Arthashastra at the Oriental Research Institute, Mysore, and published the text in 1909 (an English translation followed in 1915). "
  "Statement 2 reverses the mandala theory: with the ruler seeking conquest (vijigishu) at the centre, the immediate neighbour is the natural enemy (ari) and the state beyond it the natural friend (mitra). "
  "Statement 3 is incorrect: the Arthashastra is a Sanskrit treatise; Prakrit is the language of most of Ashoka's inscriptions.",
  "केवल कथन 1 सही है। आर. शामशास्त्री ने मैसूर के ओरिएंटल रिसर्च इंस्टिट्यूट में अर्थशास्त्र की एक पांडुलिपि पहचानी और 1909 में इसका पाठ प्रकाशित किया (अंग्रेज़ी अनुवाद 1915 में आया)। "
  "कथन 2 मंडल सिद्धांत को उलट देता है: केंद्र में विजय चाहने वाले राजा (विजिगीषु) के लिए ठीक पड़ोसी स्वाभाविक शत्रु (अरि) है और उसके आगे का राज्य स्वाभाविक मित्र (मित्र)। "
  "कथन 3 गलत है: अर्थशास्त्र संस्कृत का ग्रंथ है; प्राकृत अशोक के अधिकांश अभिलेखों की भाषा है।",
  f"{SHARMA} -- chapter on the Maurya age; Kautilya's Arthashastra, tr. R. Shamasastry (1915), Book VI (the mandala of states).",
  "ancient-arthashastra-mauryan-administration")

S("91583205-aacc-4a40-ab5c-14c3c7ee78b0", "Ancient", "medium",
  "Consider the following statements regarding Ashoka's Dhamma:",
  "अशोक के धम्म के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Ashoka appointed special officers called 'Dhamma Mahamattas' to spread and oversee the practice of Dhamma.",
   "His edicts urge respect towards both Brahmanas and Shramanas, and restraint in speech so that other sects are not disparaged.",
   "The Rummindei pillar inscription commemorates Ashoka's visit to Bodh Gaya, the place of the Buddha's birth."],
  ["अशोक ने धम्म के प्रचार और उसके पालन की देखरेख के लिए 'धम्म महामात्र' नामक विशेष अधिकारी नियुक्त किए।",
   "उसके अभिलेख ब्राह्मणों और श्रमणों, दोनों के प्रति आदर का आग्रह करते हैं, और वाणी पर संयम की बात करते हैं ताकि दूसरे संप्रदायों की निंदा न हो।",
   "रुम्मिनदेई स्तंभ-लेख अशोक की बोधगया यात्रा की स्मृति में है, जो बुद्ध का जन्मस्थान है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Rock Edict V records the appointment of Dhamma Mahamattas. Rock Edict XII asks for respect to all sects and restraint in speech (vachaguti), and several edicts pair Brahmanas with Shramanas as deserving respect: Ashoka's Dhamma was an ethical code, not a demand for conversion. "
  "Statement 3 is incorrect: the Rummindei (Lumbini) pillar in Nepal marks Ashoka's visit to Lumbini, the Buddha's birthplace, and records that the village was exempted from tax (bali) and paid only one-eighth of its produce (bhaga). Bodh Gaya is the place of enlightenment.",
  "कथन 1 और 2 सही हैं। शिलालेख V में धम्म महामात्रों की नियुक्ति का उल्लेख है। शिलालेख XII सभी संप्रदायों के प्रति आदर और वाणी पर संयम (वचगुत्ति) का आग्रह करता है, और कई अभिलेख ब्राह्मणों और श्रमणों को साथ-साथ आदर योग्य बताते हैं: अशोक का धम्म एक नैतिक आचार-संहिता था, धर्म-परिवर्तन की माँग नहीं। "
  "कथन 3 गलत है: नेपाल में स्थित रुम्मिनदेई (लुम्बिनी) स्तंभ अशोक की लुम्बिनी यात्रा का स्मारक है, जो बुद्ध का जन्मस्थान है; इसमें लिखा है कि गाँव को बलि (कर) से मुक्त किया गया और उसे उपज का केवल आठवाँ भाग (भाग) देना था। बोधगया ज्ञान-प्राप्ति का स्थान है।",
  f"Ashokan inscriptions: Rock Edicts V and XII, Rummindei Pillar Inscription (tr. in D.C. Sircar, Inscriptions of Asoka); {THEMES1} -- 'Kings, Farmers and Towns'.",
  "ancient-ashoka-dhamma")

S("5ec33226-7aad-4c2a-a3c5-808a65356546", "Ancient", "medium",
  "Consider the following statements regarding Chandragupta Maurya:",
  "चंद्रगुप्त मौर्य के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Greek and Latin writers refer to him as 'Sandrocottus'.",
   "Under the settlement that ended his war with Seleucus Nicator, territories in the north-west, including Arachosia and Gedrosia, passed to him.",
   "According to Jain tradition, he gave up the throne and ended his life at Shravanabelagola by the Jain rite of fasting."],
  ["यूनानी और लैटिन लेखक उसे 'सैंड्रोकोट्टस' कहते हैं।",
   "सेल्यूकस निकेटर के साथ युद्ध समाप्त करने वाले समझौते के तहत अराकोसिया और जेड्रोसिया सहित उत्तर-पश्चिम के कुछ क्षेत्र उसे मिले।",
   "जैन परंपरा के अनुसार, उसने सिंहासन त्याग दिया और श्रवणबेलगोला में जैन विधि से उपवास करते हुए प्राण त्यागे।"],
  C3, 2,
  "All three statements are correct. Classical writers such as Justin and Plutarch call him Sandrocottus, an identification made by William Jones that anchors Indian chronology. "
  "After the conflict of about 305-303 BCE, Seleucus ceded Arachosia (Kandahar region), Gedrosia (Baluchistan) and Paropamisadae (Kabul region) in return for 500 war elephants, and Megasthenes was later sent to his court. "
  "Jain tradition holds that he went south with the monk Bhadrabahu during a famine and died at Shravanabelagola by sallekhana (fasting unto death). "
  "A solver who expects one planted error in every question will wrongly pick 'Only two'.",
  "तीनों कथन सही हैं। जस्टिन और प्लूटार्क जैसे क्लासिकल लेखक उसे सैंड्रोकोट्टस कहते हैं; विलियम जोन्स द्वारा की गई इस पहचान पर भारतीय कालक्रम टिका है। "
  "लगभग 305-303 ई.पू. के संघर्ष के बाद सेल्यूकस ने 500 युद्ध-हाथियों के बदले अराकोसिया (कंधार क्षेत्र), जेड्रोसिया (बलूचिस्तान) और पैरोपेमिसडाई (काबुल क्षेत्र) सौंप दिए, और बाद में मेगस्थनीज़ को उसके दरबार में भेजा गया। "
  "जैन परंपरा के अनुसार वह अकाल के समय मुनि भद्रबाहु के साथ दक्षिण गया और श्रवणबेलगोला में सल्लेखना (आमरण उपवास) द्वारा देह त्यागी। "
  "जो विद्यार्थी हर प्रश्न में एक गलत कथन की अपेक्षा रखता है, वह भूल से 'केवल दो' चुन लेगा।",
  f"{SHARMA} -- chapter on the Maurya age; Plutarch, Life of Alexander 62 and Strabo, Geography XV.2.9 (the settlement with Seleucus).",
  "ancient-chandragupta-maurya-sources")

S("39d87640-e001-460f-b9dc-97d95d33a044", "Ancient", "medium",
  "With reference to the Chinese pilgrim Fa-Hien (Faxian), consider the following statements:",
  "चीनी यात्री फाह्यान (फ़ाश्यान) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He visited India during the reign of Chandragupta II.",
   "He came to India overland through Central Asia and returned to China by sea, by way of Sri Lanka.",
   "He described the Chandalas, who lived outside the towns and struck a piece of wood to announce their approach."],
  ["वह चंद्रगुप्त द्वितीय के शासनकाल में भारत आया।",
   "वह मध्य एशिया होकर स्थल मार्ग से भारत आया और श्रीलंका होते हुए समुद्री मार्ग से चीन लौटा।",
   "उसने चांडालों का वर्णन किया है, जो नगरों के बाहर रहते थे और अपने आने की सूचना देने के लिए लकड़ी का एक टुकड़ा बजाते थे।"],
  C3, 2,
  "All three statements are correct. Fa-Hien travelled between about 399 and 414 CE, in the reign of Chandragupta II, although his account never names the king. "
  "He went overland through Central Asia, and returned by sea from Tamralipti, halting in Sri Lanka and Java. "
  "He records that the Chandalas lived apart and struck a piece of wood when entering a town so that others could avoid them, which is evidence of untouchability in the Gupta period. "
  "(He also notes that the king ruled without capital punishment, imposing fines instead.)",
  "तीनों कथन सही हैं। फाह्यान लगभग 399 से 414 ई. के बीच, चंद्रगुप्त द्वितीय के शासनकाल में, भारत आया, यद्यपि उसके विवरण में राजा का नाम कहीं नहीं आता। "
  "वह मध्य एशिया होकर स्थल मार्ग से आया और ताम्रलिप्ति से समुद्री मार्ग द्वारा श्रीलंका और जावा होते हुए लौटा। "
  "वह लिखता है कि चांडाल अलग रहते थे और नगर में प्रवेश करते समय लकड़ी का टुकड़ा बजाते थे ताकि दूसरे लोग उनसे बच सकें; यह गुप्त काल में छुआछूत का प्रमाण है। "
  "(वह यह भी लिखता है कि राजा मृत्युदंड नहीं देता था, बल्कि अर्थदंड लगाता था।)",
  f"{SHARMA} -- chapter on the Gupta age; A Record of Buddhistic Kingdoms: Fa-Hien's travels, tr. James Legge (1886), chapter XVI.",
  "ancient-fa-hien-gupta-visit")

S("ce531f48-0056-4de0-ac5c-4b7e4ea2bdce", "Ancient", "medium",
  "Consider the following statements regarding the Sarnath Lion Capital:",
  "सारनाथ के सिंह-शीर्ष के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Lion Capital of Ashoka from Sarnath was adopted as the National Emblem of India.",
   "The motto 'Satyameva Jayate' inscribed below the National Emblem is taken from the Katha Upanishad.",
   "On the abacus of the capital, the figures of an elephant, a horse, a bull and a lion are separated by lotus flowers."],
  ["सारनाथ से प्राप्त अशोक के सिंह-शीर्ष को भारत के राष्ट्रीय प्रतीक के रूप में अपनाया गया।",
   "राष्ट्रीय प्रतीक के नीचे अंकित आदर्श-वाक्य 'सत्यमेव जयते' कठ उपनिषद से लिया गया है।",
   "शीर्ष के फलक (abacus) पर हाथी, घोड़ा, बैल और सिंह की आकृतियाँ कमल के फूलों द्वारा एक-दूसरे से अलग की गई हैं।"],
  C3, 0,
  "Only statement 1 is correct: the Sarnath capital was adopted as the State Emblem on 26 January 1950. "
  "Statement 2 is incorrect: 'Satyameva Jayate' comes from the Mundaka Upanishad (III.1.6), not the Katha Upanishad (the source of the Nachiketa dialogue). "
  "Statement 3 is incorrect: on the circular abacus the four animals -- elephant, horse, bull and lion -- are separated by Dharma wheels (chakras), not lotuses. The lotus is below the abacus, in the inverted bell-shaped base. "
  "The trap in statement 3 mixes two real elements of the same capital.",
  "केवल कथन 1 सही है: सारनाथ के शीर्ष को 26 जनवरी 1950 को राजकीय प्रतीक के रूप में अपनाया गया। "
  "कथन 2 गलत है: 'सत्यमेव जयते' मुंडक उपनिषद (III.1.6) से लिया गया है, कठ उपनिषद से नहीं (कठ उपनिषद नचिकेता संवाद का स्रोत है)। "
  "कथन 3 गलत है: गोल फलक पर चारों पशु (हाथी, घोड़ा, बैल और सिंह) धर्म-चक्रों द्वारा अलग किए गए हैं, कमल द्वारा नहीं। कमल फलक के नीचे, उलटी घंटी के आकार के आधार में है। "
  "कथन 3 का जाल एक ही शीर्ष के दो वास्तविक हिस्सों को आपस में मिला देने का है।",
  f"{ART} -- chapter on Mauryan art; State Emblem of India (Prohibition of Improper Use) Act, 2005, Schedule.",
  "ancient-sarnath-lion-capital")

S("ad9d29fa-865c-41b6-a5b0-c6e36e51ba84", "Ancient", "hard",
  "With reference to the Kalinga War and its record in Ashoka's inscriptions, consider the following statements:",
  "कलिंग युद्ध और अशोक के अभिलेखों में उसके उल्लेख के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Ashoka's remorse over the war is expressed in Major Rock Edict XIII.",
   "At Dhauli and Jaugada in Kalinga itself, Rock Edict XIII is not inscribed; two 'Separate Edicts' appear there instead.",
   "In the same edict that expresses his remorse, Ashoka also warns the forest peoples that he still has the power to punish them."],
  ["युद्ध पर अशोक का पश्चाताप बृहद् शिलालेख XIII में व्यक्त हुआ है।",
   "स्वयं कलिंग में, धौली और जौगढ़ में, शिलालेख XIII अंकित नहीं है; वहाँ इसकी जगह दो 'पृथक् शिलालेख' मिलते हैं।",
   "जिस शिलालेख में वह पश्चाताप व्यक्त करता है, उसी में अशोक वन्य लोगों को यह चेतावनी भी देता है कि उसके पास उन्हें दंड देने की शक्ति अब भी है।"],
  C3, 2,
  "All three statements are correct. Rock Edict XIII describes the conquest of Kalinga, with 150,000 deported and 100,000 killed, and Ashoka's remorse. "
  "At Dhauli and Jaugada, Rock Edicts XI to XIII are left out and two Separate Kalinga Edicts, addressed to the officials of Tosali and Samapa, are added -- understandably, the remorse edict was not engraved where the war was fought. "
  "The same Rock Edict XIII warns the forest peoples (atavikas) that the king, though penitent, retains his power: conquest by Dhamma did not mean giving up the state's coercive power.",
  "तीनों कथन सही हैं। शिलालेख XIII कलिंग विजय का वर्णन करता है, जिसमें 1,50,000 लोग बंदी बनाकर ले जाए गए और 1,00,000 मारे गए, और इसमें अशोक का पश्चाताप दर्ज है। "
  "धौली और जौगढ़ में शिलालेख XI से XIII छोड़ दिए गए हैं और तोसली तथा समापा के अधिकारियों को संबोधित दो पृथक् कलिंग शिलालेख जोड़े गए हैं; समझा जा सकता है कि पश्चाताप वाला अभिलेख वहीं नहीं खुदवाया गया जहाँ युद्ध हुआ था। "
  "यही शिलालेख XIII वन्य लोगों (आटविक) को चेतावनी देता है कि राजा पश्चाताप के बावजूद अपनी शक्ति बनाए हुए है: धम्म-विजय का अर्थ राज्य की दंड-शक्ति छोड़ देना नहीं था।",
  f"Ashokan inscriptions: Major Rock Edict XIII and the Separate Kalinga Edicts at Dhauli and Jaugada (tr. in D.C. Sircar, Inscriptions of Asoka); {SHARMA} -- chapter on the Maurya age.",
  "ancient-kalinga-war-edicts")

S("2e1352fa-bde4-4d0b-9ffc-693a381d170a", "Ancient", "easy",
  "Consider the following statements regarding the seals and script of the Harappan civilisation:",
  "हड़प्पा सभ्यता की मुहरों और लिपि के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most Harappan seals are made of steatite and carry animal motifs such as the humped bull and the 'unicorn'.",
   "The so-called 'Pashupati' seal, showing a seated figure surrounded by animals, was found at Mohenjodaro.",
   "The Harappan script is generally held to have been written from right to left."],
  ["हड़प्पा की अधिकांश मुहरें सेलखड़ी (steatite) की बनी हैं और उन पर कूबड़ वाले बैल और 'एकशृंगी' (unicorn) जैसे पशुओं की आकृतियाँ हैं।",
   "तथाकथित 'पशुपति' मुहर, जिस पर पशुओं से घिरी एक बैठी हुई आकृति है, मोहनजोदड़ो से मिली थी।",
   "आम तौर पर माना जाता है कि हड़प्पा लिपि दाएँ से बाएँ लिखी जाती थी।"],
  C3, 2,
  "All three statements are correct. Steatite seals with the 'unicorn' (the commonest motif), the humped bull and other animals are typical of Harappan sites. "
  "The 'Pashupati' seal, a cross-legged figure surrounded by an elephant, a tiger, a rhinoceros and a buffalo, is from Mohenjodaro; calling the figure a proto-Shiva is only an interpretation. "
  "The script is still undeciphered, but the spacing of signs on seals, which cramps on the left, shows that it was usually written from right to left.",
  "तीनों कथन सही हैं। 'एकशृंगी' (सबसे आम आकृति), कूबड़ वाले बैल और अन्य पशुओं वाली सेलखड़ी की मुहरें हड़प्पा स्थलों की पहचान हैं। "
  "'पशुपति' मुहर, जिस पर पालथी मारकर बैठी आकृति हाथी, बाघ, गैंडे और भैंसे से घिरी है, मोहनजोदड़ो की है; इस आकृति को आद्य-शिव कहना केवल एक व्याख्या है। "
  "लिपि अभी तक पढ़ी नहीं जा सकी है, पर मुहरों पर चिह्नों के बीच की दूरी, जो बाईं ओर सिकुड़ जाती है, दिखाती है कि इसे आम तौर पर दाएँ से बाएँ लिखा जाता था।",
  f"{THEMES1} -- 'Bricks, Beads and Bones: The Harappan Civilisation'.",
  "ancient-indus-seals-script")

S("17c2a588-f4b9-4aec-ab0d-6ae655e11f0e", "Ancient", "medium",
  "Consider the following statements regarding the Rig Veda:",
  "ऋग्वेद के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a collection of hymns (suktas) arranged in ten books called mandalas.",
   "The Purusha Sukta, which describes the origin of the four varnas, is in its tenth mandala.",
   "The Gayatri Mantra, addressed to Savitri, is also in its tenth mandala."],
  ["यह सूक्तों (स्तुतियों) का संग्रह है, जो दस मंडलों में व्यवस्थित है।",
   "चारों वर्णों की उत्पत्ति का वर्णन करने वाला पुरुष सूक्त इसके दसवें मंडल में है।",
   "सविता को संबोधित गायत्री मंत्र भी इसके दसवें मंडल में है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Rig Veda has 1,028 hymns in ten mandalas; mandalas II to VII (the 'family books') are the oldest, while I and X are later additions. "
  "The Purusha Sukta (X.90), which derives the four varnas from the cosmic being, is in the late tenth mandala. "
  "Statement 3 is incorrect: the Gayatri Mantra (III.62.10), addressed to Savitri, is in the third mandala, attributed to the family of Vishvamitra.",
  "कथन 1 और 2 सही हैं। ऋग्वेद में दस मंडलों में 1,028 सूक्त हैं; मंडल II से VII ('कुल-मंडल') सबसे पुराने हैं, जबकि I और X बाद में जोड़े गए। "
  "पुरुष सूक्त (X.90), जो चारों वर्णों को विराट पुरुष से उत्पन्न बताता है, बाद के दसवें मंडल में है। "
  "कथन 3 गलत है: सविता को संबोधित गायत्री मंत्र (III.62.10) तीसरे मंडल में है, जो विश्वामित्र के कुल से जुड़ा है।",
  f"{SHARMA} -- chapter on the Rig Vedic age; Rig Veda X.90 and III.62.10.",
  "ancient-rig-veda-structure")

S("c4b8cc00-0c69-4aef-badc-908d37f4d3cd", "Ancient", "hard",
  "Consider the following statements regarding the end of the Maurya dynasty:",
  "मौर्य वंश के अंत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["After Ashoka, some accounts suggest that the empire was divided among his successors, who included Dasharatha and Samprati.",
   "The last Mauryan ruler, Brihadratha, was killed by his commander Pushyamitra, who then founded the Kanva dynasty.",
   "The Ayodhya inscription of Dhanadeva records that Pushyamitra performed two Rajasuya sacrifices."],
  ["अशोक के बाद, कुछ विवरणों के अनुसार साम्राज्य उसके उत्तराधिकारियों में बँट गया, जिनमें दशरथ और संप्रति थे।",
   "अंतिम मौर्य शासक बृहद्रथ की हत्या उसके सेनापति पुष्यमित्र ने की, जिसने फिर कण्व वंश की स्थापना की।",
   "धनदेव के अयोध्या अभिलेख में लिखा है कि पुष्यमित्र ने दो राजसूय यज्ञ किए।"],
  C3, 0,
  "Only statement 1 is correct. Puranic, Buddhist and Jain lists name different successors of Ashoka (Dasharatha, who dedicated the Nagarjuni caves to the Ajivikas, and Samprati, a patron of Jainism), which suggests a divided empire. "
  "Statement 2 is incorrect: Pushyamitra, having killed Brihadratha in about 185 BCE, founded the Shunga dynasty; the Kanvas later overthrew the last Shunga ruler, Devabhuti. "
  "Statement 3 is incorrect: the Ayodhya inscription of Dhanadeva calls Pushyamitra the performer of two Ashvamedhas (dvir-ashvamedha-yajin), the horse sacrifice of a paramount king; it does not mention the Rajasuya, the royal consecration.",
  "केवल कथन 1 सही है। पुराण, बौद्ध और जैन सूचियाँ अशोक के अलग-अलग उत्तराधिकारियों के नाम देती हैं (दशरथ, जिसने नागार्जुनी गुफाएँ आजीविकों को दान कीं, और संप्रति, जो जैन धर्म का संरक्षक था), जिससे बँटे हुए साम्राज्य का संकेत मिलता है। "
  "कथन 2 गलत है: लगभग 185 ई.पू. में बृहद्रथ की हत्या करके पुष्यमित्र ने शुंग वंश की स्थापना की; कण्वों ने बाद में अंतिम शुंग शासक देवभूति को हटाया। "
  "कथन 3 गलत है: धनदेव का अयोध्या अभिलेख पुष्यमित्र को दो अश्वमेध करने वाला (द्विरश्वमेधयाजी) कहता है, जो चक्रवर्ती राजा का अश्व-यज्ञ है; इसमें राजसूय (राज्याभिषेक का यज्ञ) का उल्लेख नहीं है।",
  f"{SHARMA} -- chapters on the Maurya age and on the post-Maurya period; Ayodhya inscription of Dhanadeva (Epigraphia Indica XX).",
  "ancient-mauryan-decline-shunga")

S("e024e971-2267-44c1-9a6c-b42aa01858a7", "Ancient", "medium",
  "Consider the following statements regarding Harshavardhana:",
  "हर्षवर्धन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He convened an assembly at Kanauj to honour Hiuen Tsang and to publicise the Mahayana doctrine.",
   "He held an assembly at Prayaga every five years at which he gave away his accumulated wealth in charity.",
   "The Sanskrit plays Ratnavali, Nagananda and Priyadarshika are attributed to him."],
  ["उसने ह्वेनसांग के सम्मान और महायान मत के प्रचार के लिए कन्नौज में एक सभा बुलाई।",
   "वह हर पाँच वर्ष पर प्रयाग में एक सभा करता था, जिसमें वह अपना संचित धन दान में दे देता था।",
   "संस्कृत नाटक रत्नावली, नागानंद और प्रियदर्शिका उसके रचे माने जाते हैं।"],
  C3, 2,
  "All three statements are correct. Hiuen Tsang describes the Kanauj assembly (about 643 CE) held in his honour, at which the Mahayana doctrine was expounded. "
  "He also describes the quinquennial assembly (the sixth, which he attended) at Prayaga, the confluence of the Ganga and Yamuna, where Harsha gave away his treasure. "
  "The three Sanskrit plays are attributed to Harsha, who also honoured Shiva and the Sun along with the Buddha. "
  "The trap is to shift the Prayaga assembly to Nalanda, a Buddhist centre Harsha patronised.",
  "तीनों कथन सही हैं। ह्वेनसांग उसके सम्मान में लगभग 643 ई. में हुई कन्नौज सभा का वर्णन करता है, जिसमें महायान मत की व्याख्या की गई। "
  "वह गंगा-यमुना के संगम प्रयाग में होने वाली पंचवर्षीय सभा का भी वर्णन करता है (वह छठी सभा में उपस्थित था), जिसमें हर्ष अपना खजाना दान कर देता था। "
  "तीनों संस्कृत नाटक हर्ष के रचे माने जाते हैं; वह बुद्ध के साथ-साथ शिव और सूर्य का भी सम्मान करता था। "
  "यहाँ जाल यह है कि प्रयाग की सभा को नालंदा से जोड़ दिया जाए, जो हर्ष द्वारा संरक्षित एक बौद्ध केंद्र था।",
  f"{SHARMA} -- chapter on the age of Harsha; Si-Yu-Ki: Buddhist Records of the Western World, tr. Samuel Beal (1884), Book V.",
  "ancient-harsha-assemblies-plays")

S("48300813-d3d7-4905-8649-4d844a7bd219", "Ancient", "hard",
  "Consider the following statements regarding the Sangam age:",
  "संगम युग के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Velir were the three crowned dynasties of the Sangam age: the Cheras, the Cholas and the Pandyas.",
   "Sangam poems refer to 'Yavana' merchants who came to the Tamil ports.",
   "Of the five 'tinai' (landscapes) into which the Sangam texts divide the land, 'marutam' denotes the hill country."],
  ["संगम युग के तीन मुकुटधारी राजवंश, यानी चेर, चोल और पांड्य, 'वेलिर' कहलाते थे।",
   "संगम कविताओं में तमिल बंदरगाहों पर आने वाले 'यवन' व्यापारियों का उल्लेख है।",
   "संगम ग्रंथ भूमि को जिन पाँच 'तिणै' (भू-दृश्यों) में बाँटते हैं, उनमें 'मरुतम' पहाड़ी क्षेत्र को कहा गया है।"],
  C3, 0,
  "Only statement 2 is correct. Sangam poems speak of Yavanas (Greeks and Romans) arriving with gold and wine and leaving with pepper; Arikamedu and Muziris confirm this Roman trade. "
  "Statement 3 is incorrect: of the five tinai, kurinji is the hill country; marutam is the wet farmland of the river valleys, with mullai (forest and pasture), neytal (coast) and palai (dry land) making up the rest. "
  "Statement 1 is incorrect: the three crowned kings were the muvendar (Chera, Chola and Pandya); the Velir were lesser chieftains, often allied with or subdued by them.",
  "केवल कथन 2 सही है। संगम कविताएँ यवनों (यूनानियों और रोमनों) का वर्णन करती हैं जो सोना और मदिरा लेकर आते थे और काली मिर्च लेकर जाते थे; अरिकामेडु और मुज़िरिस इस रोमन व्यापार की पुष्टि करते हैं। "
  "कथन 3 गलत है: पाँच तिणै में पहाड़ी क्षेत्र कुरिंजि है; मरुतम नदी घाटियों की सिंचित खेती वाली भूमि है, और बाकी मुल्लै (वन और चरागाह), नेयतल (समुद्र-तट) और पालै (शुष्क भूमि) हैं। "
  "कथन 1 गलत है: तीन मुकुटधारी राजा मूवेंदर (चेर, चोल और पांड्य) कहलाते थे; वेलिर छोटे सरदार थे, जो प्रायः इनके सहयोगी होते थे या इनके अधीन कर लिए जाते थे।",
  f"{SHARMA} -- chapter on early states and society in South India; NCERT Class XII, Themes in Indian History Part I -- 'Kings, Farmers and Towns'.",
  "ancient-sangam-polity-economy")

S("56bd5122-8072-4116-854d-508cdb28c45b", "Ancient", "hard",
  "Consider the following statements regarding Gupta coinage and trade:",
  "गुप्तकालीन सिक्कों और व्यापार के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gupta gold coins, called 'dinaras', show the rulers in varied poses, including as archers and lion-slayers.",
   "Some historians see the debasement of gold coins and a fall in long-distance trade in the later Gupta period as signs of economic decline.",
   "The Guptas issued copper coins in far larger numbers than gold coins."],
  ["गुप्तों के सोने के सिक्के, जिन्हें 'दीनार' कहा जाता था, राजाओं को धनुर्धर और सिंह-हंता जैसी अलग-अलग मुद्राओं में दिखाते हैं।",
   "कुछ इतिहासकार बाद के गुप्त काल में सोने के सिक्कों में मिलावट और लंबी दूरी के व्यापार में गिरावट को आर्थिक पतन का संकेत मानते हैं।",
   "गुप्तों ने सोने के सिक्कों की तुलना में ताँबे के सिक्के कहीं अधिक संख्या में जारी किए।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Guptas issued the largest number of gold coins in ancient India, the dinaras, with types such as the archer, lion-slayer, horseman and lyre-player. "
  "The gold content of the coins fell under the later Guptas, and several historians read this, with the loss of Roman trade, as economic decline. "
  "Statement 3 is incorrect: Gupta copper coinage was meagre compared with that of the Kushanas, and it is their gold coins that are abundant -- one of the arguments that everyday exchange was shrinking.",
  "कथन 1 और 2 सही हैं। प्राचीन भारत में सबसे अधिक सोने के सिक्के गुप्तों ने जारी किए, जिन्हें दीनार कहा जाता था; इनके धनुर्धर, सिंह-हंता, अश्वारोही और वीणावादक जैसे प्रकार हैं। "
  "बाद के गुप्तों के समय सिक्कों में सोने की मात्रा घट गई, और कई इतिहासकार इसे रोमन व्यापार के समाप्त होने के साथ जोड़कर आर्थिक पतन मानते हैं। "
  "कथन 3 गलत है: कुषाणों की तुलना में गुप्तों के ताँबे के सिक्के बहुत कम हैं और उनके सोने के सिक्के ही प्रचुर हैं; यह इस तर्क का एक आधार है कि रोज़मर्रा का लेन-देन सिमट रहा था।",
  f"{SHARMA} -- chapter on the Gupta age; {THEMES1} -- 'Kings, Farmers and Towns' (coins).",
  "ancient-gupta-coinage-trade")

S("f7d6131e-232f-4cc3-bb0c-f3fe6a137219", "Ancient", "hard",
  "Consider the following statements regarding the schools of sculpture of the early centuries CE:",
  "आरंभिक ईसवी शताब्दियों की मूर्तिकला शैलियों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Gandhara school worked mainly in the spotted red sandstone of its region.",
   "The Mathura school shows stronger Hellenistic influence than the Gandhara school.",
   "The Amaravati school, under the Satavahanas and the Ikshvakus, is credited with the earliest images of the Buddha in human form."],
  ["गांधार शैली मुख्य रूप से अपने क्षेत्र के चित्तीदार लाल बलुआ पत्थर में काम करती थी।",
   "मथुरा शैली पर गांधार शैली की तुलना में अधिक यूनानी (हेलेनिस्टिक) प्रभाव है।",
   "सातवाहनों और इक्ष्वाकुओं के अधीन अमरावती शैली को मानव रूप में बुद्ध की सबसे आरंभिक प्रतिमाओं का श्रेय दिया जाता है।"],
  C3, 3,
  "None of the statements is correct. The spotted red sandstone belongs to Mathura; Gandhara worked in grey-blue schist and, later, stucco. "
  "The relation in statement 2 is reversed: Gandhara, in the north-west, drew on Greco-Roman models (wavy hair, heavy folds, realistic anatomy), while Mathura was largely indigenous. "
  "The first images of the Buddha in human form appear in the Kushana period at Gandhara and Mathura (which came first is debated); Amaravati, in the Krishna valley, is later and is known for its narrative reliefs in whitish limestone. "
  "Each statement moves a real feature to the wrong school.",
  "कोई भी कथन सही नहीं है। चित्तीदार लाल बलुआ पत्थर मथुरा का है; गांधार धूसर-नीले शिस्ट पत्थर और बाद में चूने (स्टुको) में काम करता था। "
  "कथन 2 में संबंध उलटा है: उत्तर-पश्चिम का गांधार यूनानी-रोमन नमूनों से प्रभावित था (लहरदार बाल, भारी चुन्नटें, यथार्थ शरीर-रचना), जबकि मथुरा मुख्यतः देशी शैली थी। "
  "मानव रूप में बुद्ध की पहली प्रतिमाएँ कुषाण काल में गांधार और मथुरा में मिलती हैं (पहले कौन, इस पर मतभेद है); कृष्णा घाटी की अमरावती शैली बाद की है और सफ़ेद चूना-पत्थर के कथात्मक उभारों के लिए जानी जाती है। "
  "हर कथन एक वास्तविक विशेषता को गलत शैली से जोड़ देता है।",
  f"{ART} -- chapter on post-Mauryan trends in Indian art and architecture.",
  "ancient-gandhara-mathura-amaravati-schools")

# ---- one-liners replaced by questions that test a real distinction ---------------------
M("1143a245-1e43-4e1a-9a35-aedd6e807c75", "Ancient", "medium",
  "The 'Nasadiya Sukta', the hymn of creation that asks how the universe came into being and whether even its overseer knows, is found in:",
  "'नासदीय सूक्त', सृष्टि का वह सूक्त जो पूछता है कि ब्रह्मांड कैसे उत्पन्न हुआ और क्या इसका अध्यक्ष भी यह जानता है, कहाँ मिलता है?",
  ["the Rig Veda", "the Atharva Veda", "the Chandogya Upanishad", "the Shatapatha Brahmana"],
  ["ऋग्वेद में", "अथर्ववेद में", "छांदोग्य उपनिषद में", "शतपथ ब्राह्मण में"],
  0,
  "The Nasadiya Sukta is hymn 129 of the tenth mandala of the Rig Veda. It opens 'there was neither non-existence nor existence then' and ends by doubting whether even the one who watches over creation knows how it began -- an early instance of philosophical questioning within the Vedic corpus. "
  "The other three are later Vedic texts; the Upanishads carry such speculation further, but this hymn is Rigvedic.",
  "नासदीय सूक्त ऋग्वेद के दसवें मंडल का 129वाँ सूक्त है। यह 'तब न असत् था, न सत्' से आरंभ होता है और इस संदेह पर समाप्त होता है कि क्या सृष्टि का अध्यक्ष भी जानता है कि इसका आरंभ कैसे हुआ; वैदिक साहित्य में दार्शनिक जिज्ञासा का यह एक आरंभिक उदाहरण है। "
  "बाकी तीनों बाद के वैदिक ग्रंथ हैं; उपनिषद ऐसे चिंतन को आगे बढ़ाते हैं, पर यह सूक्त ऋग्वैदिक है।",
  f"Rig Veda X.129; {SHARMA} -- chapter on the Rig Vedic age.",
  "ancient-nasadiya-sukta")

M("ba549cae-6aab-4e27-bfa8-1789ed3e03e7", "Ancient", "medium",
  "The Buddha gave his first sermon, the 'Dhammachakkappavattana Sutta', at a deer park known in the early texts as:",
  "बुद्ध ने अपना पहला उपदेश, 'धम्मचक्कपवत्तन सुत्त', जिस मृगदाव (हिरणों के उपवन) में दिया, उसे आरंभिक ग्रंथों में क्या कहा गया है?",
  ["Isipatana", "Jetavana", "Veluvana", "Uruvela"],
  ["इसिपतन", "जेतवन", "वेलुवन", "उरुवेला"],
  0,
  "The first sermon, 'setting in motion the wheel of Dhamma', was given to five companions at Isipatana Migadaya, the deer park now called Sarnath, near Varanasi. "
  "Jetavana was the grove at Shravasti bought for the Sangha by the merchant Anathapindika; Veluvana was the bamboo grove at Rajagriha gifted by Bimbisara; Uruvela, near Bodh Gaya, is where the Buddha practised austerities and attained enlightenment.",
  "पहला उपदेश, 'धम्म का चक्र घुमाना', पाँच साथियों को इसिपतन मृगदाव में दिया गया, जिसे आज वाराणसी के पास सारनाथ कहा जाता है। "
  "जेतवन श्रावस्ती का उपवन था, जिसे व्यापारी अनाथपिंडक ने संघ के लिए खरीदा था; वेलुवन राजगृह का बाँस-वन था, जिसे बिंबिसार ने दान किया था; बोधगया के पास उरुवेला वह स्थान है जहाँ बुद्ध ने तपस्या की और ज्ञान प्राप्त किया।",
  f"{THEMES1} -- 'Thinkers, Beliefs and Buildings'; Samyutta Nikaya 56.11 (Dhammacakkappavattana Sutta).",
  "ancient-buddha-first-sermon-isipatana")

M("bba97c26-6af4-41a4-8aff-121773b70ba7", "Ancient", "medium",
  "The 'Periplus of the Erythraean Sea', written by an anonymous Greek-speaking sailor in the first century CE, is an important source for:",
  "'पेरिप्लस ऑफ़ द एरिथ्रियन सी', जिसे पहली शताब्दी ई. में एक अज्ञात यूनानी-भाषी नाविक ने लिखा, किस विषय का महत्त्वपूर्ण स्रोत है?",
  ["the ports and goods of Indo-Roman sea trade", "the missions Ashoka sent to Greek kings", "the provincial administration of the Guptas", "the route taken by the pilgrim Hiuen Tsang"],
  ["भारत-रोम समुद्री व्यापार के बंदरगाह और वस्तुएँ", "अशोक द्वारा यूनानी राजाओं के पास भेजे गए दूत-मंडल", "गुप्तों का प्रांतीय प्रशासन", "यात्री ह्वेनसांग का यात्रा-मार्ग"],
  0,
  "The Periplus is a merchant's guide to the ports of the Red Sea, the Arabian coast and India. It names Barygaza (Bharuch), Muziris and other ports, and lists what was traded -- pepper, textiles, precious stones and ivory going west, and gold, wine and coral coming in. "
  "It is a first-century CE text, so it cannot describe Ashoka (3rd century BCE), the Guptas (4th-6th century CE) or Hiuen Tsang (7th century CE).",
  "पेरिप्लस लाल सागर, अरब तट और भारत के बंदरगाहों के लिए एक व्यापारी की मार्गदर्शिका है। इसमें बारिगाज़ा (भरूच), मुज़िरिस और अन्य बंदरगाहों के नाम हैं, और व्यापार की वस्तुएँ गिनाई गई हैं: पश्चिम की ओर जाने वाली काली मिर्च, वस्त्र, बहुमूल्य पत्थर और हाथीदाँत, और भारत आने वाला सोना, मदिरा और मूँगा। "
  "यह पहली शताब्दी ई. का ग्रंथ है, इसलिए इसमें अशोक (तीसरी शताब्दी ई.पू.), गुप्त (चौथी से छठी शताब्दी ई.) या ह्वेनसांग (सातवीं शताब्दी ई.) का वर्णन नहीं हो सकता।",
  f"{SHARMA} -- chapter on the Central Asian contact and trade; The Periplus Maris Erythraei, ed. and tr. Lionel Casson (1989).",
  "ancient-periplus-indo-roman-trade")

M("de62ef1c-3289-4ee8-9e9a-ec29d1c7b3c5", "Ancient", "hard",
  "In the Mauryan administration described in the Arthashastra, the 'Sannidhata' was the officer in charge of:",
  "अर्थशास्त्र में वर्णित मौर्य प्रशासन में 'सन्निधाता' किसका प्रभारी अधिकारी था?",
  ["the royal treasury and storehouses", "the assessment and collection of revenue", "the administration of the capital city", "the state's mines and metal workshops"],
  ["राजकीय कोष और भंडार-गृह", "राजस्व का निर्धारण और वसूली", "राजधानी नगर का प्रशासन", "राज्य की खानें और धातु-कार्यशालाएँ"],
  0,
  "The Sannidhata was the chief custodian of the treasury and the royal storehouses. The Samaharta was the chief collector who assessed and collected revenue; the Nagaraka administered the city; and the Akaradhyaksha supervised mines. "
  "The pairing Samaharta-Sannidhata (collection and custody) is the classic confusion in questions on Mauryan officials.",
  "सन्निधाता कोष और राजकीय भंडार-गृहों का मुख्य संरक्षक था। समाहर्ता मुख्य समाहर्ता (कलेक्टर) था जो राजस्व का निर्धारण और वसूली करता था; नागरक नगर का प्रशासन देखता था; और आकराध्यक्ष खानों की देखरेख करता था। "
  "मौर्य अधिकारियों पर प्रश्नों में समाहर्ता और सन्निधाता (वसूली और संरक्षण) का भ्रम सबसे आम है।",
  f"Kautilya's Arthashastra, Book II (the superintendents), tr. R.P. Kangle (1972); {SHARMA} -- chapter on the Maurya age.",
  "ancient-mauryan-officials-sannidhata")

M("cdee1025-ca5c-498e-88e2-5ed869b51797", "Ancient", "medium",
  "Which one of the following is NOT traditionally counted among the 'Navaratnas' (nine gems) of the court of King Vikramaditya?",
  "निम्नलिखित में से किसे परंपरागत रूप से राजा विक्रमादित्य के दरबार के 'नवरत्नों' में नहीं गिना जाता?",
  ["Kalidasa", "Amarasimha", "Varahamihira", "Aryabhata"],
  ["कालिदास", "अमरसिंह", "वराहमिहिर", "आर्यभट"],
  3,
  "The traditional list of the nine gems -- Dhanvantari, Kshapanaka, Amarasimha, Shanku, Vetalabhatta, Ghatakarpara, Kalidasa, Varahamihira and Vararuchi -- does not include Aryabhata, the mathematician-astronomer of Kusumapura who wrote the Aryabhatiya in 499 CE. "
  "The list comes from a much later text and is usually linked with Chandragupta II 'Vikramaditya'; historians treat it as tradition rather than record, since its members did not all live at the same time.",
  "नवरत्नों की परंपरागत सूची में धन्वंतरि, क्षपणक, अमरसिंह, शंकु, वेतालभट्ट, घटकर्पर, कालिदास, वराहमिहिर और वररुचि हैं; इसमें आर्यभट नहीं हैं, जो कुसुमपुर के गणितज्ञ-खगोलशास्त्री थे और जिन्होंने 499 ई. में आर्यभटीय लिखा। "
  "यह सूची बहुत बाद के एक ग्रंथ से आती है और इसे प्रायः चंद्रगुप्त द्वितीय 'विक्रमादित्य' से जोड़ा जाता है; इतिहासकार इसे अभिलेख नहीं, परंपरा मानते हैं, क्योंकि इसके सभी सदस्य एक ही समय में नहीं रहे।",
  f"{SHARMA} -- chapter on the Gupta age (science and literature); NCERT Class XI, Knowledge Traditions and Practices of India -- astronomy.",
  "ancient-navaratnas-tradition")

# ---- pre-2020 code matches converted to the current pairs format ----------------------
P("9909059c-2cf7-4cae-8677-34c134292c48", "Ancient", "medium",
  "Consider the following pairs of ancient ports and their regions:",
  "प्राचीन बंदरगाहों और उनके क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Barygaza : Estuary of the Narmada", "Muziris : Malabar coast", "Tamralipti : Delta of the Godavari", "Arikamedu : Coromandel coast"],
  ["बारिगाज़ा : नर्मदा का ज्वारनदमुख", "मुज़िरिस : मालाबार तट", "ताम्रलिप्ति : गोदावरी का डेल्टा", "अरिकामेडु : कोरोमंडल तट"],
  2,
  "Three pairs are correct. Barygaza (Bharuch) lay on the Narmada estuary; Muziris, near present Kodungallur in Kerala, was the pepper port of the Malabar coast; Arikamedu, near Puducherry on the Coromandel coast, has yielded Roman amphorae and Arretine ware. "
  "Pair 3 is wrong: Tamralipti (Tamluk, West Bengal) was the great port of the Ganga delta, on the Rupnarayan, from which Fa-Hien sailed for Sri Lanka.",
  "तीन युग्म सही हैं। बारिगाज़ा (भरूच) नर्मदा के ज्वारनदमुख पर था; केरल के वर्तमान कोडुंगल्लूर के पास स्थित मुज़िरिस मालाबार तट का काली मिर्च का बंदरगाह था; कोरोमंडल तट पर पुदुच्चेरी के पास अरिकामेडु से रोमन मदिरा-पात्र (एम्फ़ोरा) और एरेटाइन बर्तन मिले हैं। "
  "युग्म 3 गलत है: ताम्रलिप्ति (तामलुक, पश्चिम बंगाल) रूपनारायण नदी पर गंगा डेल्टा का बड़ा बंदरगाह था, जहाँ से फाह्यान श्रीलंका के लिए रवाना हुआ।",
  f"{SHARMA} -- chapter on trade in the post-Maurya period; The Periplus Maris Erythraei, tr. Lionel Casson (1989).",
  "ancient-ports-regions-pairs")

P("d0a09dc3-0ad3-4b2d-9652-fa4730f1d13b", "Ancient", "medium",
  "Consider the following pairs of Harappan sites and features found there:",
  "हड़प्पा स्थलों और वहाँ पाई गई विशेषताओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Dholavira : Large water reservoirs and a signboard of big Harappan characters", "Rakhigarhi : The largest known Harappan site in India", "Kalibangan : A ploughed field", "Chanhudaro : Workshops for making beads"],
  ["धोलावीरा : बड़े जलाशय और हड़प्पा लिपि के बड़े अक्षरों वाला सूचना-पट्ट", "राखीगढ़ी : भारत में ज्ञात सबसे बड़ा हड़प्पा स्थल", "कालीबंगा : जुता हुआ खेत", "चन्हूदड़ो : मनके बनाने की कार्यशालाएँ"],
  3,
  "All four pairs are correct. Dholavira (Kachchh; a World Heritage Site since 2021) has elaborate reservoirs and a 'signboard' of ten large signs. "
  "Rakhigarhi (Haryana) is the largest Harappan site known in India. Kalibangan (Rajasthan) has an early ploughed field with furrows in a grid. Chanhudaro (Sindh) was a craft centre with bead-making and seal-cutting workshops. "
  "A student trained to expect one wrong pair has to verify each one.",
  "चारों युग्म सही हैं। धोलावीरा (कच्छ; 2021 से विश्व धरोहर स्थल) में विस्तृत जलाशय और दस बड़े चिह्नों वाला 'सूचना-पट्ट' मिला है। "
  "राखीगढ़ी (हरियाणा) भारत में ज्ञात सबसे बड़ा हड़प्पा स्थल है। कालीबंगा (राजस्थान) में जाली जैसे पैटर्न में खाँचों वाला आरंभिक जुता हुआ खेत मिला है। चन्हूदड़ो (सिंध) मनके बनाने और मुहरें काटने की कार्यशालाओं वाला शिल्प केंद्र था। "
  "जो विद्यार्थी एक गलत युग्म की अपेक्षा रखता है, उसे हर युग्म को जाँचना पड़ेगा।",
  f"{THEMES1} -- 'Bricks, Beads and Bones: The Harappan Civilisation'; UNESCO World Heritage List: Dholavira (2021).",
  "ancient-harappan-sites-features-pairs")

P("8fb34718-1f45-468f-8a71-20719332516b", "Ancient", "hard",
  "Consider the following pairs of Buddhist councils and the monks traditionally said to have presided over them:",
  "बौद्ध संगीतियों और परंपरा के अनुसार उनकी अध्यक्षता करने वाले भिक्षुओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["First Council : Mahakassapa", "Second Council : Ananda", "Third Council : Moggaliputta Tissa", "Fourth Council : Nagarjuna"],
  ["प्रथम संगीति : महाकस्सप", "द्वितीय संगीति : आनंद", "तृतीय संगीति : मोग्गलिपुत्त तिस्स", "चतुर्थ संगीति : नागार्जुन"],
  1,
  "Two pairs are correct: Mahakassapa presided over the First Council at Rajagriha, and Moggaliputta Tissa over the Third, at Pataliputra under Ashoka. "
  "Pair 2 is wrong: Ananda recited the Sutta Pitaka at the First Council; the Second Council at Vaishali was presided over by Sabakami. "
  "Pair 4 is wrong: the Fourth Council in Kashmir under Kanishka was presided over by Vasumitra, with Ashvaghosha as his deputy; Nagarjuna was the Madhyamaka philosopher. "
  "Both wrong names are real figures tied to the Buddhist tradition, which is what makes them tempting.",
  "दो युग्म सही हैं: राजगृह में प्रथम संगीति की अध्यक्षता महाकस्सप ने की, और अशोक के समय पाटलिपुत्र में तृतीय संगीति की अध्यक्षता मोग्गलिपुत्त तिस्स ने की। "
  "युग्म 2 गलत है: आनंद ने प्रथम संगीति में सुत्त पिटक का पाठ किया था; वैशाली की द्वितीय संगीति की अध्यक्षता सबकामी ने की। "
  "युग्म 4 गलत है: कनिष्क के समय कश्मीर में चतुर्थ संगीति की अध्यक्षता वसुमित्र ने की, और अश्वघोष उपाध्यक्ष थे; नागार्जुन माध्यमिक दर्शन के दार्शनिक थे। "
  "दोनों गलत नाम बौद्ध परंपरा से जुड़े वास्तविक व्यक्ति हैं, इसीलिए ये आकर्षक लगते हैं।",
  f"{SHARMA} -- chapter on Jainism and Buddhism; Dipavamsa and Mahavamsa (the council traditions).",
  "ancient-buddhist-councils-presiding-pairs")

P("8d0e199f-f436-4212-b8dd-bd59ebba942d", "Ancient", "hard",
  "Consider the following pairs of ancient texts and their authors:",
  "प्राचीन ग्रंथों और उनके लेखकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Mudrarakshasa : Vishakhadatta", "Harshacharita : Harshavardhana", "Mrichchhakatika : Bhasa", "Kavyamimamsa : Kalidasa"],
  ["मुद्राराक्षस : विशाखदत्त", "हर्षचरित : हर्षवर्धन", "मृच्छकटिक : भास", "काव्यमीमांसा : कालिदास"],
  0,
  "Only one pair is correct: Vishakhadatta wrote the Mudrarakshasa, a political drama on how Chanakya won over Rakshasa, the minister of the Nandas. "
  "The Harshacharita was written by Banabhatta, Harsha's court poet, not by Harsha. The Mrichchhakatika is by Shudraka; it expands the incomplete play 'Charudatta' ascribed to Bhasa, which is the source of the trap. "
  "The Kavyamimamsa, a work on poetics, is by Rajashekhara (about 10th century), not Kalidasa.",
  "केवल एक युग्म सही है: विशाखदत्त ने मुद्राराक्षस लिखा, जो एक राजनीतिक नाटक है कि चाणक्य ने नंदों के मंत्री राक्षस को कैसे अपने पक्ष में किया। "
  "हर्षचरित हर्ष के दरबारी कवि बाणभट्ट ने लिखा, हर्ष ने नहीं। मृच्छकटिक शूद्रक की रचना है; यह भास के माने जाने वाले अधूरे नाटक 'चारुदत्त' का विस्तार है, और यही इस जाल का स्रोत है। "
  "काव्यशास्त्र की रचना काव्यमीमांसा राजशेखर (लगभग 10वीं शताब्दी) की है, कालिदास की नहीं।",
  f"{SHARMA} -- chapters on the Gupta age and the age of Harsha (literature); A.B. Keith, The Sanskrit Drama (1924).",
  "ancient-texts-authors-pairs")

P("5c391615-afbe-4c60-98a6-e8b23f4a1fbc", "Ancient", "hard",
  "Consider the following pairs of rulers and the titles or epithets used for them:",
  "शासकों और उनके लिए प्रयुक्त उपाधियों या विशेषणों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Ashoka : Devanampiya", "Samudragupta : Kaviraja", "Kanishka : Devaputra", "Chandragupta II : Lichchhavi-dauhitra"],
  ["अशोक : देवानंपिय", "समुद्रगुप्त : कविराज", "कनिष्क : देवपुत्र", "चंद्रगुप्त द्वितीय : लिच्छवि-दौहित्र"],
  2,
  "Three pairs are correct. Ashoka calls himself Devanampiya Piyadasi (beloved of the gods) in his edicts; the Allahabad Prashasti calls Samudragupta a Kaviraja (king of poets); Kanishka's inscriptions use Devaputra (son of god), a title of Chinese origin. "
  "Pair 4 is wrong: Lichchhavi-dauhitra (daughter's son of the Lichchhavis) describes Samudragupta, whose mother Kumaradevi was a Lichchhavi princess, as the gold coins of Chandragupta I and Kumaradevi celebrate.",
  "तीन युग्म सही हैं। अशोक अपने अभिलेखों में स्वयं को देवानंपिय पियदसि (देवताओं का प्रिय) कहता है; प्रयाग प्रशस्ति समुद्रगुप्त को कविराज (कवियों का राजा) कहती है; कनिष्क के अभिलेखों में देवपुत्र (ईश्वर का पुत्र) उपाधि है, जो चीनी मूल की है। "
  "युग्म 4 गलत है: लिच्छवि-दौहित्र (लिच्छवियों की पुत्री का पुत्र) समुद्रगुप्त के लिए है, जिसकी माता कुमारदेवी लिच्छवि राजकुमारी थीं; चंद्रगुप्त प्रथम और कुमारदेवी के सोने के सिक्के इसी संबंध का उत्सव मनाते हैं।",
  f"Allahabad Pillar Inscription of Samudragupta (Corpus Inscriptionum Indicarum III); {SHARMA} -- chapters on the Maurya, Kushana and Gupta periods.",
  "ancient-rulers-titles-pairs")

P("6a850255-fb68-4726-8bba-007aa878b351", "Ancient", "medium",
  "Consider the following pairs of dynasties and their capitals:",
  "राजवंशों और उनकी राजधानियों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kushanas : Purushapura", "Satavahanas : Pratishthana", "Indo-Greeks under Menander : Sakala", "Western Kshatrapas : Ujjayini"],
  ["कुषाण : पुरुषपुर", "सातवाहन : प्रतिष्ठान", "मिनांडर के अधीन हिंद-यूनानी : साकल", "पश्चिमी क्षत्रप : उज्जयिनी"],
  3,
  "All four pairs are correct. Purushapura (Peshawar) was Kanishka's capital; Pratishthana (Paithan, on the Godavari) was the Satavahana seat; Menander (Milinda of the Milindapanha) ruled from Sakala (Sialkot); and the Kardamaka line of Western Kshatrapas, including Chashtana and Rudradaman I, ruled from Ujjayini. "
  "The question rewards knowing that every one of these is standard, rather than hunting for a planted error.",
  "चारों युग्म सही हैं। पुरुषपुर (पेशावर) कनिष्क की राजधानी था; गोदावरी तट पर प्रतिष्ठान (पैठण) सातवाहनों का केंद्र था; मिनांडर (मिलिंदपन्ह का मिलिंद) साकल (सियालकोट) से शासन करता था; और चष्टन तथा रुद्रदामन प्रथम समेत पश्चिमी क्षत्रपों का कार्दमक वंश उज्जयिनी से शासन करता था। "
  "यह प्रश्न इस बात को परखता है कि विद्यार्थी जानता हो कि ये सभी सही हैं, न कि किसी गलत युग्म की खोज करता रहे।",
  f"{SHARMA} -- chapters on the Central Asian contact and on the Satavahanas.",
  "ancient-dynasties-capitals-pairs")

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "history_rewrite_ancient.sql"), "w", encoding="utf-8").write("\n".join(OUT) + "\n")
    print(len(OUT), "rows;", dict(sorted(TALLY.items())))
