# -*- coding: utf-8 -*-
"""Environment & Ecology batch 2: every remaining cell for Fauna & Animal Behaviour (22) and
Flora, Fungi & Forests (12) -- the "Ecology & Biodiversity" Level-2 test -- from the live gap
report regenerated 2026-09-28 (config e6f68e99; bank = the 5 batch-1 rows).

Formats follow Environment's own 2023-26 mix: 'which of the statements' combinations (both the
classic '1 and 2 only' set and 2026's '1 only / 1 and 2 / 2 and 3 / 3 only' set, plus 2025's
Roman-numbered form), 'how many' counts and 2-statement rows. All five Statement-I/II rows here
use the two-statement form: the real 2023-24 evidence for that form is species biology
(2023-Q12 Marsupials, 2024-Q20 Indian Flying Fox); the 2025 three-statement variant appears only
in climate/pollution questions and is used in batches 3-5.

No topic repeats a 2023-26 PYQ (environment_ecology_qs_2023_2026.txt) or a 2015-22 one in the
same angle. The 2024 snow-leopard estimate (718, SPAI) and the 2017 bamboo amendment were
checked by web search on 2026-09-28; the rest are standard NCERT / IUCN / WPA facts.
"""
import os
import polity_common as pc
from polity_common import stmt, stmt_opts, mcq, ar, pairs, C3, C4, T2, write_sql

pc.SUBJECT = "Environment & Ecology"
FA = "Fauna & Animal Behaviour"
FL = "Flora, Fungi & Forests"

CLASSIC = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
Y26 = ["1 only", "1 and 2", "2 and 3", "3 only"]
ROMAN = ["I and II only", "II and III only", "I and III only", "I, II and III"]
NCERT_BIO12 = "NCERT Biology Class XII"
IUCN = "IUCN Red List of Threatened Species"
WPA = "Wildlife (Protection) Act, 1972 (as amended in 2022)"
FALSE_AT = {}

# ============================ FAUNA (22) ============================

# --- medium / statement (8) ---
stmt_opts(FA, "medium", "Consider the following statements about the olive ridley turtle:",
  ["It is known for 'arribada', a synchronised mass nesting in which thousands of females come ashore together.",
   "Gahirmatha, the mouth of the Rushikulya and the mouth of the Devi river in Odisha are among its main mass-nesting sites.",
   "It is listed in Schedule I of the Wildlife (Protection) Act, 1972."],
  CLASSIC, 3,
  "All three statements are correct. Olive ridleys nest en masse ('arribada'), and Odisha's Gahirmatha, Rushikulya and Devi "
  "river mouth are among the world's largest such rookeries. Like every sea turtle in Indian waters, the olive ridley is in "
  "Schedule I of the Wildlife (Protection) Act; it is listed as Vulnerable by the IUCN. It is one of the smallest sea turtles -- "
  "the leatherback is the largest.",
  "env-olive-ridley-arribada", f"{IUCN}, Lepidochelys olivacea; {WPA}, Schedule I; Odisha Forest Department, sea-turtle rookeries.")

stmt(FA, "medium", "Consider the following statements about the red panda:",
  ["It belongs to the same family as the giant panda.",
   "It is the State animal of Sikkim.",
   "Its diet consists mainly of bamboo leaves and shoots."],
  C3, 1,
  "Only statements 2 and 3 are correct. The red panda is Sikkim's State animal and feeds mostly on bamboo. Statement 1 is the "
  "trap: despite the shared name and diet, the red panda is the only living member of its own family, Ailuridae, while the "
  "giant panda is a bear (Ursidae). It is listed as Endangered by the IUCN.",
  "env-red-panda", f"{IUCN}, Ailurus fulgens; Government of Sikkim, State symbols.")
FALSE_AT["env-red-panda"] = 1

