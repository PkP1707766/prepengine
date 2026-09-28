# -*- coding: utf-8 -*-
"""Geography batch 1 (checkpoint): one row from each of the five largest cells of the live gap
report generated 2026-09-28 from the re-tagged config (retag_geography_subtopics.py):
  1. medium / statement / World Regions, Water Bodies & Places   (8)
  2. medium / statement / Climatology & Biomes                   (7)
  3. medium / statement / Indian Physiography, Climate & Regions (6)
  4. medium / statement / Indian Rivers, Lakes & Wetlands        (5)
  5. medium / mcq / Climatology & Biomes                         (4)

Formats follow Geography's own 2023-26 mix: a 'how many of the following countries' count
(2023-Q61 Ukraine, 2024-Q8 North Sea), a 'how many statements' count, the 2025 Roman-numbered
combination form, 2026's '1 only / 1 and 2 / 2 and 3 / 3 only' set, and a single-answer MCQ.
None repeats a PYQ angle from geography_subtopic_retag.csv (the Caspian, local winds, Ghats
relief, peninsular rivers and annual temperature range are all untested in 2015-26).

UPSC Geography rows use the concept prefix 'ugeo-': BPSC's Geography rows already use 'geo-'.
"""
import os
import polity_common as pc
from polity_common import stmt, stmt_opts, mcq, C4, write_sql

pc.SUBJECT = "Geography"
WR = "World Regions, Water Bodies & Places"
CL = "Climatology & Biomes"
IP = "Indian Physiography, Climate & Regions"
IR = "Indian Rivers, Lakes & Wetlands"

Y26 = ["1 only", "1 and 2", "2 and 3", "3 only"]
NCERT_FPG = "NCERT Geography Class XI, 'Fundamentals of Physical Geography'"
NCERT_IPE = "NCERT Geography Class XI, 'India: Physical Environment'"
FALSE_AT = {}

# 1. medium / statement / World Regions -- a country-list count, as in 2023-Q61 and 2024-Q8
stmt(WR, "medium", "Consider the following countries:",
  ["Azerbaijan", "Georgia", "Iran", "Uzbekistan"],
  C4, 1,
  "Only two -- Azerbaijan and Iran. The Caspian Sea is bordered by five countries: Russia, Kazakhstan, Turkmenistan, "
  "Iran and Azerbaijan. Georgia lies on the Black Sea coast, on the other side of the Caucasus. Uzbekistan is one of "
  "the world's two doubly landlocked countries; the water body it shares with Kazakhstan is the Aral Sea, not the "
  "Caspian.",
  "ugeo-caspian-littoral-states", "Encyclopaedia Britannica, 'Caspian Sea'; CIA World Factbook, country profiles of Georgia and Uzbekistan.",
  closing="How many of the above countries have a coastline on the Caspian Sea?")
FALSE_AT["ugeo-caspian-littoral-states"] = "2,4"

# 2. medium / statement / Climatology -- local winds
stmt(CL, "medium", "Consider the following statements about local winds:",
  ["The Chinook is a warm, dry wind that blows down the eastern slopes of the Rocky Mountains.",
   "The Mistral is a cold wind that blows down the Rhone valley towards the Mediterranean.",
   "The Harmattan is a hot, humid wind that blows from the Atlantic onto the coast of West Africa.",
   "The Sirocco is a hot wind that blows from the Sahara towards southern Europe."],
  C4, 2,
  "Only statements 1, 2 and 4 are correct. The Chinook is a fohn-type wind: air warms as it descends the leeward "
  "(eastern) side of the Rockies, melting snow quickly, hence 'snow eater'. The Mistral is funnelled down the Rhone "
  "valley to the Gulf of Lion, and the Sirocco carries hot, dusty Saharan air across the Mediterranean. Statement 3 "
  "is wrong: the Harmattan is a dry, dusty north-easterly that blows from the Sahara over West Africa; its dryness "
  "is such a relief from the humid coast that it is called 'the doctor'.",
  "ugeo-local-winds", f"{NCERT_FPG}, ch. 'Atmospheric Circulation and Weather Systems' (local winds); Encyclopaedia Britannica, 'Harmattan'.")
FALSE_AT["ugeo-local-winds"] = 3

# 3. medium / statement / Indian Physiography -- 2025 Roman-numbered combination
stmt_opts(IP, "medium", "Consider the following statements about the Western and Eastern Ghats:",
  ["The Western Ghats are more continuous than the Eastern Ghats.",
   "The Western Ghats are generally lower in elevation than the Eastern Ghats.",
   "Anamudi, the highest peak of peninsular India, lies in the Western Ghats."],
  ["I and III only", "I and II only", "II and III only", "I, II and III"], 0,
  "Statements I and III are correct. The Western Ghats run almost unbroken along the west coast and can be crossed "
  "only through passes such as the Thal, Bhor and Pal Ghats, whereas the Eastern Ghats are discontinuous, broken up "
  "by the Mahanadi, Godavari, Krishna and Kaveri. Anamudi (2,695 m) in the Anaimalai Hills of Kerala is the highest "
  "peak of peninsular India. Statement II is the reverse: the Western Ghats are higher (roughly 900-1,600 m on "
  "average) than the Eastern Ghats (roughly 600 m).",
  "ugeo-western-eastern-ghats", f"{NCERT_IPE}, ch. 'Structure and Physiography' (the Peninsular Plateau).",
  roman=True)
FALSE_AT["ugeo-western-eastern-ghats"] = 2

# 4. medium / statement / Indian Rivers -- 2026's '1 only / 1 and 2 / 2 and 3 / 3 only' set
stmt_opts(IR, "medium", "Consider the following statements about the rivers of peninsular India:",
  ["The Narmada and the Tapi flow westwards through rift valleys.",
   "The Mahanadi rises in Chhattisgarh and forms a delta in Odisha.",
   "The Godavari, the longest river of peninsular India, ends in an estuary rather than a delta."],
  Y26, 1,
  "Statements 1 and 2 are correct. The Narmada and the Tapi are the two large west-flowing rivers of the Peninsula; "
  "they run through faulted rift valleys and end in estuaries, not deltas. The Mahanadi rises near Sihawa in "
  "Chhattisgarh and builds a delta on the Odisha coast. Statement 3 is wrong: the Godavari (about 1,465 km) is indeed "
  "the longest peninsular river, but like the other east-flowing rivers it forms a large delta on the Bay of Bengal.",
  "ugeo-peninsular-river-mouths", f"{NCERT_IPE}, ch. 'Drainage System' (the Peninsular drainage system).")
FALSE_AT["ugeo-peninsular-river-mouths"] = 3

# 5. medium / mcq / Climatology -- annual temperature range by climate type
mcq(CL, "medium", "Which one of the following climate types has the largest annual range of temperature?",
  ["Equatorial rainforest climate", "Mediterranean climate", "Tropical savanna climate", "Sub-arctic continental (taiga) climate"], 3,
  "The sub-arctic continental climate of Siberia and northern Canada, deep inside large landmasses, has the largest "
  "annual range on Earth: Verkhoyansk averages below -45 degrees Celsius in January and about +15 degrees in July, a "
  "range above 60 degrees. The equatorial climate has the smallest annual range (2-3 degrees), and the other two are "
  "moderated by latitude or by the sea.",
  "ugeo-taiga-annual-range", f"{NCERT_FPG}, ch. 'World Climate and Climate Change' (Koppen's classification).")

print("false statement at position:", FALSE_AT)
write_sql(os.path.dirname(os.path.abspath(__file__)), "geography_batch1_insert.sql")
