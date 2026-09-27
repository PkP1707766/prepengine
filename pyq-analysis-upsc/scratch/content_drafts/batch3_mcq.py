# -*- coding: utf-8 -*-
"""Batch 3: medium/mcq/Modern (6) + medium/mcq/Ancient (7) = 13 questions."""

def sql_str(s):
    return "'" + s.replace("'", "''") + "'"

def build_options_json(bodies, correct_idx):
    import json
    arr = []
    for i, b in enumerate(bodies):
        arr.append({"id": ["a", "b", "c", "d"][i], "body": b, "isCorrect": (i == correct_idx)})
    return json.dumps(arr)

def q_row(subject, topic, qtype, difficulty, body, options_bodies, correct_idx, marks_c, marks_w, explanation, concept_group_id, source_type, source_citation, status="draft"):
    options_json = build_options_json(options_bodies, correct_idx)
    return (
        "('upsc'," + sql_str(subject) + "," + sql_str(topic) + "," + sql_str(qtype) + "," + sql_str(difficulty) + ","
        + sql_str(body) + ",'{}'::jsonb," + sql_str(options_json) + "::jsonb," + str(marks_c) + "," + str(marks_w) + ","
        + sql_str(explanation) + "," + sql_str(concept_group_id) + "," + sql_str(source_type) + ","
        + sql_str(source_citation) + "," + sql_str(status) + ")"
    )

rows = []

# ---- MODERN MCQ (medium) x6 ----

rows.append(q_row(
    "History", "Modern", "mcq", "medium",
    "The Champaran Satyagraha (1917), Mahatma Gandhi's first satyagraha within India, was directed against which system of forced indigo cultivation imposed on peasants?",
    ["Tinkathia system", "Permanent Settlement", "Ryotwari System", "Mahalwari System"], 0,
    2, 0.66,
    "The Tinkathia system forced Champaran peasants to grow indigo on 3/20th (roughly 3 kathas per bigha) of their land for European planters, at prices fixed by the planters. Gandhi's 1917 inquiry into these grievances was his first satyagraha on Indian soil. The Permanent Settlement, Ryotwari and Mahalwari systems are colonial land-revenue arrangements, not cultivation mandates, and are unrelated to the Champaran grievance.",
    "modern-champaran-satyagraha-1917", "original_pattern_matched",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on Gandhi's early movements in India."
))

rows.append(q_row(
    "History", "Modern", "mcq", "medium",
    "The Non-Cooperation Movement (1920-22) was called off by Mahatma Gandhi in the immediate aftermath of which incident?",
    ["Jallianwala Bagh massacre", "Chauri Chaura incident", "Moplah Rebellion", "Kakori Conspiracy"], 1,
    2, 0.66,
    "Gandhi withdrew the Non-Cooperation Movement in February 1922 after a violent mob at Chauri Chaura (United Provinces) killed 22 policemen, which he felt violated the movement's commitment to non-violence. The Jallianwala Bagh massacre (1919) predates and helped provoke the movement rather than end it; the Moplah Rebellion (1921) was a separate, communally-inflected uprising in Malabar; the Kakori Conspiracy (1925) was a later revolutionary action unconnected to the NCM's withdrawal.",
    "modern-non-cooperation-chauri-chaura", "original_pattern_matched",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Non-Cooperation Movement."
))

rows.append(q_row(
    "History", "Modern", "mcq", "medium",
    "The Indian National Congress formally split into 'Moderate' and 'Extremist' factions at which session, often referred to as the Surat Split?",
    ["Calcutta Session, 1906", "Surat Session, 1907", "Nagpur Session, 1920", "Lahore Session, 1929"], 1,
    2, 0.66,
    "The Surat Session of 1907 saw the open split between the Moderates (led by figures like Gokhale) and Extremists (led by Tilak and others) over leadership and methods. The Calcutta Session (1906) had earlier adopted the Swadeshi/Boycott resolutions but did not itself produce the split; the Nagpur Session (1920) adopted the Non-Cooperation programme; the Lahore Session (1929) passed the Purna Swaraj resolution.",
    "modern-surat-split-1907", "original_pattern_matched",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Moderate-Extremist split."
))

