# -*- coding: utf-8 -*-
"""Set up the UPSC Prelims 2027 test series from scratch (owner's request, 2026-10-11): one series per
level, a blueprint for every planned paper, and the 27 complete Level-2 papers, dated and unpublished.

  1. Export the bank (signed-in Supabase CLI, -o json) to asm_bank.json:
       select id, concept_group_id as cg, subject, topic, difficulty, type, status, is_active, created_at,
              (select (o.ord - 1)::int from jsonb_array_elements(options) with ordinality o(v, ord)
                where (o.v->>'isCorrect')::boolean limit 1) as key,
              jsonb_array_length(options) as nopt,
              coalesce((question_data->>'fixed_option_order')::boolean, false) as fixed,
              question_data->>'csat_set' as csat_set, (question_data->>'csat_order')::int as csat_order,
              marks_correct::float as mc, marks_wrong::float as mw
       from public.questions where exam_category = 'upsc' order by concept_group_id;
  2. node pyq-analysis-upsc/scratch/upsc_l2_cell_targets.mjs > l2_targets.json   (from the repo root)
  3. node pyq-analysis-upsc/scratch/upsc_l1_cell_targets.mjs > l1_targets.jsonl   (from the repo root)
  4. PYTHONIOENCODING=utf-8 python upsc_series_setup.py asm_bank.json l2_targets.json l1_targets.jsonl
     -> writes upsc_series_setup.sql (one transaction; re-running it updates in place).

How each Level-2 paper is made:
  - GS Test n (1-20): the bank rows of its sub-topic scope, minus Test 21's static rows (their ids are the
    concept_group_ids in gs_l2_t21_*_v2.sql and upg_l2_t21_polity_art21.sql), keeping only rows whose
    (difficulty, type, sub-topic) cell is in the test's buildCells() targets. Every cell must then hold
    exactly its target, which leaves out 7 older published rows whose format is not in their paper's mix.
  - The 100 rows are put in one fixed order (shuffling off, so every candidate sees the same numbering and
    answer key): sub-topics interleaved, about the same number of hard items in every ten positions, the
    first item not hard, no answer letter four times running and no sub-topic three times running.
  - Every paper must have (d) as the key of at least 22 per cent of its items (asserted): the fixed UPSC
    ladders put None / Neither / All at (d), and a bank that drifts to 'Only one' keys makes (d) a guessable
    non-answer (fixed on 2026-10-11 by l2_dshare_fix.sql and pol_l1_t1_dfix.sql).
  - CSAT Test n (1-7): the 80 rows of csat_set 'csat-l2-tNN' in their authored csat_order.
  - Test 21 has 84 of its 100 rows (its 16 current-affairs rows are written nearer its date), so only its
    blueprint is made now.
Level-1 papers are assembled the same way once all 100 rows of a paper exist (their concept ids carry the
paper's prefix, e.g. l1-pol-), checked cell by cell against upsc_l1_cell_targets.mjs. They stay undated until
the owner decides whether Level 1 runs on dates or self-paced.
Tests are created unpublished; the owner approves publishing (the 27 Level-2 papers went live on 2026-10-11 via
upsc_l2_publish.sql, after the answer-(d) fix in l2_dshare_fix.sql). A published paper is frozen: a re-run leaves
its question order, usages and dates untouched, since students may already have sat it. Each test is linked to
the UPSC plan (prelims-2026) and its question_usages are recorded exactly as commit_generated_test() does."""
import glob, io, json, os, random, re, sys, uuid
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
NS = uuid.UUID("6f1c9b52-1d3e-4a43-9a6e-2b7f0c5d8e11")       # fixed namespace: re-runs reuse the same ids
def uid(name): return str(uuid.uuid5(NS, name))
def q(s): return "null" if s is None else "'" + str(s).replace("'", "''") + "'"
def j(o): return q(json.dumps(o, ensure_ascii=False)) + "::jsonb"

GS_CFG, CSAT_CFG = "e6f68e99-3cc7-45de-8b7e-9de24273ff89", "c0626ff4-80be-48ad-a379-5810f2a5dc88"
PLAN = "prelims-2026"
L2_SERIES = "2bd2e098-2e48-4ebf-95a1-d86166211a77"           # the existing Level-2 series, kept

