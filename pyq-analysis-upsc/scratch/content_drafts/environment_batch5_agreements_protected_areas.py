# -*- coding: utf-8 -*-
"""Environment & Ecology batch 5 (last): every remaining cell for Climate Agreements & Carbon
Markets (12) and Protected Areas & Wildlife Protection (14), from the live gap report
regenerated 2026-09-28 after batch 4 (bank 94 rows, 26 to draft).

This batch completes the 2026-09-27 Statement-I/II allocation: Climate Agreements takes the fifth
and last three-statement slot (keyed (b), since batches 3-4 already used a/b/c/d once each and b
is the most common key in 2025's three-statement set), and Protected Areas takes the last two
two-statement slots.

No row repeats a 2015-26 PYQ angle for these sub-topics (environment_subtopic_retag.csv): 2026
asked about LT-LEDS/BUR-4, the Plan Vivo REDD+ project and Madhav National Park; 2022-Q89 asked
about WPA ownership and self-defence, not the 2022 schedule overhaul used here. Web-checked on
2026-09-28 or earlier this session: COP29's New Collective Quantified Goal (USD 300 billion a year
by 2035; USD 1.3 trillion call), the loss and damage fund (agreed COP27, operationalised COP28,
World Bank as interim host), the second cheetah site (Gandhi Sagar, April 2025). Counts that
change often (Ramsar sites, tiger reserves) are avoided.
"""
import os
import polity_common as pc
from polity_common import stmt, stmt_opts, mcq, ar, ar3, pairs, C3, C4, T2, write_sql

pc.SUBJECT = "Environment & Ecology"
CA = "Climate Agreements & Carbon Markets"
PA = "Protected Areas & Wildlife Protection"

CLASSIC = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
Y26 = ["1 only", "1 and 2", "2 and 3", "3 only"]
WPA = "Wildlife (Protection) Act, 1972"
FALSE_AT = {}

# ============================ CLIMATE AGREEMENTS & CARBON MARKETS (12) ============================

# --- medium / statement (4) ---
stmt_opts(CA, "medium", "Consider the following statements about the United Nations Framework Convention on Climate Change (UNFCCC):",
  ["It sets legally binding emission-reduction targets for each developed country.",
   "It was opened for signature at the 1992 Earth Summit in Rio de Janeiro.",
   "The principle of 'common but differentiated responsibilities and respective capabilities' is written into it."],
  CLASSIC, 1,
  "Statements 2 and 3 are correct. The UNFCCC was adopted in 1992, opened for signature at Rio and entered into force in "
  "1994; Article 3 sets out common but differentiated responsibilities. Statement 1 is wrong: the Convention itself sets "
  "only a non-binding aim for developed countries. Binding, country-by-country targets came with the Kyoto Protocol "
  "(1997).",
  "env-unfccc-basics", "United Nations Framework Convention on Climate Change (1992), Articles 3 and 4.")
FALSE_AT["env-unfccc-basics"] = 1

stmt(CA, "medium", "Consider the following statements about the fund for responding to loss and damage under the UNFCCC:",
  ["Contributions to it are legally mandatory for all developed countries.",
   "Agreement to set it up was reached at COP27 in Sharm el-Sheikh in 2022.",
   "It was operationalised at COP28 in Dubai in 2023.",
   "The World Bank hosts it, for an interim period, as a financial intermediary fund."],
  C4, 2,
  "Only statements 2, 3 and 4 are correct. COP27 agreed to create the fund, and COP28 adopted the decision that "
  "operationalised it, with the World Bank as its interim host and trustee. Statement 1 is wrong: developed countries are "
  "'urged' to lead in contributing, and others are encouraged to, but contributions are voluntary.",
  "env-loss-damage-fund", "UNFCCC decisions 2/CP.27 and 1/CP.28 (Fund for responding to Loss and Damage).")
FALSE_AT["env-loss-damage-fund"] = 1

