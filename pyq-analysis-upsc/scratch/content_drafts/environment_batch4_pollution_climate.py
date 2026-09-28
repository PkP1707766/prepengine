# -*- coding: utf-8 -*-
"""Environment & Ecology batch 4: every remaining cell for Pollution, Waste & Resources (18) and
Climate Science & Mitigation (15), from the live gap report regenerated 2026-09-28 after batch 3
(bank 61 rows, 59 to draft).

Three of the 2026-09-27 Statement-I/II allocation's three-statement slots fall here (Climate
Science 2, Pollution 1). The direct PYQ precedent is 2025-Q31 (cement emissions), whose angle is
not reused. Their keys are spread across the 2025 ladder: (b) and (d) for Climate Science and
(c) for Pollution -- batch 3's Montreal/Kigali row took (a).

No row repeats a 2015-26 PYQ angle for these sub-topics (environment_subtopic_retag.csv) or a
batch-1 row: env-ground-level-ozone already uses 'NAAQS cover twelve pollutants', and
env-gwp-methane-n2o covers methane's lifetime, so neither fact is used again. Checked by web
search on 2026-09-28: the E-Waste (Management) Rules, 2022 (in force 1 April 2023) cover solar
PV modules in Chapter V; the Solid Waste Management Rules, 2026 replaced the 2016 Rules from
1 April 2026 with four-stream segregation (wet, dry, sanitary, special care). Chapters that the
2023 NCERT rationalisation dropped ('Environmental Issues', 'Environmental Chemistry') are cited
with the edition.
"""
import os
import polity_common as pc
from polity_common import stmt, stmt_opts, mcq, ar3, pairs, C3, C4, T2, write_sql

pc.SUBJECT = "Environment & Ecology"
PW = "Pollution, Waste & Resources"
CS = "Climate Science & Mitigation"

CLASSIC = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
ENV_ISSUES = "NCERT Biology Class XII (pre-2023 edition), ch. 'Environmental Issues'"
ENV_CHEM = "NCERT Chemistry Class XI (pre-2023 edition), ch. 'Environmental Chemistry'"
AR6 = "IPCC Sixth Assessment Report (AR6)"
FALSE_AT = {}

# ============================ POLLUTION, WASTE & RESOURCES (18) ============================

# --- medium / statement (7) ---
stmt(PW, "medium", "Consider the following statements about eutrophication:",
  ["Algal blooms caused by eutrophication raise the dissolved oxygen of the water at night.",
   "It is the enrichment of a water body with nutrients, chiefly nitrates and phosphates.",
   "Accelerated (cultural) eutrophication is caused by human activities such as the discharge of sewage and the run-off of fertilisers."],
  C3, 1,
  "Only statements 2 and 3 are correct. Nutrient enrichment, much of it from sewage and farm run-off, fuels algal blooms. "
  "Statement 1 is wrong: at night the algae only respire, and when the bloom dies its decomposition by bacteria uses up "
  "dissolved oxygen, which is why eutrophic lakes suffer fish kills.",
  "env-eutrophication", f"{ENV_ISSUES} (eutrophication).")
FALSE_AT["env-eutrophication"] = 1