# ------------------------------------------------------------------ series
SERIES = [
    ("l1", uid("series/l1"), "UPSC Prelims 2027 — Level 1: NCERT Foundation",
     "UPSC प्रारंभिक परीक्षा 2027 — स्तर 1: एनसीईआरटी आधार",
     "Foundation papers built on the NCERT textbooks: six GS Paper I subject tests (100 questions, 200 marks, "
     "2 hours each), one GS foundation revision test, and three CSAT half papers (40 questions, 1 hour).",
     "2026-10-11 10:05:00+05:30"),
    ("l2", L2_SERIES, "UPSC Prelims 2027 — Level 2: Sectional Mastery",
     "UPSC प्रारंभिक परीक्षा 2027 — स्तर 2: खंडवार दक्षता",
     "Subject-by-subject papers on the UPSC pattern. 21 GS Paper I tests (100 questions, 200 marks, 2 hours; "
     "+2 / -0.66), one every Sunday at 9:30 am from 1 November 2026 to 21 March 2027, and 7 CSAT Paper II tests "
     "(80 questions, 200 marks, 2 hours; +2.5 / -0.83), every third Saturday at 2:30 pm from 7 November 2026.",
     "2026-10-11 10:04:00+05:30"),
    ("l3", uid("series/l3"), "UPSC Prelims 2027 — Level 3: Integration & Precision",
     "UPSC प्रारंभिक परीक्षा 2027 — स्तर 3: समेकन और सटीकता",
     "Late March to April 2027: six comprehensive GS Paper I tests across the whole syllabus (100 questions, "
     "2 hours) and four harder CSAT Paper II tests (80 questions, 2 hours).",
     "2026-10-11 10:03:00+05:30"),
    ("l4", uid("series/l4"), "UPSC Prelims 2027 — Level 4: Full-Length Simulation",
     "UPSC प्रारंभिक परीक्षा 2027 — स्तर 4: पूर्ण परीक्षा-अनुकरण",
     "April to May 2027, exam-day conditions: ten GS Paper I simulators and nine CSAT Paper II simulators, "
     "two a week in the final stretch, the last one a week before the Prelims.",
     "2026-10-11 10:02:00+05:30"),
    ("ca", uid("series/ca"), "UPSC Prelims 2027 — Current Affairs: Quarterly Tests",
     "UPSC प्रारंभिक परीक्षा 2027 — समसामयिकी: त्रैमासिक टेस्ट",
     "Five current-affairs GS Paper I tests (100 questions, 2 hours), one for each quarter from January-March "
     "2026 to January-March 2027, each linking the quarter's events to the static syllabus.",
     "2026-10-11 10:01:00+05:30"),
]
SID = {k: i for k, i, *_ in SERIES}

