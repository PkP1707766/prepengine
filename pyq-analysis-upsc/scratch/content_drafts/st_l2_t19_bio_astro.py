# -*- coding: utf-8 -*-
"""Level 2 · Test 19 (Science & Technology 1: General Science) -- Biology, Health & Biotechnology (19) and
Astronomy & Earth Science (29).
  Biology: medium statement 8, easy statement 3, hard statement 2, medium MCQ 3, easy MCQ 1, hard MCQ 1,
    medium Statement-I/II 1.
  Astronomy & Earth: medium statement 12, easy statement 4, hard statement 4, medium MCQ 4, medium
    Statement-I/II 2, easy Statement-I/II 1, easy MCQ 1, hard MCQ 1.
Nipah and fruit bats, deep-sea mining of polymetallic nodules and ozone are Environment; the Earth's interior,
seismic waves, tides, the atmosphere's layers and scattering are Geography. Space missions (Chandrayaan,
Aditya-L1, Gaganyaan) are left for Test 20; this file keeps to the science of stars, planets and space weather."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
BI = "Biology, Health & Biotechnology"
AS = "Astronomy & Earth Science"
NBI = "NCERT Biology, Classes XI-XII"
NSC = "NCERT Science, Classes VIII-X"
NOBEL = "The Nobel Prize -- official press releases"
NASA = "NASA Science"

# ================================================================ BIOLOGY: MEDIUM STATEMENTS (8)
S(BI, "medium", "Consider the following statements about the Wolbachia method of controlling dengue:",
  "डेंगू नियंत्रण की वोल्बाचिया विधि के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Aedes mosquitoes carrying Wolbachia are less able to transmit viruses such as dengue.",
   "Wolbachia is a virus.",
   "The method releases Wolbachia-carrying mosquitoes so that they gradually replace the wild population."],
  ["वोल्बाचिया वाले एडीज़ मच्छर डेंगू जैसे विषाणुओं को फैलाने में कम सक्षम होते हैं।",
   "वोल्बाचिया एक विषाणु है।",
   "इस विधि में वोल्बाचिया वाले मच्छर छोड़े जाते हैं ताकि वे धीरे-धीरे जंगली आबादी का स्थान ले लें।"],
  C3, 1,
  "Statements 1 and 3 are correct: the bacterium blocks the virus from multiplying inside the mosquito, and because infected females pass it to all their young, it spreads through the population on its own. "
  "Statement 2 is wrong: Wolbachia is a bacterium that lives naturally in many insects -- the method uses no genetic modification. India's ICMR has developed Wolbachia strains of Aedes aegypti at its Puducherry centre.",
  "कथन 1 और 3 सही हैं: यह जीवाणु मच्छर के भीतर विषाणु को बढ़ने से रोकता है, और चूँकि संक्रमित मादाएँ इसे अपनी सभी संतानों को दे देती हैं, यह स्वयं ही आबादी में फैल जाता है। "
  "कथन 2 गलत है: वोल्बाचिया एक जीवाणु है जो कई कीटों में प्राकृतिक रूप से रहता है; इस विधि में कोई आनुवंशिक संशोधन नहीं होता। भारत के ICMR ने अपने पुडुचेरी केंद्र में एडीज़ इजिप्टी के वोल्बाचिया स्ट्रेन विकसित किए हैं।",
  "World Mosquito Program; Indian Council of Medical Research -- Vector Control Research Centre.",
  "bi-wolbachia")

S(BI, "medium", "Consider the following statements about mRNA vaccines:",
  "mRNA टीकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They instruct the body's cells to make a viral protein that trains the immune system.",
   "The mRNA is carried into cells inside tiny fat droplets called lipid nanoparticles.",
   "The 2023 Nobel Prize in Physiology or Medicine was awarded for discoveries that made them possible."],
  ["ये शरीर की कोशिकाओं को एक विषाणु प्रोटीन बनाने का निर्देश देते हैं, जो प्रतिरक्षा प्रणाली को प्रशिक्षित करता है।",
   "mRNA को लिपिड नैनोकण कहलाने वाली छोटी वसा बूँदों के भीतर कोशिकाओं तक पहुँचाया जाता है।",
   "फ़िज़ियोलॉजी या मेडिसिन का 2023 का नोबेल पुरस्कार उन खोजों के लिए दिया गया जिन्होंने इन्हें संभव बनाया।"],
  C3, 2,
  "All three statements are correct. Katalin Karikó and Drew Weissman found that modifying the building blocks of mRNA stops the body from treating it as an intruder, which made the COVID-19 vaccines possible. The mRNA never enters the cell nucleus and cannot change a person's DNA; it breaks down within days.",
  "तीनों कथन सही हैं। कैटलिन कारिको और ड्रयू वीसमैन ने पाया कि mRNA के निर्माण खंडों को बदलने से शरीर उसे घुसपैठिया नहीं मानता; इसी ने COVID-19 के टीके संभव बनाए। mRNA कभी कोशिका के केंद्रक में नहीं जाता और किसी व्यक्ति का DNA नहीं बदल सकता; यह कुछ दिनों में टूट जाता है।",
  f"{NOBEL} (Physiology or Medicine, 2023); World Health Organization.",
  "bi-mrna-vaccines")

S(BI, "medium", "Consider the following statements about Nobel Prizes in Physiology or Medicine:",
  "फ़िज़ियोलॉजी या मेडिसिन के नोबेल पुरस्कारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 2024 prize was awarded for the discovery of microRNA and its role in gene regulation.",
   "The 2025 prize was awarded for discoveries about peripheral immune tolerance.",
   "The 2020 prize in this category was awarded for the gene-editing tool CRISPR-Cas9."],
  ["2024 का पुरस्कार माइक्रोRNA और जीन नियमन में उसकी भूमिका की खोज के लिए दिया गया।",
   "2025 का पुरस्कार परिधीय प्रतिरक्षा सहिष्णुता (peripheral immune tolerance) से संबंधित खोजों के लिए दिया गया।",
   "इस श्रेणी में 2020 का पुरस्कार जीन-संपादन उपकरण CRISPR-Cas9 के लिए दिया गया।"],
  C3, 1,
  "Statements 1 and 2 are correct: Victor Ambros and Gary Ruvkun were honoured in 2024, and Mary Brunkow, Fred Ramsdell and Shimon Sakaguchi in 2025 for identifying regulatory T cells, which stop the immune system from attacking the body. "
  "Statement 3 is wrong: CRISPR-Cas9 won Emmanuelle Charpentier and Jennifer Doudna the 2020 Nobel Prize in Chemistry; the 2020 medicine prize was for the discovery of the hepatitis C virus.",
  "कथन 1 और 2 सही हैं: 2024 में विक्टर एम्ब्रोस और गैरी रुवकुन को, और 2025 में मैरी ब्रंको, फ़्रेड रैम्सडेल और शिमोन साकागुची को नियामक T कोशिकाओं की पहचान के लिए सम्मानित किया गया, जो प्रतिरक्षा प्रणाली को शरीर पर हमला करने से रोकती हैं। "
  "कथन 3 गलत है: CRISPR-Cas9 के लिए इमैनुएल शार्पेंतिये और जेनिफ़र डाउडना को 2020 का रसायन विज्ञान का नोबेल मिला; 2020 का चिकित्सा पुरस्कार हेपेटाइटिस C विषाणु की खोज के लिए था।",
  f"{NOBEL} (Physiology or Medicine, 2020, 2024 and 2025; Chemistry, 2020).",
  "bi-nobel-medicine-recent")

S(BI, "medium", "Consider the following statements about monoclonal antibodies:",
  "एकक्लोनी प्रतिरक्षियों (monoclonal antibodies) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are identical antibodies produced by cells descended from a single clone.",
   "They are used to treat some cancers and autoimmune diseases.",
   "They are a type of antibiotic that kills bacteria directly.",
   "They were first produced with hybridoma technology, which fuses antibody-making cells with cancerous myeloma cells."],
  ["ये एक ही क्लोन से उत्पन्न कोशिकाओं द्वारा बनाई गई समान प्रतिरक्षियाँ हैं।",
   "इनका उपयोग कुछ कैंसरों और स्व-प्रतिरक्षी रोगों के उपचार में होता है।",
   "ये एक प्रकार की प्रतिजैविक (antibiotic) हैं जो जीवाणुओं को सीधे मारती हैं।",
   "इन्हें पहली बार हाइब्रिडोमा तकनीक से बनाया गया, जिसमें प्रतिरक्षी बनाने वाली कोशिकाओं को कैंसरयुक्त मायलोमा कोशिकाओं से जोड़ा जाता है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct: because every molecule targets the same site on an antigen, monoclonals can block a cancer cell's growth signal or an inflammatory molecule, and are also used in rapid diagnostic tests. The myeloma partner makes the fused cells multiply without end. "
  "Statement 3 is wrong: they are proteins of the immune system, not antibiotics.",
  "कथन 1, 2 और 4 सही हैं: चूँकि हर अणु प्रतिजन के एक ही स्थान को लक्ष्य बनाता है, एकक्लोनी प्रतिरक्षियाँ कैंसर कोशिका के वृद्धि संकेत या किसी सूजनकारी अणु को रोक सकती हैं, और त्वरित नैदानिक परीक्षणों में भी प्रयुक्त होती हैं। मायलोमा साथी जुड़ी हुई कोशिकाओं को अनंत रूप से गुणित होने देता है। "
  "कथन 3 गलत है: ये प्रतिरक्षा प्रणाली के प्रोटीन हैं, प्रतिजैविक नहीं।",
  f"{NBI} -- Human Health and Disease; Biotechnology and its Applications.",
  "bi-monoclonal-antibodies",
  closing="How many of the above statements are correct?",
  closing_hi="उपर्युक्त में से कितने कथन सही हैं?")

S(BI, "medium", "Consider the following statements about new therapies:",
  "नई चिकित्सा पद्धतियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Casgevy, approved in 2023, was the first CRISPR-based therapy, for sickle cell disease and beta thalassaemia.",
   "CAR-T cell therapy re-engineers a patient's own immune cells to attack cancer.",
   "India approved its first indigenous CAR-T cell therapy in 2023."],
  ["2023 में स्वीकृत कैसजेवी (Casgevy) सिकल सेल रोग और बीटा थैलेसीमिया के लिए पहली CRISPR-आधारित चिकित्सा थी।",
   "CAR-T कोशिका चिकित्सा रोगी की अपनी प्रतिरक्षा कोशिकाओं को कैंसर पर हमला करने के लिए पुनः अभियांत्रित करती है।",
   "भारत ने 2023 में अपनी पहली स्वदेशी CAR-T कोशिका चिकित्सा को स्वीकृति दी।"],
  C3, 2,
  "All three statements are correct. Casgevy edits a patient's blood stem cells so that they make fetal haemoglobin again, relieving the disease; CAR-T cells are T cells given a receptor that recognises a cancer. India's NexCAR19, developed by IIT Bombay and Tata Memorial Centre for certain blood cancers, costs a fraction of imported therapies.",
  "तीनों कथन सही हैं। कैसजेवी रोगी की रक्त स्टेम कोशिकाओं को संपादित करती है ताकि वे फिर से भ्रूणीय हीमोग्लोबिन बनाएँ, जिससे रोग में राहत मिलती है; CAR-T कोशिकाएँ वे T कोशिकाएँ हैं जिन्हें कैंसर पहचानने वाला ग्राही दिया जाता है। कुछ रक्त कैंसरों के लिए IIT बॉम्बे और टाटा मेमोरियल सेंटर द्वारा विकसित भारत की NexCAR19 आयातित चिकित्साओं की तुलना में बहुत सस्ती है।",
  "Central Drugs Standard Control Organisation; IIT Bombay; US Food and Drug Administration (2023).",
  "bi-crispr-car-t")

S(BI, "medium", "Consider the following statements about antimicrobial resistance:",
  "प्रतिरोगाणुक प्रतिरोध (antimicrobial resistance) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Antibiotics are effective against viral infections such as the common cold.",
   "The heavy use of antibiotics in poultry and livestock contributes to resistance.",
   "Bacteriophages are bacteria that infect viruses."],
  ["प्रतिजैविक (antibiotics) सामान्य ज़ुकाम जैसे विषाणु संक्रमणों के विरुद्ध प्रभावी हैं।",
   "मुर्गी पालन और पशुधन में प्रतिजैविकों का भारी उपयोग प्रतिरोध में योगदान देता है।",
   "बैक्टीरियोफ़ेज वे जीवाणु हैं जो विषाणुओं को संक्रमित करते हैं।"],
  C3, 0,
  "Only statement 2 is correct: antibiotics used to make animals grow faster expose bacteria to low doses, favouring resistant strains that can pass to people. "
  "Statement 1 is wrong: antibiotics act on bacteria, not viruses, and taking them for colds only breeds resistance. "
  "Statement 3 is wrong: bacteriophages are viruses that infect bacteria; 'phage therapy' is being revived to treat infections that antibiotics can no longer cure.",
  "केवल कथन 2 सही है: जानवरों को तेज़ी से बढ़ाने के लिए प्रयुक्त प्रतिजैविक जीवाणुओं को कम मात्रा के संपर्क में लाते हैं, जिससे प्रतिरोधी स्ट्रेन पनपते हैं जो लोगों तक पहुँच सकते हैं। "
  "कथन 1 गलत है: प्रतिजैविक जीवाणुओं पर काम करते हैं, विषाणुओं पर नहीं, और ज़ुकाम के लिए इन्हें लेना केवल प्रतिरोध बढ़ाता है। "
  "कथन 3 गलत है: बैक्टीरियोफ़ेज वे विषाणु हैं जो जीवाणुओं को संक्रमित करते हैं; जिन संक्रमणों को प्रतिजैविक अब ठीक नहीं कर पाते, उनके उपचार के लिए 'फ़ेज चिकित्सा' फिर से अपनाई जा रही है।",
  "World Health Organization -- Antimicrobial resistance; Indian Council of Medical Research -- AMR surveillance.",
  "bi-antimicrobial-resistance")

S(BI, "medium", "Consider the following statements about genomics:",
  "जीनोमिकी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The GenomeIndia project sequenced the genomes of ten lakh Indians.",
   "Microsatellites are long, single-copy genes that code for proteins.",
   "Metagenomics studies the genome of a single organism grown in the laboratory."],
  ["जीनोमइंडिया परियोजना ने दस लाख भारतीयों के जीनोम अनुक्रमित किए।",
   "माइक्रोसैटेलाइट लंबे, एकल-प्रति वाले जीन हैं जो प्रोटीन बनाते हैं।",
   "मेटाजीनोमिकी प्रयोगशाला में उगाए गए एक ही जीव के जीनोम का अध्ययन करती है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: GenomeIndia sequenced about 10,000 genomes from dozens of population groups and released the data in 2025, to map genetic variation for medicine. "
  "Statement 2 is wrong: microsatellites are short DNA sequences repeated many times; the number of repeats varies so much between people that they are used in DNA fingerprinting and in tracing wildlife. "
  "Statement 3 is wrong: metagenomics reads all the DNA in a sample of soil, water, air or gut contents at once, revealing microbes that cannot be grown in a lab.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: जीनोमइंडिया ने दर्जनों जनसंख्या समूहों से लगभग 10,000 जीनोम अनुक्रमित किए और 2025 में आँकड़े जारी किए, ताकि चिकित्सा के लिए आनुवंशिक विविधता का मानचित्र बने। "
  "कथन 2 गलत है: माइक्रोसैटेलाइट छोटे DNA अनुक्रम हैं जो कई बार दोहराए जाते हैं; दोहरावों की संख्या लोगों के बीच इतनी भिन्न होती है कि इनका उपयोग DNA फ़िंगरप्रिंटिंग और वन्यजीवों का पता लगाने में होता है। "
  "कथन 3 गलत है: मेटाजीनोमिकी मिट्टी, पानी, हवा या आँत की सामग्री के किसी नमूने के सारे DNA को एक साथ पढ़ती है, जिससे वे सूक्ष्मजीव सामने आते हैं जिन्हें प्रयोगशाला में उगाया नहीं जा सकता।",
  "Department of Biotechnology -- GenomeIndia; NCERT Biology, Class XII -- Molecular Basis of Inheritance.",
  "bi-genomics-none")

S(BI, "medium", "Consider the following statements about viruses:",
  "विषाणुओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Viruses can multiply only inside living cells.",
   "All viruses have DNA as their genetic material.",
   "Viruses are larger than most bacteria."],
  ["विषाणु केवल जीवित कोशिकाओं के भीतर ही गुणित हो सकते हैं।",
   "सभी विषाणुओं का आनुवंशिक पदार्थ DNA है।",
   "विषाणु अधिकांश जीवाणुओं से बड़े होते हैं।"],
  C3, 0,
  "Only statement 1 is correct: outside a host cell a virus is inert, which is why viruses are said to lie on the border of the living and non-living. "
  "Statement 2 is wrong: many viruses, such as those causing influenza, COVID-19, dengue and HIV, have RNA instead. "
  "Statement 3 is wrong: most viruses are far smaller than bacteria and can be seen only with an electron microscope.",
  "केवल कथन 1 सही है: मेज़बान कोशिका के बाहर विषाणु निष्क्रिय होता है; इसीलिए कहा जाता है कि विषाणु सजीव और निर्जीव की सीमा पर हैं। "
  "कथन 2 गलत है: इन्फ़्लुएंज़ा, COVID-19, डेंगू और HIV पैदा करने वाले जैसे कई विषाणुओं में इसके बजाय RNA होता है। "
  "कथन 3 गलत है: अधिकांश विषाणु जीवाणुओं से कहीं छोटे होते हैं और केवल इलेक्ट्रॉन सूक्ष्मदर्शी से देखे जा सकते हैं।",
  f"{NBI} -- Biological Classification.",
  "bi-viruses")

# ================================================================ BIOLOGY: EASY STATEMENTS (3)
S(BI, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Vaccines help the body build immunity against diseases.",
   "Malaria is spread by mosquitoes."],
  ["टीके शरीर को रोगों के विरुद्ध प्रतिरक्षा बनाने में मदद करते हैं।",
   "मलेरिया मच्छरों से फैलता है।"],
  T2, 2,
  "Both statements are correct: vaccines train the immune system without causing the disease, and malaria is carried from person to person by female Anopheles mosquitoes.",
  "दोनों कथन सही हैं: टीके रोग पैदा किए बिना प्रतिरक्षा प्रणाली को प्रशिक्षित करते हैं, और मलेरिया मादा एनोफ़िलीज़ मच्छरों द्वारा एक व्यक्ति से दूसरे तक पहुँचाया जाता है।",
  f"{NSC} -- Why Do We Fall Ill?",
  "bi-vaccines-malaria-easy")

S(BI, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Red blood cells carry oxygen around the body.",
   "Insulin is produced by the liver."],
  ["लाल रक्त कोशिकाएँ पूरे शरीर में ऑक्सीजन ले जाती हैं।",
   "इंसुलिन यकृत (liver) बनाता है।"],
  T2, 0,
  "Only statement 1 is correct: the haemoglobin in red cells binds oxygen. Statement 2 is wrong: insulin is made by the pancreas; when it is lacking or does not work, blood sugar rises -- diabetes.",
  "केवल कथन 1 सही है: लाल कोशिकाओं का हीमोग्लोबिन ऑक्सीजन से जुड़ता है। कथन 2 गलत है: इंसुलिन अग्न्याशय (pancreas) बनाता है; जब इसकी कमी हो या यह काम न करे, तो रक्त शर्करा बढ़ती है, यानी मधुमेह।",
  f"{NSC} -- Life Processes; Control and Coordination.",
  "bi-rbc-insulin-easy")

S(BI, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A lack of vitamin C causes rickets.",
   "A lack of iodine can cause goitre."],
  ["विटामिन C की कमी से सूखा रोग (rickets) होता है।",
   "आयोडीन की कमी से घेंघा (goitre) हो सकता है।"],
  T2, 1,
  "Only statement 2 is correct: iodine is needed to make thyroid hormones, which is why salt is iodised. Statement 1 is wrong: rickets comes from a lack of vitamin D; a lack of vitamin C causes scurvy.",
  "केवल कथन 2 सही है: थायरॉइड हार्मोन बनाने के लिए आयोडीन चाहिए; इसीलिए नमक को आयोडीनयुक्त किया जाता है। कथन 1 गलत है: सूखा रोग विटामिन D की कमी से होता है; विटामिन C की कमी से स्कर्वी होता है।",
  f"{NSC}; {NBI}.",
  "bi-deficiency-diseases-easy")

# ================================================================ BIOLOGY: HARD STATEMENTS (2)
S(BI, "hard", "Consider the following statements about stem cells:",
  "स्टेम कोशिकाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Induced pluripotent stem cells are made by reprogramming ordinary adult cells.",
   "Embryonic stem cells can develop only into blood cells.",
   "Umbilical cord blood is a source of blood-forming stem cells."],
  ["प्रेरित बहुशक्त (induced pluripotent) स्टेम कोशिकाएँ सामान्य वयस्क कोशिकाओं को पुनः प्रोग्राम करके बनाई जाती हैं।",
   "भ्रूणीय स्टेम कोशिकाएँ केवल रक्त कोशिकाओं में विकसित हो सकती हैं।",
   "गर्भनाल का रक्त (umbilical cord blood) रक्त बनाने वाली स्टेम कोशिकाओं का एक स्रोत है।"],
  C3, 1,
  "Statements 1 and 3 are correct: Shinya Yamanaka showed in 2006 that adding four genes turns skin cells into cells that behave like embryonic ones, which won him a Nobel Prize in 2012; cord blood is banked and used to treat blood disorders. "
  "Statement 2 is wrong: embryonic stem cells are pluripotent -- they can become almost any cell type in the body.",
  "कथन 1 और 3 सही हैं: शिन्या यामानाका ने 2006 में दिखाया कि चार जीन जोड़ने से त्वचा कोशिकाएँ भ्रूणीय कोशिकाओं जैसा व्यवहार करने लगती हैं, जिसके लिए उन्हें 2012 में नोबेल पुरस्कार मिला; गर्भनाल का रक्त संग्रहीत किया जाता है और रक्त विकारों के उपचार में प्रयुक्त होता है। "
  "कथन 2 गलत है: भ्रूणीय स्टेम कोशिकाएँ बहुशक्त होती हैं; वे शरीर की लगभग किसी भी कोशिका में बदल सकती हैं।",
  f"{NOBEL} (Physiology or Medicine, 2012); Indian Council of Medical Research -- National Guidelines for Stem Cell Research.",
  "bi-stem-cells")

S(BI, "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Genetically edited pig kidneys have been transplanted into living human patients.",
   "Organ-on-a-chip devices imitate human organs to test how drugs act on them.",
   "Prions are infectious proteins that cause diseases such as 'mad cow disease'."],
  ["आनुवंशिक रूप से संपादित सूअर के गुर्दे जीवित मानव रोगियों में प्रत्यारोपित किए गए हैं।",
   "ऑर्गन-ऑन-ए-चिप उपकरण मानव अंगों की नक़ल करते हैं ताकि जाँचा जा सके कि दवाएँ उन पर कैसे असर करती हैं।",
   "प्रायॉन संक्रामक प्रोटीन हैं जो 'मैड काउ रोग' जैसे रोग पैदा करते हैं।"],
  C3, 2,
  "All three statements are correct. Since 2024 surgeons in the United States have transplanted pig kidneys, edited to remove sugars that trigger rejection, into living patients. Organ chips, lined with human cells, can reduce the use of animals in drug testing. Prions, which carry no DNA or RNA, make normal proteins misfold and destroy brain tissue.",
  "तीनों कथन सही हैं। 2024 से संयुक्त राज्य अमेरिका में सर्जनों ने अस्वीकृति भड़काने वाली शर्कराओं को हटाने के लिए संपादित सूअर के गुर्दे जीवित रोगियों में लगाए हैं। मानव कोशिकाओं से पंक्तिबद्ध अंग-चिप दवा परीक्षण में जानवरों का उपयोग घटा सकते हैं। प्रायॉन, जिनमें कोई DNA या RNA नहीं होता, सामान्य प्रोटीनों को गलत ढंग से मोड़ते हैं और मस्तिष्क ऊतक नष्ट करते हैं।",
  "World Health Organization; US Food and Drug Administration.",
  "bi-xenotransplant-organ-chip-prions")

# ================================================================ BIOLOGY: MEDIUM MCQs (3)
M(BI, "medium", "A vaccine that uses a harmless, modified virus to carry genetic instructions for a target protein into the body's cells is called a:",
  "जो टीका किसी लक्ष्य प्रोटीन के आनुवंशिक निर्देश शरीर की कोशिकाओं तक पहुँचाने के लिए एक हानिरहित, संशोधित विषाणु का उपयोग करता है, वह क्या कहलाता है?",
  ["viral vector vaccine", "live attenuated vaccine made from a weakened pathogen",
   "inactivated vaccine made from a killed whole pathogen", "toxoid vaccine made from an inactivated bacterial toxin"],
  ["विषाणु वाहक (viral vector) टीका", "कमज़ोर रोगाणु से बना जीवित क्षीणित टीका",
   "मारे गए पूरे रोगाणु से बना निष्क्रिय टीका", "निष्क्रिय किए गए जीवाणु विष से बना टॉक्सॉइड टीका"],
  0,
  "Covishield, for example, used a chimpanzee adenovirus that cannot multiply to deliver the gene for the coronavirus spike protein. Live attenuated vaccines (such as the oral polio vaccine) use a weakened form of the pathogen itself, inactivated vaccines (such as Covaxin) a killed one, and toxoids (tetanus, diphtheria) a neutralised toxin.",
  "उदाहरण के लिए, कोविशील्ड ने कोरोनावायरस स्पाइक प्रोटीन का जीन पहुँचाने के लिए चिंपैंज़ी के ऐसे एडेनोवायरस का उपयोग किया जो गुणित नहीं हो सकता। जीवित क्षीणित टीके (जैसे मुँह से दिया जाने वाला पोलियो टीका) स्वयं रोगाणु के कमज़ोर रूप का, निष्क्रिय टीके (जैसे कोवैक्सिन) मारे गए रोगाणु का, और टॉक्सॉइड (टिटनेस, डिप्थीरिया) निष्प्रभावी विष का उपयोग करते हैं।",
  "World Health Organization -- vaccine types; Central Drugs Standard Control Organisation.",
  "bi-viral-vector-vaccine")

M(BI, "medium", "People with blood group O negative are often called 'universal donors' because their red blood cells:",
  "O नेगेटिव रक्त समूह वाले लोगों को प्रायः 'सार्वभौमिक दाता' कहा जाता है, क्योंकि उनकी लाल रक्त कोशिकाएँ:",
  ["carry none of the A, B or Rh(D) antigens", "carry all of the A, B and Rh(D) antigens on their surface",
   "contain no haemoglobin that could react with the patient's blood", "are produced in the spleen rather than in the bone marrow"],
  ["A, B या Rh(D) में से कोई भी प्रतिजन नहीं रखतीं", "अपनी सतह पर A, B और Rh(D) सभी प्रतिजन रखती हैं",
   "में ऐसा कोई हीमोग्लोबिन नहीं होता जो रोगी के रक्त से प्रतिक्रिया करे", "अस्थि मज्जा के बजाय प्लीहा में बनती हैं"],
  0,
  "With no A, B or Rh(D) antigens, these red cells are not attacked by antibodies in the recipient's plasma, so they can be given in emergencies when the patient's group is not known. AB positive people, who have no anti-A or anti-B antibodies, are 'universal recipients' of red cells.",
  "A, B या Rh(D) प्रतिजन न होने से प्राप्तकर्ता के प्लाज़्मा की प्रतिरक्षियाँ इन लाल कोशिकाओं पर हमला नहीं करतीं, इसलिए रोगी का समूह ज्ञात न होने पर आपात स्थिति में ये दी जा सकती हैं। AB पॉज़िटिव लोग, जिनमें एंटी-A या एंटी-B प्रतिरक्षियाँ नहीं होतीं, लाल कोशिकाओं के 'सार्वभौमिक प्राप्तकर्ता' हैं।",
  f"{NBI} -- Body Fluids and Circulation.",
  "bi-universal-donor")

M(BI, "medium", "Which one of the following diseases is caused by a protozoan?",
  "निम्नलिखित में से कौन-सा रोग एक प्रोटोज़ोआ से होता है?",
  ["Malaria", "Tuberculosis", "Dengue", "Ringworm"],
  ["मलेरिया", "क्षय रोग (TB)", "डेंगू", "दाद (ringworm)"],
  0,
  "Malaria is caused by Plasmodium, a single-celled protozoan parasite, carried by mosquitoes. Tuberculosis is caused by a bacterium, dengue by a virus, and ringworm -- despite its name -- by a fungus.",
  "मलेरिया प्लाज़्मोडियम से होता है, जो मच्छरों द्वारा पहुँचाया जाने वाला एककोशिकीय प्रोटोज़ोआ परजीवी है। क्षय रोग एक जीवाणु से, डेंगू एक विषाणु से, और दाद, अपने अंग्रेज़ी नाम 'ringworm' के बावजूद, एक कवक से होता है।",
  f"{NBI} -- Human Health and Disease.",
  "bi-protozoan-disease")

# ================================================================ BIOLOGY: EASY MCQ (1)
M(BI, "easy", "Which organ pumps blood around the human body?",
  "मानव शरीर में रक्त को कौन-सा अंग पंप करता है?",
  ["Heart", "Lungs", "Kidneys", "Liver"],
  ["हृदय", "फेफड़े", "गुर्दे", "यकृत"],
  0,
  "The heart pumps blood through the arteries; the lungs add oxygen to it, the kidneys filter it, and the liver processes nutrients and removes toxins.",
  "हृदय धमनियों के ज़रिए रक्त पंप करता है; फेफड़े उसमें ऑक्सीजन मिलाते हैं, गुर्दे उसे छानते हैं, और यकृत पोषक तत्वों को संसाधित करता तथा विषैले पदार्थ हटाता है।",
  f"{NSC} -- Life Processes.",
  "bi-heart-easy")

# ================================================================ BIOLOGY: HARD MCQ (1)
M(BI, "hard", "The share of a population that must be immune to stop a disease spreading is roughly 1 - 1/R0, where R0 is the average number of people one case infects in a fully susceptible population. For a disease with R0 = 4, this threshold is about:",
  "किसी रोग का फैलना रोकने के लिए जनसंख्या का जितना हिस्सा प्रतिरक्षित होना चाहिए, वह लगभग 1 - 1/R0 है, जहाँ R0 पूरी तरह संवेदनशील जनसंख्या में एक रोगी से संक्रमित होने वाले लोगों की औसत संख्या है। R0 = 4 वाले रोग के लिए यह सीमा लगभग कितनी है?",
  ["75 per cent", "25 per cent", "40 per cent", "96 per cent"],
  ["75 प्रतिशत", "25 प्रतिशत", "40 प्रतिशत", "96 प्रतिशत"],
  0,
  "1 - 1/4 = 3/4, or 75 per cent. The more contagious a disease, the higher the bar: measles, with an R0 of 12-18, needs over 90 per cent immunity, which is why even small gaps in vaccination cause outbreaks. The 25 per cent option is 1/R0 -- the trap.",
  "1 - 1/4 = 3/4, यानी 75 प्रतिशत। रोग जितना संक्रामक, सीमा उतनी ऊँची: 12-18 के R0 वाले ख़सरे के लिए 90 प्रतिशत से अधिक प्रतिरक्षा चाहिए; इसीलिए टीकाकरण में छोटी कमियाँ भी प्रकोप पैदा करती हैं। 25 प्रतिशत वाला विकल्प 1/R0 है; यही जाल है।",
  "World Health Organization -- Herd immunity.",
  "bi-herd-immunity-threshold")

# ================================================================ BIOLOGY: STATEMENT-I/II (medium 1)
A(BI, "medium",
  "Antibiotic resistance is a growing threat to public health.",
  "प्रतिजैविक प्रतिरोध सार्वजनिक स्वास्थ्य के लिए बढ़ता ख़तरा है।",
  "Resistance arises because individual bacteria learn to avoid antibiotics during their lifetime.",
  "प्रतिरोध इसलिए पैदा होता है कि अलग-अलग जीवाणु अपने जीवनकाल में प्रतिजैविकों से बचना सीख जाते हैं।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Bacteria do not 'learn': random mutations, or genes picked up from other bacteria, happen to protect a few of them, and every course of antibiotics kills the rest and lets the resistant ones multiply -- natural selection at speed. The WHO counts drug-resistant infections among the leading causes of death worldwide.",
  "कथन-I सही है पर कथन-II गलत है। जीवाणु 'सीखते' नहीं: यादृच्छिक उत्परिवर्तन, या दूसरे जीवाणुओं से मिले जीन, संयोग से उनमें से कुछ की रक्षा करते हैं, और प्रतिजैविकों का हर कोर्स शेष को मार देता है और प्रतिरोधी जीवाणुओं को बढ़ने देता है; यह तेज़ गति से होने वाला प्राकृतिक चयन है। WHO दवा-प्रतिरोधी संक्रमणों को विश्व में मृत्यु के प्रमुख कारणों में गिनता है।",
  "World Health Organization -- Antimicrobial resistance; NCERT Biology, Class XII -- Evolution.",
  "bi-amr-natural-selection")

# ================================================================ ASTRONOMY: MEDIUM STATEMENTS (12)
S(AS, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A light-year is a unit of distance.",
   "Light from the Sun takes about eight minutes to reach the Earth.",
   "The nearest star to the Sun is about 4.2 light-years away."],
  ["प्रकाश-वर्ष दूरी की एक इकाई है।",
   "सूर्य के प्रकाश को पृथ्वी तक पहुँचने में लगभग आठ मिनट लगते हैं।",
   "सूर्य का निकटतम तारा लगभग 4.2 प्रकाश-वर्ष दूर है।"],
  C3, 2,
  "All three statements are correct. A light-year is the distance light travels in a year, about 9.5 trillion km. Proxima Centauri, a small red dwarf, is the closest star; so when we look at distant objects we see them as they were when their light set out.",
  "तीनों कथन सही हैं। प्रकाश-वर्ष वह दूरी है जो प्रकाश एक वर्ष में तय करता है, लगभग 9.5 लाख करोड़ किमी। एक छोटा लाल बौना तारा, प्रॉक्सिमा सेंटॉरी, निकटतम तारा है; इसलिए जब हम दूर की वस्तुओं को देखते हैं, तो उन्हें वैसा देखते हैं जैसी वे अपने प्रकाश के चलने के समय थीं।",
  f"{NASA}; {NSC} -- Stars and the Solar System.",
  "as-light-year-distances")

S(AS, "medium", "Consider the following statements about the life of stars:",
  "तारों के जीवन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Sun will swell into a red giant late in its life.",
   "The Sun will end as a white dwarf.",
   "The Sun is massive enough to end its life as a black hole."],
  ["अपने जीवन के अंतिम चरण में सूर्य फूलकर एक लाल दानव (red giant) बन जाएगा।",
   "सूर्य का अंत एक श्वेत वामन (white dwarf) के रूप में होगा।",
   "सूर्य इतना विशाल है कि वह अपना जीवन एक कृष्ण विवर (black hole) के रूप में समाप्त करेगा।"],
  C3, 1,
  "Statements 1 and 2 are correct: in about five billion years, when the hydrogen in its core runs low, the Sun will expand, shed its outer layers and leave behind a hot, dense white dwarf the size of the Earth. "
  "Statement 3 is wrong: only stars many times more massive than the Sun explode as supernovae and leave neutron stars or black holes.",
  "कथन 1 और 2 सही हैं: लगभग पाँच अरब वर्षों में, जब इसके केंद्र में हाइड्रोजन कम हो जाएगी, सूर्य फैलेगा, अपनी बाहरी परतें छोड़ देगा और पृथ्वी के आकार का एक गर्म, सघन श्वेत वामन पीछे छोड़ेगा। "
  "कथन 3 गलत है: केवल सूर्य से कई गुना विशाल तारे ही अधिनव तारे (supernova) के रूप में फटते हैं और न्यूट्रॉन तारे या कृष्ण विवर छोड़ते हैं।",
  f"{NASA} -- Stars.",
  "as-sun-life-cycle")

S(AS, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Cepheid variable stars are used to measure distances to other galaxies.",
   "Pulsars are rotating neutron stars that emit beams of radiation.",
   "A nebula is a cloud of gas and dust in space."],
  ["सेफ़ीड परिवर्ती तारों का उपयोग दूसरी आकाशगंगाओं की दूरी मापने में होता है।",
   "पल्सर घूमते हुए न्यूट्रॉन तारे हैं जो विकिरण की किरणपुंज छोड़ते हैं।",
   "नीहारिका (nebula) अंतरिक्ष में गैस और धूल का एक बादल है।"],
  C3, 2,
  "All three statements are correct. A Cepheid's true brightness is linked to how fast it pulses, so comparing that with how bright it looks gives its distance -- the method Edwin Hubble used to show that other galaxies exist. A pulsar's beam sweeps past the Earth like a lighthouse, and nebulae are where new stars form.",
  "तीनों कथन सही हैं। सेफ़ीड की वास्तविक चमक उसके स्पंदन की गति से जुड़ी है, इसलिए इसकी तुलना उसकी दिखने वाली चमक से करने पर दूरी मिलती है; इसी विधि से एडविन हबल ने दिखाया कि दूसरी आकाशगंगाएँ हैं। पल्सर की किरणपुंज प्रकाश-स्तंभ की तरह पृथ्वी के पास से घूमती है, और नीहारिकाएँ वे स्थान हैं जहाँ नए तारे बनते हैं।",
  f"{NASA} -- Galaxies; Neutron stars.",
  "as-cepheids-pulsars-nebulae")

S(AS, "medium", "Consider the following statements about black holes:",
  "कृष्ण विवरों (black holes) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Nothing, not even light, can escape from inside a black hole's event horizon.",
   "The Event Horizon Telescope released the first image of a black hole's shadow in 2019.",
   "Black holes form only from the collapse of stars smaller than the Sun."],
  ["कृष्ण विवर के घटना क्षितिज (event horizon) के भीतर से कुछ भी, प्रकाश भी, बाहर नहीं निकल सकता।",
   "इवेंट होराइज़न टेलीस्कोप ने 2019 में किसी कृष्ण विवर की छाया का पहला चित्र जारी किया।",
   "कृष्ण विवर केवल सूर्य से छोटे तारों के ढहने से बनते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: the image, of the giant black hole at the centre of the galaxy M87, came from linking radio dishes across the world into one Earth-sized telescope; an image of Sagittarius A*, at the heart of the Milky Way, followed in 2022. "
  "Statement 3 is wrong: stellar black holes come from the collapse of very massive stars, and supermassive ones, millions of times the Sun's mass, sit at the centres of galaxies.",
  "कथन 1 और 2 सही हैं: M87 आकाशगंगा के केंद्र में स्थित विशाल कृष्ण विवर का यह चित्र पूरे विश्व के रेडियो एंटेनों को जोड़कर पृथ्वी जितनी बड़ी एक दूरबीन बनाने से मिला; 2022 में आकाशगंगा (मिल्की वे) के केंद्र में स्थित सैजिटेरियस A* का चित्र आया। "
  "कथन 3 गलत है: तारकीय कृष्ण विवर बहुत विशाल तारों के ढहने से बनते हैं, और सूर्य से लाखों गुना द्रव्यमान वाले अतिविशाल कृष्ण विवर आकाशगंगाओं के केंद्र में होते हैं।",
  "Event Horizon Telescope Collaboration; NASA Science.",
  "as-black-holes")

S(AS, "medium", "Consider the following statements about gravitational waves:",
  "गुरुत्वाकर्षण तरंगों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gravitational waves were first detected directly by LIGO in 2015.",
   "LIGO-India is being built in Maharashtra.",
   "LISA is a ground-based gravitational-wave detector in Europe."],
  ["गुरुत्वाकर्षण तरंगों का पहली बार प्रत्यक्ष पता LIGO ने 2015 में लगाया।",
   "LIGO-इंडिया महाराष्ट्र में बनाया जा रहा है।",
   "LISA यूरोप में स्थित एक भू-आधारित गुरुत्वाकर्षण-तरंग संसूचक है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the waves, ripples in space-time predicted by Einstein, came from two black holes merging about 1.3 billion years ago; LIGO-India, in Hingoli district, will be part of the global network and help locate sources in the sky. "
  "Statement 3 is wrong: LISA, the Laser Interferometer Space Antenna led by the European Space Agency, will be made of three spacecraft millions of kilometres apart, to catch waves too slow for detectors on the ground.",
  "कथन 1 और 2 सही हैं: आइंस्टीन द्वारा भविष्यवाणी की गई ये तरंगें, यानी दिक्-काल की लहरें, लगभग 1.3 अरब वर्ष पहले दो कृष्ण विवरों के मिलने से आई थीं; हिंगोली ज़िले में LIGO-इंडिया वैश्विक नेटवर्क का भाग होगा और आकाश में स्रोतों का पता लगाने में मदद करेगा। "
  "कथन 3 गलत है: यूरोपीय अंतरिक्ष एजेंसी के नेतृत्व वाला LISA, यानी लेज़र इंटरफ़ेरोमीटर स्पेस एंटीना, लाखों किलोमीटर दूर स्थित तीन अंतरिक्ष यानों से बनेगा, ताकि उन तरंगों को पकड़ सके जो भूमि पर स्थित संसूचकों के लिए बहुत धीमी हैं।",
  "LIGO Scientific Collaboration; Department of Atomic Energy -- LIGO-India; European Space Agency -- LISA.",
  "as-gravitational-waves")

S(AS, "medium", "Consider the following statements about space weather:",
  "अंतरिक्ष मौसम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Solar flares and coronal mass ejections can disrupt satellites, radio communication and power grids.",
   "The Sun's activity rises and falls over a cycle of about 11 years.",
   "Auroras are caused by sunlight reflecting off polar ice."],
  ["सौर ज्वालाएँ (solar flares) और कोरोनल द्रव्य उत्क्षेपण उपग्रहों, रेडियो संचार और बिजली ग्रिडों को बाधित कर सकते हैं।",
   "सूर्य की गतिविधि लगभग 11 वर्षों के चक्र में घटती-बढ़ती है।",
   "ध्रुवीय ज्योति (aurora) ध्रुवीय बर्फ़ से सूर्य के प्रकाश के परावर्तन से बनती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the cycle is marked by the number of sunspots, and near its peak -- as in 2024-25 -- strong storms become more frequent. "
  "Statement 3 is wrong: auroras appear when charged particles from the Sun, guided by the Earth's magnetic field towards the poles, strike gases in the upper atmosphere and make them glow; in May 2024 a strong storm made them visible even from Ladakh.",
  "कथन 1 और 2 सही हैं: चक्र सौर कलंकों (sunspots) की संख्या से पहचाना जाता है, और इसके शिखर के आसपास, जैसे 2024-25 में, तेज़ तूफ़ान अधिक बार आते हैं। "
  "कथन 3 गलत है: ध्रुवीय ज्योति तब दिखती है जब सूर्य के आवेशित कण, पृथ्वी के चुंबकीय क्षेत्र द्वारा ध्रुवों की ओर ले जाए जाकर, ऊपरी वायुमंडल की गैसों से टकराते हैं और उन्हें चमकाते हैं; मई 2024 के एक तेज़ तूफ़ान में यह लद्दाख से भी दिखी।",
  "NASA Space Weather; Indian Institute of Astrophysics.",
  "as-space-weather")

S(AS, "medium", "Consider the following statements about the Earth and the Moon:",
  "पृथ्वी और चंद्रमा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Earth's rotation is very gradually slowing over long periods, lengthening the day.",
   "Melting ice and the pumping of groundwater can shift the Earth's axis of rotation slightly.",
   "The Moon is slowly moving away from the Earth."],
  ["लंबी अवधि में पृथ्वी का घूर्णन बहुत धीरे-धीरे धीमा हो रहा है, जिससे दिन लंबा हो रहा है।",
   "पिघलती बर्फ़ और भूजल का दोहन पृथ्वी के घूर्णन अक्ष को थोड़ा खिसका सकते हैं।",
   "चंद्रमा धीरे-धीरे पृथ्वी से दूर जा रहा है।"],
  C3, 2,
  "All three statements are correct. Tidal friction transfers the Earth's spin to the Moon's orbit, so the day lengthens by a couple of milliseconds a century while the Moon recedes by about 3.8 cm a year. Moving large masses of water from ice sheets and aquifers into the oceans changes how mass is spread over the planet, nudging the poles by centimetres to metres.",
  "तीनों कथन सही हैं। ज्वारीय घर्षण पृथ्वी के घूर्णन को चंद्रमा की कक्षा में स्थानांतरित करता है, इसलिए दिन प्रति शताब्दी कुछ मिलीसेकंड लंबा होता है और चंद्रमा प्रति वर्ष लगभग 3.8 सेमी दूर जाता है। बर्फ़ की चादरों और जलभृतों से बड़ी मात्रा में पानी महासागरों में जाने से ग्रह पर द्रव्यमान का वितरण बदलता है, जो ध्रुवों को सेंटीमीटरों से मीटरों तक खिसकाता है।",
  f"{NASA}; Geophysical Research Letters (2023).",
  "as-earth-rotation-moon-recession")

S(AS, "medium", "Consider the following statements about the planets:",
  "ग्रहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Venus rotates in the opposite direction to most planets.",
   "Mercury is the hottest planet in the solar system.",
   "Jupiter is a rocky planet."],
  ["शुक्र अधिकांश ग्रहों की विपरीत दिशा में घूर्णन करता है।",
   "बुध सौरमंडल का सबसे गर्म ग्रह है।",
   "बृहस्पति एक चट्टानी ग्रह है।"],
  C3, 0,
  "Only statement 1 is correct: on Venus the Sun rises in the west, and a day there is longer than its year. "
  "Statement 2 is wrong: Venus, not Mercury, is the hottest, at about 460 °C, because its thick carbon dioxide atmosphere traps heat; Mercury, with no atmosphere, swings between extreme heat and cold. "
  "Statement 3 is wrong: Jupiter is a gas giant made mostly of hydrogen and helium.",
  "केवल कथन 1 सही है: शुक्र पर सूर्य पश्चिम में उगता है, और वहाँ का एक दिन उसके वर्ष से लंबा है। "
  "कथन 2 गलत है: बुध नहीं, बल्कि शुक्र सबसे गर्म है, लगभग 460 °C, क्योंकि उसका घना कार्बन डाइऑक्साइड वायुमंडल ऊष्मा रोकता है; वायुमंडल-रहित बुध अत्यधिक गर्मी और ठंड के बीच झूलता है। "
  "कथन 3 गलत है: बृहस्पति मुख्य रूप से हाइड्रोजन और हीलियम से बना एक गैस दानव है।",
  f"{NASA} -- Planets; {NSC}.",
  "as-planets-venus-mercury")

S(AS, "medium", "Consider the following statements about small bodies of the solar system:",
  "सौरमंडल के छोटे पिंडों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most asteroids are found between the orbits of Mars and Jupiter.",
   "A meteorite is a meteoroid that survives its passage through the atmosphere and reaches the ground.",
   "A comet's tail always points towards the Sun.",
   "The Kuiper Belt lies beyond the orbit of Neptune."],
  ["अधिकांश क्षुद्रग्रह मंगल और बृहस्पति की कक्षाओं के बीच पाए जाते हैं।",
   "उल्कापिंड (meteorite) वह उल्काभ (meteoroid) है जो वायुमंडल से गुज़रते हुए बच जाता है और धरती तक पहुँचता है।",
   "धूमकेतु की पूँछ सदा सूर्य की ओर होती है।",
   "काइपर पट्टी नेपच्यून की कक्षा से आगे स्थित है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct: the Kuiper Belt, home of Pluto, and the more distant Oort Cloud are the sources of most comets. "
  "Statement 3 is wrong: a comet's tails point away from the Sun, pushed by sunlight and the solar wind, so when a comet moves outward its tail leads the way.",
  "कथन 1, 2 और 4 सही हैं: प्लूटो का घर, काइपर पट्टी, और उससे दूर स्थित ऊर्ट बादल अधिकांश धूमकेतुओं के स्रोत हैं। "
  "कथन 3 गलत है: धूमकेतु की पूँछें सूर्य से दूर की ओर होती हैं, जिन्हें सूर्य का प्रकाश और सौर पवन धकेलते हैं; इसलिए जब धूमकेतु बाहर की ओर जाता है, तो उसकी पूँछ आगे चलती है।",
  f"{NASA} -- Asteroids, Comets and Meteors.",
  "as-small-bodies",
  closing="How many of the above statements are correct?",
  closing_hi="उपर्युक्त में से कितने कथन सही हैं?")

S(AS, "medium", "Consider the following statements about the universe:",
  "ब्रह्मांड के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Dark matter gives out no light but reveals itself through its gravity.",
   "Dark energy is the energy released by black holes as they swallow stars.",
   "The cosmic microwave background is radiation given off by the Sun's corona."],
  ["अदृश्य द्रव्य (dark matter) कोई प्रकाश नहीं देता, पर अपने गुरुत्व से अपनी उपस्थिति दिखाता है।",
   "अदृश्य ऊर्जा (dark energy) वह ऊर्जा है जो कृष्ण विवर तारों को निगलते समय छोड़ते हैं।",
   "ब्रह्मांडीय सूक्ष्मतरंग पृष्ठभूमि (CMB) सूर्य के कोरोना से निकलने वाला विकिरण है।"],
  C3, 0,
  "Only statement 1 is correct: galaxies spin too fast to be held together by their visible matter alone. "
  "Statement 2 is wrong: dark energy is the unknown cause of the accelerating expansion of the universe, making up about 70 per cent of its energy. "
  "Statement 3 is wrong: the CMB is the faint afterglow of the hot early universe, released about 380,000 years after the Big Bang and now seen in every direction.",
  "केवल कथन 1 सही है: आकाशगंगाएँ इतनी तेज़ घूमती हैं कि केवल उनका दृश्य पदार्थ उन्हें बाँधे नहीं रख सकता। "
  "कथन 2 गलत है: अदृश्य ऊर्जा ब्रह्मांड के त्वरित होते विस्तार का अज्ञात कारण है, जो उसकी ऊर्जा का लगभग 70 प्रतिशत है। "
  "कथन 3 गलत है: CMB गर्म प्रारंभिक ब्रह्मांड की धुँधली चमक है, जो बिग बैंग के लगभग 3,80,000 वर्ष बाद निकली और अब हर दिशा में दिखती है।",
  f"{NASA} -- Dark Energy, Dark Matter; Cosmic Microwave Background.",
  "as-dark-matter-cmb")

S(AS, "medium", "Consider the following statements about the Earth's magnetic field:",
  "पृथ्वी के चुंबकीय क्षेत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Van Allen belts are belts of asteroids that circle the Earth.",
   "The Earth's magnetic poles have stayed in the same place throughout its history.",
   "The magnetic north pole coincides with the geographic North Pole."],
  ["वैन एलन पट्टियाँ पृथ्वी की परिक्रमा करने वाले क्षुद्रग्रहों की पट्टियाँ हैं।",
   "पृथ्वी के चुंबकीय ध्रुव उसके पूरे इतिहास में एक ही स्थान पर रहे हैं।",
   "चुंबकीय उत्तरी ध्रुव भौगोलिक उत्तरी ध्रुव से मेल खाता है।"],
  C3, 3,
  "None of the statements is correct. The Van Allen belts are zones of charged particles trapped by the magnetic field -- satellites passing through them need shielding. The field has reversed many times, a record preserved in volcanic rocks on the ocean floor, and the magnetic poles wander continually; the magnetic north pole lies hundreds of kilometres from the geographic pole and has been drifting from Canada towards Siberia.",
  "कोई भी कथन सही नहीं है। वैन एलन पट्टियाँ चुंबकीय क्षेत्र द्वारा फँसाए गए आवेशित कणों के क्षेत्र हैं; इनसे गुज़रने वाले उपग्रहों को परिरक्षण चाहिए। क्षेत्र कई बार उलटा है, जिसका अभिलेख समुद्र तल की ज्वालामुखीय चट्टानों में सुरक्षित है, और चुंबकीय ध्रुव लगातार खिसकते रहते हैं; चुंबकीय उत्तरी ध्रुव भौगोलिक ध्रुव से सैकड़ों किलोमीटर दूर है और कनाडा से साइबेरिया की ओर खिसकता रहा है।",
  f"{NASA}; British Geological Survey -- World Magnetic Model.",
  "as-magnetic-field-none")

S(AS, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bharat Forecast System, launched in 2025, produces weather forecasts at a resolution of about 6 km.",
   "The Deep Ocean Mission includes a crewed submersible called Matsya-6000.",
   "The Deep Ocean Mission is run by the Ministry of Earth Sciences."],
  ["2025 में शुरू हुई भारत पूर्वानुमान प्रणाली (Bharat Forecast System) लगभग 6 किमी के विभेदन (resolution) पर मौसम पूर्वानुमान देती है।",
   "डीप ओशन मिशन में मत्स्य-6000 नामक एक मानवयुक्त पनडुब्बी शामिल है।",
   "डीप ओशन मिशन पृथ्वी विज्ञान मंत्रालय चलाता है।"],
  C3, 2,
  "All three statements are correct. The Bharat Forecast System, developed by the Indian Institute of Tropical Meteorology, is among the finest-resolution global weather models, helping to predict local heavy rain. Under the Samudrayaan project, Matsya-6000 is designed to carry three people to a depth of 6,000 metres to study the deep sea and its resources.",
  "तीनों कथन सही हैं। भारतीय उष्णदेशीय मौसम विज्ञान संस्थान द्वारा विकसित भारत पूर्वानुमान प्रणाली सबसे बारीक विभेदन वाले वैश्विक मौसम मॉडलों में से है, जो स्थानीय भारी वर्षा की भविष्यवाणी में मदद करती है। समुद्रयान परियोजना के तहत मत्स्य-6000 को गहरे समुद्र और उसके संसाधनों के अध्ययन के लिए तीन लोगों को 6,000 मीटर की गहराई तक ले जाने के लिए बनाया गया है।",
  "Ministry of Earth Sciences -- Deep Ocean Mission; Indian Institute of Tropical Meteorology -- Bharat Forecast System.",
  "as-bharatfs-deep-ocean")

# ================================================================ ASTRONOMY: EASY STATEMENTS (4)
S(AS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Moon shines by reflecting sunlight.",
   "The Earth revolves around the Sun."],
  ["चंद्रमा सूर्य के प्रकाश को परावर्तित करके चमकता है।",
   "पृथ्वी सूर्य की परिक्रमा करती है।"],
  T2, 2,
  "Both statements are correct: the Moon has no light of its own, and the Earth takes about 365¼ days to go once round the Sun.",
  "दोनों कथन सही हैं: चंद्रमा का अपना कोई प्रकाश नहीं है, और पृथ्वी को सूर्य की एक परिक्रमा में लगभग 365¼ दिन लगते हैं।",
  f"{NSC} -- Stars and the Solar System.",
  "as-moon-earth-easy")

S(AS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A solar eclipse happens when the Moon comes between the Sun and the Earth.",
   "A lunar eclipse can happen only on a new moon day."],
  ["सूर्य ग्रहण तब होता है जब चंद्रमा सूर्य और पृथ्वी के बीच आ जाता है।",
   "चंद्र ग्रहण केवल अमावस्या के दिन हो सकता है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: a lunar eclipse happens when the Earth comes between the Sun and the Moon, which is possible only at full moon; solar eclipses happen at new moon.",
  "केवल कथन 1 सही है। कथन 2 गलत है: चंद्र ग्रहण तब होता है जब पृथ्वी सूर्य और चंद्रमा के बीच आती है, जो केवल पूर्णिमा को संभव है; सूर्य ग्रहण अमावस्या को होते हैं।",
  f"{NSC}.",
  "as-eclipses-easy")

S(AS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Sun is a planet.",
   "Jupiter is the largest planet in the solar system."],
  ["सूर्य एक ग्रह है।",
   "बृहस्पति सौरमंडल का सबसे बड़ा ग्रह है।"],
  T2, 1,
  "Only statement 2 is correct. Statement 1 is wrong: the Sun is a star -- it makes its own light and heat by nuclear fusion -- and the planets revolve around it.",
  "केवल कथन 2 सही है। कथन 1 गलत है: सूर्य एक तारा है; यह नाभिकीय संलयन से अपना प्रकाश और ऊष्मा बनाता है, और ग्रह इसकी परिक्रमा करते हैं।",
  f"{NSC}.",
  "as-sun-jupiter-easy")

S(AS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Stars shine by reflecting light from the Sun.",
   "The Moon has a thick atmosphere."],
  ["तारे सूर्य के प्रकाश को परावर्तित करके चमकते हैं।",
   "चंद्रमा का वायुमंडल घना है।"],
  T2, 3,
  "Neither statement is correct. Stars, like the Sun, produce their own light. The Moon has almost no atmosphere, which is why its sky is black even by day and its craters are not worn away by wind and rain.",
  "कोई भी कथन सही नहीं है। तारे, सूर्य की तरह, अपना प्रकाश स्वयं पैदा करते हैं। चंद्रमा पर लगभग कोई वायुमंडल नहीं है; इसीलिए वहाँ दिन में भी आकाश काला दिखता है और उसके गड्ढे हवा और वर्षा से घिसते नहीं।",
  f"{NSC}.",
  "as-stars-moon-atmosphere-easy")

# ================================================================ ASTRONOMY: HARD STATEMENTS (4)
S(AS, "hard", "Consider the following statements about exoplanets:",
  "बाह्य ग्रहों (exoplanets) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The transit method finds planets from the dip in a star's brightness as a planet passes in front of it.",
   "The James Webb Space Telescope observes mainly in infrared light.",
   "Most known exoplanets have been found by photographing them directly."],
  ["पारगमन (transit) विधि किसी ग्रह के तारे के सामने से गुज़रते समय तारे की चमक में गिरावट से ग्रहों का पता लगाती है।",
   "जेम्स वेब अंतरिक्ष दूरबीन मुख्य रूप से अवरक्त (infrared) प्रकाश में देखती है।",
   "अधिकांश ज्ञात बाह्य ग्रह उनका सीधे चित्र लेकर खोजे गए हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: missions such as Kepler and TESS have found thousands of planets by transits, and Webb, working in the infrared, can study the atmospheres of some of them as starlight filters through. "
  "Statement 3 is wrong: planets are billions of times fainter than their stars, so only a few dozen have been imaged; most were found indirectly, by transits or by the wobble they cause in their star.",
  "कथन 1 और 2 सही हैं: केप्लर और TESS जैसे मिशनों ने पारगमन से हज़ारों ग्रह खोजे हैं, और अवरक्त में काम करने वाली वेब दूरबीन उनमें से कुछ के वायुमंडल का अध्ययन कर सकती है, जब तारे का प्रकाश उनसे छनकर आता है। "
  "कथन 3 गलत है: ग्रह अपने तारों से अरबों गुना धुँधले होते हैं, इसलिए केवल कुछ दर्जन के चित्र लिए गए हैं; अधिकांश अप्रत्यक्ष रूप से, पारगमन से या अपने तारे में पैदा होने वाले डगमगाहट से, खोजे गए।",
  f"{NASA} -- Exoplanet Exploration; James Webb Space Telescope.",
  "as-exoplanets-jwst")

S(AS, "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Neutrinos interact so weakly with matter that their detectors are built deep underground.",
   "Fast radio bursts are long-lasting radio signals that come from the Sun.",
   "The India-based Neutrino Observatory is planned in Ladakh."],
  ["न्यूट्रिनो पदार्थ से इतनी कमज़ोर अंतःक्रिया करते हैं कि उनके संसूचक ज़मीन के बहुत नीचे बनाए जाते हैं।",
   "तीव्र रेडियो प्रस्फोट (fast radio bursts) सूर्य से आने वाले लंबे समय तक चलने वाले रेडियो संकेत हैं।",
   "भारत-आधारित न्यूट्रिनो वेधशाला लद्दाख में प्रस्तावित है।"],
  C3, 0,
  "Only statement 1 is correct: trillions of neutrinos pass through each of us every second; rock overhead shields detectors from cosmic rays that would swamp the rare neutrino signals. "
  "Statement 2 is wrong: fast radio bursts last only milliseconds and mostly come from other galaxies, some from magnetars. "
  "Statement 3 is wrong: the India-based Neutrino Observatory is planned under a mountain in the Bodi West Hills of Theni district, Tamil Nadu.",
  "केवल कथन 1 सही है: हर सेकंड हम सबमें से खरबों न्यूट्रिनो गुज़रते हैं; ऊपर की चट्टान संसूचकों को उन ब्रह्मांडीय किरणों से बचाती है जो दुर्लभ न्यूट्रिनो संकेतों को ढक देंगी। "
  "कथन 2 गलत है: तीव्र रेडियो प्रस्फोट केवल मिलीसेकंड तक चलते हैं और अधिकतर दूसरी आकाशगंगाओं से, कुछ मैग्नेटार से, आते हैं। "
  "कथन 3 गलत है: भारत-आधारित न्यूट्रिनो वेधशाला तमिलनाडु के थेनी ज़िले की बोडी पश्चिमी पहाड़ियों में एक पर्वत के नीचे प्रस्तावित है।",
  "Department of Atomic Energy -- India-based Neutrino Observatory; NASA Science.",
  "as-neutrinos-frbs")

S(AS, "hard", "Consider the following statements about the remains of stars:",
  "तारों के अवशेषों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Chandrasekhar limit, the largest mass a white dwarf can have, is about 1.4 times the mass of the Sun.",
   "A teaspoonful of neutron-star material would weigh billions of tonnes on the Earth.",
   "Magnetars are neutron stars with extremely strong magnetic fields."],
  ["चंद्रशेखर सीमा, यानी किसी श्वेत वामन का अधिकतम द्रव्यमान, सूर्य के द्रव्यमान का लगभग 1.4 गुना है।",
   "न्यूट्रॉन तारे के पदार्थ का एक चम्मच पृथ्वी पर अरबों टन भारी होगा।",
   "मैग्नेटार अत्यधिक शक्तिशाली चुंबकीय क्षेत्र वाले न्यूट्रॉन तारे हैं।"],
  C3, 2,
  "All three statements are correct. Subrahmanyan Chandrasekhar showed in the 1930s that above this limit electron pressure cannot hold a white dwarf up, which won him a share of the 1983 Nobel Prize in Physics. A neutron star packs more than the Sun's mass into a ball about 20 km across, and a magnetar's field is a thousand trillion times the Earth's.",
  "तीनों कथन सही हैं। सुब्रह्मण्यन चंद्रशेखर ने 1930 के दशक में दिखाया कि इस सीमा से ऊपर इलेक्ट्रॉन दाब श्वेत वामन को थामे नहीं रख सकता, जिसके लिए उन्हें 1983 के भौतिकी नोबेल पुरस्कार का हिस्सा मिला। न्यूट्रॉन तारा सूर्य से अधिक द्रव्यमान को लगभग 20 किमी व्यास की गेंद में समेट लेता है, और मैग्नेटार का क्षेत्र पृथ्वी के क्षेत्र का हज़ार खरब गुना है।",
  f"{NOBEL} (Physics, 1983); {NASA} -- Neutron stars.",
  "as-chandrasekhar-neutron-stars")

S(AS, "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A sidereal day, measured against the stars, is longer than a solar day.",
   "The Earth is closest to the Sun in July.",
   "The seasons are caused mainly by changes in the Earth's distance from the Sun."],
  ["तारों के सापेक्ष मापा गया नाक्षत्र दिवस (sidereal day) सौर दिवस से लंबा होता है।",
   "पृथ्वी जुलाई में सूर्य के सबसे निकट होती है।",
   "ऋतुएँ मुख्य रूप से पृथ्वी की सूर्य से दूरी में परिवर्तन के कारण होती हैं।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: the sidereal day is about 23 hours 56 minutes -- four minutes shorter than the solar day, because the Earth must turn a little extra each day to face the Sun again as it moves along its orbit. "
  "Statement 2 is wrong: the Earth is closest to the Sun (perihelion) in early January, in the northern winter. "
  "Statement 3 is wrong: seasons come from the 23.5° tilt of the Earth's axis, which changes the height of the Sun and the length of the day -- which is why the two hemispheres have opposite seasons.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: नाक्षत्र दिवस लगभग 23 घंटे 56 मिनट का है, सौर दिवस से चार मिनट छोटा, क्योंकि कक्षा में आगे बढ़ती पृथ्वी को फिर से सूर्य के सामने आने के लिए हर दिन थोड़ा अधिक घूमना पड़ता है। "
  "कथन 2 गलत है: पृथ्वी जनवरी के आरंभ में, उत्तरी गोलार्ध की सर्दी में, सूर्य के सबसे निकट (उपसौर, perihelion) होती है। "
  "कथन 3 गलत है: ऋतुएँ पृथ्वी के अक्ष के 23.5° झुकाव से आती हैं, जो सूर्य की ऊँचाई और दिन की लंबाई बदलता है; इसीलिए दोनों गोलार्धों में विपरीत ऋतुएँ होती हैं।",
  f"{NASA}; NCERT Geography, Class XI -- Fundamentals of Physical Geography.",
  "as-sidereal-perihelion-seasons-none")

# ================================================================ ASTRONOMY: MEDIUM MCQs (4)
M(AS, "medium", "The Hubble constant measures:",
  "हबल स्थिरांक (Hubble constant) क्या मापता है?",
  ["how fast the universe is expanding", "the brightness of the most distant stars that can be seen from the Earth",
   "the time a telescope takes to capture a clear image of a galaxy", "the number of galaxies found in a given region of the sky"],
  ["ब्रह्मांड कितनी तेज़ी से फैल रहा है", "पृथ्वी से दिख सकने वाले सबसे दूर के तारों की चमक",
   "किसी आकाशगंगा का स्पष्ट चित्र लेने में दूरबीन को लगने वाला समय", "आकाश के किसी क्षेत्र में पाई जाने वाली आकाशगंगाओं की संख्या"],
  0,
  "Edwin Hubble found that the farther a galaxy is, the faster it is moving away; the constant gives that speed per unit of distance, about 70 km per second for every megaparsec. Different methods give slightly different values -- the 'Hubble tension' that puzzles cosmologists.",
  "एडविन हबल ने पाया कि कोई आकाशगंगा जितनी दूर है, उतनी ही तेज़ी से दूर जा रही है; स्थिरांक दूरी की प्रति इकाई यह गति बताता है, लगभग 70 किमी प्रति सेकंड प्रति मेगापारसेक। अलग-अलग विधियाँ थोड़े अलग मान देती हैं; यही 'हबल तनाव' ब्रह्मांड-विज्ञानियों को उलझाता है।",
  f"{NASA} -- Hubble's law.",
  "as-hubble-constant")

M(AS, "medium", "Which one of the following planets has the shortest day?",
  "निम्नलिखित में से किस ग्रह का दिन सबसे छोटा है?",
  ["Jupiter", "Mercury", "Mars", "Venus"],
  ["बृहस्पति", "बुध", "मंगल", "शुक्र"],
  0,
  "Jupiter, the largest planet, spins fastest, once in just under 10 hours, which flattens it visibly at the poles. Mars takes about 24 hours 37 minutes, Mercury about 59 Earth days and Venus 243 Earth days.",
  "सबसे बड़ा ग्रह, बृहस्पति, सबसे तेज़ घूमता है, 10 घंटे से थोड़े कम में एक बार, जिससे वह ध्रुवों पर स्पष्ट रूप से चपटा है। मंगल को लगभग 24 घंटे 37 मिनट, बुध को पृथ्वी के लगभग 59 दिन, और शुक्र को पृथ्वी के 243 दिन लगते हैं।",
  f"{NASA} -- Planets.",
  "as-shortest-day-jupiter")

M(AS, "medium", "The 'habitable' or 'Goldilocks' zone around a star is the region where:",
  "किसी तारे के चारों ओर 'रहने योग्य' या 'गोल्डीलॉक्स' क्षेत्र वह है जहाँ:",
  ["liquid water could exist on a planet's surface", "planets are shielded from all of their star's radiation by a thick cloud of dust",
   "the star's gravity is too weak to hold any planets in orbit", "asteroids gather because of the balance of forces from two stars"],
  ["किसी ग्रह की सतह पर द्रव जल रह सकता है", "ग्रह धूल के घने बादल से अपने तारे के सारे विकिरण से बचे रहते हैं",
   "तारे का गुरुत्व किसी भी ग्रह को कक्षा में रखने के लिए बहुत कमज़ोर है", "दो तारों के बलों के संतुलन से क्षुद्रग्रह इकट्ठा होते हैं"],
  0,
  "Not too hot and not too cold -- like the porridge in the story -- for water to stay liquid. Its distance depends on the star: close in for dim red dwarfs, farther out for hot bright stars. Being in the zone does not guarantee life; Venus lies near its inner edge.",
  "न बहुत गर्म, न बहुत ठंडा, कहानी के दलिये की तरह, ताकि पानी द्रव बना रहे। इसकी दूरी तारे पर निर्भर है: धुँधले लाल बौनों के लिए पास, गर्म चमकीले तारों के लिए दूर। इस क्षेत्र में होना जीवन की गारंटी नहीं है; शुक्र इसके भीतरी किनारे के पास है।",
  f"{NASA} -- Exoplanet Exploration.",
  "as-goldilocks-zone")

M(AS, "medium", "The distances to the nearest stars are measured mainly by:",
  "निकटतम तारों की दूरियाँ मुख्य रूप से किससे मापी जाती हैं?",
  ["stellar parallax", "bouncing radar signals off them and timing the echo",
   "the redshift of their spectral lines caused by the universe's expansion", "gravitational lensing of light from galaxies behind them"],
  ["तारकीय लंबन (stellar parallax)", "उनसे रडार संकेत टकराकर और प्रतिध्वनि का समय मापकर",
   "ब्रह्मांड के विस्तार से उनकी वर्णक्रमीय रेखाओं के अभिरक्त विस्थापन से", "उनके पीछे की आकाशगंगाओं के प्रकाश के गुरुत्वीय लेंसन से"],
  0,
  "As the Earth goes round the Sun, a nearby star seems to shift slightly against distant ones; the size of that shift gives its distance by simple geometry, and the unit 'parsec' comes from it. Radar reaches only planets and asteroids, while redshift is used for distant galaxies.",
  "पृथ्वी के सूर्य की परिक्रमा करते समय कोई निकट का तारा दूर के तारों के सापेक्ष थोड़ा खिसकता दिखता है; इस खिसकाव का आकार सरल ज्यामिति से उसकी दूरी देता है, और 'पारसेक' इकाई इसी से आती है। रडार केवल ग्रहों और क्षुद्रग्रहों तक पहुँचता है, जबकि अभिरक्त विस्थापन दूर की आकाशगंगाओं के लिए प्रयुक्त होता है।",
  f"{NASA}; European Space Agency -- Gaia.",
  "as-stellar-parallax")

# ================================================================ ASTRONOMY: EASY MCQ (1)
M(AS, "easy", "Which planet is known as the 'Red Planet'?",
  "किस ग्रह को 'लाल ग्रह' कहा जाता है?",
  ["Mars", "Venus", "Mercury", "Saturn"],
  ["मंगल", "शुक्र", "बुध", "शनि"],
  0,
  "Mars looks red because its surface dust is rich in iron oxide -- rust.",
  "मंगल लाल दिखता है क्योंकि उसकी सतह की धूल आयरन ऑक्साइड, यानी जंग, से भरपूर है।",
  f"{NSC}.",
  "as-red-planet-easy")

# ================================================================ ASTRONOMY: HARD MCQ (1)
M(AS, "hard", "One parsec is about 3.26 light-years. A star 10 parsecs away is therefore at a distance of about:",
  "एक पारसेक लगभग 3.26 प्रकाश-वर्ष है। इसलिए 10 पारसेक दूर स्थित तारा लगभग कितनी दूरी पर है?",
  ["32.6 light-years", "3.26 light-years", "10.0 light-years", "326 light-years"],
  ["32.6 प्रकाश-वर्ष", "3.26 प्रकाश-वर्ष", "10.0 प्रकाश-वर्ष", "326 प्रकाश-वर्ष"],
  0,
  "10 x 3.26 = 32.6 light-years. A parsec is the distance at which a star would show a parallax of one arcsecond; the nearest star, at about 1.3 parsecs, has a parallax of under one arcsecond.",
  "10 x 3.26 = 32.6 प्रकाश-वर्ष। पारसेक वह दूरी है जिस पर किसी तारे का लंबन एक चाप-सेकंड होगा; लगभग 1.3 पारसेक पर स्थित निकटतम तारे का लंबन एक चाप-सेकंड से कम है।",
  f"{NASA}.",
  "as-parsec-numerical")

# ================================================================ ASTRONOMY: STATEMENT-I/II (medium 2, easy 1)
A(AS, "medium",
  "Astronauts on the International Space Station feel weightless.",
  "अंतरराष्ट्रीय अंतरिक्ष स्टेशन पर अंतरिक्ष यात्री भारहीनता महसूस करते हैं।",
  "They and the station are falling freely around the Earth all the time.",
  "वे और स्टेशन हर समय पृथ्वी के चारों ओर स्वतंत्र रूप से गिर रहे होते हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. At the station's height, about 400 km, gravity is still about 90 per cent as strong as on the ground; the crew feel weightless because they and the station fall together, moving sideways fast enough that they keep missing the Earth -- which is what an orbit is.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। स्टेशन की लगभग 400 किमी की ऊँचाई पर गुरुत्व अब भी ज़मीन का लगभग 90 प्रतिशत है; यात्री इसलिए भारहीन महसूस करते हैं कि वे और स्टेशन एक साथ गिरते हैं, और इतनी तेज़ी से बगल की ओर बढ़ते हैं कि पृथ्वी से टकराने से चूकते रहते हैं; कक्षा यही है।",
  f"{NASA}; NCERT Physics, Class XI -- Gravitation.",
  "as-iss-free-fall")

A(AS, "medium",
  "The same side of the Moon always faces the Earth.",
  "चंद्रमा का एक ही भाग सदा पृथ्वी की ओर रहता है।",
  "The Moon does not rotate on its axis.",
  "चंद्रमा अपने अक्ष पर घूर्णन नहीं करता।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The Moon does rotate -- once in about 27.3 days, exactly the time it takes to orbit the Earth. This 'tidal locking', caused by the Earth's pull on the Moon over billions of years, is why we always see the same face; if it did not rotate, we would see every side in turn.",
  "कथन-I सही है पर कथन-II गलत है। चंद्रमा घूर्णन करता है, लगभग 27.3 दिनों में एक बार, ठीक उतने समय में जितने में वह पृथ्वी की परिक्रमा करता है। अरबों वर्षों में चंद्रमा पर पृथ्वी के खिंचाव से हुआ यह 'ज्वारीय बंधन' (tidal locking) ही कारण है कि हम सदा एक ही भाग देखते हैं; यदि यह घूर्णन न करता, तो हम बारी-बारी से हर भाग देखते।",
  f"{NASA} -- Moon.",
  "as-moon-tidal-locking")

A(AS, "easy",
  "The Moon seems to change its shape over a month.",
  "एक महीने में चंद्रमा का आकार बदलता हुआ दिखता है।",
  "As the Moon goes round the Earth, we see different portions of its sunlit half.",
  "जैसे-जैसे चंद्रमा पृथ्वी की परिक्रमा करता है, हम उसके सूर्य से प्रकाशित आधे भाग के अलग-अलग हिस्से देखते हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I: half the Moon is always lit by the Sun, and its phases, from new moon to full moon and back, show how much of that lit half faces us.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है: चंद्रमा का आधा भाग सदा सूर्य से प्रकाशित रहता है, और अमावस्या से पूर्णिमा और वापस तक उसकी कलाएँ दिखाती हैं कि उस प्रकाशित आधे का कितना भाग हमारी ओर है।",
  f"{NSC}.",
  "as-moon-phases-easy")

if __name__ == "__main__":
    write("st_l2_t19_bio_astro.sql")
