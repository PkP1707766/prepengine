# -*- coding: utf-8 -*-
"""Level 2 · Test 1 (Polity 1: Constitutional Framework & Rights) -- Constitutional Framework,
44 new bilingual rows against the live gap report: medium statement 16, hard statement 9,
medium MCQ 4, medium Statement-I/II 4, hard MCQ 2, hard Statement-I/II(/III) 2, medium pairs 2,
easy statement 1, hard pairs 2, easy MCQ 1, easy Statement-I/II 1. The 18 existing Framework
rows are not repeated, and no new row states the date the Constitution was adopted, who chaired
the Drafting Committee, that the Assembly came from the Cabinet Mission plan, when the Fundamental
Duties were added, what the 61st/86th/91st Amendments did, or the Article 3 / Article 368 points
(President's recommendation and views of the State, Articles 2-3 not being amendments, the
President bound to assent) -- facts that existing rows test. The British-era rows use only facts
that History Test 5's constitutional-acts rows do not already test."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
CF = "Constitutional Framework"
COI = "Constitution of India"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
GA = "Granville Austin, The Indian Constitution: Cornerstone of a Nation"
CAD = "Constituent Assembly Debates (Lok Sabha Secretariat)"

# ---------------------------------------------------------------- medium statements (16)
S(CF, "medium", "Consider the following statements about the Constituent Assembly:",
  "संविधान सभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its members from the provinces were elected indirectly by the members of the provincial legislative assemblies.",
   "The representatives of the princely states were to be elected by the people of those states.",
   "The Muslim League took part in the Assembly from its first session."],
  ["प्रांतों से इसके सदस्य प्रांतीय विधानसभाओं के सदस्यों द्वारा अप्रत्यक्ष रूप से चुने गए थे।",
   "रियासतों के प्रतिनिधियों को उन रियासतों की जनता द्वारा चुना जाना था।",
   "मुस्लिम लीग ने पहले ही सत्र से सभा में भाग लिया।"],
  C3, 0,
  "Only statement 1 is correct. Seats were allotted to the provinces roughly in proportion to population and divided among Muslims, Sikhs and 'general' members, who were elected by the corresponding members of the provincial assemblies by proportional representation with the single transferable vote. "
  "Statement 2 is wrong: the princely states' representatives were to be nominated by their rulers, so the Assembly was only partly elected, and even that indirectly. "
  "Statement 3 is wrong: the Muslim League boycotted the Assembly from its first meeting in December 1946, and after Partition its members from the areas that became Pakistan left for Pakistan's own Constituent Assembly.",
  "केवल कथन 1 सही है। प्रांतों को लगभग जनसंख्या के अनुपात में सीटें मिलीं, जो मुसलमानों, सिखों और 'सामान्य' सदस्यों में बँटी थीं, और इन्हें प्रांतीय विधानसभाओं के संबंधित सदस्यों ने एकल संक्रमणीय मत द्वारा आनुपातिक प्रतिनिधित्व से चुना। "
  "कथन 2 गलत है: रियासतों के प्रतिनिधि उनके शासकों द्वारा मनोनीत किए जाने थे, इसलिए सभा केवल आंशिक रूप से, और वह भी अप्रत्यक्ष रूप से, निर्वाचित थी। "
  "कथन 3 गलत है: मुस्लिम लीग ने दिसंबर 1946 की पहली बैठक से ही सभा का बहिष्कार किया, और विभाजन के बाद पाकिस्तान बने क्षेत्रों के उसके सदस्य पाकिस्तान की अपनी संविधान सभा में चले गए।",
  f"{NC} -- Constitution: Why and How?; {GA}.",
  "polity-ca-composition-election")

S(CF, "medium", "Consider the following statements about the Objectives Resolution:",
  "उद्देश्य प्रस्ताव (Objectives Resolution) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was moved in the Constituent Assembly by Jawaharlal Nehru in December 1946.",
   "It was adopted by the Assembly in January 1947.",
   "Its ideas were later reflected in the Preamble to the Constitution."],
  ["इसे दिसंबर 1946 में जवाहरलाल नेहरू ने संविधान सभा में प्रस्तुत किया।",
   "सभा ने इसे जनवरी 1947 में स्वीकार किया।",
   "इसके विचार बाद में संविधान की प्रस्तावना में झलके।"],
  C3, 2,
  "All three statements are correct. Moved on 13 December 1946 and adopted on 22 January 1947, the Resolution declared the resolve to make India an 'Independent Sovereign Republic' in which all power derived from the people, with justice, equality and freedom guaranteed to all and adequate safeguards for minorities and backward classes. The Preamble condenses these aims, which is why courts read the Resolution to understand the Preamble.",
  "तीनों कथन सही हैं। 13 दिसंबर 1946 को प्रस्तुत और 22 जनवरी 1947 को स्वीकृत इस प्रस्ताव ने भारत को एक 'स्वतंत्र संप्रभु गणराज्य' बनाने का संकल्प घोषित किया, जिसमें सारी शक्ति जनता से आए, सभी को न्याय, समानता और स्वतंत्रता की गारंटी हो और अल्पसंख्यकों तथा पिछड़े वर्गों के लिए पर्याप्त सुरक्षा उपाय हों। प्रस्तावना इन्हीं उद्देश्यों को संक्षेप में रखती है, इसीलिए न्यायालय प्रस्तावना को समझने के लिए इस प्रस्ताव को पढ़ते हैं।",
  f"{CAD}, 13 December 1946 and 22 January 1947; {NC}.",
  "polity-objectives-resolution")

S(CF, "medium", "Consider the following statements about the Constituent Assembly:",
  "संविधान सभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["After independence it also functioned as the legislature of the Dominion of India.",
   "It adopted the national flag in January 1950.",
   "It adopted the national anthem in 1947."],
  ["स्वतंत्रता के बाद इसने भारत डोमिनियन के विधानमंडल के रूप में भी काम किया।",
   "इसने जनवरी 1950 में राष्ट्रीय ध्वज अपनाया।",
   "इसने 1947 में राष्ट्रगान अपनाया।"],
  C3, 0,
  "Only statement 1 is correct: from August 1947 the Assembly sat both as the constitution-making body and, separately, as the Dominion legislature, and after 26 January 1950 it continued as the Provisional Parliament until the first elected Parliament met in 1952. "
  "Statement 2 is wrong: the tricolour was adopted on 22 July 1947, before independence. "
  "Statement 3 is wrong: Jana Gana Mana was adopted as the national anthem, and Vande Mataram given equal honour as the national song, on 24 January 1950, at the Assembly's last session.",
  "केवल कथन 1 सही है: अगस्त 1947 से सभा संविधान-निर्माता निकाय के रूप में और अलग से डोमिनियन विधानमंडल के रूप में बैठती रही, और 26 जनवरी 1950 के बाद 1952 में पहली निर्वाचित संसद की बैठक तक अस्थायी संसद के रूप में बनी रही। "
  "कथन 2 गलत है: तिरंगा स्वतंत्रता से पहले, 22 जुलाई 1947 को, अपनाया गया। "
  "कथन 3 गलत है: जन गण मन को राष्ट्रगान के रूप में, और वंदे मातरम् को राष्ट्रगीत के रूप में बराबर सम्मान, 24 जनवरी 1950 को सभा के अंतिम सत्र में दिया गया।",
  f"{CAD}; {NC}.",
  "polity-ca-other-functions-symbols")

S(CF, "medium", "Consider the following statements about the Constitution of India:",
  "भारत के संविधान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It provides for a single citizenship for the whole of India.",
   "It vests the residuary powers of legislation in the State Legislatures.",
   "If a Union law and a State law on a Concurrent List subject conflict, the Union law generally prevails."],
  ["यह पूरे भारत के लिए एकल नागरिकता का प्रावधान करता है।",
   "यह विधि-निर्माण की अवशिष्ट शक्तियाँ राज्य विधानमंडलों को देता है।",
   "यदि समवर्ती सूची के किसी विषय पर संघ का कानून और राज्य का कानून टकराएँ, तो सामान्यतः संघ का कानून प्रभावी होता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Unlike the United States, India has no separate State citizenship. Under Article 254(1) a Union law prevails over a repugnant State law on a Concurrent subject; the exception in Article 254(2) lets a State law reserved for and assented to by the President prevail in that State, which is why the statement says 'generally'. "
  "Statement 2 is wrong: Article 248 and Entry 97 of the Union List give the residuary power to Parliament, following the Canadian model rather than the American one, where the residue lies with the states.",
  "कथन 1 और 3 सही हैं। संयुक्त राज्य अमेरिका के विपरीत भारत में अलग राज्य-नागरिकता नहीं है। अनुच्छेद 254(1) के तहत समवर्ती विषय पर विरोधी राज्य कानून के ऊपर संघ का कानून प्रभावी होता है; अनुच्छेद 254(2) का अपवाद राष्ट्रपति के विचार के लिए आरक्षित और उनकी अनुमति पाए राज्य कानून को उस राज्य में प्रभावी होने देता है, इसीलिए कथन में 'सामान्यतः' कहा गया है। "
  "कथन 2 गलत है: अनुच्छेद 248 और संघ सूची की प्रविष्टि 97 अवशिष्ट शक्ति संसद को देते हैं; यह कनाडा का नमूना है, अमेरिका का नहीं, जहाँ अवशिष्ट शक्ति राज्यों के पास है।",
  f"{COI}, Articles 5-11, 248 and 254; Seventh Schedule, List I, Entry 97; {NC} -- Federalism.",
  "polity-salient-features-citizenship-residuary")

S(CF, "medium", "Consider the following statements about the power of Parliament to amend the Constitution:",
  "संविधान में संशोधन की संसद की शक्ति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Golaknath (1967), the Supreme Court held that Parliament could not amend the Fundamental Rights.",
   "In Kesavananda Bharati (1973), the Supreme Court propounded the doctrine of the 'basic structure'.",
   "In Kesavananda Bharati, the Supreme Court held that the Fundamental Rights cannot be amended."],
  ["गोलकनाथ (1967) में उच्चतम न्यायालय ने माना कि संसद मौलिक अधिकारों में संशोधन नहीं कर सकती।",
   "केशवानंद भारती (1973) में उच्चतम न्यायालय ने 'मूल ढाँचे' (basic structure) का सिद्धांत प्रतिपादित किया।",
   "केशवानंद भारती में उच्चतम न्यायालय ने माना कि मौलिक अधिकारों में संशोधन नहीं किया जा सकता।"],
  C3, 1,
  "Statements 1 and 2 are correct. Golaknath held that an amendment was 'law' under Article 13, so it could not take away Fundamental Rights; Parliament responded with the 24th Amendment. "
  "Statement 3 confuses the two cases: Kesavananda overruled Golaknath on this point and accepted that any part of the Constitution, including Part III, can be amended -- but not so as to destroy its basic structure. That limit, not a bar on amending rights, has governed every amendment since.",
  "कथन 1 और 2 सही हैं। गोलकनाथ ने माना कि संशोधन अनुच्छेद 13 के तहत 'विधि' है, इसलिए वह मौलिक अधिकार नहीं छीन सकता; संसद ने 24वें संशोधन से इसका उत्तर दिया। "
  "कथन 3 दोनों मामलों को आपस में मिला देता है: केशवानंद ने इस बिंदु पर गोलकनाथ को पलटा और स्वीकार किया कि भाग III सहित संविधान के किसी भी भाग में संशोधन हो सकता है, पर इस तरह नहीं कि उसका मूल ढाँचा नष्ट हो। अधिकारों में संशोधन पर रोक नहीं, बल्कि यही सीमा तब से हर संशोधन पर लागू है।",
  "Supreme Court of India -- I.C. Golaknath v. State of Punjab (1967); Kesavananda Bharati v. State of Kerala (1973); " + NC + " -- Constitution as a Living Document.",
  "polity-golaknath-kesavananda")

S(CF, "medium", "Consider the following statements about the reorganisation of States:",
  "राज्यों के पुनर्गठन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Dar Commission (1948) advised against reorganising the provinces mainly on the basis of language.",
   "The JVP Committee was made up of Jawaharlal Nehru, Vallabhbhai Patel and Pattabhi Sitaramayya.",
   "Andhra State was formed before the States Reorganisation Commission was appointed."],
  ["दर आयोग (1948) ने मुख्य रूप से भाषा के आधार पर प्रांतों के पुनर्गठन के विरुद्ध सलाह दी।",
   "JVP समिति में जवाहरलाल नेहरू, वल्लभभाई पटेल और पट्टाभि सीतारमैया थे।",
   "आंध्र राज्य राज्य पुनर्गठन आयोग की नियुक्ति से पहले बन चुका था।"],
  C3, 2,
  "All three statements are correct. The Dar Commission preferred administrative convenience to language, and the JVP Committee, set up by the Congress, also cautioned against linguistic states for the time being. "
  "Popular pressure overtook both: Andhra State was carved out of Madras in October 1953 after Potti Sriramulu died following a long fast, and only then, in December 1953, was the States Reorganisation Commission under Fazl Ali appointed. Its report shaped the States Reorganisation Act, 1956. Students who assume Andhra was a product of the Commission fall for statement 3.",
  "तीनों कथन सही हैं। दर आयोग ने भाषा के बजाय प्रशासनिक सुविधा को प्राथमिकता दी, और कांग्रेस द्वारा बनाई गई JVP समिति ने भी फ़िलहाल भाषाई राज्यों के विरुद्ध सावधान किया। "
  "जन-दबाव दोनों पर भारी पड़ा: लंबे अनशन के बाद पोट्टि श्रीरामुलु की मृत्यु होने पर अक्टूबर 1953 में मद्रास से आंध्र राज्य अलग किया गया, और उसके बाद ही, दिसंबर 1953 में, फ़ज़ल अली के नेतृत्व में राज्य पुनर्गठन आयोग नियुक्त हुआ। इसकी रिपोर्ट ने राज्य पुनर्गठन अधिनियम, 1956 को आकार दिया। जो विद्यार्थी आंध्र को आयोग की देन मानते हैं, वे कथन 3 पर चूकते हैं।",
  f"{NC} -- Federalism; NCERT Class XII, Politics in India since Independence -- Challenges of Nation Building.",
  "polity-states-reorganisation-dar-jvp")

S(CF, "medium", "Consider the following statements about the Union and its territory:",
  "संघ और उसके राज्यक्षेत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 1 describes India as a 'Union of States'.",
   "The 'Union of India' is a wider expression than the 'territory of India'.",
   "Sikkim became a full-fledged State of the Indian Union through the 35th Amendment Act."],
  ["अनुच्छेद 1 भारत को 'राज्यों का संघ' बताता है।",
   "'भारत संघ' (Union of India) 'भारत के राज्यक्षेत्र' (territory of India) से व्यापक अभिव्यक्ति है।",
   "सिक्किम 35वें संशोधन अधिनियम के ज़रिए भारतीय संघ का पूर्ण राज्य बना।"],
  C3, 0,
  "Only statement 1 is correct. Ambedkar explained that 'Union' was chosen because the federation was not the result of an agreement among States and no State has the right to secede. "
  "Statement 2 reverses the relation: the 'Union of India' covers only the States, while the 'territory of India' under Article 1(3) also includes the Union Territories and any territory India may acquire, so it is the wider expression. "
  "Statement 3 is wrong: the 35th Amendment (1974) made Sikkim an 'associate State'; the 36th Amendment (1975) made it a full State.",
  "केवल कथन 1 सही है। आंबेडकर ने समझाया कि 'संघ' (Union) इसलिए चुना गया कि यह संघ राज्यों के किसी समझौते का परिणाम नहीं है और किसी राज्य को अलग होने का अधिकार नहीं है। "
  "कथन 2 संबंध को उलट देता है: 'भारत संघ' में केवल राज्य आते हैं, जबकि अनुच्छेद 1(3) के तहत 'भारत के राज्यक्षेत्र' में केंद्रशासित प्रदेश और भारत द्वारा अर्जित किया जाने वाला कोई भी क्षेत्र भी शामिल है, इसलिए वही व्यापक अभिव्यक्ति है। "
  "कथन 3 गलत है: 35वें संशोधन (1974) ने सिक्किम को 'सहयोगी राज्य' बनाया; 36वें संशोधन (1975) ने उसे पूर्ण राज्य बनाया।",
  f"{COI}, Article 1; Constitution (Thirty-fifth and Thirty-sixth Amendment) Acts; {CAD}, 4 November 1948.",
  "polity-union-territory-art1-sikkim")

S(CF, "medium", "Consider the following statements about the procedure for amending the Constitution under Article 368:",
  "अनुच्छेद 368 के तहत संविधान संशोधन की प्रक्रिया के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A Bill to amend the Constitution can be introduced only with the prior recommendation of the President.",
   "A Constitution Amendment Bill can also be introduced in a State Legislature.",
   "A Constitution Amendment Bill can be introduced only by a minister and not by a private member."],
  ["संविधान संशोधन विधेयक केवल राष्ट्रपति की पूर्व सिफ़ारिश से ही प्रस्तुत किया जा सकता है।",
   "संविधान संशोधन विधेयक किसी राज्य विधानमंडल में भी प्रस्तुत किया जा सकता है।",
   "संविधान संशोधन विधेयक केवल मंत्री द्वारा प्रस्तुत किया जा सकता है, निजी सदस्य द्वारा नहीं।"],
  C3, 3,
  "None of the statements is correct. An amendment Bill can be introduced in either House of Parliament, by a minister or by a private member, and needs no prior recommendation of the President -- unlike a Bill under Article 3 to form or alter States, which does. "
  "The initiative lies only with Parliament; State Legislatures come in only to ratify the amendments listed in the proviso to Article 368(2).",
  "कोई भी कथन सही नहीं है। संशोधन विधेयक संसद के किसी भी सदन में, मंत्री या निजी सदस्य द्वारा, प्रस्तुत किया जा सकता है, और इसके लिए राष्ट्रपति की पूर्व सिफ़ारिश नहीं चाहिए; जबकि राज्य बनाने या बदलने वाले अनुच्छेद 3 के विधेयक के लिए यह चाहिए। "
  "पहल केवल संसद के पास है; राज्य विधानमंडल केवल अनुच्छेद 368(2) के परंतुक में गिनाए गए संशोधनों का अनुसमर्थन करने के लिए आते हैं।",
  f"{COI}, Articles 3 and 368; {NC} -- Constitution as a Living Document.",
  "polity-amendment-procedure-initiation")

S(CF, "medium", "Consider the following statements about recent Constitution Amendment Acts:",
  "हाल के संविधान संशोधन अधिनियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 104th Amendment Act ended the nomination of Anglo-Indian members to the Lok Sabha and the State Legislative Assemblies.",
   "The 106th Amendment Act reserves one-third of the seats for women in the Lok Sabha, the State Legislative Assemblies and the Rajya Sabha.",
   "The reservation for women under the 106th Amendment came into effect in the 2024 Lok Sabha elections."],
  ["104वें संशोधन अधिनियम ने लोकसभा और राज्य विधानसभाओं में आंग्ल-भारतीय सदस्यों का मनोनयन समाप्त किया।",
   "106वाँ संशोधन अधिनियम लोकसभा, राज्य विधानसभाओं और राज्यसभा में एक-तिहाई सीटें महिलाओं के लिए आरक्षित करता है।",
   "106वें संशोधन के तहत महिलाओं का आरक्षण 2024 के लोकसभा चुनावों में लागू हो गया।"],
  C3, 0,
  "Only statement 1 is correct: the 104th Amendment (2019) extended the reservation of seats for Scheduled Castes and Scheduled Tribes until 2030 but let the Anglo-Indian nomination lapse. "
  "Statement 2 is wrong: the 106th Amendment (2023), the 'Nari Shakti Vandan Adhiniyam', reserves seats for women in the Lok Sabha, the State Legislative Assemblies and the Legislative Assembly of Delhi -- not in the Rajya Sabha or the Legislative Councils, whose members are elected indirectly. "
  "Statement 3 is wrong: the reservation takes effect only after delimitation based on the first census taken after the Act's commencement; it is to last fifteen years, with rotation of seats.",
  "केवल कथन 1 सही है: 104वें संशोधन (2019) ने अनुसूचित जातियों और अनुसूचित जनजातियों के लिए सीटों का आरक्षण 2030 तक बढ़ाया, पर आंग्ल-भारतीय मनोनयन को समाप्त होने दिया। "
  "कथन 2 गलत है: 106वाँ संशोधन (2023), 'नारी शक्ति वंदन अधिनियम', लोकसभा, राज्य विधानसभाओं और दिल्ली की विधानसभा में महिलाओं के लिए सीटें आरक्षित करता है; राज्यसभा या विधान परिषदों में नहीं, जिनके सदस्य अप्रत्यक्ष रूप से चुने जाते हैं। "
  "कथन 3 गलत है: आरक्षण अधिनियम के लागू होने के बाद हुई पहली जनगणना पर आधारित परिसीमन के बाद ही प्रभावी होता है; यह सीटों के चक्रानुक्रम के साथ पंद्रह वर्ष तक चलेगा।",
  "Constitution (One Hundred and Fourth Amendment) Act, 2019; Constitution (One Hundred and Sixth Amendment) Act, 2023, Articles 239AA, 330A, 332A and 334A.",
  "polity-104th-106th-amendments")

S(CF, "medium", "Consider the following statements about Overseas Citizenship of India (OCI) cardholders:",
  "भारत की प्रवासी नागरिकता (OCI) कार्डधारकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They can vote in elections to the Lok Sabha.",
   "They can be appointed judges of the Supreme Court.",
   "They get a multiple-entry, multi-purpose lifelong visa for visiting India."],
  ["वे लोकसभा चुनावों में मत दे सकते हैं।",
   "वे उच्चतम न्यायालय के न्यायाधीश नियुक्त किए जा सकते हैं।",
   "उन्हें भारत आने के लिए बहु-प्रवेश, बहु-उद्देशीय आजीवन वीज़ा मिलता है।"],
  C3, 0,
  "Only statement 3 is correct. Introduced by the Citizenship (Amendment) Act, 2003 under section 7A of the Citizenship Act, OCI gives foreign citizens of Indian origin a lifelong visa and parity with NRIs in many economic and educational matters, but it is not citizenship. "
  "So OCI cardholders cannot vote, cannot be elected to Parliament or a State Legislature, and cannot hold constitutional offices such as President, Vice-President or judge of the Supreme Court or a High Court.",
  "केवल कथन 3 सही है। नागरिकता अधिनियम की धारा 7A के तहत नागरिकता (संशोधन) अधिनियम, 2003 से शुरू हुई OCI भारतीय मूल के विदेशी नागरिकों को आजीवन वीज़ा और कई आर्थिक व शैक्षिक मामलों में अनिवासी भारतीयों के बराबर दर्जा देती है, पर यह नागरिकता नहीं है। "
  "इसलिए OCI कार्डधारक मत नहीं दे सकते, संसद या राज्य विधानमंडल के लिए नहीं चुने जा सकते, और राष्ट्रपति, उपराष्ट्रपति या उच्चतम न्यायालय अथवा उच्च न्यायालय के न्यायाधीश जैसे संवैधानिक पद नहीं धारण कर सकते।",
  "Citizenship Act, 1955, sections 7A-7D; Ministry of Home Affairs -- OCI cardholder rights.",
  "polity-oci-cardholders")

S(CF, "medium", "Consider the following statements about constitutional developments under British rule:",
  "ब्रिटिश शासन के दौरान संवैधानिक विकास के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Charter Act of 1833 deprived the Governors of Bombay and Madras of their legislative powers.",
   "The Charter Act of 1853 separated, for the first time, the legislative and executive functions of the Governor-General's Council.",
   "The Indian Councils Act of 1861 provided for Indians to be elected to the Viceroy's legislative council."],
  ["1833 के चार्टर अधिनियम ने बंबई और मद्रास के गवर्नरों से उनकी विधायी शक्तियाँ छीन लीं।",
   "1853 के चार्टर अधिनियम ने पहली बार गवर्नर-जनरल की परिषद के विधायी और कार्यकारी कार्यों को अलग किया।",
   "1861 के भारतीय परिषद अधिनियम ने वायसराय की विधान परिषद में भारतीयों के निर्वाचन का प्रावधान किया।"],
  C3, 1,
  "Statements 1 and 2 are correct. The 1833 Act centralised law-making in the Governor-General of India in Council, and the 1853 Act added separate legislative members, creating a Central Legislative Council that worked like a small parliament. "
  "Statement 3 is wrong: the 1861 Act allowed the Viceroy to nominate some Indians as non-official members -- Lord Canning nominated the Raja of Benares, the Maharaja of Patiala and Sir Dinkar Rao -- but there was no election. An element of election came only indirectly in 1892, and direct election in 1919.",
  "कथन 1 और 2 सही हैं। 1833 के अधिनियम ने कानून बनाने की शक्ति भारत के गवर्नर-जनरल-इन-काउंसिल में केंद्रित की, और 1853 के अधिनियम ने अलग विधायी सदस्य जोड़कर एक केंद्रीय विधान परिषद बनाई, जो एक छोटी संसद की तरह काम करती थी। "
  "कथन 3 गलत है: 1861 के अधिनियम ने वायसराय को कुछ भारतीयों को गैर-सरकारी सदस्यों के रूप में मनोनीत करने दिया; लॉर्ड कैनिंग ने बनारस के राजा, पटियाला के महाराजा और सर दिनकर राव को मनोनीत किया; पर कोई चुनाव नहीं था। चुनाव का तत्व 1892 में केवल अप्रत्यक्ष रूप में, और प्रत्यक्ष चुनाव 1919 में आया।",
  "Charter Act, 1833 (3 & 4 Will. IV, c. 85); Charter Act, 1853; Indian Councils Acts, 1861 and 1892.",
  "polity-british-acts-1833-1853-1861")

S(CF, "medium", "Consider the following statements about the Parts of the Constitution:",
  "संविधान के भागों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Part IVA contains the Fundamental Duties.",
   "Part IX deals with the Municipalities.",
   "Part VI deals with the Union Executive."],
  ["भाग IVA में मौलिक कर्तव्य हैं।",
   "भाग IX नगरपालिकाओं से संबंधित है।",
   "भाग VI संघ की कार्यपालिका से संबंधित है।"],
  C3, 0,
  "Only statement 1 is correct: Part IVA has a single Article, 51A, listing the duties. "
  "Statement 2 is wrong: Part IX deals with the Panchayats; the Municipalities are in Part IXA, and co-operative societies in Part IXB. "
  "Statement 3 is wrong: Part V deals with the Union (executive, Parliament and judiciary), while Part VI deals with the States. Such Part numbers are a common source of UPSC traps because the lettered Parts (IVA, IXA, IXB, XIVA) were added later.",
  "केवल कथन 1 सही है: भाग IVA में एक ही अनुच्छेद, 51A, है, जो कर्तव्यों को गिनाता है। "
  "कथन 2 गलत है: भाग IX पंचायतों से संबंधित है; नगरपालिकाएँ भाग IXA में और सहकारी समितियाँ भाग IXB में हैं। "
  "कथन 3 गलत है: भाग V संघ (कार्यपालिका, संसद और न्यायपालिका) से संबंधित है, जबकि भाग VI राज्यों से। ऐसे भाग-क्रमांक UPSC के जालों का आम स्रोत हैं, क्योंकि अक्षर वाले भाग (IVA, IXA, IXB, XIVA) बाद में जोड़े गए।",
  f"{COI}, Parts V, VI, IVA, IX, IXA and IXB.",
  "polity-parts-iva-ix-vi")

S(CF, "medium", "Which of the following are unitary features of the Constitution of India?",
  "निम्नलिखित में से कौन-सी भारत के संविधान की एकात्मक विशेषताएँ हैं?",
  ["The All-India Services, common to the Union and the States",
   "The appointment of State Governors by the President",
   "The division of powers between the Union and the States in the Seventh Schedule",
   "A single Election Commission for elections to Parliament and the State Legislatures"],
  ["संघ और राज्यों के लिए साझा अखिल भारतीय सेवाएँ",
   "राष्ट्रपति द्वारा राज्यपालों की नियुक्ति",
   "सातवीं अनुसूची में संघ और राज्यों के बीच शक्तियों का बँटवारा",
   "संसद और राज्य विधानमंडलों के चुनावों के लिए एक ही निर्वाचन आयोग"],
  C4, 2,
  "Three are unitary features. Officers of the IAS, IPS and Indian Forest Service are recruited by the Union but serve the States and can be removed only by the Union; Governors are appointed by the President; and one Election Commission conducts elections at both levels. "
  "Item 3 is the odd one out: a constitutional division of powers between two levels of government is the defining federal feature, not a unitary one. With the emergency powers and the integrated judiciary, the unitary features are why K.C. Wheare called India 'quasi-federal'.",
  "तीन एकात्मक विशेषताएँ हैं। IAS, IPS और भारतीय वन सेवा के अधिकारी संघ द्वारा भर्ती होते हैं पर राज्यों की सेवा करते हैं और केवल संघ उन्हें हटा सकता है; राज्यपालों की नियुक्ति राष्ट्रपति करते हैं; और एक ही निर्वाचन आयोग दोनों स्तरों पर चुनाव कराता है। "
  "मद 3 अलग है: शासन के दो स्तरों के बीच शक्तियों का संवैधानिक बँटवारा संघवाद की निर्णायक विशेषता है, एकात्मक नहीं। आपातकालीन शक्तियों और एकीकृत न्यायपालिका के साथ ये एकात्मक विशेषताएँ ही कारण हैं कि के.सी. व्हेयर ने भारत को 'अर्ध-संघीय' कहा।",
  f"{COI}, Articles 155, 246, 312 and 324; {NC} -- Federalism.",
  "polity-unitary-features",
  closing="How many of the above are unitary features?",
  closing_hi="उपर्युक्त में से कितनी एकात्मक विशेषताएँ हैं?")

S(CF, "medium", "The Preamble to the Constitution of India speaks of:",
  "भारत के संविधान की प्रस्तावना किसकी बात करती है?",
  ["Justice -- social, economic and religious",
   "Liberty of thought, expression, belief, faith and worship",
   "Equality of status and of opportunity"],
  ["न्याय: सामाजिक, आर्थिक और धार्मिक",
   "विचार, अभिव्यक्ति, विश्वास, धर्म और उपासना की स्वतंत्रता",
   "प्रतिष्ठा और अवसर की समता"],
  C3, 1,
  "Two of them are correct. The Preamble secures liberty of thought, expression, belief, faith and worship, and equality of status and of opportunity, and promotes fraternity assuring the dignity of the individual and the unity and integrity of the Nation. "
  "Statement 1 changes one word: the Preamble speaks of justice -- social, economic and political. Religious freedom appears under 'liberty', not 'justice', which is exactly the swap UPSC-style questions test.",
  "इनमें से दो सही हैं। प्रस्तावना विचार, अभिव्यक्ति, विश्वास, धर्म और उपासना की स्वतंत्रता, तथा प्रतिष्ठा और अवसर की समता सुनिश्चित करती है, और व्यक्ति की गरिमा तथा राष्ट्र की एकता और अखंडता सुनिश्चित करने वाली बंधुता बढ़ाती है। "
  "कथन 1 एक शब्द बदल देता है: प्रस्तावना न्याय को सामाजिक, आर्थिक और राजनीतिक कहती है। धार्मिक स्वतंत्रता 'स्वतंत्रता' के तहत आती है, 'न्याय' के तहत नहीं; UPSC-शैली के प्रश्न ठीक इसी अदला-बदली को परखते हैं।",
  f"{COI}, Preamble; {NC} -- Philosophy of the Constitution.",
  "polity-preamble-text-justice-liberty",
  closing="How many of the above are correct?",
  closing_hi="उपर्युक्त में से कितने सही हैं?")

S(CF, "medium", "Which of the following are federal features of the Constitution of India?",
  "निम्नलिखित में से कौन-सी भारत के संविधान की संघीय विशेषताएँ हैं?",
  ["A written Constitution",
   "A bicameral Union legislature with a House representing the States",
   "The original jurisdiction of the Supreme Court in disputes between the Union and the States"],
  ["लिखित संविधान",
   "राज्यों का प्रतिनिधित्व करने वाले एक सदन सहित द्विसदनीय संघीय विधानमंडल",
   "संघ और राज्यों के बीच विवादों में उच्चतम न्यायालय का मूल क्षेत्राधिकार"],
  C3, 2,
  "All three are federal features. A federation needs a written and supreme Constitution dividing powers, a second chamber through which the units are represented (the Rajya Sabha), and an umpire to settle disputes between the levels of government -- the Supreme Court under Article 131. With the division of powers in the Seventh Schedule and the need for State ratification of some amendments, these make India a federation, though one with a strong Centre.",
  "तीनों संघीय विशेषताएँ हैं। संघ के लिए शक्तियों को बाँटने वाला लिखित और सर्वोच्च संविधान, एक दूसरा सदन जिससे इकाइयों का प्रतिनिधित्व हो (राज्यसभा), और शासन के स्तरों के बीच विवाद सुलझाने वाला निर्णायक, यानी अनुच्छेद 131 के तहत उच्चतम न्यायालय, ज़रूरी है। सातवीं अनुसूची में शक्तियों के बँटवारे और कुछ संशोधनों के लिए राज्यों के अनुसमर्थन की ज़रूरत के साथ ये भारत को एक संघ बनाते हैं, हालाँकि सशक्त केंद्र वाला।",
  f"{COI}, Articles 79-80, 131, 246; {NC} -- Federalism.",
  "polity-federal-features",
  closing="How many of the above are federal features?",
  closing_hi="उपर्युक्त में से कितनी संघीय विशेषताएँ हैं?")

S(CF, "medium", "Consider the following statements about Articles 6 to 8 of the Constitution:",
  "संविधान के अनुच्छेद 6 से 8 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 6 dealt with persons who had migrated to India from Pakistan.",
   "Article 7 dealt with persons who had migrated from India to Pakistan after 1 March 1947.",
   "Article 8 allowed persons of Indian origin living abroad to become citizens by applying to the Governor-General of India."],
  ["अनुच्छेद 6 पाकिस्तान से भारत आए व्यक्तियों से संबंधित था।",
   "अनुच्छेद 7 उन व्यक्तियों से संबंधित था जो 1 मार्च 1947 के बाद भारत से पाकिस्तान चले गए।",
   "अनुच्छेद 8 ने विदेश में रहने वाले भारतीय मूल के व्यक्तियों को भारत के गवर्नर-जनरल को आवेदन देकर नागरिक बनने दिया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Articles 5 to 8 settled who was a citizen on 26 January 1950: Article 5 covered those domiciled in India, Article 6 migrants from Pakistan (with a cut-off of 19 July 1948 after which registration was needed), and Article 7 generally excluded those who had migrated to Pakistan unless they returned under a permit for resettlement. "
  "Statement 3 is wrong: persons of Indian origin residing outside India registered with the diplomatic or consular representative of India in the country where they lived, not with the Governor-General.",
  "कथन 1 और 2 सही हैं। अनुच्छेद 5 से 8 ने तय किया कि 26 जनवरी 1950 को कौन नागरिक था: अनुच्छेद 5 भारत में अधिवासियों को, अनुच्छेद 6 पाकिस्तान से आए प्रवासियों को (19 जुलाई 1948 की अंतिम तिथि के साथ, जिसके बाद पंजीकरण ज़रूरी था), और अनुच्छेद 7 सामान्यतः पाकिस्तान चले गए लोगों को बाहर रखता था, जब तक वे पुनर्वास-परमिट पर न लौटें। "
  "कथन 3 गलत है: भारत के बाहर रहने वाले भारतीय मूल के व्यक्ति उस देश में भारत के राजनयिक या कांसुलर प्रतिनिधि के पास पंजीकरण कराते थे जहाँ वे रहते थे, गवर्नर-जनरल के पास नहीं।",
  f"{COI}, Articles 5-8.",
  "polity-citizenship-articles-6-8")

# ---------------------------------------------------------------- hard statements (9)
S(CF, "hard", "Consider the following statements about later cases on the basic structure:",
  "मूल ढाँचे पर बाद के मामलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Indira Gandhi v. Raj Narain (1975), the Supreme Court upheld the clause of the 39th Amendment that placed the Prime Minister's election beyond judicial scrutiny.",
   "In Waman Rao (1981), the Supreme Court held that laws placed in the Ninth Schedule before 24 April 1973 could be challenged for violating the basic structure.",
   "In I.R. Coelho (2007), the Supreme Court held that a law placed in the Ninth Schedule after 24 April 1973 cannot be challenged under Articles 14, 19 and 21."],
  ["इंदिरा गांधी बनाम राज नारायण (1975) में उच्चतम न्यायालय ने 39वें संशोधन के उस खंड को सही ठहराया जिसने प्रधानमंत्री के चुनाव को न्यायिक जाँच से बाहर रखा।",
   "वामन राव (1981) में उच्चतम न्यायालय ने माना कि 24 अप्रैल 1973 से पहले नौवीं अनुसूची में रखे गए कानूनों को मूल ढाँचे के उल्लंघन के आधार पर चुनौती दी जा सकती है।",
   "आई.आर. कोएल्हो (2007) में उच्चतम न्यायालय ने माना कि 24 अप्रैल 1973 के बाद नौवीं अनुसूची में रखे गए कानून को अनुच्छेद 14, 19 और 21 के तहत चुनौती नहीं दी जा सकती।"],
  C3, 3,
  "None of the statements is correct -- each reverses what the Court held. "
  "In Raj Narain, the Court struck down clause (4) of Article 329A, inserted by the 39th Amendment, because free and fair elections and judicial review of election disputes are basic features. "
  "Waman Rao drew the line at 24 April 1973, the date of Kesavananda: laws placed in the Ninth Schedule before that date were protected, and only later ones could be tested against the basic structure. "
  "In Coelho, a nine-judge bench held that such later laws can be tested against the basic structure, including the rights in Articles 14, 19 and 21, so the Schedule is no blanket shield.",
  "कोई भी कथन सही नहीं है; हर कथन न्यायालय के निर्णय को उलट देता है। "
  "राज नारायण में न्यायालय ने 39वें संशोधन द्वारा जोड़े गए अनुच्छेद 329A के खंड (4) को रद्द किया, क्योंकि स्वतंत्र और निष्पक्ष चुनाव तथा चुनाव-विवादों की न्यायिक समीक्षा मूल विशेषताएँ हैं। "
  "वामन राव ने केशवानंद की तिथि, 24 अप्रैल 1973, पर रेखा खींची: उस तिथि से पहले नौवीं अनुसूची में रखे गए कानून सुरक्षित रहे, और केवल बाद वालों को मूल ढाँचे की कसौटी पर परखा जा सकता था। "
  "कोएल्हो में नौ न्यायाधीशों की पीठ ने माना कि ऐसे बाद वाले कानूनों को अनुच्छेद 14, 19 और 21 के अधिकारों सहित मूल ढाँचे की कसौटी पर परखा जा सकता है, इसलिए अनुसूची कोई संपूर्ण ढाल नहीं है।",
  "Supreme Court of India -- Indira Nehru Gandhi v. Raj Narain (1975); Waman Rao v. Union of India (1981); I.R. Coelho v. State of Tamil Nadu (2007).",
  "polity-basic-structure-later-cases")

S(CF, "hard", "Consider the following statements about the Constitution (Forty-fourth Amendment) Act, 1978:",
  "संविधान (44वाँ संशोधन) अधिनियम, 1978 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It removed the right to property from the list of Fundamental Rights and made it a legal right under Article 300A.",
   "It replaced 'internal disturbance' with 'armed rebellion' as a ground for proclaiming a national emergency.",
   "It removed the bar, inserted by the 38th Amendment, on judicial review of the President's satisfaction in proclaiming an emergency.",
   "It extended the term of the Lok Sabha and the State Legislative Assemblies from five to six years."],
  ["इसने संपत्ति के अधिकार को मौलिक अधिकारों की सूची से हटाकर अनुच्छेद 300A के तहत विधिक अधिकार बनाया।",
   "इसने राष्ट्रीय आपात की घोषणा के आधार के रूप में 'आंतरिक अशांति' की जगह 'सशस्त्र विद्रोह' रखा।",
   "इसने आपात की घोषणा में राष्ट्रपति की संतुष्टि की न्यायिक समीक्षा पर 38वें संशोधन द्वारा लगाई गई रोक हटा दी।",
   "इसने लोकसभा और राज्य विधानसभाओं का कार्यकाल पाँच से बढ़ाकर छह वर्ष किया।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Passed by the Janata government, the 44th Amendment undid much of the 42nd and tightened emergency powers: 'armed rebellion' replaced the vaguer 'internal disturbance', a proclamation now needs the Cabinet's written advice and approval by a special majority within a month, and the President's satisfaction was made reviewable again. "
  "Statement 4 reverses it: the 42nd Amendment had extended the term to six years, and the 44th restored it to five.",
  "कथन 1, 2 और 3 सही हैं। जनता सरकार द्वारा पारित 44वें संशोधन ने 42वें के बहुत-से प्रावधानों को पलटा और आपातकालीन शक्तियों को कसा: अस्पष्ट 'आंतरिक अशांति' की जगह 'सशस्त्र विद्रोह' आया, घोषणा के लिए अब मंत्रिमंडल की लिखित सलाह और एक महीने के भीतर विशेष बहुमत से अनुमोदन ज़रूरी है, और राष्ट्रपति की संतुष्टि फिर से समीक्षा-योग्य बनाई गई। "
  "कथन 4 उलटा है: 42वें संशोधन ने कार्यकाल छह वर्ष किया था, और 44वें ने उसे फिर पाँच वर्ष किया।",
  "Constitution (Forty-second Amendment) Act, 1976; Constitution (Forty-fourth Amendment) Act, 1978; " + COI + ", Articles 83, 172, 300A and 352.",
  "polity-44th-amendment")

S(CF, "hard", "Consider the following statements about the Constituent Assembly:",
  "संविधान सभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was to have 389 members, 296 from British India and 93 from the princely states.",
   "After Partition, its membership fell to 299.",
   "It took nearly three years to complete the Constitution."],
  ["इसमें 389 सदस्य होने थे, 296 ब्रिटिश भारत से और 93 रियासतों से।",
   "विभाजन के बाद इसकी सदस्य-संख्या घटकर 299 रह गई।",
   "इसे संविधान पूरा करने में लगभग तीन वर्ष लगे।"],
  C3, 2,
  "All three statements are correct. The 296 British Indian seats included 4 for the Chief Commissioners' provinces. After the Muslim-majority areas left, 299 members remained, of whom 284 signed the Constitution. The Assembly took 2 years, 11 months and 18 days, and the draft was discussed clause by clause for 114 days.",
  "तीनों कथन सही हैं। ब्रिटिश भारत की 296 सीटों में चीफ़ कमिश्नरों के प्रांतों की 4 सीटें शामिल थीं। मुस्लिम-बहुल क्षेत्रों के अलग होने के बाद 299 सदस्य रहे, जिनमें से 284 ने संविधान पर हस्ताक्षर किए। सभा को 2 वर्ष, 11 महीने और 18 दिन लगे, और मसौदे पर 114 दिनों तक खंड-दर-खंड चर्चा हुई।",
  f"{CAD}; {NC} -- Constitution: Why and How?",
  "polity-ca-numbers-duration")

S(CF, "hard", "Which of the following changes can be made by Parliament by a simple majority, without following the procedure of Article 368?",
  "निम्नलिखित में से कौन-से परिवर्तन संसद अनुच्छेद 368 की प्रक्रिया अपनाए बिना साधारण बहुमत से कर सकती है?",
  ["Changes in the quorum of the Houses of Parliament",
   "Changes in the Fifth and Sixth Schedules",
   "Changes in the representation of States in Parliament",
   "Changes in the manner of election of the President"],
  ["संसद के सदनों की गणपूर्ति (कोरम) में परिवर्तन",
   "पाँचवीं और छठी अनुसूची में परिवर्तन",
   "संसद में राज्यों के प्रतिनिधित्व में परिवर्तन",
   "राष्ट्रपति के निर्वाचन की रीति में परिवर्तन"],
  C4, 1,
  "The first two can be made by a simple majority. The quorum is fixed by Article 100 only 'until Parliament by law otherwise provides', and amendments of the Fifth and Sixth Schedules under their own provisions are expressly declared not to be amendments under Article 368. "
  "The last two cannot: the representation of States in Parliament and the election of the President (Articles 54 and 55) are among the matters in the proviso to Article 368(2), which need a special majority and ratification by at least half of the State Legislatures, because they touch the federal balance.",
  "पहले दो परिवर्तन साधारण बहुमत से हो सकते हैं। अनुच्छेद 100 गणपूर्ति को केवल 'जब तक संसद विधि द्वारा अन्यथा उपबंध न करे' तय करता है, और पाँचवीं तथा छठी अनुसूची के अपने प्रावधानों के तहत उनके संशोधनों को स्पष्ट रूप से अनुच्छेद 368 के तहत संशोधन नहीं माना गया है। "
  "अंतिम दो नहीं हो सकते: संसद में राज्यों का प्रतिनिधित्व और राष्ट्रपति का निर्वाचन (अनुच्छेद 54 और 55) अनुच्छेद 368(2) के परंतुक के उन विषयों में हैं जिनके लिए विशेष बहुमत और कम से कम आधे राज्य विधानमंडलों का अनुसमर्थन चाहिए, क्योंकि वे संघीय संतुलन को छूते हैं।",
  f"{COI}, Articles 54, 55, 100(4), 368(2); Fifth Schedule para 7; Sixth Schedule para 21.",
  "polity-simple-majority-amendments",
  closing="How many of the above can be made by a simple majority?",
  closing_hi="उपर्युक्त में से कितने साधारण बहुमत से किए जा सकते हैं?")

S(CF, "hard", "Consider the following statements about the Schedules of the Constitution:",
  "संविधान की अनुसूचियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The First Schedule lists the States and the Union Territories.",
   "The Second Schedule contains provisions on the emoluments of the President, the Governors, judges and the Chief Election Commissioner.",
   "The oath of office of the President is prescribed in the Third Schedule."],
  ["पहली अनुसूची राज्यों और केंद्रशासित प्रदेशों को गिनाती है।",
   "दूसरी अनुसूची में राष्ट्रपति, राज्यपालों, न्यायाधीशों और मुख्य निर्वाचन आयुक्त की उपलब्धियों (वेतन आदि) के प्रावधान हैं।",
   "राष्ट्रपति की पद की शपथ तीसरी अनुसूची में निर्धारित है।"],
  C3, 0,
  "Only statement 1 is correct: the First Schedule gives the names and territories of the States and UTs and changes whenever a State is created or reorganised. "
  "Statement 2 is wrong: the Second Schedule covers the President, the Governors, the presiding officers of the legislatures, the judges of the Supreme Court and High Courts, and the Comptroller and Auditor-General; the Chief Election Commissioner's salary and conditions are fixed by a law of Parliament, not by the Schedule. "
  "Statement 3 is also wrong: the Third Schedule prescribes oaths for Union and State ministers, MPs and MLAs, judges and the CAG, but the oaths of the President and the Vice-President are set out in Articles 60 and 69 themselves, and the Governor's in Article 159.",
  "केवल कथन 1 सही है: पहली अनुसूची राज्यों और केंद्रशासित प्रदेशों के नाम और क्षेत्र बताती है और हर बार कोई राज्य बनने या पुनर्गठित होने पर बदलती है। "
  "कथन 2 गलत है: दूसरी अनुसूची में राष्ट्रपति, राज्यपाल, विधानमंडलों के पीठासीन अधिकारी, उच्चतम न्यायालय और उच्च न्यायालयों के न्यायाधीश, और नियंत्रक-महालेखापरीक्षक आते हैं; मुख्य निर्वाचन आयुक्त का वेतन और सेवा-शर्तें संसद के कानून से तय होती हैं, अनुसूची से नहीं। "
  "कथन 3 भी गलत है: तीसरी अनुसूची संघ और राज्य के मंत्रियों, सांसदों और विधायकों, न्यायाधीशों और CAG की शपथें निर्धारित करती है, पर राष्ट्रपति और उपराष्ट्रपति की शपथें स्वयं अनुच्छेद 60 और 69 में, और राज्यपाल की अनुच्छेद 159 में दी गई हैं।",
  f"{COI}, First, Second and Third Schedules; Articles 60, 69 and 159; Chief Election Commissioner and Other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023.",
  "polity-schedules-first-second-third")

S(CF, "hard", "Consider the following statements about Constitution Amendment Acts:",
  "संविधान संशोधन अधिनियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 7th Amendment Act, 1956 gave effect to the reorganisation of States on a linguistic basis.",
   "The 69th Amendment Act provided a legislature and council of ministers for Puducherry.",
   "The 100th Amendment Act gave effect to the land boundary agreement between India and Bangladesh."],
  ["7वें संशोधन अधिनियम, 1956 ने भाषाई आधार पर राज्यों के पुनर्गठन को लागू किया।",
   "69वें संशोधन अधिनियम ने पुदुचेरी के लिए विधानमंडल और मंत्रिपरिषद का प्रावधान किया।",
   "100वें संशोधन अधिनियम ने भारत और बांग्लादेश के बीच भूमि सीमा समझौते को लागू किया।"],
  C3, 1,
  "Statements 1 and 3 are correct. The 7th Amendment abolished the old Part A, B, C and D classification and created 14 States and 6 Union Territories. The 100th Amendment (2015) allowed the exchange of enclaves under the 1974 land boundary agreement and its 2011 protocol, amending the First Schedule. "
  "Statement 2 is wrong: the 69th Amendment (1991) inserted Article 239AA, creating the Legislative Assembly and Council of Ministers of the National Capital Territory of Delhi; Puducherry's legislature rests on Article 239A, inserted by the 14th Amendment (1962).",
  "कथन 1 और 3 सही हैं। 7वें संशोधन ने पुराने भाग A, B, C और D के वर्गीकरण को समाप्त करके 14 राज्य और 6 केंद्रशासित प्रदेश बनाए। 100वें संशोधन (2015) ने पहली अनुसूची में संशोधन करके 1974 के भूमि सीमा समझौते और उसके 2011 के प्रोटोकॉल के तहत बस्तियों (एनक्लेव) की अदला-बदली की अनुमति दी। "
  "कथन 2 गलत है: 69वें संशोधन (1991) ने अनुच्छेद 239AA जोड़कर राष्ट्रीय राजधानी क्षेत्र दिल्ली की विधानसभा और मंत्रिपरिषद बनाई; पुदुचेरी का विधानमंडल 14वें संशोधन (1962) द्वारा जोड़े गए अनुच्छेद 239A पर आधारित है।",
  "Constitution (Seventh, Fourteenth, Sixty-ninth and One Hundredth Amendment) Acts.",
  "polity-amendments-7th-69th-100th")

S(CF, "hard", "Consider the following statements about the sources of the Constitution of India:",
  "भारत के संविधान के स्रोतों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The idea of a Concurrent List was taken from the Constitution of Australia.",
   "'Procedure established by law' in Article 21 was taken from the Constitution of the USA.",
   "Freedom of trade, commerce and intercourse was taken from British constitutional practice.",
   "The joint sitting of the two Houses of Parliament was taken from British constitutional practice."],
  ["समवर्ती सूची का विचार ऑस्ट्रेलिया के संविधान से लिया गया।",
   "अनुच्छेद 21 में 'विधि द्वारा स्थापित प्रक्रिया' अमेरिका के संविधान से ली गई।",
   "व्यापार, वाणिज्य और समागम की स्वतंत्रता ब्रिटिश संवैधानिक व्यवहार से ली गई।",
   "संसद के दोनों सदनों की संयुक्त बैठक ब्रिटिश संवैधानिक व्यवहार से ली गई।"],
  C4, 0,
  "Only statement 1 is correct. The Concurrent List, freedom of trade, commerce and intercourse, and the joint sitting of the two Houses all came from Australia. "
  "Statement 2 is the classic trap: the Assembly deliberately rejected the American 'due process of law' and took 'procedure established by law' from the Constitution of Japan, to keep the courts from striking down laws on their substance. The Supreme Court later read fairness into it in Maneka Gandhi (1978).",
  "केवल कथन 1 सही है। समवर्ती सूची, व्यापार, वाणिज्य और समागम की स्वतंत्रता, और दोनों सदनों की संयुक्त बैठक, तीनों ऑस्ट्रेलिया से आए। "
  "कथन 2 पारंपरिक जाल है: सभा ने अमेरिकी 'विधि की सम्यक प्रक्रिया' (due process of law) को जान-बूझकर अस्वीकार किया और 'विधि द्वारा स्थापित प्रक्रिया' जापान के संविधान से ली, ताकि न्यायालय कानूनों को उनकी विषय-वस्तु के आधार पर रद्द न कर सकें। बाद में उच्चतम न्यायालय ने मेनका गांधी (1978) में इसमें निष्पक्षता का तत्व पढ़ा।",
  f"{COI}, Articles 21, 108 and 301; Seventh Schedule, List III; {GA}.",
  "polity-sources-australia-japan")

S(CF, "hard", "Consider the following statements about the Constituent Assembly:",
  "संविधान सभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Indian Independence Act, 1947 made it a fully sovereign body.",
   "Its Drafting Committee had seven members.",
   "Hyderabad was among the princely states that sent representatives to it."],
  ["भारतीय स्वतंत्रता अधिनियम, 1947 ने इसे पूर्ण संप्रभु निकाय बनाया।",
   "इसकी प्रारूप समिति में सात सदस्य थे।",
   "हैदराबाद उन रियासतों में था जिन्होंने इसमें अपने प्रतिनिधि भेजे।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Independence Act freed the Assembly from the limits of the Cabinet Mission plan and allowed it to repeal or change any law made by the British Parliament for India. The Drafting Committee, set up on 29 August 1947, had seven members; two of the original members were later replaced. "
  "Statement 3 is wrong: the Nizam never sent representatives, so Hyderabad had no part in framing the Constitution even after its integration in 1948.",
  "कथन 1 और 2 सही हैं। स्वतंत्रता अधिनियम ने सभा को कैबिनेट मिशन योजना की सीमाओं से मुक्त किया और उसे भारत के लिए ब्रिटिश संसद द्वारा बनाए गए किसी भी कानून को रद्द करने या बदलने दिया। 29 अगस्त 1947 को बनी प्रारूप समिति में सात सदस्य थे; मूल सदस्यों में से दो बाद में बदले गए। "
  "कथन 3 गलत है: निज़ाम ने कभी प्रतिनिधि नहीं भेजे, इसलिए 1948 में एकीकरण के बाद भी संविधान-निर्माण में हैदराबाद की कोई भागीदारी नहीं रही।",
  f"{CAD}; Indian Independence Act, 1947, section 8; {NC}.",
  "polity-ca-sovereign-drafting-hyderabad")

S(CF, "hard", "Consider the following statements about the Government of India Act, 1935:",
  "भारत सरकार अधिनियम, 1935 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It divided legislative powers between the Centre and the provinces in three lists.",
   "It vested the residuary powers in the Governor-General.",
   "It abolished the Council of India, which had advised the Secretary of State for India.",
   "It made the legislatures of six of the eleven provinces bicameral."],
  ["इसने केंद्र और प्रांतों के बीच विधायी शक्तियों को तीन सूचियों में बाँटा।",
   "इसने अवशिष्ट शक्तियाँ गवर्नर-जनरल में निहित कीं।",
   "इसने भारत सचिव (Secretary of State for India) को सलाह देने वाली इंडिया काउंसिल को समाप्त किया।",
   "इसने ग्यारह में से छह प्रांतों के विधानमंडलों को द्विसदनीय बनाया।"],
  C4, 3,
  "All four statements are correct. The Act created a Federal List, a Provincial List and a Concurrent List -- the model for the Seventh Schedule -- but, unlike the Constitution, it left the residuary powers with the Governor-General, which is the statement most students mark wrong. It replaced the Council of India with a small body of advisers, and gave Bengal, Bombay, Madras, Bihar, Assam and the United Provinces bicameral legislatures.",
  "चारों कथन सही हैं। अधिनियम ने संघीय सूची, प्रांतीय सूची और समवर्ती सूची बनाई, जो सातवीं अनुसूची का नमूना बनी; पर संविधान के विपरीत इसने अवशिष्ट शक्तियाँ गवर्नर-जनरल के पास रखीं, और अधिकांश विद्यार्थी इसी कथन को गलत मान लेते हैं। इसने इंडिया काउंसिल की जगह सलाहकारों का एक छोटा दल रखा, और बंगाल, बंबई, मद्रास, बिहार, असम तथा संयुक्त प्रांत को द्विसदनीय विधानमंडल दिए।",
  "Government of India Act, 1935, sections 100 and 104, and its Seventh Schedule.",
  "polity-goi-act-1935-lists-residuary")

# ---------------------------------------------------------------- MCQs (medium 4, hard 2, easy 1)
M(CF, "medium", "Which one of the following is NOT a feature of the Constitution of India?",
  "निम्नलिखित में से कौन-सी भारत के संविधान की विशेषता नहीं है?",
  ["A presidential form of government", "A parliamentary form of government", "Universal adult franchise", "Fundamental Duties of citizens"],
  ["शासन का अध्यक्षीय रूप", "शासन का संसदीय रूप", "सार्वभौम वयस्क मताधिकार", "नागरिकों के मौलिक कर्तव्य"],
  0,
  "India follows the parliamentary system, modelled on Westminster, in which the President is the constitutional head and the Council of Ministers, responsible to the Lok Sabha, holds real executive power. A presidential system, as in the United States, has a directly elected executive head who is not responsible to the legislature; the Assembly rejected it as offering stability but not enough day-to-day accountability.",
  "भारत वेस्टमिंस्टर के नमूने पर संसदीय व्यवस्था अपनाता है, जिसमें राष्ट्रपति संवैधानिक प्रमुख हैं और लोकसभा के प्रति उत्तरदायी मंत्रिपरिषद के पास वास्तविक कार्यपालिका शक्ति है। संयुक्त राज्य अमेरिका जैसी अध्यक्षीय व्यवस्था में प्रत्यक्ष रूप से निर्वाचित कार्यकारी प्रमुख होता है जो विधायिका के प्रति उत्तरदायी नहीं होता; सभा ने इसे स्थिरता देने वाली पर रोज़मर्रा के पर्याप्त उत्तरदायित्व न देने वाली व्यवस्था मानकर अस्वीकार किया।",
  f"{NC} -- Executive; {CAD}, 4 November 1948.",
  "polity-not-a-feature-presidential")

M(CF, "medium", "Who was the Constitutional Adviser to the Constituent Assembly?",
  "संविधान सभा के संवैधानिक सलाहकार कौन थे?",
  ["B.N. Rau", "K.M. Munshi", "Alladi Krishnaswami Ayyar", "N. Gopalaswami Ayyangar"],
  ["बी.एन. राव", "के.एम. मुंशी", "अल्लादि कृष्णास्वामी अय्यर", "एन. गोपालस्वामी अय्यंगार"],
  0,
  "Sir Benegal Narsing Rau, a civil servant and jurist, prepared the first draft of the Constitution in October 1947 after studying the constitutions of many countries, and it was this draft that the Drafting Committee examined; he later served as a judge of the International Court of Justice. Munshi, Alladi Krishnaswami Ayyar and Gopalaswami Ayyangar were members of the Drafting Committee -- the natural distractors.",
  "सिविल सेवक और विधिवेत्ता सर बेनेगल नरसिंह राव ने कई देशों के संविधानों का अध्ययन करके अक्टूबर 1947 में संविधान का पहला मसौदा तैयार किया, और इसी मसौदे की जाँच प्रारूप समिति ने की; बाद में वे अंतरराष्ट्रीय न्यायालय के न्यायाधीश रहे। मुंशी, अल्लादि कृष्णास्वामी अय्यर और गोपालस्वामी अय्यंगार प्रारूप समिति के सदस्य थे; यही स्वाभाविक गलत विकल्प हैं।",
  f"{GA}; {CAD}.",
  "polity-bn-rau-constitutional-adviser")

M(CF, "medium", "Who presided over the first meeting of the Constituent Assembly as its temporary Chairman?",
  "संविधान सभा की पहली बैठक की अध्यक्षता उसके अस्थायी अध्यक्ष के रूप में किसने की?",
  ["Sachchidananda Sinha", "Rajendra Prasad", "Maulana Abul Kalam Azad", "Jawaharlal Nehru"],
  ["सच्चिदानंद सिन्हा", "राजेंद्र प्रसाद", "मौलाना अबुल कलाम आज़ाद", "जवाहरलाल नेहरू"],
  0,
  "Following the French practice of the oldest member presiding, Sachchidananda Sinha chaired the opening session on 9 December 1946. Rajendra Prasad was elected permanent President on 11 December, and Nehru moved the Objectives Resolution -- which is why both names tempt.",
  "सबसे वरिष्ठ सदस्य के अध्यक्षता करने की फ़्रांसीसी प्रथा के अनुसार सच्चिदानंद सिन्हा ने 9 दिसंबर 1946 को उद्घाटन सत्र की अध्यक्षता की। 11 दिसंबर को राजेंद्र प्रसाद स्थायी अध्यक्ष चुने गए, और नेहरू ने उद्देश्य प्रस्ताव प्रस्तुत किया; इसीलिए दोनों नाम आकर्षक लगते हैं।",
  f"{CAD}, 9 and 11 December 1946.",
  "polity-ca-temporary-chairman-sinha")

M(CF, "medium", "By signing the Instrument of Accession in 1947, a princely state normally ceded to the Dominion of India power over:",
  "1947 में विलय-पत्र (Instrument of Accession) पर हस्ताक्षर करके कोई रियासत सामान्यतः भारत डोमिनियन को किन विषयों पर शक्ति सौंपती थी?",
  ["Defence, external affairs and communications", "Defence, finance, and law and order in their territories", "Defence alone", "All subjects in the Union List"],
  ["रक्षा, विदेश मामले और संचार", "अपने क्षेत्रों में रक्षा, वित्त और क़ानून-व्यवस्था", "केवल रक्षा", "संघ सूची के सभी विषय"],
  0,
  "The Instruments of Accession, drawn up by V.P. Menon and Sardar Patel's States Department, asked the rulers to accede only on defence, external affairs and communications, leaving other matters with them; most states later signed 'merger agreements' and were fully integrated, and the princely states accepted the Constitution in 1949-50. The limited scope of accession is also why Jammu and Kashmir's accession was later governed by Article 370.",
  "वी.पी. मेनन और सरदार पटेल के रियासत विभाग द्वारा तैयार विलय-पत्रों में शासकों से केवल रक्षा, विदेश मामलों और संचार पर विलय करने को कहा गया, दूसरे विषय उनके पास छोड़े गए; अधिकांश रियासतों ने बाद में 'विलय समझौतों' पर हस्ताक्षर किए और पूरी तरह एकीकृत हुईं, और रियासतों ने 1949-50 में संविधान स्वीकार किया। विलय का सीमित दायरा ही कारण है कि जम्मू-कश्मीर का विलय बाद में अनुच्छेद 370 से संचालित हुआ।",
  "NCERT Class XII, Politics in India since Independence -- Challenges of Nation Building; V.P. Menon, The Story of the Integration of the Indian States.",
  "polity-instrument-of-accession")

M(CF, "hard", "The principle of 'prospective overruling' was first applied by the Supreme Court of India in:",
  "'भावी प्रभाव से निरस्तीकरण' (prospective overruling) का सिद्धांत भारत के उच्चतम न्यायालय ने सबसे पहले किस मामले में लागू किया?",
  ["I.C. Golaknath v. State of Punjab", "Kesavananda Bharati v. State of Kerala", "Shankari Prasad v. Union of India", "Minerva Mills v. Union of India"],
  ["आई.सी. गोलकनाथ बनाम पंजाब राज्य", "केशवानंद भारती बनाम केरल राज्य", "शंकरी प्रसाद बनाम भारत संघ", "मिनर्वा मिल्स बनाम भारत संघ"],
  0,
  "In Golaknath (1967), having held that Parliament could not abridge Fundamental Rights, Chief Justice Subba Rao applied the doctrine borrowed from American jurisprudence, so that the ruling operated only for the future: the earlier amendments (the 1st, 4th and 17th) that had already been acted upon were left undisturbed. This avoided unsettling land reform laws already in force.",
  "गोलकनाथ (1967) में यह मानने के बाद कि संसद मौलिक अधिकारों को कम नहीं कर सकती, मुख्य न्यायाधीश सुब्बा राव ने अमेरिकी न्यायशास्त्र से लिया गया यह सिद्धांत लागू किया, ताकि निर्णय केवल भविष्य के लिए लागू हो: पहले के संशोधन (1ला, 4था और 17वाँ), जिन पर अमल हो चुका था, छेड़े नहीं गए। इससे पहले से लागू भूमि-सुधार कानूनों को अस्थिर होने से बचाया गया।",
  "Supreme Court of India -- I.C. Golaknath v. State of Punjab, AIR 1967 SC 1643.",
  "polity-prospective-overruling-golaknath")

M(CF, "hard", "The Constituent Assembly ratified India's decision to remain in the Commonwealth as a republic in:",
  "संविधान सभा ने गणराज्य के रूप में राष्ट्रमंडल में बने रहने के भारत के निर्णय का अनुसमर्थन कब किया?",
  ["May 1949", "August 1947", "January 1950", "November 1946"],
  ["मई 1949", "अगस्त 1947", "जनवरी 1950", "नवंबर 1946"],
  0,
  "After the London Declaration of April 1949, which allowed a republic to remain a member by accepting the British monarch only as the 'symbol of the free association' and Head of the Commonwealth, the Constituent Assembly ratified the decision on 16-17 May 1949. Membership involves no allegiance to the Crown, which is why it does not affect India's sovereignty.",
  "अप्रैल 1949 की लंदन घोषणा के बाद, जिसने किसी गणराज्य को ब्रिटिश सम्राट को केवल 'स्वतंत्र संघ के प्रतीक' और राष्ट्रमंडल के प्रमुख के रूप में स्वीकार करके सदस्य बने रहने दिया, संविधान सभा ने 16-17 मई 1949 को इस निर्णय का अनुसमर्थन किया। सदस्यता में क्राउन के प्रति कोई निष्ठा नहीं है, इसीलिए यह भारत की संप्रभुता को प्रभावित नहीं करती।",
  f"{CAD}, 16-17 May 1949; London Declaration (1949).",
  "polity-commonwealth-ratification-1949")

M(CF, "easy", "According to the Preamble, the source of authority of the Constitution of India is:",
  "प्रस्तावना के अनुसार भारत के संविधान के अधिकार का स्रोत है:",
  ["The people of India", "The British Parliament", "The President of India", "The Constituent Assembly"],
  ["भारत की जनता", "ब्रिटिश संसद", "भारत के राष्ट्रपति", "संविधान सभा"],
  0,
  "The Preamble opens 'We, the people of India ... do hereby adopt, enact and give to ourselves this Constitution', making the people the ultimate source of authority. The Constituent Assembly is the tempting answer because it framed the Constitution, but it did so in the name of the people.",
  "प्रस्तावना 'हम, भारत के लोग ... इस संविधान को अंगीकृत, अधिनियमित और आत्मार्पित करते हैं' से शुरू होती है, जो जनता को अधिकार का अंतिम स्रोत बनाती है। संविधान सभा आकर्षक उत्तर है क्योंकि उसने संविधान बनाया, पर उसने ऐसा जनता के नाम पर किया।",
  f"{COI}, Preamble; {NC} -- Philosophy of the Constitution.",
  "polity-preamble-source-of-authority")

# ---------------------------------------------------------------- Statement-I/II (medium 4, hard 2, easy 1)
A(CF, "medium",
  "K.C. Wheare described the Indian Constitution as 'quasi-federal'.",
  "के.सी. व्हेयर ने भारतीय संविधान को 'अर्ध-संघीय' (quasi-federal) कहा।",
  "The Constitution combines federal features with a strong Centre and several unitary features.",
  "संविधान संघीय विशेषताओं को एक सशक्त केंद्र और कई एकात्मक विशेषताओं के साथ जोड़ता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Wheare saw a federation in form, with a division of powers and a written Constitution, but one in which the Union's powers -- over new States, emergencies, residuary subjects and the All-India Services -- make the States subordinate in important ways; hence 'quasi-federal'.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। व्हेयर ने रूप में शक्तियों के बँटवारे और लिखित संविधान वाला संघ देखा, पर ऐसा जिसमें नए राज्यों, आपात, अवशिष्ट विषयों और अखिल भारतीय सेवाओं पर संघ की शक्तियाँ राज्यों को महत्त्वपूर्ण रूप से अधीन बनाती हैं; इसीलिए 'अर्ध-संघीय'।",
  f"K.C. Wheare, Federal Government; {NC} -- Federalism.",
  "polity-quasi-federal-wheare")

A(CF, "medium",
  "A person born outside India on or after 3 December 2004 does not become a citizen of India by descent unless the birth is registered at an Indian consulate, normally within one year.",
  "3 दिसंबर 2004 को या उसके बाद भारत के बाहर जन्मा व्यक्ति वंश से भारत का नागरिक तब तक नहीं बनता जब तक जन्म का पंजीकरण भारतीय वाणिज्य दूतावास में, सामान्यतः एक वर्ष के भीतर, न हो।",
  "This condition was introduced by the Citizenship (Amendment) Act, 1986.",
  "यह शर्त नागरिकता (संशोधन) अधिनियम, 1986 से लागू हुई।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The registration condition, together with a declaration that the child holds no other country's passport, was added to section 4 of the Citizenship Act by the 2003 amendment. The 1986 amendment dealt with citizenship by birth, requiring for births after 1 July 1987 that at least one parent be an Indian citizen.",
  "कथन-I सही है पर कथन-II गलत है। पंजीकरण की शर्त, इस घोषणा के साथ कि बच्चे के पास किसी दूसरे देश का पासपोर्ट नहीं है, 2003 के संशोधन द्वारा नागरिकता अधिनियम की धारा 4 में जोड़ी गई। 1986 का संशोधन जन्म से नागरिकता से संबंधित था, जिसने 1 जुलाई 1987 के बाद के जन्मों के लिए कम से कम एक माता या पिता का भारतीय नागरिक होना ज़रूरी किया।",
  "Citizenship Act, 1955, sections 3 and 4 (as amended in 1986 and 2003).",
  "polity-citizenship-by-descent-registration")

A(CF, "medium",
  "The Government of India Act, 1919 extended separate electorates to Sikhs, Indian Christians, Anglo-Indians and Europeans.",
  "भारत सरकार अधिनियम, 1919 ने सिखों, भारतीय ईसाइयों, आंग्ल-भारतीयों और यूरोपीयों तक पृथक निर्वाचक-मंडल का विस्तार किया।",
  "The Act provided for a Public Service Commission, and a Central Public Service Commission was set up in 1926.",
  "अधिनियम ने लोक सेवा आयोग का प्रावधान किया, और 1926 में केंद्रीय लोक सेवा आयोग की स्थापना हुई।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The extension of communal representation, begun for Muslims in 1909, is a separate provision of the 1919 Act from the one on recruitment to the services; the Central Public Service Commission of 1926 followed the Lee Commission's recommendations and is the forerunner of the UPSC.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। 1909 में मुसलमानों के लिए शुरू हुए सांप्रदायिक प्रतिनिधित्व का विस्तार 1919 के अधिनियम का सेवाओं में भर्ती वाले प्रावधान से अलग प्रावधान है; 1926 का केंद्रीय लोक सेवा आयोग ली आयोग की सिफ़ारिशों के बाद बना और UPSC का पूर्ववर्ती है।",
  "Government of India Act, 1919, section 96C; Union Public Service Commission -- history of the Commission.",
  "polity-goi-act-1919-electorates-psc")

A(CF, "medium",
  "The High Courts in India are subordinate to the Supreme Court in administrative matters.",
  "भारत में उच्च न्यायालय प्रशासनिक मामलों में उच्चतम न्यायालय के अधीन हैं।",
  "India has a single integrated system of courts, with the Supreme Court at the top.",
  "भारत में न्यायालयों की एक ही एकीकृत व्यवस्था है, जिसके शीर्ष पर उच्चतम न्यायालय है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. The integration is judicial: appeals lie from the High Courts to the Supreme Court and its law binds all courts (Article 141). Administratively, however, the Supreme Court has no power of superintendence over the High Courts -- that power, under Article 227, runs from each High Court to the courts below it -- and the Supreme Court has itself said the High Courts are not subordinate to it.",
  "कथन-I गलत है पर कथन-II सही है। एकीकरण न्यायिक है: उच्च न्यायालयों से अपीलें उच्चतम न्यायालय में जाती हैं और उसकी घोषित विधि सभी न्यायालयों पर बाध्यकारी है (अनुच्छेद 141)। पर प्रशासनिक रूप से उच्चतम न्यायालय के पास उच्च न्यायालयों पर अधीक्षण की कोई शक्ति नहीं है; अनुच्छेद 227 के तहत यह शक्ति हर उच्च न्यायालय से उसके नीचे के न्यायालयों तक जाती है; और उच्चतम न्यायालय ने स्वयं कहा है कि उच्च न्यायालय उसके अधीन नहीं हैं।",
  f"{COI}, Articles 141 and 227; Tirupati Balaji Developers v. State of Bihar (2004).",
  "polity-integrated-judiciary-hc-not-subordinate")

A(CF, "hard",
  "The Preamble was enacted by the Constituent Assembly after the rest of the Constitution had been enacted.",
  "प्रस्तावना को संविधान सभा ने शेष संविधान के अधिनियमित हो जाने के बाद अधिनियमित किया।",
  "The Preamble is not enforceable in a court of law.",
  "प्रस्तावना न्यायालय में प्रवर्तनीय नहीं है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Preamble was taken up last so that it would match the Constitution as finally adopted -- a matter of drafting. That it is non-justiciable, being neither a source of power nor a limit on it, is a separate point about its legal character; courts use it to interpret ambiguous provisions.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। प्रस्तावना को सबसे अंत में इसलिए लिया गया कि वह अंततः अपनाए गए संविधान से मेल खाए; यह मसौदा-निर्माण का विषय है। वह न्यायालय में प्रवर्तनीय नहीं है, क्योंकि वह न शक्ति का स्रोत है न उस पर सीमा; यह उसके विधिक स्वरूप के बारे में एक अलग बात है; न्यायालय अस्पष्ट प्रावधानों की व्याख्या में उसका उपयोग करते हैं।",
  f"{CAD}, 17 October 1949; {NC} -- Philosophy of the Constitution.",
  "polity-preamble-enacted-last-nonjusticiable")

A(CF, "hard",
  "The Rajya Sabha can prevent a Constitution Amendment Bill from being passed, even if the Lok Sabha has passed it.",
  "लोकसभा द्वारा पारित कर दिए जाने पर भी राज्यसभा किसी संविधान संशोधन विधेयक को पारित होने से रोक सकती है।",
  "A Constitution Amendment Bill must be passed by each House separately by a special majority.",
  "संविधान संशोधन विधेयक को हर सदन द्वारा अलग से विशेष बहुमत से पारित होना चाहिए।",
  0,
  "All three statements are correct, and both Statements II and III explain Statement I. Because each House must pass the Bill on its own by a majority of its total membership and two-thirds of those present and voting, and because no joint sitting can be called to override a disagreement, the Rajya Sabha has an effective veto over constitutional amendments -- unlike ordinary Bills, where the Lok Sabha's larger numbers prevail at a joint sitting, or Money Bills, where the Rajya Sabha can only delay.",
  "तीनों कथन सही हैं, और कथन II तथा III दोनों कथन I की व्याख्या करते हैं। चूँकि हर सदन को विधेयक अपने आप में अपनी कुल सदस्य-संख्या के बहुमत और उपस्थित व मत देने वालों के दो-तिहाई से पारित करना होता है, और असहमति दूर करने के लिए संयुक्त बैठक नहीं बुलाई जा सकती, इसलिए संविधान संशोधनों पर राज्यसभा के पास प्रभावी वीटो है; सामान्य विधेयकों से अलग, जहाँ संयुक्त बैठक में लोकसभा की बड़ी संख्या हावी रहती है, या धन विधेयकों से अलग, जिन्हें राज्यसभा केवल रोक कर देर कर सकती है।",
  f"{COI}, Articles 108, 109 and 368(2).",
  "polity-rajya-sabha-veto-amendment",
  s3="There is no provision for a joint sitting of the two Houses on a Constitution Amendment Bill.",
  s3_hi="संविधान संशोधन विधेयक पर दोनों सदनों की संयुक्त बैठक का कोई प्रावधान नहीं है।")

A(CF, "easy",
  "The Constitution of India is often described as a 'living document'.",
  "भारत के संविधान को प्रायः एक 'जीवंत दस्तावेज़' कहा जाता है।",
  "The Constitution of India cannot be amended without the consent of all the States.",
  "सभी राज्यों की सहमति के बिना भारत के संविधान में संशोधन नहीं किया जा सकता।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The Constitution is called a living document because it can be amended and because courts interpret it to meet new situations. Most provisions are amended by Parliament alone; even the federal provisions need ratification by only half of the State Legislatures, not all of them.",
  "कथन-I सही है पर कथन-II गलत है। संविधान को जीवंत दस्तावेज़ इसलिए कहा जाता है कि उसमें संशोधन हो सकता है और न्यायालय नई परिस्थितियों के अनुसार उसकी व्याख्या करते हैं। अधिकांश प्रावधान केवल संसद संशोधित करती है; संघीय प्रावधानों के लिए भी सभी राज्यों का नहीं, केवल आधे राज्य विधानमंडलों का अनुसमर्थन चाहिए।",
  f"{NC} -- Constitution as a Living Document; {COI}, Article 368.",
  "polity-living-document-easy")

# ---------------------------------------------------------------- pairs (medium 2, hard 2)
P(CF, "medium", "Consider the following pairs of words in the Preamble and their meanings:",
  "प्रस्तावना के शब्दों और उनके अर्थों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sovereign : Not subject to any external authority", "Republic : The Head of State is elected and not hereditary",
   "Secular : The State has an official religion but tolerates others", "Socialist : State ownership of the means of production and the abolition of private property"],
  ["संप्रभु : किसी बाहरी सत्ता के अधीन नहीं", "गणराज्य : राष्ट्र का प्रमुख निर्वाचित होता है, वंशानुगत नहीं",
   "पंथनिरपेक्ष : राज्य का एक आधिकारिक धर्म है पर वह दूसरों को सहन करता है", "समाजवादी : उत्पादन के साधनों पर राज्य का स्वामित्व और निजी संपत्ति का उन्मूलन"],
  1,
  "Only pairs 1 and 2 are correct. India decides its internal and external affairs free of any outside control, and its President is elected for a fixed term. "
  "Pair 3 is wrong: Indian secularism means the State has no religion of its own and treats all religions with equal respect, while allowing it to intervene in religious practice for social reform. "
  "Pair 4 is wrong: Indian socialism is 'democratic socialism' -- a mixed economy in which the public and private sectors co-exist -- not the State socialism of the communist model.",
  "केवल युग्म 1 और 2 सही हैं। भारत अपने आंतरिक और बाहरी मामले किसी बाहरी नियंत्रण के बिना तय करता है, और इसके राष्ट्रपति एक निश्चित कार्यकाल के लिए चुने जाते हैं। "
  "युग्म 3 गलत है: भारतीय पंथनिरपेक्षता का अर्थ है कि राज्य का अपना कोई धर्म नहीं है और वह सभी धर्मों को समान सम्मान देता है, साथ ही सामाजिक सुधार के लिए धार्मिक प्रथाओं में हस्तक्षेप कर सकता है। "
  "युग्म 4 गलत है: भारतीय समाजवाद 'लोकतांत्रिक समाजवाद' है, यानी एक मिश्रित अर्थव्यवस्था जिसमें सार्वजनिक और निजी क्षेत्र साथ-साथ चलते हैं; यह साम्यवादी नमूने का राजकीय समाजवाद नहीं है।",
  f"{NC} -- Philosophy of the Constitution; Secularism.",
  "polity-preamble-terms-pairs")

P(CF, "medium", "Consider the following pairs of persons and their roles in the making of the Constitution:",
  "व्यक्तियों और संविधान-निर्माण में उनकी भूमिकाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["H.C. Mukherjee : Vice-President of the Constituent Assembly", "S.N. Mukherjee : Chief Justice of the Federal Court",
   "Prem Behari Narain Raizada : Calligrapher of the original English Constitution", "Nandalal Bose : Calligrapher of the original Hindi Constitution"],
  ["एच.सी. मुखर्जी : संविधान सभा के उपाध्यक्ष", "एस.एन. मुखर्जी : संघीय न्यायालय (फ़ेडरल कोर्ट) के मुख्य न्यायाधीश",
   "प्रेम बिहारी नारायण रायज़ादा : अंग्रेज़ी में मूल संविधान के सुलेखक", "नंदलाल बोस : हिंदी में मूल संविधान के सुलेखक"],
  1,
  "Only pairs 1 and 3 are correct. H.C. Mukherjee was a Vice-President of the Assembly, and Prem Behari Narain Raizada hand-wrote the original English text in flowing italic. "
  "Pair 2 is wrong: S.N. Mukherjee was the Assembly's Chief Draftsman, who gave legal shape to the Drafting Committee's decisions. Pair 4 is wrong: Nandalal Bose and his students of Santiniketan illuminated and decorated the pages; the Hindi version was hand-written by Vasant Krishan Vaidya.",
  "केवल युग्म 1 और 3 सही हैं। एच.सी. मुखर्जी सभा के उपाध्यक्ष थे, और प्रेम बिहारी नारायण रायज़ादा ने प्रवाही इटैलिक शैली में मूल अंग्रेज़ी पाठ हाथ से लिखा। "
  "युग्म 2 गलत है: एस.एन. मुखर्जी सभा के मुख्य प्रारूपकार थे, जिन्होंने प्रारूप समिति के निर्णयों को कानूनी रूप दिया। युग्म 4 गलत है: नंदलाल बोस और शांतिनिकेतन के उनके विद्यार्थियों ने पृष्ठों को चित्रों से सजाया; हिंदी संस्करण वसंत कृष्ण वैद्य ने हाथ से लिखा।",
  f"{CAD}; Lok Sabha Secretariat -- The Constitution of India (calligraphed edition).",
  "polity-ca-persons-roles-pairs")

P(CF, "hard", "Consider the following pairs of scholars and their descriptions of the Indian Constitution or federalism:",
  "विद्वानों और भारतीय संविधान या संघवाद के उनके वर्णनों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Ivor Jennings : 'A lawyers' paradise'", "Granville Austin : 'Cooperative federalism'", "W.H. Morris-Jones : 'Bargaining federalism'", "Paul Appleby : 'Extremely federal'"],
  ["आइवर जेनिंग्स : 'वकीलों का स्वर्ग'", "ग्रैनविल ऑस्टिन : 'सहकारी संघवाद'", "डब्ल्यू.एच. मॉरिस-जोन्स : 'सौदेबाज़ी वाला संघवाद'", "पॉल एपलबी : 'अत्यंत संघीय'"],
  3,
  "All four pairs are correct. Jennings thought the Constitution too long and detailed, a 'lawyers' paradise'; Austin saw Indian federalism as cooperative, with the Union and States working together; Morris-Jones described it as 'bargaining federalism', driven by negotiation between the two levels; and Appleby, a public administration expert, surprisingly found India 'extremely federal' because of how much the Union depended on the States to carry out its programmes. "
  "A student who expects one mismatch will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। जेनिंग्स ने संविधान को बहुत लंबा और विस्तृत, 'वकीलों का स्वर्ग', माना; ऑस्टिन ने भारतीय संघवाद को सहकारी देखा, जिसमें संघ और राज्य मिलकर काम करते हैं; मॉरिस-जोन्स ने इसे दोनों स्तरों के बीच बातचीत से चलने वाला 'सौदेबाज़ी वाला संघवाद' कहा; और लोक प्रशासन विशेषज्ञ एपलबी ने, आश्चर्यजनक रूप से, भारत को 'अत्यंत संघीय' पाया, क्योंकि संघ अपने कार्यक्रम लागू करने के लिए राज्यों पर कितना निर्भर था। "
  "जो विद्यार्थी एक बेमेल की अपेक्षा करता है, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{GA}; W.H. Morris-Jones, The Government and Politics of India; Paul Appleby, Public Administration in India (1953).",
  "polity-scholars-descriptions-pairs")

P(CF, "hard", "Consider the following pairs of princely states and the way they became part of India:",
  "रियासतों और उनके भारत का भाग बनने के तरीके के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Junagadh : A plebiscite", "Hyderabad : Military action ('Operation Polo')", "Manipur : A merger agreement signed in 1949", "Travancore : A plebiscite"],
  ["जूनागढ़ : जनमत-संग्रह", "हैदराबाद : सैन्य कार्रवाई ('ऑपरेशन पोलो')", "मणिपुर : 1949 में हस्ताक्षरित विलय समझौता", "त्रावणकोर : जनमत-संग्रह"],
  2,
  "Three pairs are correct. The Nawab of Junagadh acceded to Pakistan and fled; a plebiscite in February 1948 went overwhelmingly for India. Hyderabad, whose Nizam sought independence, was integrated after police action in September 1948. The Maharaja of Manipur signed a merger agreement in September 1949 without consulting the state's elected Legislative Assembly. "
  "Pair 4 is wrong: Travancore's Dewan C.P. Ramaswami Iyer first declared independence, but after protests and an attempt on his life the Maharaja acceded in July 1947 without any plebiscite.",
  "तीन युग्म सही हैं। जूनागढ़ के नवाब ने पाकिस्तान में विलय किया और भाग गए; फ़रवरी 1948 का जनमत-संग्रह भारी बहुमत से भारत के पक्ष में रहा। स्वतंत्रता चाहने वाले निज़ाम के हैदराबाद को सितंबर 1948 की पुलिस कार्रवाई के बाद एकीकृत किया गया। मणिपुर के महाराजा ने सितंबर 1949 में विलय समझौते पर हस्ताक्षर किए, राज्य की निर्वाचित विधानसभा से परामर्श किए बिना। "
  "युग्म 4 गलत है: त्रावणकोर के दीवान सी.पी. रामास्वामी अय्यर ने पहले स्वतंत्रता की घोषणा की, पर विरोध-प्रदर्शनों और उन पर हमले के बाद महाराजा ने जुलाई 1947 में बिना किसी जनमत-संग्रह के विलय किया।",
  "NCERT Class XII, Politics in India since Independence -- Challenges of Nation Building; V.P. Menon, The Story of the Integration of the Indian States.",
  "polity-princely-states-integration-pairs")

# ---------------------------------------------------------------- easy statement (1)
S(CF, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Constitution of India gives the Supreme Court and the High Courts the power of judicial review.",
   "The President of India is elected directly by the people."],
  ["भारत का संविधान उच्चतम न्यायालय और उच्च न्यायालयों को न्यायिक समीक्षा की शक्ति देता है।",
   "भारत के राष्ट्रपति जनता द्वारा प्रत्यक्ष रूप से चुने जाते हैं।"],
  T2, 0,
  "Only statement 1 is correct: the courts can strike down laws and executive actions that violate the Constitution, through Articles 13, 32 and 226 among others. Statement 2 is wrong: the President is elected indirectly, by an electoral college of the elected members of both Houses of Parliament and of the Legislative Assemblies of the States and of Delhi and Puducherry, by proportional representation with the single transferable vote.",
  "केवल कथन 1 सही है: न्यायालय अनुच्छेद 13, 32 और 226 आदि के ज़रिए संविधान का उल्लंघन करने वाले कानूनों और कार्यकारी कार्यों को रद्द कर सकते हैं। कथन 2 गलत है: राष्ट्रपति संसद के दोनों सदनों और राज्यों तथा दिल्ली और पुदुचेरी की विधानसभाओं के निर्वाचित सदस्यों वाले निर्वाचक-मंडल द्वारा एकल संक्रमणीय मत से आनुपातिक प्रतिनिधित्व के आधार पर अप्रत्यक्ष रूप से चुने जाते हैं।",
  f"{COI}, Articles 13, 32, 54-55 and 226.",
  "polity-judicial-review-president-election")

if __name__ == "__main__":
    write("pol_l2_t1_framework.sql")