# ------------------------------------------------------------------ Level-2 GS papers
# (no, existing blueprint id or None, title, title_hi, theme group, part, syllabus description)
L2 = [
    (1, "4d197c4b", "Polity 1: Constitutional Framework & Rights", "राजव्यवस्था 1: संवैधानिक ढाँचा और अधिकार", "polity", 1,
     "Historical background and making of the Constitution, Preamble, salient features and basic structure, the Union "
     "and its territory, citizenship; Fundamental Rights, Directive Principles, Fundamental Duties; amendment. "
     "Sources: NCERT Class XI 'Indian Constitution at Work'; the Constitution of India."),
    (2, "d537a884", "Polity 2: Parliament & Executive", "राजव्यवस्था 2: संसद और कार्यपालिका", "polity", 2,
     "Parliament and State Legislatures (composition, sessions, law-making, budget, committees, privileges); "
     "President, Vice-President, Prime Minister and Council of Ministers, Attorney General; Governor and Chief "
     "Minister. Sources: NCERT Class XI 'Indian Constitution at Work'; the Constitution; Rules of Procedure."),
    (3, "98d4de60", "Polity 3: Judiciary, Bodies, Elections & Laws", "राजव्यवस्था 3: न्यायपालिका, संस्थाएँ, चुनाव और कानून", "polity", 3,
     "Supreme Court and High Courts, writs, tribunals and landmark judgments; constitutional and statutory bodies; "
     "elections, the Representation of the People Acts and anti-defection; key statutes. Sources: the Constitution; "
     "the Acts; judgments of the Supreme Court."),
    (4, "3fca9f81", "Polity 4: Federalism, Local Government & Governance", "राजव्यवस्था 4: संघवाद, स्थानीय शासन और शासन-व्यवस्था", "polity", 4,
     "Centre-State relations, emergency provisions, special provisions (Fifth and Sixth Schedules, Article 371) and "
     "Union Territories; Panchayats, Municipalities and co-operatives; RTI, e-governance and the civil services. "
     "Sources: the Constitution; NCERT Class XI 'Indian Constitution at Work'; ARC reports."),
    (5, "2beac8f6", "History 1: Modern India", "इतिहास 1: आधुनिक भारत", "history", 1,
     "European arrival and British expansion, 1857, socio-religious reform, the rise of nationalism, phases of the "
     "Congress, Gandhian movements, revolutionaries, constitutional reforms 1909-1935, independence and partition. "
     "Sources: NCERT 'Our Pasts III', 'Themes in Indian History III'."),
    (6, "4063e542", "History 2: Ancient India", "इतिहास 2: प्राचीन भारत", "history", 2,
     "Prehistory, Harappan civilisation, the Vedic age, Mahajanapadas, Buddhism and Jainism, the Mauryas, "
     "post-Mauryan kingdoms, the Sangam age, the Guptas and the post-Gupta period to c. 750 CE. "
     "Sources: NCERT 'Themes in Indian History I', old NCERT 'Ancient India'."),
    (7, "6a6fcb43", "History 3: Medieval India", "इतिहास 3: मध्यकालीन भारत", "history", 3,
     "Early medieval kingdoms, the Delhi Sultanate, Vijayanagara and the Bahmanis, Bhakti and Sufi movements, the "
     "Mughals, the Marathas and regional states. Sources: NCERT 'Our Pasts II', 'Themes in Indian History II'."),
    (8, "c8c1f4f7", "History 4: Art & Culture", "इतिहास 4: कला और संस्कृति", "history", 4,
     "Architecture, sculpture and iconography, painting, music and dance, theatre and puppetry, literature, "
     "philosophy, festivals and heritage lists. Sources: NCERT 'An Introduction to Indian Art'; CCRT; "
     "Ministry of Culture; UNESCO lists."),
    (9, "5338f30b", "Environment 1: Ecology & Biodiversity", "पर्यावरण 1: पारिस्थितिकी और जैव विविधता", "environment", 1,
     "Ecosystems (energy flow, nutrient cycles, succession), fauna and animal behaviour, flora, fungi and forests, "
     "biomes. Sources: NCERT Class XII Biology (ecology unit); IUCN; BSI and ZSI."),
    (10, "fa894e46", "Environment 2: Climate Change & Pollution", "पर्यावरण 2: जलवायु परिवर्तन और प्रदूषण", "environment", 2,
     "Climate science and mitigation, UNFCCC, Kyoto and Paris, carbon markets and India's commitments; air, water, "
     "noise and waste pollution and their rules. Sources: IPCC AR6; UNFCCC; CPCB; MoEFCC."),
    (11, "661e7256", "Environment 3: Policies & Conservation", "पर्यावरण 3: नीतियाँ और संरक्षण", "environment", 3,
     "Protected areas (national parks, sanctuaries, tiger and biosphere reserves, Ramsar sites), the Wild Life "
     "(Protection) Act as amended in 2022, conservation projects; India's environmental laws and bodies; "
     "international conventions and organisations. Sources: MoEFCC; the Acts; Ramsar and UNESCO lists."),
    (12, "f66a6f2d", "Geography 1: World Physical Geography", "भूगोल 1: विश्व का भौतिक भूगोल", "geography", 1,
     "Earth's interior, plates, earthquakes and volcanoes, rocks and landforms; atmosphere, winds, cyclones, "
     "climate types and biomes; oceans; world regions, water bodies and places. Sources: NCERT Class XI "
     "'Fundamentals of Physical Geography'; an atlas."),
    (13, "d47e9834", "Geography 2: Indian Physical Geography", "भूगोल 2: भारत का भौतिक भूगोल", "geography", 2,
     "Physiography, drainage, lakes and wetlands, monsoon and climate, soils, natural vegetation, States and "
     "borders. Sources: NCERT Class XI 'India: Physical Environment'; an atlas."),
    (14, "8752f33c", "Geography 3: Human & Economic Geography", "भूगोल 3: मानव और आर्थिक भूगोल", "geography", 3,
     "Minerals and energy, agriculture, industry, transport and ports, population of India and the world. "
     "Sources: NCERT Class XII 'India: People and Economy', 'Fundamentals of Human Geography'."),
    (15, None, "Economy 1: Basic Concepts, Money & Banking", "अर्थव्यवस्था 1: मूल अवधारणाएँ, मुद्रा और बैंकिंग", "economy", 1,
     "National income, inflation and macro concepts; money, banking, the RBI and monetary policy; financial "
     "markets, instruments and fintech. Sources: NCERT Class XII 'Introductory Macroeconomics'; RBI; SEBI."),
    (16, None, "Economy 2: Growth, Development & External Sector", "अर्थव्यवस्था 2: संवृद्धि, विकास और बाह्य क्षेत्र", "economy", 2,
     "Balance of payments, exchange rates, trade policy, the WTO, the IMF and World Bank and other international "
     "institutions; growth, development, poverty, employment and planning. Sources: NCERT Class XI 'Indian "
     "Economic Development'; Economic Survey; RBI; Ministry of Commerce."),
    (17, None, "Economy 3: Fiscal Policy, Budget & Taxation", "अर्थव्यवस्था 3: राजकोषीय नीति, बजट और कराधान", "economy", 3,
     "Receipts and expenditure, deficits, FRBM and public debt; direct and indirect taxes, GST, and fiscal "
     "federalism. Sources: Union Budget documents; Economic Survey; Finance Commission reports."),
    (18, None, "Economy 4: Agriculture, Industry, Infrastructure & Inclusive Growth", "अर्थव्यवस्था 4: कृषि, उद्योग, अवसंरचना और समावेशी विकास", "economy", 4,
     "Agriculture, food management and farm policy; industry, infrastructure, energy and services; inclusive "
     "growth, welfare and demography. Sources: Economic Survey; Ministry of Agriculture; DPIIT; NSO surveys."),
    (19, None, "Science & Technology 1: General Science", "विज्ञान और प्रौद्योगिकी 1: सामान्य विज्ञान", "science", 1,
     "Physics and everyday science, chemistry and materials, biology, health and biotechnology, astronomy and "
     "earth science. Sources: NCERT Science (Classes VI-X), Physics, Chemistry and Biology (XI-XII)."),
    (20, None, "Science & Technology 2: Space, Digital, Energy & Defence Technology", "विज्ञान और प्रौद्योगिकी 2: अंतरिक्ष, डिजिटल, ऊर्जा और रक्षा प्रौद्योगिकी", "science", 2,
     "Space technology and missions; IT, communication and emerging technologies; energy and environmental "
     "technology; defence, aerospace and security technology. Sources: ISRO; MeitY; DST; DRDO; PIB."),
]
# Rows written for other levels carry a level prefix in their concept id; Level 2 never draws them.
OTHER_LEVELS = ("l1-", "l3-", "l4-", "ca-")

