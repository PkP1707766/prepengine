# -*- coding: utf-8 -*-
"""Batch 9: the 11 singleton Art & Culture cells --
Music & Dance(3), Painting(2), Iconography(2), Architecture(3), Culture-Other(1)."""
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

# ---- MUSIC & DANCE (3) ----

rows.append(mcq_row(
    "History", "Music & Dance", "easy",
    "The 'Natya Shastra', a foundational ancient Indian treatise on dramaturgy, dance and music, is attributed to which sage?",
    ["Valmiki", "Bharata Muni", "Patanjali", "Panini"], 1,
    "The Natya Shastra is attributed to the sage Bharata Muni and is considered the foundational text of Indian dramaturgy, dance and music, laying out theories of rasa (aesthetic emotion) still referenced today. Valmiki is associated with the Ramayana, Patanjali with the Yoga Sutras (and a Sanskrit grammar commentary), and Panini with the Sanskrit grammar text Ashtadhyayi -- none of whom authored the Natya Shastra.",
    "art-culture-natya-shastra-bharata-muni",
    "NCERT Fine Arts textbook -- chapter on the origins of Indian performing arts."
))

rows.append(stmt_row(
    "History", "Music & Dance", "medium",
    "Consider the following statements regarding classical dance forms of India and their states of origin:",
    [
        "Bharatanatyam originated in Tamil Nadu, traditionally associated with temple dance traditions.",
        "Kathakali and Mohiniyattam both originated in Kerala.",
        "Kathak, one of the eight classical dance forms, originated in and is associated with Karnataka.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Bharatanatyam is rooted in Tamil Nadu's temple traditions, and both Kathakali and Mohiniyattam originated in Kerala. Statement 3 is incorrect: Kathak is associated with North India, particularly the region of Uttar Pradesh, and its temple/storytelling and later Mughal-court traditions -- not Karnataka, whose associated classical form is Yakshagana (a dance-drama, distinct from the eight recognised classical dance forms).",
    "art-culture-classical-dance-forms-states",
    "NCERT Fine Arts textbook -- chapter on the classical dance forms of India."
))

rows.append(mcq_row(
    "History", "Music & Dance", "medium",
    "Tansen, counted among Emperor Akbar's 'Navaratnas', is most closely associated with which genre of Hindustani classical music?",
    ["Khayal", "Dhrupad", "Thumri", "Qawwali"], 1,
    "Tansen is most closely associated with Dhrupad, a serious, austere genre of Hindustani classical vocal music, and is credited in tradition with composing several ragas, including Miyan ki Malhar and Miyan ki Todi. Khayal developed later as a distinct genre; Thumri is a lighter, semi-classical form; and Qawwali is a Sufi devotional musical tradition, distinct from Tansen's Dhrupad association.",
    "art-culture-tansen-dhrupad",
    "NCERT Fine Arts textbook -- chapter on Hindustani classical music and the Mughal court."
))

# ---- PAINTING (2) ----

rows.append(mcq_row(
    "History", "Painting", "medium",
    "The murals at the Ajanta Caves predominantly depict scenes from which of the following?",
    ["Ramayana and Mahabharata episodes", "Jataka tales and the life of the Buddha", "Mughal court life and hunting scenes", "Puranic legends of Shiva and Vishnu"], 1,
    "The Ajanta cave murals are predominantly Buddhist in theme, depicting Jataka tales (stories of the Buddha's previous births) and episodes from the Buddha's life. Depictions of the Ramayana/Mahabharata, Mughal court scenes, and Puranic Shiva/Vishnu legends belong to entirely different artistic and religious traditions, unrelated to Ajanta's Buddhist iconographic programme.",
    "art-culture-ajanta-murals-jataka",
    "NCERT Fine Arts textbook -- chapter on Ajanta cave paintings."
))

rows.append(stmt_row(
    "History", "Painting", "easy",
    "Consider the following statements regarding Mughal miniature painting:",
    [
        "Mughal painting developed significant Persian influence, partly through artists such as Mir Sayyid Ali and Abd as-Samad, who were associated with the Mughal court under Humayun and Akbar.",
        "Akbar is credited with establishing a large royal painting workshop (Tasvir Khana) that employed numerous artists.",
        "Mughal painting remained entirely uninfluenced by indigenous Indian artistic traditions, drawing exclusively from Persian models throughout its development.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Persian artists such as Mir Sayyid Ali and Abd as-Samad shaped early Mughal painting, and Akbar established a large royal painting workshop. Statement 3 is incorrect: Mughal painting is well recognised for blending Persian technique with indigenous Indian artistic elements, evolving its own distinct synthesis rather than remaining a purely Persian import.",
    "art-culture-mughal-miniature-painting",
    "NCERT Fine Arts textbook -- chapter on Mughal painting."
))

# ---- ICONOGRAPHY (2) ----

rows.append(mcq_row(
    "History", "Iconography", "hard",
    "The 'Bhumisparsha Mudra' in Buddhist iconography, in which the Buddha's right hand touches the earth, is most closely associated with which event of his life?",
    ["His birth at Lumbini", "His attainment of enlightenment at Bodh Gaya, calling the earth to witness", "His first sermon at Sarnath", "His mahaparinirvana at Kushinagar"], 1,
    "The Bhumisparsha Mudra ('earth-touching gesture') depicts the moment the Buddha called the earth to witness his enlightenment at Bodh Gaya, resisting the temptations of Mara. It is distinct from the Dharmachakra Mudra (associated with his first sermon at Sarnath) and from separate iconographic conventions used for scenes of his birth and mahaparinirvana.",
    "art-culture-bhumisparsha-mudra",
    "NCERT Fine Arts textbook -- chapter on Buddhist iconography and mudras."
))

rows.append(mcq_row(
    "History", "Iconography", "medium",
    "The iconic bronze 'Nataraja' image, depicting Shiva as the cosmic dancer, is most closely associated with the patronage of which dynasty?",
    ["Pallavas", "Cholas", "Chalukyas of Badami", "Rashtrakutas"], 1,
    "The classical Nataraja bronze, depicting Shiva performing the cosmic Tandava dance within a ring of fire, is most closely associated with Chola-era bronze casting, particularly flourishing under Chola patronage in Tamil Nadu. The Pallavas, Chalukyas of Badami and Rashtrakutas are all significant South/Deccan Indian dynasties known for their own distinct architectural and sculptural contributions, but the Nataraja bronze tradition is specifically identified with the Cholas.",
    "art-culture-nataraja-chola-bronze",
    "NCERT Fine Arts textbook -- chapter on Chola bronze sculpture."
))

# ---- ARCHITECTURE (3) ----

rows.append(mcq_row(
    "History", "Architecture", "easy",
    "In Buddhist stupa architecture, the square railing enclosing the relic chamber at the top of the dome is known as the:",
    ["Anda", "Harmika", "Chatra", "Vedika"], 1,
    "The 'Harmika' is the square railing atop the stupa's dome, enclosing the relic chamber and supporting the chatra (umbrella) above it. The 'Anda' is the hemispherical dome itself; the 'Chatra' is the umbrella-shaped finial crowning the structure; and the 'Vedika' is the railing surrounding the base of the stupa -- each a distinct structural element.",
    "art-culture-stupa-harmika",
    "NCERT Fine Arts textbook -- chapter on stupa architecture."
))

rows.append(stmt_row(
    "History", "Architecture", "hard",
    "Consider the following statements regarding Indo-Islamic architecture:",
    [
        "Indo-Islamic architecture represents a synthesis of the indigenous trabeate (post-and-lintel) tradition with the arcuate (true arch-and-dome) tradition introduced by the Turks.",
        "The Alai Darwaza, built under Alauddin Khalji, is considered among the earliest structures in Delhi Sultanate architecture to employ a scientifically constructed true arch and dome.",
        "Early Delhi Sultanate structures, such as parts of the Qutub complex, initially relied on corbelling techniques rather than the true arch, reflecting continued reliance on indigenous building methods even after the arrival of Turkish rule.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. Indo-Islamic architecture blended the indigenous trabeate tradition with the arcuate tradition brought by the Turks; the Alai Darwaza is widely credited as an early example of a true, scientifically built arch and dome in Delhi Sultanate architecture; and earlier structures in the Qutub complex show continued use of corbelling, reflecting a gradual, syncretic transition rather than an abrupt architectural break.",
    "art-culture-indo-islamic-architecture-synthesis",
    "NCERT Fine Arts textbook / Themes in Indian History-II -- chapter on Indo-Islamic architecture."
))

rows.append(mcq_row(
    "History", "Architecture", "medium",
    "The 'Indo-Saracenic' architectural style, seen in colonial-era buildings such as the Victoria Memorial (Kolkata) and the Gateway of India (Mumbai), is best described as a blend of which architectural traditions?",
    ["Dravidian and Nagara temple styles", "Indian (Mughal/Rajput) and European (Gothic/neoclassical) elements", "Buddhist stupa architecture and Persian mosque design", "Indus Valley urban planning and Roman architecture"], 1,
    "Indo-Saracenic architecture, developed under British colonial patronage, deliberately blended Indian architectural elements (such as Mughal domes and Rajput chhatris) with European Gothic Revival and neoclassical features, seen in landmark buildings like the Victoria Memorial and Gateway of India. It is unrelated to a Dravidian-Nagara temple blend, a Buddhist-Persian mosque blend, or Indus Valley/Roman architecture, which belong to entirely different periods and traditions.",
    "art-culture-indo-saracenic-architecture",
    "NCERT Fine Arts textbook -- chapter on colonial-era architecture in India."
))

# ---- CULTURE-OTHER (1) ----

rows.append(stmt_row(
    "History", "Culture-Other", "medium",
    "Consider the following statements regarding the 'Classical Language' status conferred by the Government of India:",
    [
        "Tamil was the first Indian language to be granted 'Classical Language' status, in 2004.",
        "Sanskrit was granted classical language status in 2005, the year after Tamil.",
        "The criteria for classical language status include high antiquity of early texts and a body of ancient literature considered a valuable heritage.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. Tamil became the first language to receive classical status in 2004, Sanskrit followed in 2005, and the criteria for classical status centre on high antiquity of texts and a valuable, independent body of ancient literature.",
    "art-culture-classical-language-status",
    "Ministry of Culture, Government of India -- criteria and history of Classical Language status; NCERT Fine Arts textbook."
))

statements_sql = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements_sql + "\n"
    "returning id, subject, topic, type, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch9_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
