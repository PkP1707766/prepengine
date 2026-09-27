# -*- coding: utf-8 -*-
"""Batch 7: easy/statement_based/Medieval(3) + hard/statement_based/Medieval(3) +
medium/mcq/Medieval(3) + easy/mcq/Medieval(2) + hard/mcq/Modern(3) + hard/mcq/Ancient(3) = 17."""
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

# ---- MEDIEVAL EASY statement_based (3) ----

rows.append(stmt_row(
    "History", "Medieval", "easy",
    "Consider the following statements regarding Babur and the founding of the Mughal Empire:",
    [
        "Babur founded the Mughal Empire in India after defeating Ibrahim Lodi at the First Battle of Panipat in 1526.",
        "Babur made effective use of artillery and the Ottoman-style 'Tulughma' tactic in this battle.",
        "Babur's autobiography, the 'Baburnama', was originally written in Persian, his native language.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Babur defeated Ibrahim Lodi at the First Battle of Panipat (1526) using artillery and Tulughma flanking tactics. Statement 3 is incorrect: the Baburnama was originally written in Chagatai Turkish, Babur's native tongue, and was only later translated into Persian.",
    "medieval-babur-first-panipat-1526",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the founding of the Mughal Empire."
))

rows.append(stmt_row(
    "History", "Medieval", "easy",
    "Consider the following statements regarding the Sufi Chishti order in medieval India:",
    [
        "The Chishti order was introduced to India by Khwaja Moinuddin Chishti, who settled at Ajmer.",
        "Sufi saints typically lived in hospices called 'Khanqahs', which served as centres of spiritual and social activity.",
        "The Chishti order actively sought and accepted land grants and state patronage from Sultanate rulers as a central part of its practice.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Khwaja Moinuddin Chishti introduced the order at Ajmer, and Sufi saints commonly lived in Khanqahs. Statement 3 is incorrect: the Chishti order was known for deliberately avoiding state patronage and close association with political power -- a marked contrast with the Suhrawardi order, which did accept such patronage.",
    "medieval-chishti-sufi-order",
    "NCERT, Themes in Indian History-II -- chapter on the Bhakti and Sufi movements."
))

rows.append(stmt_row(
    "History", "Medieval", "easy",
    "Consider the following statements regarding Sher Shah Suri's administration:",
    [
        "Sher Shah Suri, who briefly displaced the Mughals, introduced a new silver currency called the 'Rupiya'.",
        "He is credited with constructing/renovating the Grand Trunk Road connecting Bengal to the Indus region.",
        "Sher Shah Suri's administrative reforms had no lasting influence on the later Mughal administration under Akbar.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Sher Shah Suri introduced the silver Rupiya and developed the Grand Trunk Road. Statement 3 is incorrect: his land revenue and currency reforms are widely regarded as having significantly influenced Akbar's later administrative system.",
    "medieval-sher-shah-suri-administration",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on Sher Shah Suri."
))

# ---- MEDIEVAL HARD statement_based (3) ----

rows.append(stmt_row(
    "History", "Medieval", "hard",
    "Consider the following statements regarding Kabir and the Bhakti-Sufi confluence:",
    [
        "Kabir's religious identity remains debated among scholars, with traditions pointing to both Hindu and Muslim influences, some holding that he was raised in a Muslim weaver family.",
        "The Sufi concept of 'Wahdat-ul-Wujud' (Unity of Being), associated with Ibn Arabi, found resonance among some Indian Sufi thinkers and is seen by some historians as paralleling certain Bhakti ideas of divine unity.",
        "There is unanimous scholarly agreement, with no historical dispute, that Kabir was formally initiated as a disciple of the Bhakti saint Ramananda.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Kabir's background and influences are genuinely debated, and Wahdat-ul-Wujud is noted by historians as a point of resonance with certain Bhakti ideas. Statement 3 is incorrect: Kabir's discipleship under Ramananda is itself a matter of historical and legendary uncertainty, not a point of unanimous, undisputed scholarly agreement.",
    "medieval-kabir-bhakti-sufi-confluence",
    "NCERT, Themes in Indian History-II -- chapter on the Bhakti and Sufi movements."
))

rows.append(stmt_row(
    "History", "Medieval", "hard",
    "Consider the following statements regarding Shivaji and Maratha administration:",
    [
        "Shivaji's coronation in 1674 at Raigad involved a formal Vedic ceremony, presided over by the Brahmin scholar Gaga Bhatt.",
        "Aurangzeb's prolonged Deccan campaigns against the Marathas, occupying much of the later part of his reign, are generally seen by historians as a major drain on Mughal resources and stability.",
        "Shivaji's administrative council, the 'Ashtapradhan', consisted of eight ministers, all of whom held hereditary, non-transferable positions passed down within fixed families.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Gaga Bhatt presided over Shivaji's 1674 coronation, and Aurangzeb's extended Deccan campaigns are widely regarded as having drained Mughal resources. Statement 3 is incorrect: Ashtapradhan positions were generally appointive rather than hereditary, made at the king's discretion on the basis of merit, unlike older hereditary offices.",
    "medieval-shivaji-maratha-administration",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the rise of the Marathas."
))

rows.append(stmt_row(
    "History", "Medieval", "hard",
    "Consider the following statements regarding Akbar's religious policy:",
    [
        "'Sulh-i-Kul' (peace with all), a broader policy principle of religious tolerance under Akbar, is often confused with but is distinct from 'Din-i-Ilahi', his more specific syncretic religious order.",
        "The Ain-i-Akbari, part of the Akbarnama compiled by Abul Fazl, provides detailed administrative and statistical information about Akbar's empire.",
        "Akbar himself never personally attended or participated in the interfaith religious discussions held at the Ibadat Khana (House of Worship) in Fatehpur Sikri.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Sulh-i-Kul and Din-i-Ilahi are related but distinct, and the Ain-i-Akbari (part of Abul Fazl's Akbarnama) is a key administrative and statistical source. Statement 3 is incorrect: Akbar actively participated in and personally hosted interfaith discussions at the Ibadat Khana, a well-documented feature of his religious policy.",
    "medieval-akbar-sulh-i-kul-ibadat-khana",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on Akbar's religious policy."
))

# ---- MEDIEVAL MEDIUM mcq (3) ----

rows.append(mcq_row(
    "History", "Medieval", "medium",
    "Who was the founder of the Mughal Empire in India?",
    ["Humayun", "Babur", "Akbar", "Sher Shah Suri"], 1,
    "Babur founded the Mughal Empire in India in 1526, after his victory at the First Battle of Panipat. Humayun was his son and successor (who briefly lost and later regained the throne), Akbar was his grandson who greatly expanded and consolidated the empire, and Sher Shah Suri was the Afghan ruler who temporarily displaced the Mughals between Humayun's two reigns.",
    "medieval-mughal-empire-founder",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the founding of the Mughal Empire."
))

rows.append(mcq_row(
    "History", "Medieval", "medium",
    "The 'Iqta' system, an important feature of Delhi Sultanate administration, primarily referred to which of the following?",
    ["A tax levied specifically on non-Muslim subjects", "A territorial assignment of land revenue given to nobles/officers in lieu of salary", "A hereditary system of permanent land ownership for peasants", "A military rank system denoting cavalry strength"], 1,
    "The Iqta system involved assigning territorial units to nobles and officers, who collected land revenue from them in lieu of a cash salary, in return for military and administrative service. It is distinct from the jizya (a tax on non-Muslims), was not a system of hereditary peasant land ownership, and is distinct from the Mansabdari rank system, which is a later Mughal institution.",
    "medieval-iqta-system-delhi-sultanate",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on Delhi Sultanate administration."
))

rows.append(mcq_row(
    "History", "Medieval", "medium",
    "Guru Arjan Dev, the fifth Sikh Guru, is credited with which of the following?",
    ["Founding the Khalsa Panth", "Founding the Sikh faith", "Compiling the Adi Granth and constructing the Harmandir Sahib (Golden Temple) at Amritsar", "Founding the city of Amritsar"], 2,
    "Guru Arjan Dev compiled the Adi Granth (the core scripture later expanded into the Guru Granth Sahib) and built the Harmandir Sahib at Amritsar. The Khalsa Panth was founded later by Guru Gobind Singh, the Sikh faith itself was founded by Guru Nanak, and the city of Amritsar was founded earlier by Guru Ram Das, Arjan Dev's father -- each a distinct contribution by a different Guru, commonly confused with one another.",
    "medieval-guru-arjan-dev-adi-granth",
    "NCERT, Themes in Indian History-II -- chapter on the Sikh Gurus and the development of Sikhism."
))

# ---- MEDIEVAL EASY mcq (2) ----

rows.append(mcq_row(
    "History", "Medieval", "easy",
    "Which Mughal emperor built the Taj Mahal?",
    ["Akbar", "Jahangir", "Shah Jahan", "Aurangzeb"], 2,
    "The Taj Mahal was built by Shah Jahan in memory of his wife, Mumtaz Mahal. Akbar and Jahangir preceded Shah Jahan, and Aurangzeb was his son and successor -- none of the three is associated with the Taj Mahal's construction.",
    "medieval-taj-mahal-shah-jahan",
    "NCERT, Themes in Indian History-II -- chapter on Mughal architecture."
))

rows.append(mcq_row(
    "History", "Medieval", "easy",
    "The First Battle of Panipat (1526), which laid the foundation of Mughal rule in India, was fought between Babur and which ruler?",
    ["Rana Sanga", "Sher Shah Suri", "Ibrahim Lodi", "Humayun"], 2,
    "The First Battle of Panipat (1526) was fought between Babur and Ibrahim Lodi, the last ruler of the Delhi Sultanate's Lodi dynasty, whom Babur defeated. Rana Sanga was defeated by Babur in a separate, later battle (Khanwa, 1527); Sher Shah Suri rose to prominence afterward, during Humayun's reign; and Humayun was Babur's own son, not an opposing ruler.",
    "medieval-first-battle-panipat-1526",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the founding of the Mughal Empire."
))

# ---- MODERN HARD mcq (3) ----

rows.append(mcq_row(
    "History", "Modern", "hard",
    "The 'Pact of 1932' between Mahatma Gandhi and B. R. Ambedkar, which replaced separate electorates for the Depressed Classes with a system of reserved seats within the general electorate, is known as the:",
    ["Lucknow Pact", "Gandhi-Irwin Pact", "Poona Pact", "Delhi Pact"], 2,
    "The Poona Pact (1932) replaced the Communal Award's separate electorates for the Depressed Classes with reserved seats to be filled through joint electorates, following Gandhi's fast against separate electorates. The Lucknow Pact (1916) concerned Congress-League cooperation; the Gandhi-Irwin Pact (1931) concerned the suspension of Civil Disobedience; and 'Delhi Pact' is another name sometimes loosely applied to the Gandhi-Irwin Pact, not this agreement.",
    "modern-poona-pact-naming-hard",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Communal Award and the Poona Pact."
))

rows.append(mcq_row(
    "History", "Modern", "hard",
    "The 'August Kranti' (August Revolution) of 1942 is an alternative name most closely associated with which movement?",
    ["Non-Cooperation Movement", "Civil Disobedience Movement", "Quit India Movement", "Individual Satyagraha"], 2,
    "'August Kranti' refers to the Quit India Movement, launched in August 1942 after the AICC's Bombay resolution and Gandhi's 'Do or Die' call. The Non-Cooperation Movement (1920-22) and Civil Disobedience Movement (1930-34) belong to earlier phases of the struggle, and the Individual Satyagraha (1940) was a more limited, symbolic campaign preceding Quit India.",
    "modern-august-kranti-quit-india",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Quit India Movement."
))

rows.append(mcq_row(
    "History", "Modern", "hard",
    "The 'Karachi Resolution' of the Indian National Congress, passed in 1931, is chiefly significant for which of the following?",
    ["It formally adopted the demand for Purna Swaraj (complete independence)", "It laid down the Congress's vision of Fundamental Rights and economic policy for a future free India", "It ratified the Gandhi-Irwin Pact and endorsed the suspension of Civil Disobedience", "It formally split the Congress into Moderate and Extremist factions"], 1,
    "The Karachi Resolution (1931) is chiefly remembered for articulating the Congress's vision of Fundamental Rights and a broad economic and social policy programme for a future independent India. The Purna Swaraj demand had already been adopted earlier, at the Lahore Session (1929); ratifying the Gandhi-Irwin Pact was a related but separate agenda item at the same Karachi session, not the resolution's chief significance; and the Moderate-Extremist split occurred decades earlier, at Surat (1907).",
    "modern-karachi-resolution-1931",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Karachi Session and Fundamental Rights resolution."
))

# ---- ANCIENT HARD mcq (3) ----

rows.append(mcq_row(
    "History", "Ancient", "hard",
    "The Junagadh Rock Inscription, one of the earliest known Sanskrit inscriptions of significant length, was issued by which ruler and is notable for recording repairs to which structure?",
    ["Ashoka; the Barabar Caves", "Rudradaman I; the Sudarshana Lake", "Samudragupta; the Mehrauli Iron Pillar", "Kharavela; the Hathigumpha Caves"], 1,
    "The Junagadh Rock Inscription was issued by the Western Kshatrapa (Saka) ruler Rudradaman I and records his repair of the Sudarshana Lake, originally built under the Mauryas. Ashoka's rock edicts are a separate body of inscriptions, mostly in Prakrit rather than the polished Sanskrit of this inscription; Samudragupta is associated with the Allahabad Prashasti and the Mehrauli Iron Pillar inscription is linked to a Chandra (traditionally identified with Chandragupta II); and Kharavela's Hathigumpha inscription is a separate Kalinga-related record.",
    "ancient-junagadh-rock-inscription-rudradaman",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Western Kshatrapas and epigraphic sources."
))

rows.append(mcq_row(
    "History", "Ancient", "hard",
    "The Allahabad Prashasti (Pillar Inscription), composed by Harishena, is a key source for the reign and military campaigns of which Gupta ruler?",
    ["Chandragupta I", "Samudragupta", "Chandragupta II", "Kumaragupta I"], 1,
    "The Allahabad Prashasti, composed by the court poet Harishena, eulogises Samudragupta's military campaigns and is a principal source for reconstructing the extent of his conquests. Chandragupta I was Samudragupta's father and predecessor; Chandragupta II and Kumaragupta I were later Gupta rulers, whose reigns are documented through separate, distinct inscriptions.",
    "ancient-allahabad-prashasti-samudragupta",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Gupta Empire and Samudragupta's conquests."
))

rows.append(mcq_row(
    "History", "Ancient", "hard",
    "The Hathigumpha Inscription, an important source for the political history of ancient Kalinga, was issued by which ruler?",
    ["Kharavela", "Rudradaman I", "Ashoka", "Gautamiputra Satakarni"], 0,
    "The Hathigumpha Inscription, found near Bhubaneswar, was issued by Kharavela, the Chedi/Mahameghavahana ruler of Kalinga, and details his reign and military campaigns. Rudradaman I's comparable inscription is the Junagadh Rock Inscription; Ashoka's Kalinga-related edicts (the Separate Kalinga Edicts) are a distinct set of records from an earlier period, prior to Kharavela; and Gautamiputra Satakarni is associated with the Nashik Prashasti, unrelated to Kalinga.",
    "ancient-hathigumpha-inscription-kharavela",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on post-Mauryan regional kingdoms."
))

statements_sql = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements_sql + "\n"
    "returning id, subject, topic, type, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch7_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
