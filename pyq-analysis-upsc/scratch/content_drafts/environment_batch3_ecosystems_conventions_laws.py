# -*- coding: utf-8 -*-
"""Environment & Ecology batch 3: every remaining cell for Ecosystems & Ecological Processes (10),
International Conventions & Organisations (7) and Indian Environmental Laws & Bodies (5), from the
live gap report regenerated 2026-09-28 after batch 2 (bank 39 rows, 81 to draft).

Formats follow the PYQ evidence for these sub-topics: Ecosystems uses 2025's Roman-numbered
'which of the statements' form (2025-Q40) alongside counts and pairs; Laws uses 2026's
'1 and 3 only' combination style (2026-Q77 NIRANTAR). The Statement-I/II slots are the ones
allotted on 2026-09-27: Ecosystems gets the two-statement form, and International Conventions
gets the 2025 three-statement form (Statements II and III as explanations of I).

No row repeats a PYQ angle for these sub-topics (the 2015-26 list in
environment_subtopic_retag.csv). The Polity bank already pairs CPCB with its ministry, so the
easy Laws row is about the NTCA instead. Currency-sensitive facts were web-checked on
2026-09-28: the High Seas (BBNJ) Agreement entered into force on 17 January 2026 and India has
signed it (its ratification is not asserted); the Forest (Conservation) Amendment Act, 2023
(in force 1 December 2023) exempts strategic linear projects within 100 km of the borders and
counts government zoos and safaris outside protected areas as forestry activities; the
Biological Diversity (Amendment) Act, 2023 exempts registered AYUSH practitioners from prior
intimation. NCERT chapters are cited by name, since the rationalised editions renumbered them.
"""
import os
import polity_common as pc
from polity_common import stmt, stmt_opts, mcq, ar, ar3, pairs, C3, C4, T2, write_sql

pc.SUBJECT = "Environment & Ecology"
EC = "Ecosystems & Ecological Processes"
IC = "International Conventions & Organisations"
IL = "Indian Environmental Laws & Bodies"

CLASSIC = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
Y26 = ["1 only", "1 and 2", "2 and 3", "3 only"]
ROMAN = ["I and II only", "II and III only", "I and III only", "I, II and III"]
NCERT_ECO = "NCERT Biology Class XII, ch. 'Ecosystem'"
NCERT_ORG = "NCERT Biology Class XII, ch. 'Organisms and Populations'"
FALSE_AT = {}

# ============================ ECOSYSTEMS (10) ============================

# --- medium / statement (4) ---
stmt(EC, "medium", "Consider the following statements about ecological pyramids:",
  ["The pyramid of energy is always upright.",
   "In the sea, the pyramid of biomass is generally inverted, because the biomass of fishes far exceeds that of the phytoplankton at any one time.",
   "The pyramid of numbers for a single large tree and the insects feeding on it is upright."],
  C3, 1,
  "Only statements 1 and 2 are correct. Energy is lost as heat at every transfer, so the pyramid of energy can never be "
  "inverted. In the sea the standing crop of phytoplankton at any moment is smaller than the biomass of the fishes it "
  "supports (the phytoplankton turn over very fast), so the biomass pyramid is inverted. Statement 3 is wrong: one tree "
  "supports a great many insects, so that pyramid of numbers is inverted.",
  "env-ecological-pyramids", f"{NCERT_ECO} (ecological pyramids).")
FALSE_AT["env-ecological-pyramids"] = 3

stmt(EC, "medium", "Consider the following statements about ecological succession:",
  ["In hydrarch succession, the series progresses from mesic towards hydric conditions.",
   "Primary succession begins where no soil existed before, such as on bare rock or newly cooled lava.",
   "Secondary succession is usually faster than primary succession, because soil is already present.",
   "The community that is in near-equilibrium with the environment at the end of a succession is called the climax community."],
  C4, 2,
  "Only statements 2, 3 and 4 are correct. Primary succession starts where there was no soil; secondary succession, on "
  "abandoned farmland or burnt or felled forest, is faster because soil (and often seeds) remains. Succession ends in a "
  "climax community. Statement 1 reverses the direction: hydrarch succession runs from hydric (wet) towards mesic "
  "conditions, and xerarch succession from xeric towards mesic -- both converge on medium-moisture conditions.",
  "env-succession-hydrarch", f"{NCERT_ECO} (ecological succession).")
