# -*- coding: utf-8 -*-
"""Cross-question cue found while drafting Test 5: the existing MCQ modern-vande-mataram-anandamath
names Bankim Chandra as the author of 'Vande Mataram', which gave away statement 2 of
modern-swadeshi-movement-1905 ("composed by Rabindranath Tagore"). The statement now tests
Tagore's 'Amar Sonar Bangla' instead; the row is in no published test."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rewrite_common import S, write
from polity_common import C3

S("10188259-abec-4802-867f-08149ba2cab6", "Modern", "medium",
  "Consider the following statements regarding the Swadeshi movement that followed the partition of Bengal:",
  "बंगाल विभाजन के बाद चले स्वदेशी आंदोलन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The boycott of British goods was formally proclaimed at a meeting in the Calcutta Town Hall on 7 August 1905.",
   "'Amar Sonar Bangla', which Rabindranath Tagore wrote during the movement, later became the national anthem of Bangladesh.",
   "The National Council of Education, set up during the movement, promoted Western-style education under government control."],
  ["7 अगस्त 1905 को कलकत्ता टाउन हॉल की एक सभा में ब्रिटिश माल के बहिष्कार की औपचारिक घोषणा की गई।",
   "रवींद्रनाथ टैगोर द्वारा आंदोलन के दौरान लिखा गया 'आमार सोनार बांग्ला' बाद में बांग्लादेश का राष्ट्रगान बना।",
   "आंदोलन के दौरान स्थापित राष्ट्रीय शिक्षा परिषद ने सरकारी नियंत्रण में पश्चिमी ढंग की शिक्षा को बढ़ावा दिया।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Swadeshi movement was formally launched at the Calcutta Town Hall meeting of 7 August 1905, where the boycott resolution was passed, before the partition took effect on 16 October 1905. Tagore wrote 'Amar Sonar Bangla' in 1905 for the agitation against the partition, and on 16 October he led the tying of rakhis as a symbol of unity; the song became Bangladesh's national anthem in 1971. "
  "Statement 3 is incorrect: the National Council of Education (1906) was set up to give education on national lines, independent of government control, and led to the Bengal National College with Aurobindo Ghosh as principal.",
  "कथन 1 और 2 सही हैं। स्वदेशी आंदोलन की औपचारिक शुरुआत 7 अगस्त 1905 को कलकत्ता टाउन हॉल की सभा में हुई, जहाँ बहिष्कार का प्रस्ताव पारित हुआ; यह 16 अक्टूबर 1905 को विभाजन लागू होने से पहले की बात है। टैगोर ने 1905 में विभाजन-विरोधी आंदोलन के लिए 'आमार सोनार बांग्ला' लिखा, और 16 अक्टूबर को एकता के प्रतीक के रूप में राखी बाँधने का नेतृत्व किया; यह गीत 1971 में बांग्लादेश का राष्ट्रगान बना। "
  "कथन 3 गलत है: राष्ट्रीय शिक्षा परिषद (1906) की स्थापना सरकारी नियंत्रण से स्वतंत्र, राष्ट्रीय ढंग की शिक्षा देने के लिए हुई, और इसी से बंगाल नेशनल कॉलेज बना, जिसके प्राचार्य अरविंद घोष थे।",
  "Bipan Chandra et al., India's Struggle for Independence -- chapter on the Swadeshi movement; Bipan Chandra, History of Modern India (Orient BlackSwan) -- chapter on the struggle of 1905-1918.",
  "modern-swadeshi-movement-1905")

if __name__ == "__main__":
    write("hist_l2_t5_crosscue_fix.sql")