rows.append(q_row(
    "History", "Modern", "mcq", "medium",
    "The All India Muslim League, founded in 1906 at Dacca, had which person appointed as its first President?",
    ["Muhammad Ali Jinnah", "Nawab Salimullah Khan", "Aga Khan III", "Syed Ahmed Khan"], 2,
    2, 0.66,
    "Aga Khan III was elected the first President of the All India Muslim League at its founding in Dacca in December 1906. Nawab Salimullah Khan hosted and was a key organiser of the founding meeting but was not its first president. Jinnah joined and later led the League, but only years afterward. Syed Ahmed Khan, associated with the Aligarh movement, had died in 1898, before the League was formed.",
    "modern-muslim-league-founding-1906", "original_pattern_matched",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on communal politics and the founding of the Muslim League."
))

rows.append(q_row(
    "History", "Modern", "mcq", "medium",
    "Lord Curzon's partition of Bengal, announced in 1905, was annulled by the colonial government in which year?",
    ["1908", "1911", "1919", "1935"], 1,
    2, 0.66,
    "The partition of Bengal was annulled in 1911, announced at the Delhi Durbar, following sustained Swadeshi-era agitation. 1908 falls within the agitation period itself, not the annulment; 1919 and 1935 relate to unrelated later constitutional reforms (Government of India Acts).",
    "modern-partition-of-bengal-annulment", "original_pattern_matched",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Swadeshi Movement and partition of Bengal."
))

rows.append(q_row(
    "History", "Modern", "mcq", "medium",
    "In the Individual Satyagraha launched by Mahatma Gandhi in October 1940, who was selected as the first individual satyagrahi?",
    ["Jawaharlal Nehru", "Vinoba Bhave", "Rajendra Prasad", "Sardar Vallabhbhai Patel"], 1,
    2, 0.66,
    "Vinoba Bhave was chosen by Gandhi as the first individual satyagrahi in October 1940, offering token anti-war resistance on an individual basis rather than through mass mobilisation. Jawaharlal Nehru was selected as the second satyagrahi in the sequence, not the first -- a detail that is a common source of confusion.",
    "modern-individual-satyagraha-1940", "original_pattern_matched",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Individual Satyagraha."
))

