# -*- coding: utf-8 -*-
"""Environment & Ecology batch 1 (checkpoint): one question for each of the top 5 rows of the
live gap report (environment_gap_report_output.txt, config e6f68e99 with the content-derived
Environment weights written 2026-09-28). All five rows are medium / statement_based:

  1  Fauna & Animal Behaviour              (9 in cell)   Nilgiri tahr            C3 ladder
  2  Pollution, Waste & Resources          (8)           ground-level ozone      C3 ladder
  3  Climate Science & Mitigation          (6)           global warming potential T2 ladder
  4  Flora, Fungi & Forests                (5)           mangroves               2026-style combinations
  5  Climate Agreements & Carbon Markets   (5)           Paris Agreement Art. 6  C4 ladder

Statement formats follow Environment's own 2023-26 mix (count, 2-statement and the combination
options that 6 of 2026's 7 statement questions used). The false statement sits at position 1, 2
and 3 respectively in the three questions that have one. Facts cross-checked 2026-09-28 against
the IPCC AR6 WGI Ch.7 table, UNFCCC's Article 6 / A6.4 pages, the PIB release of 17 Feb 2023 on
India's Article 6.2 activities, the US EPA ozone basics page, the CPCB NAAQS 2009 notification,
and WWF-India / Kerala Forest Department material on the Nilgiri tahr. No topic repeats a
2023-26 PYQ (checked against environment_ecology_qs_2023_2026.txt).
"""
import os
import polity_common as pc
from polity_common import stmt, stmt_opts, C3, C4, T2, write_sql

pc.SUBJECT = "Environment & Ecology"

FA = "Fauna & Animal Behaviour"
PW = "Pollution, Waste & Resources"
CS = "Climate Science & Mitigation"
FL = "Flora, Fungi & Forests"
CA = "Climate Agreements & Carbon Markets"

# 1. Fauna -- trap ED1 (species-habitat swap): a real species, right range, wrong habitat.
stmt(FA, "medium", "Consider the following statements about the Nilgiri tahr:",
  ["It is chiefly a browser of dense evergreen forest interiors and avoids open grassland.",
   "Eravikulam National Park in Kerala holds the largest single population of the species.",
   "It is endemic to the Western Ghats and is the State animal of Tamil Nadu."],
  C3, 1,
  "Only statements 2 and 3 are correct. The Nilgiri tahr lives on the open montane grasslands and rocky cliffs of the southern "
  "Western Ghats, roughly 1,200-2,600 m up, and grazes on grasses -- it is not a forest-interior browser, which is the planted "
  "habitat swap in statement 1. Eravikulam National Park near Munnar holds the largest single population. The species is endemic "
  "to the Western Ghats, is Tamil Nadu's State animal, is listed as Endangered by the IUCN and is in Schedule I of the Wildlife "
  "(Protection) Act, 1972.",
  "env-nilgiri-tahr-habitat",
  "WWF-India, 'Nilgiri tahr' (priority species); Kerala Forest Department, Eravikulam National Park; IUCN Red List, Nilgiritragus hylocrius.")

# 2. Pollution -- trap: 'not emitted, so not regulated' -- a secondary pollutant sounds like it
# would fall outside emission-based standards. All three statements are true.
stmt(PW, "medium", "Consider the following statements about ground-level (tropospheric) ozone:",
  ["It is not emitted directly in significant quantities; it forms when oxides of nitrogen and volatile organic compounds react in the presence of sunlight.",
   "Because its formation is driven by sunlight and heat, it tends to reach its highest levels on hot, sunny days.",
   "It is one of the twelve pollutants covered by India's National Ambient Air Quality Standards notified in 2009."],
  C3, 2,
  "All three statements are correct. Ground-level ozone is a secondary pollutant: vehicles, power plants and industry emit its "
  "precursors (NOx and VOCs), and ozone forms from them in sunlight, so levels build up on hot, sunny days and it is mainly a "
  "summertime pollutant. Being secondary does not keep it out of regulation: the National Ambient Air Quality Standards, 2009 "
  "cover twelve pollutants, including ozone (8-hour and 1-hour limits), alongside SO2, NO2, PM10, PM2.5, CO, lead, ammonia, "
  "benzene, benzo(a)pyrene, arsenic and nickel. Do not confuse it with the stratospheric ozone layer, which is protective.",
  "env-ground-level-ozone",
  "US EPA, 'Ground-level Ozone Basics'; CPCB, National Ambient Air Quality Standards (notification of 18 November 2009).")