stmt(FA, "medium", "Consider the following statements about the Great Indian Bustard:",
  ["It is listed as Critically Endangered on the IUCN Red List.",
   "Collision with overhead power lines is a major cause of death of the Great Indian Bustard in the Thar."],
  T2, 2,
  "Both statements are correct. The Great Indian Bustard is Critically Endangered, with most of the surviving birds in "
  "Rajasthan's Thar. Because it has poor frontal vision and flies low and heavily, it frequently collides with overhead power "
  "lines; Wildlife Institute of India studies identified these collisions as a leading cause of adult deaths, which is why "
  "undergrounding of lines in its habitat has been ordered.",
  "env-great-indian-bustard-powerlines", f"{IUCN}, Ardeotis nigriceps; Wildlife Institute of India, power-line mortality assessment in the Thar.")

stmt_opts(FA, "medium", "Consider the following statements:",
  ["Aestivation is a state of dormancy that some animals enter to survive hot, dry periods.",
   "Hibernation is seen only in mammals; no reptile or amphibian hibernates.",
   "The African lungfish survives the drying of its pool by aestivating inside a mucus cocoon in the mud."],
  CLASSIC, 2,
  "Statements 1 and 3 are correct. Aestivation is summer dormancy in response to heat and drought; the African lungfish is the "
  "classic example, sealing itself in a mucus cocoon when its pool dries up. Statement 2 is wrong: many reptiles and amphibians "
  "(frogs, turtles, snakes) pass the winter in a dormant state, so hibernation is not confined to mammals.",
  "env-aestivation-hibernation", f"{NCERT_BIO12}, ch. 13 'Organisms and Populations' (responses to abiotic factors).")
FALSE_AT["env-aestivation-hibernation"] = 2

stmt(FA, "medium", "Consider the following statements about horseshoe crabs:",
  ["They are more closely related to spiders and scorpions than to true crabs.",
   "Their blood is red because it carries oxygen with haemoglobin.",
   "An extract of their blood is used to test vaccines and medical devices for bacterial endotoxins.",
   "In India they are found only around the Andaman and Nicobar Islands."],
  C4, 1,
  "Only statements 1 and 3 are correct. Horseshoe crabs are chelicerates, grouped with spiders and scorpions. Their blood is "
  "blue, not red: oxygen is carried by the copper-based protein haemocyanin. Amoebocyte lysate made from their blood is the "
  "standard test for bacterial endotoxins in injectable drugs and devices. In India they occur along the east coast, notably "
  "Odisha (Balasore) and West Bengal, not only in the Andaman and Nicobar Islands.",
  "env-horseshoe-crab", "Zoological Survey of India, horseshoe crabs of India; US FDA guidance on bacterial endotoxins testing (LAL).")
FALSE_AT["env-horseshoe-crab"] = 2

stmt_opts(FA, "medium", "Consider the following statements about the sloth bear:",
  ["It feeds largely on termites and ants, which it sucks up through a gap left by missing upper front teeth.",
   "It is found only in India.",
   "Mothers carry their cubs on their backs."],
  ["1 only", "1 and 3", "2 and 3", "3 only"], 1,
  "Statements 1 and 3 are correct. The sloth bear is a specialist insect-eater: it lacks the upper incisors and uses the gap "
  "and its mobile lips to suck termites and ants from their mounds. Mothers carry cubs on their backs. Statement 2 is wrong -- "
  "the species also lives in Sri Lanka and Nepal. It is listed as Vulnerable by the IUCN.",
  "env-sloth-bear", f"{IUCN}, Melursus ursinus.")
FALSE_AT["env-sloth-bear"] = 2

stmt(FA, "medium", "Consider the following statements about seahorses:",
  ["The male carries the fertilised eggs in a brood pouch until they hatch.",
   "Seahorses are fish.",
   "All seahorse species are listed in Appendix II of CITES."],
  C3, 2,
  "All three statements are correct. In seahorses the female deposits eggs in the male's brood pouch, where they are "
  "fertilised and carried until the young emerge. Seahorses are bony fish of the family Syngnathidae (with pipefishes). Since "
  "2004 the whole genus Hippocampus has been listed in CITES Appendix II, because of heavy trade for traditional medicine and "
  "aquariums.",
  "env-seahorse-male-pregnancy", "CITES Appendices (Hippocampus spp., Appendix II); Zoological Survey of India, syngnathid fishes.")

