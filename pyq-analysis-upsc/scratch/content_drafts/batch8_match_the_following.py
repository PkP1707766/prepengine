# -*- coding: utf-8 -*-
"""Batch 8: medium/match_the_following/Modern(3) + medium/match_the_following/Ancient(3) +
easy/match_the_following/Modern(2) + easy/match_the_following/Ancient(2) = 10 questions."""
import json, os

def sql_str(s):
    return "'" + s.replace("'", "''") + "'"

def mtf_options_json(bodies, correct_idx):
    arr = []
    for i, b in enumerate(bodies):
        arr.append({"id": ["a", "b", "c", "d"][i], "body": b, "isCorrect": (i == correct_idx)})
    return json.dumps(arr)

def mtf_row(subject, topic, difficulty, body, list1, list2, closing, option_bodies, correct_idx, explanation, concept_group_id, source_citation):
    qdata = json.dumps({"list_1": list1, "list_2": list2, "closing": closing})
    return (
        "('upsc'," + sql_str(subject) + "," + sql_str(topic) + ",'match_the_following'," + sql_str(difficulty) + ","
        + sql_str(body) + "," + sql_str(qdata) + "::jsonb," + sql_str(mtf_options_json(option_bodies, correct_idx)) + "::jsonb,"
        + "2,0.66," + sql_str(explanation) + "," + sql_str(concept_group_id) + ",'original_pattern_matched',"
        + sql_str(source_citation) + ",'draft')"
    )

rows = []

# ---- MODERN MEDIUM match_the_following (3) ----

