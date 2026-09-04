import json

data = json.load(open('bihar_special_batch_01_history_culture.json', encoding='utf-8'))
by_ref = {q['batch_ref']: q for q in data['questions']}

fixes = [
  ("bs1-005", "Licchavi", "Licchavi (of Vaishali)"),
  ("bs1-005", "Videha", "Videha (of Mithila)"),
  ("bs1-005", "Malla", "Malla (of Kushinagar)"),

  ("bs1-011", "A doctrinal dispute between Bhadrabahu and Sthulabhadra over the interpretation of the Angas",
              "A doctrinal dispute between Bhadrabahu and Sthulabhadra over the correct interpretation of the Angas, a disagreement that predated the famine and remained unresolved even after Vallabhi"),
  ("bs1-011", "Chandragupta Maurya ordered a formal division of the Sangha after his conversion",
              "Chandragupta Maurya, after his own conversion to Jainism, formally ordered the Sangha split into two administratively separate wings to smooth his transition into asceticism"),
  ("bs1-011", "The Second Jain Council at Vallabhi formally created the two sects by compiling separate scriptures",
              "The Second Jain Council at Vallabhi formally created the two sects when Devarddhi Kshamashraman compiled two separate, incompatible sets of the Angas and Upangas for each"),

  ("bs1-014", "Alexander himself judged Dhanananda's forces unbeatable and called off the campaign",
              "Alexander himself judged Dhanananda's forces unbeatable after intelligence reports on Nanda troop strength, and personally called off the campaign"),
  ("bs1-014", "A treaty was signed between Alexander and Dhanananda's envoys before any confrontation occurred",
              "A treaty was signed between Alexander and envoys sent by Dhanananda, averting any confrontation before the two armies could meet near the Beas"),
  ("bs1-014", "Dhanananda's forces launched a pre-emptive attack that forced Alexander into retreat",
              "Dhanananda's forces launched a pre-emptive attack across the Beas that forced Alexander's army into a hasty retreat toward the Indus"),

  ("bs1-018", "That the Mauryan army used war elephants extensively in battle",
              "That the Mauryan army used war elephants extensively in battle, a practice Megasthenes considered distinctive to Indian warfare"),
  ("bs1-018", "That Pataliputra was administered by six committees of five members each",
              "That Pataliputra was administered by six committees of five members each, overseeing trade, foreigners and manufacturing separately"),
  ("bs1-018", "That the Mauryan state employed two categories of spies, stationary and wandering",
              "That the Mauryan state employed two categories of spies, stationary and wandering, both reporting directly to the king"),

  ("bs1-021", "Both regions were treated identically under grahana-moksha-anugraha, differing only in the tribute rate charged",
              "Both regions were treated under the same grahana-moksha-anugraha policy, though the tribute rate charged varied significantly by region"),

  ("bs1-026", "He seized the throne through a palace coup against a Kanva-dynasty minister",
              "He seized the throne through a palace coup against a Kanva-dynasty minister who had ruled Magadh through the anarchy's final years"),
  ("bs1-026", "He was appointed governor by the Gupta court before declaring independence",
              "He was appointed governor of the region by the Gupta court before declaring independence once Gupta central authority collapsed"),
  ("bs1-026", "He won the throne through a marriage alliance with the Licchavi royal family",
              "He won the throne through a marriage alliance with the Licchavi royal family, echoing the earlier Gupta-Licchavi political marriages"),

  ("bs1-028", "It restored the Karnat dynasty to power after a period of Delhi Sultanate direct rule",
              "It restored the Karnat dynasty to power in Tirhut after an earlier period of direct Delhi Sultanate administration"),
  ("bs1-028", "It established the Karnat dynasty for the first time, replacing an earlier Pala-appointed governor",
              "It established the Karnat dynasty for the first time, replacing an earlier Pala-appointed governor of the region"),
  ("bs1-028", "It had no lasting effect on Tirhut, which remained under the Karnat dynasty until the Mughal period",
              "It had no lasting effect on Tirhut, which remained under the Karnat dynasty's control right through the Mughal period"),

  ("bs1-034", "Plassey was decided by battlefield betrayal (Mir Jafar's defection); Buxar was a genuine full-scale military contest that the British won outright against a combined force including the Mughal Emperor himself",
              "Plassey hinged on Mir Jafar's battlefield defection; Buxar was a genuine full-scale contest the British won outright against a three-way alliance including the Mughal Emperor"),
  ("bs1-034", "Buxar was decided by betrayal, while Plassey was a straightforward military victory",
              "Buxar was decided by betrayal, when a Company-aligned general defected mid-battle, while Plassey was a straightforward military victory without any such defection"),
  ("bs1-034", "Both battles were decided primarily through betrayal by an Indian commander on the losing side",
              "Both battles were decided primarily through betrayal by an Indian commander switching sides on the losing party's payroll"),
  ("bs1-034", "Plassey was fought in Bihar, while Buxar was fought in Bengal",
              "Plassey was fought on Bihar's soil near Patna, while Buxar took place across the border inside Bengal territory"),

  ("bs1-037", "It began earlier than either Delhi or Meerut, in 1855",
              "It began earlier than either Delhi or Meerut, with isolated unrest reported in Bihar as early as 1855"),
  ("bs1-037", "It was led entirely by regular sepoy regiments with no civilian involvement",
              "It was led entirely by regular sepoy regiments, with local zamindars and peasants staying uninvolved throughout"),
  ("bs1-037", "It was suppressed without any British military casualties",
              "It was suppressed swiftly, with British forces reporting almost no casualties across the entire Bihar campaign"),

  ("bs1-038", "He surrendered his weapons to protect his troops from further bombardment",
              "He surrendered his weapons on the riverbank to protect his remaining troops from further British bombardment"),
  ("bs1-038", "He ordered his own boat sunk to draw British fire away from his soldiers",
              "He ordered his own boat deliberately sunk mid-river to draw British cannon fire away from his soldiers' boats"),
  ("bs1-038", "He swam the river alone to negotiate a ceasefire with British officers",
              "He swam across the river alone at night to personally negotiate a ceasefire with the pursuing British officers"),

  ("bs1-039", "The Arya Samaj", "The Arya Samaj (Swami Dayanand Saraswati)"),
  ("bs1-039", "The Aligarh Movement", "The Aligarh Movement (Sir Syed Ahmad Khan)"),
  ("bs1-039", "The Theosophical Society", "The Theosophical Society (a Gaya-based centre)"),

  ("bs1-043", "Salt was smuggled in from coastal Bengal, and Bihar's addition was a boycott of British-made cloth",
              "Salt was smuggled overland from coastal Bengal by rail, and Bihar's own contribution was a parallel boycott of British-made cloth"),
  ("bs1-043", "Salt was manufactured industrially at Golghar and distributed free to protestors",
              "Salt was manufactured industrially at the Golghar granary in Patna and distributed free to protestors across the district"),

  ("bs1-045", "The Kaimur hills", "The Kaimur hills (Amar Singh's later resistance base)"),
  ("bs1-045", "Rohtasgarh Fort", "Rohtasgarh Fort (the old Sher Shah-era stronghold)"),
  ("bs1-045", "Munger district's underground parallel government",
              "Munger district's underground parallel government, set up during the same 1942 uprising"),

  ("bs1-046", "Ghosh was a Bihar-based HSRA member who helped Bhagat Singh escape custody, and was later honoured for it",
              "Ghosh was a Bihar-based HSRA member who helped Bhagat Singh escape custody during his trial, and was later honoured with a state pension"),
  ("bs1-046", "Ghosh was executed alongside Bhagat Singh after refusing to testify against him",
              "Ghosh was arrested and executed alongside Bhagat Singh in 1931 after refusing every offer to testify against him"),
  ("bs1-046", "Ghosh led the Patna Conspiracy Case unrelated to the Bhagat Singh trial",
              "Ghosh led the unrelated Patna Conspiracy Case of 1930, a case with no real connection to the Bhagat Singh trial"),

  ("bs1-051", "Kachni relies on solid, vivid colour fills, while Bharni uses only fine line work without colour",
              "Kachni relies on solid, vivid colour fills applied heavily across the canvas, while Bharni is instead built from fine, uncoloured line work throughout"),
  ("bs1-051", "Kachni is exclusively religious in theme, while Bharni depicts only natural motifs like the sun and lotus",
              "Kachni is generally religious in theme, while Bharni tends to depict natural motifs like the sun, moon and lotus instead"),
  ("bs1-051", "Kachni uses synthetic dyes, while Bharni is restricted to natural pigments only",
              "Kachni is typically made using synthetic dyes, while Bharni sticks to the traditional natural pigments like turmeric and indigo"),

  ("bs1-053", "Maithili is included in the Indian Constitution's Eighth Schedule, while Bhojpuri -- despite being far more widely spoken through migration and having a large film industry -- has no such constitutional status",
              "Maithili is in the Constitution's Eighth Schedule, while Bhojpuri -- despite far wider reach through migration and a large film industry -- has no such status"),
  ("bs1-053", "Bhojpuri has its own traditional script (Mithilakshar), while Maithili has never had a dedicated script",
              "Bhojpuri has its own traditional script called Kaithi, while Maithili's literary tradition has relied throughout on the Devanagari script instead"),
  ("bs1-053", "Maithili is spoken mainly through migrant diaspora communities, while Bhojpuri is confined entirely to its home districts",
              "Maithili is spoken mainly through migrant diaspora communities abroad, while Bhojpuri has remained confined to its home districts within Bihar"),
  ("bs1-053", "Both languages were added to the Eighth Schedule in the same 2003 constitutional amendment",
              "Both languages were added to the Constitution's Eighth Schedule together, under the same 2003 constitutional amendment"),
]

applied = 0
missing = []
for ref, old, new in fixes:
    q = by_ref[ref]
    found = False
    for o in q['options']:
        if o['body'] == old:
            o['body'] = new
            found = True
            applied += 1
            break
    if not found:
        missing.append((ref, old))

print(f"applied {applied}/{len(fixes)} fixes")
if missing:
    print("MISSING (no exact match found):")
    for ref, old in missing:
        print(f"  {ref}: {old[:80]}")

json.dump(data, open('bihar_special_batch_01_history_culture.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