stmt_opts(FA, "medium", "Consider the following statements about the snow leopard:",
  ["It is listed as Vulnerable on the IUCN Red List.",
   "In India its range covers the high Himalaya of Ladakh, Jammu & Kashmir, Himachal Pradesh, Uttarakhand, Sikkim and Arunachal Pradesh.",
   "India's first Snow Leopard Population Assessment, released in 2024, estimated fewer than 200 snow leopards in the country."],
  ROMAN, 0,
  "Statements I and II are correct. The snow leopard was moved from Endangered to Vulnerable by the IUCN in 2017. India's "
  "range runs across the high Himalaya, from Ladakh to Arunachal Pradesh. Statement III is wrong: the Snow Leopard Population "
  "Assessment in India (SPAI), released in January 2024, estimated 718 snow leopards, more than half of them (477) in Ladakh.",
  "env-snow-leopard-spai", f"{IUCN}, Panthera uncia; MoEFCC / Wildlife Institute of India, Status of Snow Leopards in India (SPAI), January 2024.",
  roman=True)
FALSE_AT["env-snow-leopard-spai"] = 3

# --- easy / statement (3) ---
stmt(FA, "easy", "Consider the following statements about vultures in India:",
  ["Vultures are scavengers that feed mainly on carcasses.",
   "The collapse of India's Gyps vulture populations was caused mainly by DDT residues in carcasses.",
   "Veterinary use of diclofenac is still permitted in India."],
  C3, 0,
  "Only statement 1 is correct. The crash of India's Gyps vultures from the 1990s was traced to diclofenac, a painkiller given "
  "to cattle: vultures feeding on treated carcasses suffered kidney failure. DDT was not the cause. India banned veterinary use "
  "of diclofenac in 2006, so statement 3 is also wrong.",
  "env-vultures-diclofenac", "Ministry of Health and Family Welfare, ban on veterinary diclofenac (2006); MoEFCC, Action Plan for Vulture Conservation in India 2020-25.")
FALSE_AT["env-vultures-diclofenac"] = 2

stmt(FA, "easy", "Consider the following statements about echolocation:",
  ["Bats and dolphins use echolocation to locate their prey.",
   "Echolocation is used only by nocturnal animals."],
  T2, 0,
  "Only statement 1 is correct. Echolocating animals emit sounds and interpret the returning echoes; bats and toothed whales "
  "such as dolphins are the best-known examples. It is not limited to night-active animals -- dolphins hunt by echolocation by "
  "day as well, in murky water.",
  "env-echolocation", f"{NCERT_BIO12}, ch. 13 'Organisms and Populations'.")
FALSE_AT["env-echolocation"] = 2

stmt_opts(FA, "easy", "Consider the following statements about the blackbuck:",
  ["It is an antelope of open grasslands and scrub.",
   "It is the State animal of Punjab.",
   "The Bishnoi community is known for protecting it."],
  CLASSIC, 3,
  "All three statements are correct. The blackbuck is an antelope of open plains and grassland. It is the State animal of "
  "Punjab (as well as of Haryana and Andhra Pradesh). The Bishnoi community of Rajasthan is known for protecting blackbuck and "
  "chinkara. It is in Schedule I of the Wildlife (Protection) Act.",
  "env-blackbuck", f"{IUCN}, Antilope cervicapra; {WPA}, Schedule I.")

# --- hard / statement (3) ---
stmt(FA, "hard", "Consider the following statements about birds of India:",
  ["The Forest Owlet, once thought extinct, was rediscovered in 1997 in the forests of Maharashtra.",
   "Jerdon's Courser was rediscovered in 1986 in Andhra Pradesh.",
   "The Pink-headed Duck has not been reliably recorded in the wild since the late 1940s.",
   "The Great Indian Bustard is the State bird of Rajasthan."],
  C4, 3,
  "All four statements are correct. The Forest Owlet was rediscovered in 1997 near Shahada in Maharashtra, over a century after "
  "the last specimen. Jerdon's Courser was rediscovered in 1986 in the Lankamalleswara area of Andhra Pradesh. The Pink-headed "
  "Duck has had no confirmed record since 1949 and may be extinct. The Great Indian Bustard (godawan) is Rajasthan's State "
  "bird. The difficulty is that each fact sounds improbable, so candidates tend to under-count.",
  "env-rediscovered-birds", "BirdLife International species factsheets (Heteroglaux blewitti, Rhinoptilus bitorquatus, Rhodonessa caryophyllacea); Government of Rajasthan, State symbols.")

