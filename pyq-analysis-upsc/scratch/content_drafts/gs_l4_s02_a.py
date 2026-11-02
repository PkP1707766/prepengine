# -*- coding: utf-8 -*-
"""Level 4 · Simulator 2 (GS Paper I full mock, Layout B: the 2025 shape) -- part A: Polity (13)
(upsc_l4_gs_cell_targets.mjs 2).
Layout B keeps about nine Statement-I/II items across the paper, Statement III included, and is harder than Layout A
(9% easy, 36% hard). Every tested proposition was swept against the whole UPSC bank (bank_dump.json, 5,397 rows
after Simulator 1) and is one no row tests: judicial review of Delimitation Commission orders after Rathod (2024);
Articles 344, 349 and 351; Article 246(4) and Parliament's retained power over Union Territories with legislatures;
Article 257; Article 15(5) and Pramati; the Central Administrative Tribunal's exclusions; RTI appeals and penalties;
Bhim Singh, Centre for PIL, Aruna Shanbaug and Hanif Quareshi; Kishansing Tomar and Article 243U; Articles 322, 112(3)(d)(iii)
and 202(3)(d) against the Election Commission's voted budget; vacation of seats under section 70 of the
Representation of the People Act and Articles 59, 66 and 158; the Prohibition of Child Marriage Act; S. R. Chaudhuri.
MCQ keys are pinned (pos)."""
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
  "An order of the Delimitation Commission, once published in the Gazette, cannot be examined by a constitutional court on any ground.",
  "परिसीमन आयोग का कोई आदेश, राजपत्र में प्रकाशित हो जाने के बाद, किसी भी आधार पर किसी संवैधानिक न्यायालय द्वारा जाँचा नहीं जा सकता।",
  "Article 329(a) bars the courts from questioning the validity of any law relating to the delimitation of constituencies made under Article 327 or Article 328.",
  "अनुच्छेद 329(क) न्यायालयों को अनुच्छेद 327 या अनुच्छेद 328 के अंतर्गत बनी, निर्वाचन-क्षेत्रों के परिसीमन से संबंधित किसी विधि की वैधता पर प्रश्न उठाने से रोकता है।",
  3,
  "Statement I is incorrect but Statement II is correct. Article 329(a) shields any law on the delimitation of constituencies or the allotment of seats made under Article 327 or 328 from challenge in the courts, and section 10(2) of the Delimitation Act, 2002 gives the Commission's published orders the force of law and says that they shall not be called in question in any court. In Meghraj Kothari (1966) a Constitution Bench treated such orders as 'law' covered by the bar, so that elections are not held up by litigation over boundaries. "
  "But in Kishorchandra Chhanganlal Rathod (2024) the Supreme Court held that the bar is not total: a constitutional court may still examine an order of the Commission that is manifestly arbitrary or irreconcilable with constitutional values, though it will be slow to interfere once the electoral process is under way. The bar narrows judicial review rather than removing it -- which matters as the next delimitation, after the freeze on seats ends, approaches.",
  "कथन I ग़लत है पर कथन II सही है। अनुच्छेद 329(क) अनुच्छेद 327 या 328 के अंतर्गत बनी, निर्वाचन-क्षेत्रों के परिसीमन या सीटों के आवंटन संबंधी किसी विधि को न्यायालयों में चुनौती से बचाता है, और परिसीमन अधिनियम, 2002 की धारा 10(2) आयोग के प्रकाशित आदेशों को विधि का बल देती है और कहती है कि किसी न्यायालय में उन पर प्रश्न नहीं उठाया जाएगा। मेघराज कोठारी (1966) में एक संविधान पीठ ने ऐसे आदेशों को इस रोक के अंतर्गत आने वाली 'विधि' माना, ताकि सीमाओं को लेकर मुक़दमेबाज़ी से चुनाव न रुकें। "
  "पर किशोरचंद्र छगनलाल राठौड़ (2024) में सर्वोच्च न्यायालय ने कहा कि यह रोक पूर्ण नहीं है: कोई संवैधानिक न्यायालय आयोग के ऐसे आदेश की जाँच फिर भी कर सकता है जो प्रकट रूप से मनमाना हो या संवैधानिक मूल्यों से मेल न खाता हो, यद्यपि चुनाव प्रक्रिया आरंभ हो जाने के बाद वह हस्तक्षेप में संयम बरतेगा। यह रोक न्यायिक पुनर्विलोकन को सीमित करती है, समाप्त नहीं करती -- जो सीटों पर लगी रोक समाप्त होने के बाद होने वाले अगले परिसीमन को देखते हुए महत्त्वपूर्ण है।",
  COI + ", Articles 327-329; Delimitation Act, 2002, section 10; Meghraj Kothari v. Delimitation Commission (1966); Kishorchandra Chhanganlal Rathod v. Union of India (2024).",
  "l4-s02-pol-delimitation-orders-rathod-329a", craft="precision")