stmt(CA, "medium", "Consider the following statements about India's Carbon Credit Trading Scheme, 2023:",
  ["It is a voluntary international market run by the UNFCCC secretariat.",
   "It was notified under the Energy Conservation Act, 2001.",
   "The Bureau of Energy Efficiency is its administrator.",
   "Under its compliance mechanism, obligated entities in energy-intensive sectors are given greenhouse gas emission intensity targets."],
  C4, 2,
  "Only statements 2, 3 and 4 are correct. The scheme was notified by the Ministry of Power in June 2023 under the Energy "
  "Conservation Act (as amended in 2022), with the Bureau of Energy Efficiency as administrator. Obligated entities that "
  "beat their emission-intensity targets earn carbon credit certificates that others can buy. Statement 1 is wrong: it is "
  "India's domestic carbon market, with a compliance mechanism and a separate offset (voluntary) mechanism.",
  "env-carbon-credit-trading-scheme", "Ministry of Power, Carbon Credit Trading Scheme, 2023 (notified 28 June 2023); Bureau of Energy Efficiency, Indian Carbon Market.")
FALSE_AT["env-carbon-credit-trading-scheme"] = 1

stmt_opts(CA, "medium", "Consider the following statements about the International Solar Alliance (ISA):",
  ["It was launched by India and France at COP21 in Paris in 2015.",
   "Its membership is limited to countries lying wholly between the Tropic of Cancer and the Tropic of Capricorn.",
   "Its headquarters are in Gurugram, India."],
  ["I only", "I and III only", "II and III only", "I, II and III"], 1,
  "Statements I and III are correct. The ISA was launched at COP21 and is headquartered in Gurugram. Statement II is wrong: "
  "it began with a focus on solar-rich countries between the tropics, but an amendment to its Framework Agreement opened "
  "membership to all member states of the United Nations.",
  "env-international-solar-alliance", "International Solar Alliance, Framework Agreement (as amended); MEA, International Solar Alliance.",
  roman=True)
FALSE_AT["env-international-solar-alliance"] = 2

# --- easy / statement (2) ---
stmt(CA, "easy", "Consider the following statements about the Kyoto Protocol:",
  ["It was adopted in 1997.",
   "It set binding emission-reduction targets for developing countries such as India and China."],
  T2, 0,
  "Only statement 1 is correct. The Protocol was adopted at COP3 in Kyoto in 1997 and entered into force in 2005. "
  "Statement 2 is wrong: binding targets applied only to the developed and transition economies listed in its Annex B; "
  "developing countries had none, though they could host Clean Development Mechanism projects.",
  "env-kyoto-protocol-targets", "Kyoto Protocol to the UNFCCC (1997), Article 3 and Annex B.")
FALSE_AT["env-kyoto-protocol-targets"] = 2

stmt(CA, "easy", "Consider the following statements:",
  ["The Conference of the Parties (COP) is the supreme decision-making body of the UNFCCC.",
   "COP30 was held in Belem, Brazil, in 2025."],
  T2, 2,
  "Both statements are correct. The COP, which meets every year, is the Convention's supreme body. COP30 was held in "
  "Belem, in the Brazilian Amazon, in November 2025, after COP29 in Baku (2024) and COP28 in Dubai (2023).",
  "env-cop-basics", "UNFCCC, Conference of the Parties (COP); UNFCCC, COP30 (Belem, November 2025).")

# --- hard / statement (2) ---
stmt(CA, "hard", "Consider the following statements about the New Collective Quantified Goal (NCQG) on climate finance:",
  ["It was adopted at COP29 in Baku in 2024.",
   "Under it, developed countries are to take the lead in mobilising at least USD 300 billion a year for developing countries by 2035.",
   "It calls on all actors to scale up finance to developing countries to at least USD 1.3 trillion a year by 2035.",
   "It succeeds the goal of USD 100 billion a year that developed countries first pledged at COP15 in Copenhagen in 2009."],
  C4, 3,
  "All four statements are correct. COP29's NCQG set a core goal of at least USD 300 billion a year by 2035, led by "
  "developed countries, inside a wider call for USD 1.3 trillion a year from all sources. It replaced the USD 100 billion "
  "goal pledged at Copenhagen and formalised at Cancun in 2010. India objected to its adoption as too little.",
  "env-ncqg-cop29", "UNFCCC decision 1/CMA.6, New collective quantified goal on climate finance (Baku, November 2024).")