# ---- ANCIENT MCQ (medium) x7 ----

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "Bindusara, the second Mauryan emperor and father of Ashoka, is referred to in Greek accounts by which title/name?",
    ["Sandrocottus", "Amitrochates", "Devanampiya", "Piyadasi"], 1,
    2, 0.66,
    "Greek writers referred to Bindusara as 'Amitrochates' (a Hellenised rendering of 'Amitraghata', roughly 'slayer of foes'). 'Sandrocottus' is the Greek name for Chandragupta Maurya, Bindusara's father, not Bindusara himself. 'Devanampiya' and 'Piyadasi' are epithets associated with Ashoka in his edicts.",
    "ancient-bindusara-mauryan-empire", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Mauryan Empire."
))

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "The Saka Era, used alongside the Gregorian calendar in the Indian national calendar, is traditionally dated to 78 CE and associated with the accession of which ruler?",
    ["Kanishka", "Chandragupta II", "Kadphises I", "Rudradaman I"], 0,
    2, 0.66,
    "The Saka Era of 78 CE is conventionally linked to the accession of the Kushan ruler Kanishka, despite the era's name suggesting a Saka origin. Rudradaman I was a Western Kshatrapa (Saka) ruler and a plausible-sounding distractor precisely because of the era's name, but he is not the ruler credited with its introduction. Chandragupta II and Kadphises I belong to different dynasties and periods.",
    "ancient-saka-era-kanishka", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Kushans."
))

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "According to the Nashik Prashasti inscription of Gautami Balashri, her son Gautamiputra Satakarni of the Satavahana dynasty defeated which Saka ruler?",
    ["Rudradaman I", "Menander", "Kanishka", "Nahapana"], 3,
    2, 0.66,
    "The Nashik Prashasti records Gautamiputra Satakarni's defeat of the Western Kshatrapa (Saka) ruler Nahapana. Rudradaman I is a related but distinct figure -- in fact he later defeated the Satavahanas in turn, the reverse of this event, which makes him a common point of confusion here. Menander was an earlier Indo-Greek king, and Kanishka was a Kushan ruler, unconnected to this specific engagement.",
    "ancient-gautamiputra-satakarni-nahapana", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Satavahanas."
))

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "Nalanda University, a major centre of ancient learning, is traditionally credited as having been founded under the patronage of which Gupta ruler?",
    ["Samudragupta", "Chandragupta II", "Kumaragupta I", "Skandagupta"], 2,
    2, 0.66,
    "Nalanda's founding is traditionally credited to Kumaragupta I in the early fifth century CE. Samudragupta and Chandragupta II preceded him and are associated with military expansion and the 'Vikramaditya' title respectively, while Skandagupta is chiefly remembered for repelling Huna invasions -- none of the three are credited with Nalanda's founding.",
    "ancient-nalanda-university-founding", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Gupta Empire and centres of learning."
))

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "Chandragupta II, who adopted the title 'Vikramaditya', is traditionally associated with a court that included nine distinguished scholars known as the:",
    ["Ashtapradhan", "Navaratnas", "Saptarishis", "Panchayatan"], 1,
    2, 0.66,
    "Chandragupta II's court is traditionally associated with the 'Navaratnas' (Nine Gems), a group of nine eminent scholars said to include Kalidasa. 'Ashtapradhan' refers to the eight-member council of ministers in the much later Maratha administration under Shivaji, an unrelated era. 'Saptarishis' refers to the seven sages of Puranic tradition, and 'Panchayatan' is a term from temple architecture, not court scholarship.",
    "ancient-chandragupta-ii-navaratnas", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Gupta Empire, Chandragupta II."
))

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "Megasthenes, the Greek ambassador whose account 'Indica' provides valuable information on Mauryan India, was sent to Chandragupta Maurya's court by which Hellenistic ruler?",
    ["Alexander the Great", "Seleucus I Nicator", "Antiochus I", "Ptolemy I"], 1,
    2, 0.66,
    "Megasthenes was sent as ambassador to Chandragupta Maurya's court by Seleucus I Nicator, one of Alexander's successors, following a treaty between the two rulers. Alexander the Great himself had died (323 BCE) before this embassy took place, making him a tempting but incorrect answer given his general association with this period of Indo-Greek contact. Antiochus I and Ptolemy I were contemporaries of Seleucus but not the ones who dispatched Megasthenes.",
    "ancient-megasthenes-seleucus-indica", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Mauryan Empire and foreign accounts."
))

rows.append(q_row(
    "History", "Ancient", "mcq", "medium",
    "The Sangam-era Tamil epic 'Silappadikaram', centred on the character Kannagi, is attributed to which author?",
    ["Sattanar", "Thiruvalluvar", "Ilango Adigal", "Nakkirar"], 2,
    2, 0.66,
    "The Silappadikaram is attributed to Ilango Adigal. Sattanar is the traditional author of the 'Manimekalai', a companion epic continuing the story of Kannagi's daughter, and is a common point of confusion given the thematic link between the two works. Thiruvalluvar is associated with the separate ethical text 'Tirukkural', and Nakkirar is a different Sangam-era poet.",
    "ancient-silappadikaram-sangam-literature", "original_pattern_matched",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Sangam Age and Tamil literature."
))

import os
statements = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements + "\n"
    "returning id, subject, topic, type, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch3_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
