# -*- coding: utf-8 -*-
"""Batch 6: hard/statement_based/Ancient (5) + easy/mcq/Modern (4) + easy/mcq/Ancient (4) = 13 questions."""
import json, os

def sql_str(s):
    return "'" + s.replace("'", "''") + "'"

STMT_OPTIONS = ["Only one", "Only two", "All three", "None"]

def stmt_options_json(correct_idx):
    arr = []
    for i, b in enumerate(STMT_OPTIONS):
        arr.append({"id": ["a", "b", "c", "d"][i], "body": b, "isCorrect": (i == correct_idx)})
    return json.dumps(arr)

def build_mcq_options_json(bodies, correct_idx):
    arr = []
    for i, b in enumerate(bodies):
        arr.append({"id": ["a", "b", "c", "d"][i], "body": b, "isCorrect": (i == correct_idx)})
    return json.dumps(arr)

def stmt_row(subject, topic, difficulty, body, statements, closing, correct_idx, explanation, concept_group_id, source_citation):
    qdata = json.dumps({"statements": statements, "closing": closing})
    return (
        "('upsc'," + sql_str(subject) + "," + sql_str(topic) + ",'statement_based'," + sql_str(difficulty) + ","
        + sql_str(body) + "," + sql_str(qdata) + "::jsonb," + sql_str(stmt_options_json(correct_idx)) + "::jsonb,"
        + "2,0.66," + sql_str(explanation) + "," + sql_str(concept_group_id) + ",'original_pattern_matched',"
        + sql_str(source_citation) + ",'draft')"
    )

def mcq_row(subject, topic, difficulty, body, options_bodies, correct_idx, explanation, concept_group_id, source_citation):
    options_json = build_mcq_options_json(options_bodies, correct_idx)
    return (
        "('upsc'," + sql_str(subject) + "," + sql_str(topic) + ",'mcq'," + sql_str(difficulty) + ","
        + sql_str(body) + ",'{}'::jsonb," + sql_str(options_json) + "::jsonb,"
        + "2,0.66," + sql_str(explanation) + "," + sql_str(concept_group_id) + ",'original_pattern_matched',"
        + sql_str(source_citation) + ",'draft')"
    )

rows = []

# ---- ANCIENT HARD statement_based (5) ----