stmt_opts(CA, "hard", "Consider the following statements about the Global Stocktake under the Paris Agreement:",
  ["It assesses each country's compliance individually and imposes penalties on countries that fall short.",
   "It takes place every five years.",
   "The first Global Stocktake concluded at COP28 in Dubai in 2023."],
  CLASSIC, 1,
  "Statements 2 and 3 are correct. Article 14 provides for a stocktake every five years; the first ended at COP28, whose "
  "decision called for 'transitioning away from fossil fuels in energy systems' and tripling renewable capacity by 2030. "
  "Statement 1 is wrong: the stocktake assesses collective progress towards the Agreement's goals and is non-punitive; "
  "its findings are meant to inform countries' next NDCs.",
  "env-global-stocktake", "Paris Agreement, Article 14; UNFCCC decision 1/CMA.5, Outcome of the first global stocktake (Dubai, 2023).")
FALSE_AT["env-global-stocktake"] = 1

# --- easy / mcq (1) ---
mcq(CA, "easy", "India announced its 'Panchamrit' climate commitments, including net-zero emissions by 2070, at:",
  ["COP21, Paris", "COP24, Katowice", "COP27, Sharm el-Sheikh", "COP26, Glasgow"], 3,
  "The Prime Minister announced the Panchamrit at COP26 in Glasgow in November 2021: 500 GW of non-fossil capacity, 50 "
  "per cent of energy needs from renewables, a one-billion-tonne cut in projected emissions and a 45 per cent cut in "
  "emission intensity by 2030, and net zero by 2070.",
  "env-panchamrit-cop26", "PIB, National Statement by the Prime Minister at COP26, Glasgow (1 November 2021).")

# --- medium / mcq (1) ---
mcq(CA, "medium", "India's 'Green Credit Programme', notified in 2023, is implemented under which of the following laws?",
  ["Environment (Protection) Act, 1986", "Energy Conservation Act, 2001", "Forest (Conservation) Act, 1980", "Biological Diversity Act, 2002"], 0,
  "The Green Credit Rules, 2023 were notified in October 2023 under the Environment (Protection) Act, 1986, to reward "
  "voluntary actions such as tree plantation and water conservation with tradeable green credits; the Indian Council of "
  "Forestry Research and Education administers it. The carbon market, by contrast, runs under the Energy Conservation Act.",
  "env-green-credit-programme", "MoEFCC, Green Credit Rules, 2023 (notified 12 October 2023).")

# --- easy / match (1) ---
pairs(CA, "easy", "Consider the following pairs of UNFCCC Conferences of the Parties and their outcomes:",
  ["COP3, Kyoto", "COP13, Bali", "COP21, Paris", "COP26, Glasgow"],
  ["Kyoto Protocol", "Bali Action Plan", "Paris Agreement", "Glasgow Climate Pact"],
  3,
  "All four pairs are correct. COP3 (1997) adopted the Kyoto Protocol; COP13 (2007) the Bali Action Plan, which launched "
  "talks on long-term cooperation; COP21 (2015) the Paris Agreement; and COP26 (2021) the Glasgow Climate Pact, with its "
  "call to 'phase down' unabated coal power.",
  "env-cop-outcomes-pairs", "UNFCCC, decisions and outcomes of COP3, COP13, COP21 and COP26.")

# --- medium / Statement-I/II/III (1) ---
ar3(CA, "medium", "Under the Paris Agreement, each country decides for itself how much it will cut its emissions.",
  "Nationally determined contributions (NDCs) are prepared by each Party itself, rather than being assigned or negotiated internationally.",
  "The Paris Agreement requires each Party to communicate an NDC every five years, each reflecting its highest possible ambition.",
  1,
  "Both Statement II and Statement III are correct, but only Statement II explains Statement I. The Agreement's bottom-up "
  "design lets each country set its own contribution, which is why its targets are 'nationally determined'. Statement III "
  "is also true (Article 4.3 and 4.9: successive NDCs every five years, each a progression), but it describes the timing "
  "and ratchet of the NDCs, not why their level is set nationally.",
  "env-paris-ndc-design", "Paris Agreement (2015), Articles 3, 4.2, 4.3 and 4.9.")