# ---------------------------------------------------------------- Constitutional Framework (statement, hard)
S("Constitutional Framework", "hard", "With reference to the provisions on official language in Part XVII of the Constitution, consider the following statements:",
  "संविधान के भाग XVII में राजभाषा संबंधी प्रावधानों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 344 required the President to constitute an Official Language Commission at the end of five years from the commencement of the Constitution, and again at the end of ten years.",
   "The Committee of Parliament that examines the recommendations of such a Commission is drawn from the Lok Sabha alone.",
   "Article 349 permanently requires the President's previous sanction for introducing any Bill on the language to be used in the Supreme Court.",
   "Article 351 directs the Union to draw for the vocabulary of Hindi primarily on Hindustani."],
  ["अनुच्छेद 344 राष्ट्रपति से अपेक्षा करता था कि वे संविधान के प्रारंभ से पाँच वर्ष की समाप्ति पर, और फिर दस वर्ष की समाप्ति पर, एक राजभाषा आयोग गठित करें।",
   "ऐसे आयोग की संस्तुतियों की जाँच करने वाली संसद की समिति केवल लोक सभा से ली जाती है।",
   "अनुच्छेद 349 सर्वोच्च न्यायालय में प्रयुक्त होने वाली भाषा संबंधी कोई भी विधेयक प्रस्तुत करने के लिए स्थायी रूप से राष्ट्रपति की पूर्व स्वीकृति अपेक्षित करता है।",
   "अनुच्छेद 351 संघ को निर्देश देता है कि वह हिंदी की शब्दावली के लिए मुख्यतः हिंदुस्तानी पर निर्भर रहे।"],
  C4, 0,
  "Only statement 1 is correct. Article 344(1) provides for a Commission at the expiration of five years and again at the expiration of ten years from the commencement; the first, under B. G. Kher, was set up in 1955 and reported in 1956. Statement 2 is wrong: Article 344(4) sets up a Committee of thirty members -- twenty from the Lok Sabha and ten from the Rajya Sabha, elected by proportional representation by the single transferable vote -- which examines the Commission's recommendations and reports to the President. "
  "Statement 3 is wrong: the President's previous sanction under Article 349 was needed only during the first fifteen years from the commencement, for Bills on the language of the Supreme Court and the High Courts and of Acts, Bills and orders under Article 348(1). Statement 4 is wrong: Article 351 asks the Union to develop Hindi by assimilating the forms, style and expressions of Hindustani and of the other Eighth Schedule languages, and to draw for its vocabulary primarily on Sanskrit and secondarily on other languages. Together these Articles set a managed, time-bound transition from English -- which is why the Official Languages Act, 1963 could continue English after 1965.",
  "केवल कथन 1 सही है। अनुच्छेद 344(1) प्रारंभ से पाँच वर्ष की समाप्ति पर और फिर दस वर्ष की समाप्ति पर एक आयोग का प्रावधान करता है; पहला आयोग, बी. जी. खेर के अधीन, 1955 में बना और 1956 में उसने प्रतिवेदन दिया। कथन 2 ग़लत है: अनुच्छेद 344(4) तीस सदस्यों की एक समिति बनाता है -- बीस लोक सभा से और दस राज्य सभा से, जो एकल संक्रमणीय मत द्वारा आनुपातिक प्रतिनिधित्व से चुने जाते हैं -- जो आयोग की संस्तुतियों की जाँच कर राष्ट्रपति को प्रतिवेदन देती है। "
  "कथन 3 ग़लत है: अनुच्छेद 349 के अंतर्गत राष्ट्रपति की पूर्व स्वीकृति केवल प्रारंभ से पहले पंद्रह वर्षों में आवश्यक थी, सर्वोच्च न्यायालय और उच्च न्यायालयों की भाषा तथा अनुच्छेद 348(1) के अधीन अधिनियमों, विधेयकों और आदेशों की भाषा संबंधी विधेयकों के लिए। कथन 4 ग़लत है: अनुच्छेद 351 संघ से कहता है कि वह हिंदुस्तानी और आठवीं अनुसूची की अन्य भाषाओं के रूप, शैली और पदों को आत्मसात करते हुए हिंदी का विकास करे, और उसकी शब्दावली के लिए मुख्यतः संस्कृत और गौणतः अन्य भाषाओं से शब्द ग्रहण करे। ये अनुच्छेद मिलकर अंग्रेज़ी से एक नियोजित, समयबद्ध संक्रमण तय करते हैं -- इसी कारण राजभाषा अधिनियम, 1963 1965 के बाद भी अंग्रेज़ी को जारी रख सका।",
  COI + ", Articles 344, 348, 349 and 351; Report of the Official Language Commission (1956); Official Languages Act, 1963.",
  "l4-s02-pol-part17-art344-349-351-official-language", craft="precision")

# ---------------------------------------------------------------- Constitutional Framework (statement, medium)
S("Constitutional Framework", "medium", "With reference to legislation for the Union Territories, consider the following statements:",
  "संघ राज्यक्षेत्रों के लिए विधि-निर्माण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Parliament can make laws for a Union Territory on matters in the State List.",
   "Once a Union Territory has a Legislative Assembly, Parliament can no longer make laws for it on matters in the State List."],
  ["संसद किसी संघ राज्यक्षेत्र के लिए राज्य सूची के विषयों पर विधि बना सकती है।",
   "किसी संघ राज्यक्षेत्र में विधान सभा बन जाने के बाद संसद उसके लिए राज्य सूची के विषयों पर विधि नहीं बना सकती।"],
  T2, 0,
  "Only statement 1 is correct. Article 246(4) lets Parliament make laws for any part of India not included in a State, even on matters in the State List, because that List exists for the States. Statement 2 is wrong: an Assembly given to a Union Territory shares the field without displacing Parliament. The Government of Union Territories Act, 1963, made under Article 239A, lets the Puducherry Assembly legislate on State and Concurrent List matters but says that nothing in it derogates from Parliament's power, and Article 239AA(3)(b) says expressly that Parliament keeps its power to make laws on any matter for Delhi; where the two conflict, the law of Parliament prevails. "
  "This is the core difference between a Union Territory with a legislature and a State: the Assembly's competence rests on a law of Parliament or a special provision, and is not guaranteed against Parliament as a State's competence is.",
  "केवल कथन 1 सही है। अनुच्छेद 246(4) संसद को भारत के उस किसी भी भाग के लिए, जो किसी राज्य में सम्मिलित नहीं है, राज्य सूची के विषयों पर भी विधि बनाने देता है, क्योंकि वह सूची राज्यों के लिए है। कथन 2 ग़लत है: किसी संघ राज्यक्षेत्र को दी गई विधान सभा संसद को हटाए बिना इस क्षेत्र में भागीदार बनती है। अनुच्छेद 239क के अंतर्गत बना संघ राज्यक्षेत्र शासन अधिनियम, 1963 पुदुचेरी विधान सभा को राज्य और समवर्ती सूची के विषयों पर विधि बनाने देता है, पर कहता है कि इससे संसद की शक्ति में कोई कमी नहीं होती, और अनुच्छेद 239कक(3)(ख) स्पष्ट कहता है कि दिल्ली के लिए किसी भी विषय पर विधि बनाने की शक्ति संसद के पास बनी रहती है; दोनों में टकराव होने पर संसद की विधि प्रभावी होती है। "
  "विधानमंडल वाले संघ राज्यक्षेत्र और राज्य में यही मूल अंतर है: विधान सभा की क्षमता संसद की किसी विधि या विशेष प्रावधान पर टिकी है, और राज्य की क्षमता की तरह संसद के विरुद्ध प्रत्याभूत नहीं है।",
  COI + ", Articles 239A, 239AA(3) and 246(4); Government of Union Territories Act, 1963, section 18.",
  "l4-s02-pol-art246-4-ut-state-list-parliament", craft="linkage")