rows.append(stmt_row(
    "History", "Ancient", "hard",
    "Consider the following statements regarding the decline of the Mauryan Empire:",
    [
        "After Ashoka's death, the Mauryan Empire began to decline, with some accounts suggesting a partition of the empire among his successors, including Dasaratha and Samprati.",
        "The last Mauryan ruler, Brihadratha, was assassinated by his own commander-in-chief, Pushyamitra Shunga, who then founded the Shunga dynasty.",
        "Pushyamitra Shunga is regarded, without dispute among ancient and modern historians, as a devout patron of Buddhism who continued Ashoka's Dhamma policy without interruption.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the empire weakened and reportedly fragmented among Ashoka's successors, and Brihadratha, the last Mauryan, was killed by Pushyamitra Shunga, who founded the Shunga dynasty. Statement 3 is incorrect: Pushyamitra Shunga is traditionally associated with a Brahmanical revival, and some Buddhist sources (such as the Divyavadana) even allege hostility toward Buddhism under his rule -- the claim of undisputed, uninterrupted continuation of Ashoka's Dhamma policy does not hold.",
    "ancient-mauryan-decline-shunga",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the decline of the Mauryan Empire and the rise of the Shungas."
))

rows.append(stmt_row(
    "History", "Ancient", "hard",
    "Consider the following statements regarding Kushan-era art schools:",
    [
        "The Gandhara school of art, which flourished under Kushan patronage, shows strong Hellenistic/Greco-Roman influence in its depiction of the Buddha.",
        "The Mathura school of art developed largely indigenously and is generally considered to show more native Indian stylistic elements compared to Gandhara.",
        "Both the Gandhara and Mathura schools relied exclusively on red sandstone as their primary sculpting material.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Gandhara art reflects strong Greco-Roman influence, while Mathura art is considered more indigenous in style. Statement 3 is incorrect: the two schools used different materials -- Gandhara sculptures were typically carved from grey or bluish-grey schist, while Mathura sculptures characteristically used red sandstone, not both exclusively the same material.",
    "ancient-gandhara-mathura-art-schools",
    "NCERT Fine Arts textbook -- chapter on Kushan-era art; Old NCERT, Ancient India (R. S. Sharma)."
))

rows.append(stmt_row(
    "History", "Ancient", "hard",
    "Consider the following statements regarding the Sangam Age polity and economy:",
    [
        "Alongside the three major Sangam dynasties (Chera, Chola and Pandya), several minor chieftaincies known as the 'Velir' also existed across the Tamil region.",
        "The Sangam-age economy is understood to have relied significantly on trade with the Roman Empire, evidenced by finds of Roman gold coins at sites such as Arikamedu.",
        "Sangam texts indicate that a rigid, uniform four-fold varna system was universally practised across the entire Tamil region during this period.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the Velir chieftaincies existed alongside the three crowned Sangam dynasties, and Indo-Roman trade is well attested by finds such as Roman coins at Arikamedu. Statement 3 is incorrect: Sangam society had its own distinct social classifications rather than a rigid, uniformly enforced four-fold varna order across the region, with Brahmanical influence being only partial and gradual.",
    "ancient-sangam-polity-economy",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Sangam Age."
))

rows.append(stmt_row(
    "History", "Ancient", "hard",
    "Consider the following statements regarding Gupta-era trade and coinage:",
    [
        "Gupta gold coins, known as 'dinaras', depict rulers in various poses, including as archers, and are considered artistically sophisticated.",
        "Some historians point to a decline in long-distance trade and reduced gold coin circulation in the Later Gupta period as evidence of the empire's weakening economy.",
        "There is unanimous consensus among historians that the decline in overseas trade during the Gupta period was caused entirely by a single factor -- the Huna invasions -- with no other contributing cause.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Gupta gold dinaras, including archer-type coins, are noted for their artistry, and historians do cite reduced trade and coin circulation as evidence of later Gupta economic decline. Statement 3 is incorrect: there is no such unanimous single-cause consensus -- historians debate multiple contributing factors, including Huna invasions, disruptions in Roman trade, and internal administrative changes, rather than attributing the decline to one factor alone.",
    "ancient-gupta-trade-decline-debate",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Gupta economy and its decline."
))

rows.append(stmt_row(
    "History", "Ancient", "hard",
    "Consider the following statements regarding Harshavardhana's religious patronage:",
    [
        "Harshavardhana convened a religious assembly at Kannauj that is associated with honouring and propagating Mahayana Buddhist teachings.",
        "He also convened a quinquennial (once-in-five-years) assembly at Prayaga (Allahabad) for the distribution of charity.",
        "Harshavardhana's court exclusively patronised Buddhism and extended no patronage to Brahmanical or Jain traditions.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Harsha convened the Kannauj assembly associated with Mahayana Buddhism, and held the quinquennial Prayaga assembly for charitable distribution, both recorded by Xuanzang. Statement 3 is incorrect: Harsha's patronage was eclectic, extending to Shaivism and other Brahmanical traditions as well as Buddhism -- reflected even in his own plays, which invoke Shaiva themes, alongside his Buddhist-associated assemblies.",
    "ancient-harsha-religious-patronage",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on Harshavardhana."
))

# ---- MODERN EASY MCQ (4) ----

rows.append(mcq_row(
    "History", "Modern", "easy",
    "Who among the following is known as the 'Grand Old Man of India'?",
    ["Gopal Krishna Gokhale", "Dadabhai Naoroji", "Surendranath Banerjee", "Womesh Chandra Bonnerjee"], 1,
    "Dadabhai Naoroji is known as the 'Grand Old Man of India', a senior Moderate leader, author of 'Poverty and Un-British Rule in India' (the Drain Theory), and the first Indian to become a member of the British House of Commons. Gokhale, Banerjee and Bonnerjee were all prominent contemporaries but are not associated with this particular title.",
    "modern-dadabhai-naoroji-title",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on early nationalist leaders."
))

rows.append(mcq_row(
    "History", "Modern", "easy",
    "In which year was the Quit India Movement launched?",
    ["1940", "1942", "1930", "1945"], 1,
    "The Quit India Movement was launched in August 1942, following the failure of the Cripps Mission. 1940 marks the Individual Satyagraha, 1930 the launch of Civil Disobedience (Dandi March), and 1945 the Shimla Conference -- none of which is the Quit India launch year.",
    "modern-quit-india-year",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Quit India Movement."
))

rows.append(mcq_row(
    "History", "Modern", "easy",
    "'Vande Mataram', later adopted as India's national song, was composed by which of the following?",
    ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Muhammad Iqbal"], 1,
    "'Vande Mataram' was composed by Bankim Chandra Chatterjee, appearing in his 1882 novel Anandamath. Rabindranath Tagore notably set a portion of it to music and sang it at the 1896 Congress session, which is why he is often mistakenly credited as its composer, but authorship remains Bankim Chandra's. Sarojini Naidu and Muhammad Iqbal are unrelated to the song's composition.",
    "modern-vande-mataram-authorship",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on cultural nationalism."
))

rows.append(mcq_row(
    "History", "Modern", "easy",
    "Who was the first Governor-General of independent India (1947-48)?",
    ["C. Rajagopalachari", "Lord Wavell", "Lord Mountbatten", "Lord Linlithgow"], 2,
    "Lord Mountbatten served as the first Governor-General of independent India, from August 1947 until June 1948. C. Rajagopalachari succeeded him and is instead correctly remembered as the first (and only) Indian-born Governor-General of India -- a common point of confusion with 'first Governor-General of independent India'. Wavell and Linlithgow were earlier Viceroys under British rule, before independence.",
    "modern-first-governor-general-independent-india",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the transfer of power."
))

# ---- ANCIENT EASY MCQ (4) ----

rows.append(mcq_row(
    "History", "Ancient", "easy",
    "Who founded the Mauryan Empire?",
    ["Ashoka", "Bindusara", "Chandragupta Maurya", "Chanakya"], 2,
    "Chandragupta Maurya founded the Mauryan Empire around 321 BCE, guided by his mentor Chanakya (Kautilya). Bindusara and Ashoka were his son and grandson respectively, later rulers of the dynasty, while Chanakya was Chandragupta's chief advisor and strategist, not the founder-emperor himself.",
    "ancient-mauryan-empire-founder",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the rise of the Mauryan Empire."
))

rows.append(mcq_row(
    "History", "Ancient", "easy",
    "Which of the following is the oldest of the four Vedas?",
    ["Sama Veda", "Yajur Veda", "Rig Veda", "Atharva Veda"], 2,
    "The Rig Veda is the oldest of the four Vedas, primarily a collection of hymns. The Sama Veda, Yajur Veda and Atharva Veda were composed later, drawing in part on Rig Vedic material for liturgical and ritual purposes.",
    "ancient-oldest-veda",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Vedic Period."
))

rows.append(mcq_row(
    "History", "Ancient", "easy",
    "Which ancient Indian text, attributed to Kautilya, is a treatise on statecraft, economics and military strategy?",
    ["Manusmriti", "Mudrarakshasa", "Arthashastra", "Indica"], 2,
    "The Arthashastra, attributed to Kautilya (Chanakya), is a treatise on statecraft, economic policy and military strategy. The Manusmriti is a separate text on law and social conduct; the Mudrarakshasa is a Sanskrit play by Vishakhadatta about Chandragupta Maurya's rise to power, not a statecraft treatise itself; and the Indica is the account of the Greek ambassador Megasthenes, not an Indian text.",
    "ancient-arthashastra-authorship",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Mauryan Empire and Kautilya's Arthashastra."
))

rows.append(mcq_row(
    "History", "Ancient", "easy",
    "At which of the following places did Gautama Buddha deliver his first sermon after attaining enlightenment?",
    ["Bodh Gaya", "Kushinagar", "Sarnath", "Lumbini"], 2,
    "The Buddha delivered his first sermon (the Dharmachakra Pravartana, 'turning of the wheel of law') at Sarnath, near Varanasi. Bodh Gaya is where he attained enlightenment, Kushinagar is where he attained mahaparinirvana (death), and Lumbini is his birthplace -- each a genuine site associated with the Buddha's life, but tied to a different event.",
    "ancient-buddha-first-sermon-sarnath",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the life of the Buddha and Buddhist sites."
))

statements_sql = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements_sql + "\n"
    "returning id, subject, topic, type, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch6_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
