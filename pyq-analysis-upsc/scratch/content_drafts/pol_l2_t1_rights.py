# -*- coding: utf-8 -*-
"""Level 2 · Test 1 (Polity 1: Constitutional Framework & Rights) -- Fundamental Rights, DPSP &
Duties, 28 new bilingual rows against the live gap report: medium statement 10, hard statement 6,
medium MCQ 4, medium Statement-I/II 2, medium pairs 2, hard MCQ 1, hard Statement-I/II/III 1,
easy statement 1, hard pairs 1. The 11 existing rows are not repeated: no new row names Articles
15(2), 17, 18, 20, 21A or 25-28, the Directive Principles in Articles 39A, 40, 43A, 43B, 44, 45,
48A or 50, the EWS clauses, Article 37, or when the Fundamental Duties were added, and none
mentions the 86th Amendment (an existing pairs row tests it)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
FR = "Fundamental Rights, DPSP & Duties"
COI = "Constitution of India"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
SC = "Supreme Court of India"

# ---------------------------------------------------------------- medium statements (10)
S(FR, "medium", "Consider the following statements about the meaning of 'the State' in Article 12:",
  "अनुच्छेद 12 में 'राज्य' के अर्थ के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It includes Parliament and the State Legislatures.",
   "It includes local authorities such as municipalities and panchayats.",
   "A body not created by a statute can also be an 'other authority' if it is financially, functionally and administratively dominated by the Government."],
  ["इसमें संसद और राज्य विधानमंडल शामिल हैं।",
   "इसमें नगरपालिकाएँ और पंचायतें जैसे स्थानीय प्राधिकरण शामिल हैं।",
   "क़ानून द्वारा न बनाया गया कोई निकाय भी 'अन्य प्राधिकरण' हो सकता है, यदि वह वित्तीय, कार्यात्मक और प्रशासनिक रूप से सरकार के प्रभुत्व में हो।"],
  C3, 2,
  "All three statements are correct. Article 12 defines 'the State' for Part III to include the Government and Parliament of India, the Government and Legislature of each State, and all local and other authorities within India or under the control of the Government of India. "
  "The courts have read 'other authorities' widely: in Pradeep Kumar Biswas (2002) a seven-judge bench held that the test is whether the body is financially, functionally and administratively dominated by or under the control of the Government, whatever its form. This matters because Fundamental Rights are mainly enforceable against 'the State'.",
  "तीनों कथन सही हैं। अनुच्छेद 12 भाग III के लिए 'राज्य' में भारत की सरकार और संसद, हर राज्य की सरकार और विधानमंडल, तथा भारत के भीतर या भारत सरकार के नियंत्रण में सभी स्थानीय और अन्य प्राधिकरण शामिल करता है। "
  "न्यायालयों ने 'अन्य प्राधिकरण' को व्यापक रूप से पढ़ा है: प्रदीप कुमार बिस्वास (2002) में सात न्यायाधीशों की पीठ ने माना कि कसौटी यह है कि निकाय, उसका रूप जो भी हो, वित्तीय, कार्यात्मक और प्रशासनिक रूप से सरकार के प्रभुत्व या नियंत्रण में है या नहीं। यह इसलिए महत्त्वपूर्ण है कि मौलिक अधिकार मुख्यतः 'राज्य' के विरुद्ध प्रवर्तनीय हैं।",
  f"{COI}, Article 12; {SC} -- Pradeep Kumar Biswas v. Indian Institute of Chemical Biology (2002).",
  "rights-art12-state-other-authorities")

S(FR, "medium", "Consider the following statements about Article 14:",
  "अनुच्छेद 14 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Equality before the law' is of American origin and 'equal protection of the laws' is of British origin.",
   "It permits reasonable classification based on an intelligible differentia that has a rational relation to the object of the law.",
   "In E.P. Royappa (1974), the Supreme Court held that equality and arbitrariness are sworn enemies."],
  ["'विधि के समक्ष समता' अमेरिकी मूल की है और 'विधियों का समान संरक्षण' ब्रिटिश मूल का है।",
   "यह ऐसे युक्तियुक्त वर्गीकरण की अनुमति देता है जो बोधगम्य अंतर (intelligible differentia) पर आधारित हो और कानून के उद्देश्य से तर्कसंगत संबंध रखता हो।",
   "ई.पी. रोयप्पा (1974) में उच्चतम न्यायालय ने माना कि समता और मनमानापन एक-दूसरे के कट्टर शत्रु हैं।"],
  C3, 1,
  "Statements 2 and 3 are correct. Article 14 forbids class legislation but not classification, and Royappa added that arbitrary State action itself violates equality -- the basis of the 'non-arbitrariness' doctrine later applied in Maneka Gandhi. "
  "Statement 1 reverses the origins: 'equality before the law' comes from the British idea of the rule of law and is a negative concept (no special privileges), while 'equal protection of the laws' comes from the Fourteenth Amendment to the US Constitution and is a positive concept (like treatment in like circumstances).",
  "कथन 2 और 3 सही हैं। अनुच्छेद 14 वर्ग-विधान को मना करता है, वर्गीकरण को नहीं, और रोयप्पा ने जोड़ा कि राज्य का मनमाना कार्य अपने आप में समता का उल्लंघन है; यही 'अमनमानेपन' (non-arbitrariness) के सिद्धांत का आधार है, जो बाद में मेनका गांधी में लागू हुआ। "
  "कथन 1 मूल को उलट देता है: 'विधि के समक्ष समता' विधि के शासन के ब्रिटिश विचार से आती है और एक नकारात्मक धारणा है (कोई विशेषाधिकार नहीं), जबकि 'विधियों का समान संरक्षण' अमेरिकी संविधान के चौदहवें संशोधन से आता है और एक सकारात्मक धारणा है (समान परिस्थितियों में समान व्यवहार)।",
  f"{COI}, Article 14; {SC} -- E.P. Royappa v. State of Tamil Nadu (1974).",
  "rights-art14-origins-classification")

S(FR, "medium", "Consider the following statements about Articles 15 and 16:",
  "अनुच्छेद 15 और 16 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 15(1) prohibits discrimination by the State on grounds of religion, race, caste, sex, place of birth and residence.",
   "Article 16(2) lists descent and residence among the grounds on which discrimination in public employment is prohibited.",
   "A State Legislature can prescribe residence within the State as a condition for employment under that State."],
  ["अनुच्छेद 15(1) राज्य द्वारा धर्म, मूलवंश, जाति, लिंग, जन्मस्थान और निवास के आधार पर विभेद को मना करता है।",
   "अनुच्छेद 16(2) उन आधारों में उद्भव (descent) और निवास को गिनाता है जिन पर सार्वजनिक रोज़गार में विभेद मना है।",
   "कोई राज्य विधानमंडल उस राज्य के अधीन रोज़गार के लिए राज्य में निवास को शर्त के रूप में निर्धारित कर सकता है।"],
  C3, 0,
  "Only statement 2 is correct. The grounds differ between the two Articles: Article 15(1) names religion, race, caste, sex and place of birth only, while Article 16(2) adds descent and residence for public employment. "
  "Statement 3 is wrong: under Article 16(3) only Parliament can prescribe a residence requirement for jobs in a State, so that no State can close its services to other Indians on its own.",
  "केवल कथन 2 सही है। दोनों अनुच्छेदों के आधार अलग हैं: अनुच्छेद 15(1) केवल धर्म, मूलवंश, जाति, लिंग और जन्मस्थान गिनाता है, जबकि अनुच्छेद 16(2) सार्वजनिक रोज़गार के लिए उद्भव और निवास जोड़ता है। "
  "कथन 3 गलत है: अनुच्छेद 16(3) के तहत किसी राज्य की नौकरियों के लिए निवास की शर्त केवल संसद निर्धारित कर सकती है, ताकि कोई राज्य अपने आप अपनी सेवाएँ दूसरे भारतीयों के लिए बंद न कर सके।",
  f"{COI}, Articles 15(1), 16(2) and 16(3).",
  "rights-art15-16-grounds-residence")

S(FR, "medium", "Consider the following statements about Article 19:",
  "अनुच्छेद 19 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Freedom of the press is not mentioned in it expressly but has been held to be part of the freedom of speech and expression.",
   "It guarantees the right to assemble peaceably and without arms.",
   "'The sovereignty and integrity of India' was added as a ground for reasonable restrictions by the 16th Amendment Act."],
  ["प्रेस की स्वतंत्रता का इसमें स्पष्ट उल्लेख नहीं है, पर उसे वाक् और अभिव्यक्ति की स्वतंत्रता का भाग माना गया है।",
   "यह शांतिपूर्वक और बिना हथियारों के एकत्र होने के अधिकार की गारंटी देता है।",
   "'भारत की संप्रभुता और अखंडता' को युक्तियुक्त निर्बंधनों के आधार के रूप में 16वें संशोधन अधिनियम ने जोड़ा।"],
  C3, 2,
  "All three statements are correct. The Supreme Court has read press freedom into Article 19(1)(a) since Romesh Thappar and Brij Bhushan (1950); Article 19(1)(b) protects peaceful assembly without arms. The 16th Amendment (1963), passed after the war with China and amid separatist demands, added 'the sovereignty and integrity of India' to clauses (2), (3) and (4).",
  "तीनों कथन सही हैं। उच्चतम न्यायालय ने रोमेश थापर और बृज भूषण (1950) से प्रेस की स्वतंत्रता को अनुच्छेद 19(1)(a) में पढ़ा है; अनुच्छेद 19(1)(b) बिना हथियारों के शांतिपूर्ण सभा की रक्षा करता है। चीन से युद्ध के बाद और अलगाववादी माँगों के बीच पारित 16वें संशोधन (1963) ने खंड (2), (3) और (4) में 'भारत की संप्रभुता और अखंडता' जोड़ी।",
  f"{COI}, Article 19; Constitution (Sixteenth Amendment) Act, 1963; {SC} -- Romesh Thappar v. State of Madras (1950).",
  "rights-art19-press-assembly-16th")

S(FR, "medium", "Consider the following statements about the interpretation of Article 21:",
  "अनुच्छेद 21 की व्याख्या के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Common Cause (2018), the Supreme Court recognised passive euthanasia and advance directives as part of the right to die with dignity.",
   "In A.K. Gopalan (1950), the Supreme Court held that Article 21 protects against arbitrary legislative action as well as arbitrary executive action.",
   "In Francis Coralie Mullin (1981), the Supreme Court held that the right to life includes the right to live with human dignity."],
  ["कॉमन कॉज़ (2018) में उच्चतम न्यायालय ने निष्क्रिय इच्छामृत्यु और अग्रिम निर्देशों (advance directives) को गरिमा के साथ मरने के अधिकार के भाग के रूप में मान्यता दी।",
   "ए.के. गोपालन (1950) में उच्चतम न्यायालय ने माना कि अनुच्छेद 21 मनमाने कार्यकारी कार्य के साथ-साथ मनमाने विधायी कार्य से भी रक्षा करता है।",
   "फ़्रांसिस कोरली मुलिन (1981) में उच्चतम न्यायालय ने माना कि जीवन के अधिकार में मानवीय गरिमा के साथ जीने का अधिकार शामिल है।"],
  C3, 1,
  "Statements 1 and 3 are correct. From Maneka Gandhi (1978) onwards, Article 21 has been read to cover a life with dignity, and Common Cause extended this to a dignified death, allowing life support to be withdrawn under safeguards. "
  "Statement 2 reverses Gopalan: the Court took a narrow view, holding that Article 21 protects only against arbitrary executive action, so any procedure laid down by a valid law would do. Maneka Gandhi overturned that by requiring the procedure itself to be fair, just and reasonable.",
  "कथन 1 और 3 सही हैं। मेनका गांधी (1978) के बाद से अनुच्छेद 21 को गरिमापूर्ण जीवन तक विस्तृत पढ़ा गया है, और कॉमन कॉज़ ने इसे गरिमापूर्ण मृत्यु तक बढ़ाया, सुरक्षा उपायों के साथ जीवन-रक्षक प्रणाली हटाने की अनुमति देकर। "
  "कथन 2 गोपालन को उलट देता है: न्यायालय ने संकीर्ण दृष्टि अपनाई और माना कि अनुच्छेद 21 केवल मनमाने कार्यकारी कार्य से रक्षा करता है, इसलिए किसी वैध कानून द्वारा निर्धारित कोई भी प्रक्रिया पर्याप्त थी। मेनका गांधी ने इसे पलटा और माँगा कि प्रक्रिया स्वयं निष्पक्ष, न्यायसंगत और युक्तियुक्त हो।",
  f"{SC} -- A.K. Gopalan v. State of Madras (1950); Maneka Gandhi v. Union of India (1978); Francis Coralie Mullin v. Administrator, Union Territory of Delhi (1981); Common Cause v. Union of India (2018).",
  "rights-art21-gopalan-dignity-euthanasia")

S(FR, "medium", "Consider the following statements about the right against exploitation:",
  "शोषण के विरुद्ध अधिकार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The prohibition of traffic in human beings and forced labour in Article 23 operates against private persons as well as the State.",
   "Article 23 expressly lists sex among the grounds on which the State cannot discriminate while imposing compulsory service for public purposes.",
   "Article 24 prohibits the employment of children below the age of sixteen years in factories and mines."],
  ["अनुच्छेद 23 में मानव तस्करी और बलात् श्रम का निषेध राज्य के साथ-साथ निजी व्यक्तियों के विरुद्ध भी लागू होता है।",
   "अनुच्छेद 23 सार्वजनिक प्रयोजनों के लिए अनिवार्य सेवा लगाते समय जिन आधारों पर राज्य विभेद नहीं कर सकता, उनमें लिंग का स्पष्ट उल्लेख करता है।",
   "अनुच्छेद 24 कारखानों और खानों में सोलह वर्ष से कम आयु के बच्चों के नियोजन को मना करता है।"],
  C3, 0,
  "Only statement 1 is correct: Article 23 is one of the few rights enforceable against private employers, and the Supreme Court has held that paying less than the minimum wage can amount to forced labour (PUDR, 1982). "
  "Statement 2 is wrong: Article 23(2) lets the State impose compulsory service such as military or social service, and bars discrimination only on grounds of religion, race, caste or class -- sex is not listed. "
  "Statement 3 is wrong: Article 24 protects children below fourteen from work in factories, mines and other hazardous employment.",
  "केवल कथन 1 सही है: अनुच्छेद 23 उन गिने-चुने अधिकारों में है जो निजी नियोक्ताओं के विरुद्ध भी प्रवर्तनीय हैं, और उच्चतम न्यायालय ने माना है कि न्यूनतम मज़दूरी से कम देना बलात् श्रम हो सकता है (PUDR, 1982)। "
  "कथन 2 गलत है: अनुच्छेद 23(2) राज्य को सैन्य या सामाजिक सेवा जैसी अनिवार्य सेवा लगाने देता है, और केवल धर्म, मूलवंश, जाति या वर्ग के आधार पर विभेद को मना करता है; लिंग का उल्लेख नहीं है। "
  "कथन 3 गलत है: अनुच्छेद 24 चौदह वर्ष से कम आयु के बच्चों को कारखानों, खानों और अन्य जोखिम भरे कामों से बचाता है।",
  f"{COI}, Articles 23 and 24; {SC} -- People's Union for Democratic Rights v. Union of India (1982).",
  "rights-art23-24-exploitation")

S(FR, "medium", "Consider the following statements about Articles 29 and 30:",
  "अनुच्छेद 29 और 30 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 30 gives religious, linguistic and cultural minorities the right to establish and administer educational institutions.",
   "For the purposes of Article 30, minority status is determined with reference to the population of the whole country.",
   "Article 29(1) protects the interests of minorities alone."],
  ["अनुच्छेद 30 धार्मिक, भाषाई और सांस्कृतिक अल्पसंख्यकों को शिक्षा संस्थाएँ स्थापित करने और उनका प्रशासन करने का अधिकार देता है।",
   "अनुच्छेद 30 के प्रयोजन से अल्पसंख्यक का दर्जा पूरे देश की जनसंख्या के संदर्भ में तय होता है।",
   "अनुच्छेद 29(1) केवल अल्पसंख्यकों के हितों की रक्षा करता है।"],
  C3, 3,
  "None of the statements is correct. Article 30 speaks only of religious and linguistic minorities; 'cultural' appears in Article 29, not Article 30. "
  "In T.M.A. Pai Foundation (2002), an eleven-judge bench held that since States were reorganised on linguistic lines, both religious and linguistic minorities are identified State by State. "
  "Article 29(1) protects any section of citizens with a distinct language, script or culture of its own -- which can include a group that is a majority elsewhere -- so it is not confined to minorities, although its heading uses the word.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 30 केवल धार्मिक और भाषाई अल्पसंख्यकों की बात करता है; 'संस्कृति' शब्द अनुच्छेद 29 में है, अनुच्छेद 30 में नहीं। "
  "टी.एम.ए. पाई फ़ाउंडेशन (2002) में ग्यारह न्यायाधीशों की पीठ ने माना कि चूँकि राज्यों का पुनर्गठन भाषाई आधार पर हुआ, इसलिए धार्मिक और भाषाई, दोनों अल्पसंख्यकों की पहचान राज्य-दर-राज्य होती है। "
  "अनुच्छेद 29(1) अपनी अलग भाषा, लिपि या संस्कृति वाले नागरिकों के किसी भी वर्ग की रक्षा करता है, जिसमें ऐसा समूह भी हो सकता है जो कहीं और बहुसंख्यक हो; इसलिए यह अल्पसंख्यकों तक सीमित नहीं है, भले ही इसके शीर्षक में यह शब्द आता है।",
  f"{COI}, Articles 29 and 30; {SC} -- T.M.A. Pai Foundation v. State of Karnataka (2002).",
  "rights-art29-30-minorities")

S(FR, "medium", "Consider the following statements about the enforcement of Fundamental Rights:",
  "मौलिक अधिकारों के प्रवर्तन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The right to move the Supreme Court for the enforcement of Fundamental Rights is itself a Fundamental Right.",
   "The High Courts can issue writs for the enforcement of ordinary legal rights as well as Fundamental Rights.",
   "Parliament can empower any other court to issue writs within its local limits for the enforcement of Fundamental Rights."],
  ["मौलिक अधिकारों के प्रवर्तन के लिए उच्चतम न्यायालय जाने का अधिकार स्वयं एक मौलिक अधिकार है।",
   "उच्च न्यायालय मौलिक अधिकारों के साथ-साथ सामान्य विधिक अधिकारों के प्रवर्तन के लिए भी रिट जारी कर सकते हैं।",
   "संसद किसी अन्य न्यायालय को अपनी स्थानीय सीमाओं के भीतर मौलिक अधिकारों के प्रवर्तन के लिए रिट जारी करने की शक्ति दे सकती है।"],
  C3, 2,
  "All three statements are correct. Because the remedy is itself guaranteed in Part III, the Supreme Court cannot refuse to hear a genuine petition simply because the Constitution provides no other remedy. Under Article 226 a High Court's writ jurisdiction is wider, reaching 'any other purpose' besides Fundamental Rights. Article 32(3) allows Parliament to confer writ powers on other courts, though no such law has yet been made.",
  "तीनों कथन सही हैं। चूँकि उपचार स्वयं भाग III में गारंटीशुदा है, इसलिए उच्चतम न्यायालय किसी वास्तविक याचिका को केवल इस आधार पर नहीं ठुकरा सकता कि संविधान कोई दूसरा उपचार नहीं देता। अनुच्छेद 226 के तहत उच्च न्यायालय का रिट क्षेत्राधिकार व्यापक है, जो मौलिक अधिकारों के अलावा 'किसी अन्य प्रयोजन' तक जाता है। अनुच्छेद 32(3) संसद को दूसरे न्यायालयों को रिट शक्तियाँ देने देता है, हालाँकि अब तक ऐसा कोई कानून नहीं बना है।",
  f"{COI}, Articles 32 and 226.",
  "rights-writ-jurisdiction-32-226")

S(FR, "medium", "Consider the following statements about the Directive Principles of State Policy:",
  "राज्य के नीति-निदेशक तत्वों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 41 directs the State to secure the right to work, to education and to public assistance in cases of unemployment, old age, sickness and disablement.",
   "Article 42 directs the State to secure just and humane conditions of work and maternity relief.",
   "Article 43 directs the State to secure a minimum wage for all workers."],
  ["अनुच्छेद 41 राज्य को काम, शिक्षा और बेरोज़गारी, बुढ़ापे, बीमारी तथा निःशक्तता में सार्वजनिक सहायता का अधिकार सुनिश्चित करने का निर्देश देता है।",
   "अनुच्छेद 42 राज्य को काम की न्यायसंगत और मानवीय दशाएँ तथा प्रसूति सहायता सुनिश्चित करने का निर्देश देता है।",
   "अनुच्छेद 43 राज्य को सभी कामगारों के लिए न्यूनतम मज़दूरी सुनिश्चित करने का निर्देश देता है।"],
  C3, 1,
  "Statements 1 and 2 are correct; Article 41 is qualified by 'within the limits of its economic capacity and development'. "
  "Statement 3 changes a key word: Article 43 speaks of a living wage and conditions of work ensuring a decent standard of life and full enjoyment of leisure and social and cultural opportunities -- a higher goal than a minimum wage, which only guards against exploitation.",
  "कथन 1 और 2 सही हैं; अनुच्छेद 41 पर 'अपनी आर्थिक सामर्थ्य और विकास की सीमाओं के भीतर' की शर्त है। "
  "कथन 3 एक मुख्य शब्द बदल देता है: अनुच्छेद 43 निर्वाह मज़दूरी (living wage) और ऐसी काम की दशाओं की बात करता है जो उचित जीवन-स्तर तथा अवकाश और सामाजिक-सांस्कृतिक अवसरों का पूरा उपभोग सुनिश्चित करें; यह न्यूनतम मज़दूरी से ऊँचा लक्ष्य है, जो केवल शोषण से बचाती है।",
  f"{COI}, Articles 41-43.",
  "rights-dpsp-41-42-43-living-wage")

S(FR, "medium", "Which of the following are Fundamental Duties under Article 51A?",
  "निम्नलिखित में से कौन-से अनुच्छेद 51A के तहत मौलिक कर्तव्य हैं?",
  ["To develop the scientific temper, humanism and the spirit of inquiry and reform",
   "To pay taxes",
   "To safeguard public property and to abjure violence",
   "To protect and improve the natural environment, including forests, lakes, rivers and wildlife"],
  ["वैज्ञानिक दृष्टिकोण, मानववाद और ज्ञानार्जन तथा सुधार की भावना का विकास करना",
   "कर चुकाना",
   "सार्वजनिक संपत्ति को सुरक्षित रखना और हिंसा से दूर रहना",
   "वनों, झीलों, नदियों और वन्यजीवों सहित प्राकृतिक पर्यावरण की रक्षा और उसका संवर्धन करना"],
  C4, 2,
  "Three are Fundamental Duties: clauses (h), (i) and (g) of Article 51A. "
  "Item 2 is the trap: a duty to pay taxes was suggested during the framing of the duties but was not included, so it is a legal obligation under tax laws rather than a Fundamental Duty. Voting is likewise not among the duties.",
  "तीन मौलिक कर्तव्य हैं: अनुच्छेद 51A के खंड (h), (i) और (g)। "
  "मद 2 जाल है: कर्तव्यों को तय करते समय कर चुकाने का कर्तव्य सुझाया गया था, पर शामिल नहीं किया गया; इसलिए यह मौलिक कर्तव्य नहीं, बल्कि कर-कानूनों के तहत एक विधिक दायित्व है। इसी तरह मतदान भी कर्तव्यों में नहीं है।",
  f"{COI}, Article 51A; {NC} -- Rights in the Indian Constitution.",
  "rights-fundamental-duties-which",
  closing="How many of the above are Fundamental Duties?",
  closing_hi="उपर्युक्त में से कितने मौलिक कर्तव्य हैं?")

# ---------------------------------------------------------------- hard statements (6)
S(FR, "hard", "Consider the following statements about preventive detention under Article 22:",
  "अनुच्छेद 22 के तहत निवारक निरोध के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The grounds of detention must be communicated to the detenu, though facts considered against the public interest need not be disclosed.",
   "Detention beyond three months normally requires an Advisory Board to report that there is sufficient cause for it.",
   "The Constitution itself fixes the maximum period for which a person may be held under a preventive detention law."],
  ["निरोध के आधार निरुद्ध व्यक्ति को बताए जाने चाहिए, हालाँकि लोकहित के विरुद्ध माने गए तथ्य प्रकट करना ज़रूरी नहीं है।",
   "तीन महीने से अधिक निरोध के लिए सामान्यतः सलाहकार बोर्ड की यह रिपोर्ट ज़रूरी है कि उसके लिए पर्याप्त कारण है।",
   "निवारक निरोध कानून के तहत किसी व्यक्ति को अधिकतम कितने समय तक रखा जा सकता है, यह संविधान स्वयं तय करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: Article 22(5) requires the grounds to be communicated and a chance to make a representation, and 22(6) lets the authority withhold facts against the public interest; Article 22(4) requires an Advisory Board of persons qualified to be High Court judges for detention beyond three months, unless Parliament's law under 22(7) provides otherwise. "
  "Statement 3 is wrong: Article 22(7)(b) leaves it to Parliament to prescribe the maximum period of detention under any class of preventive detention law; the Constitution sets only the three-month threshold for the Advisory Board. Detainees are also outside the ordinary arrest safeguards of Article 22(1) and (2), which is why preventive detention is so contested.",
  "कथन 1 और 2 सही हैं: अनुच्छेद 22(5) आधार बताना और अभ्यावेदन का अवसर देना ज़रूरी करता है, और 22(6) प्राधिकारी को लोकहित के विरुद्ध तथ्य रोकने देता है; अनुच्छेद 22(4) तीन महीने से अधिक निरोध के लिए उच्च न्यायालय का न्यायाधीश बनने योग्य व्यक्तियों वाला सलाहकार बोर्ड ज़रूरी करता है, जब तक 22(7) के तहत संसद का कानून अन्यथा न कहे। "
  "कथन 3 गलत है: अनुच्छेद 22(7)(b) किसी भी वर्ग के निवारक निरोध कानून के तहत निरोध की अधिकतम अवधि तय करना संसद पर छोड़ता है; संविधान केवल सलाहकार बोर्ड के लिए तीन महीने की सीमा तय करता है। निरुद्ध व्यक्ति अनुच्छेद 22(1) और (2) के सामान्य गिरफ़्तारी-सुरक्षा उपायों से भी बाहर हैं; इसीलिए निवारक निरोध इतना विवादित है।",
  f"{COI}, Article 22(3)-(7).",
  "rights-art22-preventive-detention")

S(FR, "hard", "Consider the following statements about Articles 33 and 34:",
  "अनुच्छेद 33 और 34 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 33 empowers Parliament, and not the State Legislatures, to restrict or abrogate the Fundamental Rights of members of the armed forces, police forces and intelligence agencies.",
   "The Constitution defines the expression 'martial law'.",
   "A declaration of martial law automatically suspends the writ of habeas corpus."],
  ["अनुच्छेद 33 संसद को, न कि राज्य विधानमंडलों को, सशस्त्र बलों, पुलिस बलों और खुफ़िया एजेंसियों के सदस्यों के मौलिक अधिकारों को सीमित या समाप्त करने की शक्ति देता है।",
   "संविधान 'सेना विधि' (martial law) पद को परिभाषित करता है।",
   "सेना विधि की घोषणा अपने आप बंदी प्रत्यक्षीकरण (habeas corpus) की रिट को निलंबित कर देती है।"],
  C3, 0,
  "Only statement 1 is correct: the power is Parliament's alone, so the rules for the forces are uniform across the country; laws such as the Army Act, 1950 and the Police Forces (Restriction of Rights) Act, 1966 use it. "
  "Statement 2 is wrong: the Constitution uses 'martial law' in Article 34 without defining it; the concept comes from English common law. "
  "Statement 3 is wrong: martial law does not by itself suspend habeas corpus. Article 34 only lets Parliament indemnify acts done to restore order in an area under martial law.",
  "केवल कथन 1 सही है: यह शक्ति केवल संसद की है, ताकि बलों के नियम पूरे देश में एक समान रहें; सेना अधिनियम, 1950 और पुलिस बल (अधिकारों का निर्बंधन) अधिनियम, 1966 जैसे कानून इसी का उपयोग करते हैं। "
  "कथन 2 गलत है: संविधान अनुच्छेद 34 में 'सेना विधि' शब्द का प्रयोग करता है, पर उसे परिभाषित नहीं करता; यह धारणा अंग्रेज़ी कॉमन लॉ से आती है। "
  "कथन 3 गलत है: सेना विधि अपने आप बंदी प्रत्यक्षीकरण को निलंबित नहीं करती। अनुच्छेद 34 केवल संसद को सेना विधि वाले क्षेत्र में व्यवस्था बहाल करने के लिए किए गए कार्यों की क्षतिपूर्ति (indemnity) का कानून बनाने देता है।",
  f"{COI}, Articles 33 and 34; Police Forces (Restriction of Rights) Act, 1966.",
  "rights-art33-34-forces-martial-law")

S(FR, "hard", "Which of the following are Directive Principles of State Policy?",
  "निम्नलिखित में से कौन-से राज्य के नीति-निदेशक तत्व हैं?",
  ["To promote international peace and security",
   "To value and preserve the rich heritage of the country's composite culture",
   "To organise agriculture and animal husbandry on modern and scientific lines",
   "To strive towards excellence in all spheres of individual and collective activity"],
  ["अंतरराष्ट्रीय शांति और सुरक्षा को बढ़ावा देना",
   "देश की सामासिक संस्कृति की समृद्ध विरासत का महत्त्व समझना और उसका परिरक्षण करना",
   "कृषि और पशुपालन को आधुनिक और वैज्ञानिक प्रणालियों से संगठित करना",
   "व्यक्तिगत और सामूहिक गतिविधियों के सभी क्षेत्रों में उत्कर्ष की ओर बढ़ने का सतत प्रयास करना"],
  C4, 1,
  "Two are Directive Principles: Article 51 (international peace and security) and Article 48 (agriculture and animal husbandry). "
  "Items 2 and 4 are Fundamental Duties -- Article 51A(f) and 51A(j). The two lists sit next to each other, the Directive Principles ending with Article 51 and the duties following in Article 51A, and they share themes such as heritage and the environment, which is what makes this a trap: the Directive Principles instruct the State, while the duties are addressed to citizens.",
  "दो नीति-निदेशक तत्व हैं: अनुच्छेद 51 (अंतरराष्ट्रीय शांति और सुरक्षा) और अनुच्छेद 48 (कृषि और पशुपालन)। "
  "मद 2 और 4 मौलिक कर्तव्य हैं: अनुच्छेद 51A(f) और 51A(j)। दोनों सूचियाँ पास-पास हैं, नीति-निदेशक तत्व अनुच्छेद 51 पर समाप्त होते हैं और कर्तव्य अनुच्छेद 51A में आते हैं, और दोनों में विरासत और पर्यावरण जैसे विषय साझा हैं; यही इसे जाल बनाता है: नीति-निदेशक तत्व राज्य को निर्देश देते हैं, जबकि कर्तव्य नागरिकों से कहे गए हैं।",
  f"{COI}, Articles 48, 51 and 51A.",
  "rights-dpsp-vs-duties-which",
  closing="How many of the above are Directive Principles?",
  closing_hi="उपर्युक्त में से कितने नीति-निदेशक तत्व हैं?")

S(FR, "hard", "Consider the following statements about Article 13:",
  "अनुच्छेद 13 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the doctrine of eclipse, a pre-Constitution law that violates a Fundamental Right is not void from the start but becomes unenforceable, and revives if the conflict is removed by a constitutional amendment.",
   "Under the doctrine of severability, only the part of a law that violates a Fundamental Right is void, if it can be separated from the rest.",
   "For the purposes of Article 13, 'law' includes ordinances, rules, bye-laws and customs having the force of law."],
  ["आच्छादन के सिद्धांत (doctrine of eclipse) के तहत मौलिक अधिकार का उल्लंघन करने वाला संविधान-पूर्व कानून आरंभ से शून्य नहीं होता, बल्कि अप्रवर्तनीय हो जाता है, और संविधान संशोधन द्वारा टकराव हटने पर फिर से जीवित हो जाता है।",
   "पृथक्करणीयता के सिद्धांत (doctrine of severability) के तहत किसी कानून का केवल वही भाग शून्य होता है जो मौलिक अधिकार का उल्लंघन करता है, यदि उसे शेष से अलग किया जा सके।",
   "अनुच्छेद 13 के प्रयोजन से 'विधि' में अध्यादेश, नियम, उपनियम और विधि का बल रखने वाली रूढ़ियाँ शामिल हैं।"],
  C3, 2,
  "All three statements are correct. In Bhikaji Narain Dhakras (1955) a pre-Constitution law overshadowed by Article 19 revived when the First Amendment removed the conflict; the doctrine of severability comes from the words 'to the extent of the inconsistency' in Article 13; and Article 13(3)(a) defines 'law' broadly to include ordinances, orders, bye-laws, rules, regulations, notifications, customs and usages having the force of law. Students often doubt the last because ordinances are made by the executive.",
  "तीनों कथन सही हैं। भीकाजी नारायण ढाकरास (1955) में अनुच्छेद 19 से आच्छादित एक संविधान-पूर्व कानून पहले संशोधन द्वारा टकराव हटाए जाने पर फिर जीवित हुआ; पृथक्करणीयता का सिद्धांत अनुच्छेद 13 के शब्दों 'उल्लंघन की मात्रा तक' से आता है; और अनुच्छेद 13(3)(a) 'विधि' को व्यापक रूप से परिभाषित करता है, जिसमें अध्यादेश, आदेश, उपनियम, नियम, विनियम, अधिसूचनाएँ, और विधि का बल रखने वाली रूढ़ियाँ व प्रथाएँ शामिल हैं। विद्यार्थी अक्सर अंतिम कथन पर संदेह करते हैं, क्योंकि अध्यादेश कार्यपालिका बनाती है।",
  f"{COI}, Article 13; {SC} -- Bhikaji Narain Dhakras v. State of Madhya Pradesh (1955); R.M.D. Chamarbaugwalla v. Union of India (1957).",
  "rights-art13-eclipse-severability")

S(FR, "hard", "Consider the following statements about the freedoms in Article 19:",
  "अनुच्छेद 19 की स्वतंत्रताओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The freedom to move and to reside anywhere in India can be restricted for the protection of the interests of any Scheduled Tribe.",
   "The State cannot carry on a trade or business to the exclusion of citizens, since that would violate the freedom of profession, trade and business.",
   "The right to form associations includes a Fundamental Right to strike."],
  ["भारत में कहीं भी घूमने और बसने की स्वतंत्रता किसी अनुसूचित जनजाति के हितों की रक्षा के लिए सीमित की जा सकती है।",
   "राज्य नागरिकों को बाहर रखकर कोई व्यापार या कारोबार नहीं चला सकता, क्योंकि इससे वृत्ति, व्यापार और कारोबार की स्वतंत्रता का उल्लंघन होगा।",
   "संगम बनाने के अधिकार में हड़ताल करने का मौलिक अधिकार शामिल है।"],
  C3, 0,
  "Only statement 1 is correct: Article 19(5) allows restrictions on movement and residence in the interests of the general public or of Scheduled Tribes, so that tribal lands and cultures can be shielded from outsiders. "
  "Statement 2 is wrong: Article 19(6)(ii) expressly allows the State to carry on any trade, business, industry or service to the complete or partial exclusion of citizens, which is the basis of State monopolies such as the railways. "
  "Statement 3 is wrong: the Supreme Court has held that there is no Fundamental Right to strike (All India Bank Employees' Association, 1962; T.K. Rangarajan, 2003); strikes are regulated by industrial law.",
  "केवल कथन 1 सही है: अनुच्छेद 19(5) आम जनता या अनुसूचित जनजातियों के हित में घूमने और बसने पर निर्बंधन की अनुमति देता है, ताकि जनजातीय भूमि और संस्कृति को बाहरी लोगों से बचाया जा सके। "
  "कथन 2 गलत है: अनुच्छेद 19(6)(ii) राज्य को नागरिकों को पूरी तरह या आंशिक रूप से बाहर रखकर कोई भी व्यापार, कारोबार, उद्योग या सेवा चलाने की स्पष्ट अनुमति देता है; रेलवे जैसे राजकीय एकाधिकार इसी पर आधारित हैं। "
  "कथन 3 गलत है: उच्चतम न्यायालय ने माना है कि हड़ताल का कोई मौलिक अधिकार नहीं है (ऑल इंडिया बैंक एम्प्लॉइज़ एसोसिएशन, 1962; टी.के. रंगराजन, 2003); हड़तालें औद्योगिक कानूनों से नियंत्रित होती हैं।",
  f"{COI}, Article 19(5) and (6); {SC} -- All India Bank Employees' Association v. National Industrial Tribunal (1962); T.K. Rangarajan v. Government of Tamil Nadu (2003).",
  "rights-art19-tribes-state-trade-strike")

S(FR, "hard", "Consider the following statements about directives found outside Part IV of the Constitution:",
  "संविधान के भाग IV के बाहर पाए जाने वाले निदेशों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 350A directs every State to provide facilities for instruction in the mother tongue at the primary stage to children of linguistic minority groups.",
   "Article 335 requires the claims of Scheduled Castes and Scheduled Tribes to services and posts to be taken into consideration consistently with the maintenance of efficiency of administration.",
   "Unlike the Directive Principles in Part IV, these directives can be enforced in the courts."],
  ["अनुच्छेद 350A हर राज्य को भाषाई अल्पसंख्यक समूहों के बच्चों को प्राथमिक स्तर पर मातृभाषा में शिक्षा की सुविधाएँ देने का निर्देश देता है।",
   "अनुच्छेद 335 अपेक्षा करता है कि सेवाओं और पदों में अनुसूचित जातियों और अनुसूचित जनजातियों के दावों पर प्रशासन की दक्षता बनाए रखते हुए विचार किया जाए।",
   "भाग IV के नीति-निदेशक तत्वों के विपरीत, इन निदेशों को न्यायालयों में प्रवर्तित कराया जा सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Besides Part IV, the Constitution contains other directives -- Article 335 in Part XVI, and Articles 350A and 351 in Part XVII. "
  "Statement 3 is wrong: these too are non-justiciable, though courts give them weight because the Constitution must be read as a whole.",
  "कथन 1 और 2 सही हैं। भाग IV के अलावा संविधान में दूसरे निदेश भी हैं: भाग XVI में अनुच्छेद 335, और भाग XVII में अनुच्छेद 350A और 351। "
  "कथन 3 गलत है: ये भी न्यायालय में प्रवर्तनीय नहीं हैं, हालाँकि न्यायालय इन्हें महत्त्व देते हैं, क्योंकि संविधान को समग्र रूप में पढ़ा जाना चाहिए।",
  f"{COI}, Articles 335 and 350A.",
  "rights-directives-outside-part-iv")

# ---------------------------------------------------------------- MCQs (medium 4, hard 1)
M(FR, "medium", "Which one of the following is NOT a ground on which reasonable restrictions may be imposed on the freedom of speech and expression under Article 19(2)?",
  "निम्नलिखित में से कौन-सा वह आधार नहीं है जिस पर अनुच्छेद 19(2) के तहत वाक् और अभिव्यक्ति की स्वतंत्रता पर युक्तियुक्त निर्बंधन लगाए जा सकते हैं?",
  ["Economic interests of the State", "Public order", "Friendly relations with foreign States", "Contempt of court"],
  ["राज्य के आर्थिक हित", "लोक व्यवस्था", "विदेशी राज्यों के साथ मैत्रीपूर्ण संबंध", "न्यायालय की अवमानना"],
  0,
  "Article 19(2) permits restrictions only in the interests of the sovereignty and integrity of India, the security of the State, friendly relations with foreign States, public order, decency or morality, and in relation to contempt of court, defamation or incitement to an offence. The State's economic interests are not a ground, so a law cannot curb speech merely to protect revenue or business; economic regulation is judged under Article 19(6) instead.",
  "अनुच्छेद 19(2) केवल भारत की संप्रभुता और अखंडता, राज्य की सुरक्षा, विदेशी राज्यों के साथ मैत्रीपूर्ण संबंधों, लोक व्यवस्था, शिष्टाचार या सदाचार के हित में, और न्यायालय की अवमानना, मानहानि या अपराध के लिए उकसाने के संबंध में निर्बंधनों की अनुमति देता है। राज्य के आर्थिक हित आधार नहीं हैं, इसलिए कोई कानून केवल राजस्व या कारोबार की रक्षा के लिए अभिव्यक्ति पर रोक नहीं लगा सकता; आर्थिक नियमन को अनुच्छेद 19(6) के तहत परखा जाता है।",
  f"{COI}, Article 19(2) and (6).",
  "rights-art19-2-grounds-not")

M(FR, "medium", "The safeguards in Article 22(1) and (2) -- being told the grounds of arrest, consulting a lawyer and being produced before a magistrate within 24 hours -- are NOT available to:",
  "अनुच्छेद 22(1) और (2) के सुरक्षा उपाय -- गिरफ़्तारी के आधार बताया जाना, वकील से परामर्श और 24 घंटे के भीतर मजिस्ट्रेट के सामने पेशी -- किसे उपलब्ध नहीं हैं?",
  ["An enemy alien", "A national of a friendly foreign country", "A citizen arrested for a non-bailable offence", "A citizen arrested without a warrant"],
  ["शत्रु विदेशी", "किसी मित्र विदेशी देश का नागरिक", "अजमानतीय अपराध के लिए गिरफ़्तार नागरिक", "बिना वारंट गिरफ़्तार नागरिक"],
  0,
  "Article 22(3) excludes enemy aliens from these safeguards, along with persons held under preventive detention laws. Every other arrested person -- citizen or friendly foreigner, with or without a warrant, for any offence -- is protected; that the safeguards reach foreigners at all is what the distractors play on.",
  "अनुच्छेद 22(3) शत्रु विदेशियों को, निवारक निरोध कानूनों के तहत रखे गए व्यक्तियों के साथ, इन सुरक्षा उपायों से बाहर रखता है। बाकी हर गिरफ़्तार व्यक्ति, नागरिक हो या मित्र देश का विदेशी, वारंट के साथ या बिना, किसी भी अपराध के लिए, संरक्षित है; सुरक्षा उपाय विदेशियों तक भी पहुँचते हैं, गलत विकल्प इसी पर खेलते हैं।",
  f"{COI}, Article 22(1)-(3).",
  "rights-art22-enemy-alien")

M(FR, "medium", "The enforcement of which of the following Fundamental Rights cannot be suspended by the President even during a national emergency?",
  "निम्नलिखित में से किन मौलिक अधिकारों का प्रवर्तन राष्ट्रीय आपात के दौरान भी राष्ट्रपति निलंबित नहीं कर सकते?",
  ["Articles 20 and 21", "Articles 19 and 21", "Articles 14 and 21", "Articles 21 and 32"],
  ["अनुच्छेद 20 और 21", "अनुच्छेद 19 और 21", "अनुच्छेद 14 और 21", "अनुच्छेद 21 और 32"],
  0,
  "Under Article 359, the President can suspend the right to move the courts for the enforcement of Fundamental Rights during an emergency, but not for Articles 20 (protection in respect of conviction for offences) and 21 (life and personal liberty). This limit was written in after ADM Jabalpur (1976), where the Court had held that even habeas corpus could not be sought during the Emergency. Article 19 is the tempting distractor, because it is suspended automatically in an emergency declared on the ground of war or external aggression.",
  "अनुच्छेद 359 के तहत राष्ट्रपति आपात के दौरान मौलिक अधिकारों के प्रवर्तन के लिए न्यायालय जाने का अधिकार निलंबित कर सकते हैं, पर अनुच्छेद 20 (अपराधों के लिए दोषसिद्धि के संबंध में संरक्षण) और 21 (जीवन और व्यक्तिगत स्वतंत्रता) के लिए नहीं। यह सीमा ए.डी.एम. जबलपुर (1976) के बाद जोड़ी गई, जहाँ न्यायालय ने माना था कि आपातकाल में बंदी प्रत्यक्षीकरण भी नहीं माँगा जा सकता। अनुच्छेद 19 आकर्षक गलत विकल्प है, क्योंकि युद्ध या बाहरी आक्रमण के आधार पर घोषित आपात में वह अपने आप निलंबित हो जाता है।",
  f"{COI}, Articles 358 and 359; {SC} -- ADM Jabalpur v. Shivkant Shukla (1976).",
  "rights-art20-21-non-suspendable")

M(FR, "medium", "Guidelines to prevent the sexual harassment of women at the workplace were laid down by the Supreme Court in:",
  "कार्यस्थल पर महिलाओं के यौन उत्पीड़न की रोकथाम के दिशानिर्देश उच्चतम न्यायालय ने किस मामले में दिए?",
  ["Vishaka v. State of Rajasthan", "Maneka Gandhi v. Union of India", "Mohd. Ahmed Khan v. Shah Bano Begum", "Mohini Jain v. State of Karnataka"],
  ["विशाखा बनाम राजस्थान राज्य", "मेनका गांधी बनाम भारत संघ", "मोहम्मद अहमद खान बनाम शाह बानो बेगम", "मोहिनी जैन बनाम कर्नाटक राज्य"],
  0,
  "In Vishaka (1997), filling a gap in legislation, the Court drew on Articles 14, 15, 19(1)(g) and 21 and on India's obligations under CEDAW to lay down binding guidelines. They held the field until Parliament enacted the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013.",
  "विशाखा (1997) में कानून की कमी भरते हुए न्यायालय ने अनुच्छेद 14, 15, 19(1)(g) और 21 तथा CEDAW के तहत भारत के दायित्वों के आधार पर बाध्यकारी दिशानिर्देश दिए। ये तब तक लागू रहे जब तक संसद ने कार्यस्थल पर महिलाओं का लैंगिक उत्पीड़न (निवारण, प्रतिषेध और प्रतितोष) अधिनियम, 2013 नहीं बनाया।",
  f"{SC} -- Vishaka v. State of Rajasthan (1997); Sexual Harassment of Women at Workplace Act, 2013.",
  "rights-vishaka-guidelines")

M(FR, "hard", "Which judgment upheld 27 per cent reservation for the Other Backward Classes in Central Government jobs, subject to the exclusion of the 'creamy layer'?",
  "किस निर्णय ने 'क्रीमी लेयर' को बाहर रखने की शर्त के साथ केंद्र सरकार की नौकरियों में अन्य पिछड़े वर्गों के लिए 27 प्रतिशत आरक्षण को सही ठहराया?",
  ["Indra Sawhney v. Union of India", "Ashoka Kumar Thakur v. Union of India", "M. Nagaraj v. Union of India", "Janhit Abhiyan v. Union of India"],
  ["इंद्रा साहनी बनाम भारत संघ", "अशोक कुमार ठाकुर बनाम भारत संघ", "एम. नागराज बनाम भारत संघ", "जनहित अभियान बनाम भारत संघ"],
  0,
  "Indra Sawhney (1992), the 'Mandal case', upheld the OBC quota in Central Government posts, required the creamy layer to be excluded, fixed a 50 per cent ceiling on reservation except in extraordinary situations, and barred reservation in promotions. Ashoka Kumar Thakur (2008) is the close distractor: it upheld OBC reservation in central educational institutions, not jobs.",
  "इंद्रा साहनी (1992), 'मंडल मामला', ने केंद्र सरकार के पदों में OBC कोटे को सही ठहराया, क्रीमी लेयर को बाहर रखना ज़रूरी किया, असाधारण स्थितियों को छोड़कर आरक्षण पर 50 प्रतिशत की सीमा तय की, और पदोन्नति में आरक्षण को रोका। अशोक कुमार ठाकुर (2008) निकट का गलत विकल्प है: उसने केंद्रीय शिक्षा संस्थानों में OBC आरक्षण को सही ठहराया, नौकरियों में नहीं।",
  f"{SC} -- Indra Sawhney v. Union of India (1992); Ashoka Kumar Thakur v. Union of India (2008).",
  "rights-indra-sawhney-obc-jobs")

# ---------------------------------------------------------------- Statement-I/II (medium 2) and I/II/III (hard 1)
A(FR, "medium",
  "In State of Madras v. Champakam Dorairajan (1951), the Supreme Court held that the Directive Principles have to conform to and run subsidiary to the Fundamental Rights.",
  "मद्रास राज्य बनाम चंपकम दोराईराजन (1951) में उच्चतम न्यायालय ने माना कि नीति-निदेशक तत्वों को मौलिक अधिकारों के अनुरूप और उनके अधीन रहना होगा।",
  "Article 15(4), enabling special provisions for socially and educationally backward classes, was inserted by the First Amendment Act, 1951.",
  "सामाजिक और शैक्षिक रूप से पिछड़े वर्गों के लिए विशेष प्रावधानों को संभव बनाने वाला अनुच्छेद 15(4) पहले संशोधन अधिनियम, 1951 द्वारा जोड़ा गया।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I -- the causation runs the other way. Champakam struck down the Madras communal G.O. that reserved college seats by community, and Parliament responded by inserting Article 15(4). Statement-II is a consequence of the judgment, not its reason.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता; कारण-संबंध उलटी दिशा में है। चंपकम ने मद्रास के उस सांप्रदायिक सरकारी आदेश को रद्द किया जो समुदाय के आधार पर कॉलेज सीटें आरक्षित करता था, और संसद ने इसके उत्तर में अनुच्छेद 15(4) जोड़ा। कथन-II निर्णय का परिणाम है, उसका कारण नहीं।",
  f"{SC} -- State of Madras v. Champakam Dorairajan (1951); Constitution (First Amendment) Act, 1951.",
  "rights-champakam-15-4")

A(FR, "medium",
  "The right to privacy is protected as a Fundamental Right.",
  "निजता का अधिकार मौलिक अधिकार के रूप में संरक्षित है।",
  "In K.S. Puttaswamy (2017), a nine-judge bench held that privacy is intrinsic to the right to life and personal liberty under Article 21.",
  "के.एस. पुट्टास्वामी (2017) में नौ न्यायाधीशों की पीठ ने माना कि निजता अनुच्छेद 21 के तहत जीवन और व्यक्तिगत स्वतंत्रता के अधिकार में अंतर्निहित है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Constitution nowhere mentions privacy; it is protected because Puttaswamy read it into Article 21 and the freedoms of Part III, overruling the earlier view in M.P. Sharma (1954) and Kharak Singh (1962). Like other rights, it can be limited by a law that is necessary and proportionate.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। संविधान में कहीं भी निजता का उल्लेख नहीं है; यह इसलिए संरक्षित है कि पुट्टास्वामी ने इसे अनुच्छेद 21 और भाग III की स्वतंत्रताओं में पढ़ा, एम.पी. शर्मा (1954) और खड़क सिंह (1962) के पहले के मत को पलटते हुए। दूसरे अधिकारों की तरह इसे भी आवश्यक और आनुपातिक कानून द्वारा सीमित किया जा सकता है।",
  f"{SC} -- Justice K.S. Puttaswamy (Retd.) v. Union of India (2017).",
  "rights-privacy-puttaswamy")

A(FR, "hard",
  "Reservation in promotion for Scheduled Castes and Scheduled Tribes is constitutionally permissible.",
  "अनुसूचित जातियों और अनुसूचित जनजातियों के लिए पदोन्नति में आरक्षण संवैधानिक रूप से अनुमेय है।",
  "Article 16(4A), inserted by the 77th Amendment Act, 1995, enables such reservation.",
  "77वें संशोधन अधिनियम, 1995 द्वारा जोड़ा गया अनुच्छेद 16(4A) ऐसे आरक्षण को संभव बनाता है।",
  2,
  "Only one of Statements II and III is correct -- Statement II -- and it explains Statement I. After Indra Sawhney barred reservation in promotions, Parliament inserted Article 16(4A). "
  "Statement III is wrong: M. Nagaraj (2006) upheld Article 16(4A), but required the State to show backwardness, inadequacy of representation and the effect on administrative efficiency before providing such reservation; Jarnail Singh (2018) later dropped the need to show backwardness for SCs and STs.",
  "कथन II और III में से केवल एक, कथन II, सही है और वह कथन I की व्याख्या करता है। इंद्रा साहनी द्वारा पदोन्नति में आरक्षण रोके जाने के बाद संसद ने अनुच्छेद 16(4A) जोड़ा। "
  "कथन III गलत है: एम. नागराज (2006) ने अनुच्छेद 16(4A) को सही ठहराया, पर ऐसा आरक्षण देने से पहले राज्य से पिछड़ेपन, प्रतिनिधित्व की अपर्याप्तता और प्रशासनिक दक्षता पर प्रभाव को दिखाने की अपेक्षा की; जरनैल सिंह (2018) ने बाद में अनुसूचित जातियों और जनजातियों के लिए पिछड़ापन दिखाने की शर्त हटा दी।",
  f"{COI}, Article 16(4A); {SC} -- M. Nagaraj v. Union of India (2006); Jarnail Singh v. Lachhmi Narain Gupta (2018).",
  "rights-promotion-reservation-16-4a",
  s3="In M. Nagaraj (2006), the Supreme Court struck down Article 16(4A).",
  s3_hi="एम. नागराज (2006) में उच्चतम न्यायालय ने अनुच्छेद 16(4A) को रद्द कर दिया।")

# ---------------------------------------------------------------- pairs (medium 2, hard 1)
P(FR, "medium", "Consider the following pairs of writs and their features:",
  "रिटों और उनकी विशेषताओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Habeas corpus : Can be issued against private individuals as well as public authorities",
   "Prohibition : Issued only before a lower court or tribunal decides a matter, to stop it acting beyond its jurisdiction",
   "Certiorari : Cannot be issued against administrative authorities",
   "Quo warranto : Can be sought only by the person aggrieved"],
  ["बंदी प्रत्यक्षीकरण : सार्वजनिक प्राधिकरणों के साथ-साथ निजी व्यक्तियों के विरुद्ध भी जारी हो सकती है",
   "प्रतिषेध : केवल किसी निचले न्यायालय या अधिकरण के मामला तय करने से पहले, उसे अधिकार-क्षेत्र से बाहर जाने से रोकने के लिए जारी होती है",
   "उत्प्रेषण : प्रशासनिक प्राधिकरणों के विरुद्ध जारी नहीं हो सकती",
   "अधिकार-पृच्छा : केवल पीड़ित व्यक्ति ही माँग सकता है"],
  1,
  "Only pairs 1 and 2 are correct. Habeas corpus lies against anyone holding a person unlawfully, and prohibition is purely preventive, issued while proceedings are pending. "
  "Pair 3 is wrong: certiorari, once confined to judicial and quasi-judicial bodies, can now be issued against administrative authorities whose orders affect individual rights. "
  "Pair 4 is wrong: quo warranto tests a person's title to a public office, and any interested person may seek it -- the requirement that the petitioner be aggrieved is relaxed for this writ.",
  "केवल युग्म 1 और 2 सही हैं। बंदी प्रत्यक्षीकरण किसी व्यक्ति को अवैध रूप से रोकने वाले किसी के भी विरुद्ध जारी हो सकती है, और प्रतिषेध पूरी तरह निवारक है, जो कार्यवाही लंबित रहने के दौरान जारी होती है। "
  "युग्म 3 गलत है: उत्प्रेषण, जो कभी न्यायिक और अर्ध-न्यायिक निकायों तक सीमित थी, अब उन प्रशासनिक प्राधिकरणों के विरुद्ध भी जारी हो सकती है जिनके आदेश व्यक्तिगत अधिकारों को प्रभावित करते हैं। "
  "युग्म 4 गलत है: अधिकार-पृच्छा किसी व्यक्ति के सार्वजनिक पद पर अधिकार को परखती है, और कोई भी हितबद्ध व्यक्ति इसे माँग सकता है; इस रिट के लिए याचिकाकर्ता के पीड़ित होने की शर्त ढीली है।",
  f"{COI}, Articles 32 and 226; {NC} -- Rights in the Indian Constitution.",
  "rights-writs-features-pairs")

P(FR, "medium", "Consider the following pairs of Articles and the Directive Principles they contain:",
  "अनुच्छेदों और उनमें दिए गए नीति-निदेशक तत्वों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Article 38 : Minimising inequalities in income, status, facilities and opportunities",
   "Article 39(d) : Equal pay for equal work for both men and women",
   "Article 46 : Promoting the educational and economic interests of the Scheduled Castes, Scheduled Tribes and other weaker sections",
   "Article 47 : Raising the level of nutrition and the standard of living, and improving public health"],
  ["अनुच्छेद 38 : आय, प्रतिष्ठा, सुविधाओं और अवसरों की असमानताओं को कम करना",
   "अनुच्छेद 39(d) : पुरुषों और स्त्रियों, दोनों के लिए समान काम का समान वेतन",
   "अनुच्छेद 46 : अनुसूचित जातियों, अनुसूचित जनजातियों और अन्य दुर्बल वर्गों के शैक्षिक और आर्थिक हितों को बढ़ावा देना",
   "अनुच्छेद 47 : पोषण-स्तर और जीवन-स्तर को ऊँचा करना और सार्वजनिक स्वास्थ्य में सुधार"],
  3,
  "All four pairs are correct. Article 38(2) directs the State to minimise inequalities; Article 39(d) is the basis on which the courts have enforced equal pay through the Equal Remuneration Act (now part of the Code on Wages, 2019); Article 46 underpins protective measures for weaker sections; and Article 47 joins public health with the prohibition of intoxicating drinks. "
  "A student who expects one mismatch in every set will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। अनुच्छेद 38(2) राज्य को असमानताएँ कम करने का निर्देश देता है; अनुच्छेद 39(d) वह आधार है जिस पर न्यायालयों ने समान पारिश्रमिक अधिनियम (अब वेतन संहिता, 2019 का भाग) के ज़रिए समान वेतन लागू किया; अनुच्छेद 46 दुर्बल वर्गों के संरक्षणात्मक उपायों का आधार है; और अनुच्छेद 47 सार्वजनिक स्वास्थ्य को मादक पेयों के निषेध से जोड़ता है। "
  "जो विद्यार्थी हर सेट में एक बेमेल की अपेक्षा करता है, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{COI}, Articles 38, 39, 46 and 47.",
  "rights-dpsp-articles-pairs")

P(FR, "hard", "Consider the following pairs of Supreme Court judgments and what they held:",
  "उच्चतम न्यायालय के निर्णयों और उनमें कही गई बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Olga Tellis (1985) : The right to livelihood is part of the right to life",
   "Hussainara Khatoon (1979) : The right to a speedy trial",
   "Shreya Singhal (2015) : Struck down the offence of sedition in Section 124A of the Indian Penal Code",
   "Navtej Singh Johar (2018) : Decriminalised consensual same-sex relations between adults"],
  ["ओल्गा टेलिस (1985) : आजीविका का अधिकार जीवन के अधिकार का भाग है",
   "हुसैनारा खातून (1979) : शीघ्र सुनवाई (speedy trial) का अधिकार",
   "श्रेया सिंघल (2015) : भारतीय दंड संहिता की धारा 124A के राजद्रोह के अपराध को रद्द किया",
   "नवतेज सिंह जौहर (2018) : वयस्कों के बीच सहमति से समलैंगिक संबंधों को अपराध की श्रेणी से बाहर किया"],
  2,
  "Three pairs are correct. Olga Tellis, the Bombay pavement dwellers' case, linked livelihood to life; Hussainara Khatoon, on undertrials held for years in Bihar's jails, established speedy trial as part of Article 21; and Navtej Singh Johar read down Section 377 of the IPC. "
  "Pair 3 is wrong: Shreya Singhal struck down Section 66A of the Information Technology Act, 2000 for vagueness and its chilling effect on speech. Sedition was not struck down there; its use was put on hold by the Court in 2022, and the Bharatiya Nyaya Sanhita, 2023 dropped the offence in that form.",
  "तीन युग्म सही हैं। मुंबई के फ़ुटपाथ-निवासियों वाले ओल्गा टेलिस मामले ने आजीविका को जीवन से जोड़ा; बिहार की जेलों में वर्षों से बंद विचाराधीन क़ैदियों वाले हुसैनारा खातून मामले ने शीघ्र सुनवाई को अनुच्छेद 21 का भाग बनाया; और नवतेज सिंह जौहर ने IPC की धारा 377 को सीमित किया। "
  "युग्म 3 गलत है: श्रेया सिंघल ने सूचना प्रौद्योगिकी अधिनियम, 2000 की धारा 66A को अस्पष्टता और अभिव्यक्ति पर डराने वाले प्रभाव के कारण रद्द किया। राजद्रोह वहाँ रद्द नहीं हुआ; न्यायालय ने 2022 में उसके प्रयोग पर रोक लगाई, और भारतीय न्याय संहिता, 2023 ने उस रूप में यह अपराध हटा दिया।",
  f"{SC} -- Olga Tellis v. Bombay Municipal Corporation (1985); Hussainara Khatoon v. State of Bihar (1979); Shreya Singhal v. Union of India (2015); Navtej Singh Johar v. Union of India (2018); S.G. Vombatkere v. Union of India (2022).",
  "rights-judgments-pairs")

# ---------------------------------------------------------------- easy statement (1)
S(FR, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Fundamental Duties are addressed to citizens and not to foreigners.",
   "The right to vote in elections is a Fundamental Right."],
  ["मौलिक कर्तव्य नागरिकों के लिए हैं, विदेशियों के लिए नहीं।",
   "चुनावों में मत देने का अधिकार एक मौलिक अधिकार है।"],
  T2, 0,
  "Only statement 1 is correct: Article 51A opens with 'It shall be the duty of every citizen of India', whereas some Fundamental Rights extend to all persons. Statement 2 is wrong: the right to vote rests on Article 326 (adult suffrage) and the Representation of the People Act, 1951; it is a constitutional and statutory right, not one of the Fundamental Rights in Part III.",
  "केवल कथन 1 सही है: अनुच्छेद 51A 'भारत के प्रत्येक नागरिक का यह कर्तव्य होगा' से शुरू होता है, जबकि कुछ मौलिक अधिकार सभी व्यक्तियों को मिलते हैं। कथन 2 गलत है: मत देने का अधिकार अनुच्छेद 326 (वयस्क मताधिकार) और लोक प्रतिनिधित्व अधिनियम, 1951 पर आधारित है; यह संवैधानिक और वैधानिक अधिकार है, भाग III के मौलिक अधिकारों में से नहीं।",
  f"{COI}, Articles 51A and 326; Representation of the People Act, 1951.",
  "rights-duties-citizens-vote-easy")

if __name__ == "__main__":
    write("pol_l2_t1_rights.sql")