L1_PAPERS = [  # (paper no, concept-id prefix, syllabus description)
    (1, "l1-pol-", "Polity at the NCERT foundation level: the functions and philosophy of the Constitution, liberty, equality, rights, "
     "justice and the rule of law, Parliament and the executive compared with other systems, federalism and power sharing, "
     "local government, elections and electoral systems, governance and the laws NCERT uses to discuss social justice. "
     "Sources: NCERT Classes VIII-XII Political Science; the Constitution of India."),
    (2, "l1-his-", "History at the NCERT foundation level: how historians know the past (sources, methods and the limits of "
     "evidence), the Harappan city, early villages, towns and states, Vedic, Buddhist and Jaina traditions, the medieval world "
     "through travellers, chronicles and the Ain, regional cultures, the colonial countryside, crafts and cities, 1857, reform, "
     "Gandhi and Partition, with the basics of art, architecture and music. "
     "Sources: NCERT Classes VI-VIII Our Pasts I-III; Class XII Themes in Indian History I-III; NCERT art and craft books."),
    (3, "l1-env-", "Environment and Ecology at the NCERT foundation level: forests, plants, fungi and animals and how they live, "
     "populations and the loss of biodiversity, the ozone layer, the greenhouse effect and the carbon cycle, energy and fuels, "
     "water, waste and pollution, conservation by the State and by communities, India's climate policy and carbon markets, and "
     "the ideas behind the international environmental order. "
     "Sources: NCERT Science VII-X, Geography X-XI, Biology XI-XII and Chemistry XI; MoEFCC, BEE, UNFCCC and UNEP."),
    (4, "l1-geo-", "Geography at the NCERT foundation level: the globe, latitudes, longitudes and time, maps, scale and contours, "
     "the atmosphere, winds, rain and the biomes, the continents, oceans and the regions NCERT studies, India's size, relief, "
     "climate and rainfall, rivers, lakes and water resources, rocks, the interior, plates and landforms, the oceans' "
     "temperature, relief and salinity, population, settlements and transport, and resources, minerals and crops. "
     "Sources: NCERT Classes VI-VIII Geography; Contemporary India I-II; Class XI Fundamentals of Physical Geography, "
     "India: Physical Environment and Practical Work; Class XII Fundamentals of Human Geography and India: People and Economy."),
    (5, "l1-eco-", "Economy at the NCERT foundation level: money, credit and banks, how banks create money, sources of business "
     "finance, financial markets, insurance and banking services, the payment systems and investor rules met first, national "
     "income and the Keynesian ideas, taxes and the budget's objectives, food security and the farm economy, land reform and "
     "the Green Revolution, sectors and infrastructure, globalisation and the foreign exchange market, poverty and human capital. "
     "Sources: NCERT Economics IX-XII and Business Studies XI-XII; RBI, SEBI, NPCI and the Ministry of Finance."),
    (6, "l1-sci-", "Science and Technology at the NCERT foundation level: materials, reactions and acids in daily life, combustion, "
     "pressure, sound, light and the eye, electricity at home and electromagnetism, the human body, microbes and heredity, "
     "work, energy and power stations, stars, gravitation and Kepler's laws, ISRO's landmark missions, computer systems, "
     "networks, the internet and software licences, and the basics of India's defence technology. "
     "Sources: NCERT Science VII-X, Physics and Biology XI-XII, Computer Science and Informatics Practices XI-XII; ISRO, DRDO, MNRE and the Ministries of Power and Defence."),
    (7, "l1-rev-", "GS Foundation Revision: the whole static GS syllabus at the NCERT foundation level, in the full-length paper's "
     "subject mix without current affairs -- Polity 18, History with art and culture 19, Environment 18, Geography 12, "
     "Economy 20 and Science and Technology 13 -- revisiting each subject through NCERT chapters and official sources that "
     "the six subject papers did not use. "
     "Sources: NCERT Classes VI-XII (Political Science, History, Fine Art, Geography, Science, Physics, Chemistry, Biology, "
     "Economics and Business Studies); the Constitution and Central Acts; MoEFCC, RBI, SEBI, ISRO and the Ministries concerned."),
]

L2_TEST21 = ("GS Revision: Full Syllabus", "सामान्य अध्ययन पुनरावृत्ति: संपूर्ण पाठ्यक्रम",
             "The whole GS Paper I syllabus on the UPSC mix, with 16 current-affairs questions from the months before it.")

