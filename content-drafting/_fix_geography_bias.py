import json

data = json.load(open('bihar_special_batch_02_geography.json', encoding='utf-8'))
by_ref = {q['batch_ref']: q for q in data['questions']}

fixes = [
  ("bs1-058", "Both are equally fertile and differ only in colour, not in elevation or age",
              "Both are considered equally fertile, differing mainly in colour rather than in elevation or age"),
  ("bs1-058", "Bhangar is confined to south Bihar only, while Khadar covers both north and south Bihar equally",
              "Bhangar is generally confined to south Bihar, while Khadar is found across both north and south Bihar"),

  ("bs1-059", "The region sits directly above an extinct volcanic hotspot beneath the Gangetic sediment",
              "The region sits directly above an extinct volcanic hotspot buried deep beneath the Gangetic sediment layer"),
  ("bs1-059", "Frequent large-scale groundwater extraction alone is understood to be the primary cause of seismic activity here",
              "Frequent large-scale groundwater extraction is widely understood to be the single primary cause of all seismic activity recorded in this region"),
  ("bs1-059", "The Kosi and Gandak rivers generate seismic tremors through their high sediment discharge during floods",
              "The Kosi and Gandak rivers are believed to generate seismic tremors directly through their unusually high sediment discharge during flood events"),

  ("bs1-062", "Heavy industrial groundwater extraction lowers the water table, creating depressions that fill seasonally",
              "Heavy industrial groundwater extraction lowers the regional water table, creating shallow depressions that fill up only during the monsoon season"),
  ("bs1-062", "Limestone bedrock dissolution creates sinkhole-like depressions across the region",
              "Limestone bedrock dissolution gradually creates sinkhole-like depressions scattered across this part of south Bihar"),
  ("bs1-062", "Deliberate irrigation-canal overflow is channelled into the Tal region by design each monsoon",
              "Deliberate irrigation-canal overflow has historically been channelled into the Tal region by design during every monsoon"),

  ("bs1-064", "It is the only Bihar river that flows from south to north instead of the usual drainage pattern",
              "It flows from south to north, the sole Bihar river confirmed to follow this reversed drainage pattern"),
  ("bs1-064", "It is Bihar's only river with a source entirely within Bihar's own borders",
              "It is one of very few Bihar rivers whose entire course, from source to confluence, lies within Bihar's own borders"),
  ("bs1-064", "It is the only south Bihar river that remains perennial through the dry season",
              "It is the south Bihar river most frequently cited as remaining perennial right through the dry season"),

  ("bs1-065", "The Bagmati", "The Bagmati (a Kosi tributary)"),
  ("bs1-065", "The Kamla", "The Kamla (a Kosi tributary)"),
  ("bs1-065", "The Burhi Gandak", "The Burhi Gandak (flows entirely within Bihar)"),

  ("bs1-066", "These rivers are entirely man-made canal systems built during the Mughal period",
              "These rivers are entirely man-made canal systems, first engineered and built during the Mughal period"),
  ("bs1-066", "These rivers only began flowing after the Himalaya had fully formed, following the path of least resistance around it",
              "These rivers began flowing well after the Himalaya had fully formed, simply following the path of least resistance around it"),
  ("bs1-066", "These rivers reverse their flow direction seasonally depending on monsoon intensity",
              "These rivers are believed to reverse their flow direction seasonally, depending on monsoon intensity each year"),

  ("bs1-069", "Residual heat from ancient volcanic activity beneath the Dharwar rock system",
              "Residual heat left over from ancient volcanic activity deep beneath the Dharwar rock system formation"),
  ("bs1-069", "Direct surface heating of shallow groundwater by unusually intense sunlight in these specific valleys",
              "Direct surface heating of shallow groundwater pools by unusually intense sunlight specific to these narrow valley locations"),
  ("bs1-069", "Underground coal-seam combustion left over from historical mining activity",
              "Underground coal-seam combustion, a leftover effect from historical mining activity in these hills"),

  ("bs1-072", "A tropical rainforest climate with no distinct dry season",
              "A tropical rainforest climate typically found near the equator, with no distinct dry season at all"),
  ("bs1-072", "A cold desert climate with minimal annual rainfall",
              "A cold desert climate characterised by extremely minimal annual rainfall throughout the year"),
  ("bs1-072", "A humid subtropical climate with wet winters and dry summers",
              "A humid subtropical climate defined by comparatively wet winters and notably dry summers"),

  ("bs1-073", "It marks the peak of the hot, dry 'Loo' winds that damage standing summer crops",
              "It marks the seasonal peak of the hot, dry 'Loo' winds that typically damage standing summer crops"),
  ("bs1-073", "It marks the onset of winter cold waves driven by the Siberian High",
              "It marks the seasonal onset of winter cold waves driven southward by the Siberian High-pressure system"),

  ("bs1-080", "Is India's only region growing maize as a purely rain-fed Kharif crop with no winter cultivation at all",
              "Is India's leading region growing maize as a purely rain-fed Kharif crop, without any real winter cultivation"),
  ("bs1-080", "Grows the only frost-resistant maize variety cultivated anywhere in eastern India",
              "Grows a distinct frost-resistant maize variety not cultivated anywhere else in eastern India"),
  ("bs1-080", "Is the sole source of maize seed stock distributed to the rest of the state",
              "Is officially designated as the sole source of maize seed stock distributed across the rest of the state"),

  ("bs1-081", "A dense cluster confined entirely to a single district, Rohtas",
              "A dense cluster of mineral deposits confined entirely to the single district of Rohtas"),
  ("bs1-081", "A north-to-south belt running along the Nepal border districts",
              "A north-to-south mineral belt running specifically along Bihar's Nepal-border districts"),
  ("bs1-081", "Scattered deposits with no discernible geographic pattern at all",
              "Scattered, isolated mineral deposits that follow no discernible geographic pattern at all"),

  ("bs1-082", "Mica, used for electrical insulation", "Mica, primarily used for electrical insulation in manufacturing"),
  ("bs1-082", "Bauxite, used as the primary ore for aluminium", "Bauxite, used as the primary raw ore for producing aluminium metal"),
  ("bs1-082", "Quartz, used in glassmaking and ceramics", "Quartz, used mainly in glassmaking and fine ceramics production"),
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
    print("MISSING:")
    for ref, old in missing:
        print(f"  {ref}: {old[:80]}")

json.dump(data, open('bihar_special_batch_02_geography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
