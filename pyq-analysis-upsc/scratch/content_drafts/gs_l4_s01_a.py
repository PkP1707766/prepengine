# -*- coding: utf-8 -*-
"""Level 4 · Simulator 1 (GS Paper I full mock, Layout A: the 2023/24 shape) -- part A: Polity (16)
(upsc_l4_gs_cell_targets.mjs 1).
Layout A leans on 'How many' counts and Statement-I/II items, as the 2023 and 2024 papers did. Every tested statement
was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: the CAG's supplementary audit of
government companies; Articles 130, 139, 144 and 146; Article 340 and the Kalelkar and Mandal commissions; Article 339
and the Dhebar and Bhuria commissions; the Governor's report on Scheduled Areas and Samatha; Article 30(1A); the
proviso to Article 309 and the exceptions in Article 311(2); victim compensation schemes; Nandini Sundar, Supriyo and
Laxmi; Article 243U; Article 96; Article 368(2) for a bill on States' representation; the Rajya Sabha's resolutions;
the Cape Town Convention Act and the 2025 shipping laws; Articles 177 and 105(4). MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
COI = "Constitution of India"

# ---------------------------------------------------------------- Constitutional & Statutory Bodies (AR, hard)
A("Constitutional & Statutory Bodies", "hard",
  "The Comptroller and Auditor General of India does not himself carry out the statutory audit of the accounts of a government company.",
  "भारत के नियंत्रक-महालेखापरीक्षक किसी सरकारी कंपनी के लेखाओं की सांविधिक लेखापरीक्षा स्वयं नहीं करते।",
  "Under the Companies Act, 2013 the statutory auditor of a government company is appointed by the Comptroller and Auditor General, who may then conduct a supplementary audit of its accounts.",
  "कंपनी अधिनियम, 2013 के अंतर्गत किसी सरकारी कंपनी के सांविधिक लेखापरीक्षक की नियुक्ति नियंत्रक-महालेखापरीक्षक करते हैं, जो फिर उसके लेखाओं की अनुपूरक लेखापरीक्षा कर सकते हैं।",
  0,
  "Both statements are correct, and Statement II explains Statement I. Article 149 lets Parliament prescribe the CAG's duties, and the CAG's (Duties, Powers and Conditions of Service) Act, 1971 says that a government company is audited in the manner its own law lays down. The Companies Act, 2013 (sections 139(5) and 143(6)) makes the CAG appoint a chartered accountant as statutory auditor within 180 days of the start of the financial year; the CAG may then conduct a supplementary audit within 60 days of receiving the audit report and comment on or supplement it, and these comments are placed before the company's annual general meeting. "
  "This two-tier arrangement is why the CAG's findings on public sector undertakings appear as comments on accounts audited by others, and why the Committee on Public Undertakings, not only the Public Accounts Committee, takes them up.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। अनुच्छेद 149 संसद को नियंत्रक-महालेखापरीक्षक के कर्तव्य निर्धारित करने देता है, और नियंत्रक-महालेखापरीक्षक (कर्तव्य, शक्तियाँ और सेवा की शर्तें) अधिनियम, 1971 कहता है कि सरकारी कंपनी की लेखापरीक्षा उसकी अपनी विधि में बताए तरीक़े से होगी। कंपनी अधिनियम, 2013 (धारा 139(5) और 143(6)) नियंत्रक-महालेखापरीक्षक को वित्तीय वर्ष आरंभ होने के 180 दिन के भीतर किसी चार्टर्ड अकाउंटेंट को सांविधिक लेखापरीक्षक नियुक्त करने को कहता है; फिर नियंत्रक-महालेखापरीक्षक लेखापरीक्षा प्रतिवेदन पाने के 60 दिन के भीतर अनुपूरक लेखापरीक्षा कर सकते हैं और उस पर टिप्पणी या उसका अनुपूरण कर सकते हैं, और ये टिप्पणियाँ कंपनी की वार्षिक आम बैठक के समक्ष रखी जाती हैं। "
  "इसी दो-स्तरीय व्यवस्था के कारण सार्वजनिक उपक्रमों पर नियंत्रक-महालेखापरीक्षक के निष्कर्ष दूसरों द्वारा लेखापरीक्षित लेखाओं पर टिप्पणियों के रूप में आते हैं, और उन्हें केवल लोक लेखा समिति ही नहीं, सरकारी उपक्रमों संबंधी समिति भी उठाती है।",
  COI + ", Article 149; Comptroller and Auditor General's (Duties, Powers and Conditions of Service) Act, 1971, section 19; Companies Act, 2013, sections 139(5) and 143(6).",
  "l4-s01-pol-cag-govt-company-supplementary-audit", craft="linkage")

# ---------------------------------------------------------------- Constitutional Framework (pairs, hard)
P("Constitutional Framework", "hard", "Consider the following pairs of Articles of the Constitution and what they provide about the Supreme Court:",
  "संविधान के अनुच्छेदों और सर्वोच्च न्यायालय के बारे में उनके प्रावधानों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Article 130 : The Court sits in Delhi or at any other place that the Chief Justice of India appoints with the President's approval",
   "Article 139 : Parliament may by law empower the Court to issue writs for purposes other than the enforcement of Fundamental Rights",
   "Article 144 : All authorities, civil and judicial, in the territory of India shall act in aid of the Court",
   "Article 146 : The officers and servants of the Court are appointed by the President"],
  ["अनुच्छेद 130 : न्यायालय दिल्ली में या किसी अन्य स्थान पर बैठता है जिसे भारत के मुख्य न्यायाधीश राष्ट्रपति के अनुमोदन से नियत करें",
   "अनुच्छेद 139 : संसद विधि द्वारा न्यायालय को मौलिक अधिकारों के प्रवर्तन से भिन्न प्रयोजनों के लिए रिट जारी करने की शक्ति दे सकती है",
   "अनुच्छेद 144 : भारत के राज्यक्षेत्र के सभी सिविल और न्यायिक प्राधिकारी न्यायालय की सहायता में कार्य करेंगे",
   "अनुच्छेद 146 : न्यायालय के अधिकारियों और सेवकों की नियुक्ति राष्ट्रपति करते हैं"],
  2,
  "Only three pairs are correct. Article 130 makes Delhi the seat but lets the Chief Justice, with the President's approval, appoint other places, which is the constitutional basis of every proposal for regional benches. Article 139 lets Parliament widen the Court's writ jurisdiction beyond Article 32 -- a power never used, which is why the High Courts' wider writ power under Article 226 remains broader than the Supreme Court's. Article 144 binds every authority to act in aid of the Court, which underpins the enforcement of its orders. "
  "Pair 4 is wrong: under Article 146 the officers and servants of the Court are appointed by the Chief Justice of India, or by another judge or officer he directs; the President may only require, by rule, that the UPSC be consulted for some posts. Leaving staffing to the Chief Justice is part of the Court's administrative independence.",
  "केवल तीन युग्म सही हैं। अनुच्छेद 130 दिल्ली को स्थान बनाता है पर मुख्य न्यायाधीश को राष्ट्रपति के अनुमोदन से अन्य स्थान नियत करने देता है, जो क्षेत्रीय पीठों के हर प्रस्ताव का संवैधानिक आधार है। अनुच्छेद 139 संसद को न्यायालय की रिट अधिकारिता अनुच्छेद 32 से आगे बढ़ाने देता है -- ऐसी शक्ति जिसका कभी प्रयोग नहीं हुआ, इसी कारण अनुच्छेद 226 के अंतर्गत उच्च न्यायालयों की रिट शक्ति सर्वोच्च न्यायालय से व्यापक बनी हुई है। अनुच्छेद 144 हर प्राधिकारी को न्यायालय की सहायता में कार्य करने को बाध्य करता है, जिस पर उसके आदेशों का प्रवर्तन टिका है। "
  "युग्म 4 ग़लत है: अनुच्छेद 146 के अंतर्गत न्यायालय के अधिकारियों और सेवकों की नियुक्ति भारत के मुख्य न्यायाधीश, या उनके निर्देश पर कोई अन्य न्यायाधीश या अधिकारी, करते हैं; राष्ट्रपति केवल नियम द्वारा कुछ पदों के लिए संघ लोक सेवा आयोग से परामर्श अपेक्षित कर सकते हैं। कर्मचारियों की नियुक्ति मुख्य न्यायाधीश पर छोड़ना न्यायालय की प्रशासनिक स्वतंत्रता का भाग है।",
  COI + ", Articles 130, 139, 144 and 146.",
  "l4-s01-pol-sc-articles-130-139-144-146-pairs", craft="precision")

# ---------------------------------------------------------------- Constitutional Framework (statement, easy)
S("Constitutional Framework", "easy", "With reference to Article 340 of the Constitution, consider the following statements:",
  "संविधान के अनुच्छेद 340 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first commission appointed under it was chaired by Kaka Kalelkar.",
   "The Mandal Commission was appointed under it in 1990.",
   "It obliges the Government to implement the recommendations of a commission appointed under it."],
  ["इसके अंतर्गत नियुक्त पहले आयोग के अध्यक्ष काका कालेलकर थे।",
   "मंडल आयोग इसके अंतर्गत 1990 में नियुक्त किया गया।",
   "यह सरकार को इसके अंतर्गत नियुक्त आयोग की संस्तुतियाँ लागू करने के लिए बाध्य करता है।"],
  C3, 0,
  "Only statement 1 is correct. Article 340 lets the President appoint a commission to investigate the conditions of socially and educationally backward classes and the difficulties they face, and to recommend steps to improve their condition. The first such commission, under Kaka Kalelkar, was set up in 1953 and reported in 1955, but its report was not accepted, partly because it used caste as the criterion. "
  "Statement 2 is wrong: the second commission, under B. P. Mandal, was appointed in 1979 and reported in 1980; it was in 1990 that the Government announced 27 per cent reservation in central government jobs on its basis, which the Supreme Court upheld with the creamy-layer exclusion in Indra Sawhney (1992). Statement 3 is wrong: the President only lays the report before each House of Parliament, with a memorandum explaining the action taken; acting on it is a policy choice.",
  "केवल कथन 1 सही है। अनुच्छेद 340 राष्ट्रपति को सामाजिक और शैक्षिक रूप से पिछड़े वर्गों की दशाओं और उनकी कठिनाइयों की जाँच करने तथा उनकी दशा सुधारने के उपाय सुझाने के लिए आयोग नियुक्त करने देता है। ऐसा पहला आयोग, काका कालेलकर के अधीन, 1953 में बना और 1955 में प्रतिवेदन दिया, पर उसका प्रतिवेदन स्वीकार नहीं हुआ, कुछ इस कारण कि उसने जाति को कसौटी बनाया था। "
  "कथन 2 ग़लत है: बी. पी. मंडल के अधीन दूसरा आयोग 1979 में नियुक्त हुआ और 1980 में प्रतिवेदन दिया; 1990 में सरकार ने उसके आधार पर केंद्र सरकार की नौकरियों में 27 प्रतिशत आरक्षण की घोषणा की, जिसे सर्वोच्च न्यायालय ने इंद्रा साहनी (1992) में क्रीमी लेयर के अपवर्जन के साथ बरक़रार रखा। कथन 3 ग़लत है: राष्ट्रपति प्रतिवेदन को केवल की गई कार्रवाई को स्पष्ट करने वाले ज्ञापन के साथ संसद के प्रत्येक सदन के समक्ष रखवाते हैं; उस पर कार्य करना नीतिगत विकल्प है।",
  COI + ", Article 340; Report of the Backward Classes Commission (1955) and Report of the Backward Classes Commission (1980).",
  "l4-s01-pol-art340-kalelkar-mandal-1979-not-binding", craft="precision")

# ---------------------------------------------------------------- Federalism & Special Provisions (MCQ, medium)
M("Federalism & Special Provisions", "medium",
  "The Dhebar Commission (1960-61) and the Bhuria Commission (2002-04) were appointed under a provision of the Constitution that relates to",
  "ढेबर आयोग (1960-61) और भूरिया आयोग (2002-04) संविधान के जिस प्रावधान के अंतर्गत नियुक्त किए गए, वह संबंधित है",
  ["the administration of the Scheduled Areas and the welfare of the Scheduled Tribes",
   "the reorganisation of the States on the basis of the languages spoken in each of them",
   "the conditions of socially and educationally backward classes of citizens",
   "the review of the working of the Constitution after its first fifty years"],
  ["अनुसूचित क्षेत्रों के प्रशासन और अनुसूचित जनजातियों के कल्याण से",
   "राज्यों में से प्रत्येक में बोली जाने वाली भाषाओं के आधार पर उनके पुनर्गठन से",
   "नागरिकों के सामाजिक और शैक्षिक रूप से पिछड़े वर्गों की दशाओं से",
   "संविधान के पहले पचास वर्षों के बाद उसके कार्यकरण की समीक्षा से"],
  0,
  "Article 339(1) lets the President appoint, and required him to appoint ten years after the Constitution began, a commission to report on the administration of the Scheduled Areas and the welfare of the Scheduled Tribes. The commission under U. N. Dhebar, appointed in 1960, was the first; the one under Dilip Singh Bhuria, appointed in 2002, the second. Article 339(2) adds that the Union's executive power extends to directing a State to draw up and carry out schemes essential for the welfare of the Scheduled Tribes in it, one of the few places where the Constitution lets the Union direct a State on a welfare matter. "
  "Linguistic reorganisation followed the States Reorganisation Commission (1953-55), set up by executive resolution; commissions on backward classes are appointed under Article 340; and the review of the Constitution was the task of the National Commission to Review the Working of the Constitution (2000-02), also set up by resolution.",
  "अनुच्छेद 339(1) राष्ट्रपति को अनुसूचित क्षेत्रों के प्रशासन और अनुसूचित जनजातियों के कल्याण पर प्रतिवेदन देने के लिए आयोग नियुक्त करने देता है, और संविधान के प्रारंभ के दस वर्ष बाद ऐसा करना उनके लिए अनिवार्य था। 1960 में नियुक्त यू. एन. ढेबर के अधीन आयोग पहला था; 2002 में नियुक्त दिलीप सिंह भूरिया के अधीन आयोग दूसरा। अनुच्छेद 339(2) जोड़ता है कि संघ की कार्यपालिका शक्ति किसी राज्य को उसमें अनुसूचित जनजातियों के कल्याण के लिए आवश्यक योजनाएँ बनाने और लागू करने का निर्देश देने तक विस्तृत है, यह उन गिने-चुने स्थानों में है जहाँ संविधान संघ को किसी कल्याण-विषय पर राज्य को निर्देश देने देता है। "
  "भाषाई पुनर्गठन राज्य पुनर्गठन आयोग (1953-55) के बाद हुआ, जो कार्यकारी संकल्प से बना था; पिछड़े वर्गों संबंधी आयोग अनुच्छेद 340 के अंतर्गत नियुक्त होते हैं; और संविधान की समीक्षा संविधान के कार्यकरण की समीक्षा के लिए राष्ट्रीय आयोग (2000-02) का कार्य थी, जो भी संकल्प से बना था।",
  COI + ", Article 339; Report of the Scheduled Areas and Scheduled Tribes Commission (1961); Report of the Scheduled Areas and Scheduled Tribes Commission (2004).",
  "l4-s01-pol-art339-dhebar-bhuria-scheduled-areas", pos=3, craft="linkage")

# ---------------------------------------------------------------- Federalism & Special Provisions (statement, medium)
S("Federalism & Special Provisions", "medium", "With reference to the Scheduled Areas under the Fifth Schedule, consider the following statements:",
  "पाँचवीं अनुसूची के अंतर्गत अनुसूचित क्षेत्रों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Governor of a State having Scheduled Areas reports to the President on their administration every year, or whenever the President so requires.",
   "The executive power of the Union extends to giving directions to such a State about the administration of those areas.",
   "In the Samatha case, the Supreme Court held that a State may lease tribal land in a Scheduled Area to private mining companies."],
  ["अनुसूचित क्षेत्रों वाले राज्य का राज्यपाल उनके प्रशासन पर प्रति वर्ष, या जब भी राष्ट्रपति अपेक्षा करें, राष्ट्रपति को प्रतिवेदन देता है।",
   "संघ की कार्यपालिका शक्ति ऐसे राज्य को उन क्षेत्रों के प्रशासन के बारे में निर्देश देने तक विस्तृत है।",
   "समता मामले में सर्वोच्च न्यायालय ने कहा कि राज्य अनुसूचित क्षेत्र की जनजातीय भूमि निजी खनन कंपनियों को पट्टे पर दे सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Paragraph 3 of the Fifth Schedule requires the Governor's report and extends the Union's executive power to directions on the administration of these areas -- a deliberate departure from the ordinary federal division, because the Constitution treats the protection of the Scheduled Tribes as a shared national responsibility. "
  "Statement 3 is wrong: in Samatha v. State of Andhra Pradesh (1997) the Court held the opposite -- that leases of tribal land in Scheduled Areas to private, non-tribal mining companies were void under the State's land-transfer regulations read with the Fifth Schedule, so that mining there could be carried on only by a State undertaking or by cooperatives of the tribal people. The ruling shaped later debates on mining in tribal areas, including the role of the gram sabha.",
  "कथन 1 और 2 सही हैं। पाँचवीं अनुसूची का पैरा 3 राज्यपाल का प्रतिवेदन अनिवार्य करता है और इन क्षेत्रों के प्रशासन पर निर्देश देने तक संघ की कार्यपालिका शक्ति बढ़ाता है -- सामान्य संघीय बँटवारे से यह जान-बूझकर किया गया विचलन है, क्योंकि संविधान अनुसूचित जनजातियों के संरक्षण को साझा राष्ट्रीय दायित्व मानता है। "
  "कथन 3 ग़लत है: समता बनाम आंध्र प्रदेश राज्य (1997) में न्यायालय ने उलटा कहा -- कि अनुसूचित क्षेत्रों की जनजातीय भूमि के निजी, गैर-जनजातीय खनन कंपनियों को पट्टे पाँचवीं अनुसूची के साथ पढ़े गए राज्य के भूमि-अंतरण विनियमों के अंतर्गत शून्य थे, इसलिए वहाँ खनन केवल राज्य के उपक्रम या जनजातीय लोगों की सहकारी समितियाँ कर सकती थीं। इस निर्णय ने जनजातीय क्षेत्रों में खनन पर बाद की बहसों को, ग्राम सभा की भूमिका सहित, आकार दिया।",
  COI + ", Fifth Schedule, paragraph 3; Samatha v. State of Andhra Pradesh (1997) 8 SCC 191.",
  "l4-s01-pol-fifth-schedule-governor-report-union-directions-samatha", craft="linkage")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (statement, medium)
S("Fundamental Rights, DPSP & Duties", "medium", "With reference to the right of minorities to establish and administer educational institutions, consider the following statements:",
  "अल्पसंख्यकों के शिक्षा संस्थाओं की स्थापना और प्रशासन के अधिकार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["If the State acquires the property of such an institution, the law must fix an amount that does not restrict or abrogate the right.",
   "The right belongs only to religious minorities, not to linguistic minorities.",
   "The safeguard on acquisition in statement 1 was added when the right to property was removed from Part III of the Constitution."],
  ["यदि राज्य ऐसी संस्था की संपत्ति अर्जित करता है, तो विधि को ऐसी राशि तय करनी होगी जो उस अधिकार को सीमित या निराकृत न करे।",
   "यह अधिकार केवल धार्मिक अल्पसंख्यकों का है, भाषाई अल्पसंख्यकों का नहीं।",
   "कथन 1 वाला अर्जन संबंधी संरक्षण तब जोड़ा गया जब संपत्ति का अधिकार संविधान के भाग III से हटाया गया।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Forty-fourth Amendment (1978) deleted the fundamental right to property (Article 31) and made property a constitutional right under Article 300A, which carries no guarantee of compensation. To keep minority institutions from being starved of property under that new regime, it inserted Article 30(1A): when the State compulsorily acquires the property of a minority educational institution, the amount fixed must not restrict or abrogate the right guaranteed by Article 30(1). "
  "Statement 2 is wrong: Article 30(1) protects all minorities, 'whether based on religion or language', and the Supreme Court has held that minority status is judged with reference to the State concerned, since States are organised largely on linguistic lines.",
  "कथन 1 और 3 सही हैं। चवालीसवें संशोधन (1978) ने संपत्ति का मौलिक अधिकार (अनुच्छेद 31) हटाया और संपत्ति को अनुच्छेद 300क के अंतर्गत संवैधानिक अधिकार बनाया, जिसमें प्रतिकर की कोई गारंटी नहीं है। उस नई व्यवस्था में अल्पसंख्यक संस्थाओं को संपत्ति से वंचित होने से बचाने के लिए उसने अनुच्छेद 30(1क) जोड़ा: जब राज्य किसी अल्पसंख्यक शिक्षा संस्था की संपत्ति का अनिवार्य अर्जन करे, तो तय राशि अनुच्छेद 30(1) द्वारा प्रत्याभूत अधिकार को सीमित या निराकृत न करे। "
  "कथन 2 ग़लत है: अनुच्छेद 30(1) सभी अल्पसंख्यकों की रक्षा करता है, ‘चाहे वे धर्म पर आधारित हों या भाषा पर’, और सर्वोच्च न्यायालय ने कहा है कि अल्पसंख्यक स्थिति संबंधित राज्य के संदर्भ में आँकी जाती है, क्योंकि राज्य बड़े पैमाने पर भाषाई आधार पर गठित हैं।",
  COI + ", Articles 30(1), 30(1A) and 300A; Constitution (Forty-fourth Amendment) Act, 1978.",
  "l4-s01-pol-art30-1a-acquisition-44th-linguistic", craft="linkage")

# ---------------------------------------------------------------- Governance (statement, hard)
S("Governance", "hard", "With reference to the constitutional position of civil servants, consider the following statements:",
  "सिविल सेवकों की संवैधानिक स्थिति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Until Parliament makes a law on the subject, rules made by the President can regulate the recruitment and conditions of service of persons serving the Union.",
   "A civil servant can be dismissed without an inquiry if the President is satisfied that holding one is not expedient in the interest of the security of the State.",
   "No inquiry is needed before dismissing a civil servant on the ground of conduct that has led to his conviction on a criminal charge."],
  ["जब तक संसद इस विषय पर विधि न बनाए, राष्ट्रपति द्वारा बनाए गए नियम संघ की सेवा में लगे व्यक्तियों की भर्ती और सेवा-शर्तों का विनियमन कर सकते हैं।",
   "यदि राष्ट्रपति संतुष्ट हों कि राज्य की सुरक्षा के हित में जाँच करना समीचीन नहीं है, तो किसी सिविल सेवक को बिना जाँच के पदच्युत किया जा सकता है।",
   "किसी सिविल सेवक को उस आचरण के आधार पर पदच्युत करने से पहले जाँच आवश्यक नहीं है जिसके कारण उसे आपराधिक आरोप में दोषसिद्ध किया गया हो।"],
  C3, 2,
  "All three statements are correct. Article 309 lets the legislature regulate recruitment and conditions of service, and its proviso lets the President (for the Union) and the Governor (for a State) make rules until a law is made; most service rules, such as the Central Civil Services rules, rest on this proviso, since Parliament has passed few such laws. "
  "Article 311(2) requires an inquiry, with a reasonable opportunity of being heard, before a civil servant is dismissed, removed or reduced in rank, but its second proviso lists three exceptions: conduct that has led to conviction on a criminal charge; cases in which the authority, for reasons recorded in writing, finds an inquiry not reasonably practicable; and cases in which the President or Governor is satisfied that an inquiry is not expedient in the interest of the security of the State. These exceptions temper the doctrine of pleasure in Article 310 with procedure, while keeping the State able to act in emergencies.",
  "तीनों कथन सही हैं। अनुच्छेद 309 विधानमंडल को भर्ती और सेवा-शर्तों का विनियमन करने देता है, और उसका परंतुक विधि बनने तक राष्ट्रपति (संघ के लिए) और राज्यपाल (राज्य के लिए) को नियम बनाने देता है; अधिकांश सेवा नियम, जैसे केंद्रीय सिविल सेवा नियम, इसी परंतुक पर टिके हैं, क्योंकि संसद ने ऐसी कम विधियाँ बनाई हैं। "
  "अनुच्छेद 311(2) किसी सिविल सेवक की पदच्युति, हटाए जाने या पंक्ति में अवनति से पहले सुनवाई के युक्तियुक्त अवसर सहित जाँच अनिवार्य करता है, पर उसका दूसरा परंतुक तीन अपवाद गिनाता है: वह आचरण जिसके कारण आपराधिक आरोप पर दोषसिद्धि हुई; वे मामले जिनमें प्राधिकारी, लिखित कारणों से, जाँच को युक्तियुक्त रूप से साध्य नहीं पाता; और वे मामले जिनमें राष्ट्रपति या राज्यपाल संतुष्ट हों कि राज्य की सुरक्षा के हित में जाँच समीचीन नहीं। ये अपवाद अनुच्छेद 310 के प्रसाद-सिद्धांत को प्रक्रिया से संतुलित करते हैं, और राज्य को आपात स्थिति में कार्य करने योग्य भी रखते हैं।",
  COI + ", Articles 309, 310 and 311; Union of India v. Tulsiram Patel (1985).",
  "l4-s01-pol-art309-proviso-311-2-exceptions", craft="precision")

# ---------------------------------------------------------------- Governance (statement, medium)
S("Governance", "medium", "With reference to compensation for victims of crime in India, consider the following statements:",
  "भारत में अपराध-पीड़ितों के प्रतिकर के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Every State Government is required by law to prepare a scheme for compensating victims of crime.",
   "Compensation under such a scheme can be paid only after the offender has been convicted.",
   "A victim can apply for compensation even when the offender has not been traced or identified."],
  ["प्रत्येक राज्य सरकार के लिए विधि द्वारा अपराध-पीड़ितों के प्रतिकर की एक योजना बनाना अनिवार्य है।",
   "ऐसी योजना के अंतर्गत प्रतिकर अपराधी की दोषसिद्धि के बाद ही दिया जा सकता है।",
   "अपराधी का पता न चलने या उसकी पहचान न होने पर भी पीड़ित प्रतिकर के लिए आवेदन कर सकता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Section 396 of the Bharatiya Nagarik Suraksha Sanhita, 2023, carrying forward section 357A of the old Code of Criminal Procedure (added in 2009), requires every State Government, in coordination with the Centre, to prepare a scheme for compensating victims or their dependants who need rehabilitation; the district or State legal services authority decides the amount. Where the offender is not traced or identified but the victim is, and no trial takes place, the victim or the dependants may apply to the legal services authority. "
  "Statement 2 is wrong: compensation does not wait for a conviction -- it can be recommended by the trial court even after an acquittal or discharge, and the legal services authority can order immediate first aid or medical benefits. The scheme reflects a shift in criminal justice from punishing the offender alone towards restoring the victim.",
  "कथन 1 और 3 सही हैं। भारतीय नागरिक सुरक्षा संहिता, 2023 की धारा 396, पुरानी दंड प्रक्रिया संहिता की धारा 357क (2009 में जोड़ी गई) को आगे बढ़ाते हुए, प्रत्येक राज्य सरकार से केंद्र के समन्वय से उन पीड़ितों या उनके आश्रितों के प्रतिकर की योजना बनाने की अपेक्षा करती है जिन्हें पुनर्वास की आवश्यकता है; राशि ज़िला या राज्य विधिक सेवा प्राधिकरण तय करता है। जहाँ अपराधी का पता न चले या पहचान न हो पर पीड़ित की पहचान हो, और कोई विचारण न हो, वहाँ पीड़ित या आश्रित विधिक सेवा प्राधिकरण को आवेदन कर सकते हैं। "
  "कथन 2 ग़लत है: प्रतिकर दोषसिद्धि की प्रतीक्षा नहीं करता -- विचारण न्यायालय दोषमुक्ति या उन्मोचन के बाद भी इसकी संस्तुति कर सकता है, और विधिक सेवा प्राधिकरण तत्काल प्राथमिक उपचार या चिकित्सा सुविधा का आदेश दे सकता है। यह योजना आपराधिक न्याय में केवल अपराधी को दंड देने से पीड़ित की बहाली की ओर बदलाव को दर्शाती है।",
  "Bharatiya Nagarik Suraksha Sanhita, 2023, section 396; Code of Criminal Procedure, 1973, section 357A (inserted 2009); Legal Services Authorities Act, 1987.",
  "l4-s01-pol-victim-compensation-396-bnss-untraced-offender", craft="application")

# ---------------------------------------------------------------- Judicial-Verdicts (pairs, easy)
P("Judicial-Verdicts", "easy", "Consider the following pairs of Supreme Court judgments and what they decided:",
  "सर्वोच्च न्यायालय के निर्णयों और उनमें तय की गई बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Nandini Sundar v. State of Chhattisgarh (2011) : Held unconstitutional the arming of tribal youth as special police officers against Maoists",
   "Supriyo v. Union of India (2023) : Declined to read a right of same-sex couples to marry into the Special Marriage Act",
   "Laxmi v. Union of India : Struck down Section 377 of the Indian Penal Code",
   "Vishaka v. State of Rajasthan (1997) : Held that the right to privacy is a fundamental right"],
  ["नंदिनी सुंदर बनाम छत्तीसगढ़ राज्य (2011) : माओवादियों के विरुद्ध जनजातीय युवाओं को विशेष पुलिस अधिकारी के रूप में सशस्त्र करना असंवैधानिक माना",
   "सुप्रियो बनाम भारत संघ (2023) : विशेष विवाह अधिनियम में समलैंगिक जोड़ों के विवाह के अधिकार को पढ़ने से इनकार किया",
   "लक्ष्मी बनाम भारत संघ : भारतीय दंड संहिता की धारा 377 निरस्त की",
   "विशाखा बनाम राजस्थान राज्य (1997) : निजता के अधिकार को मौलिक अधिकार माना"],
  1,
  "Only two pairs are correct. In Nandini Sundar the Court struck down the Salwa Judum model of arming barely trained tribal youth as special police officers, holding that it violated Articles 14 and 21 of both the youths and the people they were set against. In Supriyo (2023) a five-judge bench unanimously held that there is no unqualified fundamental right to marry and that the Special Marriage Act cannot be read to include same-sex couples; by 3:2 it also declined to recognise civil unions, leaving the question to Parliament. "
  "Pair 3 is wrong: Laxmi v. Union of India, brought by an acid-attack survivor, led to directions regulating the sale of acid and on compensation and treatment for survivors; Section 377 was read down in Navtej Singh Johar (2018). Pair 4 is wrong: Vishaka laid down guidelines against sexual harassment at the workplace, later enacted as the POSH Act, 2013; privacy was declared a fundamental right in K. S. Puttaswamy (2017).",
  "केवल दो युग्म सही हैं। नंदिनी सुंदर में न्यायालय ने बमुश्किल प्रशिक्षित जनजातीय युवाओं को विशेष पुलिस अधिकारी बनाकर सशस्त्र करने के सलवा जुडूम मॉडल को निरस्त किया, यह मानते हुए कि इससे उन युवाओं और जिनके विरुद्ध उन्हें खड़ा किया गया उन लोगों, दोनों के अनुच्छेद 14 और 21 का उल्लंघन होता है। सुप्रियो (2023) में पाँच न्यायाधीशों की पीठ ने सर्वसम्मति से कहा कि विवाह का कोई अप्रतिबंधित मौलिक अधिकार नहीं है और विशेष विवाह अधिनियम को समलैंगिक जोड़ों को शामिल करने के लिए नहीं पढ़ा जा सकता; 3:2 से उसने सिविल यूनियन को मान्यता देने से भी इनकार किया, प्रश्न संसद पर छोड़ते हुए। "
  "युग्म 3 ग़लत है: एक एसिड-हमले की उत्तरजीवी द्वारा लाया गया लक्ष्मी बनाम भारत संघ एसिड की बिक्री के विनियमन तथा उत्तरजीवियों के प्रतिकर और उपचार संबंधी निर्देशों का कारण बना; धारा 377 को नवतेज सिंह जौहर (2018) में सीमित किया गया। युग्म 4 ग़लत है: विशाखा ने कार्यस्थल पर यौन उत्पीड़न के विरुद्ध दिशानिर्देश दिए, जो बाद में पॉश अधिनियम, 2013 बने; निजता को मौलिक अधिकार के. एस. पुट्टस्वामी (2017) में घोषित किया गया।",
  "Nandini Sundar v. State of Chhattisgarh (2011) 7 SCC 547; Supriyo v. Union of India (2023); Laxmi v. Union of India (2014) 4 SCC 427; Vishaka v. State of Rajasthan (1997) 6 SCC 241.",
  "l4-s01-pol-verdicts-nandini-sundar-supriyo-laxmi-vishaka", craft="recall")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (AR, hard)
A("Panchayati Raj & Local Governance", "hard",
  "The provisions of Part IXA of the Constitution, on municipalities, do not apply to the Scheduled Areas.",
  "नगरपालिकाओं संबंधी संविधान के भाग 9क के प्रावधान अनुसूचित क्षेत्रों पर लागू नहीं होते।",
  "Parliament has extended Part IXA to the Scheduled Areas by a law corresponding to the Panchayats (Extension to the Scheduled Areas) Act, 1996.",
  "संसद ने पंचायत (अनुसूचित क्षेत्रों पर विस्तार) अधिनियम, 1996 के अनुरूप एक विधि द्वारा भाग 9क को अनुसूचित क्षेत्रों तक विस्तारित किया है।",
  2,
  "Statement I is correct, but Statement II is incorrect. Article 243ZC keeps Part IXA out of the Scheduled Areas under Article 244(1) and the tribal areas under Article 244(2), and lets Parliament extend it to them by law, with such exceptions and modifications as it specifies -- the same design as Article 243M for panchayats. Parliament used that power for panchayats in PESA, 1996, which gave the gram sabhas of Scheduled Areas powers over land, minor forest produce and local disputes. "
  "Statement II is wrong: a corresponding law for municipalities, the Municipalities (Extension to the Scheduled Areas) Bill, was drafted in 2001 but never enacted. Towns in Scheduled Areas are therefore run under ordinary State municipal laws whose application there has been contested, a gap that matters as tribal districts urbanise.",
  "कथन I सही है, पर कथन II ग़लत है। अनुच्छेद 243यग भाग 9क को अनुच्छेद 244(1) के अनुसूचित क्षेत्रों और अनुच्छेद 244(2) के जनजातीय क्षेत्रों से बाहर रखता है, और संसद को विधि द्वारा, अपने बताए अपवादों और उपांतरणों के साथ, इसे उन तक विस्तारित करने देता है -- पंचायतों के लिए अनुच्छेद 243ड जैसी ही रचना। संसद ने पंचायतों के लिए इस शक्ति का उपयोग 1996 के पेसा अधिनियम में किया, जिसने अनुसूचित क्षेत्रों की ग्राम सभाओं को भूमि, लघु वनोपज और स्थानीय विवादों पर शक्तियाँ दीं। "
  "कथन II ग़लत है: नगरपालिकाओं के लिए ऐसी विधि, नगरपालिका (अनुसूचित क्षेत्रों पर विस्तार) विधेयक, 2001 में प्रारूपित हुई पर कभी अधिनियमित नहीं हुई। इसलिए अनुसूचित क्षेत्रों के नगर साधारण राज्य नगरपालिका विधियों के अंतर्गत चलते हैं, जिनका वहाँ लागू होना विवादित रहा है, और जनजातीय ज़िलों के नगरीकरण के साथ यह कमी महत्त्वपूर्ण होती जा रही है।",
  COI + ", Articles 243M, 243ZC and 244; Panchayats (Extension to the Scheduled Areas) Act, 1996; Ministry of Panchayati Raj, draft Municipalities (Extension to the Scheduled Areas) Bill (2001).",
  "l4-s01-pol-art243zc-part-ixa-scheduled-areas-mesa-unenacted", craft="linkage")

# ---------------------------------------------------------------- Parliament & State Legislature (MCQ, medium)
M("Parliament & State Legislature", "medium",
  "While a resolution for the removal of the Speaker of the Lok Sabha is under consideration, the Speaker",
  "जब लोकसभा अध्यक्ष को हटाने का संकल्प विचाराधीन हो, तब अध्यक्ष",
  ["cannot preside, but may speak and vote on the resolution in the first instance",
   "may preside over the sitting but cannot vote on the resolution at any stage",
   "must stay away from the House until the resolution has been disposed of",
   "cannot speak in the House, but may cast a vote if the votes are equally divided"],
  ["पीठासीन नहीं हो सकता, पर बोल सकता है और संकल्प पर प्रथमतः मत दे सकता है",
   "बैठक की अध्यक्षता कर सकता है पर किसी भी चरण में संकल्प पर मत नहीं दे सकता",
   "संकल्प का निपटारा होने तक सदन से दूर रहना होगा",
   "सदन में बोल नहीं सकता, पर मत बराबर बँटने पर मत दे सकता है"],
  0,
  "Under Article 96 the Speaker does not preside at a sitting while a resolution for his or her removal is under consideration -- no one judges his own cause -- but keeps the rights of a member: to speak, to take part in the proceedings and to vote in the first instance on the resolution or any other matter, though not to give a casting vote if the votes are tied. The Deputy Speaker is in the same position when a resolution to remove the Deputy Speaker is taken up. "
  "Presiding while one's own removal is debated would breach natural justice, so that option is wrong; nothing requires the Speaker to leave the House; and the casting vote under Article 100 is the one power the Speaker loses during such proceedings, not the only one kept. Article 181 makes the same provision for the Speaker of a State Legislative Assembly.",
  "अनुच्छेद 96 के अंतर्गत जब अध्यक्ष को हटाने का संकल्प विचाराधीन हो, तब अध्यक्ष उस बैठक में पीठासीन नहीं होता -- कोई अपने ही मामले में न्यायाधीश नहीं होता -- पर सदस्य के अधिकार बनाए रखता है: बोलना, कार्यवाही में भाग लेना और संकल्प या किसी अन्य विषय पर प्रथमतः मत देना, यद्यपि मत बराबर होने पर निर्णायक मत नहीं। उपाध्यक्ष को हटाने का संकल्प उठने पर उपाध्यक्ष की स्थिति भी यही होती है। "
  "अपने ही हटाए जाने की बहस में पीठासीन होना नैसर्गिक न्याय का उल्लंघन होगा, इसलिए वह विकल्प ग़लत है; अध्यक्ष के लिए सदन छोड़ना आवश्यक नहीं; और अनुच्छेद 100 का निर्णायक मत ही वह शक्ति है जो ऐसी कार्यवाही में अध्यक्ष खोता है, बची रहने वाली एकमात्र शक्ति नहीं। अनुच्छेद 181 राज्य विधानसभा के अध्यक्ष के लिए यही प्रावधान करता है।",
  COI + ", Articles 96, 100 and 181.",
  "l4-s01-pol-art96-speaker-removal-not-preside-first-vote", pos=2, craft="precision")

# ---------------------------------------------------------------- Parliament & State Legislature (statement, hard)
S("Parliament & State Legislature", "hard", "Who decides the following questions? Consider the following statements:",
  "निम्नलिखित प्रश्नों का निर्णय कौन करता है? निम्नलिखित कथनों पर विचार कीजिए:",
  ["Whether a member of a State Legislative Assembly has become disqualified by holding an office of profit is decided by the Governor, acting according to the opinion of the Election Commission.",
   "Whether such a member has become disqualified on the ground of defection is decided by the Speaker of the Assembly.",
   "A dispute about the election of the Vice-President is decided by the Election Commission."],
  ["राज्य विधानसभा का कोई सदस्य लाभ का पद धारण करने से निरर्हित हुआ है या नहीं, इसका निर्णय राज्यपाल निर्वाचन आयोग की राय के अनुसार करता है।",
   "ऐसा सदस्य दल-बदल के आधार पर निरर्हित हुआ है या नहीं, इसका निर्णय विधानसभा अध्यक्ष करता है।",
   "उपराष्ट्रपति के निर्वाचन संबंधी विवाद का निर्णय निर्वाचन आयोग करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Constitution assigns different deciders to different grounds. Disqualifications under Article 191(1) -- office of profit, unsound mind, insolvency, loss of citizenship or a disqualification under a law of Parliament -- are decided under Article 192 by the Governor, whose decision is final but who must act according to the opinion of the Election Commission; Article 103 makes the same provision for members of Parliament, with the President in place of the Governor. "
  "Disqualification for defection under the Tenth Schedule is decided by the Speaker or Chairman (paragraph 6), subject to judicial review since Kihoto Hollohan (1992). Statement 3 is wrong: under Article 71 disputes about the election of the President or the Vice-President are inquired into and decided only by the Supreme Court; the Election Commission conducts the election but does not judge disputes about it.",
  "कथन 1 और 2 सही हैं। संविधान अलग-अलग आधारों के लिए अलग-अलग निर्णायक तय करता है। अनुच्छेद 191(1) की निरर्हताएँ -- लाभ का पद, विकृतचित्तता, दिवालियापन, नागरिकता का अंत या संसद की किसी विधि के अंतर्गत निरर्हता -- अनुच्छेद 192 के अंतर्गत राज्यपाल तय करता है, जिसका निर्णय अंतिम है पर जिसे निर्वाचन आयोग की राय के अनुसार कार्य करना होता है; अनुच्छेद 103 संसद-सदस्यों के लिए यही प्रावधान करता है, राज्यपाल के स्थान पर राष्ट्रपति के साथ। "
  "दसवीं अनुसूची के अंतर्गत दल-बदल की निरर्हता अध्यक्ष या सभापति (पैरा 6) तय करते हैं, जो किहोतो होलोहन (1992) से न्यायिक पुनर्विलोकन के अधीन है। कथन 3 ग़लत है: अनुच्छेद 71 के अंतर्गत राष्ट्रपति या उपराष्ट्रपति के निर्वाचन संबंधी विवादों की जाँच और निर्णय केवल सर्वोच्च न्यायालय करता है; निर्वाचन आयोग निर्वाचन संचालित करता है पर उससे जुड़े विवादों का निर्णय नहीं करता।",
  COI + ", Articles 71, 103, 191 and 192 and the Tenth Schedule, paragraph 6; Kihoto Hollohan v. Zachillhu (1992).",
  "l4-s01-pol-who-decides-192-tenth-schedule-art71", craft="application")

# ---------------------------------------------------------------- Parliament & State Legislature (statement, medium)
S("Parliament & State Legislature", "medium", "With reference to the committees of Parliament, consider the following statements:",
  "संसद की समितियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Committee on the Welfare of Scheduled Castes and Scheduled Tribes consists of members of the Lok Sabha only.",
   "The Joint Committee on Offices of Profit decides finally whether a member of Parliament has become disqualified.",
   "The Committee on Empowerment of Women consists of members of the Lok Sabha only."],
  ["अनुसूचित जातियों और अनुसूचित जनजातियों के कल्याण संबंधी समिति में केवल लोकसभा के सदस्य होते हैं।",
   "लाभ के पदों संबंधी संयुक्त समिति अंतिम रूप से तय करती है कि कोई संसद-सदस्य निरर्हित हुआ है या नहीं।",
   "महिला सशक्तीकरण संबंधी समिति में केवल लोकसभा के सदस्य होते हैं।"],
  C3, 3,
  "None of the statements is correct. Statements 1 and 3 are wrong: the Committee on the Welfare of Scheduled Castes and Scheduled Tribes (set up in 1968) and the Committee on Empowerment of Women (set up in 1997) each have 30 members, 20 from the Lok Sabha and 10 from the Rajya Sabha; they examine the reports of the national commissions concerned and the working of welfare programmes, keeping the executive answerable on subjects that cut across ministries. "
  "Statement 2 is wrong: the Joint Committee on Offices of Profit, with 15 members (10 from the Lok Sabha, 5 from the Rajya Sabha), examines committees and bodies set up by governments and recommends which offices should or should not disqualify their holders; Parliament then exempts offices by amending the Parliament (Prevention of Disqualification) Act, 1959. Whether a sitting member has become disqualified is decided by the President on the Election Commission's opinion, under Article 103.",
  "कोई भी कथन सही नहीं है। कथन 1 और 3 ग़लत हैं: अनुसूचित जातियों और अनुसूचित जनजातियों के कल्याण संबंधी समिति (1968 में गठित) और महिला सशक्तीकरण संबंधी समिति (1997 में गठित) में से प्रत्येक में 30 सदस्य हैं, 20 लोकसभा से और 10 राज्यसभा से; ये संबंधित राष्ट्रीय आयोगों के प्रतिवेदनों और कल्याण कार्यक्रमों के कार्यकरण की जाँच करती हैं, और कई मंत्रालयों से जुड़े विषयों पर कार्यपालिका को उत्तरदायी रखती हैं। "
  "कथन 2 ग़लत है: 15 सदस्यों (10 लोकसभा से, 5 राज्यसभा से) वाली लाभ के पदों संबंधी संयुक्त समिति सरकारों द्वारा गठित समितियों और निकायों की जाँच करती है और संस्तुति करती है कि कौन-से पद धारकों को निरर्हित करें या न करें; संसद फिर संसद (निरर्हता निवारण) अधिनियम, 1959 में संशोधन करके पदों को छूट देती है। कोई वर्तमान सदस्य निरर्हित हुआ है या नहीं, यह अनुच्छेद 103 के अंतर्गत राष्ट्रपति निर्वाचन आयोग की राय पर तय करते हैं।",
  "Lok Sabha Secretariat, Parliamentary Committees (Committee on the Welfare of SCs and STs, Committee on Empowerment of Women, Joint Committee on Offices of Profit); Parliament (Prevention of Disqualification) Act, 1959; " + COI + ", Article 103.",
  "l4-s01-pol-committees-sc-st-women-jcop-composition", craft="precision")

# ---------------------------------------------------------------- Statutory-Laws (MCQ, medium)
M("Statutory-Laws", "medium",
  "The Protection of Interests in Aircraft Objects Act, 2025 gives legal force in India to",
  "विमान वस्तुओं में हितों का संरक्षण अधिनियम, 2025 भारत में किसे विधिक बल प्रदान करता है?",
  ["the Cape Town Convention on interests in mobile equipment, with its aircraft protocol",
   "the Chicago Convention on international civil aviation, which set up the ICAO",
   "the Montreal Convention on the liability of air carriers towards their passengers and their cargo",
   "the Tokyo Convention on offences committed on board an aircraft in flight"],
  ["चल उपकरणों में हितों पर केप टाउन अभिसमय को, उसके विमान प्रोटोकॉल सहित",
   "अंतरराष्ट्रीय नागरिक विमानन पर शिकागो अभिसमय को, जिसने आईसीएओ स्थापित किया",
   "अपने यात्रियों और माल के प्रति विमान वाहकों के दायित्व पर मॉन्ट्रियल अभिसमय को",
   "उड़ान में विमान पर किए गए अपराधों पर टोक्यो अभिसमय को"],
  0,
  "The Act gives force of law to the Cape Town Convention (2001) and its Protocol on aircraft equipment, which India had acceded to in 2008 without giving them domestic effect. It lets lessors and lenders register their interests in aircraft, engines and helicopters in an international registry and, on default, repossess and export the asset within set time limits -- an issue that came to a head when a domestic airline collapsed in 2023 and lessors could not recover their aircraft. Stronger creditor rights are expected to lower leasing costs for Indian airlines, since most of their fleets are leased. "
  "The Chicago Convention (1944) created the International Civil Aviation Organization; the Montreal Convention (1999) governs carriers' liability for passengers, baggage and cargo; the Tokyo Convention (1963) deals with offences on board.",
  "यह अधिनियम केप टाउन अभिसमय (2001) और विमान उपकरण संबंधी उसके प्रोटोकॉल को विधि का बल देता है, जिन्हें भारत ने 2008 में स्वीकार किया था पर घरेलू प्रभाव नहीं दिया था। यह पट्टादाताओं और ऋणदाताओं को विमानों, इंजनों और हेलिकॉप्टरों में अपने हित एक अंतरराष्ट्रीय रजिस्ट्री में दर्ज कराने और चूक होने पर तय समय-सीमा में परिसंपत्ति वापस लेने और निर्यात करने देता है -- यह मुद्दा तब उभरा जब 2023 में एक घरेलू एयरलाइन ढह गई और पट्टादाता अपने विमान वापस नहीं ले सके। सशक्त ऋणदाता-अधिकारों से भारतीय एयरलाइनों की पट्टा-लागत घटने की आशा है, क्योंकि उनके अधिकांश बेड़े पट्टे पर हैं। "
  "शिकागो अभिसमय (1944) ने अंतरराष्ट्रीय नागरिक विमानन संगठन बनाया; मॉन्ट्रियल अभिसमय (1999) यात्रियों, सामान और माल के प्रति वाहकों के दायित्व को नियंत्रित करता है; टोक्यो अभिसमय (1963) विमान पर अपराधों से संबंधित है।",
  "Protection of Interests in Aircraft Objects Act, 2025; Ministry of Civil Aviation (PIB, April 2025); Convention on International Interests in Mobile Equipment (Cape Town, 2001) and Aircraft Protocol.",
  "l4-s01-pol-aircraft-objects-act-2025-cape-town", pos=3, craft="recall")

# ---------------------------------------------------------------- Statutory-Laws (statement, medium)
S("Statutory-Laws", "medium", "Parliament replaced several old shipping laws in 2025. With reference to the new laws, consider the following statements:",
  "संसद ने 2025 में कई पुराने नौवहन क़ानूनों को बदला। नए क़ानूनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Carriage of Goods by Sea Act, 2025 replaced a law of 1925 that governed the liability of carriers for cargo.",
   "Trade along the Indian coast, including the licensing of foreign ships for it, is now governed by a separate Coastal Shipping Act.",
   "The Directorate General of Shipping was abolished and its functions were given to the Indian Ports Association."],
  ["समुद्र द्वारा माल का वहन अधिनियम, 2025 ने 1925 के उस क़ानून का स्थान लिया जो माल के प्रति वाहकों के दायित्व को नियंत्रित करता था।",
   "भारतीय तट के साथ व्यापार, उसके लिए विदेशी जहाज़ों के लाइसेंस सहित, अब एक अलग तटीय नौवहन अधिनियम से नियंत्रित होता है।",
   "नौवहन महानिदेशालय को समाप्त करके उसके कार्य भारतीय पत्तन संघ को सौंप दिए गए।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Carriage of Goods by Sea Act, 2025 replaced the Indian Carriage of Goods by Sea Act, 1925, keeping the internationally used Hague-Visby framework of carriers' duties and liability limits but in a modern statute that the Centre can update by notification. The Merchant Shipping Act, 2025 replaced the 1958 Act, and the coasting trade -- earlier in Part XIV of that Act -- moved to the Coastal Shipping Act, 2025, which keeps priority for Indian ships but lets the regulator license foreign vessels when Indian capacity falls short. "
  "Statement 3 is wrong: the maritime regulator was not abolished; it continues as the Directorate General of Maritime Administration. The Indian Ports Association is a society of the major ports, not a regulator.",
  "कथन 1 और 2 सही हैं। समुद्र द्वारा माल का वहन अधिनियम, 2025 ने भारतीय समुद्र द्वारा माल का वहन अधिनियम, 1925 का स्थान लिया, वाहकों के कर्तव्यों और दायित्व-सीमाओं का अंतरराष्ट्रीय रूप से प्रयुक्त हेग-विस्बी ढाँचा रखते हुए पर एक आधुनिक क़ानून में जिसे केंद्र अधिसूचना से अद्यतन कर सकता है। वाणिज्य पोत परिवहन अधिनियम, 2025 ने 1958 के अधिनियम का स्थान लिया, और तटीय व्यापार -- जो पहले उस अधिनियम के भाग XIV में था -- तटीय नौवहन अधिनियम, 2025 में गया, जो भारतीय जहाज़ों की प्राथमिकता रखता है पर भारतीय क्षमता कम पड़ने पर नियामक को विदेशी जहाज़ों को लाइसेंस देने देता है। "
  "कथन 3 ग़लत है: समुद्री नियामक समाप्त नहीं हुआ; वह समुद्री प्रशासन महानिदेशालय के रूप में बना हुआ है। भारतीय पत्तन संघ प्रमुख पत्तनों की एक सोसायटी है, नियामक नहीं।",
  "Carriage of Goods by Sea Act, 2025; Merchant Shipping Act, 2025 (Act 24 of 2025, in force 15 March 2026); Coastal Shipping Act, 2025; Directorate General of Maritime Administration, circulars (2026).",
  "l4-s01-pol-shipping-laws-2025-cogsa-coastal-dgma", craft="precision")

# ---------------------------------------------------------------- Union & State Executive (statement, medium)
S("Union & State Executive", "medium", "With reference to the law officers of the Union and the States, consider the following statements:",
  "संघ और राज्यों के विधि अधिकारियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Advocate General of a State is entitled to vote in the State Legislative Assembly on the matters on which he speaks.",
   "The privileges and immunities of a House of Parliament do not extend to the Attorney General, since he is not its member.",
   "The Advocate General can speak in the State Legislature only if he is a member of it."],
  ["राज्य का महाधिवक्ता राज्य विधानसभा में उन विषयों पर मत देने का हक़दार है जिन पर वह बोलता है।",
   "संसद के किसी सदन के विशेषाधिकार और उन्मुक्तियाँ महान्यायवादी पर लागू नहीं होतीं, क्योंकि वह उसका सदस्य नहीं है।",
   "महाधिवक्ता राज्य विधानमंडल में तभी बोल सकता है जब वह उसका सदस्य हो।"],
  C3, 3,
  "None of the statements is correct. Article 177 gives every minister and the Advocate General of a State the right to speak in, and otherwise take part in the proceedings of, the Legislative Assembly and the Legislative Council, and in any committee of which they are named members, but not the right to vote; membership is not required -- the Advocate General is normally not a legislator at all. Article 88 gives the Attorney General the same position in either House of Parliament. "
  "Statement 2 is wrong: Article 105(4) extends the privileges and immunities of members to every person who, under the Constitution, has the right to speak in a House, so the Attorney General is protected for what he says there; Article 194(4) does the same for the Advocate General in a State legislature. The design lets the government's chief legal adviser explain the law to the House while keeping him outside the voting body.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 177 प्रत्येक मंत्री और राज्य के महाधिवक्ता को विधानसभा और विधान परिषद में, और जिस समिति में वे सदस्य नामित हों उसमें, बोलने और कार्यवाही में अन्यथा भाग लेने का अधिकार देता है, पर मत देने का नहीं; सदस्यता आवश्यक नहीं -- महाधिवक्ता सामान्यतः विधायक होता ही नहीं। अनुच्छेद 88 महान्यायवादी को संसद के किसी भी सदन में यही स्थिति देता है। "
  "कथन 2 ग़लत है: अनुच्छेद 105(4) सदस्यों के विशेषाधिकार और उन्मुक्तियाँ हर उस व्यक्ति तक बढ़ाता है जिसे संविधान के अंतर्गत किसी सदन में बोलने का अधिकार है, इसलिए वहाँ कही बातों के लिए महान्यायवादी संरक्षित है; अनुच्छेद 194(4) राज्य विधानमंडल में महाधिवक्ता के लिए यही करता है। यह रचना सरकार के प्रमुख विधि सलाहकार को सदन को विधि समझाने देती है और उसे मतदाता निकाय से बाहर भी रखती है।",
  COI + ", Articles 88, 105(4), 177 and 194(4).",
  "l4-s01-pol-art177-advocate-general-105-4-privileges", craft="linkage")

write("gs_l4_s01_a.sql")
