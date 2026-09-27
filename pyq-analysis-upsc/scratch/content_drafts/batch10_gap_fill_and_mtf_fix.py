# -*- coding: utf-8 -*-
"""Batch 10: (a) INSERT the 11 gap-report cells still empty after batches 1-9,
(b) UPDATE the 10 existing match_the_following rows so the correct code is not always A-1,B-2,C-3,D-4."""
import json, os, random
from itertools import permutations

def sql_str(s):
    return "'" + s.replace("'", "''") + "'"

CLOSING = "Select the correct answer using the codes given below:"
STMT_OPTIONS = ["Only one", "Only two", "All three", "None"]

def stmt_options_json(correct_idx):
    return json.dumps([{"id": "abcd"[i], "body": b, "isCorrect": i == correct_idx} for i, b in enumerate(STMT_OPTIONS)])

def mcq_options_json(bodies, correct_idx):
    return json.dumps([{"id": "abcd"[i], "body": b, "isCorrect": i == correct_idx} for i, b in enumerate(bodies)])

def code_str(mapping):
    return ", ".join("%s-%d" % ("ABCD"[i], m) for i, m in enumerate(mapping))

def build_mtf(items, mapping, correct_pos, seed):
    """items[i] is the true partner of list_1[i]; mapping[i] = 1-based slot of that partner in the shown list_2."""
    assert sorted(mapping) == [1, 2, 3, 4] and list(mapping) != [1, 2, 3, 4]
    shown = [None] * 4
    for i, m in enumerate(mapping):
        shown[m - 1] = items[i]
    list_2 = ["%d. %s" % (k + 1, t) for k, t in enumerate(shown)]
    correct = tuple(mapping)
    rng = random.Random(seed)
    cands = [p for p in permutations([1, 2, 3, 4]) if sum(a == b for a, b in zip(p, correct)) in (1, 2)]
    wrong = rng.sample(cands, 3)
    bodies = [code_str(w) for w in wrong]
    bodies.insert(correct_pos, code_str(correct))
    assert len(set(bodies)) == 4
    return list_2, bodies

def stmt_row(topic, difficulty, body, statements, correct_idx, explanation, cg, cite):
    qdata = json.dumps({"statements": statements, "closing": "How many of the above statements are correct?"})
    return ("('upsc','History'," + sql_str(topic) + ",'statement_based'," + sql_str(difficulty) + "," + sql_str(body) + ","
            + sql_str(qdata) + "::jsonb," + sql_str(stmt_options_json(correct_idx)) + "::jsonb,2,0.66,"
            + sql_str(explanation) + "," + sql_str(cg) + ",'original_pattern_matched'," + sql_str(cite) + ",'draft')")

def mcq_row(topic, difficulty, body, bodies, correct_idx, explanation, cg, cite):
    return ("('upsc','History'," + sql_str(topic) + ",'mcq'," + sql_str(difficulty) + "," + sql_str(body) + ",'{}'::jsonb,"
            + sql_str(mcq_options_json(bodies, correct_idx)) + "::jsonb,2,0.66," + sql_str(explanation) + ","
            + sql_str(cg) + ",'original_pattern_matched'," + sql_str(cite) + ",'draft')")

def mtf_row(topic, difficulty, body, list_1, items, mapping, correct_pos, seed, explanation, cg, cite):
    list_2, bodies = build_mtf(items, mapping, correct_pos, seed)
    qdata = json.dumps({"list_1": list_1, "list_2": list_2, "closing": CLOSING})
    return ("('upsc','History'," + sql_str(topic) + ",'match_the_following'," + sql_str(difficulty) + "," + sql_str(body) + ","
            + sql_str(qdata) + "::jsonb," + sql_str(mcq_options_json(bodies, correct_pos)) + "::jsonb,2,0.66,"
            + sql_str(explanation) + "," + sql_str(cg) + ",'original_pattern_matched'," + sql_str(cite) + ",'draft')")

rows = []

# ---- 5 statement_based cells ----
rows.append(stmt_row(
    "Music & Dance", "easy", "Consider the following statements regarding Indian classical music and dance:",
    ["Kuchipudi, a classical dance form, originated in Andhra Pradesh.",
     "Sattriya, associated with the Vaishnava monasteries (Sattras) of Assam, was accorded classical dance status by the Sangeet Natak Akademi in 2000.",
     "Carnatic music is the classical music tradition of North India, while Hindustani music is the classical tradition of South India."],
    1,
    "Statements 1 and 2 are correct: Kuchipudi originated in Andhra Pradesh, and Sattriya, rooted in the Sattras of Assam, was recognised as a classical dance form in 2000. Statement 3 reverses the two traditions: Hindustani music is the classical tradition of North India and Carnatic music that of South India.",
    "art-culture-classical-music-dance-basics", "NCERT Fine Arts textbook -- chapter on the performing arts of India."))