# ======================= PROTECTED AREAS & WILDLIFE PROTECTION (14) =======================

# --- medium / statement (5) ---
stmt(PA, "medium", "With reference to the Wildlife (Protection) Act, 1972, consider the following statements:",
  ["Hunting of wild animals in a Wildlife Sanctuary is allowed with a licence from the District Collector.",
   "Grazing of livestock is not permitted in a National Park.",
   "State Governments can declare both National Parks and Wildlife Sanctuaries."],
  C3, 1,
  "Only statements 2 and 3 are correct. Section 35(7) bars grazing in a National Park, and the State Government declares "
  "Sanctuaries (section 18) and National Parks (section 35). Statement 1 is wrong: hunting is prohibited; only the Chief "
  "Wild Life Warden can permit the capture or killing of an animal, and only for purposes the Act specifies.",
  "env-np-vs-sanctuary", f"{WPA}, sections 18, 29, 33 and 35.")
FALSE_AT["env-np-vs-sanctuary"] = 1

stmt_opts(PA, "medium", "Consider the following statements about biosphere reserves:",
  ["UNESCO's Man and the Biosphere (MAB) Programme recognises biosphere reserves in its World Network.",
   "A biosphere reserve has a core zone, a buffer zone and a transition zone, and human settlements are permitted in the transition zone.",
   "The Nilgiri Biosphere Reserve, India's first, lies wholly in Tamil Nadu."],
  CLASSIC, 0,
  "Statements 1 and 2 are correct. The MAB Programme (1971) recognises biosphere reserves in its World Network; the core "
  "is protected, the buffer allows research and limited use, and the transition zone includes settlements and sustainable "
  "economic activity. Statement 3 is wrong: the Nilgiri Biosphere Reserve (1986) spans Tamil Nadu, Kerala and Karnataka.",
  "env-biosphere-reserves", "UNESCO, Man and the Biosphere Programme and the World Network of Biosphere Reserves; MoEFCC, Biosphere Reserves of India.")
FALSE_AT["env-biosphere-reserves"] = 3

stmt_opts(PA, "medium", "Consider the following statements about Ramsar sites in India:",
  ["Chilika Lake and Keoladeo National Park were India's first Ramsar sites.",
   "Loktak Lake has never been placed on the Montreux Record.",
   "The Montreux Record lists Ramsar sites where changes in ecological character have occurred, are occurring or are likely to occur."],
  ["I only", "II and III only", "I and III only", "I, II and III"], 2,
  "Statements I and III are correct. Chilika and Keoladeo were designated in 1981, soon after India joined the Convention. "
  "Statement II is wrong: Loktak Lake in Manipur was put on the Montreux Record in 1993 and, with Keoladeo, is still on "
  "it; Chilika was placed on it and later removed after its restoration.",
  "env-ramsar-montreux-record", "Ramsar Convention Secretariat, Montreux Record and Ramsar Sites Information Service (India).",
  roman=True)
FALSE_AT["env-ramsar-montreux-record"] = 2

stmt(PA, "medium", "Consider the following statements about the Wild Life (Protection) Amendment Act, 2022:",
  ["It reduced the number of Schedules in the Act from six to four.",
   "It removed the separate Schedule of vermin species.",
   "It added a Schedule for specimens listed in the Appendices of CITES.",
   "It placed all protected plants and animals in a single Schedule."],
  C4, 2,
  "Only statements 1, 2 and 3 are correct. After the amendment, Schedules I and II cover animals (I giving the highest "
  "protection), Schedule III covers specified plants and Schedule IV covers CITES-listed specimens, with a new chapter to "
  "implement CITES. The vermin Schedule was dropped; the Centre can still declare a species vermin by notification. "
  "Statement 4 is wrong: plants and animals are in different Schedules.",
  "env-wpa-2022-schedules", "Wild Life (Protection) Amendment Act, 2022; PRS Legislative Research, The Wild Life (Protection) Amendment Bill, 2021.")
