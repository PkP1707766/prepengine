# -*- coding: utf-8 -*-
"""Batch 4: easy/statement_based/Modern (6) + easy/statement_based/Ancient (6) = 12 questions."""
import json, os

def sql_str(s):
    return "'" + s.replace("'", "''") + "'"

OPTION_BODIES = ["Only one", "Only two", "All three", "None"]

def options_json(correct_idx):
    arr = []
    for i, b in enumerate(OPTION_BODIES):
        arr.append({"id": ["a", "b", "c", "d"][i], "body": b, "isCorrect": (i == correct_idx)})
    return json.dumps(arr)

def q_row(subject, topic, difficulty, body, statements, closing, correct_idx, explanation, concept_group_id, source_citation):
    qdata = json.dumps({"statements": statements, "closing": closing})
    return (
        "('upsc'," + sql_str(subject) + "," + sql_str(topic) + ",'statement_based'," + sql_str(difficulty) + ","
        + sql_str(body) + "," + sql_str(qdata) + "::jsonb," + sql_str(options_json(correct_idx)) + "::jsonb,"
        + "2,0.66," + sql_str(explanation) + "," + sql_str(concept_group_id) + ",'original_pattern_matched',"
        + sql_str(source_citation) + ",'draft')"
    )

rows = []

# ---- MODERN EASY (6) ----