# ---------------------------------------------------------------- Federalism & Special Provisions (statement, medium)
S("Federalism & Special Provisions", "medium", "With reference to Article 257 of the Constitution, consider the following statements:",
  "संविधान के अनुच्छेद 257 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Union may give directions to a State on the construction and maintenance of means of communication declared to be of national or military importance.",
   "The Union may give directions to a State on the measures to be taken to protect the railways within the State.",
   "Where carrying out such directions costs a State more than its normal duties would have, the State bears the extra cost itself."],
  ["संघ किसी राज्य को राष्ट्रीय या सैनिक महत्त्व के घोषित संचार-साधनों के निर्माण और अनुरक्षण के बारे में निर्देश दे सकता है।",
   "संघ किसी राज्य को राज्य के भीतर रेलों की सुरक्षा के लिए किए जाने वाले उपायों के बारे में निर्देश दे सकता है।",
   "जहाँ ऐसे निर्देशों के पालन में किसी राज्य का व्यय उसके सामान्य कर्तव्यों से अधिक हो, वहाँ अतिरिक्त व्यय राज्य स्वयं वहन करता है।"],
  C3, 1,
  "Only statements 1 and 2 are correct. Article 257(1) requires every State to exercise its executive power so as not to impede the Union's, and lets the Union give the directions needed for that. Clause (2) adds directions on means of communication declared to be of national or military importance -- without limiting Parliament's power to declare national highways and waterways or the Union's own works for the armed forces -- and clause (3) directions on protecting the railways within a State. "
  "Statement 3 is wrong: under Article 257(4), where such directions make a State spend more than its normal duties would have required, the Government of India pays the State the extra cost, as agreed or, failing agreement, as fixed by an arbitrator appointed by the Chief Justice of India. Behind these directions stands Article 365: if a State fails to comply with directions given under the Union's executive power, the President may hold that its government cannot be carried on in accordance with the Constitution.",
  "केवल कथन 1 और 2 सही हैं। अनुच्छेद 257(1) हर राज्य से अपेक्षा करता है कि वह अपनी कार्यपालिका शक्ति का प्रयोग इस प्रकार करे कि संघ की शक्ति में बाधा न पड़े, और संघ को इसके लिए आवश्यक निर्देश देने देता है। खंड (2) राष्ट्रीय या सैनिक महत्त्व के घोषित संचार-साधनों के बारे में निर्देश जोड़ता है -- राष्ट्रीय राजमार्ग और जलमार्ग घोषित करने की संसद की शक्ति या सशस्त्र बलों के लिए संघ के अपने निर्माण-कार्यों को सीमित किए बिना -- और खंड (3) राज्य के भीतर रेलों की सुरक्षा के बारे में निर्देश। "
  "कथन 3 ग़लत है: अनुच्छेद 257(4) के अंतर्गत, जहाँ ऐसे निर्देशों के कारण किसी राज्य को अपने सामान्य कर्तव्यों से अधिक व्यय करना पड़े, वहाँ भारत सरकार राज्य को अतिरिक्त व्यय चुकाती है -- सहमति से, या सहमति न होने पर भारत के मुख्य न्यायाधीश द्वारा नियुक्त मध्यस्थ द्वारा तय राशि। इन निर्देशों के पीछे अनुच्छेद 365 है: यदि कोई राज्य संघ की कार्यपालिका शक्ति के अंतर्गत दिए गए निर्देशों का पालन नहीं करता, तो राष्ट्रपति यह मान सकते हैं कि उसका शासन संविधान के अनुसार नहीं चलाया जा सकता।",
  COI + ", Articles 256, 257 and 365.",
  "l4-s02-pol-art257-communications-railways-extra-cost", craft="precision")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (statement, medium)
S("Fundamental Rights, DPSP & Duties", "medium", "With reference to Article 15(5) of the Constitution, consider the following statements:",
  "संविधान के अनुच्छेद 15(5) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was inserted by the Constitution (Ninety-third Amendment) Act, 2005.",
   "It permits special provisions for the admission of socially and educationally backward classes, Scheduled Castes and Scheduled Tribes to private educational institutions, whether aided or unaided.",
   "It does not apply to the minority educational institutions referred to in Article 30(1).",
   "In Pramati Educational and Cultural Trust (2014), the Supreme Court struck it down as violating the basic structure."],
  ["इसे संविधान (तिरानबेवाँ संशोधन) अधिनियम, 2005 द्वारा जोड़ा गया।",
   "यह सामाजिक और शैक्षिक रूप से पिछड़े वर्गों, अनुसूचित जातियों और अनुसूचित जनजातियों के निजी शिक्षण संस्थानों में, चाहे सहायता-प्राप्त हों या नहीं, प्रवेश के लिए विशेष प्रावधानों की अनुमति देता है।",
   "यह अनुच्छेद 30(1) में उल्लिखित अल्पसंख्यक शिक्षण संस्थानों पर लागू नहीं होता।",
   "प्रमति एजुकेशनल एंड कल्चरल ट्रस्ट (2014) में सर्वोच्च न्यायालय ने इसे मूल ढाँचे का उल्लंघन बताकर रद्द कर दिया।"],
  C4, 2,
  "The first three statements are correct. Article 15(5) was added after P. A. Inamdar (2005) held that the State could not impose reservation on unaided private institutions. It lets the State make special provisions by law for the advancement of socially and educationally backward classes, Scheduled Castes and Scheduled Tribes relating to their admission to educational institutions, including private institutions whether aided or unaided, other than the minority institutions referred to in Article 30(1). "
  "The Central Educational Institutions (Reservation in Admission) Act, 2006 rests on it, and Ashoka Kumar Thakur (2008) upheld 27 per cent reservation for the other backward classes in central institutions with the creamy layer excluded. Statement 4 is wrong: in Pramati (2014) a Constitution Bench upheld Article 15(5) against the challenge of the unaided institutions, and also held that the Right of Children to Free and Compulsory Education Act, 2009 does not apply to minority schools, aided or unaided.",
  "पहले तीन कथन सही हैं। अनुच्छेद 15(5) तब जोड़ा गया जब पी. ए. इनामदार (2005) ने कहा कि राज्य सहायता न पाने वाले निजी संस्थानों पर आरक्षण नहीं थोप सकता। यह राज्य को सामाजिक और शैक्षिक रूप से पिछड़े वर्गों, अनुसूचित जातियों और अनुसूचित जनजातियों की उन्नति के लिए, शिक्षण संस्थानों में उनके प्रवेश के संबंध में, विधि द्वारा विशेष प्रावधान करने देता है -- निजी संस्थानों सहित, चाहे सहायता-प्राप्त हों या नहीं, पर अनुच्छेद 30(1) में उल्लिखित अल्पसंख्यक संस्थानों को छोड़कर। "
  "केंद्रीय शिक्षण संस्थान (प्रवेश में आरक्षण) अधिनियम, 2006 इसी पर टिका है, और अशोक कुमार ठाकुर (2008) ने केंद्रीय संस्थानों में अन्य पिछड़े वर्गों के लिए क्रीमी लेयर को बाहर रखते हुए 27 प्रतिशत आरक्षण को बरक़रार रखा। कथन 4 ग़लत है: प्रमति (2014) में एक संविधान पीठ ने सहायता न पाने वाले संस्थानों की चुनौती के विरुद्ध अनुच्छेद 15(5) को बरक़रार रखा, और यह भी कहा कि निःशुल्क और अनिवार्य बाल शिक्षा का अधिकार अधिनियम, 2009 अल्पसंख्यक विद्यालयों पर, सहायता-प्राप्त हों या नहीं, लागू नहीं होता।",
  COI + ", Article 15(5); Constitution (Ninety-third Amendment) Act, 2005; P. A. Inamdar v. State of Maharashtra (2005); Ashoka Kumar Thakur v. Union of India (2008); Pramati Educational and Cultural Trust v. Union of India (2014).",
  "l4-s02-pol-art15-5-93rd-pramati-minority-excluded", craft="precision")