FALSE_AT["env-wpa-2022-schedules"] = 4

stmt(PA, "medium", "Consider the following statements about Project Cheetah:",
  ["The first cheetahs under the project were brought from Namibia to Kuno National Park in 2022.",
   "Gandhi Sagar Wildlife Sanctuary in Madhya Pradesh became the project's second site.",
   "The cheetahs brought to India belong to the Asiatic subspecies and came from Iran."],
  C3, 1,
  "Only statements 1 and 2 are correct. Eight cheetahs from Namibia were released in Kuno in September 2022 and twelve from "
  "South Africa followed in 2023; in April 2025 cheetahs were moved to Gandhi Sagar Wildlife Sanctuary. Statement 3 is "
  "wrong: the animals are African cheetahs -- Iran's few surviving Asiatic cheetahs were never part of the project.",
  "env-project-cheetah", "National Tiger Conservation Authority, Action Plan for Introduction of Cheetah in India (2022); PIB, cheetah release at Gandhi Sagar Wildlife Sanctuary (April 2025).")
FALSE_AT["env-project-cheetah"] = 3

# --- easy / statement (2) ---
stmt(PA, "easy", "Consider the following statements:",
  ["Project Tiger was launched in 1973.",
   "India's first national park was set up in 1936 as Hailey National Park, now Jim Corbett National Park."],
  T2, 2,
  "Both statements are correct. Project Tiger began in 1973 with nine tiger reserves. Hailey National Park, set up in "
  "the United Provinces in 1936, was renamed Ramganga and then Corbett National Park, after the hunter-naturalist Jim "
  "Corbett.",
  "env-project-tiger-corbett", "National Tiger Conservation Authority, Project Tiger; Uttarakhand Forest Department, Corbett Tiger Reserve.")

stmt(PA, "easy", "Consider the following statements:",
  ["World Wetlands Day is observed on 2 February.",
   "The Ramsar Convention on Wetlands was signed at Ramsar in India."],
  T2, 0,
  "Only statement 1 is correct. World Wetlands Day, 2 February, marks the signing of the Convention in 1971. Statement 2 "
  "is wrong: Ramsar is a town on the Caspian Sea coast of Iran.",
  "env-world-wetlands-day", "Ramsar Convention Secretariat, World Wetlands Day and the history of the Convention.")
FALSE_AT["env-world-wetlands-day"] = 2

# --- hard / statement (2) ---
stmt(PA, "hard", "Consider the following statements about tiger conservation in India:",
  ["Tiger reserves are notified by State Governments on the recommendation of the National Tiger Conservation Authority.",
   "A tiger reserve consists of a core or critical tiger habitat and a buffer or peripheral area.",
   "The 2022 cycle of the All India Tiger Estimation put India's tiger population at about 3,682 (mean estimate).",
   "Madhya Pradesh had the largest number of tigers in the 2022 estimate."],
  C4, 3,
  "All four statements are correct. Under section 38V of the Wildlife (Protection) Act, a State notifies a tiger reserve "
  "on the NTCA's recommendation, with an inviolate core and a buffer where people and wildlife coexist. The 2022 estimate "
  "(released in 2023) gave a mean of 3,682 tigers, about three-quarters of the world's wild tigers, with Madhya Pradesh "
  "(785) ahead of Karnataka and Uttarakhand.",
  "env-tiger-reserves-estimation", f"{WPA}, section 38V; NTCA and Wildlife Institute of India, Status of Tigers, Co-predators and Prey in India 2022 (2023).")