rows.append(q_row(
    "History", "Modern", "easy",
    "Consider the following statements regarding the founding of the Indian National Congress (1885):",
    [
        "The Indian National Congress was founded in 1885 by Allan Octavian Hume, a retired British civil servant.",
        "The first session of the Congress was held in Bombay, with Womesh Chandra Bonnerjee as its first president.",
        "The Indian National Congress was originally conceived only as a platform for revolutionary armed struggle against British rule.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the Congress was founded in 1885 by A. O. Hume, and its first session was held in Bombay under the presidency of W. C. Bonnerjee. Statement 3 is incorrect: the early Congress under Moderate leadership pursued constitutional methods -- petitions, resolutions and dialogue with the colonial government -- not revolutionary armed struggle.",
    "modern-inc-founding-1885",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the founding of the Indian National Congress."
))

rows.append(q_row(
    "History", "Modern", "easy",
    "Consider the following statements regarding the Jallianwala Bagh massacre (1919):",
    [
        "The Jallianwala Bagh massacre took place on 13 April 1919 in Amritsar, Punjab.",
        "It was ordered by General Reginald Dyer, who directed troops to fire on an unarmed crowd gathered at Jallianwala Bagh.",
        "The gathering at Jallianwala Bagh took place on the occasion of Baisakhi.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. The massacre occurred on 13 April 1919 at Amritsar, on the day of the Baisakhi festival, when General Reginald Dyer ordered troops to open fire on the unarmed crowd gathered at Jallianwala Bagh, killing hundreds.",
    "modern-jallianwala-bagh-1919",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Rowlatt Act and Jallianwala Bagh."
))

rows.append(q_row(
    "History", "Modern", "easy",
    "Consider the following statements regarding the Doctrine of Lapse:",
    [
        "The Doctrine of Lapse was a policy adopted by Lord Dalhousie, under which a princely state without a natural male heir would be annexed by the British.",
        "Satara, Jhansi and Nagpur were among the states annexed under this doctrine.",
        "The Doctrine of Lapse was welcomed by most princely rulers, as it strengthened their succession rights.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Dalhousie's Doctrine of Lapse allowed annexation of states lacking a natural male heir, and Satara, Jhansi and Nagpur were among those annexed. Statement 3 is incorrect: the doctrine was deeply resented by princely rulers, since it denied their traditional right to adopt an heir, and is counted among the grievances behind the Revolt of 1857.",
    "modern-doctrine-of-lapse",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the policy of annexation under Dalhousie."
))

rows.append(q_row(
    "History", "Modern", "easy",
    "Consider the following statements regarding the Revolt of 1857:",
    [
        "The Revolt of 1857 began at Meerut in May 1857.",
        "Mangal Pandey, a sepoy, is often cited as one of the early figures associated with the uprising.",
        "Bahadur Shah Zafar, the Mughal emperor, was proclaimed the nominal leader of the revolt by the rebels in Delhi.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. The revolt broke out at Meerut in May 1857, Mangal Pandey's earlier act of defiance at Barrackpore is widely cited as a precursor, and the rebels proclaimed the aged Mughal emperor Bahadur Shah Zafar as their nominal leader after taking Delhi.",
    "modern-revolt-of-1857",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Revolt of 1857."
))

rows.append(q_row(
    "History", "Modern", "easy",
    "Consider the following statements regarding the Brahmo Samaj:",
    [
        "The Brahmo Samaj was founded by Raja Ram Mohan Roy in Calcutta in 1828.",
        "It opposed idol worship and advocated monotheism, drawing on Upanishadic philosophy.",
        "Raja Ram Mohan Roy played a key role in the abolition of Sati, enacted through the Bengal Sati Regulation of 1829 under Governor-General Lord William Bentinck.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. Ram Mohan Roy founded the Brahmo Samaj in Calcutta in 1828, built on monotheistic, Upanishad-based ideas opposing idol worship, and was instrumental in the campaign that led Bentinck to abolish Sati through the 1829 regulation.",
    "modern-brahmo-samaj-1828",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on socio-religious reform movements."
))

rows.append(q_row(
    "History", "Modern", "easy",
    "Consider the following statements regarding the Arya Samaj:",
    [
        "The Arya Samaj was founded by Swami Dayanand Saraswati in 1875.",
        "Its motto was 'Back to the Vedas', emphasising the authority of Vedic scriptures.",
        "The Arya Samaj supported idol worship as a central part of Hindu religious life.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the Arya Samaj was founded in 1875 by Swami Dayanand Saraswati under the motto 'Back to the Vedas'. Statement 3 is incorrect: the Arya Samaj strongly opposed idol worship, along with caste rigidities and polytheistic ritual, advocating a return to what it held to be pure Vedic monotheism.",
    "modern-arya-samaj-1875",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on socio-religious reform movements."
))

# ---- ANCIENT EASY (6) ----

rows.append(q_row(
    "History", "Ancient", "easy",
    "Consider the following statements regarding the Kalinga War:",
    [
        "The Kalinga War was fought in 261 BCE between the Mauryan emperor Ashoka and the state of Kalinga (present-day Odisha).",
        "The immense bloodshed of the war led Ashoka to embrace Buddhism and adopt a policy of Dhamma.",
        "Kalinga was annexed without significant resistance or loss of life.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Ashoka fought and annexed Kalinga in 261 BCE, and the war's devastation is recorded (in his own Rock Edict XIII) as the turning point that led him toward Buddhism and Dhamma. Statement 3 is incorrect: the war involved massive casualties and fierce resistance, which is precisely what is said to have caused Ashoka's remorse.",
    "ancient-kalinga-war-261bce",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on Ashoka and the Kalinga War."
))

rows.append(q_row(
    "History", "Ancient", "easy",
    "Consider the following statements regarding the Indus Valley Civilization:",
    [
        "Steatite seals engraved with animal motifs, such as the humped bull and unicorn, have been found at Indus Valley sites.",
        "The so-called 'Pashupati seal', found at Mohenjodaro, depicts a seated figure surrounded by animals.",
        "The script found on Indus Valley seals has been definitively deciphered by historians.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Indus sites have yielded steatite seals with animal motifs, including the well-known Pashupati seal from Mohenjodaro. Statement 3 is incorrect: despite many attempts, the Indus script remains undeciphered to date.",
    "ancient-indus-seals-script",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Indus Valley Civilisation."
))

rows.append(q_row(
    "History", "Ancient", "easy",
    "Consider the following statements regarding Chandragupta Maurya:",
    [
        "Chandragupta Maurya, founder of the Mauryan Empire, overthrew the Nanda dynasty with the help of his mentor Chanakya (Kautilya).",
        "Chandragupta Maurya, according to Jain tradition, later became a Jain monk and spent his last days at Shravanabelagola.",
        "Chandragupta Maurya was the grandfather of Ashoka.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. Chandragupta Maurya, guided by Chanakya, overthrew the Nanda dynasty to found the Mauryan Empire; Jain tradition holds that he later renounced the throne, became a Jain monk under Bhadrabahu, and died at Shravanabelagola; and he was indeed Ashoka's grandfather, succeeded by his son Bindusara and then Ashoka.",
    "ancient-chandragupta-maurya-chanakya",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the rise of the Mauryan Empire."
))

rows.append(q_row(
    "History", "Ancient", "easy",
    "Consider the following statements regarding the Chinese pilgrim Fa-Hien:",
    [
        "Fa-Hien, a Chinese Buddhist pilgrim, visited India during the reign of Chandragupta II.",
        "Fa-Hien's account describes the general prosperity and good administration of the Gupta Empire.",
        "Fa-Hien visited India during the reign of Harshavardhana, nearly two centuries after the Guptas.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Fa-Hien visited Gupta India during Chandragupta II's reign and recorded its general prosperity and administration favourably. Statement 3 is incorrect and confuses Fa-Hien with a later Chinese pilgrim, Xuanzang (Hiuen Tsang), who visited India under Harshavardhana roughly two centuries afterward.",
    "ancient-fa-hien-gupta-visit",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Gupta Empire and foreign accounts."
))

rows.append(q_row(
    "History", "Ancient", "easy",
    "Consider the following statements regarding the Rig Veda:",
    [
        "The Rig Veda is the oldest of the four Vedas.",
        "It is a collection of hymns (suktas) organised into ten books called Mandalas.",
        "The Rig Veda was composed after the decline of the Indus Valley Civilization and primarily describes an urban, mercantile society.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the Rig Veda is the oldest of the four Vedas and is organised into ten Mandalas of hymns. Statement 3 is incorrect: the society reflected in the Rig Veda was predominantly pastoral and rural, centred on cattle-rearing and tribal chieftaincy, in contrast to the urban, mercantile character of the earlier Indus Valley Civilization.",
    "ancient-rig-veda-society",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Rig Vedic Period."
))

rows.append(q_row(
    "History", "Ancient", "easy",
    "Consider the following statements regarding the Sarnath Lion Capital:",
    [
        "The Lion Capital of Ashoka, originally erected at Sarnath, was adopted as the National Emblem of India.",
        "The national motto inscribed below the emblem, 'Satyameva Jayate', is taken from the Mundaka Upanishad.",
        "The Sarnath pillar commemorates the spot where Ashoka is said to have attained enlightenment.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the Sarnath Lion Capital was adopted as India's National Emblem, and its motto 'Satyameva Jayate' is drawn from the Mundaka Upanishad. Statement 3 is incorrect on two counts: it was the Buddha, not Ashoka, who is associated with enlightenment (at Bodh Gaya), and the Sarnath pillar instead commemorates the Buddha's first sermon (Dharmachakra Pravartana) delivered at Sarnath.",
    "ancient-sarnath-lion-capital",
    "Old NCERT, Ancient India (R. S. Sharma); NCERT Fine Arts -- chapter on Mauryan art and the Ashokan pillars."
))

statements_sql = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements_sql + "\n"
    "returning id, subject, topic, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch4_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
