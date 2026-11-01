# -*- coding: utf-8 -*-
"""Whole-series audit fixes, November 2026 (no attempts on any UPSC test yet).

1. Poona Pact item: statement 1 said the Pact was "signed between Mahatma Gandhi and Dr. B. R. Ambedkar".
   Gandhi was not a signatory -- Ambedkar signed for the Depressed Classes and Madan Mohan Malaviya for the
   caste Hindus, to end Gandhi's fast in Yerwada jail -- so the statement is reworded and the key (Only two) kept.
2. Two old items carried option ids q1a..q1d / q2a..q2d; they are renamed a..d like every other row.
3. Hindi longest-key giveaways: in these MCQs the Hindi of the key was clearly the longest option although the
   English was not. The Hindi options are re-translated (key shortened, distractors made fuller and closer to
   the English) so that length gives nothing away in either language. English text is unchanged.

Usage: python audit_fixes_2026_11.py <qs.json export>  ->  audit_fixes_2026_11.sql
Each update matches the row's current options/text exactly, so a row edited since the export is left alone.
"""
import io, json, os, sys

HI = {
    "medieval-malik-ambar-ahmadnagar": {
        0: "पुर्तगाली बेड़े का समर्थन पाया, जिसने समुद्र के रास्ते मुग़ल सेनाओं की रसद काट दी",
        1: "फ़ारस के सफ़वी शाह से गठबंधन किया, जिसने उसकी सहायता के लिए दक्कन में अपनी एक सेना भेजी",
        2: "मराठा हल्के घुड़सवारों से छापामार युद्ध किया और उचित राजस्व व्यवस्था से किसानों को जीता",
        3: "पूरे दक्कन में ऐसे क़िलों की शृंखला बनाई जिनमें यूरोपीय तोपची तैनात थे",
    },
    "fb-effective-capex": {
        0: "पूँजीगत व्यय में से राज्यों को दिए गए ऋणों और अग्रिमों को घटाकर प्राप्त राशि",
        1: "पूँजीगत व्यय और उसी वर्ष में प्राप्त विनिवेश आय का योग",
        3: "पूँजीगत व्यय और पूँजीगत परिसंपत्तियों के सृजन हेतु सहायता अनुदान का योग",
    },
    "medieval-hughli-portuguese-1632": {
        0: "तब तक डचों के विरुद्ध युद्ध में पुर्तगालियों को ही अपना मुख्य सहयोगी बना चुके थे",
        1: "ने सत्रहवीं शताब्दी के शेष भाग के लिए सभी यूरोपीय व्यापारिक कंपनियों को बंगाल से बाहर निकाल दिया",
        2: "ने गोवा से पुर्तगालियों को बाहर निकालने के लिए एक बड़ी नौसेना का निर्माण शुरू कर दिया था",
        3: "थल पर यूरोपीयों पर निर्णायक कार्रवाई कर सकते थे, यद्यपि समुद्र में उनकी बराबरी की नौसेना न थी",
    },
    "art-kutiyattam-kerala": {
        0: "कथकली का सबसे पुराना जीवित रूप है, जिससे आगे चलकर कथकली के मुखौटे और रंग-सज्जा विकसित हुए",
        1: "फ़सल के त्योहार के समय खुले चौकों में गाँव की नाट्य-मंडलियों द्वारा तमिल भाषा में खेला जाता है",
        2: "केरल के मंदिर-रंगमंचों में संस्कृत नाटक जीवित रखता है; इसमें स्त्री-पात्र स्त्रियाँ निभाती हैं",
    },
    "econ-money-multiplier-currency-ratio": {
        1: "जनता द्वारा नकदी के रूप में रखी गई मुद्रा के अनुपात में कमी",
        3: "किसी त्योहार के मौसम के दौरान बैंकों से नकदी की निकासी में वृद्धि",
    },
    "ex-world-investment-report": {
        3: "अंकटाड (UNCTAD)",
    },
    "en-otec": {
        1: "ऐसी उथली खाड़ियों में जहाँ ऊँचे ज्वार और निम्न ज्वार के बीच का अंतर सबसे अधिक होता है",
        3: "उष्णकटिबंधीय समुद्रों में, जहाँ सतह का जल गहरे जल से बहुत अधिक गर्म है",
    },
    "ancient-jataka-tales": {
        0: "मगध के राजाओं के उत्तराधिकार के ठीक-ठीक क्रम और उनकी सही तिथियों का",
        2: "अश्वमेध जैसे बड़े वैदिक यज्ञों को संपन्न करने के विधि-नियमों का",
        3: "अपने युग के सामाजिक-आर्थिक जीवन का -- व्यापार, शिल्प, श्रेणियाँ",
    },
    "igeo-western-ghats-order": {
        0: "सह्याद्रि - नीलगिरि - अन्नामलाई - इलायची",
    },
    "ancient-tirthankara-meaning": {
        0: "'घाट बनाने वाला', जो पुनर्जन्म की धारा पार करने की राह दिखाता है",
        1: "एक गृहस्थ अनुयायी जिसने गृहस्थों के लिए निर्धारित बारह लघु व्रत ग्रहण किए हैं",
    },
    "elections-corrupt-practice-vs-offence": {
        1: "उम्मीदवार के धर्म या जाति के नाम पर अपील करके मतदाताओं से मत माँगना",
        3: "मतदान समाप्ति से पहले के 48 घंटों में सार्वजनिक सभा करना",
    },
    "df-navy-submarines-easy": {
        0: "अपने सभी इंजन बंद करके, ताकि वह अपने-आप उतनी गहराई तक डूब जाए जितनी उसे चाहिए",
        1: "अपनी टंकियों में अतिरिक्त संपीडित हवा भरकर, जो पनडुब्बी के ढाँचे को नीचे की ओर धकेलती है",
        2: "अपनी गिट्टी टंकियों में समुद्री पानी भरकर, ताकि वह आकार के अनुपात में भारी हो जाए",
    },
    "ancient-junagadh-rock-inscription-rudradaman": {
        0: "सुदर्शन झील का निर्माण स्वयं अशोक ने सौराष्ट्र की शुष्क भूमि की सिंचाई के उद्देश्य से करवाया था",
        1: "विदेशी मूल के एक शासक ने गुप्तों से पहले ही राजकीय अभिलेखों में लंबी, परिष्कृत संस्कृत अपनाई",
        3: "ईसा की दूसरी सदी के मध्य तक सौराष्ट्र सातवाहन शासकों के अधीन आ चुका था",
    },
    "art-culture-tansen-dhrupad": {
        0: "आरंभ से अंत तक तीव्र गति में गाया जाता है, और इसके हर खंड में तेज़ अलंकारिक तानें होती हैं",
        2: "सूफ़ियों का एक भक्ति-गीत है, जिसे दरगाहों पर एक समूह (कोरस) द्वारा गाया जाता है",
        3: "कम अलंकरण वाले कठोर, गंभीर रूपों में बँधा है, और प्रायः देवों या राजाओं की स्तुति करता है",
    },
    "l1-his-prabhavati-gupta-land-grant": {
        0: "इसमें एक राजवंशी स्त्री अपने अधिकार से भूमि दान करती है, जबकि ग्रंथ स्त्रियों से भूमि रखने की अपेक्षा नहीं करते थे",
        2: "यह सिद्ध करता है कि वाकाटक राज्य का गुप्त साम्राज्य में विलय हो चुका था और अब उस पर गुप्त सम्राट सीधे शासन करते थे",
        3: "यह भारत में किसी भी शासक द्वारा किसी बौद्ध विहार को दिए गए सबसे पहले भूमि-अनुदान को दर्ज करता है",
    },
    "l1-env-polyblend-plastic-roads": {
        0: "उसे पॉलीब्लेंड चूर्ण बनाकर, जिसे सड़क बिछाने में बिटुमेन से मिलाते हैं",
        1: "उसे बड़े-बड़े बिजलीघरों में जलाकर पूरे नगर के लिए बिजली का उत्पादन करके",
        2: "उसे ऑक्सीजन की अनुपस्थिति में गर्म करके डीज़ल ईंधन में परिवर्तित करके",
    },
    "l1-eco-paradox-of-thrift": {
        1: "से का बाज़ार नियम",
        2: "मितव्ययिता का विरोधाभास",
    },
    "l1-eco-marketed-surplus": {
        1: "विपणित अधिशेष",
    },
}

