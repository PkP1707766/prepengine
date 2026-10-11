# -*- coding: utf-8 -*-
"""MCQ reorders for the Level-2 answer-(d) fix: concept id -> the key letter before the move (l2_dshare_fix.py moves
the key to (d) and keeps the distractors in order). Chosen by paper: the most over-used letter first, only MCQs whose
option order means nothing, MCQ (d) share capped at about 36 % of the paper's MCQs."""
REORDERS = {
    # Level 2 · Test 1 — Polity 1: Constitutional Framework & Rights
    "polity-prospective-overruling-golaknath": "a",
    "polity-not-a-feature-presidential": "b",
    # Level 2 · Test 2 — Polity 2: Parliament & Executive
    "parl-money-bill-fines-not": "b",
    "executive-president-discharge-functions-cji": "b",
    # Level 2 · Test 3 — Polity 3: Judiciary, Bodies, Elections & Laws
    "elections-national-party-four-states": "b",
    "polity-constitutional-statutory-nonstatutory-bodies": "c",
    # Level 2 · Test 4 — Polity 4: Federalism, Local Government & Governance
    "gov-umang-app": "c",
    "federalism-centre-state-commissions": "c",
    "federalism-art268-stamp-duties": "a",
    # Level 2 · Test 5 — History 1: Modern India
    "modern-all-india-kisan-sabha-1936": "b",
    "modern-morley-minto-viceroy": "b",
    "modern-tilak-swaraj-birthright": "b",
    "modern-tebhaga-movement": "b",
    # Level 2 · Test 6 — History 2: Ancient India
    "ancient-mehrauli-pillar-chandra": "b",
    "ancient-vedanga-jyotisha": "b",
    "ancient-mahapadma-nanda": "b",
    "ancient-taxila-gandhara": "b",
    "ancient-mauryan-officials-sannidhata": "a",
    "ancient-bindusara-mauryan-empire": "b",
    # Level 2 · Test 7 — History 3: Medieval India
    "medieval-iqta-system-delhi-sultanate": "b",
    "medieval-chola-port-nagapattinam": "b",
    "medieval-gita-govinda-jayadeva": "b",
    "medieval-razia-sultan": "b",
    # Level 2 · Test 8 — History 4: Art & Culture
    "art-dilwara-jain-temples": "c",
    "culture-chhath-surya": "c",
    # Level 2 · Test 9 — Environment 1: Ecology & Biodiversity
    "env-gymnosperm-groups": "a",
    "env-jacana-polyandry": "c",
    "env-seagrass-angiosperm": "a",
    # Level 2 · Test 11 — Environment 3: Policies & Conservation
    "env-first-marine-national-park": "a",
    "env-eco-sensitive-zones": "a",
    # Level 2 · Test 12 — Geography 1: World Physical Geography
    "geo-thinnest-layer-easy": "b",
    "geo-hottest-deserts-not-equator": "b",
    "geo-air-mass-mt": "b",
    "geo-tornadoes-great-plains": "a",
    "geo-red-sea-salinity": "b",
    # Level 2 · Test 13 — Geography 2: Indian Physical Geography
    "igeo-largest-state-rajasthan-easy": "a",
    "irv-chilika-largest-lagoon": "a",
    # Level 2 · Test 14 — Geography 3: Human & Economic Geography
    "res-jharia-coalfield": "c",
    "res-golden-fibre-jute-easy": "c",
    "res-operation-flood-milk": "a",
    "tr-sagarmala": "c",
    # Level 2 · Test 15 — Economy 1: Basic Concepts, Money & Banking
    "econ-qualitative-moral-suasion": "b",
    "fm-unified-lending-interface": "a",
    # Level 2 · Test 16 — Economy 2: Growth, Development & External Sector
    "ex-rodtep": "a",
    "ex-hot-money": "b",
    "ex-merchandise-trade-easy": "a",
    # Level 2 · Test 17 — Economy 3: Fiscal Policy, Budget & Taxation
    "ft-15th-fc-criteria": "a",
    # Level 2 · Test 18 — Economy 4: Agriculture, Industry, Infrastructure & Inclusive Growth
    "ag-msp-not-covered": "c",
    "in-capacity-utilisation": "c",
    "in-infrastructure-easy": "b",
    # Level 2 · Test 19 — Science & Technology 1: General Science
    "as-red-planet-easy": "a",
    "ch-baking-soda-vinegar-easy": "a",
    "as-hubble-constant": "a",
    # Level 2 · Test 20 — Science & Technology 2: Space, Digital, Energy & Defence Technology
    "en-hydro-easy": "b",
    "df-amca": "a",
    "it-federated-learning": "b",
    "en-otec": "a",
    # Level 2 · Test 21 (static)
    "ft-pigouvian-tax": "a",
    "medieval-suraj-mal-bharatpur": "a",
}