stmt(PA, "hard", "Consider the following statements about Biodiversity Heritage Sites:",
  ["They are notified by State Governments under the Biological Diversity Act, 2002.",
   "Nallur Tamarind Grove in Karnataka was India's first Biodiversity Heritage Site.",
   "Notifying an area as a Biodiversity Heritage Site bans all use of it by local communities."],
  C3, 1,
  "Only statements 1 and 2 are correct. Section 37 of the Act lets a State Government, in consultation with local bodies, "
  "notify areas of biodiversity importance as Biodiversity Heritage Sites; Nallur Tamarind Grove was the first, in 2007. "
  "Statement 3 is wrong: the national guidelines say notification should not restrict the prevailing practices and usages "
  "of local communities, other than those they decide on voluntarily.",
  "env-biodiversity-heritage-sites", "Biological Diversity Act, 2002, section 37; National Biodiversity Authority, Guidelines for Selection and Management of Biodiversity Heritage Sites.")
FALSE_AT["env-biodiversity-heritage-sites"] = 3

# --- medium / mcq (2) ---
mcq(PA, "medium", "Which one of the following protected areas, known for the greater one-horned rhinoceros, is a UNESCO World Heritage Site?",
  ["Jaldapara National Park", "Orang National Park", "Dudhwa National Park", "Kaziranga National Park"], 3,
  "Kaziranga in Assam, home to about two-thirds of the world's greater one-horned rhinos, was inscribed as a natural World "
  "Heritage Site in 1985. Jaldapara (West Bengal), Orang (Assam) and Dudhwa (Uttar Pradesh) also hold rhinos but are not "
  "World Heritage Sites.",
  "env-kaziranga-whs", "UNESCO World Heritage Centre, Kaziranga National Park (inscribed 1985).")

mcq(PA, "medium", "India's first Marine National Park was established in the:",
  ["Gulf of Kutch", "Gulf of Mannar", "Andaman Islands (Wandoor)", "Malvan coast"], 0,
  "The Marine National Park in the Gulf of Kutch, Gujarat, notified in 1982, was India's first. The Mahatma Gandhi Marine "
  "National Park at Wandoor in the Andamans followed in 1983 and the Gulf of Mannar Marine National Park in 1986.",
  "env-first-marine-national-park", "Gujarat Forest Department, Marine National Park, Gulf of Kutch; ENVIS Centre on Wildlife and Protected Areas (WII), Marine Protected Areas of India.")

# --- easy / mcq (1) ---
mcq(PA, "easy", "Silent Valley National Park, the focus of a famous campaign against a hydroelectric project in the 1970s-80s, is in:",
  ["Karnataka", "Tamil Nadu", "Kerala", "Goa"], 2,
  "Silent Valley is in Kerala's Palakkad district, in the Nilgiri Biosphere Reserve. The 'Save Silent Valley' movement "
  "against a proposed dam on the Kunthipuzha river led to the project being dropped and the forest being declared a "
  "national park in 1984.",
  "env-silent-valley", "Kerala Forest Department, Silent Valley National Park.")

# --- easy / Statement-I/II (1) ---
ar(PA, "easy", "The tiger is described as an 'umbrella species'.",
  "Protecting the tiger's large habitat also protects the many other species that share it.",
  0,
  "Both statements are correct and Statement-II explains Statement-I. An umbrella species needs such a large area of "
  "habitat that conserving it automatically conserves many other plants and animals -- which is why tiger reserves also "
  "protect watersheds, elephants, deer and countless smaller species.",
  "env-tiger-umbrella-species", "National Tiger Conservation Authority, Project Tiger; Wildlife Institute of India.")

# --- medium / Statement-I/II (1) ---
ar(PA, "medium", "Elephant Reserves in India are notified under the Wildlife (Protection) Act, 1972.",
  "Project Elephant was launched in 1992 to protect elephants, their habitats and their corridors.",
  3,
  "Statement-I is incorrect but Statement-II is correct. Elephant Reserves are an administrative designation made by the "
  "States under Project Elephant; unlike tiger reserves, they have no separate legal status under the Wildlife "
  "(Protection) Act, though they often contain National Parks and Sanctuaries. Project Elephant was launched in 1992.",
  "env-elephant-reserves-status", "MoEFCC, Project Elephant (Project Elephant and Tiger Division); Wildlife Institute of India, Right of Passage: Elephant Corridors of India.")

print("false statement at position:", FALSE_AT)
write_sql(os.path.dirname(os.path.abspath(__file__)), "environment_batch5_insert.sql")