POONA = "modern-poona-pact-1932"
POONA_S1 = "It was agreed upon while Mahatma Gandhi was on a fast in Yerwada jail against separate electorates for the Depressed Classes."
POONA_S1_HI = "यह तब तय हुआ जब महात्मा गांधी दलित वर्गों के पृथक निर्वाचन के विरुद्ध यरवदा जेल में अनशन पर थे।"
POONA_E1_OLD = ("Statement 1 is correct: the Poona Pact (24 September 1932) was signed between Mahatma Gandhi, fasting in Yerwada "
                "Central Jail against separate electorates for the Depressed Classes, and Dr. B. R. Ambedkar, who represented the Depressed Classes.")
POONA_E1 = ("Statement 1 is correct: the Poona Pact (24 September 1932) was reached to end the fast that Mahatma Gandhi had begun in "
            "Yerwada Central Jail against separate electorates for the Depressed Classes. Dr. B. R. Ambedkar signed it for the Depressed "
            "Classes and Madan Mohan Malaviya for the caste Hindus; Gandhi himself was not a signatory, though he accepted the Pact and "
            "broke his fast once the British government approved it.")
POONA_E1_HI_OLD = ("कथन 1 सही है: पूना समझौता (24 सितंबर 1932) दलित वर्गों के पृथक निर्वाचन के विरुद्ध यरवदा केंद्रीय जेल में अनशन कर रहे "
                   "महात्मा गांधी और दलित वर्गों का प्रतिनिधित्व कर रहे डॉ. बी.आर. आंबेडकर के बीच हुआ।")