rows.append(mtf_row(
    "History", "Modern", "medium",
    "Match List-I (Viceroy) with List-II (Event associated with their tenure):",
    ["A. Lord Curzon", "B. Lord Ripon", "C. Lord Irwin", "D. Lord Linlithgow"],
    ["1. Partition of Bengal (1905)", "2. Ilbert Bill controversy (1883)", "3. Civil Disobedience Movement / Dandi March (1930)", "4. August Offer (1940)"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-1, D-3"], 0,
    "The correct pairing is: Lord Curzon -- Partition of Bengal (1905); Lord Ripon -- Ilbert Bill controversy (1883); Lord Irwin -- Civil Disobedience Movement and the Dandi March (1930); Lord Linlithgow -- the August Offer (1940). Each viceroy is associated with a distinct, well-documented event of their tenure.",
    "modern-viceroys-events-match",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapters covering the viceroyalties from Ripon to Linlithgow."
))

rows.append(mtf_row(
    "History", "Modern", "medium",
    "Match List-I (Revolutionary/Leader) with List-II (Organisation they founded or led):",
    ["A. Bhagat Singh", "B. Surya Sen", "C. V. D. Savarkar", "D. Lala Hardayal"],
    ["1. Naujawan Bharat Sabha", "2. Led the Chittagong Armoury Raid group", "3. Abhinav Bharat Society", "4. Ghadar Party"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-3, B-2, C-1, D-4", "A-1, B-4, C-3, D-2", "A-2, B-1, C-4, D-3"], 0,
    "The correct pairing is: Bhagat Singh -- co-founder of the Naujawan Bharat Sabha; Surya Sen -- leader of the group behind the Chittagong Armoury Raid; V. D. Savarkar -- founder of the Abhinav Bharat Society; Lala Hardayal -- a founding figure of the Ghadar Party in the United States.",
    "modern-revolutionaries-organisations-match",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on revolutionary movements."
))

rows.append(mtf_row(
    "History", "Modern", "medium",
    "Match List-I (Legislation) with List-II (Key provision):",
    ["A. Indian Councils Act, 1909", "B. Government of India Act, 1919", "C. Government of India Act, 1935", "D. Indian Independence Act, 1947"],
    ["1. Introduced separate electorates for Muslims", "2. Introduced dyarchy in the provinces", "3. Provided for an All India Federation and provincial autonomy", "4. Partitioned British India into India and Pakistan"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-4, D-2", "A-3, B-2, C-1, D-4"], 0,
    "The correct pairing is: the 1909 Act (Morley-Minto reforms) introduced separate electorates for Muslims; the 1919 Act (Montagu-Chelmsford reforms) introduced dyarchy in the provinces; the 1935 Act proposed an All India Federation and provincial autonomy; and the 1947 Act partitioned British India into the dominions of India and Pakistan.",
    "modern-constitutional-acts-provisions-match",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on constitutional developments."
))

# ---- ANCIENT MEDIUM match_the_following (3) ----

rows.append(mtf_row(
    "History", "Ancient", "medium",
    "Match List-I (Dynasty) with List-II (Capital):",
    ["A. Mauryas", "B. Kushans", "C. Satavahanas", "D. Indo-Greeks (under Menander)"],
    ["1. Pataliputra", "2. Purushapura (Peshawar)", "3. Pratishthana (Paithan)", "4. Sagala (Sialkot)"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-1, B-3, C-2, D-4", "A-2, B-1, C-4, D-3", "A-4, B-2, C-3, D-1"], 0,
    "The correct pairing is: the Mauryas were centred at Pataliputra; the Kushans (under rulers like Kanishka) at Purushapura, present-day Peshawar; the Satavahanas at Pratishthana (Paithan) in the Deccan; and the Indo-Greeks, including Menander, at Sagala (present-day Sialkot).",
    "ancient-dynasties-capitals-match",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapters on the Mauryas, Kushans, Satavahanas and Indo-Greeks."
))

rows.append(mtf_row(
    "History", "Ancient", "medium",
    "Match List-I (Text) with List-II (Author):",
    ["A. Arthashastra", "B. Mudrarakshasa", "C. Indica", "D. Harshacharita"],
    ["1. Kautilya", "2. Vishakhadatta", "3. Megasthenes", "4. Banabhatta"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1", "A-2, B-1, C-4, D-3"], 0,
    "The correct pairing is: the Arthashastra is attributed to Kautilya; the Mudrarakshasa, a play about Chandragupta Maurya's rise, was written by Vishakhadatta; the Indica is the account of the Greek ambassador Megasthenes; and the Harshacharita, a biography of Harshavardhana, was written by his court poet Banabhatta.",
    "ancient-texts-authors-match",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapters on Mauryan and post-Gupta literary sources."
))

rows.append(mtf_row(
    "History", "Ancient", "medium",
    "Match List-I (Buddhist Council) with List-II (Venue):",
    ["A. First Buddhist Council", "B. Second Buddhist Council", "C. Third Buddhist Council", "D. Fourth Buddhist Council"],
    ["1. Rajagriha", "2. Vaishali", "3. Pataliputra", "4. Kundalavana (Kashmir)"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-3, B-2, C-1, D-4"], 0,
    "The correct pairing is: the First Council was held at Rajagriha, the Second at Vaishali, the Third (under Ashoka) at Pataliputra, and the Fourth (under Kanishka) at Kundalavana in Kashmir.",
    "ancient-buddhist-councils-venues-match",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the spread and councils of Buddhism."
))

# ---- MODERN EASY match_the_following (2) ----

rows.append(mtf_row(
    "History", "Modern", "easy",
    "Match List-I (Leader) with List-II (Newspaper/journal founded by them):",
    ["A. Bal Gangadhar Tilak", "B. Mahatma Gandhi", "C. Annie Besant", "D. Lala Lajpat Rai"],
    ["1. Kesari", "2. Young India", "3. New India", "4. The Punjabee"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-1, D-3"], 0,
    "The correct pairing is: Tilak founded Kesari; Gandhi founded Young India; Annie Besant founded New India; and Lala Lajpat Rai founded The Punjabee.",
    "modern-leaders-newspapers-match",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the nationalist press."
))

rows.append(mtf_row(
    "History", "Modern", "easy",
    "Match List-I (Event) with List-II (Year):",
    ["A. Formation of the Indian National Congress", "B. Partition of Bengal", "C. Jallianwala Bagh massacre", "D. Quit India Movement"],
    ["1. 1885", "2. 1905", "3. 1919", "4. 1942"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-1, D-3"], 0,
    "The correct pairing is: the Indian National Congress was formed in 1885, the Partition of Bengal was announced in 1905, the Jallianwala Bagh massacre occurred in 1919, and the Quit India Movement was launched in 1942.",
    "modern-events-years-match",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- general chronology of the freedom struggle."
))

# ---- ANCIENT EASY match_the_following (2) ----

rows.append(mtf_row(
    "History", "Ancient", "easy",
    "Match List-I (Indus Valley site) with List-II (Present-day location):",
    ["A. Harappa", "B. Mohenjodaro", "C. Lothal", "D. Kalibangan"],
    ["1. Punjab, Pakistan", "2. Sindh, Pakistan", "3. Gujarat, India", "4. Rajasthan, India"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-3, B-2, C-1, D-4"], 0,
    "The correct pairing is: Harappa is in Punjab, Pakistan; Mohenjodaro is in Sindh, Pakistan; Lothal is in Gujarat, India; and Kalibangan is in Rajasthan, India.",
    "ancient-indus-sites-locations-match",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Indus Valley Civilisation and its sites."
))

rows.append(mtf_row(
    "History", "Ancient", "easy",
    "Match List-I (Ruler) with List-II (Dynasty):",
    ["A. Chandragupta Maurya", "B. Kanishka", "C. Samudragupta", "D. Gautamiputra Satakarni"],
    ["1. Mauryan dynasty", "2. Kushan dynasty", "3. Gupta dynasty", "4. Satavahana dynasty"],
    "Select the correct answer using the codes given below:",
    ["A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-1, D-3"], 0,
    "The correct pairing is: Chandragupta Maurya belonged to the Mauryan dynasty, Kanishka to the Kushan dynasty, Samudragupta to the Gupta dynasty, and Gautamiputra Satakarni to the Satavahana dynasty.",
    "ancient-rulers-dynasties-match",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapters on the major ancient Indian dynasties."
))

statements_sql = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements_sql + "\n"
    "returning id, subject, topic, type, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch8_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