# ---------------------------------------------------------------- Governance (MCQ, medium)
M("Governance", "medium",
  "The Central Administrative Tribunal can decide a dispute about the conditions of service of which one of the following?",
  "केंद्रीय प्रशासनिक अधिकरण निम्नलिखित में से किसकी सेवा-शर्तों से संबंधित विवाद का निर्णय कर सकता है?",
  ["An IAS officer posted in a Union ministry",
   "An officer on the staff of the Registry of the Supreme Court",
   "A member of the secretarial staff of either House of Parliament",
   "A commissioned officer serving in the Indian Army"],
  ["किसी केंद्रीय मंत्रालय में पदस्थ आईएएस अधिकारी",
   "सर्वोच्च न्यायालय की रजिस्ट्री के कर्मचारी-वर्ग का कोई अधिकारी",
   "संसद के किसी भी सदन के सचिवालयी कर्मचारी-वर्ग का कोई सदस्य",
   "भारतीय सेना में सेवारत कोई कमीशन-प्राप्त अधिकारी"],
  0,
  "The Administrative Tribunals Act, 1985, made under Article 323A, gives the Central Administrative Tribunal jurisdiction over recruitment and conditions of service of persons appointed to the public services and posts of the Union, including members of the All India Services. Section 2 keeps three groups out. Members of the armed forces have their own Armed Forces Tribunal, working since 2009. Officers and servants of the Supreme Court and the High Courts are under the control of the Chief Justices (Articles 146 and 229). "
  "The secretarial staff of Parliament and of the State Legislatures serve under rules made for the Houses (Articles 98 and 187). These exclusions keep the staff of the judiciary and the legislature out of a tribunal set up by executive law, protecting the separation of powers. Since L. Chandra Kumar (1997), a decision of the Tribunal can be challenged before a division bench of the High Court.",
  "अनुच्छेद 323क के अंतर्गत बना प्रशासनिक अधिकरण अधिनियम, 1985 केंद्रीय प्रशासनिक अधिकरण को संघ की लोक सेवाओं और पदों पर नियुक्त व्यक्तियों की भर्ती और सेवा-शर्तों पर अधिकारिता देता है, अखिल भारतीय सेवाओं के सदस्यों सहित। धारा 2 तीन वर्गों को बाहर रखती है। सशस्त्र बलों के सदस्यों के लिए उनका अपना सशस्त्र बल अधिकरण है, जो 2009 से कार्यरत है। सर्वोच्च न्यायालय और उच्च न्यायालयों के अधिकारी और सेवक मुख्य न्यायाधीशों के नियंत्रण में हैं (अनुच्छेद 146 और 229)। "
  "संसद और राज्य विधानमंडलों का सचिवालयी कर्मचारी-वर्ग सदनों के लिए बने नियमों के अधीन सेवा करता है (अनुच्छेद 98 और 187)। ये अपवर्जन न्यायपालिका और विधायिका के कर्मचारियों को कार्यपालिका की विधि से बने अधिकरण से बाहर रखकर शक्तियों के पृथक्करण की रक्षा करते हैं। एल. चंद्र कुमार (1997) के बाद से अधिकरण के निर्णय को उच्च न्यायालय की खंड पीठ के समक्ष चुनौती दी जा सकती है।",
  COI + ", Articles 98, 146, 187, 229 and 323A; Administrative Tribunals Act, 1985, sections 2 and 14; L. Chandra Kumar v. Union of India (1997).",
  "l4-s02-pol-cat-jurisdiction-exclusions-sc-parliament-army", pos=0, craft="application")