POONA_E1_HI = ("कथन 1 सही है: पूना समझौता (24 सितंबर 1932) उस अनशन को समाप्त कराने के लिए हुआ जो महात्मा गांधी ने दलित वर्गों के पृथक "
               "निर्वाचन के विरुद्ध यरवदा केंद्रीय जेल में शुरू किया था। दलित वर्गों की ओर से डॉ. बी.आर. आंबेडकर और सवर्ण हिंदुओं की ओर से "
               "मदन मोहन मालवीय ने इस पर हस्ताक्षर किए; गांधी स्वयं हस्ताक्षरकर्ता नहीं थे, यद्यपि उन्होंने समझौते को स्वीकार किया और "
               "ब्रिटिश सरकार की स्वीकृति मिलने पर अपना अनशन तोड़ा।")

IDS = ("ancient-ashokan-edicts-script", POONA)


def q(s):
    return "'" + s.replace("'", "''") + "'"


def main(path):
    Q = {r["concept_group_id"]: r for r in json.load(io.open(path, encoding="utf-8"))}
    out = []
    for cg, fix in HI.items():
        r = Q[cg]
        ops = json.loads(json.dumps(r["options"]))
        k = [i for i, o in enumerate(ops) if o["isCorrect"]][0]
        for i, t in fix.items():
            assert ops[i]["body_hi"] != t, (cg, i)
            ops[i]["body_hi"] = t
        L = [len(o["body_hi"]) for o in ops]
        assert L[k] <= max(l for i, l in enumerate(L) if i != k), (cg, L, k)
        print(f"{cg}: hi {L} key {'abcd'[k]}")
        out.append((r, ops, None))
    for cg in IDS:
        r = Q[cg]
        ops = json.loads(json.dumps(r["options"]))
        for i, o in enumerate(ops):
            assert o["id"].endswith("abcd"[i]), (cg, o["id"])
            o["id"] = "abcd"[i]
        out.append((r, ops, None))
    stmts = []
    for r, ops, _ in out:
        stmts.append(f"update public.questions set options = {q(json.dumps(ops, ensure_ascii=False))}::jsonb, updated_at = now() "
                     f"where exam_category = 'upsc' and id = {q(r['id'])} and options = {q(json.dumps(r['options'], ensure_ascii=False))}::jsonb "
                     "returning concept_group_id;")
    r = Q[POONA]
    qd = json.loads(json.dumps(r["question_data"]))
    qd["statements"][0] = POONA_S1
    qd["statements_hi"][0] = POONA_S1_HI
    assert r["explanation"].startswith(POONA_E1_OLD) and r["explanation_hi"].startswith(POONA_E1_HI_OLD)
    e = POONA_E1 + r["explanation"][len(POONA_E1_OLD):]
    ehi = POONA_E1_HI + r["explanation_hi"][len(POONA_E1_HI_OLD):]
    stmts.append(f"update public.questions set question_data = {q(json.dumps(qd, ensure_ascii=False))}::jsonb, explanation = {q(e)}, "
                 f"explanation_hi = {q(ehi)}, updated_at = now() where exam_category = 'upsc' and id = {q(r['id'])} "
                 f"and question_data = {q(json.dumps(r['question_data'], ensure_ascii=False))}::jsonb returning concept_group_id;")
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "audit_fixes_2026_11.sql"), "w", encoding="utf-8", newline="\n").write(
        "begin;\n" + "\n".join(stmts) + "\ncommit;\n")
    print(len(stmts), "updates")


if __name__ == "__main__":
    main(sys.argv[1])