stmt_opts(FA, "hard", "Consider the following statements about fish migration:",
  ["Hilsa is an anadromous fish: it lives in the sea and moves up rivers to spawn.",
   "Freshwater eels are catadromous: they live in rivers and migrate to the sea to spawn.",
   "Salmon are catadromous fish."],
  ["I and III only", "I and II only", "II and III only", "I, II and III"], 1,
  "Statements I and II are correct. Anadromous fish (hilsa, salmon) grow in the sea and migrate into rivers to breed; "
  "catadromous fish (freshwater eels) do the reverse. Statement III therefore gets salmon backwards -- salmon are the textbook "
  "anadromous fish.",
  "env-anadromous-catadromous", "ICAR-Central Inland Fisheries Research Institute, hilsa biology; FAO fisheries glossary (anadromous, catadromous).",
  roman=True)
FALSE_AT["env-anadromous-catadromous"] = 3

stmt(FA, "hard", "Consider the following statements about the king cobra:",
  ["It belongs to the same genus as the Indian spectacled cobra.",
   "It is the only snake known to build a nest for its eggs.",
   "It feeds mainly on other snakes."],
  C3, 1,
  "Only statements 2 and 3 are correct. The female king cobra gathers leaf litter into a nest and guards it, which no other "
  "snake is known to do; its diet is chiefly other snakes, hence its genus name Ophiophagus ('snake-eater'). That also makes "
  "statement 1 wrong: the spectacled cobra is Naja naja, a different genus. The king cobra is listed as Vulnerable.",
  "env-king-cobra", f"{IUCN}, Ophiophagus hannah.")
FALSE_AT["env-king-cobra"] = 1

# --- MCQ (4) ---
mcq(FA, "medium", "The wool of which animal, protected in India, is used to make 'shahtoosh' shawls?",
  ["Himalayan tahr", "Bharal", "Markhor", "Tibetan antelope (chiru)"], 3,
  "Shahtoosh is woven from the fine underwool of the Tibetan antelope, or chiru, which must be killed to obtain it. The chiru "
  "lives on the Tibetan plateau and in Ladakh's Changthang; it is in Schedule I of the Wildlife (Protection) Act and in CITES "
  "Appendix I, and trade in shahtoosh is banned.",
  "env-chiru-shahtoosh", f"{WPA}, Schedule I; CITES Appendix I (Pantholops hodgsonii).")

mcq(FA, "medium", "Which one of the following birds lays its eggs in the nests of crows and leaves the crows to raise its young?",
  ["Asian koel", "House sparrow", "Indian robin", "Common myna"], 0,
  "The Asian koel is a brood parasite: the female lays her eggs in crows' nests and the crows rear the chicks. Brood "
  "parasitism is an interaction in which one species exploits another's parental care.",
  "env-koel-brood-parasite", f"{NCERT_BIO12}, ch. 13 'Organisms and Populations' (population interactions: brood parasitism).")

mcq(FA, "easy", "Which animal was declared India's 'National Heritage Animal' in 2010?",
  ["Tiger", "Elephant", "Asiatic lion", "Gaur"], 1,
  "The Indian elephant was declared the National Heritage Animal in 2010, on the recommendation of the Elephant Task Force. The "
  "tiger remains the national animal.",
  "env-elephant-heritage-animal", "MoEFCC, notification declaring the elephant the National Heritage Animal (2010); Elephant Task Force report 'Gajah' (2010).")

