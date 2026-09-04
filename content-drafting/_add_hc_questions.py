# -*- coding: utf-8 -*-
import json

data = json.load(open('bihar_special_batch_01_history_culture.json', encoding='utf-8'))

new_qs = [
{"batch_ref":"bs1-101","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"medium",
 "body":"Somapura Mahavihara, one of the great Buddhist monastic universities of the Pala era, was founded by which ruler whose empire was centred on Bihar?",
 "options":[
   {"body":"Gopala", "isCorrect": False},
   {"body":"Dharmapala", "isCorrect": True},
   {"body":"Devapala", "isCorrect": False},
   {"body":"Ramapala", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Dharmapala, the most expansionist Pala ruler, founded Somapura Mahavihara (now in present-day Bangladesh) in addition to Vikramshila -- a reminder that the Pala empire, though centred on Bihar, extended its Buddhist patronage well beyond the region's present borders.",
 "concept_group_id":"bs1-hc-somapura-dharmapala",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-102","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"medium",
 "body":"The Bihari Students' Conference, founded in 1906, is significant in Bihar's freedom movement chiefly because it was:",
 "options":[
   {"body":"The first organisation to demand full independence rather than dominion status", "isCorrect": False},
   {"body":"India's first such body to specifically mobilise students for political goals, later training many future freedom fighters", "isCorrect": True},
   {"body":"A purely literary society with no political activity until the 1940s", "isCorrect": False},
   {"body":"Founded by the British administration to channel student energy away from politics", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Founded by Dr. Rajendra Prasad in 1906 during the Swadeshi era, the Bihari Students' Conference was one of India's first bodies specifically organised to mobilise students for political goals, and became a training ground for a generation of Bihar's later freedom fighters across the Gandhian and revolutionary movements alike.",
 "concept_group_id":"bs1-hc-bihari-students-conference",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-103","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"medium",
 "body":"The 'Panjpariya' cult, a distinctive feature of Bihar's medieval religious landscape, is notable for which characteristic?",
 "options":[
   {"body":"It was a strictly Sufi practice confined entirely to Bihar Sharif's Firdausi order", "isCorrect": False},
   {"body":"It involved joint worship of '5 Pirs' by both Hindus and Muslims, a genuinely syncretic tradition", "isCorrect": True},
   {"body":"It was a Vaishnavite reform movement that rejected all forms of image worship", "isCorrect": False},
   {"body":"It emerged only after independence as a state-sponsored communal-harmony initiative", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"The Panjpariya cult centred on the joint worship of '5 Pirs' by both Hindu and Muslim communities together, making it a genuinely syncretic tradition distinct from the more institutionally separate Sufi silsilas and Bhakti movements that otherwise shaped medieval Bihar's religious life.",
 "concept_group_id":"bs1-hc-panjpariya-cult",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-104","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"hard",
 "body":"Vidyapati, Mithila's most celebrated poet, is usually remembered for his secular court poetry, yet his body of work also carries a genuine devotional dimension. What form did this take?",
 "options":[
   {"body":"Sanskrit hymns composed exclusively for the Karnat royal coronation ceremony", "isCorrect": False},
   {"body":"Nachari songs devoted to Shiva, which helped build a lasting Mithila bhakti tradition alongside his court poetry", "isCorrect": True},
   {"body":"A prose commentary on the Bhagavad Gita commissioned by the Oinwar dynasty", "isCorrect": False},
   {"body":"Devotional paintings rather than poetry, created in his final years as a monk", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Alongside his famous Radha-Krishna court poetry (Padavali) and secular works like Kirtilata, Vidyapati also composed Nachari songs devoted to Shiva -- a genuinely devotional strand of his output that helped establish a lasting bhakti culture in Mithila, distinct from, and often overlooked beside, his better-known secular and courtly reputation.",
 "concept_group_id":"bs1-hc-vidyapati-nachari-bhakti",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-105","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"hard",
 "body":"Maner Sharif, Bihar's oldest major Sufi centre, is home to two distinct dargahs. Which pairing correctly identifies them?",
 "options":[
   {"body":"'Badi Dargah', the larger shrine, and 'Chhoti Dargah', the tomb of Makhdum Daulat", "isCorrect": True},
   {"body":"'Firdausi Dargah' and 'Suhrawardi Dargah', named for the two rival Sufi orders based there", "isCorrect": False},
   {"body":"A single dargah known by two alternate names depending on the season of pilgrimage", "isCorrect": False},
   {"body":"'Sharfuddin Dargah' and 'Bihar Sharif Dargah', both dedicated to the same saint at different life stages", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Maner Sharif houses two genuinely distinct dargahs: the larger 'Badi Dargah', and the 'Chhoti Dargah' (Makhdum Daulat's tomb, built 1616 under Ibrahim Khan) -- a pairing frequently confused for a single shrine, when in fact both stand at the same site under different names and separate histories.",
 "concept_group_id":"bs1-hc-maner-sharif-two-dargahs",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-106","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"hard",
 "body":"Patna Qalam, a distinct miniature-painting style that flourished under British patronage, differs from Madhubani painting in a fundamental way. What is it?",
 "options":[
   {"body":"Patna Qalam used only natural pigments, while Madhubani has always used synthetic dyes", "isCorrect": False},
   {"body":"Patna Qalam focused on everyday scenes of common people, such as washermen and fish-sellers, rather than the religious and royal themes typical of Madhubani", "isCorrect": True},
   {"body":"Patna Qalam was practised exclusively by women, while Madhubani was historically a male-only tradition", "isCorrect": False},
   {"body":"Patna Qalam originated centuries before Madhubani and directly inspired its later development", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Patna Qalam (also called the 'Company School', flourishing under British patronage, associated with artists like Sewak Ram and Hulas Lal) broke from Madhubani's religious and royal themes to focus instead on everyday scenes -- washermen, fish-sellers, common trades -- making it a genuinely distinct painting tradition rather than a regional variant of Madhubani.",
 "concept_group_id":"bs1-hc-patna-qalam-vs-madhubani","source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-107","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"hard",
 "body":"Rohtasgarh Fort, on the Kaimur plateau, illustrates a rare instance of strategic continuity across two very different ruling periods. Which two figures both relied on it as a key stronghold?",
 "options":[
   {"body":"Ashoka and Chandragupta II, as a Mauryan-Gupta frontier post", "isCorrect": False},
   {"body":"Sher Shah Suri and, later, the Mughal governor Raja Man Singh", "isCorrect": True},
   {"body":"Bakhtiyar Khilji and Qutbuddin Aibak, as their first joint base in Bihar", "isCorrect": False},
   {"body":"Kunwar Singh and Jayaprakash Narayan, as successive centres of anti-British resistance", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Rohtasgarh Fort was seized by Sher Shah Suri as his most secure stronghold in the 16th century, and was later separately reinforced and relied upon by Raja Man Singh, Akbar's governor of Bihar -- a genuine continuity of strategic use across the Sur and Mughal periods, despite the very different political contexts.",
 "concept_group_id":"bs1-hc-rohtasgarh-sher-shah-man-singh",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-108","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"hard",
 "body":"The Golghar in Patna, built in 1786 by Captain John Garstin after the 1770 famine, carries a notable irony alongside its distinctive twin spiral staircases. What is it?",
 "options":[
   {"body":"It was built facing the wrong direction for effective grain loading, and had to be structurally modified within a decade", "isCorrect": False},
   {"body":"Despite being purpose-built as an emergency grain store to prevent future famine, it was never actually used for that emergency purpose", "isCorrect": True},
   {"body":"It was originally designed as a fort and only converted into a granary after construction had already finished", "isCorrict": False} if False else {"body":"It was originally designed as a fort and only converted into a granary after construction had already finished", "isCorrect": False},
   {"body":"Its twin staircases were added only in the 20th century as a tourist modification, not part of the original design", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"The Golghar's beehive-shaped design, with its distinctive twin spiral staircases to the top, was purpose-built as an emergency grain store following the catastrophic 1770 Bengal famine -- yet it was, notably, never actually used for that intended emergency purpose, an irony often noted alongside its engineering.",
 "concept_group_id":"bs1-hc-golghar-irony-never-used",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},

{"batch_ref":"bs1-109","subject":"Bihar-Specific","topic":"History & Culture","type":"mcq","difficulty":"hard",
 "body":"Nalanda's continued upkeep under the Pala dynasty involved an unusual diplomatic gesture from outside the Indian subcontinent. What was it?",
 "options":[
   {"body":"The Tibetan king Songtsen Gampo funded a permanent Nalanda library wing", "isCorrect": False},
   {"body":"Sumatra's king Balaputradeva requested, and was granted, a 5-village land grant specifically to fund Nalanda's upkeep", "isCorrect": True},
   {"body":"The Chinese Tang court sent an annual shipment of silk to sustain Nalanda's monks", "isCorrect": False},
   {"body":"Sri Lanka's ruling dynasty sent a delegation of monks to permanently administer Nalanda on Dharmapala's behalf", "isCorrect": False}],
 "marks_correct":1,"marks_wrong":0.33,
 "explanation":"Sumatra's king Balaputradeva (of the Srivijaya empire) requested a grant of five villages specifically to fund Nalanda's upkeep, and Dharmapala granted it -- a genuine Southeast Asian diplomatic link illustrating Nalanda's reach as an international Buddhist institution even while under Pala patronage.",
 "concept_group_id":"bs1-hc-nalanda-balaputradeva-grant",
 "source_citation":"Perfection IAS (Dhananjay IAS), Bihar Special Orange Book","status":"draft"},
]

# fix accidental typo key from a paste slip
for q in new_qs:
    for o in q['options']:
        if 'isCorrict' in o:
            o['isCorrect'] = o.pop('isCorrict')

assert len(new_qs) == 9
diffs = [q['difficulty'] for q in new_qs]
assert diffs.count('medium') == 3 and diffs.count('hard') == 6, diffs

data['questions'].extend(new_qs)
data['meta']['total_questions'] = len(data['questions'])
data['meta']['target_cells'] = {
    "Bihar_History & Culture_easy_mcq": 2,
    "Bihar_History & Culture_medium_mcq": 33,
    "Bihar_History & Culture_hard_mcq": 25,
    "Bihar_History & Culture_hard_statement_based": 1,
    "Bihar_History & Culture_hard_match_the_following": 1
}
data['meta']['batch'] = 'Bihar Special Paper I, Batch 01 (History & Culture topic, rebalanced 62-question allocation -- 53 original + 9 added after the Economy-shortfall rebalance)'

json.dump(data, open('bihar_special_batch_01_history_culture.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('total now:', len(data['questions']))