rows.append(stmt_row(
    "Music & Dance", "hard", "Consider the following statements regarding the history of Hindustani vocal music:",
    ["Dhrupad received significant royal patronage from Raja Man Singh Tomar of Gwalior in the 15th-16th centuries.",
     "Khayal is described in detail in Bharata's Natya Shastra as a principal genre of vocal music.",
     "Sadarang (Niyamat Khan), a court musician under Aurangzeb, is credited with giving Khayal its refined classical form."],
    0,
    "Only statement 1 is correct: Raja Man Singh Tomar of Gwalior was a major patron of Dhrupad. Statement 2 is an anachronism: Khayal is a medieval genre and is not described in the Natya Shastra, an ancient treatise. Statement 3 swaps the ruler: Sadarang is associated with the court of Muhammad Shah 'Rangila' in the 18th century, not Aurangzeb, who is remembered for discouraging court music.",
    "art-culture-dhrupad-khayal-history", "NCERT Fine Arts textbook -- chapter on Hindustani classical music."))

rows.append(stmt_row(
    "Painting", "medium", "Consider the following statements regarding Pahari and Rajput schools of painting:",
    ["Basohli is regarded as the earliest of the Pahari schools of painting, noted for bold colours and strong lines.",
     "The Kangra school of Pahari painting flourished under the patronage of Raja Sawant Singh of Kishangarh.",
     "The 'Bani Thani' painting is associated with the Bundi school of Rajasthan."],
    0,
    "Only statement 1 is correct. Statement 2 swaps the patron: the Kangra school flourished under Raja Sansar Chand of Kangra, while Sawant Singh (Nagari Das) patronised the Kishangarh school. Statement 3 swaps the school: 'Bani Thani' is the celebrated Kishangarh portrait, attributed to the artist Nihal Chand, not a Bundi work.",
    "art-culture-pahari-rajput-painting-schools", "NCERT Fine Arts textbook -- chapter on Pahari and Rajput painting."))

rows.append(stmt_row(
    "Iconography", "medium", "Consider the following statements regarding Jain iconography:",
    ["Jain Tirthankara images are commonly distinguished by distinctive emblems (lanchhanas); the emblem of Rishabhanatha is the bull.",
     "Mahavira is typically depicted beneath a canopy of serpent hoods.",
     "The emblem associated with Mahavira is the elephant."],
    0,
    "Only statement 1 is correct: Tirthankaras are identified by lanchhanas, and Rishabhanatha's is the bull. Statement 2 swaps the Tirthankara: the serpent-hood canopy identifies Parshvanatha, not Mahavira. Statement 3 is also a swap: Mahavira's emblem is the lion, while the elephant is the emblem of Ajitanatha.",
    "art-culture-jain-iconography-lanchhana", "NCERT Fine Arts textbook -- chapter on Jain art and iconography."))

rows.append(stmt_row(
    "Architecture", "medium", "Consider the following statements regarding styles of Indian temple architecture:",
    ["The Nagara style is characterised by a pyramidal vimana and is chiefly associated with South India.",
     "The Dravida style is characterised by a curvilinear shikhara and is chiefly associated with North India.",
     "The Vesara style, a blend of Nagara and Dravida features, is found exclusively in Tamil Nadu."],
    3,
    "None of the statements is correct. Statements 1 and 2 swap the defining features and regions: the Nagara style has a curvilinear shikhara and is associated with North India, while the Dravida style has a pyramidal vimana and is associated with South India. Statement 3 misplaces the Vesara style, which developed mainly in Karnataka and the Deccan (for example under the Chalukyas and Hoysalas), not exclusively in Tamil Nadu.",
    "art-culture-temple-styles-nagara-dravida-vesara", "NCERT Fine Arts textbook -- chapter on temple architecture."))

# ---- 1 mcq cell ----
rows.append(mcq_row(
    "Medieval", "hard",
    "The 'Diwan-i-Mustakhraj', a department created to recover arrears of revenue, was established by which Delhi Sultan?",
    ["Balban", "Muhammad bin Tughlaq", "Firuz Shah Tughlaq", "Alauddin Khalji"], 3,
    "Alauddin Khalji set up the Diwan-i-Mustakhraj to recover arrears of revenue. The other departments are commonly confused with it: the Diwan-i-Amir-i-Kohi (agriculture) was created by Muhammad bin Tughlaq, the Diwan-i-Khairat (charity) and Diwan-i-Bandagan (slaves) by Firuz Shah Tughlaq, and Balban is associated with reorganising the military department, the Diwan-i-Arz.",
    "medieval-diwan-i-mustakhraj-alauddin", "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapters on the Khalji and Tughlaq administrations."))