mcq(FA, "hard", "The Hangul (Kashmir stag), the State animal of Jammu and Kashmir, survives mainly in which protected area?",
  ["Hemis National Park", "Great Himalayan National Park", "Dachigam National Park", "Valley of Flowers National Park"], 2,
  "The last viable Hangul population is centred on Dachigam National Park near Srinagar. Hemis is in Ladakh (snow leopard "
  "country), the Great Himalayan NP in Himachal Pradesh and the Valley of Flowers in Uttarakhand.",
  "env-hangul-dachigam", "Department of Wildlife Protection, Jammu & Kashmir, Dachigam National Park; Wildlife Institute of India, Hangul conservation.")

# --- Statement-I/II (3, two-statement form) ---
ar(FA, "easy", "Camels can survive long periods without drinking water.",
  "Camels store water in their humps.", 2,
  "Statement-I is correct: camels tolerate long periods without drinking, thanks to efficient kidneys, very dry dung and "
  "tolerance of dehydration. Statement-II is the popular misconception: the hump stores fat, not water.",
  "env-camel-hump-fat", f"{NCERT_BIO12}, ch. 13 'Organisms and Populations' (adaptations to desert conditions).")

ar(FA, "medium", "Arctic foxes have short ears and a short muzzle.",
  "Arctic foxes change the colour of their coat with the seasons.", 1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Short ears and muzzle cut heat loss in the cold "
  "(Allen's rule: mammals of cold climates have shorter extremities). The seasonal coat change -- white in winter, brown or grey "
  "in summer -- is camouflage, a separate adaptation.",
  "env-arctic-fox-allens-rule", f"{NCERT_BIO12}, ch. 13 'Organisms and Populations' (Allen's rule).")

ar(FA, "hard", "Bar-headed geese can fly over the Himalaya during their migration.",
  "The haemoglobin of bar-headed geese has a higher affinity for oxygen than that of lowland geese, helping them take up oxygen in thin air.", 0,
  "Both statements are correct and Statement-II explains Statement-I. Bar-headed geese cross the Himalaya between Central Asia "
  "and India. Their haemoglobin binds oxygen more strongly, which lets them load enough oxygen at altitudes where the air is "
  "very thin.",
  "env-bar-headed-goose", "Scott, G. R. et al. (2015), 'How bar-headed geese fly over the Himalayas', Physiology 30(2).")

# --- match (1) ---
pairs(FA, "medium", "Consider the following pairs of animals and the States of which they are the State animal:",
  ["Mithun", "Clouded leopard", "Snow leopard", "Red panda"],
  ["Arunachal Pradesh", "Meghalaya", "Himachal Pradesh", "Kerala"], 2,
  "Only three pairs are correct. The mithun is the State animal of Arunachal Pradesh (and Nagaland), the clouded leopard of "
  "Meghalaya, and the snow leopard of Himachal Pradesh. The red panda is Sikkim's State animal; Kerala's is the Indian elephant.",
  "env-state-animals-pairs", "State governments' notified State symbols (Arunachal Pradesh, Meghalaya, Himachal Pradesh, Sikkim, Kerala).")

# ============================ FLORA (12) ============================

stmt(FL, "medium", "Consider the following statements about Neelakurinji (Strobilanthes kunthiana):",
  ["It flowers once in about twelve years.",
   "It grows in the shola-grassland landscape of the southern Western Ghats, notably around Munnar.",
   "The plants die after flowering."],
  C3, 2,
  "All three statements are correct. Neelakurinji blooms en masse roughly every twelve years (the last mass bloom around Munnar "
  "was in 2018), carpeting the montane grasslands blue. Like many Strobilanthes, it is monocarpic: the plants die after "
  "flowering and seeding, and the next generation grows from seed.",
  "env-neelakurinji", "Kerala Forest Department, Kurinjimala Sanctuary; Botanical Survey of India, Strobilanthes of the Western Ghats.")