# ---------------------------------------------------------------- Governance (statement, medium)
S("Governance", "medium", "With reference to appeals and penalties under the Right to Information Act, 2005, consider the following statements:",
  "सूचना का अधिकार अधिनियम, 2005 के अंतर्गत अपीलों और शास्तियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A first appeal lies to an officer senior in rank to the Public Information Officer, within thirty days of the decision or of the expiry of the time allowed for it.",
   "A second appeal lies to the Information Commission within ninety days of the date on which the first appellate decision was made or should have been made.",
   "A penalty on a Public Information Officer is imposed by the Government on the recommendation of the Information Commission.",
   "The Act provides for an appeal against a decision of the Information Commission to the High Court."],
  ["पहली अपील लोक सूचना अधिकारी से वरिष्ठ पद के किसी अधिकारी के पास, निर्णय से या उसके लिए दिए गए समय की समाप्ति से तीस दिन के भीतर होती है।",
   "दूसरी अपील सूचना आयोग के पास, उस तिथि से नब्बे दिन के भीतर होती है जिस पर पहला अपीलीय निर्णय हुआ या होना चाहिए था।",
   "लोक सूचना अधिकारी पर शास्ति सूचना आयोग की संस्तुति पर सरकार द्वारा लगाई जाती है।",
   "अधिनियम सूचना आयोग के निर्णय के विरुद्ध उच्च न्यायालय में अपील का प्रावधान करता है।"],
  C4, 1,
  "Only statements 1 and 2 are correct. Section 19(1) gives a first appeal to an officer senior to the Public Information Officer within thirty days, which the appellate officer may admit later for sufficient cause, and section 19(3) a second appeal to the Central or State Information Commission within ninety days. In an appeal, the burden of proving that a denial was justified lies on the officer who denied the request (section 19(5)). "
  "Statement 3 is wrong: under section 20(1) the Commission itself imposes the penalty -- ₹250 for each day of delay, up to ₹25,000 -- after hearing the officer; it only recommends disciplinary action, under section 20(2). Statement 4 is wrong: section 19(7) makes the Commission's decision binding and section 23 bars suits and applications in the courts, so the Act provides no appeal; a decision can be challenged only through the writ jurisdiction of the High Courts or the Supreme Court, which no Act can take away.",
  "केवल कथन 1 और 2 सही हैं। धारा 19(1) लोक सूचना अधिकारी से वरिष्ठ अधिकारी के पास तीस दिन के भीतर पहली अपील देती है, जिसे अपीलीय अधिकारी पर्याप्त कारण होने पर बाद में भी स्वीकार कर सकता है, और धारा 19(3) केंद्रीय या राज्य सूचना आयोग के पास नब्बे दिन के भीतर दूसरी अपील। अपील में यह सिद्ध करने का भार कि अनुरोध अस्वीकार करना उचित था, अस्वीकार करने वाले अधिकारी पर होता है (धारा 19(5))। "
  "कथन 3 ग़लत है: धारा 20(1) के अंतर्गत आयोग स्वयं, अधिकारी को सुनने के बाद, शास्ति लगाता है -- विलंब के प्रत्येक दिन के लिए ₹250, अधिकतम ₹25,000; धारा 20(2) के अंतर्गत वह केवल अनुशासनिक कार्रवाई की संस्तुति करता है। कथन 4 ग़लत है: धारा 19(7) आयोग के निर्णय को बाध्यकारी बनाती है और धारा 23 न्यायालयों में वादों और आवेदनों पर रोक लगाती है, इसलिए अधिनियम कोई अपील नहीं देता; निर्णय को केवल उच्च न्यायालयों या सर्वोच्च न्यायालय की रिट अधिकारिता से चुनौती दी जा सकती है, जिसे कोई अधिनियम छीन नहीं सकता।",
  "Right to Information Act, 2005, sections 19, 20 and 23.",
  "l4-s02-pol-rti-appeals-section-19-20-penalty", craft="precision")

# ---------------------------------------------------------------- Judicial-Verdicts (pairs, easy)
P("Judicial-Verdicts", "easy", "Consider the following pairs of judgments of the Supreme Court and what they decided:",
  "सर्वोच्च न्यायालय के निर्णयों और उनके निष्कर्षों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bhim Singh (2010) : Upheld the Members of Parliament Local Area Development Scheme",
   "Centre for PIL (2011) : Quashed the appointment of a Central Vigilance Commissioner",
   "Aruna Shanbaug (2011) : Allowed passive euthanasia subject to safeguards",
   "Mohd. Hanif Quareshi (1958) : Upheld a total ban on the slaughter of cows and calves"],
  ["भीम सिंह (2010) : संसद सदस्य स्थानीय क्षेत्र विकास योजना को बरक़रार रखा",
   "सेंटर फ़ॉर पीआईएल (2011) : एक केंद्रीय सतर्कता आयुक्त की नियुक्ति को रद्द किया",
   "अरुणा शानबाग (2011) : सुरक्षा-उपायों के अधीन निष्क्रिय इच्छामृत्यु की अनुमति दी",
   "मोहम्मद हनीफ़ क़ुरैशी (1958) : गायों और बछड़ों के वध पर पूर्ण प्रतिबंध को बरक़रार रखा"],
  3,
  "All four pairs are correct. In Bhim Singh a Constitution Bench upheld the MPLAD scheme: since members only recommend works, which the district authorities sanction and carry out, the scheme does not breach the separation of powers. In Centre for PIL the Court quashed the appointment of P. J. Thomas as Central Vigilance Commissioner because the selection committee had ignored a pending criminal case against him, and held that institutional integrity, not only personal integrity, must guide such appointments. "
  "In Aruna Shanbaug the Court refused to end the life of a patient in a permanent vegetative state but allowed passive euthanasia, with the approval of a High Court, laying down the safeguards that Common Cause (2018) later extended to living wills. In Mohd. Hanif Quareshi the Court, reading the butchers' right to trade with Article 48, upheld a total ban on slaughtering cows and calves, but held a total ban on slaughtering bulls and buffaloes no longer useful for work or breeding to be an unreasonable restriction; in Mirzapur Moti Kureshi Kassab Jamat (2005) a larger bench upheld a total ban that covered bulls and bullocks too.",
  "चारों युग्म सही हैं। भीम सिंह में एक संविधान पीठ ने सांसद स्थानीय क्षेत्र विकास योजना को बरक़रार रखा: क्योंकि सदस्य केवल कार्यों की संस्तुति करते हैं, जिन्हें ज़िला प्राधिकारी स्वीकृत और क्रियान्वित करते हैं, इसलिए योजना शक्तियों के पृथक्करण का उल्लंघन नहीं करती। सेंटर फ़ॉर पीआईएल में न्यायालय ने पी. जे. थॉमस की केंद्रीय सतर्कता आयुक्त के रूप में नियुक्ति रद्द की, क्योंकि चयन समिति ने उनके विरुद्ध लंबित एक आपराधिक मामले को अनदेखा किया था, और कहा कि ऐसी नियुक्तियों में केवल व्यक्तिगत नहीं, संस्थागत सत्यनिष्ठा भी मार्गदर्शक होनी चाहिए। "
  "अरुणा शानबाग में न्यायालय ने स्थायी अचेत अवस्था की एक रोगी का जीवन समाप्त करने से इनकार किया पर उच्च न्यायालय के अनुमोदन से निष्क्रिय इच्छामृत्यु की अनुमति दी, और वे सुरक्षा-उपाय तय किए जिन्हें कॉमन कॉज़ (2018) ने बाद में लिविंग विल तक बढ़ाया। मोहम्मद हनीफ़ क़ुरैशी में न्यायालय ने क़साइयों के व्यापार के अधिकार को अनुच्छेद 48 के साथ पढ़ते हुए गायों और बछड़ों के वध पर पूर्ण प्रतिबंध को बरक़रार रखा, पर काम या प्रजनन के लिए अब उपयोगी न रहे बैलों और भैंसों के वध पर पूर्ण प्रतिबंध को अनुचित प्रतिबंध माना; मिर्ज़ापुर मोती कुरैशी कसाब जमात (2005) में एक बड़ी पीठ ने ऐसे पूर्ण प्रतिबंध को बरक़रार रखा जिसमें साँड़ और बैल भी शामिल थे।",
  "Bhim Singh v. Union of India (2010); Centre for PIL v. Union of India (2011); Aruna Ramchandra Shanbaug v. Union of India (2011); Mohd. Hanif Quareshi v. State of Bihar (1958); State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (2005).",
  "l4-s02-pol-verdicts-bhim-singh-cpil-shanbaug-hanif-quareshi", craft="recall")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (AR with Statement III, hard)