FALSE_AT["env-succession-hydrarch"] = 1

stmt_opts(EC, "medium", "With reference to energy flow in ecosystems, consider the following statements:",
  ["Roughly 10 per cent of the energy at one trophic level is passed on to the next.",
   "In aquatic ecosystems, the detritus food chain is the main conduit of energy flow.",
   "In terrestrial ecosystems, a much larger fraction of energy flows through the detritus food chain than through the grazing food chain."],
  ["I and II only", "II only", "II and III only", "I and III only"], 3,
  "Statements I and III are correct. By Lindeman's ten per cent law only about a tenth of the energy at one trophic level "
  "reaches the next. Statement II is the reversal: in aquatic ecosystems the grazing food chain is the major conduit for "
  "energy flow, whereas on land a much larger fraction flows through the detritus food chain.",
  "env-energy-flow-food-chains", f"{NCERT_ECO} (energy flow; grazing and detritus food chains).",
  roman=True)
FALSE_AT["env-energy-flow-food-chains"] = 2

stmt_opts(EC, "medium", "Consider the following statements:",
  ["An ecotone is a zone of transition between two ecosystems, such as the belt where a forest meets a grassland.",
   "The number of species, and the density of some species, is often higher in an ecotone than in the adjoining communities; this is called the edge effect.",
   "A keystone species is, by definition, the most abundant species in its community."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. An ecotone mixes species of both neighbouring communities plus some of its own, which "
  "is why it is often richer -- the edge effect. Statement 3 is wrong: a keystone species is one whose influence on the "
  "community is disproportionately large relative to its abundance. The textbook case is the sea otter, whose predation on "
  "sea urchins keeps kelp forests from being grazed away; keystone species are often not abundant at all.",
  "env-ecotone-keystone", "E. P. Odum, Fundamentals of Ecology (ecotones and the edge effect); R. T. Paine (1969), American Naturalist 103 (keystone species).")
FALSE_AT["env-ecotone-keystone"] = 3

# --- easy / statement (1) ---
stmt(EC, "easy", "Consider the following statements:",
  ["The atmosphere is the main reservoir of phosphorus.",
   "Atmospheric nitrogen can be fixed by lightning as well as by certain bacteria."],
  T2, 1,
  "Only statement 2 is correct. Phosphorus has a sedimentary cycle: its natural reservoir is rock, from which weathering "
  "releases phosphates, and unlike carbon there is no respiratory release of phosphorus into the atmosphere. Nitrogen is "
  "fixed both by lightning and industrial processes and biologically, by bacteria such as Rhizobium and by cyanobacteria.",
  "env-phosphorus-nitrogen-cycles", f"{NCERT_ECO} (phosphorus cycle); NCERT Biology Class XI (pre-2023 edition), ch. 'Mineral Nutrition' (nitrogen fixation).")
FALSE_AT["env-phosphorus-nitrogen-cycles"] = 1

# --- hard / statement (1) ---
stmt(EC, "hard", "Consider the following statements about productivity in ecosystems:",
  ["Net primary productivity is gross primary productivity minus the energy the producers use in respiration.",
   "Secondary productivity is the rate at which producers form new organic matter.",
   "Although the oceans cover about 70 per cent of the Earth's surface, they account for only about one-third of the biosphere's annual net primary productivity.",
   "Primary productivity depends only on the plant species of an area, not on nutrient availability or other environmental factors."],
  C4, 1,
  "Only statements 1 and 3 are correct. NPP = GPP minus respiration losses, and NPP is what is available to consumers. "
  "Of the biosphere's roughly 170 billion tonnes (dry weight) of annual NPP, the oceans produce only about 55 billion "
  "tonnes. Statement 2 is wrong: secondary productivity is the rate at which consumers form new organic matter. "
  "Statement 4 is wrong: primary productivity depends on the plant species and also on the environment, nutrient "
  "availability and the plants' photosynthetic capacity.",
  "env-productivity-npp", f"{NCERT_ECO} (productivity).")
FALSE_AT["env-productivity-npp"] = "2,4"

# --- medium / mcq (1) ---
mcq(EC, "medium", "Gause's 'competitive exclusion principle' states that:",
  ["a predator always keeps its prey population below the carrying capacity of the habitat",
   "a species always occupies the whole of its fundamental niche",
   "only about 10 per cent of the energy at one trophic level passes on to the next",
   "two closely related species competing for the same limiting resources cannot coexist indefinitely, and the competitively inferior one is eventually eliminated"],
  3,
  "Gause's principle holds that two closely related species competing for the same resources cannot coexist indefinitely; "
  "the inferior competitor is eventually eliminated. It applies when the resources are limiting. Competitors can still "
  "coexist through resource partitioning, as in MacArthur's warblers, which feed in different parts of the same tree. "
  "The third option is Lindeman's ten per cent law.",
  "env-competitive-exclusion", f"{NCERT_ORG} (population interactions: competition).")

# --- medium / Statement-I/II (1) ---
ar(EC, "medium", "Soils under tropical rainforests are generally poor in nutrients.",
  "In tropical rainforests most nutrients are held in the living vegetation and are recycled quickly, because warm, humid conditions speed up decomposition.",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Warmth and moisture make decomposition fast, and the "
  "released nutrients are taken up almost at once by the dense vegetation, so little accumulates in the soil; heavy rain "
  "leaches away much of the rest. That is why cleared rainforest land loses its fertility within a few seasons.",
  "env-rainforest-soil-nutrients", f"{NCERT_ECO} (decomposition and the factors affecting its rate).")

# --- hard / match (2) ---
pairs(EC, "hard", "Consider the following pairs of ecological terms and their meanings:",
  ["Ecotone", "Ecological niche", "Sere", "Standing crop"],
  ["Zone of transition between two communities",
   "The physical place where an organism lives",
   "The sequence of communities that replace one another during a succession",
   "The amount of nutrients present in the soil at a given time"],
  1,
  "Only two pairs are correct: 1 and 3. Pair 2 describes a habitat; a niche is an organism's functional role together "
  "with the full range of conditions and resources it uses. Pair 4 describes the standing state; the standing crop is "
  "the mass of living material at a trophic level at a particular time.",
  "env-ecology-terms-pairs", f"{NCERT_ECO} (standing crop, standing state, seres); {NCERT_ORG} (niche).")

pairs(EC, "hard", "Consider the following pairs of types of ecological succession and where they begin:",
  ["Hydrosere", "Lithosere", "Psammosere", "Xerosere"],
  ["A water body", "Bare rock", "Saline soil or saline water", "A dry habitat"],
  2,
  "Only three pairs are correct: 1, 2 and 4. A psammosere begins on sand, such as coastal dunes; succession on saline "
  "soil or in saline water is a halosere. A lithosere (on rock) is one kind of xerosere.",
  "env-seres-pairs", f"E. P. Odum, Fundamentals of Ecology (ecological succession); {NCERT_ECO} (ecological succession).")

# ======================= INTERNATIONAL CONVENTIONS (7) =======================

# --- medium / statement (3) ---
stmt(IC, "medium", "Consider the following statements about the Convention on Biological Diversity (CBD) and its protocols:",
  ["The Cartagena Protocol deals with the safe transfer, handling and use of living modified organisms.",
   "The Nagoya-Kuala Lumpur Supplementary Protocol deals with liability and redress for damage caused by living modified organisms.",
   "The United States is a Party to the CBD."],
  C3, 1,
  "Only statements 1 and 2 are correct. The Cartagena Protocol on Biosafety (2000) covers living modified organisms, and "
  "its Nagoya-Kuala Lumpur Supplementary Protocol (2010, in force 2018) adds rules on liability and redress. Statement 3 "
  "is wrong: the United States signed the CBD in 1993 but has never ratified it, so it is not a Party.",
  "env-cbd-protocols", "CBD Secretariat, list of Parties; Cartagena Protocol on Biosafety (2000); Nagoya-Kuala Lumpur Supplementary Protocol on Liability and Redress (2010).")
FALSE_AT["env-cbd-protocols"] = 3

stmt(IC, "medium", "Consider the following statements about the Kunming-Montreal Global Biodiversity Framework:",
  ["It was adopted at the fifteenth Conference of the Parties (COP15) to the Convention on Biological Diversity in December 2022.",
   "One of its targets is to effectively conserve at least 30 per cent of the world's land and inland waters, and of its coastal and marine areas, by 2030.",
   "It sets 23 action-oriented global targets for 2030.",
   "It is a legally binding treaty that imposes penalties on countries that miss its targets."],
  C4, 2,
  "Only statements 1, 2 and 3 are correct. The framework was adopted at CBD COP15 (held in Montreal under China's "
  "presidency) in December 2022, with four goals for 2050 and 23 targets for 2030, including '30 by 30' (Target 3). "
  "Statement 4 is wrong: it is a decision of the Parties, not a treaty; countries report progress through national "
  "biodiversity strategies and action plans, and there are no penalties.",
  "env-kunming-montreal-gbf", "CBD Decision 15/4, Kunming-Montreal Global Biodiversity Framework (December 2022).")
FALSE_AT["env-kunming-montreal-gbf"] = 4

stmt_opts(IC, "medium", "Consider the following statements about the Convention on the Conservation of Migratory Species of Wild Animals (CMS):",
  ["Its Secretariat is provided by the IUCN.",
   "It is also known as the Bonn Convention.",
   "India hosted its thirteenth Conference of the Parties (COP13) at Gandhinagar in 2020."],
  ROMAN, 1,
  "Statements II and III are correct. The CMS was signed at Bonn in 1979, hence the 'Bonn Convention', and India hosted "
  "CMS COP13 at Gandhinagar in February 2020. Statement I is wrong: the CMS is an environmental treaty under the "
  "United Nations Environment Programme, which provides its Secretariat; the IUCN is a separate membership union.",
  "env-cms-bonn", "CMS Secretariat (UNEP), convention text and COP13, Gandhinagar, February 2020.",
  roman=True)
FALSE_AT["env-cms-bonn"] = 1

# --- easy / statement (1) ---
stmt(IC, "easy", "Consider the following statements about the United Nations Environment Programme (UNEP):",
  ["It is headquartered in Nairobi.",
   "It was set up following the 1972 United Nations Conference on the Human Environment at Stockholm."],
  T2, 2,
  "Both statements are correct. UNEP was established by the UN General Assembly in December 1972, following the Stockholm "
  "Conference, and has its headquarters in Nairobi, Kenya.",
  "env-unep-stockholm", "UNEP, 'About the UN Environment Programme'; UN General Assembly resolution 2997 (XXVII), 1972.")

# --- hard / statement (1) ---
stmt(IC, "hard", "Consider the following statements about the 'High Seas Treaty' (the BBNJ Agreement):",
  ["It is an agreement under the United Nations Convention on the Law of the Sea (UNCLOS).",
   "It applies to marine areas beyond national jurisdiction: the high seas and the international seabed area.",
   "It entered into force in January 2026, after the required 60 ratifications were reached.",
   "India has signed it."],
  C4, 3,
  "All four statements are correct. The Agreement on Marine Biological Diversity of Areas beyond National Jurisdiction "
  "was adopted in 2023 as the third implementing agreement under UNCLOS. It covers the high seas and 'the Area' (the "
  "international seabed). The 60th ratification came in September 2025, and it entered into force 120 days later, on "
  "17 January 2026. India signed it in 2024. The difficulty is that each statement sounds plausible either way.",
  "env-bbnj-high-seas", "UN, Agreement under UNCLOS on the Conservation and Sustainable Use of Marine Biological Diversity of Areas beyond National Jurisdiction (2023); UN Treaty Collection, status of the Agreement (in force 17 January 2026).")

# --- medium / mcq (1) ---
mcq(IC, "medium", "The 'Living Planet Report', which tracks the average change in monitored populations of wild vertebrates, is published by:",
  ["IUCN", "UNEP", "Wetlands International", "WWF"], 3,
  "The Living Planet Report is published by WWF, with the Zoological Society of London compiling the Living Planet Index. "
  "Its 2024 edition reported an average decline of 73 per cent in monitored wildlife populations between 1970 and 2020. "
  "The IUCN publishes the Red List of Threatened Species.",
  "env-living-planet-report", "WWF, Living Planet Report 2024 (Living Planet Index compiled by the Zoological Society of London).")

# --- medium / Statement-I/II/III (1) ---
ar3(IC, "medium", "The Montreal Protocol is regarded as a climate treaty as well as an ozone treaty.",
  "Many of the ozone-depleting substances it phases out, such as CFCs, are also potent greenhouse gases.",
  "Its Kigali Amendment (2016) requires the phase-down of hydrofluorocarbons (HFCs), which do not deplete the ozone layer but are powerful greenhouse gases.",
  0,
  "Both Statement II and Statement III are correct and both explain Statement I. Phasing out CFCs and other ozone-depleting "
  "substances, most of which are strong greenhouse gases, has already avoided a large amount of warming. The Kigali "
  "Amendment extended the Protocol to HFCs, the CFC substitutes that are harmless to ozone but potent greenhouse gases; "
  "their phase-down is expected to avoid up to about 0.4 degrees Celsius of warming by 2100.",
  "env-montreal-kigali-climate", "UNEP Ozone Secretariat, Montreal Protocol on Substances that Deplete the Ozone Layer and its Kigali Amendment (2016).")

# ========================= INDIAN LAWS & BODIES (5) =========================

# --- medium / statement (2) ---
stmt_opts(IL, "medium", "Consider the following statements about the National Green Tribunal (NGT):",
  ["It can hear cases arising under the Wildlife (Protection) Act, 1972.",
   "It was set up under the National Green Tribunal Act, 2010.",
   "Its principal bench sits in New Delhi."],
  Y26, 2,
  "Statements 2 and 3 are correct. The NGT was set up in 2010 under its own Act, with its principal bench in New Delhi. "
  "Statement 1 is wrong: the NGT decides cases under the laws listed in Schedule I of the NGT Act -- among them the Water, "
  "Air, Environment (Protection), Forest (Conservation) and Biological Diversity Acts -- and the Wildlife (Protection) Act "
  "and the Indian Forest Act are not among them.",
  "env-ngt-jurisdiction", "National Green Tribunal Act, 2010, section 14 and Schedule I; National Green Tribunal, 'About us'.")
FALSE_AT["env-ngt-jurisdiction"] = 1

stmt_opts(IL, "medium", "Consider the following statements about the Biological Diversity Act, 2002:",
  ["The National Biodiversity Authority set up under it is headquartered in Chennai.",
   "It was enacted to give effect to India's obligations under the Ramsar Convention.",
   "Since its 2023 amendment, registered AYUSH practitioners need not give prior intimation to the State Biodiversity Board to use biological resources in practising indigenous medicine as a profession."],
  CLASSIC, 2,
  "Statements 1 and 3 are correct. The National Biodiversity Authority sits in Chennai, and the Biological Diversity "
  "(Amendment) Act, 2023 extended the old exemption for vaids and hakims to registered AYUSH practitioners who practise "
  "for sustenance and livelihood. Statement 2 is wrong: the Act gives effect to the Convention on Biological Diversity "
  "(CBD); the Ramsar Convention concerns wetlands.",
  "env-biodiversity-act-2023", "Biological Diversity Act, 2002; Biological Diversity (Amendment) Act, 2023 (No. 10 of 2023), section 7; National Biodiversity Authority.")
FALSE_AT["env-biodiversity-act-2023"] = 2

# --- easy / statement (1) ---
stmt(IL, "easy", "Consider the following statements about the National Tiger Conservation Authority (NTCA):",
  ["It is a statutory body constituted under the Wildlife (Protection) Act, 1972.",
   "It is chaired by the Prime Minister."],
  T2, 0,
  "Only statement 1 is correct. The NTCA was constituted in 2006 under section 38L of the Wildlife (Protection) Act, "
  "inserted by that year's amendment, taking over from Project Tiger. It is chaired by the Union Minister for "
  "Environment, Forest and Climate Change, not the Prime Minister.",
  "env-ntca-statutory", "Wildlife (Protection) Act, 1972, Chapter IVB (sections 38K-38X), inserted by the Wildlife (Protection) Amendment Act, 2006; NTCA, 'About us'.")
FALSE_AT["env-ntca-statutory"] = 2

# --- hard / statement (1) ---
stmt_opts(IL, "hard", "Consider the following statements about the Forest (Conservation) Amendment Act, 2023:",
  ["It renamed the Forest (Conservation) Act, 1980 as the Van (Sanrakshan Evam Samvardhan) Adhiniyam, 1980.",
   "It exempts forest land within 100 km of India's international borders, the Line of Control or the Line of Actual Control from the Act's approval requirement when the land is needed for strategic linear projects of national importance and concerning national security.",
   "It bars zoos and safaris from forest land outside protected areas."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. The amendment, in force from 1 December 2023, renamed the Act and created the "
  "border-area exemption for strategic linear projects. Statement 3 is the reverse of what it did: it added zoos and "
  "safaris (under the Wildlife (Protection) Act) owned by the Government or any authority in forest areas outside protected "
  "areas, together with eco-tourism facilities and silvicultural operations, to the activities that do not count as a "
  "non-forest purpose. (Separately, a February 2024 interim order of the Supreme Court requires its approval for any new "
  "zoo or safari on forest land.)",
  "env-forest-conservation-amendment-2023", "Forest (Conservation) Amendment Act, 2023 (No. 15 of 2023); PRS Legislative Research, The Forest (Conservation) Amendment Bill, 2023.")
FALSE_AT["env-forest-conservation-amendment-2023"] = 3

# --- medium / mcq (1) ---
mcq(IL, "medium", "Eco-Sensitive Zones around national parks and wildlife sanctuaries are notified by the Central Government under which of the following laws?",
  ["Wildlife (Protection) Act, 1972", "Forest (Conservation) Act, 1980", "Biological Diversity Act, 2002", "Environment (Protection) Act, 1986"], 3,
  "Eco-Sensitive Zones are notified by the Ministry of Environment, Forest and Climate Change under section 3 of the "
  "Environment (Protection) Act, 1986, read with rule 5 of the Environment (Protection) Rules, 1986, which let the Centre "
  "restrict industries and processes in an area. The Wildlife (Protection) Act governs the protected areas themselves, "
  "not the buffer around them.",
  "env-eco-sensitive-zones", "Environment (Protection) Act, 1986, section 3; Environment (Protection) Rules, 1986, rule 5; MoEFCC, Guidelines for Declaration of Eco-Sensitive Zones around National Parks and Wildlife Sanctuaries (2011).")

print("false statement at position:", FALSE_AT)
write_sql(os.path.dirname(os.path.abspath(__file__)), "environment_batch3_insert.sql")