stmt_opts(FL, "medium", "Consider the following statements about insectivorous plants:",
  ["They usually grow in soils poor in nitrogen.",
   "The pitcher plant Nepenthes khasiana is endemic to Meghalaya.",
   "They cannot photosynthesise and depend wholly on insects for food."],
  Y26, 1,
  "Statements 1 and 2 are correct. Insectivorous plants grow in nitrogen-poor soils and bogs and trap insects to make up the "
  "shortfall in nitrogen. India's only native pitcher plant, Nepenthes khasiana, is endemic to Meghalaya. Statement 3 is wrong: "
  "they are green and photosynthesise; insects supply nutrients, not their main food.",
  "env-insectivorous-plants", "Botanical Survey of India, Nepenthes khasiana; NCERT Science Class VII, ch. 1 'Nutrition in Plants'.")
FALSE_AT["env-insectivorous-plants"] = 3

stmt(FL, "medium", "Consider the following statements:",
  ["Orchids growing on tree branches are parasites that draw their food from the host tree.",
   "Cuscuta (dodder) is a parasitic plant that lacks chlorophyll and takes its food from the host plant."],
  T2, 1,
  "Only statement 2 is correct. Most tree-dwelling orchids are epiphytes: they use the tree only for support and make their "
  "own food, taking moisture from the air. Cuscuta, by contrast, has no chlorophyll and draws its food from the host through "
  "suckers (haustoria). Confusing epiphytes with parasites is the planted trap.",
  "env-epiphyte-vs-parasite", "NCERT Science Class VII, ch. 1 'Nutrition in Plants'; NCERT Biology Class XI, ch. 'Morphology of Flowering Plants'.")
FALSE_AT["env-epiphyte-vs-parasite"] = 1

stmt(FL, "medium", "Consider the following statements about bamboo:",
  ["Bamboo is a grass.",
   "Some bamboo species flower gregariously at long intervals and then die.",
   "The 'mautam' in Mizoram is linked to bamboo flowering, which triggers a boom in the rat population.",
   "Bamboo grown outside forest areas is still treated as a 'tree' under the Indian Forest Act, 1927, so a permit is needed to fell and transport it."],
  C4, 2,
  "Only statements 1, 2 and 3 are correct. Bamboo belongs to the grass family (Poaceae). Many species flower together after "
  "decades and then die; Mizoram's 'mautam' follows the roughly 48-year flowering of Melocanna baccifera, whose seeds fuel a rat "
  "explosion and famine. Statement 4 is wrong: the Indian Forest (Amendment) Ordinance of November 2017, later enacted, removed "
  "bamboo grown on non-forest land from the Act's definition of 'tree', so it can be felled and moved without a permit.",
  "env-bamboo-mautam", "PIB, Indian Forest (Amendment) Ordinance, 2017 (23 November 2017); National Bamboo Mission.")
FALSE_AT["env-bamboo-mautam"] = 4

