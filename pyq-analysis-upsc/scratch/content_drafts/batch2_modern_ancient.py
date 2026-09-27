import json

def sql_str(s):
    """Escape a Python string for a SQL single-quoted literal."""
    return "'" + s.replace("'", "''") + "'"

def q_row(subject, topic, qtype, difficulty, body, statements, closing, options, marks_correct, marks_wrong, explanation, concept_group_id, source_citation):
    qdata = {}
    if statements:
        qdata = {"statements": statements, "closing": closing}
    opts = [{"id": chr(97+i), "body": o[0], "isCorrect": o[1]} for i, o in enumerate(options)]
    return (
        "('upsc'," + sql_str(subject) + "," + sql_str(topic) + "," + sql_str(qtype) + "," + sql_str(difficulty) + ","
        + sql_str(body) + "," + sql_str(json.dumps(qdata)) + "::jsonb," + sql_str(json.dumps(opts)) + "::jsonb,"
        + str(marks_correct) + "," + str(marks_wrong) + "," + sql_str(explanation) + ","
        + sql_str(concept_group_id) + ",'original_pattern_matched'," + sql_str(source_citation) + ",'draft')"
    )

rows = []

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Swadeshi Movement (1905):",
    [
        "It was launched as a direct reaction to the partition of Bengal announced in 1905.",
        "'Vande Mataram' was composed by Rabindranath Tagore as the movement's anthem.",
        "The National Council of Education was established during this movement to promote technical and scientific education outside government control.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Swadeshi Movement was launched in 1905 in direct reaction to Lord Curzon's partition of Bengal. Statement 2 is incorrect: 'Vande Mataram' was composed by Bankim Chandra Chatterjee in his 1882 novel Anandamath, not by Tagore -- Tagore set a portion of it to music and sang it at the 1896 Congress session, but did not compose it. Statement 3 is correct: the National Council of Education was set up in 1906 to promote technical and scientific education outside government-controlled institutions, part of the constructive Swadeshi programme.",
    "modern-swadeshi-movement-1905",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Partition of Bengal and the Swadeshi Movement.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Government of India Act, 1935:",
    [
        "It provided for the establishment of an All India Federation comprising British Indian provinces and Princely States.",
        "It introduced provincial autonomy, replacing the system of dyarchy in the provinces.",
        "The proposed All India Federation actually came into force in 1937 along with provincial autonomy.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Act proposed an All India Federation of British Indian provinces and willing Princely States. Statement 2 is correct: it ended dyarchy in the provinces (introducing it instead at the Centre) and gave provinces autonomy. Statement 3 is incorrect: the Federation never came into force because an insufficient number of Princely States acceded to it -- only the provincial autonomy part took effect, in 1937.",
    "modern-govt-of-india-act-1935",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on constitutional developments, 1935 Act.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Quit India Movement (1942):",
    [
        "It was launched following the rejection of the Cripps Mission proposals.",
        "Mahatma Gandhi gave the call 'Do or Die' at the Bombay session of the All India Congress Committee.",
        "The Quit India Resolution was passed by the Congress Working Committee at its Wardha session and was immediately implemented as a mass movement in the same month, July 1942.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Quit India followed the failure of the Cripps Mission (March-April 1942). Statement 2 is correct: Gandhi's 'Do or Die' call was given at the AICC session at Gowalia Tank Maidan, Bombay, on 8 August 1942. Statement 3 is incorrect: the Working Committee approved the Quit India Resolution at Wardha in July 1942, but the mass movement itself was launched the following month, in August 1942, at the Bombay AICC session -- the two events are a month apart, not the same month.",
    "modern-quit-india-1942",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Quit India Movement.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Ilbert Bill controversy (1883):",
    [
        "It sought to allow Indian judges to try British subjects in criminal cases in the provinces.",
        "It was withdrawn entirely, without any modification, due to strong opposition from the European community in India.",
        "The controversy around it is regarded as one of the factors that contributed to the formation of the Indian National Congress in 1885.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Ilbert Bill, introduced by C. P. Ilbert under Viceroy Ripon, sought to allow senior Indian judges to try European/British subjects. Statement 2 is incorrect: the Bill was not withdrawn -- it was passed in 1884 in a modified, compromise form (Europeans could demand a jury with at least half European members). Statement 3 is correct: the intensity of European opposition, and the demonstration of organised Indian political response it provoked, is cited as one of the contributing factors to the Congress's formation in 1885.",
    "modern-ilbert-bill-1883",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the origins of the Indian National Congress.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Rowlatt Act (1919):",
    [
        "It gave the government powers to imprison persons without trial for political offences.",
        "It was passed based on the recommendations of a committee headed by Sir Sidney Rowlatt.",
        "All elected Indian members of the Central/Imperial Legislative Council voted in favour of the Act.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Rowlatt Act allowed detention without trial for suspected political offenders. Statement 2 is correct: it followed the recommendations of the Rowlatt Committee, headed by Sir Sidney Rowlatt. Statement 3 is incorrect: in fact every single elected Indian member of the Imperial Legislative Council voted against the Bill -- it passed only because of the official (British) majority.",
    "modern-rowlatt-act-1919",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Rowlatt Act and Jallianwala Bagh.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Cabinet Mission Plan (1946):",
    [
        "It proposed a three-tier structure with a weak Union at the Centre and grouping of provinces into sections.",
        "It categorically rejected the demand for a separate, sovereign state of Pakistan.",
        "It was unanimously accepted by both the Indian National Congress and the Muslim League without any reservations.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Plan proposed a weak Union (handling only defence, foreign affairs and communications) with provinces grouped into three sections. Statement 2 is correct: it offered grouping and provincial autonomy as an alternative to outright partition, effectively rejecting a separate Pakistan. Statement 3 is incorrect: neither party accepted it without reservations -- the Muslim League initially accepted but later withdrew and called Direct Action Day, while Congress had its own objections to the compulsory grouping clauses.",
    "modern-cabinet-mission-1946",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Cabinet Mission and the road to Partition.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Age of Consent Act (1891):",
    [
        "It raised the age of consent for consummation of marriage for girls from 10 to 12 years.",
        "It was enacted in the aftermath of public outrage over the death of Phulmonee, a child bride.",
        "It faced opposition from sections of orthodox Hindu society, including Bal Gangadhar Tilak, who viewed it as interference in religious and social custom.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. The Act raised the age of consent from 10 to 12. It followed public outcry over the death of the child bride Phulmonee in 1890. It was opposed by sections of orthodox Hindu opinion, including Tilak, as unwarranted interference in social and religious custom -- a position that placed him at odds with reformist contemporaries on this specific issue.",
    "modern-age-of-consent-act-1891",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on social reform movements.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Vernacular Press Act (1878):",
    [
        "It was enacted during the viceroyalty of Lord Lytton.",
        "It empowered the government to confiscate the press and printing material of newspapers publishing seditious material, without right of appeal to a court of law.",
        "It was applicable equally to both vernacular-language and English-language newspapers.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Act was passed under Viceroy Lord Lytton. Statement 2 is correct: it allowed confiscation of press material with no right of appeal. Statement 3 is incorrect: the Act applied only to vernacular-language newspapers, explicitly exempting English-language papers -- the discriminatory scope that earned it the nickname the 'Gagging Act'.",
    "modern-vernacular-press-act-1878",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on press legislation under colonial rule.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Lucknow Pact (1916):",
    [
        "It was an agreement between the Indian National Congress and the All India Muslim League.",
        "Under the Pact, the Congress accepted the principle of separate electorates for Muslims.",
        "The Pact was signed at joint sessions of both parties held at Lucknow, marking a rare period of Hindu-Muslim political unity before independence.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. The Lucknow Pact (1916) was an agreement between the Congress and the Muslim League. The Congress accepted separate electorates for Muslims as part of the compromise. It was signed at the joint Lucknow sessions of both parties in December 1916, widely regarded as the high point of Hindu-Muslim unity in the national movement.",
    "modern-lucknow-pact-1916",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Lucknow Pact.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding Direct Action Day (16 August 1946):",
    [
        "It was called by the Muslim League to press its demand for a separate state of Pakistan.",
        "It led to widespread communal violence, most severely in Calcutta, an event remembered as 'The Great Calcutta Killings'.",
        "It was called by the Muslim League in response to the Congress's rejection of the Cabinet Mission Plan.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Direct Action Day was called by the Muslim League to press its Pakistan demand. Statement 2 is correct: it triggered severe communal violence, worst in Calcutta. Statement 3 is incorrect and reverses the actual sequence: it was the Muslim League itself that withdrew its earlier acceptance of the Cabinet Mission Plan and felt sidelined by the Congress-led interim government, not a case of Congress rejecting the Plan.",
    "modern-direct-action-day-1946",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the road to Partition.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Civil Disobedience Movement and the Dandi March (1930):",
    [
        "Mahatma Gandhi began the Dandi March from Sabarmati Ashram.",
        "The march covered a distance of approximately 240 miles over 24 days.",
        "The movement was formally suspended after the Gandhi-Irwin Pact of 1931, following which the Congress participated in the Second Round Table Conference.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. Gandhi began the march from Sabarmati Ashram on 12 March 1930, covering roughly 240 miles over 24 days to reach Dandi on 6 April. The movement was suspended after the Gandhi-Irwin Pact (March 1931), and Gandhi then represented the Congress at the Second Round Table Conference later that year.",
    "modern-dandi-march-1930",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Civil Disobedience Movement.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the August Offer (1940):",
    [
        "It was made by Viceroy Lord Linlithgow.",
        "It offered Dominion Status as the ultimate political goal after the war, along with an expansion of the Viceroy's Executive Council to include more Indians.",
        "It was fully accepted by both the Indian National Congress and the Muslim League.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the August Offer was made by Viceroy Lord Linlithgow. Statement 2 is correct: it promised eventual Dominion Status and an expanded, more representative Executive Council. Statement 3 is incorrect: the Congress rejected the Offer as inadequate, since it did not promise immediate self-government; the Muslim League found it somewhat more favourable (it assured no future constitution would be adopted without League consent) but this was not a case of full, unqualified acceptance by both parties.",
    "modern-august-offer-1940",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on wartime constitutional proposals.",
))

rows.append(q_row(
    "History", "Modern", "statement_based", "medium",
    "Consider the following statements regarding the Communal Award (1932):",
    [
        "It was announced by British Prime Minister Ramsay MacDonald.",
        "It extended the principle of separate electorates to the Depressed Classes, in addition to Muslims, Sikhs and other communities that already had them.",
        "It was welcomed unconditionally by Mahatma Gandhi as a positive step for the Depressed Classes.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Communal Award was announced by Ramsay MacDonald in August 1932. Statement 2 is correct: it extended separate electorates to the Depressed Classes for the first time, alongside existing separate electorates for Muslims, Sikhs and other minorities. Statement 3 is incorrect: Gandhi strongly opposed separate electorates for the Depressed Classes specifically, fearing it would permanently divide Hindu society, and went on a fast against this provision -- leading directly to the Poona Pact.",
    "modern-communal-award-1932",
    "NCERT/Bipan Chandra, India's Struggle for Independence -- chapter on the Communal Award and the Poona Pact.",
))

# ---- Ancient (12) ----

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding trade in the Indus Valley Civilization:",
    [
        "Lothal, in present-day Gujarat, had a dockyard indicating maritime trade.",
        "The Harappans had trade contacts with Mesopotamia, which Mesopotamian texts refer to as 'Meluhha'.",
        "The Harappans used a standardised system of weights, following roughly a binary progression for the lower denominations.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. Lothal had a dockyard evidencing maritime trade. Mesopotamian texts refer to a trading region called 'Meluhha', widely identified with the Indus region. Harappan weights followed a broadly standardised, roughly binary system (1, 2, 4, 8, 16...) for smaller denominations.",
    "ancient-indus-trade",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Indus Valley/Harappan Civilisation.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding the Later Vedic period:",
    [
        "Iron came into use during this period, referred to in texts as 'shyama ayas' or 'krishna ayas'.",
        "This period saw the 'varna' system become more rigid, with the emergence of untouchability.",
        "Agriculture became the predominant economic activity during this period, replacing the more pastoral economy of the Early Vedic period.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. Iron, distinguished from copper ('lohit ayas'), appears in Later Vedic texts as 'shyama/krishna ayas' (dark metal). The varna system hardened during this period, with untouchability emerging. The economy shifted from the more pastoral, cattle-centred Early Vedic pattern to a predominantly agrarian one.",
    "ancient-later-vedic-economy-society",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Later Vedic Period.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding the Buddhist Councils:",
    [
        "The First Buddhist Council was held at Rajagriha shortly after the death of the Buddha.",
        "The Second Buddhist Council, held at Vaishali, led to a split between the Sthaviravadins and the Mahasanghikas.",
        "The Fourth Buddhist Council, held under the patronage of Kanishka, was held at Pataliputra.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the First Council was held at Rajagriha soon after the Buddha's parinirvana. Statement 2 is correct: the Second Council at Vaishali led to the Sthaviravadin-Mahasanghika split over questions of monastic discipline. Statement 3 is incorrect: the Fourth Council under Kanishka is traditionally held to have been convened at Kundalavana in Kashmir, not Pataliputra -- Pataliputra was the site of the THIRD Council, held under Ashoka.",
    "ancient-buddhist-councils",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the spread and councils of Buddhism.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding Gupta administration:",
    [
        "The Gupta rulers used titles like 'Maharajadhiraja' and 'Parama Bhattaraka' to indicate paramount sovereign status.",
        "Land grants to Brahmanas and religious institutions, often tax-free, became a common practice during the Gupta period, evidenced by copper-plate inscriptions.",
        "The Gupta administration was more centralised than the Mauryan administration, with provincial and local governors having less autonomy.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Gupta rulers used titles such as Maharajadhiraja and Parama Bhattaraka. Statement 2 is correct: land grants (agraharas) to Brahmanas, often tax-free, are well attested in Gupta-era copper-plate inscriptions. Statement 3 is incorrect and reverses the actual comparison: Gupta administration is generally understood to have been LESS centralised than the Mauryan, with provincial and local functionaries enjoying greater autonomy -- an early marker of what some historians describe as the beginnings of Indian feudalism.",
    "ancient-gupta-administration",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Gupta Empire.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding the Sangam Age:",
    [
        "Sangam literature primarily describes the social, economic and political life of the Tamil region in the early centuries of the Common Era.",
        "The 'Tolkappiyam', a work on Tamil grammar and poetics, is considered one of the earliest Sangam texts.",
        "The three major ruling dynasties of the Sangam Age were the Cholas, Cheras and Pandyas.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. Sangam literature reflects Tamil society and polity of the early centuries CE. The Tolkappiyam, a grammar and poetics text, is counted among the earliest Sangam works. The Sangam polity was dominated by the three ruling houses -- Cholas, Cheras and Pandyas.",
    "ancient-sangam-age-overview",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Sangam Age.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding Harshavardhana:",
    [
        "Harshavardhana's court was visited by the Chinese pilgrim Xuanzang (Hiuen Tsang).",
        "The 'Harshacharita', a biography of Harsha, was written by Harsha himself.",
        "Harsha was decisively defeated by the Chalukya ruler Pulakeshin II on the banks of the river Narmada.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Xuanzang visited and left a detailed account of Harsha's court. Statement 2 is incorrect: the Harshacharita was written by Harsha's court poet Banabhatta, not by Harsha himself -- Harsha is instead credited with authoring plays such as Ratnavali, Priyadarshika and Nagananda. Statement 3 is correct: Harsha's southward expansion was halted by Pulakeshin II of the Chalukyas at the Narmada.",
    "ancient-harshavardhana",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on Harshavardhana and the Pushyabhuti dynasty.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding Pallava and Chalukya temple architecture:",
    [
        "The Pallavas are credited with the transition from rock-cut to structural stone temples, exemplified by the Shore Temple at Mahabalipuram.",
        "The Kailasanatha temple at Kanchipuram was built by the Pallava ruler Narasimhavarman I.",
        "The Chalukyas of Badami built temples at Aihole and Pattadakal that show both Nagara and Dravida styles.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: the Pallavas pioneered the shift from rock-cut to free-standing structural temples, seen in the Shore Temple at Mahabalipuram. Statement 2 is incorrect: the Kailasanatha temple at Kanchipuram is associated with Narasimhavarman II (Rajasimha), not Narasimhavarman I -- who is instead linked to the earlier Mahabalipuram monuments and the defeat of Pulakeshin II. Statement 3 is correct: Aihole and Pattadakal, Chalukya sites, are noted (and UNESCO-recognised) precisely for showcasing both Nagara and Dravida temple styles side by side.",
    "ancient-pallava-chalukya-architecture",
    "Old NCERT, Ancient India (R. S. Sharma); NCERT Fine Arts -- Indian temple architecture chapters.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding Jainism:",
    [
        "Mahavira, the 24th Tirthankara, was born at Kundagrama near Vaishali.",
        "The Jain Council held at Vaishali led to the compilation of the 12 Angas.",
        "The split between the Svetambara and Digambara sects of Jainism is traditionally linked to a famine that occurred during the reign of Chandragupta Maurya.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Mahavira was born at Kundagrama, near Vaishali. Statement 2 is incorrect: the compilation of the 12 Angas is traditionally linked to the Jain Council at Pataliputra (under Sthulabhadra), not Vaishali -- Vaishali's Jain association is chiefly as Mahavira's birthplace (and, separately, as the site of the Second BUDDHIST Council). Statement 3 is correct: Jain tradition links the Svetambara-Digambara split to a 12-year famine during Chandragupta Maurya's reign, when Bhadrabahu led a group south while Sthulabhadra remained in Magadha.",
    "ancient-jainism-councils-schism",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on Jainism.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding the Mahajanapadas:",
    [
        "Magadha, with its capital initially at Rajagriha, later shifted its capital to Pataliputra.",
        "Avanti, with its capital at Ujjaini, was one of the four major monarchical Mahajanapadas along with Magadha, Kosala and Vatsa.",
        "Vajji was a Mahajanapada organised as a monarchy under a hereditary king, similar to Magadha.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Magadha's capital shifted from Rajagriha to Pataliputra (under Udayin). Statement 2 is correct: Avanti, Magadha, Kosala and Vatsa are commonly grouped as the four major powers of the period. Statement 3 is incorrect: Vajji (the Vrijji confederacy, capital Vaishali) is the classic example of a gana-sangha -- a republican/oligarchic confederacy -- not a hereditary monarchy like Magadha.",
    "ancient-mahajanapadas",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Mahajanapadas.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding Ashoka's Dhamma:",
    [
        "Ashoka appointed special officers called 'Dhamma Mahamatras' to propagate and oversee the practice of Dhamma.",
        "Ashoka's Dhamma, as reflected in his edicts, was explicitly and exclusively Buddhist in content, requiring conversion to Buddhism.",
        "The Ashokan edicts record Ashoka's visit to Lumbini, the birthplace of the Buddha.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", True), ("All three", False), ("None", False)],
    2, 0.66,
    "Statement 1 is correct: Dhamma Mahamatras were special officers appointed to propagate and supervise Dhamma. Statement 2 is incorrect: Ashoka's Dhamma, as the edicts themselves present it, is a broad ethical code -- non-violence, respect for elders, tolerance of all religious sects, welfare measures -- and was not a demand for conversion to Buddhism; the edicts explicitly urge respect for other sects. Statement 3 is correct: the Rummindei (Lumbini) pillar inscription specifically commemorates Ashoka's visit to the Buddha's birthplace.",
    "ancient-ashoka-dhamma",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on Ashoka's Dhamma.",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding the rock-cut caves at Ajanta and Ellora:",
    [
        "The Ajanta caves are primarily Buddhist in nature, containing both chaityas (prayer halls) and viharas (monasteries).",
        "The Ellora caves, unlike Ajanta, contain rock-cut structures belonging to three faiths -- Buddhism, Hinduism and Jainism.",
        "The Kailasa temple at Ellora, dedicated to Shiva and carved from a single rock from the top downward, was patronised by the Rashtrakuta ruler Krishna I.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. Ajanta's caves are exclusively Buddhist, with both chaityas and viharas. Ellora, by contrast, contains Buddhist, Hindu and Jain caves side by side. The monolithic Kailasa temple at Ellora, carved top-down and dedicated to Shiva, was commissioned under the Rashtrakuta ruler Krishna I.",
    "ancient-ajanta-ellora-caves",
    "NCERT Fine Arts textbook -- chapter on rock-cut architecture; Old NCERT, Ancient India (R. S. Sharma).",
))

rows.append(q_row(
    "History", "Ancient", "statement_based", "medium",
    "Consider the following statements regarding Kautilya's Arthashastra:",
    [
        "It is attributed to Kautilya (Chanakya) and primarily deals with statecraft, economic policy and military strategy.",
        "It identifies land tax, referred to as 'Bhaga', as a principal source of state revenue.",
        "It describes a systematic espionage network, with spies reporting directly to the king.",
    ],
    "How many of the above statements are correct?",
    [("Only one", False), ("Only two", False), ("All three", True), ("None", False)],
    2, 0.66,
    "All three statements are correct. The Arthashastra, attributed to Kautilya, is a treatise on statecraft, economics and military strategy. It identifies Bhaga (a share of agricultural produce) as a principal land tax and revenue source. It also describes an elaborate espionage system reporting to the king, corroborated in part by Megasthenes' account of the Mauryan court.",
    "ancient-arthashastra-mauryan-administration",
    "Old NCERT, Ancient India (R. S. Sharma) -- chapter on the Mauryan Empire and Kautilya's Arthashastra.",
))

sql = "insert into public.questions\n(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\nvalues\n"
sql += ",\n".join(rows)
sql += "\nreturning id, subject, topic, difficulty;"

with open("C:/Users/Pk/prepengine/pyq-analysis-upsc/scratch/content_drafts/batch2_insert.sql", "w", encoding="utf-8") as f:
    f.write(sql)

print(f"Generated {len(rows)} rows, SQL length: {len(sql)} chars")