stmt_opts(PW, "medium", "Consider the following statements:",
  ["Biomagnification is the increase in the concentration of a toxic substance at successive trophic levels.",
   "Substances that are persistent and fat-soluble, such as DDT and methylmercury, are prone to biomagnification.",
   "Substances that are water-soluble and quickly excreted biomagnify the most."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. A toxicant that an organism cannot break down or excrete accumulates in its fatty "
  "tissue, and each predator eats many contaminated prey, so the concentration rises up the food chain -- the classic case "
  "is DDT thinning the eggshells of fish-eating birds. Statement 3 is the reverse: water-soluble substances that the body "
  "excretes readily do not build up.",
  "env-biomagnification", f"{ENV_ISSUES} (biomagnification).")
FALSE_AT["env-biomagnification"] = 3

stmt(PW, "medium", "Consider the following statements about the E-Waste (Management) Rules, 2022:",
  ["They came into force on 1 April 2023.",
   "They make producers responsible, through Extended Producer Responsibility, for getting a set share of their e-waste recycled.",
   "They cover solar photovoltaic modules, panels and cells.",
   "They cover only computers and mobile phones."],
  C4, 2,
  "Only statements 1, 2 and 3 are correct. The Rules replaced those of 2016 from 1 April 2023 and set annual recycling "
  "targets for producers, met by buying EPR certificates from registered recyclers. Chapter V deals with solar PV "
  "modules, panels and cells. Statement 4 is wrong: the Rules list a wide range of electrical and electronic equipment in "
  "their schedule, from IT and telecom equipment to consumer electricals and medical devices.",
  "env-ewaste-rules-2022", "E-Waste (Management) Rules, 2022 (MoEFCC, in force 1 April 2023); CPCB, FAQs on the E-Waste (Management) Rules, 2022.")
FALSE_AT["env-ewaste-rules-2022"] = 4

stmt_opts(PW, "medium", "Consider the following statements about the Noise Pollution (Regulation and Control) Rules, 2000:",
  ["An area of at least 100 metres around hospitals, educational institutions and courts can be declared a silence zone.",
   "The daytime limit in residential areas is 55 dB(A).",
   "For the purposes of the Rules, night time is from 10 p.m. to 6 a.m."],
  CLASSIC, 3,
  "All three statements are correct. The Schedule to the Rules sets ambient limits of 55 dB(A) by day and 45 dB(A) by "
  "night in residential areas, and 50 and 40 dB(A) in silence zones of at least 100 metres around hospitals, "
  "educational institutions and courts. Day time is 6 a.m. to 10 p.m. Noise is also covered by the Air (Prevention and "
  "Control of Pollution) Act, whose definition of 'air pollutant' was widened to include noise in 1987.",
  "env-noise-rules-2000", "Noise Pollution (Regulation and Control) Rules, 2000, Schedule; Air (Prevention and Control of Pollution) Act, 1981, section 2(a) (as amended in 1987).")

stmt_opts(PW, "medium", "Consider the following statements about devices used to control air pollution:",
  ["An electrostatic precipitator can remove over 99 per cent of the particulate matter in the exhaust of a thermal power plant.",
   "A wet scrubber can remove gases such as sulphur dioxide.",
   "Vehicles fitted with catalytic converters should use leaded petrol, because lead helps the catalyst work."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. Electrostatic precipitators charge dust particles and collect them on plates, removing "
  "over 99 per cent of particulates; scrubbers spray water or lime to remove gases like SO2. Statement 3 is the reverse: "
  "lead inactivates the platinum-palladium-rhodium catalyst, which is why vehicles with catalytic converters must use "
  "unleaded petrol.",
  "env-air-pollution-control-devices", f"{ENV_ISSUES} (air pollution and its control).")
FALSE_AT["env-air-pollution-control-devices"] = 3

stmt(PW, "medium", "Consider the following statements about Bharat Stage VI (BS-VI) emission norms:",
  ["They apply only to diesel vehicles.",
   "India moved to them directly from BS-IV, skipping BS-V, from 1 April 2020.",
   "BS-VI fuel has a maximum sulphur content of 10 parts per million."],
  C3, 1,
  "Only statements 2 and 3 are correct. India leapfrogged BS-V and required BS-VI vehicles and fuel nationwide from "
  "1 April 2020; BS-VI fuel carries at most 10 ppm of sulphur, against 50 ppm for BS-IV. Statement 1 is wrong: the norms "
  "cover petrol and diesel vehicles alike, though the cut in particulate and NOx limits is steepest for diesel.",
  "env-bs-vi-norms", "Ministry of Road Transport and Highways, Central Motor Vehicles Rules (BS-VI notification); Ministry of Petroleum and Natural Gas, BS-VI fuel supply from 1 April 2020.")
FALSE_AT["env-bs-vi-norms"] = 1

stmt(PW, "medium", "Consider the following statements about the Solid Waste Management Rules, 2026:",
  ["They replaced the Solid Waste Management Rules, 2016, with effect from 1 April 2026.",
   "They require waste to be segregated at source into four streams: wet, dry, sanitary and special-care waste.",
   "They allow unsegregated mixed waste to be sent to landfills without any additional charge."],
  C3, 1,
  "Only statements 1 and 2 are correct. The 2026 Rules, notified by the Environment Ministry under the Environment "
  "(Protection) Act, replaced the 2016 Rules' three-way segregation with four streams: wet, dry, sanitary (such as "
  "diapers) and special-care (such as bulbs, batteries and medicines). Statement 3 is wrong: landfills are meant only for "
  "non-recyclable, inert waste, and unsegregated waste attracts higher charges.",
  "env-swm-rules-2026", "MoEFCC, Solid Waste Management Rules, 2026 (in force 1 April 2026); PIB, 'New Solid Waste Management Rules Notified' (2026).")
FALSE_AT["env-swm-rules-2026"] = 3

# --- easy / statement (3) ---
stmt(PW, "easy", "Consider the following statements about carbon monoxide:",
  ["It binds to haemoglobin far more strongly than oxygen does.",
   "It has a strong, pungent smell, which makes leaks easy to detect."],
  T2, 0,
  "Only statement 1 is correct. Carbon monoxide binds haemoglobin roughly 200 times more tightly than oxygen, forming "
  "carboxyhaemoglobin and starving the tissues of oxygen. Statement 2 is wrong, and dangerously so: CO is colourless and "
  "odourless, which is why it is called a 'silent killer'.",
  "env-carbon-monoxide", f"{ENV_CHEM} (carbon monoxide); WHO, Guidelines for Indoor Air Quality: Selected Pollutants (2010).")
FALSE_AT["env-carbon-monoxide"] = 2

stmt(PW, "easy", "Consider the following statements about indoor air pollution:",
  ["Radon, a radioactive gas released from soil and rocks, can build up inside poorly ventilated buildings.",
   "Burning firewood, dung cakes and crop residue in traditional stoves is a major source of indoor air pollution in rural India."],
  T2, 2,
  "Both statements are correct. Radon seeps from uranium-bearing soil and rock and collects indoors; it is a leading cause "
  "of lung cancer after smoking. Smoke from solid fuels in poorly ventilated kitchens exposes women and children to high "
  "levels of particulate matter and carbon monoxide.",
  "env-indoor-air-pollution", "WHO, Household air pollution fact sheet; WHO, Radon fact sheet.")

stmt_opts(PW, "easy", "Consider the following statements about thermal pollution:",
  ["Hot water discharged from power plants lowers the dissolved oxygen of the river or sea it enters.",
   "Warm water can hold more dissolved oxygen than cold water.",
   "It can harm aquatic organisms adapted to a narrow range of temperature."],
  CLASSIC, 2,
  "Statements 1 and 3 are correct. Heated cooling water from power plants raises the temperature of the receiving water, "
  "which lowers its dissolved oxygen and stresses organisms adapted to narrow temperature ranges. Statement 2 is the "
  "reverse: the solubility of oxygen falls as water warms.",
  "env-thermal-pollution", f"{ENV_ISSUES} (water pollution).")
FALSE_AT["env-thermal-pollution"] = 2

# --- hard / statement (2) ---
stmt(PW, "hard", "Consider the following statements about India's National Ambient Air Quality Standards (NAAQS):",
  ["The annual average standard for PM2.5 is 40 micrograms per cubic metre.",
   "They were notified for the first time in 2009.",
   "Lead, arsenic and nickel are among the pollutants they cover.",
   "They prescribe separate, stricter limits for ecologically sensitive areas for every pollutant."],
  C4, 1,
  "Only statements 1 and 3 are correct. The 2009 standards set PM2.5 at 40 (annual) and 60 (24-hour) micrograms per cubic "
  "metre and include lead, arsenic, nickel, benzene, benzo(a)pyrene and ammonia. Statement 2 is wrong: the NAAQS were "
  "first notified by the CPCB in 1982 and revised in 1994 before the 2009 revision. Statement 4 is wrong: the 2009 "
  "standards set separate limits for ecologically sensitive areas only for sulphur dioxide and nitrogen dioxide.",
  "env-naaqs-2009", "CPCB, National Ambient Air Quality Standards (notification of 18 November 2009).")
FALSE_AT["env-naaqs-2009"] = "2,4"

stmt(PW, "hard", "Consider the following statements about radioactive pollutants:",
  ["Strontium-90 tends to accumulate in bones, because the body treats it like calcium.",
   "Iodine-131 concentrates in the thyroid gland.",
   "Caesium-137 spreads through the body's soft tissues and muscles.",
   "Radon-222 is formed in the decay chain of uranium-238."],
  C4, 3,
  "All four statements are correct. Strontium behaves chemically like calcium and is laid down in bone; iodine-131 is "
  "taken up by the thyroid, which is why potassium iodide tablets are issued after reactor accidents; caesium behaves "
  "like potassium and spreads through soft tissue. Radon-222 comes from the decay of radium-226 in the uranium-238 series.",
  "env-radioactive-pollutants", "WHO, Ionizing radiation and health effects; US EPA, Radionuclide Basics (strontium-90, iodine-131, caesium-137, radon).")

# --- medium / mcq (2) ---
mcq(PW, "medium", "Which one of the following is a secondary air pollutant, formed in the atmosphere rather than emitted directly?",
  ["Carbon monoxide", "Sulphur dioxide", "Soot (black carbon)", "Peroxyacetyl nitrate (PAN)"], 3,
  "Peroxyacetyl nitrate forms in photochemical smog, when oxides of nitrogen and hydrocarbons react in sunlight; it irritates "
  "the eyes and damages plants. Carbon monoxide, sulphur dioxide and soot are primary pollutants, emitted directly from "
  "combustion.",
  "env-pan-secondary-pollutant", f"{ENV_CHEM} (photochemical smog).")

mcq(PW, "medium", "The presence of which one of the following in drinking water is used as an indicator of faecal contamination?",
  ["Rhizobium", "Azotobacter", "Lactobacillus", "Escherichia coli"], 3,
  "E. coli lives in the intestines of warm-blooded animals, so finding it in water shows recent faecal contamination and "
  "the likely presence of disease-causing organisms. India's drinking water standard (IS 10500) requires it to be absent "
  "in any 100 ml sample. Rhizobium and Azotobacter are nitrogen-fixing soil bacteria, and Lactobacillus turns milk into curd.",
  "env-ecoli-indicator", "Bureau of Indian Standards, IS 10500:2012, Drinking Water - Specification; WHO, Guidelines for Drinking-water Quality.")

# --- easy / mcq (1) ---
mcq(PW, "easy", "India's National Air Quality Index, launched in 2014, classifies air quality into how many categories?",
  ["Four", "Five", "Six", "Eight"], 2,
  "The index has six categories -- Good, Satisfactory, Moderately Polluted, Poor, Very Poor and Severe -- each with its own "
  "colour code and health advice. It is based on up to eight pollutants, which is where the 'eight' distractor comes from.",
  "env-aqi-categories", "CPCB, National Air Quality Index (launched April 2014).")

# --- hard / mcq (1) ---
mcq(PW, "hard", "'Earth Overshoot Day' -- the date by which humanity's demand on nature in a year exceeds what the Earth can regenerate in that year -- is calculated by:",
  ["Global Footprint Network", "World Resources Institute", "United Nations Environment Programme", "Intergovernmental Panel on Climate Change"], 0,
  "Earth Overshoot Day is calculated by the Global Footprint Network, which compares humanity's Ecological Footprint with "
  "the Earth's biocapacity. In recent years it has fallen in late July or early August, meaning humanity uses nature about "
  "1.7 times as fast as ecosystems regenerate.",
  "env-earth-overshoot-day", "Global Footprint Network, Earth Overshoot Day and National Footprint and Biocapacity Accounts.")

# --- medium / Statement-I/II/III (1) ---
ar3(PW, "medium", "Air quality in Delhi usually deteriorates sharply in late October and November.",
  "Calm winds and low-lying temperature inversions in early winter trap pollutants close to the ground.",
  "The south-west monsoon winds, still active in November, carry dust from the Thar Desert into Delhi.",
  2,
  "Only Statement II is correct, and it explains Statement I. As winter sets in, lower wind speeds and inversions (cool air "
  "trapped beneath a warmer layer) stop pollutants from dispersing, while smoke from crop-residue burning in Punjab and "
  "Haryana and from firecrackers adds to the load. Statement III is wrong: the south-west monsoon withdraws from north-west "
  "India by October, and the post-monsoon winds over Delhi are mostly north-westerly and weak.",
  "env-delhi-winter-smog", "Commission for Air Quality Management in NCR, Graded Response Action Plan; IMD, withdrawal of the south-west monsoon; CPCB, air quality of Delhi-NCR.")

# --- medium / match (1) ---
pairs(PW, "medium", "Consider the following pairs of diseases and the pollutants that cause them:",
  ["Itai-itai disease", "Minamata disease", "Blue baby syndrome", "Black foot disease"],
  ["Mercury", "Cadmium", "Nitrates", "Lead"],
  0,
  "Only one pair, pair 3, is correct: nitrates in drinking water cause methaemoglobinaemia ('blue baby syndrome') in "
  "infants. The first two are swapped: itai-itai disease (Japan, 1910s-60s) was caused by cadmium, and Minamata disease "
  "(Japan, 1950s) by methylmercury. Black foot disease is linked to arsenic in groundwater, not lead.",
  "env-pollutant-diseases-pairs", f"{ENV_ISSUES}; WHO fact sheets on arsenic, cadmium, mercury and nitrate in drinking water.")

# ============================ CLIMATE SCIENCE & MITIGATION (15) ============================

# --- medium / statement (5) ---
stmt_opts(CS, "medium", "Consider the following statements about permafrost:",
  ["It is ground that stays at or below 0 degrees Celsius for at least two consecutive years.",
   "When it thaws, it can release carbon dioxide and methane, which add to warming.",
   "It is found only in the polar regions, and not in high mountains such as the Himalaya."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. Permafrost locks up vast amounts of frozen organic carbon; as it thaws, microbes "
  "decompose it and release CO2 and methane -- a positive feedback on warming. Statement 3 is wrong: mountain permafrost "
  "is widespread in high ranges, including the Himalaya and the Tibetan Plateau, where its thaw destabilises slopes.",
  "env-permafrost", f"{AR6}, Working Group I, ch. 9 (cryosphere); IPCC Special Report on the Ocean and Cryosphere in a Changing Climate (2019).")
FALSE_AT["env-permafrost"] = 3

stmt(CS, "medium", "Consider the following statements about aerosols and climate:",
  ["Sulphate aerosols have a net cooling effect, because they reflect sunlight back to space.",
   "Black carbon absorbs sunlight and warms the atmosphere.",
   "Black carbon deposited on snow and glaciers speeds up their melting.",
   "Aerosols stay in the atmosphere for centuries, as carbon dioxide does."],
  C4, 2,
  "Only statements 1, 2 and 3 are correct. Sulphate particles scatter sunlight and brighten clouds, masking part of "
  "greenhouse warming; black carbon (soot) absorbs sunlight, and when it settles on snow and ice it darkens them and "
  "speeds melting. Statement 4 is wrong: aerosols in the lower atmosphere are washed out within days to weeks, which is "
  "why cutting them changes their climate effect quickly, unlike long-lived CO2.",
  "env-aerosols-black-carbon", f"{AR6}, Working Group I, ch. 6 (short-lived climate forcers) and ch. 7.")
FALSE_AT["env-aerosols-black-carbon"] = 4

stmt_opts(CS, "medium", "Consider the following statements about ocean acidification:",
  ["The oceans have absorbed roughly a quarter of the carbon dioxide emitted by human activities.",
   "The absorbed carbon dioxide lowers the pH of sea water.",
   "It makes it easier for corals and molluscs to build their calcium carbonate shells and skeletons."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. Dissolved CO2 forms carbonic acid, and surface-ocean pH has fallen by about 0.1 unit "
  "since pre-industrial times. Statement 3 is the reverse: the extra acidity reduces the carbonate ions that corals, "
  "molluscs and some plankton need, making calcification harder.",
  "env-ocean-acidification", "IPCC Special Report on the Ocean and Cryosphere in a Changing Climate (2019); NOAA, Ocean Acidification.")
FALSE_AT["env-ocean-acidification"] = 3

stmt(CS, "medium", "Consider the following statements about hydrogen as a fuel:",
  ["Green hydrogen is produced by the electrolysis of water using renewable electricity.",
   "Blue hydrogen is produced by electrolysis powered by nuclear energy.",
   "Grey hydrogen is produced from natural gas without capturing the carbon dioxide released.",
   "India's National Green Hydrogen Mission aims at a green hydrogen production capacity of at least 5 million tonnes a year by 2030."],
  C4, 2,
  "Only statements 1, 3 and 4 are correct. Colour labels describe how hydrogen is made: green from renewable-powered "
  "electrolysis, grey from natural gas (steam methane reforming) with the CO2 vented. Statement 2 is wrong: blue hydrogen "
  "is made from fossil fuels with the CO2 captured and stored; hydrogen from nuclear-powered electrolysis is sometimes "
  "called pink. The National Green Hydrogen Mission, approved in January 2023, targets at least 5 MMT a year by 2030.",
  "env-hydrogen-colours", "Ministry of New and Renewable Energy, National Green Hydrogen Mission (January 2023); IEA, Global Hydrogen Review.")
FALSE_AT["env-hydrogen-colours"] = 2

stmt_opts(CS, "medium", "Consider the following statements about the urban heat island effect:",
  ["Cities are often warmer than the countryside around them, and the difference is usually greatest at night.",
   "Replacing vegetation with concrete and asphalt contributes to it.",
   "Cool roofs, coated to reflect more sunlight, can reduce it."],
  CLASSIC, 3,
  "All three statements are correct. Concrete and asphalt absorb heat by day and release it at night, while fewer trees "
  "mean less evaporative cooling, and waste heat from vehicles and air conditioners adds more. Raising the albedo of "
  "roofs and pavements and adding green cover are standard remedies, part of city heat action plans.",
  "env-urban-heat-island", f"{AR6}, Working Group I, Box TS.14 and ch. 10 (urban climate); US EPA, Heat Island Effect.")

# --- easy / statement (2) ---
stmt(CS, "easy", "Consider the following statements:",
  ["Carbon dioxide is the largest single contributor to human-caused global warming.",
   "Water vapour is not a greenhouse gas."],
  T2, 0,
  "Only statement 1 is correct. Carbon dioxide accounts for the largest share of the warming caused by human emissions. "
  "Statement 2 is wrong: water vapour is the most abundant greenhouse gas; its concentration rises as the air warms, "
  "which amplifies the warming caused by other gases (a feedback, rather than a direct human forcing).",
  "env-co2-water-vapour", f"{AR6}, Working Group I, Summary for Policymakers and FAQ 8.1.")
FALSE_AT["env-co2-water-vapour"] = 2

stmt(CS, "easy", "Consider the following statements about the Intergovernmental Panel on Climate Change (IPCC):",
  ["It carries out its own original climate research and monitoring.",
   "It was set up in 1988 by the World Meteorological Organization and the United Nations Environment Programme."],
  T2, 1,
  "Only statement 2 is correct. The IPCC was created in 1988 by the WMO and UNEP. Statement 1 is wrong: it does not run "
  "its own research or observations; it assesses the published scientific literature, and its assessment reports are "
  "written by volunteer scientists and approved by member governments.",
  "env-ipcc-role", "IPCC, 'About the IPCC'.")
FALSE_AT["env-ipcc-role"] = 1

# --- hard / statement (2) ---
stmt(CS, "hard", "With reference to the IPCC's Sixth Assessment Report (AR6), consider the following statements:",
  ["It found that global surface temperature in 2011-2020 was about 2 degrees Celsius above the 1850-1900 level.",
   "It stated that it is unequivocal that human influence has warmed the atmosphere, ocean and land.",
   "It found that pathways limiting warming to 1.5 degrees Celsius with no or limited overshoot need global greenhouse gas emissions to fall by about 43 per cent by 2030, from 2019 levels."],
  C3, 1,
  "Only statements 2 and 3 are correct. AR6 called human-caused warming 'unequivocal' and found that 1.5-degree pathways "
  "need emissions to fall about 43 per cent by 2030 and 60 per cent by 2035, from 2019 levels. Statement 1 is wrong: "
  "global surface temperature in 2011-2020 was about 1.1 degrees Celsius above 1850-1900.",
  "env-ipcc-ar6-findings", f"{AR6}, Synthesis Report, Summary for Policymakers (March 2023).")
FALSE_AT["env-ipcc-ar6-findings"] = 1

stmt(CS, "hard", "Consider the following statements about the 'Keeling Curve':",
  ["It records the atmospheric carbon dioxide concentration measured at Mauna Loa, Hawaii, since 1958.",
   "It shows a seasonal cycle in which carbon dioxide falls during the Northern Hemisphere summer, as land plants take it up.",
   "The pre-industrial concentration of carbon dioxide it is compared with was about 280 parts per million.",
   "The annual average concentration it records has been above 400 parts per million every year since 2016."],
  C4, 3,
  "All four statements are correct. Charles David Keeling began the Mauna Loa record in 1958. The Northern Hemisphere has "
  "far more land vegetation than the Southern, so CO2 dips each northern summer and rises each winter. Pre-industrial CO2 "
  "was about 280 ppm; the annual mean crossed 400 ppm in the mid-2010s and has kept rising, to above 420 ppm.",
  "env-keeling-curve", "NOAA Global Monitoring Laboratory, Trends in Atmospheric Carbon Dioxide (Mauna Loa); Scripps Institution of Oceanography, The Keeling Curve.")

# --- medium / mcq (2) ---
mcq(CS, "medium", "In climate science, the term 'carbon budget' refers to:",
  ["a country's annual public spending on climate action",
   "the cumulative amount of carbon dioxide that can still be emitted while keeping global warming below a given limit",
   "the amount of carbon stored in a country's forests",
   "the price of one tonne of carbon dioxide in an emissions trading scheme"], 1,
  "Because warming rises almost in proportion to cumulative CO2 emissions, a temperature limit implies a finite remaining "
  "'carbon budget'. AR6 put the remaining budget from 2020 for a 50 per cent chance of staying within 1.5 degrees Celsius "
  "at about 500 billion tonnes of CO2.",
  "env-carbon-budget", f"{AR6}, Working Group I, Summary for Policymakers (section D.1).")

mcq(CS, "medium", "Solar radiation modification proposals, such as stratospheric aerosol injection, aim to:",
  ["remove carbon dioxide from the air and store it underground",
   "increase the productivity of the oceans by adding iron",
   "seed clouds to increase rainfall over farmland",
   "reflect a small fraction of incoming sunlight back to space to cool the planet"], 3,
  "Solar radiation modification tries to cool the Earth by reflecting sunlight -- for example by injecting sulphate-forming "
  "gases into the stratosphere, imitating the cooling after large volcanic eruptions. It does not remove CO2, so it would "
  "not stop ocean acidification, and it carries large risks; the first option describes carbon capture and storage, the "
  "second ocean iron fertilisation.",
  "env-solar-radiation-modification", "UNEP, One Atmosphere: An Independent Expert Review on Solar Radiation Modification Research and Deployment (2023).")

# --- easy / mcq (1) ---
mcq(CS, "easy", "Which one of the following acts as a carbon sink?",
  ["A coal-fired power plant", "A cement kiln", "A growing forest", "A landfill releasing methane"], 2,
  "A carbon sink absorbs more carbon than it releases. A growing forest takes up CO2 through photosynthesis and stores the "
  "carbon in wood and soil. The other three are sources: burning coal, turning limestone into lime and rotting waste all "
  "release greenhouse gases.",
  "env-carbon-sink", f"{AR6}, Working Group I, ch. 5 (global carbon cycle).")

# --- hard / mcq (1) ---
mcq(CS, "hard", "The Arctic has been warming much faster than the global average. Which one of the following is the main reason?",
  ["The stratospheric ozone hole over the Arctic lets in more ultraviolet radiation",
   "The Arctic Ocean absorbs more carbon dioxide than tropical oceans do",
   "Heat released by volcanic activity under the Arctic seabed",
   "The loss of snow and sea ice exposes darker land and ocean, which absorb more sunlight"], 3,
  "This 'Arctic amplification' is driven mainly by the snow- and ice-albedo feedback: as bright snow and sea ice shrink, "
  "the darker surfaces beneath absorb more sunlight, which melts more ice. AR6 found the Arctic warming at more than "
  "twice the global rate. Ozone depletion mainly changes ultraviolet radiation and is not what drives the extra warming.",
  "env-arctic-amplification", f"{AR6}, Working Group I, ch. 4 and ch. 9 (Arctic amplification).")

# --- easy / Statement-I/II/III (1) ---
ar3(CS, "easy", "Most Himalayan glaciers have been losing ice in recent decades.",
  "Rising air temperatures are increasing the melting of the ice.",
  "Himalayan glaciers feed rivers such as the Indus, the Ganga and the Brahmaputra.",
  1,
  "Both Statement II and Statement III are correct, but only Statement II explains Statement I. Warming is the main "
  "reason the glaciers are shrinking (black carbon and dust on the ice add to it). Statement III is true -- the glaciers "
  "sustain the dry-season flow of the great rivers -- but that is a consequence of their existence, not a reason for "
  "their loss.",
  "env-himalayan-glacier-loss", "ICIMOD, Water, Ice, Society, and Ecosystems in the Hindu Kush Himalaya (2023); IPCC Special Report on the Ocean and Cryosphere in a Changing Climate (2019).")

# --- medium / Statement-I/II/III (1) ---
ar3(CS, "medium", "Global mean sea level is rising.",
  "The melting of floating sea ice is the main cause of the rise in global sea level.",
  "Sea water contracts as it warms, which offsets part of the rise.",
  3,
  "Statement I is correct, but neither Statement II nor Statement III is. Sea level is rising because warming water "
  "expands (not contracts) and because glaciers and the Greenland and Antarctic ice sheets on land are melting into the "
  "sea. Floating sea ice already displaces its own weight of water, so its melting adds almost nothing to sea level.",
  "env-sea-level-rise-causes", f"{AR6}, Working Group I, ch. 9 (ocean, cryosphere and sea level change).")

print("false statement at position:", FALSE_AT)
write_sql(os.path.dirname(os.path.abspath(__file__)), "environment_batch4_insert.sql")
