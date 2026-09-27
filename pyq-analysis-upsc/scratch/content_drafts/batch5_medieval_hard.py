# -*- coding: utf-8 -*-
"""Batch 5: medium/statement_based/Medieval (6) + hard/statement_based/Modern (6) = 12 questions."""
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

# ---- MEDIEVAL MEDIUM (6) ----

rows.append(q_row(
    "History", "Medieval", "medium",
    "Consider the following statements regarding Qutb-ud-din Aibak and the founding of the Delhi Sultanate:",
    [
        "Qutb-ud-din Aibak, a former slave (Mamluk) of Muhammad Ghori, founded the Slave (Mamluk) Dynasty and is regarded as the first Sultan of Delhi.",
        "Aibak began construction of the Qutub Minar, which was completed in its entirety during his own reign.",
        "Iltutmish, Aibak's successor, is credited with consolidating the Delhi Sultanate and organising the administrative system of Iqtas.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: Aibak, a former Mamluk of Muhammad Ghori, founded the Slave Dynasty, and Iltutmish later consolidated the Sultanate and organised the Iqta system of administration. Statement 2 is incorrect: Aibak only began construction of the Qutub Minar -- it was completed by Iltutmish, not within Aibak's own short reign.",
    "medieval-qutb-ud-din-aibak-delhi-sultanate",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the Delhi Sultanate."
))

rows.append(q_row(
    "History", "Medieval", "medium",
    "Consider the following statements regarding Alauddin Khalji's market reforms:",
    [
        "Alauddin Khalji introduced market control regulations to fix the prices of essential commodities, partly to sustain a large standing army at low cost.",
        "He established a dedicated department, the Diwan-i-Riyasat, to oversee market regulation and enforcement.",
        "Alauddin Khalji's strict market reforms were continued successfully by all his successors without modification.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Alauddin Khalji's market controls were designed to keep prices low and stable, chiefly to support his large army, and were administered through the Diwan-i-Riyasat. Statement 3 is incorrect: the strict controls were specific to his reign and largely lapsed after his death, rather than being continued unchanged by his successors.",
    "medieval-alauddin-khalji-market-reforms",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the Khalji dynasty."
))

rows.append(q_row(
    "History", "Medieval", "medium",
    "Consider the following statements regarding Muhammad bin Tughlaq's administrative experiments:",
    [
        "Muhammad bin Tughlaq shifted his capital from Delhi to Daulatabad in the Deccan.",
        "He introduced a token currency, issuing copper/bronze coins intended to circulate at par with silver coins.",
        "Both the transfer of the capital and the token currency experiment are generally regarded by historians as unqualified administrative successes.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Muhammad bin Tughlaq shifted the capital to Daulatabad and introduced token currency. Statement 3 is incorrect: both measures are generally regarded as poorly implemented and ultimately failed experiments, contributing to administrative and economic strain, not as successes.",
    "medieval-muhammad-bin-tughlaq-experiments",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the Tughlaq dynasty."
))

rows.append(q_row(
    "History", "Medieval", "medium",
    "Consider the following statements regarding the Vijayanagara Empire:",
    [
        "The Vijayanagara Empire was founded in 1336 by Harihara and Bukka, traditionally said to have been guided by the sage Vidyaranya.",
        "The Vijayanagara Empire reached its zenith under Krishnadevaraya of the Tuluva dynasty.",
        "The Vijayanagara Empire suffered a decisive defeat at the Battle of Talikota (1565) at the hands of a confederacy of Deccan Sultanates.",
    ],
    "How many of the above statements are correct?", 2,
    "All three statements are correct. Harihara and Bukka founded the Vijayanagara Empire in 1336, traditionally with the guidance of Vidyaranya; it reached its peak under Krishnadevaraya of the Tuluva dynasty; and it suffered a decisive defeat at Talikota in 1565 against the combined Deccan Sultanates.",
    "medieval-vijayanagara-empire",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on the Vijayanagara Empire."
))

rows.append(q_row(
    "History", "Medieval", "medium",
    "Consider the following statements regarding the Bhakti Movement:",
    [
        "Kabir, a prominent Bhakti saint, emphasised formless (Nirguna) devotion and criticised ritualism in both Hinduism and Islam.",
        "Guru Nanak, founder of Sikhism, also preached the oneness of God and rejected caste distinctions.",
        "The Bhakti Movement was confined exclusively to North India and had no earlier parallel devotional tradition in South India.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: Kabir preached Nirguna devotion critical of ritualism, and Guru Nanak taught the oneness of God while rejecting caste. Statement 3 is incorrect: the Bhakti tradition has deep South Indian roots, with the Alvars and Nayanars composing devotional poetry centuries before the North Indian Bhakti saints.",
    "medieval-bhakti-movement",
    "NCERT, Themes in Indian History-II -- chapter on the Bhakti and Sufi movements."
))

rows.append(q_row(
    "History", "Medieval", "medium",
    "Consider the following statements regarding Akbar's administration:",
    [
        "Akbar introduced the Mansabdari system to organise military and civil administration through a unified rank hierarchy of zat and sawar.",
        "Akbar founded Din-i-Ilahi, a syncretic faith combining elements of various religions, which most historians agree became a mass religion followed by a significant section of the population.",
        "Akbar abolished the pilgrimage tax and the jizya (a tax on non-Muslims) during his reign.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: Akbar introduced the Mansabdari system of zat and sawar ranks, and abolished both the pilgrimage tax and the jizya. Statement 2 is incorrect: while Akbar did found Din-i-Ilahi, it attracted only a small number of court nobles and never became a mass religion.",
    "medieval-akbar-administration",
    "NCERT, Themes in Indian History-II / Old NCERT Medieval India (Satish Chandra) -- chapter on Akbar's administration and religious policy."
))

# ---- MODERN HARD (6) ----

rows.append(q_row(
    "History", "Modern", "hard",
    "Consider the following statements regarding revolutionary movements in the freedom struggle:",
    [
        "The Anushilan Samiti had its origins in Bengal and later effectively split into two factions -- one based in Calcutta and another, the Jugantar group, also rooted in Bengal.",
        "The Chittagong Armoury Raid (1930), led by Surya Sen, aimed to seize government armouries and disrupt telegraph and rail communications in the region.",
        "The Hindustan Socialist Republican Association (HSRA) was the original name under which the organisation was founded in 1924, and it was only later renamed the Hindustan Republican Association (HRA) after Bhagat Singh joined in 1928.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 2 are correct: the Anushilan Samiti split into Calcutta and Jugantar factions, and Surya Sen's Chittagong Armoury Raid targeted armouries and communication lines. Statement 3 reverses the actual sequence: the organisation was founded in 1924 as the Hindustan Republican Association (HRA) by Ram Prasad Bismil and others, and was reorganised and renamed the Hindustan Socialist Republican Association (HSRA) only in 1928, after Bhagat Singh, Chandrashekhar Azad and others joined.",
    "modern-revolutionary-movements-hsra",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on revolutionary movements."
))

rows.append(q_row(
    "History", "Modern", "hard",
    "Consider the following statements regarding the Gandhi-Irwin Pact (1931):",
    [
        "Under the Pact, the Congress agreed to suspend the Civil Disobedience Movement and participate in the Second Round Table Conference.",
        "The government agreed to release all political prisoners without exception, including those convicted of involvement in violent revolutionary activities, such as Bhagat Singh.",
        "The Pact permitted people living near the coast to manufacture salt for personal consumption without payment of duty, as a limited concession.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: the Congress agreed to suspend Civil Disobedience and attend the Second Round Table Conference, and a limited concession allowed duty-free salt manufacture for personal use near the coast. Statement 2 is incorrect: the release of prisoners under the Pact did not extend to those convicted of violent revolutionary acts -- Bhagat Singh, Sukhdev and Rajguru were executed in March 1931 despite appeals for clemency, a major point of controversy around the Pact.",
    "modern-gandhi-irwin-pact-1931",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Civil Disobedience Movement and the Gandhi-Irwin Pact."
))

rows.append(q_row(
    "History", "Modern", "hard",
    "Consider the following statements regarding the Second Round Table Conference (1931):",
    [
        "Mahatma Gandhi attended the Second Round Table Conference in London as the sole representative of the Indian National Congress.",
        "The Conference made significant progress on the question of minority representation and communal electorates, resolving most outstanding disputes.",
        "The Conference ultimately failed largely due to disagreements over the communal question, particularly between the Congress and groups such as the Muslim League and representatives of the depressed classes.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: Gandhi attended as the Congress's sole representative, and the Conference broke down chiefly over the unresolved communal question. Statement 2 is incorrect: far from making significant progress, the Conference failed precisely because it could not resolve the competing claims over minority and communal representation -- an impasse that led the British government to announce the Communal Award the following year.",
    "modern-second-round-table-conference-1931",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Round Table Conferences."
))

rows.append(q_row(
    "History", "Modern", "hard",
    "Consider the following statements regarding the Interim Government (1946):",
    [
        "The Interim Government was formed in September 1946, with Jawaharlal Nehru as Vice-President of the Executive Council.",
        "The Muslim League joined the Interim Government from its formation in September 1946, cooperating fully with the Congress-led administration from the outset.",
        "Liaquat Ali Khan, of the Muslim League, held the finance portfolio in the Interim Government after the League joined it.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: the Interim Government was formed in September 1946 under Nehru, and Liaquat Ali Khan held the finance portfolio after the League joined. Statement 2 is incorrect: the Muslim League initially refused to join the Interim Government at its formation in September 1946, entering only in October 1946, and even then adopted an obstructionist rather than cooperative stance.",
    "modern-interim-government-1946",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the transfer of power."
))

rows.append(q_row(
    "History", "Modern", "hard",
    "Consider the following statements regarding the Shimla Conference (1945):",
    [
        "The Shimla Conference of 1945 was convened by Viceroy Lord Wavell to discuss a proposal for a new Executive Council with equal representation for Caste Hindus and Muslims.",
        "The Conference succeeded, resulting in an agreed composition for the new Executive Council.",
        "The Conference failed primarily over Jinnah's insistence that the Muslim League alone had the right to nominate all Muslim members to the Council.",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: Wavell convened the Conference to propose a reconstituted Executive Council with equal Caste Hindu and Muslim representation, and it collapsed largely because Jinnah insisted the League alone could nominate all Muslim members. Statement 2 is incorrect: the Conference failed to reach agreement and ended without a resolution, not with an agreed Council composition.",
    "modern-shimla-conference-1945",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Shimla Conference and the Wavell Plan."
))

rows.append(q_row(
    "History", "Modern", "hard",
    "Consider the following statements regarding the Cripps Mission (1942):",
    [
        "The Cripps Mission offered Dominion Status to India after the war, along with the right for any province to opt out of the proposed Indian Union.",
        "The Cripps proposals were accepted by the Indian National Congress, while being rejected only by the Muslim League.",
        "Mahatma Gandhi famously described the Cripps proposals as 'a post-dated cheque on a crashing bank.'",
    ],
    "How many of the above statements are correct?", 1,
    "Statements 1 and 3 are correct: the Mission offered post-war Dominion Status with a provincial opt-out clause, and Gandhi described the offer with his well-known 'post-dated cheque' remark. Statement 2 is incorrect: the Congress also rejected the Cripps proposals -- chiefly over the opt-out clause, seen as encouraging the country's Balkanisation, and over the refusal to transfer defence -- so both major parties rejected the Mission, not just the League.",
    "modern-cripps-mission-1942",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Cripps Mission."
))

statements_sql = ",\n".join(rows)
sql = (
    "insert into public.questions\n"
    "(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\n"
    "values\n" + statements_sql + "\n"
    "returning id, subject, topic, difficulty;\n"
)

out_path = os.path.join(os.path.dirname(__file__), "batch5_insert.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print("wrote", out_path, len(sql), "chars,", len(rows), "rows")
