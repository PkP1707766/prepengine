# -*- coding: utf-8 -*-
"""Current Affairs · Test 4 (October to December 2026) -- part C: polity and governance.

Each item ties a ruling, a renamed scheme or a new programme to the constitutional provision behind it: children's
right to the internet (Articles 21 and 19 and the data protection law), the National Social Assistance Programme
renamed (Article 41 and the disability law), and the new scheme for panchayats (Article 243G and own revenue).
Written month by month: October 2026 first. No stem carries a date (design doc, section 7)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t4_format import FORMAT, POS

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
FR, WS, LG = "Fundamental Rights", "Welfare & DPSP", "Local Government"

# ---------------------------------------------------------------- October 2026

S(FR, "medium", "The Supreme Court held that children, too, have a fundamental right to access the internet. Consider the following statements:",
  "सर्वोच्च न्यायालय ने कहा कि बच्चों को भी इंटरनेट तक पहुँच का मौलिक अधिकार है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The right to access the internet now forms part of the right to life and personal liberty under Article 21, read with the freedom of speech and expression in Article 19(1)(a).",
   "A blanket ban on children's use of the internet would fail the test of proportionality that any restriction on this right must meet.",
   "Under the Digital Personal Data Protection Act, 2023, a platform may process a child's personal data without a parent's consent once the child turns 13."],
  ["इंटरनेट तक पहुँच का अधिकार अब अनुच्छेद 21 के प्राण और दैहिक स्वतंत्रता के अधिकार का भाग है, अनुच्छेद 19(1)(क) की वाक् और अभिव्यक्ति की स्वतंत्रता के साथ पढ़ा गया।",
   "बच्चों के इंटरनेट उपयोग पर पूर्ण प्रतिबंध आनुपातिकता की उस कसौटी पर विफल होगा जिसे इस अधिकार पर हर प्रतिबंध को पूरा करना होता है।",
   "डिजिटल व्यक्तिगत डेटा संरक्षण अधिनियम, 2023 के अंतर्गत बच्चे के 13 वर्ष का होते ही कोई प्लेटफ़ॉर्म माता-पिता की सहमति के बिना उसका व्यक्तिगत डेटा संसाधित कर सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Court treated access to the internet as part of the right to life and personal liberty, read with the freedom of expression, since education, information and much of public life now pass through it. It built on the Kerala High Court's ruling in Faheema Shirin (2019) and on Anuradha Bhasin (2020), which protected speech and trade carried on over the internet. It called blanket restrictions 'unproven measures of proven disproportionality' and preferred parental consent, guidance and oversight and a 'child mode' on platforms, leaving the details to the Union -- the test of proportionality that governs any restriction on a fundamental right. "
  "Statement 3 is wrong: the 2023 Act defines a child as anyone below 18 and requires the verifiable consent of a parent or lawful guardian before a child's data is processed; it also bars tracking, behavioural monitoring and targeted advertising directed at children.",
  "कथन 1 और 2 सही हैं। न्यायालय ने इंटरनेट तक पहुँच को अभिव्यक्ति की स्वतंत्रता के साथ पढ़े गए प्राण और दैहिक स्वतंत्रता के अधिकार का भाग माना, क्योंकि शिक्षा, सूचना और सार्वजनिक जीवन का बड़ा भाग अब इसी से होकर जाता है। इसने केरल उच्च न्यायालय के फ़हीमा शिरीन (2019) निर्णय और अनुराधा भसीन (2020) पर निर्माण किया, जिसने इंटरनेट पर की जाने वाली अभिव्यक्ति और व्यापार को संरक्षण दिया था। इसने पूर्ण प्रतिबंधों को ‘सिद्ध अनुपातहीनता वाले असिद्ध उपाय’ कहा और माता-पिता की सहमति, मार्गदर्शन और निगरानी तथा प्लेटफ़ॉर्मों पर ‘चाइल्ड मोड’ को प्राथमिकता दी, विवरण संघ पर छोड़ते हुए -- यही आनुपातिकता की वह कसौटी है जो किसी मौलिक अधिकार पर हर प्रतिबंध को नियंत्रित करती है। "
  "कथन 3 ग़लत है: 2023 का अधिनियम 18 वर्ष से कम आयु के हर व्यक्ति को बच्चा मानता है और बच्चे का डेटा संसाधित करने से पहले माता-पिता या विधिक अभिभावक की सत्यापन-योग्य सहमति अनिवार्य करता है; यह बच्चों पर लक्षित ट्रैकिंग, व्यवहार-निगरानी और लक्षित विज्ञापन भी वर्जित करता है।",
  "Supreme Court of India, judgment on children's right to access the internet (October 2026); Digital Personal Data Protection Act, 2023, sections 2(f) and 9; Faheema Shirin R.K. v. State of Kerala (Kerala High Court, 2019).",
  "ca-t4-pol-children-internet-art21-19-dpdp-under-18", craft="linkage")

S(WS, "medium", "The National Social Assistance Programme was renamed the Pradhan Mantri Samajik Sahayata Yojana and continued to 2030-31. Consider the following statements:",
  "राष्ट्रीय सामाजिक सहायता कार्यक्रम का नाम बदलकर प्रधानमंत्री सामाजिक सहायता योजना किया गया और इसे 2030-31 तक जारी रखा गया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The programme was launched to give effect to the Directive Principle in Article 41 of the Constitution.",
   "The Union provides its assistance under the programme without requiring a matching share from the States.",
   "Under the revised disability pension, a person with a benchmark disability of 40 per cent qualifies, in line with the Rights of Persons with Disabilities Act, 2016."],
  ["यह कार्यक्रम संविधान के अनुच्छेद 41 के निदेशक तत्व को प्रभावी करने के लिए आरंभ किया गया था।",
   "संघ इस कार्यक्रम के अंतर्गत राज्यों से समतुल्य अंश माँगे बिना अपनी सहायता देता है।",
   "संशोधित दिव्यांगजन पेंशन के अंतर्गत 40 प्रतिशत मानक दिव्यांगता वाला व्यक्ति पात्र है, दिव्यांगजन अधिकार अधिनियम, 2016 के अनुरूप।"],
  C3, 2,
  "All three statements are correct. The programme was launched on 15 August 1995 to discharge the Centre's part of the duty in Article 41 -- public assistance in old age, sickness, disablement and other cases of undeserved want, within the limits of the State's economic capacity. It carries 100 per cent central assistance so that a minimum level of support is the same everywhere; most States add their own top-up. "
  "The 2026 decision, with ₹53,428 crore for 2026-27 to 2030-31 and about 3.2 crore beneficiaries, renamed the sub-schemes -- the old-age, widow and disability pensions and the family benefit scheme -- and changed only the disability pension: the threshold falls from 80 to 40 per cent, the 'benchmark disability' of the 2016 Act; it is available from birth rather than from adulthood; and the amount rises, since the Act requires disability assistance to be at least 25 per cent higher than that under similar schemes for others.",
  "तीनों कथन सही हैं। यह कार्यक्रम 15 अगस्त 1995 को अनुच्छेद 41 के कर्तव्य में केंद्र का भाग निभाने के लिए आरंभ हुआ -- राज्य की आर्थिक सामर्थ्य की सीमाओं के भीतर, बुढ़ापे, बीमारी, निःशक्तता और अनर्ह अभाव की अन्य दशाओं में लोक सहायता। इसमें 100 प्रतिशत केंद्रीय सहायता है ताकि न्यूनतम सहायता हर जगह एक समान रहे; अधिकांश राज्य अपनी ओर से अतिरिक्त राशि जोड़ते हैं। "
  "2026 के निर्णय ने, 2026-27 से 2030-31 के लिए ₹53,428 करोड़ और लगभग 3.2 करोड़ लाभार्थियों के साथ, उप-योजनाओं -- वृद्धावस्था, विधवा और दिव्यांगजन पेंशन तथा पारिवारिक लाभ योजना -- के नाम बदले और केवल दिव्यांगजन पेंशन में परिवर्तन किया: पात्रता की सीमा 80 से घटकर 40 प्रतिशत हुई, जो 2016 के अधिनियम की ‘मानक दिव्यांगता’ है; यह वयस्क होने के बजाय जन्म से मिलेगी; और राशि बढ़ी, क्योंकि अधिनियम अपेक्षा करता है कि दिव्यांगता संबंधी सहायता अन्य लोगों की समान योजनाओं से कम से कम 25 प्रतिशत अधिक हो।",
  "Union Cabinet, continuation of the National Social Assistance Programme for 2026-27 to 2030-31 (PIB, 14 October 2026); Constitution of India, Article 41; Rights of Persons with Disabilities Act, 2016.",
  "ca-t4-pol-nsap-pmssy-art41-central-40-benchmark", craft="linkage")

S(LG, "medium", "The Pradhan Mantri Viksit Gram Swaraj Yojana was approved for five years to strengthen Panchayati Raj institutions. Consider the following statements:",
  "पंचायती राज संस्थाओं को सुदृढ़ करने के लिए प्रधानमंत्री विकसित ग्राम स्वराज योजना को पाँच वर्षों के लिए स्वीकृति दी गई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a Central Sector Scheme funded entirely by the Union.",
   "It supports the annual development plans of gram panchayats, the kind of plans for economic development and social justice that the Constitution envisages panchayats preparing.",
   "Raising the panchayats' own-source revenue is among its aims."],
  ["यह पूर्णतः संघ द्वारा वित्तपोषित केंद्रीय क्षेत्र की योजना है।",
   "यह ग्राम पंचायतों की वार्षिक विकास योजनाओं का समर्थन करती है, उसी प्रकार की आर्थिक विकास और सामाजिक न्याय की योजनाएँ जिन्हें बनाने की कल्पना संविधान पंचायतों के लिए करता है।",
   "पंचायतों के स्वयं के राजस्व को बढ़ाना इसके उद्देश्यों में है।"],
  C3, 1,
  "Statements 2 and 3 are correct. The scheme supports holistic Gram Panchayat Development Plans for about 2.55 lakh panchayats every year, prepared through the eGramSwaraj portal and discussed in the gram sabha. Article 243G lets a State legislature endow panchayats with powers to prepare and implement plans for economic development and social justice, including on the 29 matters in the Eleventh Schedule. "
  "Own-source revenue matters because panchayats depend heavily on transfers from the Centre and States; Article 243H lets the legislature authorise them to levy taxes and fees, and State Finance Commissions review their finances under Article 243-I. Statement 1 is wrong: it is a Centrally Sponsored Scheme with an outlay of ₹7,395.55 crore for 2026-27 to 2030-31 -- ₹4,869.48 crore from the Centre and ₹2,526.07 crore from the States -- since panchayats are a State subject.",
  "कथन 2 और 3 सही हैं। यह योजना हर वर्ष लगभग 2.55 लाख पंचायतों की समग्र ग्राम पंचायत विकास योजनाओं का समर्थन करती है, जो ई-ग्रामस्वराज पोर्टल से तैयार होती हैं और ग्राम सभा में चर्चित होती हैं। अनुच्छेद 243छ राज्य विधानमंडल को पंचायतों को आर्थिक विकास और सामाजिक न्याय की योजनाएँ तैयार करने और लागू करने की शक्तियाँ देने देता है, ग्यारहवीं अनुसूची के 29 विषयों सहित। "
  "स्वयं का राजस्व इसलिए मायने रखता है कि पंचायतें केंद्र और राज्यों के हस्तांतरणों पर बहुत निर्भर हैं; अनुच्छेद 243ज विधानमंडल को उन्हें कर और शुल्क लगाने के लिए प्राधिकृत करने देता है, और अनुच्छेद 243झ के अंतर्गत राज्य वित्त आयोग उनके वित्त की समीक्षा करते हैं। कथन 1 ग़लत है: यह 2026-27 से 2030-31 के लिए ₹7,395.55 करोड़ के परिव्यय वाली केंद्र प्रायोजित योजना है -- ₹4,869.48 करोड़ केंद्र से और ₹2,526.07 करोड़ राज्यों से -- क्योंकि पंचायतें राज्य का विषय हैं।",
  "Union Cabinet, Pradhan Mantri Viksit Gram Swaraj Yojana (October 2026); Constitution of India, Articles 243G, 243H and 243-I and the Eleventh Schedule.",
  "ca-t4-pol-pm-vgsy-css-gpdp-243g-own-revenue", craft="linkage")

finish("ca_t4_c.sql", FORMAT, "2026-Q4", update="--update" in sys.argv)