A("Panchayati Raj & Local Governance", "hard",
  "A State cannot put off elections to a municipality beyond the end of its five-year term on the ground that the delimitation of wards has not been completed.",
  "कोई राज्य किसी नगरपालिका के चुनाव को इस आधार पर उसके पाँच वर्ष के कार्यकाल की समाप्ति के बाद तक नहीं टाल सकता कि वार्डों का परिसीमन पूरा नहीं हुआ है।",
  "Article 243U requires that an election to constitute a municipality be completed before the expiry of its duration.",
  "अनुच्छेद 243प अपेक्षा करता है कि किसी नगरपालिका के गठन के लिए चुनाव उसकी अवधि की समाप्ति से पहले पूरा हो जाए।",
  2,
  "Statement II is correct and explains Statement I; Statement III is incorrect. Article 243U(3) requires an election to be completed before the five-year duration of a municipality expires, or within six months of its dissolution. In Kishansing Tomar (2006) a Constitution Bench held that the State Election Commission must hold the elections on time, that delimitation and the rotation of reserved wards must be completed well in advance and are no excuse for delay, and that the Commission may approach the court if the State Government does not cooperate. "
  "Statement III is wrong: Article 243U(1) fixes the term at five years 'and no longer', with no power of extension. Article 83(2) lets Parliament extend the Lok Sabha by a year at a time during an Emergency, and Article 172(1) does the same for a State Assembly, but Parts IX and IXA give no such power for panchayats or municipalities -- a deliberate choice to end the long postponements of local elections before 1992.",
  "कथन II सही है और कथन I की व्याख्या करता है; कथन III ग़लत है। अनुच्छेद 243प(3) अपेक्षा करता है कि चुनाव नगरपालिका की पाँच वर्ष की अवधि समाप्त होने से पहले, या उसके विघटन के छह माह के भीतर, पूरा हो। किशनसिंह तोमर (2006) में एक संविधान पीठ ने कहा कि राज्य निर्वाचन आयोग को समय पर चुनाव कराने होंगे, कि परिसीमन और आरक्षित वार्डों का चक्रानुक्रम पहले ही पूरा कर लिया जाना चाहिए और वे विलंब का बहाना नहीं हैं, और कि राज्य सरकार सहयोग न करे तो आयोग न्यायालय की शरण ले सकता है। "
  "कथन III ग़लत है: अनुच्छेद 243प(1) कार्यकाल को पाँच वर्ष तय करता है 'और इससे अधिक नहीं', और विस्तार की कोई शक्ति नहीं देता। अनुच्छेद 83(2) संसद को आपातकाल में लोक सभा का कार्यकाल एक बार में एक वर्ष बढ़ाने देता है, और अनुच्छेद 172(1) राज्य विधान सभा के लिए यही करता है, पर भाग IX और IXक पंचायतों या नगरपालिकाओं के लिए ऐसी कोई शक्ति नहीं देते -- 1992 से पहले स्थानीय चुनावों के लंबे स्थगनों को समाप्त करने के लिए किया गया सोचा-समझा चुनाव।",
  COI + ", Articles 83(2), 172(1), 243U and 243ZA; Kishansing Tomar v. Municipal Corporation of the City of Ahmedabad (2006).",
  "l4-s02-pol-kishansing-tomar-243u-no-postponement",
  s3="Article 243U allows the term of a municipality to be extended by one year at a time while a Proclamation of Emergency is in operation.",
  s3_hi="अनुच्छेद 243प आपातकाल की उद्घोषणा लागू रहने के दौरान किसी नगरपालिका का कार्यकाल एक बार में एक वर्ष बढ़ाने की अनुमति देता है।",
  craft="linkage")

# ---------------------------------------------------------------- Parliament & State Legislature (statement, hard)
S("Parliament & State Legislature", "hard", "Consider the following items of expenditure:",
  "व्यय की निम्नलिखित मदों पर विचार कीजिए:",
  ["The administrative expenses of the Union Public Service Commission, including the salaries of its members",
   "The salaries and allowances of the judges of a High Court",
   "The pensions payable to the judges of High Courts",
   "The salaries of the Chief Election Commissioner and the other Election Commissioners"],
  ["संघ लोक सेवा आयोग के प्रशासनिक व्यय, उसके सदस्यों के वेतन सहित",
   "किसी उच्च न्यायालय के न्यायाधीशों के वेतन और भत्ते",
   "उच्च न्यायालयों के न्यायाधीशों को देय पेंशन",
   "मुख्य निर्वाचन आयुक्त और अन्य निर्वाचन आयुक्तों के वेतन"],
  C4, 1,
  "Only two -- items 1 and 3 -- are charged on the Consolidated Fund of India. Article 322 charges the expenses of the UPSC, including the salaries, allowances and pensions of its members and staff, on that Fund (and those of a State Commission on the State's Fund). Article 112(3)(d)(iii) charges the pensions of High Court judges on the Consolidated Fund of India, while Article 202(3)(d) charges their salaries and allowances on the Consolidated Fund of the State -- a split that is easy to miss. "
  "Item 4 is not charged: neither the Constitution nor a law of Parliament declares the Election Commission's expenditure charged, so it is voted every year within the demands of the Ministry of Law and Justice, and the Commission has proposed that it be charged, like that of the UPSC and the CAG, to secure its independence. Charged expenditure may be discussed in Parliament but is not put to the vote (Article 113(1)).",
  "केवल दो -- मद 1 और 3 -- भारत की संचित निधि पर भारित हैं। अनुच्छेद 322 संघ लोक सेवा आयोग के व्यय को, उसके सदस्यों और कर्मचारियों के वेतन, भत्तों और पेंशन सहित, उसी निधि पर भारित करता है (और राज्य आयोग के व्यय को राज्य की निधि पर)। अनुच्छेद 112(3)(घ)(iii) उच्च न्यायालय के न्यायाधीशों की पेंशन को भारत की संचित निधि पर भारित करता है, जबकि अनुच्छेद 202(3)(घ) उनके वेतन और भत्तों को राज्य की संचित निधि पर -- एक ऐसा विभाजन जो आसानी से छूट जाता है। "
  "मद 4 भारित नहीं है: न संविधान और न संसद की कोई विधि निर्वाचन आयोग के व्यय को भारित घोषित करती है, इसलिए यह हर वर्ष विधि और न्याय मंत्रालय की माँगों के भीतर मतदान से पारित होता है, और आयोग ने प्रस्ताव किया है कि उसकी स्वतंत्रता सुनिश्चित करने के लिए उसे संघ लोक सेवा आयोग और नियंत्रक-महालेखापरीक्षक की तरह भारित किया जाए। भारित व्यय पर संसद में चर्चा हो सकती है पर उस पर मतदान नहीं होता (अनुच्छेद 113(1))।",
  COI + ", Articles 112(3), 113(1), 202(3) and 322.",
  "l4-s02-pol-charged-upsc-hc-pensions-not-eci",
  closing="How many of the above are charged on the Consolidated Fund of India?",
  closing_hi="उपर्युक्त में से कितनी मदें भारत की संचित निधि पर भारित हैं?", craft="precision")

