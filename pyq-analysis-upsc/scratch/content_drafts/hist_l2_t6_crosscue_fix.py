# -*- coding: utf-8 -*-
"""Cross-question cues found while drafting Test 6, fixed in place (the row is in no published
test): ancient-harshavardhana stated that Fa-Hien visited Harsha's court, which the
Harsha-assemblies row (Hiuen Tsang honoured at Kanauj) and the Fa-Hien row (reign of
Chandragupta II) gave away, and it repeated the Harshacharita fact already tested in
ancient-texts-authors-pairs. Statements 1 and 2 now test the move to Kanauj and the dynasty."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rewrite_common import S, write
from polity_common import C3

S("d6291cea-17d1-42ae-b885-a3767577c2fb", "Ancient", "medium",
  "Consider the following statements regarding Harshavardhana:",
  "हर्षवर्धन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Harsha moved his capital from Thanesar to Kanauj.",
   "Harsha belonged to the Maukhari dynasty.",
   "Harsha was decisively defeated by the Chalukya ruler Pulakeshin II on the banks of the river Narmada."],
  ["हर्ष ने अपनी राजधानी थानेसर से कन्नौज स्थानांतरित की।",
   "हर्ष मौखरि वंश के थे।",
   "चालुक्य शासक पुलकेशिन द्वितीय ने नर्मदा नदी के तट पर हर्ष को निर्णायक रूप से पराजित किया।"],
  C3, 1,
  "Statements 1 and 3 are correct. After his brother Rajyavardhana was killed and his sister Rajyashri's husband, the Maukhari king Grahavarman of Kanauj, died, Harsha took over Kanauj and made it his capital -- the start of its long career as the prize of north Indian politics. The Aihole inscription of Pulakeshin II records Harsha's defeat on the Narmada, which fixed the southern limit of his power. "
  "Statement 2 is the trap: Harsha was of the Pushyabhuti (Vardhana) dynasty of Thanesar; the Maukharis were his sister's in-laws, whose kingdom he absorbed.",
  "कथन 1 और 3 सही हैं। उनके भाई राज्यवर्धन की हत्या और उनकी बहन राज्यश्री के पति, कन्नौज के मौखरि राजा ग्रहवर्मन, की मृत्यु के बाद हर्ष ने कन्नौज अपने हाथ में लेकर उसे राजधानी बनाया; यहीं से उत्तर भारतीय राजनीति के पुरस्कार के रूप में कन्नौज का लंबा दौर शुरू हुआ। पुलकेशिन द्वितीय का ऐहोल अभिलेख नर्मदा पर हर्ष की पराजय दर्ज करता है, जिसने उसकी शक्ति की दक्षिणी सीमा तय कर दी। "
  "कथन 2 जाल है: हर्ष थानेसर के पुष्यभूति (वर्धन) वंश के थे; मौखरि उनकी बहन के ससुराल वाले थे, जिनका राज्य उन्होंने अपने में मिला लिया।",
  "R.S. Sharma, India's Ancient Past; Upinder Singh, A History of Ancient and Early Medieval India, chapter 10.",
  "ancient-harshavardhana")

if __name__ == "__main__":
    write("hist_l2_t6_crosscue_fix.sql")