# ---- 5 new match_the_following cells (list_2 scrambled; correct code is never A-1,B-2,C-3,D-4) ----
rows.append(mtf_row(
    "Medieval", "easy", "Match List-I (Mughal emperor) with List-II (Associated work or institution):",
    ["A. Babur", "B. Akbar", "C. Jahangir", "D. Shah Jahan"],
    ["Baburnama", "Din-i-Ilahi", "Chain of Justice (Zanjir-i-Adl)", "Peacock Throne"],
    [2, 4, 1, 3], 0, 9101,
    "The correct pairing is: Babur -- the Baburnama; Akbar -- Din-i-Ilahi; Jahangir -- the Chain of Justice; Shah Jahan -- the Peacock Throne.",
    "medieval-mughal-emperors-works-match", "NCERT, Themes in Indian History-II -- chapters on the Mughal emperors."))

rows.append(mtf_row(
    "Medieval", "medium", "Match List-I (Saint/poet) with List-II (Work):",
    ["A. Kabir", "B. Tulsidas", "C. Surdas", "D. Malik Muhammad Jayasi"],
    ["Bijak", "Ramcharitmanas", "Sur Sagar", "Padmavat"],
    [4, 1, 2, 3], 2, 9102,
    "The correct pairing is: Kabir -- the Bijak; Tulsidas -- the Ramcharitmanas; Surdas -- the Sur Sagar; Malik Muhammad Jayasi -- the Padmavat.",
    "medieval-bhakti-saints-works-match", "NCERT, Themes in Indian History-II -- chapter on the Bhakti and Sufi traditions."))

rows.append(mtf_row(
    "Modern", "hard", "Match List-I (Session of the Indian National Congress) with List-II (Presiding officer):",
    ["A. Surat (1907)", "B. Lucknow (1916)", "C. Nagpur (1920)", "D. Karachi (1931)"],
    ["Rash Behari Ghosh", "Ambika Charan Mazumdar", "C. Vijayaraghavachariar", "Vallabhbhai Patel"],
    [3, 4, 2, 1], 0, 9103,
    "The correct pairing is: the Surat session (1907) was presided over by Rash Behari Ghosh; Lucknow (1916) by Ambika Charan Mazumdar; Nagpur (1920) by C. Vijayaraghavachariar; and Karachi (1931) by Vallabhbhai Patel.",
    "modern-inc-sessions-presidents-match", "NCERT/Bipan Chandra, India's Struggle for Independence -- chronology of Congress sessions."))

rows.append(mtf_row(
    "Ancient", "hard", "Match List-I (Ruler) with List-II (Title/epithet associated with them):",
    ["A. Ashoka", "B. Samudragupta", "C. Chandragupta II", "D. Kanishka"],
    ["Devanampiya Piyadasi", "Kaviraja", "Vikramaditya", "Devaputra"],
    [2, 1, 4, 3], 1, 9104,
    "The correct pairing is: Ashoka -- Devanampiya Piyadasi (as in his edicts); Samudragupta -- Kaviraja (as in the Allahabad Prashasti); Chandragupta II -- Vikramaditya; Kanishka -- Devaputra, a title used by the Kushan kings.",
    "ancient-rulers-titles-match", "Old NCERT, Ancient India (R. S. Sharma) -- chapters on the Mauryas, Kushans and Guptas."))

rows.append(mtf_row(
    "Medieval", "hard", "Match List-I (Medieval work) with List-II (Author):",
    ["A. Tabaqat-i-Nasiri", "B. Fatawa-i-Jahandari", "C. Khazain-ul-Futuh", "D. Tuzuk-i-Jahangiri"],
    ["Minhaj-us-Siraj", "Ziauddin Barani", "Amir Khusrau", "Jahangir"],
    [3, 1, 4, 2], 2, 9105,
    "The correct pairing is: the Tabaqat-i-Nasiri was written by Minhaj-us-Siraj; the Fatawa-i-Jahandari by Ziauddin Barani; the Khazain-ul-Futuh by Amir Khusrau; and the Tuzuk-i-Jahangiri is the memoir of Emperor Jahangir.",
    "medieval-chronicles-authors-match", "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapters on medieval sources."))