# The 14 Level-2 GS blueprints that already existed (kept, so their ids and history survive): short id -> id.
L2_BLUEPRINTS = {
    "4d197c4b": "4d197c4b-34de-4f4e-a1d4-a6f89373615c",
    "d537a884": "d537a884-e9d4-4a5c-8b8f-5551b5b7de90",
    "98d4de60": "98d4de60-907b-4183-a6fa-e50884157d3f",
    "3fca9f81": "3fca9f81-6358-4450-a511-4972efcd00f9",
    "2beac8f6": "2beac8f6-9a2a-42cd-a0e9-90b5d6bbc2c7",
    "4063e542": "4063e542-f332-451b-8522-0212286f84e5",
    "6a6fcb43": "6a6fcb43-f934-4f6a-994f-990ba032ffac",
    "c8c1f4f7": "c8c1f4f7-b7cd-48ad-be6b-f8afa8d85e90",
    "5338f30b": "5338f30b-0809-4320-949b-de58ebb69c72",
    "fa894e46": "fa894e46-bedd-4d8b-9f31-7671ea84c05d",
    "661e7256": "661e7256-d378-4bf6-b8fa-8ad2a5f853cb",
    "f66a6f2d": "f66a6f2d-b8be-45fb-8492-2d2ede436e28",
    "d47e9834": "d47e9834-3ccb-4073-9055-0eac6fcdbfdb",
    "8752f33c": "8752f33c-ebc7-47a5-894a-e119a6b8a9ae",
}

# ------------------------------------------------------------------ the other levels' blueprints (no papers yet)
SUBJ = [("Polity", "राजव्यवस्था"), ("History", "इतिहास"), ("Environment & Ecology", "पर्यावरण"),
        ("Geography", "भूगोल"), ("Economy", "अर्थव्यवस्था"), ("Science & Technology", "विज्ञान और प्रौद्योगिकी")]
def other_blueprints():
    out = []
    for i, (s, hi) in enumerate(SUBJ, 1):
        out.append(("l1", i, f"Level 1 · Test {i} — {s.replace(' & Ecology', '')} (NCERT Foundation)", f"स्तर 1 · टेस्ट {i} — {hi} (एनसीईआरटी आधार)",
                    "sectional", 100, {"subject": s}, GS_CFG, "upsc27-l1-gs", i))
    out.append(("l1", 7, "Level 1 · Test 7 — GS Foundation Revision", "स्तर 1 · टेस्ट 7 — सामान्य अध्ययन आधार पुनरावृत्ति",
                "full_length", 100, {}, GS_CFG, "upsc27-l1-gs", 7))
    for i in range(1, 4):
        out.append(("l1", 7 + i, f"Level 1 · CSAT Mini {i} — Paper II Half Paper", f"स्तर 1 · सीसैट मिनी {i} — प्रश्नपत्र II अर्ध-प्रश्नपत्र",
                    "full_length", 40, {}, CSAT_CFG, "upsc27-l1-csat", i))
    for i in range(1, 7):
        out.append(("l3", i, f"Level 3 · Test {i} — GS Integrated Test {i}", f"स्तर 3 · टेस्ट {i} — सामान्य अध्ययन समेकित टेस्ट {i}",
                    "full_length", 100, {}, GS_CFG, "upsc27-l3-gs", i))
    for i in range(1, 5):
        out.append(("l3", 6 + i, f"Level 3 · CSAT Test {i} — Paper II (Advanced)", f"स्तर 3 · सीसैट टेस्ट {i} — प्रश्नपत्र II (उन्नत)",
                    "full_length", 80, {}, CSAT_CFG, "upsc27-l3-csat", i))
    for i in range(1, 11):
        out.append(("l4", i, f"Level 4 · Simulator {i} — GS Paper I Full Mock", f"स्तर 4 · सिम्युलेटर {i} — सामान्य अध्ययन प्रश्नपत्र I पूर्ण मॉक",
                    "full_length", 100, {}, GS_CFG, "upsc27-l4-gs", i))
    for i in range(1, 10):
        out.append(("l4", 10 + i, f"Level 4 · CSAT Simulator {i} — Paper II Full Mock", f"स्तर 4 · सीसैट सिम्युलेटर {i} — प्रश्नपत्र II पूर्ण मॉक",
                    "full_length", 80, {}, CSAT_CFG, "upsc27-l4-csat", i))
    Q = [("January to March 2026", "जनवरी से मार्च 2026", "2026-01-01", "2026-03-31"),
         ("April to June 2026", "अप्रैल से जून 2026", "2026-04-01", "2026-06-30"),
         ("July to September 2026", "जुलाई से सितंबर 2026", "2026-07-01", "2026-09-30"),
         ("October to December 2026", "अक्टूबर से दिसंबर 2026", "2026-10-01", "2026-12-31"),
         ("January to March 2027", "जनवरी से मार्च 2027", "2027-01-01", "2027-03-31")]
    for i, (en, hi, a, b) in enumerate(Q, 1):
        out.append(("ca", i, f"Current Affairs · Test {i} — {en}", f"समसामयिकी · टेस्ट {i} — {hi}",
                    "full_length", 100, {"ca_date_range": {"from": a, "to": b}}, GS_CFG, "upsc27-ca", i))
    return out