# 3. Climate science -- traps: comparative-magnitude (N2O vs CH4) and fact-vs-inference (a true
# comparison is not asked; statement 2 pairs a wrong comparison with a wrong reason).
stmt(CS, "medium", "Consider the following statements about global warming potential (GWP):",
  ["On a 100-year time horizon, nitrous oxide has a higher global warming potential than methane.",
   "Methane's global warming potential is lower on a 20-year horizon than on a 100-year horizon, because methane stays in the atmosphere for several centuries."],
  T2, 0,
  "Only statement 1 is correct. GWP compares the warming caused by a gas over a chosen period with that of the same mass of CO2 "
  "(GWP = 1). In IPCC AR6 the 100-year GWP of nitrous oxide is 273, against about 27-30 for methane. Statement 2 is wrong on both "
  "counts: methane lasts only about 12 years in the atmosphere, so its effect is concentrated early -- its 20-year GWP (about 81) is "
  "far higher than its 100-year GWP, which is why cutting methane is seen as the fastest lever on near-term warming.",
  "env-gwp-methane-n2o",
  "IPCC AR6 Working Group I, Chapter 7, Table 7.15 (emission metrics).")

# 4. Flora -- trap: place / absolutist swap ('only along the eastern coast') inside a set of
# true adaptation facts. 2026-style combination options.
stmt_opts(FL, "medium", "Consider the following statements about mangroves:",
  ["Pneumatophores are aerial roots that help mangrove plants take in oxygen in waterlogged, oxygen-poor mud.",
   "In viviparous mangroves, the seed germinates while the fruit is still attached to the parent tree.",
   "In India, mangroves occur only along the eastern coast and in the Andaman and Nicobar Islands."],
  ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 1,
  "Statements 1 and 2 are correct. Pneumatophores (breathing roots) rise above the mud to take in air, and vivipary -- germination "
  "while still on the parent tree -- lets the seedling establish quickly in tidal mud. Statement 3 is wrong: India's west coast has "
  "extensive mangroves, notably in the Gulf of Kutch and Gulf of Khambhat in Gujarat (the State with the second-largest mangrove "
  "cover after West Bengal), and along the Maharashtra, Goa, Karnataka and Kerala coasts.",
  "env-mangrove-adaptations",
  "NCERT Class XI, 'India: Physical Environment', ch. 5 (Natural Vegetation); Forest Survey of India, India State of Forest Report 2021, mangrove cover.")

# 5. Climate agreements -- traps: currency (statement 4 is a real but little-known 2023 Indian
# decision) and scope (statement 2's CDM link). All four statements are true.
stmt(CA, "medium", "Consider the following statements regarding Article 6 of the Paris Agreement:",
  ["Under Article 6.2, countries can transfer internationally transferred mitigation outcomes (ITMOs) between themselves through bilateral or cooperative approaches.",
   "The mechanism under Article 6.4 is supervised by a Supervisory Body, and activities registered under the Kyoto Protocol's Clean Development Mechanism may transition to it.",
   "Corresponding adjustments are applied so that a transferred emission reduction is not counted towards the NDCs of both the transferring and the acquiring country.",
   "India has finalised a list of activities that it would consider for trading carbon credits under Article 6.2."],
  C4, 3,
  "All four statements are correct. Article 6.2 lets Parties cooperate bilaterally and count ITMOs towards their NDCs; Article 6.4 "
  "sets up a UN-run crediting mechanism (the Paris Agreement Crediting Mechanism), run by the Article 6.4 Supervisory Body, into "
  "which CDM activities may transition. Corresponding adjustments prevent the same reduction being counted twice. In February 2023 "
  "India finalised 13 activities under three heads -- GHG mitigation, alternate materials and removals -- that it would consider for "
  "Article 6.2 trading, such as green hydrogen, offshore wind and tidal energy.",
  "env-paris-article6",
  "UNFCCC, 'Article 6 of the Paris Agreement' and 'Article 6.4 Supervisory Body'; PIB, MoEFCC release of 17 February 2023 (Article 6.2 activities).")

# statement-position check: position of the false statement in each question that has one
FALSE_AT = {"env-nilgiri-tahr-habitat": 1, "env-gwp-methane-n2o": 2, "env-mangrove-adaptations": 3}
print("false statement at position:", FALSE_AT)

write_sql(os.path.dirname(os.path.abspath(__file__)), "environment_batch1_insert.sql")