insert_sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + ",\n".join(rows) + "\nreturning id, topic, type, difficulty;\n")

# ---- UPDATE the 10 existing MTF rows ----
existing = [
    ("modern-viceroys-events-match", ["A. Lord Curzon", "B. Lord Ripon", "C. Lord Irwin", "D. Lord Linlithgow"],
     ["Partition of Bengal (1905)", "Ilbert Bill controversy (1883)", "Civil Disobedience Movement / Dandi March (1930)", "August Offer (1940)"], [3, 1, 4, 2], 1),
    ("modern-revolutionaries-organisations-match", ["A. Bhagat Singh", "B. Surya Sen", "C. V. D. Savarkar", "D. Lala Hardayal"],
     ["Naujawan Bharat Sabha", "Led the Chittagong Armoury Raid group", "Abhinav Bharat Society", "Ghadar Party"], [2, 4, 1, 3], 3),
    ("modern-constitutional-acts-provisions-match", ["A. Indian Councils Act, 1909", "B. Government of India Act, 1919", "C. Government of India Act, 1935", "D. Indian Independence Act, 1947"],
     ["Introduced separate electorates for Muslims", "Introduced dyarchy in the provinces", "Provided for an All India Federation and provincial autonomy", "Partitioned British India into India and Pakistan"], [4, 3, 1, 2], 0),
    ("ancient-dynasties-capitals-match", ["A. Mauryas", "B. Kushans", "C. Satavahanas", "D. Indo-Greeks (under Menander)"],
     ["Pataliputra", "Purushapura (Peshawar)", "Pratishthana (Paithan)", "Sagala (Sialkot)"], [2, 1, 4, 3], 2),
    ("ancient-texts-authors-match", ["A. Arthashastra", "B. Mudrarakshasa", "C. Indica", "D. Harshacharita"],
     ["Kautilya", "Vishakhadatta", "Megasthenes", "Banabhatta"], [3, 4, 2, 1], 3),
    ("ancient-buddhist-councils-venues-match", ["A. First Buddhist Council", "B. Second Buddhist Council", "C. Third Buddhist Council", "D. Fourth Buddhist Council"],
     ["Rajagriha", "Vaishali", "Pataliputra", "Kundalavana (Kashmir)"], [4, 1, 2, 3], 1),
    ("modern-leaders-newspapers-match", ["A. Bal Gangadhar Tilak", "B. Mahatma Gandhi", "C. Annie Besant", "D. Lala Lajpat Rai"],
     ["Kesari", "Young India", "New India", "The Punjabee"], [2, 3, 4, 1], 0),
    ("modern-events-years-match", ["A. Formation of the Indian National Congress", "B. Partition of Bengal", "C. Jallianwala Bagh massacre", "D. Quit India Movement"],
     ["1885", "1905", "1919", "1942"], [3, 1, 4, 2], 2),
    ("ancient-indus-sites-locations-match", ["A. Harappa", "B. Mohenjodaro", "C. Lothal", "D. Kalibangan"],
     ["Punjab, Pakistan", "Sindh, Pakistan", "Gujarat, India", "Rajasthan, India"], [2, 4, 1, 3], 1),
    ("ancient-rulers-dynasties-match", ["A. Chandragupta Maurya", "B. Kanishka", "C. Samudragupta", "D. Gautamiputra Satakarni"],
     ["Mauryan dynasty", "Kushan dynasty", "Gupta dynasty", "Satavahana dynasty"], [4, 3, 1, 2], 3),
]
updates = []
for n, (cg, list_1, items, mapping, pos) in enumerate(existing):
    list_2, bodies = build_mtf(items, mapping, pos, 8100 + n)
    qdata = json.dumps({"list_1": list_1, "list_2": list_2, "closing": CLOSING})
    updates.append(
        "update public.questions set question_data = " + sql_str(qdata) + "::jsonb, options = "
        + sql_str(mcq_options_json(bodies, pos)) + "::jsonb, updated_at = now() where exam_category='upsc' and subject='History' and type='match_the_following' and concept_group_id = "
        + sql_str(cg) + ";")

here = os.path.dirname(__file__)
with open(os.path.join(here, "batch10_insert.sql"), "w", encoding="utf-8") as f:
    f.write(insert_sql)
with open(os.path.join(here, "batch10_mtf_updates.sql"), "w", encoding="utf-8") as f:
    f.write("\n".join(updates) + "\n")
print("insert rows:", len(rows), "| mtf updates:", len(updates))