stmt_opts(FL, "easy", "Consider the following statements about plants of dry regions:",
  ["Cacti store water in their fleshy stems.",
   "In many cacti the leaves are reduced to spines, which cuts water loss.",
   "Such plants usually have large, thin leaves with many open stomata to speed up transpiration."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. Xerophytes save water: succulent stems store it, leaves are reduced to spines, and cuticles "
  "are thick. Statement 3 describes the opposite -- large, thin leaves with many open stomata would lose water quickly.",
  "env-xerophyte-adaptations", f"{NCERT_BIO12}, ch. 13 'Organisms and Populations' (adaptations of plants to deserts).")
FALSE_AT["env-xerophyte-adaptations"] = 3

stmt(FL, "easy", "Consider the following statements about the Khejri tree (Prosopis cineraria):",
  ["It is the State tree of Gujarat.",
   "It was introduced into the Thar Desert from Mexico.",
   "The Bishnoi sacrifice at Khejarli in 1730 was made to protect sal trees."],
  C3, 3,
  "None of the statements is correct. Khejri is the State tree of Rajasthan (Gujarat's is the banyan). It is native to the "
  "Thar -- the species introduced from the Americas is a different Prosopis, P. juliflora. The 1730 Khejarli sacrifice, in which "
  "Amrita Devi and more than 360 Bishnois gave their lives, was to protect Khejri trees.",
  "env-khejri", "Government of Rajasthan, State symbols; Rajasthan Forest Department, Khejri and the Khejarli sacrifice.")

stmt(FL, "hard", "Consider the following statements about invasive plants in India:",
  ["Lantana camara was introduced into India as an ornamental plant.",
   "Prosopis juliflora, native to Central and South America, was introduced into India.",
   "Parthenium hysterophorus, native to tropical America, is believed to have entered India with imported food grain.",
   "Water hyacinth (Eichhornia crassipes) is native to South America."],
  C4, 3,
  "All four statements are correct. Lantana arrived as a garden ornamental in the early 19th century; Prosopis juliflora was "
  "introduced from the Americas for fuelwood and to check desert spread; Parthenium ('congress grass') is thought to have come "
  "with imported wheat in the 1950s; water hyacinth, an Amazonian plant, was brought in as an ornamental. All four are now "
  "among India's most damaging invasive plants.",
  "env-invasive-plants", "Botanical Survey of India, Invasive Alien Flora of India; ICAR-Directorate of Weed Research, Parthenium.",
  roman=True)

stmt_opts(FL, "hard", "Consider the following statements:",
  ["The sandalwood tree is a partial root parasite that draws water and minerals from the roots of other plants.",
   "Cycas is a flowering plant (angiosperm).",
   "The coralloid roots of Cycas harbour nitrogen-fixing cyanobacteria."],
  CLASSIC, 2,
  "Statements 1 and 3 are correct. Sandalwood (Santalum album) is a hemiparasite: it is green, but its roots tap the roots of "
  "host plants. Cycas is a gymnosperm with naked seeds, not a flowering plant; its coralloid roots host nitrogen-fixing "
  "cyanobacteria.",
  "env-sandalwood-cycas", "NCERT Biology Class XI, ch. 'Plant Kingdom' (gymnosperms: Cycas); Institute of Wood Science and Technology, sandalwood.")
FALSE_AT["env-sandalwood-cycas"] = 2

mcq(FL, "medium", "Which one of the following is a flowering plant that grows fully submerged in shallow seas?",
  ["Seagrass", "Kelp", "Sargassum", "Red algae"], 0,
  "Seagrasses are flowering plants (angiosperms) that live fully submerged in shallow coastal waters -- the meadows of the Gulf "
  "of Mannar and Palk Bay that dugongs graze. Kelp, Sargassum and red algae are algae, not flowering plants.",
  "env-seagrass-angiosperm", "Zoological Survey of India / Botanical Survey of India, seagrasses of the Gulf of Mannar; NCERT Biology Class XI, ch. 'Plant Kingdom'.")

mcq(FL, "easy", "Which one of the following is a gymnosperm?",
  ["Mango", "Neem", "Banyan", "Pine"], 3,
  "Pine is a gymnosperm: its seeds are borne naked on cone scales, not enclosed in a fruit. Mango, neem and banyan are "
  "flowering plants (angiosperms).",
  "env-pine-gymnosperm", "NCERT Biology Class XI, ch. 'Plant Kingdom'.")

ar(FL, "easy", "Lichens are often the first organisms to colonise bare rock.",
  "Lichens secrete acids that help break the rock down into the beginnings of soil.", 0,
  "Both statements are correct and Statement-II explains Statement-I. As pioneer species in primary succession on rock, lichens "
  "secrete acids that dissolve the rock and start soil formation, preparing the ground for mosses and later plants.",
  "env-lichen-pioneer", f"{NCERT_BIO12}, ch. 14 'Ecosystem' (ecological succession).")

ar(FL, "medium", "The Venus flytrap is native to the forests of India.",
  "The Venus flytrap is an insectivorous plant.", 3,
  "Statement-I is incorrect but Statement-II is correct. The Venus flytrap (Dionaea muscipula) is native only to a small area "
  "of the coastal Carolinas in the United States. It is insectivorous, closing its leaves on insects. India's native "
  "insectivorous plants include Nepenthes, Drosera and Utricularia.",
  "env-venus-flytrap", "US Fish and Wildlife Service, Dionaea muscipula; Botanical Survey of India, insectivorous plants of India.")

print("false statement at position:", FALSE_AT)
write_sql(os.path.dirname(os.path.abspath(__file__)), "environment_batch2_insert.sql")
