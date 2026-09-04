# -*- coding: utf-8 -*-
import json

def apply(path, fixes):
    data = json.load(open(path, encoding='utf-8'))
    by_ref = {q['batch_ref']: q for q in data['questions']}
    applied, missing = 0, []
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
    print(f"{path}: applied {applied}/{len(fixes)}")
    if missing:
        print("  MISSING:")
        for ref, old in missing:
            print(f"    {ref}: {old[:80]}")
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

BATCH01 = [
  ("bs1-013", "The first pan-Indian empire to be ruled entirely by a council of ministers rather than a king",
              "The first pan-Indian empire to be ruled mainly by a council of ministers rather than a king"),
  ("bs1-037", "It was led entirely by regular sepoy regiments, with local zamindars and peasants staying uninvolved throughout",
              "It was led mainly by regular sepoy regiments, with local zamindars and peasants staying largely uninvolved"),
  ("bs1-043", "Bihar did not participate in the Salt Satyagraha at all, focusing solely on the Non-Cooperation Movement's unfinished goals",
              "Bihar's participation in the Salt Satyagraha was minimal, with most local energy still directed at the Non-Cooperation Movement's unfinished goals"),
  ("bs1-046", "Ghosh was arrested and executed alongside Bhagat Singh in 1931 after refusing every offer to testify against him",
              "Ghosh was arrested and executed alongside Bhagat Singh in 1931 after refusing repeated offers to testify against him"),
  ("bs1-102", "A purely literary and cultural society that stayed clear of political activity until well into the 1940s",
              "A literary and cultural society that mostly stayed clear of political activity until well into the 1940s"),
  ("bs1-103", "It was a strictly Sufi practice confined entirely to Bihar Sharif's Firdausi order",
              "It was a Sufi practice mainly confined to Bihar Sharif's Firdausi order"),
  ("bs1-103", "It was a Vaishnavite reform movement that rejected all forms of image worship",
              "It was a Vaishnavite reform movement that rejected the practice of image worship"),
  ("bs1-109", "Sri Lanka's ruling dynasty sent a delegation of monks to permanently administer Nalanda on Dharmapala's behalf",
              "Sri Lanka's ruling dynasty sent a delegation of monks to help administer Nalanda on Dharmapala's behalf"),
]

BATCH02 = [
  ("bs1-059", "Frequent large-scale groundwater extraction across the plain is widely (though incorrectly) understood to be the single primary cause of all seismic activity recorded here",
              "Frequent large-scale groundwater extraction across the plain is sometimes assumed to be the main cause of the seismic activity recorded here"),
  ("bs1-062", "Deliberate irrigation-canal overflow has historically been channelled into the Tal region by design during every monsoon",
              "Deliberate irrigation-canal overflow has historically been channelled into the Tal region by design during the monsoon"),
  ("bs1-066", "These rivers are entirely man-made canal systems, first engineered and built during the Mughal period",
              "These rivers are man-made canal systems, first engineered and built during the Mughal period"),
  ("bs1-072", "A tropical rainforest climate typically found near the equator, with no distinct dry season at all",
              "A tropical rainforest climate typically found near the equator, with no distinct dry season"),
  ("bs1-075", "Warmer winters have shifted wheat sowing entirely into the Kharif season instead of Rabi",
              "Warmer winters have shifted wheat sowing into the Kharif season instead of Rabi"),
  ("bs1-080", "Is India's single leading region growing maize purely as a rain-fed Kharif crop, without any meaningful winter-season cultivation at all",
              "Is India's leading region growing maize mainly as a rain-fed Kharif crop, with little winter-season cultivation"),
  ("bs1-081", "A dense cluster of mineral deposits confined entirely to the single district of Rohtas",
              "A dense cluster of mineral deposits confined mainly to the district of Rohtas"),
  ("bs1-081", "A set of scattered, isolated mineral deposits that, on close inspection, follow no discernible geographic pattern at all",
              "A set of scattered, isolated mineral deposits that, on close inspection, follow no discernible geographic pattern"),
]

BATCH04 = [
  ("bs1-126", "Both houses are filled entirely through direct popular election, differing mainly in the number of seats each holds",
              "Both houses are filled through direct popular election, differing mainly in the number of seats each holds"),
  ("bs1-126", "Both houses are appointed entirely by the Governor, with no elected component in either",
              "Both houses are appointed by the Governor, with no elected component in either"),
]

BATCH05 = [
  ("bs1-135", "Support limited strictly to the single year of a girl's birth",
              "Support limited to the single year of a girl's birth"),
  ("bs1-136", "Students pursuing engineering and medical courses specifically, to the exclusion of every other stream",
              "Students pursuing engineering and medical courses specifically, with other streams not covered"),
  ("bs1-137", "Compulsory civil-services coaching for all graduates",
              "Civil-services coaching support extended to graduates"),
  ("bs1-139", "All students enrolled in government schools, regardless of academic performance",
              "Students enrolled in government schools, regardless of academic performance"),
  ("bs1-141", "It became the first Indian state to complete rural electrification using solar micro-grids exclusively",
              "It became the first Indian state to complete rural electrification using solar micro-grids as the primary technology"),
  ("bs1-141", "It became the sole state to achieve this without any central government funding support",
              "It became one of the few states to achieve this largely without central government funding support"),
  ("bs1-141", "It became the first state to offer free electricity to all households permanently thereafter",
              "It became the first state to offer free electricity to all households on a long-term basis"),
  ("bs1-143", "All families, regardless of income, as a universal marriage grant",
              "Families across income levels, as a broadly available marriage grant"),
  ("bs1-144", "Reserved government jobs allocated exclusively through this scheme",
              "Reserved government jobs allocated directly through this scheme"),
  ("bs1-144", "Monthly unemployment stipends paid regardless of any business activity",
              "Monthly unemployment stipends paid regardless of business activity"),
  ("bs1-147", "Land consolidation and abolishing all remaining tenancy arrangements",
              "Land consolidation and abolishing remaining tenancy arrangements"),
  ("bs1-147", "Converting all irrigated land to exclusively organic Kharif cultivation",
              "Converting irrigated land to organic Kharif cultivation"),
  ("bs1-149", "A one-time cash grant with no loan component at all",
              "A one-time cash grant with no loan component"),
  ("bs1-150", "An entirely unrelated, standalone programme with no connection to any earlier Bihar development scheme",
              "A standalone programme with no connection to an earlier Bihar development scheme"),
  ("bs1-151", "Both schemes are general unemployment allowances with no connection to the liquor ban at all",
              "Both schemes are general unemployment allowances with no connection to the liquor ban"),
]

apply('bihar_special_batch_01_history_culture.json', BATCH01)
apply('bihar_special_batch_02_geography.json', BATCH02)
apply('bihar_special_batch_04_polity.json', BATCH04)
apply('bihar_special_batch_05_recent_developments.json', BATCH05)
