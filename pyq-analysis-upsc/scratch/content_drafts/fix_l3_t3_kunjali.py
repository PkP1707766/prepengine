# -*- coding: utf-8 -*-
"""Level 3 Test 3: the Kunjali Marakkars MCQ's whole answer (naval commanders of the Zamorin) is stated in the
explanation of the published Level-2 row medieval-tuhfat-ul-mujahidin, so a student who read that review would find
it already answered. Replaced by the Dadu Panth (same cell: Medieval, medium MCQ, key (d)). Edits gs_l3_t3_b.py in
place and writes fix_l3_t3_kunjali.sql, which rewrites the draft row in place."""
import contextlib, importlib, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "l3_tools"))
from swap_block import swap

OLD, NEW = "l3-t3-his-kunjali-marakkars", "l3-t3-his-dadu-panth-rajasthan"
if '"' + OLD + '"' in io.open(os.path.join(HERE, "gs_l3_t3_b.py"), encoding="utf-8").read():
    swap("gs_l3_t3_b.py", OLD, '''
M("Medieval", "medium",
  "The Dadu Panth, a sect of nirguna bhakti whose founder's verses were collected as the 'Dadu Vani', took root mainly in:",
  "दादू पंथ, निर्गुण भक्ति का एक संप्रदाय जिसके संस्थापक के पद 'दादू वाणी' में संकलित हुए, मुख्यतः कहाँ जड़ें जमा सका?",
  ["Bengal", "Maharashtra", "Punjab", "Rajasthan"],
  ["बंगाल", "महाराष्ट्र", "पंजाब", "राजस्थान"],
  3,
  "Dadu Dayal (1544-1603), a cotton-carder by tradition, spent most of his life in Rajasthan -- at Sambhar, Amber and finally Naraina near Jaipur, which remains the seat of the Dadu Panth; like Kabir, whom he revered, he rejected idol worship, caste distinctions and ritual, and taught devotion to a formless God in the language of the people. "
  "His disciples Rajjab and Sundardas carried the teaching further and compiled his verses; the sect later also kept a body of armed 'naga' ascetics who served Rajput rulers. Bengal's great bhakti movement was the Vaishnavism of Chaitanya, Maharashtra's the Varkari tradition, and Punjab's the teaching of Guru Nanak.",
  "दादू दयाल (1544-1603), परंपरा के अनुसार धुनिया, ने अपना अधिकांश जीवन राजस्थान में बिताया -- सांभर, आमेर और अंत में जयपुर के पास नराणा में, जो आज भी दादू पंथ का केंद्र है; कबीर की तरह, जिनका वे आदर करते थे, उन्होंने मूर्ति-पूजा, जाति-भेद और कर्मकांड को अस्वीकार किया, और लोकभाषा में निराकार ईश्वर की भक्ति सिखाई। "
  "उनके शिष्यों रज्जब और सुंदरदास ने शिक्षा को आगे बढ़ाया और उनके पद संकलित किए; बाद में संप्रदाय ने सशस्त्र 'नागा' साधुओं का एक दल भी रखा जो राजपूत शासकों की सेवा करता था। बंगाल का महान भक्ति आंदोलन चैतन्य का वैष्णववाद था, महाराष्ट्र का वारकरी परंपरा, और पंजाब का गुरु नानक की शिक्षा।",
  TH2 + ", 'Bhakti-Sufi Traditions'; " + OP2 + ".",
  "l3-t3-his-dadu-panth-rajasthan", pos=3, craft="recall")
''')

import draft_common as d
d.write = lambda name: None
d.ROWS.clear(); d.CGS.clear(); d.CELLS.clear(); d.SPREAD.clear(); d._mcq_n[0] = 0
with contextlib.redirect_stdout(io.StringIO()):
    importlib.import_module("gs_l3_t3_b")
rows = [r for r in d.ROWS if r["concept_group_id"] == NEW]
assert len(rows) == 1
d.ROWS[:] = rows
d.write_updates("fix_l3_t3_kunjali.sql", replaces={NEW: OLD})