# ------------------------------------------------------------------ schedule (IST)
GS_DATES = ["2026-11-01", "2026-11-08", "2026-11-15", "2026-11-22", "2026-11-29", "2026-12-06", "2026-12-13",
            "2026-12-20", "2026-12-27", "2027-01-03", "2027-01-10", "2027-01-17", "2027-01-24", "2027-01-31",
            "2027-02-07", "2027-02-14", "2027-02-21", "2027-02-28", "2027-03-07", "2027-03-14", "2027-03-21"]
CSAT_DATES = ["2026-11-07", "2026-11-28", "2026-12-19", "2027-01-09", "2027-01-30", "2027-02-20", "2027-03-13"]

def main():
    bank_path, targets_path = sys.argv[1], sys.argv[2]
    l1_targets = {}
    if len(sys.argv) > 3:
        for line in io.open(sys.argv[3], encoding="utf-8"):
            if line.strip():
                x = json.loads(line)
                l1_targets[x["no"]] = Counter({(c[0], c[1], c[2]): c[3] for c in x["cells"]})
    raw = io.open(bank_path, encoding="utf-8").read()
    bank = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])["rows"]
    targets = json.load(open(targets_path, encoding="utf-8"))
    by_cg = {r["cg"]: r for r in bank}
    t21 = set()
    for f in glob.glob(os.path.join(HERE, "gs_l2_t21_*_v2.sql")) + [os.path.join(HERE, "upg_l2_t21_polity_art21.sql")]:
        t21 |= set(re.findall(r"concept_group_id = '([^']+)'", io.open(f, encoding="utf-8").read()))
    t21 &= set(by_cg)
    assert len(t21) == 84, len(t21)

    sql = ["begin;"]
    # series
    for key, sid, title, title_hi, desc, created in SERIES:
        sql.append("insert into public.test_series (id, title, title_hi, description, exam_category, is_free, price, created_at) values "
                   f"({q(sid)}, {q(title)}, {q(title_hi)}, {q(desc)}, 'upsc', false, 0, {q(created)}) on conflict (id) do update set "
                   "title = excluded.title, title_hi = excluded.title_hi, description = excluded.description, created_at = excluded.created_at;")
    # blueprints
    bp_ids = {}
    def blueprint(bid, series, pos, title, title_hi, pattern, count, scope, cfg, theme, part):
        sql.append("insert into public.test_blueprints (id, exam_category, series_id, sequence_position, title, title_hi, pattern_type, "
                   "question_count, subject_scope, distribution_config_id, theme_group_id, theme_part_index, updated_at) values "
                   f"({q(bid)}, 'upsc', {q(SID[series])}, {pos}, {q(title)}, {q(title_hi)}, {q(pattern)}, {count}, {j(scope)}, {q(cfg)}, "
                   f"{q(theme)}, {part}, now()) on conflict (id) do update set series_id = excluded.series_id, sequence_position = excluded.sequence_position, "
                   "title = excluded.title, title_hi = excluded.title_hi, pattern_type = excluded.pattern_type, question_count = excluded.question_count, "
                   "subject_scope = excluded.subject_scope, distribution_config_id = excluded.distribution_config_id, theme_group_id = excluded.theme_group_id, "
                   "theme_part_index = excluded.theme_part_index, updated_at = now();")
    existing = L2_BLUEPRINTS
    for no, short, title, title_hi, theme, part, _desc in L2:
        bid = existing[short] if short else uid(f"blueprint/l2/gs/{no}")
        bp_ids[("gs", no)] = (bid, f"upsc27-l2-{theme}")
        subs = sorted({c["topic"] for c in targets[str(no)]}, key=lambda s: [c["topic"] for c in targets[str(no)]].index(s))
        subject = next(r["subject"] for r in bank if r["topic"] == subs[0])
        blueprint(bid, "l2", no, f"Level 2 · Test {no} — {title}", f"स्तर 2 · टेस्ट {no} — {title_hi}", "sectional", 100,
                  {"subject": subject, "sub_topics": subs}, GS_CFG, f"upsc27-l2-{theme}", part)
    blueprint(uid("blueprint/l2/gs/21"), "l2", 21, f"Level 2 · Test 21 — {L2_TEST21[0]}", f"स्तर 2 · टेस्ट 21 — {L2_TEST21[1]}",
              "full_length", 100, {}, GS_CFG, "upsc27-l2-revision", 1)
    for n in range(1, 8):
        bid = uid(f"blueprint/l2/csat/{n}")
        bp_ids[("csat", n)] = (bid, "upsc27-l2-csat")
        blueprint(bid, "l2", 21 + n, f"Level 2 · CSAT Test {n} — Paper II: Aptitude & Comprehension",
                  f"स्तर 2 · सीसैट टेस्ट {n} — प्रश्नपत्र II: अभिक्षमता और बोधगम्यता", "full_length", 80, {}, CSAT_CFG, "upsc27-l2-csat", n)
    for series, pos, title, title_hi, pattern, count, scope, cfg, theme, part in other_blueprints():
        blueprint(uid(f"blueprint/{series}/{pos}"), series, pos, title, title_hi, pattern, count, scope, cfg, theme, part)

    # Level-2 papers
    report, tests = [], []
    for no, short, title, title_hi, theme, part, desc in L2:
        cells = {(c["difficulty"], c["type"], c["topic"]): c["n"] for c in targets[str(no)]}
        subs = {k[2] for k in cells}
        rows = [r for r in bank if r["topic"] in subs and not r["csat_set"] and r["cg"] not in t21 and not r["cg"].startswith(OTHER_LEVELS)
                and (r["difficulty"], r["type"], r["topic"]) in cells]
        have = Counter((r["difficulty"], r["type"], r["topic"]) for r in rows)
        assert have == Counter(cells), f"Test {no}: cells differ from targets"
        order = arrange(rows, seed=no)
        tests.append(("gs", no, f"Level 2 · Test {no} — {title}", f"स्तर 2 · टेस्ट {no} — {title_hi}",
                      desc + " 100 questions · 200 marks · 2 hours · +2 / -0.66.", f"{GS_DATES[no - 1]} 09:30:00+05:30",
                      "General Studies Paper I", "सामान्य अध्ययन प्रश्नपत्र I", order))
    for n in range(1, 8):
        rows = sorted((r for r in bank if r["csat_set"] == f"csat-l2-t{n:02d}"), key=lambda r: r["csat_order"])
        assert [r["csat_order"] for r in rows] == list(range(1, 81)), n
        tests.append(("csat", n, f"Level 2 · CSAT Test {n} — Paper II: Aptitude & Comprehension",
                      f"स्तर 2 · सीसैट टेस्ट {n} — प्रश्नपत्र II: अभिक्षमता और बोधगम्यता",
                      "The full CSAT Paper II syllabus: 34 quantitative aptitude, 18 logical reasoning and 28 reading-comprehension "
                      "questions on 10 passages, in the UPSC order. 80 questions · 200 marks · 2 hours · +2.5 / -0.83; qualifying at 33%.",
                      f"{CSAT_DATES[n - 1]} 14:30:00+05:30", "CSAT Paper II", "सीसैट प्रश्नपत्र II", rows))
    l1_titles = {pos: (t, th) for series, pos, t, th, *_ in other_blueprints() if series == "l1"}
    for no, prefix, desc in L1_PAPERS:
        rows = [r for r in bank if r["cg"].startswith(prefix)]
        if len(rows) < 100:
            print(f"Level 1 Test {no}: {len(rows)} of 100 rows, paper not made yet")
            continue
        assert Counter((r["difficulty"], r["type"], r["topic"]) for r in rows) == l1_targets[no], f"Level 1 Test {no}: cells differ from targets"
        bp_ids[("l1", no)] = (uid(f"blueprint/l1/{no}"), "upsc27-l1-gs")
        tests.append(("l1", no, *l1_titles[no], desc + " 100 questions · 200 marks · 2 hours · +2 / -0.66.", None,
                      "General Studies Paper I", "सामान्य अध्ययन प्रश्नपत्र I", arrange(rows, seed=100 + no)))
    seen = set()
    for kind, n, title, title_hi, desc, when, sec, sec_hi, rows in tests:
        ids = [r["id"] for r in rows]
        assert not (seen & set(ids)), f"{title}: a question is in two tests"
        seen |= set(ids)
        tid = uid(f"test/l1/gs/{n}") if kind == "l1" else uid(f"test/l2/{kind}/{n}")
        series_id = SID["l1"] if kind == "l1" else L2_SERIES
        bid, theme = bp_ids[(kind, n)]
        sections = [{"id": "s1", "name": sec, "name_hi": sec_hi, "questionIds": ids}]
        sql.append("insert into public.tests (id, exam_category, title, title_hi, description, series_id, blueprint_id, duration_min, sections, "
                   "is_free, is_published, shuffle_questions, shuffle_options, scheduled_for) values "
                   f"({q(tid)}, 'upsc', {q(title)}, {q(title_hi)}, {q(desc)}, {q(series_id)}, {q(bid)}, 120, {j(sections)}, false, false, false, false, {q(when)}) "
                   "on conflict (id) do update set title = excluded.title, title_hi = excluded.title_hi, description = excluded.description, "
                   "series_id = excluded.series_id, blueprint_id = excluded.blueprint_id, duration_min = excluded.duration_min, sections = excluded.sections, "
                   "shuffle_questions = excluded.shuffle_questions, shuffle_options = excluded.shuffle_options, scheduled_for = excluded.scheduled_for, updated_at = now() "
                   "where not public.tests.is_published;")      # a published paper is frozen: students may already have sat it
        draft = f"exists (select 1 from public.tests where id = {q(tid)} and not is_published)"
        sql.append(f"delete from public.question_usages where test_id = {q(tid)} and {draft};")
        sql.append("insert into public.question_usages (question_id, test_id, blueprint_id, theme_group_id, concept_group_id) "
                   f"select q.id, {q(tid)}, {q(bid)}, {q(theme)}, q.concept_group_id from public.questions q where q.id = any(array[{', '.join(q(i) for i in ids)}]::uuid[]) and {draft};")
        sql.append("update public.questions q set times_used = (select count(*) from public.question_usages u where u.question_id = q.id), "
                   f"last_used_test_id = {q(tid)}, last_used_date = now() where q.id = any(array[{', '.join(q(i) for i in ids)}]::uuid[]) and {draft};")
        sql.append(f"insert into public.plan_tests (plan_code, test_id) select {q(PLAN)}, {q(tid)} "
                   f"where not exists (select 1 from public.plan_tests where plan_code = {q(PLAN)} and test_id = {q(tid)});")
        keys = "".join("abcd"[r["key"]] for r in rows)
        report.append((title, len(rows), (when or "undated")[:10], keys, "".join(r["difficulty"][0] for r in rows)))
    sql.append("commit;")
    sql.append("select (select count(*) from public.test_series where exam_category = 'upsc') as series, "
               "(select count(*) from public.test_blueprints where exam_category = 'upsc' and series_id is not null) as blueprints, "
               "(select count(*) from public.tests where exam_category = 'upsc') as tests, "
               "(select count(*) from public.question_usages u join public.tests t on t.id = u.test_id where t.exam_category = 'upsc') as usages, "
               "(select count(*) from public.plan_tests where plan_code = 'prelims-2026') as plan_links;")
    io.open(os.path.join(HERE, "upsc_series_setup.sql"), "w", encoding="utf-8", newline="\n").write("\n".join(sql) + "\n")
    for title, n, when, keys, diff in report:
        run = best = 1
        for a, b in zip(keys, keys[1:]):
            run = run + 1 if a == b else 1; best = max(best, run)
        qtr = -(-len(diff) // 4)                    # four equal quarters (20 items in an 80-item paper)
        hard = [diff[i:i + qtr].count("h") for i in range(0, len(diff), qtr)]
        share = Counter(keys)                   # the fixed ladders put None / Neither / All at (d): keep (d) a real answer
        assert share["d"] >= round(0.22 * n), f"{title}: only {share['d']} (d) keys of {n} -- re-key some items first (see l2_dshare_fix.py)"
        print(f"{when:10} {n:>3} q | longest letter run {best} | keys {'/'.join(str(share[c]) for c in 'abcd')} | hard by quarter {hard} | {title}")
    print(f"upsc_series_setup.sql: {len(SERIES)} series, {len(L2) + 8 + len(other_blueprints())} blueprints, {len(tests)} tests, {len(seen)} questions")

def arrange(rows, seed):
    """One fixed order for a GS paper: sub-topics interleaved, hard items spread, short letter runs."""
    rng = random.Random(seed)
    topics = sorted({r["topic"] for r in rows})
    by = {t: sorted((r for r in rows if r["topic"] == t), key=lambda r: r["cg"]) for t in topics}
    for t in topics:
        rng.shuffle(by[t])
    keyed = []
    for ti, t in enumerate(topics):
        for k, r in enumerate(by[t]):
            keyed.append(((k + rng.random()) / len(by[t]), ti, r))
    order = [r for *_, r in sorted(keyed, key=lambda x: x[:2])]
    H = sum(r["difficulty"] == "hard" for r in order) / len(order)
    E = sum(r["difficulty"] == "easy" for r in order) / len(order)
    multi = len(topics) > 1
    def cost(o):
        c = 0.0
        d = [r["difficulty"] for r in o]
        for i in range(len(o) - 9):
            w = d[i:i + 10]
            c += (w.count("hard") - 10 * H) ** 2 + 0.5 * (w.count("easy") - 10 * E) ** 2
        c += 6 * (d[0] == "hard") + 3 * (d[1] == "hard")
        for key, limit, pen in (("key", 3, 40), ("topic", 2, 4 if multi else 0), ("type", 3, 1.5)):
            run = 1
            for a, b in zip(o, o[1:]):
                run = run + 1 if a[key] == b[key] else 1
                if run > limit:
                    c += pen
        run = 1
        for a, b in zip(d, d[1:]):
            run = run + 1 if a == b == "hard" else 1
            if run >= 3:
                c += 8
        return c
    cur, best, best_c = list(order), list(order), cost(order)
    cur_c, temp = best_c, 3.0
    for _ in range(20000):
        i, k = rng.sample(range(len(cur)), 2)
        cur[i], cur[k] = cur[k], cur[i]
        new = cost(cur)
        if new <= cur_c or rng.random() < pow(2.718, (cur_c - new) / temp):
            cur_c = new
            if new < best_c:
                best, best_c = list(cur), new
        else:
            cur[i], cur[k] = cur[k], cur[i]
        temp = max(0.02, temp * 0.9997)
    return best

if __name__ == "__main__":
    main()