# ---------------------------------------------------------------- Parliament & State Legislature (statement, medium)
S("Parliament & State Legislature", "medium", "With reference to the vacation of seats on election to another House or office, consider the following statements:",
  "किसी अन्य सदन या पद पर निर्वाचन होने पर स्थानों के रिक्त होने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A member of the Lok Sabha who is appointed Governor of a State vacates his seat on the date on which he enters upon his office as Governor.",
   "A member of a State Legislative Council who is elected President vacates his seat on the date on which he enters upon his office as President.",
   "A person elected to the Lok Sabha from two constituencies may keep both seats for up to six months.",
   "A member of a State Legislative Assembly who is elected Vice-President may continue to hold his seat in the Assembly."],
  ["किसी राज्य का राज्यपाल नियुक्त होने वाला लोक सभा सदस्य उस तिथि को अपना स्थान रिक्त करता है जिस दिन वह राज्यपाल के रूप में पदग्रहण करता है।",
   "राष्ट्रपति निर्वाचित होने वाला किसी राज्य विधान परिषद का सदस्य उस तिथि को अपना स्थान रिक्त करता है जिस दिन वह राष्ट्रपति के रूप में पदग्रहण करता है।",
   "दो निर्वाचन-क्षेत्रों से लोक सभा के लिए निर्वाचित व्यक्ति छह माह तक दोनों स्थान रख सकता है।",
   "उपराष्ट्रपति निर्वाचित होने वाला राज्य विधान सभा का सदस्य विधान सभा में अपना स्थान बनाए रख सकता है।"],
  C4, 1,
  "Only statements 1 and 2 are correct. The Constitution keeps the heads of State and of the States out of the legislatures. Article 158(1) bars a Governor from being a member of either House of Parliament or of a State Legislature, and a member who is appointed is deemed to vacate the seat on the date on which he enters upon office as Governor. Article 59(1) lays down the same rule for the President, and it covers a member of either House of a State Legislature -- a Legislative Council included -- as much as a member of Parliament. "
  "Statement 3 is wrong: section 33(7) of the Representation of the People Act, 1951 lets a person contest at most two constituencies, and section 70 makes him resign all but one seat within the time fixed by the rules -- fourteen days -- failing which all the seats fall vacant. Statement 4 is wrong: Article 66(2) applies the same rule to the Vice-President, so the Assembly seat is vacated when he enters upon office; the presiding role of the Vice-President in the Rajya Sabha does not make him one of its members.",
  "केवल कथन 1 और 2 सही हैं। संविधान राष्ट्र और राज्यों के प्रमुखों को विधानमंडलों से बाहर रखता है। अनुच्छेद 158(1) राज्यपाल को संसद के किसी सदन या किसी राज्य विधानमंडल का सदस्य होने से रोकता है, और नियुक्त होने वाला सदस्य राज्यपाल के रूप में पदग्रहण की तिथि को अपना स्थान रिक्त किया हुआ माना जाता है। अनुच्छेद 59(1) राष्ट्रपति के लिए यही नियम तय करता है, और यह संसद सदस्य की तरह ही किसी राज्य विधानमंडल के किसी भी सदन -- विधान परिषद सहित -- के सदस्य पर लागू होता है। "
  "कथन 3 ग़लत है: लोक प्रतिनिधित्व अधिनियम, 1951 की धारा 33(7) किसी व्यक्ति को अधिकतम दो निर्वाचन-क्षेत्रों से चुनाव लड़ने देती है, और धारा 70 उसे नियमों द्वारा तय समय -- चौदह दिन -- के भीतर एक को छोड़ सभी स्थानों से त्यागपत्र देने को बाध्य करती है, अन्यथा सभी स्थान रिक्त हो जाते हैं। कथन 4 ग़लत है: अनुच्छेद 66(2) उपराष्ट्रपति पर भी यही नियम लागू करता है, इसलिए पदग्रहण करते ही विधान सभा का स्थान रिक्त हो जाता है; राज्य सभा में सभापति की भूमिका उपराष्ट्रपति को उसका सदस्य नहीं बनाती।",
  COI + ", Articles 59(1), 66(2) and 158(1); Representation of the People Act, 1951, sections 33(7) and 70.",
  "l4-s02-pol-vacation-of-seats-158-59-66-two-constituencies", craft="multi")

# ---------------------------------------------------------------- Statutory-Laws (statement, medium)
S("Statutory-Laws", "medium", "With reference to the Prohibition of Child Marriage Act, 2006, consider the following statements:",
  "बाल विवाह प्रतिषेध अधिनियम, 2006 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A child marriage is voidable at the option of the party who was a child at the time of the marriage.",
   "A petition to annul such a marriage may be filed by that party at any time before completing two years after attaining majority.",
   "Offences under the Act are cognizable and non-bailable.",
   "A woman aged nineteen who marries a man aged twenty commits the offence, under the Act, of an adult contracting a child marriage."],
  ["बाल विवाह उस पक्षकार के विकल्प पर शून्यकरणीय है जो विवाह के समय बालक था।",
   "ऐसे विवाह को अकृत कराने की याचिका वह पक्षकार वयस्क होने के बाद दो वर्ष पूरे होने से पहले कभी भी दायर कर सकता है।",
   "अधिनियम के अंतर्गत अपराध संज्ञेय और अजमानतीय हैं।",
   "बीस वर्ष के पुरुष से विवाह करने वाली उन्नीस वर्ष की स्त्री अधिनियम के अंतर्गत किसी वयस्क द्वारा बाल विवाह करने का अपराध करती है।"],
  C4, 2,
  "The first three statements are correct. The Act defines a 'child' as a male under twenty-one or a female under eighteen. Section 3 makes a child marriage voidable at the option of the party who was a child, by a petition filed before that party completes two years after attaining majority; section 12 makes it void altogether where the minor was taken by force, enticement or sale, or trafficked. Section 15 makes the offences cognizable and non-bailable, and section 16 lets the State Government appoint Child Marriage Prohibition Officers. "
  "Statement 4 is wrong: here the man of twenty is the 'child', and section 9 punishes only 'a male adult above eighteen years of age' who contracts a child marriage, with rigorous imprisonment of up to two years, a fine of up to ₹1 lakh, or both; the Act also bars imprisoning a woman for promoting or permitting a child marriage. The different ages for men and women remain; a 2021 Bill to raise the age for women to twenty-one lapsed with the Seventeenth Lok Sabha.",
  "पहले तीन कथन सही हैं। अधिनियम 'बालक' को इक्कीस वर्ष से कम आयु के पुरुष या अठारह वर्ष से कम आयु की स्त्री के रूप में परिभाषित करता है। धारा 3 बाल विवाह को उस पक्षकार के विकल्प पर शून्यकरणीय बनाती है जो बालक था, वयस्क होने के बाद दो वर्ष पूरे होने से पहले दायर याचिका द्वारा; धारा 12 उसे पूरी तरह शून्य बनाती है जहाँ अवयस्क को बलपूर्वक, फुसलाकर या बेचकर ले जाया गया हो, या उसका दुर्व्यापार किया गया हो। धारा 15 अपराधों को संज्ञेय और अजमानतीय बनाती है, और धारा 16 राज्य सरकार को बाल विवाह प्रतिषेध अधिकारी नियुक्त करने देती है। "
  "कथन 4 ग़लत है: यहाँ बीस वर्ष का पुरुष 'बालक' है, और धारा 9 केवल 'अठारह वर्ष से अधिक आयु के वयस्क पुरुष' को दंडित करती है जो बाल विवाह करता है -- दो वर्ष तक के कठोर कारावास, ₹1 लाख तक के जुर्माने, या दोनों से; अधिनियम बाल विवाह को बढ़ावा देने या उसकी अनुमति देने के लिए किसी स्त्री को कारावास देने पर भी रोक लगाता है। पुरुषों और स्त्रियों की अलग आयु बनी हुई है; स्त्रियों की आयु इक्कीस करने वाला 2021 का विधेयक सत्रहवीं लोक सभा के साथ व्यपगत हो गया।",
  "Prohibition of Child Marriage Act, 2006, sections 2, 3, 9, 11, 12, 15 and 16.",
  "l4-s02-pol-child-marriage-act-voidable-cognizable-s9-male", craft="application")

# ---------------------------------------------------------------- Union & State Executive (MCQ, medium)
M("Union & State Executive", "medium",
  "A person who is not a member of the State Legislature is appointed a minister and is not elected to the Legislature within six months. According to the Supreme Court, which one of the following is correct?",
  "राज्य विधानमंडल का सदस्य न होने वाला एक व्यक्ति मंत्री नियुक्त होता है और छह माह के भीतर विधानमंडल के लिए निर्वाचित नहीं होता। सर्वोच्च न्यायालय के अनुसार, निम्नलिखित में से कौन-सा सही है?",
  ["He cannot be reappointed during the same Legislature's term without first being elected",
   "He may be reappointed once, for a second period of six months, but never for a third period",
   "He may be reappointed any number of times, if the Chief Minister advises the Governor to do so",
   "He may remain a minister until the Legislative Assembly is next dissolved, but not beyond that"],
  ["वह पहले निर्वाचित हुए बिना उसी विधानमंडल के कार्यकाल में पुनः नियुक्त नहीं हो सकता",
   "वह छह माह की दूसरी अवधि के लिए एक बार पुनः नियुक्त हो सकता है, पर तीसरी अवधि के लिए कभी नहीं",
   "यदि मुख्यमंत्री राज्यपाल को ऐसी सलाह दें तो वह कितनी भी बार पुनः नियुक्त हो सकता है",
   "वह विधान सभा के अगले विघटन तक मंत्री बना रह सकता है, पर उसके बाद नहीं"],
  0,
  "In S. R. Chaudhuri (2001) the Supreme Court struck down the reappointment of a Punjab minister who had not been elected within six months. Article 164(4), like Article 75(5) for the Union, is an exception that lets a non-member serve for six consecutive months only, so that a capable person can be brought in and given time to win a seat; reappointing him without an election during the term of the same Legislature would defeat the representative principle and is a 'fraud on the Constitution'. "
  "The rule does not stop a non-member from becoming a minister once, nor from becoming a member through the Legislative Council where one exists, but it bars the device of resigning and being sworn in again. The same reasoning lies behind the Court's later ruling against repeated re-promulgation of ordinances.",
  "एस. आर. चौधरी (2001) में सर्वोच्च न्यायालय ने पंजाब के उस मंत्री की पुनर्नियुक्ति रद्द कर दी जो छह माह के भीतर निर्वाचित नहीं हुआ था। अनुच्छेद 164(4), संघ के लिए अनुच्छेद 75(5) की तरह, एक अपवाद है जो किसी गैर-सदस्य को केवल लगातार छह माह तक सेवा करने देता है, ताकि किसी योग्य व्यक्ति को लाया जा सके और उसे स्थान जीतने का समय मिले; उसी विधानमंडल के कार्यकाल में बिना चुनाव के उसे फिर नियुक्त करना प्रतिनिधिक सिद्धांत को निष्फल कर देगा और 'संविधान के साथ कपट' है। "
  "यह नियम किसी गैर-सदस्य को एक बार मंत्री बनने से, या जहाँ विधान परिषद है वहाँ उसके माध्यम से सदस्य बनने से नहीं रोकता, पर त्यागपत्र देकर फिर शपथ लेने की युक्ति पर रोक लगाता है। अध्यादेशों के बार-बार पुनर्प्रख्यापन के विरुद्ध न्यायालय के बाद के निर्णय के पीछे भी यही तर्क है।",
  COI + ", Articles 75(5) and 164(4); S. R. Chaudhuri v. State of Punjab (2001).",
  "l4-s02-pol-sr-chaudhuri-non-member-minister-reappointment", pos=3, craft="application")

write("gs_l4_s02_a.sql")
