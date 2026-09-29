# -*- coding: utf-8 -*-
"""Level 2 · Test 3 (Polity 3: Judiciary, Bodies, Elections & Laws) -- Judiciary (5), Judicial-
Verdicts (10), Elections (11) and Constitutional & Statutory Bodies (18): 44 new bilingual rows
against the live gap report.
  Judiciary: medium statement 2, hard statement 1, medium MCQ 1, medium Statement-I/II 1.
  Judicial-Verdicts: medium statement 3, hard statement 2, easy statement 1, hard I/II/III 1,
    medium MCQ 1, medium Statement-I/II 1, medium pairs 1.
  Elections: medium statement 4, hard statement 2, hard MCQ 1, hard I/II/III 1, medium MCQ 1,
    medium Statement-I/II 1, medium pairs 1.
  Bodies: medium statement 6, hard statement 3, medium MCQ 2, hard MCQ 2, medium Statement-I/II 1,
    easy statement 1, hard I/II/III 1, hard pairs 1, medium pairs 1.
The 30 existing rows are not repeated: nothing here says how many judges the Supreme Court has,
how its judges are removed, which Articles 124/214/226/143 or 324-329 are, who sits on the CEC
selection or search committee, how the CEC is removed, what NOTA does, how the RPA disqualifies
or caps constituencies, who conducts local elections, how the CAG is appointed or reports, what
the UPSC/SPSC do, whether the 338-338B commissions or the Finance Commission are constitutional,
or where NITI Aayog stands -- nor any of the verdicts those rows name. Vellore (Environment) and
the GST Council and Inter-State Council (Test 4) are left to their own tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
JU = "Judiciary"
JV = "Judicial-Verdicts"
EL = "Elections"
BO = "Constitutional & Statutory Bodies"
COI = "Constitution of India"
SC = "Supreme Court of India"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
ECI = "Election Commission of India"
RPA = "Representation of the People Act, 1951"

# ================================================================ JUDICIARY (5)
S(JU, "medium", "Consider the following statements about the appointment of judges of the higher judiciary:",
  "उच्चतर न्यायपालिका के न्यायाधीशों की नियुक्ति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The collegium system originated in the Second Judges case (1993).",
   "The Constitution (Ninety-ninth Amendment) Act, which set up the National Judicial Appointments Commission, was struck down by the Supreme Court in 2015.",
   "The Memorandum of Procedure for appointing judges is laid down in the Constitution."],
  ["कॉलेजियम प्रणाली की शुरुआत द्वितीय न्यायाधीश मामले (1993) से हुई।",
   "राष्ट्रीय न्यायिक नियुक्ति आयोग बनाने वाले संविधान (99वाँ संशोधन) अधिनियम को उच्चतम न्यायालय ने 2015 में रद्द कर दिया।",
   "न्यायाधीशों की नियुक्ति का प्रक्रिया-ज्ञापन (Memorandum of Procedure) संविधान में दिया गया है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In the Second Judges case the Court read 'consultation' with the Chief Justice in Articles 124 and 217 as giving primacy to the judiciary's view, formed by the Chief Justice with senior judges; the Third Judges case (1998) enlarged the collegium to five. The NJAC Act and the 99th Amendment were struck down in the Fourth Judges case as violating judicial independence, part of the basic structure. "
  "Statement 3 is wrong: the Memorandum of Procedure is an executive document agreed between the government and the judiciary; the Constitution itself says nothing about a collegium.",
  "कथन 1 और 2 सही हैं। द्वितीय न्यायाधीश मामले में न्यायालय ने अनुच्छेद 124 और 217 में मुख्य न्यायाधीश से 'परामर्श' को न्यायपालिका के मत की प्रधानता के रूप में पढ़ा, जो मुख्य न्यायाधीश वरिष्ठ न्यायाधीशों के साथ बनाते हैं; तृतीय न्यायाधीश मामले (1998) ने कॉलेजियम को पाँच सदस्यों का किया। NJAC अधिनियम और 99वें संशोधन को चतुर्थ न्यायाधीश मामले में न्यायिक स्वतंत्रता, जो मूल ढाँचे का भाग है, के उल्लंघन के आधार पर रद्द किया गया। "
  "कथन 3 गलत है: प्रक्रिया-ज्ञापन सरकार और न्यायपालिका के बीच सहमत एक कार्यकारी दस्तावेज़ है; संविधान स्वयं कॉलेजियम के बारे में कुछ नहीं कहता।",
  f"{SC} -- Supreme Court Advocates-on-Record Association v. Union of India (1993 and 2015); In re Special Reference No. 1 of 1998; {COI}, Articles 124 and 217.",
  "judiciary-collegium-njac")

S(JU, "medium", "Consider the following statements about the High Courts:",
  "उच्च न्यायालयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A judge of a High Court holds office until the age of 62 years.",
   "Parliament can by law extend the jurisdiction of a High Court to a Union Territory or exclude it from one.",
   "Parliament can by law establish a common High Court for two or more States."],
  ["उच्च न्यायालय का न्यायाधीश 62 वर्ष की आयु तक पद पर रहता है।",
   "संसद कानून द्वारा किसी उच्च न्यायालय के क्षेत्राधिकार को किसी केंद्रशासित प्रदेश तक बढ़ा सकती है या उससे हटा सकती है।",
   "संसद कानून द्वारा दो या अधिक राज्यों के लिए एक साझा उच्च न्यायालय स्थापित कर सकती है।"],
  C3, 2,
  "All three statements are correct (Articles 217, 230 and 231). Supreme Court judges serve until 65, which is why '62' can look wrong. Common High Courts are common in practice -- the Bombay High Court serves Maharashtra, Goa, and Dadra and Nagar Haveli and Daman and Diu, and the Gauhati High Court serves Assam, Nagaland, Mizoram and Arunachal Pradesh.",
  "तीनों कथन सही हैं (अनुच्छेद 217, 230 और 231)। उच्चतम न्यायालय के न्यायाधीश 65 वर्ष तक पद पर रहते हैं, इसीलिए '62' गलत लग सकता है। साझा उच्च न्यायालय व्यवहार में आम हैं: बंबई उच्च न्यायालय महाराष्ट्र, गोवा, और दादरा व नगर हवेली तथा दमन व दीव के लिए है, और गुवाहाटी उच्च न्यायालय असम, नगालैंड, मिज़ोरम और अरुणाचल प्रदेश के लिए।",
  f"{COI}, Articles 217, 230 and 231.",
  "judiciary-high-courts-age-ut-common")

S(JU, "hard", "Consider the following statements about the jurisdiction of the Supreme Court:",
  "उच्चतम न्यायालय के क्षेत्राधिकार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its exclusive original jurisdiction extends to disputes between the Government of India and one or more States.",
   "Its exclusive original jurisdiction also covers disputes in which a private party is ranged against a State.",
   "An opinion given by it on a reference made by the President is not binding on the President.",
   "It may decline to give an opinion on a reference made by the President."],
  ["इसका अनन्य मूल क्षेत्राधिकार भारत सरकार और एक या अधिक राज्यों के बीच विवादों तक फैला है।",
   "इसका अनन्य मूल क्षेत्राधिकार उन विवादों को भी शामिल करता है जिनमें कोई निजी पक्ष किसी राज्य के विरुद्ध हो।",
   "राष्ट्रपति द्वारा किए गए संदर्भ पर इसकी दी गई राय राष्ट्रपति पर बाध्यकारी नहीं है।",
   "यह राष्ट्रपति द्वारा किए गए संदर्भ पर राय देने से इनकार कर सकता है।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct. Article 131 covers disputes between the Union and States, or among States, involving a legal right. The advisory jurisdiction of Article 143 produces an opinion, not a judgment -- and in the Ismail Faruqui case (1994) the Court declined to answer the Ayodhya reference. "
  "Statement 2 is wrong: Article 131 is confined to disputes between governments; a private party's claim against a State goes to the courts in the ordinary way, or to the High Court or Supreme Court under their writ jurisdiction.",
  "कथन 1, 3 और 4 सही हैं। अनुच्छेद 131 संघ और राज्यों के बीच, या राज्यों के आपस में, किसी विधिक अधिकार वाले विवादों को शामिल करता है। अनुच्छेद 143 का सलाहकारी क्षेत्राधिकार राय देता है, निर्णय नहीं; और इस्माइल फ़ारूक़ी मामले (1994) में न्यायालय ने अयोध्या संदर्भ का उत्तर देने से इनकार कर दिया। "
  "कथन 2 गलत है: अनुच्छेद 131 सरकारों के बीच विवादों तक सीमित है; किसी राज्य के विरुद्ध निजी पक्ष का दावा सामान्य रूप से न्यायालयों में, या उच्च न्यायालय अथवा उच्चतम न्यायालय के रिट क्षेत्राधिकार में, जाता है।",
  f"{COI}, Articles 131 and 143; {SC} -- M. Ismail Faruqui v. Union of India (1994).",
  "judiciary-original-advisory-jurisdiction")

M(JU, "medium", "Under which Article can the Supreme Court pass any decree or order necessary for doing complete justice in any cause or matter pending before it?",
  "किस अनुच्छेद के तहत उच्चतम न्यायालय अपने सामने लंबित किसी मामले में पूर्ण न्याय करने के लिए आवश्यक कोई भी डिक्री या आदेश पारित कर सकता है?",
  ["Article 142", "Article 141", "Article 137", "Article 139A"],
  ["अनुच्छेद 142", "अनुच्छेद 141", "अनुच्छेद 137", "अनुच्छेद 139A"],
  0,
  "Article 142 has been used to fill gaps in law -- for example to dissolve marriages that have irretrievably broken down, and in the Chandigarh mayor's election (2024). Article 141 makes the law declared by the Supreme Court binding on all courts, Article 137 is its power of review, and Article 139A lets it transfer cases between High Courts.",
  "अनुच्छेद 142 का उपयोग कानून की कमियाँ भरने के लिए हुआ है, उदाहरण के लिए पूरी तरह टूट चुके विवाहों को भंग करने में और चंडीगढ़ महापौर चुनाव (2024) में। अनुच्छेद 141 उच्चतम न्यायालय द्वारा घोषित विधि को सभी न्यायालयों पर बाध्यकारी बनाता है, अनुच्छेद 137 उसकी पुनर्विलोकन शक्ति है, और अनुच्छेद 139A उसे उच्च न्यायालयों के बीच मामले स्थानांतरित करने देता है।",
  f"{COI}, Articles 137, 139A, 141 and 142.",
  "judiciary-art142-complete-justice")

A(JU, "medium",
  "The Supreme Court is a court of record.",
  "उच्चतम न्यायालय एक अभिलेख न्यायालय (court of record) है।",
  "The law declared by the Supreme Court is binding on all courts within the territory of India.",
  "उच्चतम न्यायालय द्वारा घोषित विधि भारत के राज्यक्षेत्र के भीतर सभी न्यायालयों पर बाध्यकारी है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Being a court of record (Article 129) means its judgments are kept for perpetual memory and cannot be questioned when produced before any court, and that it can punish for contempt of itself. The binding force of its law comes from a different provision, Article 141.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। अभिलेख न्यायालय होने (अनुच्छेद 129) का अर्थ है कि उसके निर्णय स्थायी स्मृति के लिए रखे जाते हैं और किसी न्यायालय के सामने प्रस्तुत होने पर उन पर प्रश्न नहीं उठाया जा सकता, और वह अपनी अवमानना के लिए दंड दे सकता है। उसकी विधि का बाध्यकारी बल एक अलग प्रावधान, अनुच्छेद 141, से आता है।",
  f"{COI}, Articles 129 and 141.",
  "judiciary-court-of-record-129")

# ================================================================ JUDICIAL VERDICTS (10)
S(JV, "medium", "Consider the following statements about Supreme Court judgments on personal and family law:",
  "व्यक्तिगत और पारिवारिक कानून पर उच्चतम न्यायालय के निर्णयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Shayara Bano (2017), the Court held the practice of instant triple talaq unconstitutional.",
   "In Joseph Shine (2018), the Court struck down the offence of adultery.",
   "In Supriyo (2023), the Court recognised a fundamental right of same-sex couples to marry."],
  ["शायरा बानो (2017) में न्यायालय ने तत्काल तीन तलाक की प्रथा को असंवैधानिक माना।",
   "जोसेफ़ शाइन (2018) में न्यायालय ने व्यभिचार (adultery) के अपराध को रद्द कर दिया।",
   "सुप्रियो (2023) में न्यायालय ने समलैंगिक जोड़ों के विवाह के मौलिक अधिकार को मान्यता दी।"],
  C3, 1,
  "Statements 1 and 2 are correct: Shayara Bano was decided 3:2, the majority finding talaq-e-biddat arbitrary, and Joseph Shine struck down Section 497 of the IPC as treating the wife as her husband's property. "
  "Statement 3 is wrong: in Supriyo a five-judge bench unanimously held that there is no fundamental right to marry and left the recognition of same-sex unions to Parliament, while affirming that queer persons must not face discrimination.",
  "कथन 1 और 2 सही हैं: शायरा बानो का निर्णय 3:2 से हुआ, बहुमत ने तलाक-ए-बिद्दत को मनमाना पाया, और जोसेफ़ शाइन ने IPC की धारा 497 को इस आधार पर रद्द किया कि वह पत्नी को पति की संपत्ति मानती थी। "
  "कथन 3 गलत है: सुप्रियो में पाँच न्यायाधीशों की पीठ ने सर्वसम्मति से माना कि विवाह का कोई मौलिक अधिकार नहीं है और समलैंगिक संबंधों की मान्यता संसद पर छोड़ी, साथ ही यह पुष्टि की कि क्वीयर व्यक्तियों के साथ भेदभाव नहीं होना चाहिए।",
  f"{SC} -- Shayara Bano v. Union of India (2017); Joseph Shine v. Union of India (2018); Supriyo @ Supriya Chakraborty v. Union of India (2023).",
  "verdicts-triple-talaq-adultery-marriage")

S(JV, "medium", "Consider the following statements about Supreme Court judgments on policing and criminal procedure:",
  "पुलिस और दांडिक प्रक्रिया पर उच्चतम न्यायालय के निर्णयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In D.K. Basu (1997), the Court laid down guidelines to be followed in every case of arrest and detention.",
   "In Lalita Kumari (2013), the Court held that registration of an FIR is mandatory when the information discloses a cognizable offence.",
   "In Prakash Singh (2006), the Court directed reforms including a minimum fixed tenure for the Director General of Police."],
  ["डी.के. बसु (1997) में न्यायालय ने गिरफ़्तारी और हिरासत के हर मामले में पालन किए जाने वाले दिशानिर्देश दिए।",
   "ललिता कुमारी (2013) में न्यायालय ने माना कि जब सूचना से किसी संज्ञेय अपराध का पता चले, तो FIR दर्ज करना अनिवार्य है।",
   "प्रकाश सिंह (2006) में न्यायालय ने पुलिस महानिदेशक के न्यूनतम निश्चित कार्यकाल सहित सुधारों का निर्देश दिया।"],
  C3, 2,
  "All three statements are correct. D.K. Basu's guidelines -- identification of arresting officers, an arrest memo, informing a relative, medical examination -- grew out of custodial deaths and are now largely written into criminal procedure law. Lalita Kumari allowed only a limited preliminary inquiry in certain categories. Prakash Singh issued seven directions, including State Security Commissions and Police Establishment Boards.",
  "तीनों कथन सही हैं। डी.के. बसु के दिशानिर्देश, जैसे गिरफ़्तार करने वाले अधिकारियों की पहचान, गिरफ़्तारी ज्ञापन, किसी रिश्तेदार को सूचना और चिकित्सा जाँच, हिरासत में मौतों से निकले और अब काफ़ी हद तक दांडिक प्रक्रिया कानून में लिखे गए हैं। ललिता कुमारी ने कुछ श्रेणियों में केवल सीमित प्रारंभिक जाँच की अनुमति दी। प्रकाश सिंह ने सात निर्देश दिए, जिनमें राज्य सुरक्षा आयोग और पुलिस स्थापना बोर्ड शामिल हैं।",
  f"{SC} -- D.K. Basu v. State of West Bengal (1997); Lalita Kumari v. Government of Uttar Pradesh (2013); Prakash Singh v. Union of India (2006).",
  "verdicts-dk-basu-lalita-kumari-prakash-singh")

S(JV, "medium", "Consider the following statements about Supreme Court judgments on the criminalisation of politics:",
  "राजनीति के अपराधीकरण पर उच्चतम न्यायालय के निर्णयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Manoj Narula (2014), the Court held that a person against whom charges have been framed for a serious offence cannot be appointed a minister.",
   "In Public Interest Foundation (2018), the Court required candidates to declare their criminal antecedents and political parties to publicise them.",
   "In Public Interest Foundation, the Court barred persons against whom charges have been framed from contesting elections."],
  ["मनोज नरूला (2014) में न्यायालय ने माना कि जिस व्यक्ति पर गंभीर अपराध के आरोप तय हो चुके हैं, उसे मंत्री नियुक्त नहीं किया जा सकता।",
   "पब्लिक इंटरेस्ट फ़ाउंडेशन (2018) में न्यायालय ने उम्मीदवारों से अपना आपराधिक रिकॉर्ड घोषित करने और राजनीतिक दलों से उसका प्रचार करने की अपेक्षा की।",
   "पब्लिक इंटरेस्ट फ़ाउंडेशन में न्यायालय ने उन व्यक्तियों को चुनाव लड़ने से रोक दिया जिन पर आरोप तय हो चुके हैं।"],
  C3, 0,
  "Only statement 2 is correct: Public Interest Foundation relied on disclosure -- in bold letters in the nomination form and through repeated publicity by the candidate and the party. "
  "Statements 1 and 3 are wrong for the same reason: both judgments stopped short of adding disqualifications that the law does not contain. Manoj Narula only advised that the Prime Minister and Chief Ministers ought not to choose such persons, leaving it to the constitutional trust placed in them, and Public Interest Foundation urged Parliament to legislate rather than barring charge-sheeted candidates itself.",
  "केवल कथन 2 सही है: पब्लिक इंटरेस्ट फ़ाउंडेशन ने प्रकटीकरण पर भरोसा किया, नामांकन-पत्र में मोटे अक्षरों में और उम्मीदवार तथा दल द्वारा बार-बार प्रचार के ज़रिए। "
  "कथन 1 और 3 एक ही कारण से गलत हैं: दोनों निर्णयों ने ऐसी निरर्हताएँ जोड़ने से परहेज़ किया जो कानून में नहीं हैं। मनोज नरूला ने केवल सलाह दी कि प्रधानमंत्री और मुख्यमंत्री ऐसे व्यक्तियों को न चुनें, और इसे उन पर रखे गए संवैधानिक विश्वास पर छोड़ा, और पब्लिक इंटरेस्ट फ़ाउंडेशन ने आरोपित उम्मीदवारों पर स्वयं रोक लगाने के बजाय संसद से कानून बनाने का आग्रह किया।",
  f"{SC} -- Manoj Narula v. Union of India (2014); Public Interest Foundation v. Union of India (2018).",
  "verdicts-criminalisation-of-politics")

S(JV, "hard", "Consider the following statements about the Supreme Court's judgment in Anuradha Bhasin v. Union of India (2020):",
  "अनुराधा भसीन बनाम भारत संघ (2020) में उच्चतम न्यायालय के निर्णय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Court held that the freedom of speech and expression and the freedom to carry on trade over the internet are protected under Article 19.",
   "The Court held that an indefinite suspension of internet services is not permissible.",
   "The Court declared that access to the internet is itself a fundamental right."],
  ["न्यायालय ने माना कि इंटरनेट पर वाक् और अभिव्यक्ति की स्वतंत्रता और व्यापार करने की स्वतंत्रता अनुच्छेद 19 के तहत संरक्षित हैं।",
   "न्यायालय ने माना कि इंटरनेट सेवाओं का अनिश्चितकालीन निलंबन अनुमेय नहीं है।",
   "न्यायालय ने घोषित किया कि इंटरनेट तक पहुँच अपने आप में एक मौलिक अधिकार है।"],
  C3, 1,
  "Statements 1 and 2 are correct: arising from the restrictions in Jammu and Kashmir in 2019, the judgment required suspension orders to be published, to be proportionate and to be periodically reviewed. "
  "Statement 3 is the trap: the Court protected the freedoms exercised through the internet but expressly did not decide whether access to the internet is a fundamental right in itself, since that was not argued before it.",
  "कथन 1 और 2 सही हैं: 2019 में जम्मू-कश्मीर के प्रतिबंधों से उठे इस निर्णय ने अपेक्षा की कि निलंबन आदेश प्रकाशित हों, आनुपातिक हों और समय-समय पर उनकी समीक्षा हो। "
  "कथन 3 जाल है: न्यायालय ने इंटरनेट के ज़रिए प्रयोग की जाने वाली स्वतंत्रताओं की रक्षा की, पर स्पष्ट रूप से यह तय नहीं किया कि इंटरनेट तक पहुँच अपने आप में मौलिक अधिकार है, क्योंकि उसके सामने यह तर्क नहीं रखा गया था।",
  f"{SC} -- Anuradha Bhasin v. Union of India (2020).",
  "verdicts-anuradha-bhasin-internet")

S(JV, "hard", "Consider the following statements about Supreme Court judgments on equality and identity:",
  "समानता और पहचान पर उच्चतम न्यायालय के निर्णयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In NALSA (2014), the Court recognised transgender persons as a 'third gender' entitled to the Fundamental Rights.",
   "In Vineeta Sharma (2020), the Court held that a daughter's coparcenary right depends on her father being alive on 9 September 2005.",
   "In Indian Young Lawyers Association (2018), the Court upheld the restriction on the entry of women aged 10 to 50 into the Sabarimala temple."],
  ["नालसा (2014) में न्यायालय ने ट्रांसजेंडर व्यक्तियों को मौलिक अधिकारों के हक़दार 'तृतीय लिंग' के रूप में मान्यता दी।",
   "विनीता शर्मा (2020) में न्यायालय ने माना कि बेटी का सहदायिक (coparcenary) अधिकार इस पर निर्भर है कि 9 सितंबर 2005 को उसके पिता जीवित थे या नहीं।",
   "इंडियन यंग लॉयर्स एसोसिएशन (2018) में न्यायालय ने सबरीमाला मंदिर में 10 से 50 वर्ष की महिलाओं के प्रवेश पर प्रतिबंध को सही ठहराया।"],
  C3, 0,
  "Only statement 1 is correct: NALSA also directed that transgender persons be treated as a socially and educationally backward class. "
  "Statement 2 reverses Vineeta Sharma: a three-judge bench held that a daughter is a coparcener by birth under the 2005 amendment to the Hindu Succession Act whether or not her father was alive on that date, overruling earlier decisions. "
  "Statement 3 is wrong: in the Sabarimala case the Court struck the exclusion down by 4:1; the review petitions were later tagged with a larger bench's reference on religious practices.",
  "केवल कथन 1 सही है: नालसा ने यह भी निर्देश दिया कि ट्रांसजेंडर व्यक्तियों को सामाजिक और शैक्षिक रूप से पिछड़ा वर्ग माना जाए। "
  "कथन 2 विनीता शर्मा को उलट देता है: तीन न्यायाधीशों की पीठ ने माना कि हिंदू उत्तराधिकार अधिनियम में 2005 के संशोधन के तहत बेटी जन्म से सहदायिक है, चाहे उस तिथि को उसके पिता जीवित रहे हों या नहीं, और पहले के निर्णयों को पलटा। "
  "कथन 3 गलत है: सबरीमाला मामले में न्यायालय ने 4:1 से इस बहिष्कार को रद्द किया; पुनर्विलोकन याचिकाएँ बाद में धार्मिक प्रथाओं पर बड़ी पीठ के संदर्भ के साथ जोड़ दी गईं।",
  f"{SC} -- National Legal Services Authority v. Union of India (2014); Vineeta Sharma v. Rakesh Sharma (2020); Indian Young Lawyers Association v. State of Kerala (2018).",
  "verdicts-nalsa-vineeta-sabarimala")

S(JV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Shah Bano (1985), the Supreme Court held that a divorced Muslim woman could claim maintenance under Section 125 of the Code of Criminal Procedure.",
   "In Sarla Mudgal (1995), the Supreme Court held that a Hindu husband cannot contract a second marriage by converting to Islam without dissolving the first."],
  ["शाह बानो (1985) में उच्चतम न्यायालय ने माना कि तलाक़शुदा मुस्लिम महिला दंड प्रक्रिया संहिता की धारा 125 के तहत भरण-पोषण माँग सकती है।",
   "सरला मुद्गल (1995) में उच्चतम न्यायालय ने माना कि हिंदू पति पहली शादी भंग किए बिना इस्लाम अपनाकर दूसरी शादी नहीं कर सकता।"],
  T2, 2,
  "Both statements are correct. Shah Bano held the secular maintenance provision to apply to all communities, and Parliament's 1986 Act that followed was later read by the Court, in Danial Latifi (2001), to secure a fair provision for divorced women. Sarla Mudgal held such a second marriage void and punishable as bigamy; in both cases the Court also urged a Uniform Civil Code.",
  "दोनों कथन सही हैं। शाह बानो ने माना कि भरण-पोषण का धर्मनिरपेक्ष प्रावधान सभी समुदायों पर लागू होता है, और उसके बाद आए संसद के 1986 के अधिनियम को न्यायालय ने बाद में, डेनियल लतीफ़ी (2001) में, तलाक़शुदा महिलाओं के लिए उचित प्रावधान सुनिश्चित करने वाला पढ़ा। सरला मुद्गल ने ऐसी दूसरी शादी को शून्य और द्विविवाह के रूप में दंडनीय माना; दोनों मामलों में न्यायालय ने समान नागरिक संहिता का आग्रह भी किया।",
  f"{SC} -- Mohd. Ahmed Khan v. Shah Bano Begum (1985); Sarla Mudgal v. Union of India (1995); Danial Latifi v. Union of India (2001).",
  "verdicts-shah-bano-sarla-mudgal-easy")

A(JV, "hard",
  "The demonetisation of ₹500 and ₹1000 notes in 2016 was upheld by the Supreme Court.",
  "2016 में ₹500 और ₹1000 के नोटों के विमुद्रीकरण को उच्चतम न्यायालय ने सही ठहराया।",
  "In Vivek Narayan Sharma (2023), the majority held that the decision-making process under the Reserve Bank of India Act was not flawed.",
  "विवेक नारायण शर्मा (2023) में बहुमत ने माना कि भारतीय रिज़र्व बैंक अधिनियम के तहत निर्णय-प्रक्रिया में कोई दोष नहीं था।",
  2,
  "Only one of Statements II and III is correct -- Statement II -- and it explains Statement I: the majority found that the Centre had consulted the RBI's Central Board under Section 26(2) and that the measure was proportionate to its aims. "
  "Statement III is wrong: the judgment was 4:1. Justice B.V. Nagarathna dissented, holding that so sweeping a measure should have been taken through legislation, not a notification.",
  "कथन II और III में से केवल एक, कथन II, सही है और वह कथन I की व्याख्या करता है: बहुमत ने पाया कि केंद्र ने धारा 26(2) के तहत RBI के केंद्रीय बोर्ड से परामर्श किया था और यह उपाय अपने उद्देश्यों के अनुपात में था। "
  "कथन III गलत है: निर्णय 4:1 से था। न्यायमूर्ति बी.वी. नागरत्ना ने असहमति जताई और माना कि इतना व्यापक उपाय अधिसूचना से नहीं, कानून के ज़रिए किया जाना चाहिए था।",
  f"{SC} -- Vivek Narayan Sharma v. Union of India (2023); Reserve Bank of India Act, 1934, section 26(2).",
  "verdicts-demonetisation-2023",
  s3="The judgment was unanimous.",
  s3_hi="निर्णय सर्वसम्मत था।")

M(JV, "medium", "The 'essential religious practices' test, used by courts to decide which practices are protected by Articles 25 and 26, was first laid down in the:",
  "'अनिवार्य धार्मिक प्रथाओं' की कसौटी, जिसका उपयोग न्यायालय यह तय करने में करते हैं कि कौन-सी प्रथाएँ अनुच्छेद 25 और 26 से संरक्षित हैं, सबसे पहले किस मामले में दी गई?",
  ["Shirur Mutt case (1954)", "Sarla Mudgal case (1995)", "Sabarimala case (2018)", "Ismail Faruqui case (1994)"],
  ["शिरूर मठ मामला (1954)", "सरला मुद्गल मामला (1995)", "सबरीमाला मामला (2018)", "इस्माइल फ़ारूक़ी मामला (1994)"],
  0,
  "In Commissioner, Hindu Religious Endowments v. Shirur Mutt (1954), a seven-judge bench held that 'religion' covers not only beliefs but also practices that are an essential part of the religion, and that what is essential is to be found from the religion's own doctrines. The later cases applied or questioned the test; the Sabarimala review is part of a pending larger-bench reference on it.",
  "कमिश्नर, हिंदू रिलीजियस एंडोमेंट्स बनाम शिरूर मठ (1954) में सात न्यायाधीशों की पीठ ने माना कि 'धर्म' में केवल विश्वास ही नहीं, बल्कि वे प्रथाएँ भी आती हैं जो धर्म का अनिवार्य भाग हैं, और क्या अनिवार्य है यह धर्म के अपने सिद्धांतों से पता लगाया जाना है। बाद के मामलों ने इस कसौटी को लागू किया या उस पर प्रश्न उठाए; सबरीमाला पुनर्विलोकन इस पर लंबित बड़ी पीठ के संदर्भ का भाग है।",
  f"{SC} -- Commissioner, Hindu Religious Endowments, Madras v. Sri Lakshmindra Thirtha Swamiar of Sri Shirur Mutt (1954).",
  "verdicts-shirur-mutt-essential-practices")

A(JV, "medium",
  "In Arnesh Kumar (2014), the Supreme Court directed that the police should not arrest automatically in offences punishable with imprisonment of up to seven years.",
  "अर्नेश कुमार (2014) में उच्चतम न्यायालय ने निर्देश दिया कि सात वर्ष तक के कारावास से दंडनीय अपराधों में पुलिस अपने आप गिरफ़्तारी न करे।",
  "The law of criminal procedure requires a police officer to be satisfied that arrest is necessary, and to record the reasons, before arresting a person for such an offence.",
  "दांडिक प्रक्रिया का कानून अपेक्षा करता है कि ऐसे अपराध के लिए किसी को गिरफ़्तार करने से पहले पुलिस अधिकारी संतुष्ट हो कि गिरफ़्तारी आवश्यक है, और कारण दर्ज करे।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Court's direction, given in a dowry-harassment case, rested on the conditions in Section 41 of the Code of Criminal Procedure (now carried into Section 35 of the Bharatiya Nagarik Suraksha Sanhita): the officer must record why arrest is needed -- to prevent further offences, secure evidence or ensure appearance -- or issue a notice of appearance instead.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। दहेज उत्पीड़न के एक मामले में दिया गया न्यायालय का निर्देश दंड प्रक्रिया संहिता की धारा 41 की शर्तों पर आधारित था (जो अब भारतीय नागरिक सुरक्षा संहिता की धारा 35 में हैं): अधिकारी को दर्ज करना होगा कि गिरफ़्तारी क्यों ज़रूरी है, जैसे आगे अपराध रोकने, साक्ष्य सुरक्षित करने या उपस्थिति सुनिश्चित करने के लिए, अन्यथा उसे उपस्थिति का नोटिस जारी करना होगा।",
  f"{SC} -- Arnesh Kumar v. State of Bihar (2014); Code of Criminal Procedure, 1973, sections 41 and 41A; Bharatiya Nagarik Suraksha Sanhita, 2023, section 35.",
  "verdicts-arnesh-kumar-arrest")

P(JV, "medium", "Consider the following pairs of Supreme Court judgments and what they held:",
  "उच्चतम न्यायालय के निर्णयों और उनमें कही गई बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bilkis Bano (2024) : Quashed the remission granted by the Gujarat government to the convicts",
   "Subhash Desai (2023) : Held that the Governor was justified in calling for a floor test",
   "Kuldeep Kumar (2024) : Used Article 142 to declare the result of the Chandigarh mayoral election",
   "Lok Prahari (2018) : Struck down a law allowing former Chief Ministers to retain government bungalows for life"],
  ["बिलकिस बानो (2024) : गुजरात सरकार द्वारा दोषियों को दी गई सज़ा-माफ़ी को रद्द किया",
   "सुभाष देसाई (2023) : माना कि राज्यपाल का शक्ति-परीक्षण (floor test) बुलाना उचित था",
   "कुलदीप कुमार (2024) : चंडीगढ़ महापौर चुनाव का परिणाम घोषित करने के लिए अनुच्छेद 142 का प्रयोग किया",
   "लोक प्रहरी (2018) : पूर्व मुख्यमंत्रियों को आजीवन सरकारी बंगले रखने देने वाले कानून को रद्द किया"],
  2,
  "Three pairs are correct. In Bilkis Bano the Court held that Maharashtra, where the trial took place, was the appropriate government, so Gujarat's remission was without authority; in Kuldeep Kumar it found the returning officer had defaced ballots and declared the rightful winner; and Lok Prahari held that once out of office, former Chief Ministers are ordinary citizens. "
  "Pair 2 is wrong: in Subhash Desai, on the Maharashtra political crisis, the Constitution Bench held that the Governor had no objective material to doubt the government's majority, so calling a floor test was not justified -- though it could not restore a government that had resigned.",
  "तीन युग्म सही हैं। बिलकिस बानो में न्यायालय ने माना कि जहाँ मुक़दमा चला वह महाराष्ट्र उपयुक्त सरकार था, इसलिए गुजरात की सज़ा-माफ़ी अधिकार-विहीन थी; कुलदीप कुमार में उसने पाया कि निर्वाचन अधिकारी ने मतपत्र विकृत किए थे और वास्तविक विजेता घोषित किया; और लोक प्रहरी ने माना कि पद से हटने के बाद पूर्व मुख्यमंत्री सामान्य नागरिक हैं। "
  "युग्म 2 गलत है: महाराष्ट्र राजनीतिक संकट पर सुभाष देसाई मामले में संविधान पीठ ने माना कि राज्यपाल के पास सरकार के बहुमत पर संदेह करने की कोई वस्तुनिष्ठ सामग्री नहीं थी, इसलिए शक्ति-परीक्षण बुलाना उचित नहीं था; हालाँकि वह त्यागपत्र दे चुकी सरकार को बहाल नहीं कर सकता था।",
  f"{SC} -- Bilkis Yakub Rasool v. Union of India (2024); Subhash Desai v. Principal Secretary, Governor of Maharashtra (2023); Kuldeep Kumar v. U.T. Chandigarh (2024); Lok Prahari v. State of Uttar Pradesh (2018).",
  "verdicts-recent-judgments-pairs")

# ================================================================ ELECTIONS (11)
S(EL, "medium", "Consider the following statements about the Election Commission of India:",
  "भारत निर्वाचन आयोग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It has been a multi-member body ever since 1950.",
   "The Chief Election Commissioner and the other Election Commissioners have equal powers, and differences among them are decided by majority.",
   "An Election Commissioner cannot be removed from office except on the recommendation of the Chief Election Commissioner."],
  ["यह 1950 से ही बहु-सदस्यीय निकाय रहा है।",
   "मुख्य निर्वाचन आयुक्त और अन्य निर्वाचन आयुक्तों की शक्तियाँ बराबर हैं, और उनके बीच मतभेद बहुमत से तय होते हैं।",
   "किसी निर्वाचन आयुक्त को मुख्य निर्वाचन आयुक्त की सिफ़ारिश के बिना पद से नहीं हटाया जा सकता।"],
  C3, 1,
  "Statements 2 and 3 are correct: majority decision-making was provided by law in 1991 and upheld in T.N. Seshan v. Union of India (1995), and the proviso to Article 324(5) gives the other Commissioners this protection. "
  "Statement 1 is wrong: the Commission was a single-member body until October 1989, briefly became multi-member, reverted in 1990, and has had three members continuously only since 1993.",
  "कथन 2 और 3 सही हैं: बहुमत से निर्णय का प्रावधान 1991 में कानून द्वारा किया गया और टी.एन. शेषन बनाम भारत संघ (1995) में सही ठहराया गया, और अनुच्छेद 324(5) का परंतुक अन्य आयुक्तों को यह संरक्षण देता है। "
  "कथन 1 गलत है: आयोग अक्टूबर 1989 तक एक-सदस्यीय निकाय था, कुछ समय के लिए बहु-सदस्यीय बना, 1990 में फिर एक-सदस्यीय हुआ, और 1993 से ही लगातार तीन सदस्यों वाला है।",
  f"{COI}, Article 324(5); Election Commission (Conditions of Service of Election Commissioners and Transaction of Business) Act, 1991; {SC} -- T.N. Seshan v. Union of India (1995).",
  "elections-eci-multimember-majority")

S(EL, "medium", "Consider the following statements about the Model Code of Conduct:",
  "आदर्श आचार संहिता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It does not have statutory backing.",
   "It comes into force as soon as the Election Commission announces the election schedule.",
   "It was first adopted, in a rudimentary form, during the Kerala Assembly elections of 1960."],
  ["इसे वैधानिक समर्थन प्राप्त नहीं है।",
   "यह निर्वाचन आयोग द्वारा चुनाव कार्यक्रम की घोषणा होते ही लागू हो जाती है।",
   "इसे पहली बार, प्रारंभिक रूप में, 1960 के केरल विधानसभा चुनावों के दौरान अपनाया गया।"],
  C3, 2,
  "All three statements are correct. The Code is a consensus document of political parties that the Commission enforces through its powers under Article 324, which is why it has teeth only during elections; some of its conduct rules overlap with offences in the criminal law and the Representation of the People Act. It began as a short set of dos and don'ts in Kerala in 1960 and was extended nationally from 1962.",
  "तीनों कथन सही हैं। संहिता राजनीतिक दलों की सहमति से बना दस्तावेज़ है जिसे आयोग अनुच्छेद 324 के तहत अपनी शक्तियों से लागू करता है, इसीलिए यह केवल चुनावों के दौरान प्रभावी होती है; इसके आचरण के कुछ नियम दांडिक कानून और लोक प्रतिनिधित्व अधिनियम के अपराधों से मेल खाते हैं। यह 1960 में केरल में क्या करें और क्या न करें की एक छोटी सूची के रूप में शुरू हुई और 1962 से राष्ट्रीय स्तर पर लागू हुई।",
  f"{ECI} -- Model Code of Conduct for the Guidance of Political Parties and Candidates; {COI}, Article 324.",
  "elections-model-code-of-conduct")

S(EL, "medium", "Consider the following statements about the Delimitation Commission:",
  "परिसीमन आयोग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its orders have the force of law and cannot be modified by the Lok Sabha or the State Legislative Assembly concerned.",
   "It is chaired by the Chief Election Commissioner.",
   "Delimitation Commissions have been set up four times -- in 1952, 1963, 1973 and 2002."],
  ["इसके आदेशों को कानून का बल होता है और लोकसभा या संबंधित राज्य विधानसभा उनमें संशोधन नहीं कर सकती।",
   "इसकी अध्यक्षता मुख्य निर्वाचन आयुक्त करते हैं।",
   "परिसीमन आयोग चार बार गठित हुए हैं: 1952, 1963, 1973 और 2002 में।"],
  C3, 1,
  "Statements 1 and 3 are correct: the orders are laid before the Lok Sabha and the Assemblies, but they cannot alter them. "
  "Statement 2 is wrong: the Commission is headed by a retired judge of the Supreme Court; the Chief Election Commissioner, or an Election Commissioner he nominates, is an ex officio member, along with the State Election Commissioners concerned.",
  "कथन 1 और 3 सही हैं: आदेश लोकसभा और विधानसभाओं के सामने रखे जाते हैं, पर वे उनमें परिवर्तन नहीं कर सकतीं। "
  "कथन 2 गलत है: आयोग का प्रमुख उच्चतम न्यायालय का सेवानिवृत्त न्यायाधीश होता है; मुख्य निर्वाचन आयुक्त, या उनके द्वारा नामित निर्वाचन आयुक्त, पदेन सदस्य होते हैं, संबंधित राज्य निर्वाचन आयुक्तों के साथ।",
  f"Delimitation Act, 2002, sections 3 and 10; {COI}, Articles 82 and 170.",
  "elections-delimitation-commission")

S(EL, "medium", "Consider the following statements about voting by Indians living abroad:",
  "विदेश में रहने वाले भारतीयों के मतदान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["An Indian citizen living abroad who has not acquired another country's citizenship can be registered as an overseas elector at the address given in the passport.",
   "An Overseas Citizen of India (OCI) cardholder can be registered as an overseas elector.",
   "Every overseas elector can vote by appointing a proxy."],
  ["विदेश में रहने वाला भारतीय नागरिक, जिसने किसी दूसरे देश की नागरिकता नहीं ली है, पासपोर्ट में दिए पते पर प्रवासी निर्वाचक के रूप में पंजीकृत हो सकता है।",
   "भारत की प्रवासी नागरिकता (OCI) कार्डधारक प्रवासी निर्वाचक के रूप में पंजीकृत हो सकता है।",
   "हर प्रवासी निर्वाचक प्रॉक्सी नियुक्त करके मत दे सकता है।"],
  C3, 0,
  "Only statement 1 is correct: section 20A of the Representation of the People Act, 1950, added in 2010, allows this, but the overseas elector must vote in person at the polling station. "
  "Statement 2 is wrong: OCI cardholders are foreign citizens and cannot be electors at all. "
  "Statement 3 is wrong: proxy voting is available only to 'classified service voters', such as members of the armed forces; proposals to extend proxy or postal voting to overseas electors have not become law.",
  "केवल कथन 1 सही है: लोक प्रतिनिधित्व अधिनियम, 1950 की धारा 20A, जो 2010 में जोड़ी गई, इसकी अनुमति देती है, पर प्रवासी निर्वाचक को मतदान केंद्र पर स्वयं जाकर मत देना होता है। "
  "कथन 2 गलत है: OCI कार्डधारक विदेशी नागरिक हैं और निर्वाचक बिल्कुल नहीं हो सकते। "
  "कथन 3 गलत है: प्रॉक्सी मतदान केवल 'वर्गीकृत सेवा मतदाताओं', जैसे सशस्त्र बलों के सदस्यों, को उपलब्ध है; प्रवासी निर्वाचकों तक प्रॉक्सी या डाक मतदान बढ़ाने के प्रस्ताव कानून नहीं बने हैं।",
  f"Representation of the People Act, 1950, section 20A; {RPA}, section 60; Conduct of Election Rules, 1961.",
  "elections-overseas-electors-proxy")

S(EL, "hard", "Consider the following statements about the Voter Verifiable Paper Audit Trail (VVPAT):",
  "मतदाता सत्यापन योग्य पेपर ऑडिट ट्रेल (VVPAT) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was first used in the 2014 Lok Sabha general election.",
   "In Subramanian Swamy (2013), the Supreme Court held that a paper trail is an indispensable requirement of free and fair elections.",
   "In Association for Democratic Reforms v. Election Commission (2024), the Supreme Court directed a return to paper ballots."],
  ["इसका पहली बार प्रयोग 2014 के लोकसभा आम चुनाव में हुआ।",
   "सुब्रमण्यम स्वामी (2013) में उच्चतम न्यायालय ने माना कि पेपर ट्रेल स्वतंत्र और निष्पक्ष चुनावों की अनिवार्य आवश्यकता है।",
   "एसोसिएशन फ़ॉर डेमोक्रेटिक रिफ़ॉर्म्स बनाम निर्वाचन आयोग (2024) में उच्चतम न्यायालय ने मतपत्रों पर लौटने का निर्देश दिया।"],
  C3, 0,
  "Only statement 2 is correct: after the 2013 judgment the Commission introduced VVPATs in phases, and since 2019 every polling station has one, with the slips of five randomly chosen machines per Assembly segment counted. "
  "Statement 1 is wrong: VVPATs were first used in the Noksen Assembly by-election in Nagaland in September 2013; in the 2014 Lok Sabha election they were used in only eight constituencies. "
  "Statement 3 is wrong: in April 2024 the Court rejected the pleas for paper ballots and for counting all VVPAT slips; it only directed that symbol loading units be sealed and stored, and that the burnt memory of machines can be verified at the request of the candidates placed second or third.",
  "केवल कथन 2 सही है: 2013 के निर्णय के बाद आयोग ने चरणों में VVPAT शुरू किए, और 2019 से हर मतदान केंद्र पर एक है, जिसमें हर विधानसभा खंड की यादृच्छिक रूप से चुनी पाँच मशीनों की पर्चियाँ गिनी जाती हैं। "
  "कथन 1 गलत है: VVPAT का पहली बार प्रयोग सितंबर 2013 में नगालैंड के नोकसेन विधानसभा उपचुनाव में हुआ; 2014 के लोकसभा चुनाव में इनका प्रयोग केवल आठ निर्वाचन क्षेत्रों में हुआ। "
  "कथन 3 गलत है: अप्रैल 2024 में न्यायालय ने मतपत्रों और सभी VVPAT पर्चियों की गिनती की माँगें ठुकरा दीं; उसने केवल यह निर्देश दिया कि सिंबल लोडिंग यूनिट सील करके रखी जाएँ, और दूसरे या तीसरे स्थान पर रहे उम्मीदवारों के अनुरोध पर मशीनों की बर्न्ट मेमोरी की जाँच हो सके।",
  f"{SC} -- Subramanian Swamy v. Election Commission of India (2013); Association for Democratic Reforms v. Election Commission of India (2024); {ECI} -- Manual on EVM and VVPAT.",
  "elections-vvpat-judgments")

S(EL, "hard", "Consider the following statements about election expenditure:",
  "चुनाव व्यय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The ceiling on election expenditure applies to political parties as well as to candidates.",
   "A candidate must lodge an account of election expenses within 90 days of the declaration of the result.",
   "Exceeding the prescribed ceiling is only an electoral offence and not a corrupt practice."],
  ["चुनाव व्यय की सीमा उम्मीदवारों के साथ-साथ राजनीतिक दलों पर भी लागू होती है।",
   "उम्मीदवार को परिणाम घोषित होने के 90 दिनों के भीतर चुनाव व्यय का लेखा जमा करना होता है।",
   "निर्धारित सीमा से अधिक व्यय केवल एक चुनावी अपराध है, भ्रष्ट आचरण नहीं।"],
  C3, 3,
  "None of the statements is correct. The ceiling under section 77 applies only to candidates; spending by parties on general propaganda is not capped, which is a long-standing gap in the law. "
  "Under section 78 the account must be lodged within 30 days, and failure can lead to disqualification for three years under section 10A. "
  "Incurring expenditure in contravention of section 77 is listed as a corrupt practice in section 123(6), which can void the election.",
  "कोई भी कथन सही नहीं है। धारा 77 की सीमा केवल उम्मीदवारों पर लागू होती है; सामान्य प्रचार पर दलों के व्यय की कोई सीमा नहीं है, जो कानून की पुरानी कमी है। "
  "धारा 78 के तहत लेखा 30 दिनों के भीतर जमा करना होता है, और ऐसा न करने पर धारा 10A के तहत तीन वर्ष की निरर्हता हो सकती है। "
  "धारा 77 का उल्लंघन करते हुए व्यय करना धारा 123(6) में भ्रष्ट आचरण के रूप में सूचीबद्ध है, जिससे चुनाव शून्य हो सकता है।",
  f"{RPA}, sections 10A, 77, 78 and 123(6).",
  "elections-expenditure-ceiling-account")

M(EL, "hard", "Which one of the following is an electoral offence but NOT a 'corrupt practice' under the Representation of the People Act, 1951?",
  "निम्नलिखित में से कौन-सा लोक प्रतिनिधित्व अधिनियम, 1951 के तहत चुनावी अपराध है, पर 'भ्रष्ट आचरण' नहीं?",
  ["Holding a public meeting within 48 hours of the close of poll", "Bribing voters or candidates",
   "Seeking votes by appealing to the candidate's religion or caste", "Incurring expenditure beyond the prescribed limit"],
  ["मतदान समाप्त होने से पहले के 48 घंटों में सार्वजनिक सभा करना", "मतदाताओं या उम्मीदवारों को रिश्वत देना",
   "उम्मीदवार के धर्म या जाति के आधार पर मत माँगना", "निर्धारित सीमा से अधिक व्यय करना"],
  0,
  "Section 126 bars public meetings and the display of election matter in the 48 hours ending with the close of poll, and punishes a breach, but it is not in the list of corrupt practices in section 123. Bribery, appeals on grounds of religion, race, caste, community or language, and excess expenditure are corrupt practices, which can lead to the election being set aside and to disqualification.",
  "धारा 126 मतदान समाप्त होने तक के 48 घंटों में सार्वजनिक सभाओं और चुनावी सामग्री के प्रदर्शन पर रोक लगाती है और उल्लंघन पर दंड देती है, पर यह धारा 123 की भ्रष्ट आचरणों की सूची में नहीं है। रिश्वत, धर्म, मूलवंश, जाति, समुदाय या भाषा के आधार पर अपील, और अधिक व्यय भ्रष्ट आचरण हैं, जिनसे चुनाव रद्द हो सकता है और निरर्हता हो सकती है।",
  f"{RPA}, sections 123 and 126.",
  "elections-corrupt-practice-vs-offence")

A(EL, "hard",
  "The Election Commission cannot deregister a registered political party for violating the Model Code of Conduct.",
  "निर्वाचन आयोग किसी पंजीकृत राजनीतिक दल का पंजीकरण आदर्श आचार संहिता के उल्लंघन के लिए रद्द नहीं कर सकता।",
  "In Indian National Congress (I) v. Institute of Social Welfare (2002), the Supreme Court held that the Representation of the People Act does not empower the Commission to deregister a party, except in a few situations such as registration obtained by fraud.",
  "इंडियन नेशनल कांग्रेस (आई) बनाम इंस्टीट्यूट ऑफ़ सोशल वेलफ़ेयर (2002) में उच्चतम न्यायालय ने माना कि लोक प्रतिनिधित्व अधिनियम आयोग को किसी दल का पंजीकरण रद्द करने की शक्ति नहीं देता, सिवाय कुछ स्थितियों के, जैसे धोखे से प्राप्त पंजीकरण।",
  1,
  "Both Statements II and III are correct, but only Statement II explains Statement I. Registration under section 29A is a quasi-judicial act, and the Act contains no power to undo it for misconduct, which is why the Commission has repeatedly asked Parliament for that power. "
  "Statement III is true but concerns a different thing: recognition as a national or State party, which brings a reserved symbol, is governed by the Election Symbols Order, 1968, under which the Commission can suspend or withdraw recognition -- that does not end the party's registration.",
  "कथन II और III दोनों सही हैं, पर केवल कथन II कथन I की व्याख्या करता है। धारा 29A के तहत पंजीकरण एक अर्ध-न्यायिक कार्य है, और अधिनियम में कदाचार के लिए उसे पलटने की कोई शक्ति नहीं है; इसीलिए आयोग ने बार-बार संसद से यह शक्ति माँगी है। "
  "कथन III सही है पर एक अलग विषय से संबंधित है: राष्ट्रीय या राज्य दल के रूप में मान्यता, जिससे आरक्षित चिह्न मिलता है, निर्वाचन चिह्न आदेश, 1968 से संचालित है, जिसके तहत आयोग मान्यता निलंबित या वापस ले सकता है; इससे दल का पंजीकरण समाप्त नहीं होता।",
  f"{RPA}, section 29A; Election Symbols (Reservation and Allotment) Order, 1968, paragraph 16A; {SC} -- Indian National Congress (I) v. Institute of Social Welfare (2002).",
  "elections-deregistration-recognition",
  s3="The Commission can suspend or withdraw the recognition of a party under the Election Symbols (Reservation and Allotment) Order, 1968.",
  s3_hi="आयोग निर्वाचन चिह्न (आरक्षण और आवंटन) आदेश, 1968 के तहत किसी दल की मान्यता निलंबित या वापस ले सकता है।")

M(EL, "medium", "Under the Election Symbols (Reservation and Allotment) Order, 1968, one of the ways in which a party can be recognised as a national party is by being recognised as a State party in at least:",
  "निर्वाचन चिह्न (आरक्षण और आवंटन) आदेश, 1968 के तहत कोई दल राष्ट्रीय दल के रूप में जिन तरीकों से मान्यता पा सकता है, उनमें से एक है कम से कम कितने राज्यों में राज्य दल के रूप में मान्यता?",
  ["four States", "three States", "five States", "six States"],
  ["चार राज्यों में", "तीन राज्यों में", "पाँच राज्यों में", "छह राज्यों में"],
  0,
  "Paragraph 6B gives three alternative routes: recognition as a State party in four or more States; or 6 per cent of the valid votes in four or more States at a general election together with four Lok Sabha seats; or 2 per cent of Lok Sabha seats won from at least three States. Parties can lose national status if they fail these tests at review, as several did in 2023.",
  "अनुच्छेद 6B तीन वैकल्पिक मार्ग देता है: चार या अधिक राज्यों में राज्य दल के रूप में मान्यता; या आम चुनाव में चार या अधिक राज्यों में वैध मतों का 6 प्रतिशत और साथ में चार लोकसभा सीटें; या कम से कम तीन राज्यों से लोकसभा की 2 प्रतिशत सीटें जीतना। समीक्षा में इन कसौटियों पर खरे न उतरने पर दल राष्ट्रीय दर्जा खो सकते हैं, जैसा 2023 में कई दलों के साथ हुआ।",
  f"Election Symbols (Reservation and Allotment) Order, 1968, paragraph 6B.",
  "elections-national-party-four-states")

A(EL, "medium",
  "The elections to the offices of the President and the Vice-President are conducted by the Election Commission of India.",
  "राष्ट्रपति और उपराष्ट्रपति के पदों के चुनाव भारत निर्वाचन आयोग कराता है।",
  "The Constitution vests the superintendence, direction and control of elections to Parliament, the State Legislatures and the offices of President and Vice-President in the Election Commission.",
  "संविधान संसद, राज्य विधानमंडलों और राष्ट्रपति तथा उपराष्ट्रपति के पदों के चुनावों का अधीक्षण, निर्देशन और नियंत्रण निर्वाचन आयोग में निहित करता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Because the constitutional mandate covers these two offices, the Commission conducts their elections, appointing the Secretary-General of the Lok Sabha or the Rajya Sabha, by rotation, as the returning officer. Elections to panchayats and municipalities are outside this mandate and are held by the State Election Commissions.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। चूँकि संवैधानिक आदेश इन दोनों पदों को शामिल करता है, इसलिए आयोग उनके चुनाव कराता है और बारी-बारी से लोकसभा या राज्यसभा के महासचिव को निर्वाचन अधिकारी नियुक्त करता है। पंचायतों और नगरपालिकाओं के चुनाव इस आदेश से बाहर हैं और राज्य निर्वाचन आयोग कराते हैं।",
  f"{COI}, Article 324(1); Presidential and Vice-Presidential Elections Act, 1952.",
  "elections-president-vp-eci-mandate")

P(EL, "medium", "Consider the following pairs of electoral reforms and the year in which they were introduced:",
  "चुनाव सुधारों और उनके लागू होने के वर्ष के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Electronic voting machines first used, in a by-election in Kerala : 1982", "Electors' Photo Identity Cards : 1993",
   "'None of the Above' option on voting machines : 2013", "Voting age lowered from 21 to 18 years : 1989"],
  ["इलेक्ट्रॉनिक वोटिंग मशीनों का पहला प्रयोग, केरल के एक उपचुनाव में : 1982", "मतदाता फ़ोटो पहचान पत्र : 1993",
   "वोटिंग मशीनों पर 'उपर्युक्त में से कोई नहीं' विकल्प : 2013", "मतदान की आयु 21 से घटाकर 18 वर्ष : 1989"],
  3,
  "All four pairs are correct. EVMs were first used in some polling stations of the Parur (Paravur) Assembly constituency in 1982; EPICs were introduced in 1993 under T.N. Seshan; NOTA came after the Supreme Court's September 2013 judgment; and the 61st Amendment, passed in 1988, brought the voting age down to 18 from March 1989. "
  "Those who expect one mismatch will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। EVM का पहला प्रयोग 1982 में पारूर (परवूर) विधानसभा क्षेत्र के कुछ मतदान केंद्रों में हुआ; EPIC 1993 में टी.एन. शेषन के समय शुरू हुए; NOTA सितंबर 2013 के उच्चतम न्यायालय के निर्णय के बाद आया; और 1988 में पारित 61वें संशोधन ने मार्च 1989 से मतदान की आयु 18 वर्ष की। "
  "जो एक बेमेल की अपेक्षा करते हैं, वे 'केवल तीन युग्म' के जाल में फँसेंगे।",
  f"{ECI} -- History of electoral reforms; Constitution (Sixty-first Amendment) Act, 1988.",
  "elections-reforms-years-pairs")

# ================================================================ BODIES (18)
S(BO, "medium", "Consider the following statements about the National Human Rights Commission (NHRC):",
  "राष्ट्रीय मानवाधिकार आयोग (NHRC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a statutory body set up under the Protection of Human Rights Act, 1993.",
   "Its Chairperson must be a person who has been the Chief Justice of India or a judge of the Supreme Court.",
   "It cannot inquire into a matter after the expiry of one year from the date on which the alleged violation was committed."],
  ["यह मानवाधिकार संरक्षण अधिनियम, 1993 के तहत बना एक वैधानिक निकाय है।",
   "इसका अध्यक्ष ऐसा व्यक्ति होना चाहिए जो भारत का मुख्य न्यायाधीश या उच्चतम न्यायालय का न्यायाधीश रहा हो।",
   "यह कथित उल्लंघन की तिथि से एक वर्ष बीत जाने के बाद किसी मामले की जाँच नहीं कर सकता।"],
  C3, 2,
  "All three statements are correct. The 2019 amendment widened eligibility for Chairperson from former Chief Justices alone to former judges of the Supreme Court as well, and cut the term to three years. The one-year limit in section 36(2) is one reason critics call the Commission's reach limited; it also cannot take up matters pending before another commission set up by law.",
  "तीनों कथन सही हैं। 2019 के संशोधन ने अध्यक्ष की पात्रता को केवल पूर्व मुख्य न्यायाधीशों से बढ़ाकर उच्चतम न्यायालय के पूर्व न्यायाधीशों तक किया, और कार्यकाल घटाकर तीन वर्ष किया। धारा 36(2) की एक वर्ष की सीमा उन कारणों में है जिनसे आलोचक आयोग की पहुँच को सीमित बताते हैं; वह किसी दूसरे विधिक आयोग के सामने लंबित मामलों को भी नहीं ले सकता।",
  "Protection of Human Rights Act, 1993, sections 3 and 36 (as amended in 2019).",
  "bodies-nhrc-status-chair-limitation")

S(BO, "medium", "Consider the following statements about the Central Vigilance Commission (CVC):",
  "केंद्रीय सतर्कता आयोग (CVC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a constitutional body.",
   "The Central Vigilance Commissioner can be removed by the President on the ground of proved misbehaviour or incapacity after an inquiry by the Supreme Court.",
   "It presents its annual report directly to the Lok Sabha."],
  ["यह एक संवैधानिक निकाय है।",
   "केंद्रीय सतर्कता आयुक्त को उच्चतम न्यायालय की जाँच के बाद सिद्ध कदाचार या अक्षमता के आधार पर राष्ट्रपति हटा सकते हैं।",
   "यह अपनी वार्षिक रिपोर्ट सीधे लोकसभा को प्रस्तुत करता है।"],
  C3, 0,
  "Only statement 2 is correct (section 6 of the CVC Act, 2003), which gives the Commission a security of tenure similar to that of constitutional authorities. "
  "Statement 1 is wrong: the CVC was set up by an executive resolution in 1964 and given statutory status in 2003, after the Vineet Narain judgment (1997). "
  "Statement 3 is wrong: it presents its annual report to the President, who causes it to be laid before each House of Parliament.",
  "केवल कथन 2 सही है (CVC अधिनियम, 2003 की धारा 6), जो आयोग को संवैधानिक प्राधिकरणों जैसी पद-सुरक्षा देता है। "
  "कथन 1 गलत है: CVC 1964 में एक कार्यकारी संकल्प से बना और 1997 के विनीत नारायण निर्णय के बाद 2003 में उसे वैधानिक दर्जा मिला। "
  "कथन 3 गलत है: यह अपनी वार्षिक रिपोर्ट राष्ट्रपति को देता है, जो उसे संसद के प्रत्येक सदन के सामने रखवाते हैं।",
  f"Central Vigilance Commission Act, 2003, sections 6 and 14; {SC} -- Vineet Narain v. Union of India (1997).",
  "bodies-cvc-status-removal-report")

S(BO, "medium", "Consider the following statements about the Lokpal:",
  "लोकपाल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was established under the Lokpal and Lokayuktas Act, 2013.",
   "At least half of its members must be judicial members.",
   "The Prime Minister is wholly outside its jurisdiction."],
  ["इसकी स्थापना लोकपाल और लोकायुक्त अधिनियम, 2013 के तहत हुई।",
   "इसके कम से कम आधे सदस्य न्यायिक सदस्य होने चाहिए।",
   "प्रधानमंत्री पूरी तरह इसके क्षेत्राधिकार से बाहर हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Lokpal has a Chairperson and up to eight members, half of them judicial, and half of the members must come from the Scheduled Castes, Scheduled Tribes, OBCs, minorities and women. "
  "Statement 3 is wrong: the Prime Minister is covered, with safeguards -- allegations relating to international relations, external and internal security, public order, atomic energy and space are excluded, and any inquiry needs the approval of the full bench by a two-thirds majority, held in camera.",
  "कथन 1 और 2 सही हैं: लोकपाल में एक अध्यक्ष और अधिकतम आठ सदस्य होते हैं, जिनमें आधे न्यायिक होते हैं, और आधे सदस्य अनुसूचित जातियों, अनुसूचित जनजातियों, OBC, अल्पसंख्यकों और महिलाओं से होने चाहिए। "
  "कथन 3 गलत है: प्रधानमंत्री सुरक्षा उपायों के साथ शामिल हैं: अंतरराष्ट्रीय संबंधों, बाहरी और आंतरिक सुरक्षा, लोक व्यवस्था, परमाणु ऊर्जा और अंतरिक्ष से संबंधित आरोप बाहर हैं, और किसी भी जाँच के लिए पूर्ण पीठ का दो-तिहाई बहुमत से अनुमोदन चाहिए, जो बंद कमरे में होती है।",
  "Lokpal and Lokayuktas Act, 2013, sections 3 and 14.",
  "bodies-lokpal-structure-pm")

S(BO, "medium", "Consider the following statements about a Joint State Public Service Commission (JSPSC):",
  "संयुक्त राज्य लोक सेवा आयोग (JSPSC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It can be created by an order of the President at the request of the Governors of the States concerned.",
   "Like the UPSC, it is a constitutional body.",
   "Its members are appointed by the Governor of the largest State among those it serves."],
  ["इसे संबंधित राज्यों के राज्यपालों के अनुरोध पर राष्ट्रपति के आदेश द्वारा बनाया जा सकता है।",
   "UPSC की तरह यह भी एक संवैधानिक निकाय है।",
   "इसके सदस्य उन राज्यों में से सबसे बड़े राज्य के राज्यपाल द्वारा नियुक्त होते हैं जिनकी यह सेवा करता है।"],
  C3, 3,
  "None of the statements is correct. Article 315(2) provides for a JSPSC, but it comes into being only through a law of Parliament after the Legislature of each State concerned passes a resolution -- so it is a statutory, not a constitutional, body; the only such body existed briefly for Punjab and Haryana after Haryana was created in 1966. "
  "Statement 3 is wrong: the Chairman and members of a JSPSC are appointed by the President, and they submit their reports to each of the Governors concerned.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 315(2) JSPSC का प्रावधान करता है, पर वह संबंधित हर राज्य के विधानमंडल के संकल्प के बाद संसद के कानून से ही अस्तित्व में आता है, इसलिए यह वैधानिक निकाय है, संवैधानिक नहीं; ऐसा एकमात्र निकाय 1966 में हरियाणा बनने के बाद कुछ समय के लिए पंजाब और हरियाणा के लिए रहा। "
  "कथन 3 गलत है: JSPSC के अध्यक्ष और सदस्य राष्ट्रपति द्वारा नियुक्त होते हैं, और वे अपनी रिपोर्ट संबंधित प्रत्येक राज्यपाल को देते हैं।",
  f"{COI}, Articles 315-323.",
  "bodies-joint-state-psc")

S(BO, "medium", "Consider the following statements about the Law Commission of India:",
  "भारत के विधि आयोग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a non-statutory body constituted by an order of the Government of India.",
   "The first Law Commission after independence was set up in 1955 under M.C. Setalvad.",
   "The 21st Law Commission said in 2018 that a Uniform Civil Code was neither necessary nor desirable at that stage."],
  ["यह भारत सरकार के आदेश से गठित एक गैर-वैधानिक निकाय है।",
   "स्वतंत्रता के बाद पहला विधि आयोग 1955 में एम.सी. सीतलवाड़ की अध्यक्षता में बना।",
   "21वें विधि आयोग ने 2018 में कहा कि उस चरण में समान नागरिक संहिता न आवश्यक थी, न वांछनीय।"],
  C3, 2,
  "All three statements are correct. The Commission is reconstituted for a fixed term, usually three years, and works on references from the Law Ministry or the Supreme Court, or on its own. Its 2018 consultation paper on family law preferred reforming each personal law; the 22nd Law Commission reopened the consultation on a Uniform Civil Code in 2023.",
  "तीनों कथन सही हैं। आयोग एक निश्चित कार्यकाल के लिए, प्रायः तीन वर्ष, फिर से गठित होता है, और विधि मंत्रालय या उच्चतम न्यायालय के संदर्भों पर, या स्वयं, काम करता है। पारिवारिक कानून पर उसके 2018 के परामर्श-पत्र ने हर व्यक्तिगत कानून में सुधार को प्राथमिकता दी; 22वें विधि आयोग ने 2023 में समान नागरिक संहिता पर परामर्श फिर से खोला।",
  "Ministry of Law and Justice -- Law Commission of India; Law Commission of India, Consultation Paper on Reform of Family Law (2018).",
  "bodies-law-commission")

S(BO, "medium", "Consider the following statements about the Advocate General of a State:",
  "किसी राज्य के महाधिवक्ता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Advocate General is appointed by the Governor.",
   "The Advocate General must be qualified to be appointed a judge of the Supreme Court.",
   "The Advocate General holds office for a fixed term of five years."],
  ["महाधिवक्ता की नियुक्ति राज्यपाल करते हैं।",
   "महाधिवक्ता में उच्चतम न्यायालय का न्यायाधीश नियुक्त होने की योग्यता होनी चाहिए।",
   "महाधिवक्ता पाँच वर्ष के निश्चित कार्यकाल के लिए पद पर रहते हैं।"],
  C3, 0,
  "Only statement 1 is correct (Article 165). "
  "Statement 2 is wrong: the Advocate General must be qualified to be a judge of a High Court -- the Attorney General is the one who must be qualified for the Supreme Court. "
  "Statement 3 is wrong: the Constitution fixes no term; the Advocate General holds office during the pleasure of the Governor and, by convention, resigns when the government changes.",
  "केवल कथन 1 सही है (अनुच्छेद 165)। "
  "कथन 2 गलत है: महाधिवक्ता में उच्च न्यायालय का न्यायाधीश बनने की योग्यता होनी चाहिए; उच्चतम न्यायालय की योग्यता महान्यायवादी के लिए है। "
  "कथन 3 गलत है: संविधान कोई कार्यकाल तय नहीं करता; महाधिवक्ता राज्यपाल के प्रसादपर्यंत पद पर रहते हैं और परिपाटी के अनुसार सरकार बदलने पर त्यागपत्र दे देते हैं।",
  f"{COI}, Articles 76 and 165.",
  "bodies-advocate-general")

S(BO, "hard", "Consider the following statements about the Special Officer for Linguistic Minorities:",
  "भाषाई अल्पसंख्यकों के लिए विशेष अधिकारी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The office was created by the Seventh Amendment Act, 1956.",
   "The Special Officer is appointed by the Minister of Minority Affairs.",
   "The Special Officer's reports are laid before each House of Parliament and sent to the State governments concerned."],
  ["यह पद सातवें संशोधन अधिनियम, 1956 द्वारा बनाया गया।",
   "विशेष अधिकारी की नियुक्ति अल्पसंख्यक कार्य मंत्री करते हैं।",
   "विशेष अधिकारी की रिपोर्टें संसद के प्रत्येक सदन के सामने रखी जाती हैं और संबंधित राज्य सरकारों को भेजी जाती हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct: the office, a result of the States Reorganisation Commission's concern for minorities left in linguistic States, investigates the working of the safeguards for linguistic minorities and reports to the President, who has the reports laid before Parliament and sent to the States. "
  "Statement 2 is wrong: the Special Officer, known as the Commissioner for Linguistic Minorities, is appointed by the President; the Ministry of Minority Affairs is only the administrative ministry.",
  "कथन 1 और 3 सही हैं: राज्य पुनर्गठन आयोग की भाषाई राज्यों में रह गए अल्पसंख्यकों के प्रति चिंता से बना यह पद भाषाई अल्पसंख्यकों के सुरक्षा उपायों के कामकाज की जाँच करता है और राष्ट्रपति को रिपोर्ट देता है, जो रिपोर्टें संसद के सामने रखवाते हैं और राज्यों को भेजते हैं। "
  "कथन 2 गलत है: विशेष अधिकारी, जिसे भाषाई अल्पसंख्यक आयुक्त कहा जाता है, राष्ट्रपति द्वारा नियुक्त होता है; अल्पसंख्यक कार्य मंत्रालय केवल प्रशासनिक मंत्रालय है।",
  f"{COI}, Part XVII; Constitution (Seventh Amendment) Act, 1956; Ministry of Minority Affairs -- Commissioner for Linguistic Minorities.",
  "bodies-special-officer-linguistic-minorities")

S(BO, "hard", "Consider the following statements about the Central Bureau of Investigation (CBI):",
  "केंद्रीय अन्वेषण ब्यूरो (CBI) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was set up by a resolution of the Ministry of Home Affairs in 1963.",
   "It derives its legal powers of investigation from the Delhi Special Police Establishment Act, 1946.",
   "It can investigate an offence in any State without that State's consent.",
   "Its Director is appointed on the recommendation of a committee of the Prime Minister, the Leader of the Opposition in the Lok Sabha and the Chief Justice of India."],
  ["इसे 1963 में गृह मंत्रालय के एक संकल्प से स्थापित किया गया।",
   "यह जाँच की अपनी विधिक शक्तियाँ दिल्ली विशेष पुलिस स्थापना अधिनियम, 1946 से प्राप्त करता है।",
   "यह किसी भी राज्य में उस राज्य की सहमति के बिना किसी अपराध की जाँच कर सकता है।",
   "इसके निदेशक की नियुक्ति प्रधानमंत्री, लोकसभा में विपक्ष के नेता और भारत के मुख्य न्यायाधीश की समिति की सिफ़ारिश पर होती है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. "
  "Statement 3 is wrong: under section 6 of the DSPE Act, the CBI needs the consent of the State government to investigate in that State, whether general or case-specific, unless a constitutional court orders the investigation. Several States have withdrawn general consent in recent years, which is why the question often reaches the Supreme Court under Article 131.",
  "कथन 1, 2 और 4 सही हैं। "
  "कथन 3 गलत है: DSPE अधिनियम की धारा 6 के तहत CBI को किसी राज्य में जाँच के लिए उस राज्य सरकार की सहमति चाहिए, सामान्य या मामला-विशेष, जब तक कोई संवैधानिक न्यायालय जाँच का आदेश न दे। हाल के वर्षों में कई राज्यों ने सामान्य सहमति वापस ली है, इसीलिए यह प्रश्न अक्सर अनुच्छेद 131 के तहत उच्चतम न्यायालय पहुँचता है।",
  "Delhi Special Police Establishment Act, 1946, sections 4A and 6; Ministry of Home Affairs Resolution No. 4/31/61-T (1963).",
  "bodies-cbi-origin-consent-director")

S(BO, "hard", "Consider the following statements about tribunals under the Constitution:",
  "संविधान के तहत अधिकरणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Articles 323A and 323B were inserted by the 42nd Amendment Act, 1976.",
   "Administrative tribunals under Article 323A can be set up by State Legislatures.",
   "Tribunals under Article 323B can be set up by Parliament as well as by the State Legislatures, on the matters within their legislative competence.",
   "In L. Chandra Kumar (1997), the Supreme Court held that decisions of tribunals are final and cannot be questioned before the High Courts."],
  ["अनुच्छेद 323A और 323B, 42वें संशोधन अधिनियम, 1976 द्वारा जोड़े गए।",
   "अनुच्छेद 323A के तहत प्रशासनिक अधिकरण राज्य विधानमंडल स्थापित कर सकते हैं।",
   "अनुच्छेद 323B के तहत अधिकरण संसद और राज्य विधानमंडल, दोनों अपनी विधायी क्षमता के विषयों पर स्थापित कर सकते हैं।",
   "एल. चंद्र कुमार (1997) में उच्चतम न्यायालय ने माना कि अधिकरणों के निर्णय अंतिम हैं और उन पर उच्च न्यायालयों में प्रश्न नहीं उठाया जा सकता।"],
  C4, 1,
  "Statements 1 and 3 are correct. "
  "Statement 2 is wrong: only Parliament can set up administrative tribunals under Article 323A, for service matters -- it did so through the Administrative Tribunals Act, 1985, under which State Administrative Tribunals are also created by the Centre at a State's request. "
  "Statement 4 reverses L. Chandra Kumar: a seven-judge bench held the power of judicial review of the High Courts and the Supreme Court to be part of the basic structure, so tribunal decisions are subject to scrutiny by a division bench of the High Court.",
  "कथन 1 और 3 सही हैं। "
  "कथन 2 गलत है: अनुच्छेद 323A के तहत सेवा मामलों के लिए प्रशासनिक अधिकरण केवल संसद स्थापित कर सकती है; उसने ऐसा प्रशासनिक अधिकरण अधिनियम, 1985 से किया, जिसके तहत राज्य प्रशासनिक अधिकरण भी किसी राज्य के अनुरोध पर केंद्र बनाता है। "
  "कथन 4 एल. चंद्र कुमार को उलट देता है: सात न्यायाधीशों की पीठ ने उच्च न्यायालयों और उच्चतम न्यायालय की न्यायिक समीक्षा की शक्ति को मूल ढाँचे का भाग माना, इसलिए अधिकरणों के निर्णय उच्च न्यायालय की खंडपीठ की जाँच के अधीन हैं।",
  f"{COI}, Articles 323A and 323B; Administrative Tribunals Act, 1985; {SC} -- L. Chandra Kumar v. Union of India (1997).",
  "bodies-tribunals-323a-323b")

M(BO, "medium", "Which one of the following is a constitutional body?",
  "निम्नलिखित में से कौन-सा एक संवैधानिक निकाय है?",
  ["National Commission for Scheduled Tribes", "National Commission for Protection of Child Rights",
   "National Green Tribunal", "Central Information Commission"],
  ["राष्ट्रीय अनुसूचित जनजाति आयोग", "राष्ट्रीय बाल अधिकार संरक्षण आयोग",
   "राष्ट्रीय हरित अधिकरण", "केंद्रीय सूचना आयोग"],
  0,
  "The National Commission for Scheduled Tribes is established by Article 338A. The others were created by Acts of Parliament: the NCPCR by the Commissions for Protection of Child Rights Act, 2005, the NGT by the National Green Tribunal Act, 2010, and the CIC by the Right to Information Act, 2005 -- which is why their powers and tenure can be changed by ordinary legislation.",
  "राष्ट्रीय अनुसूचित जनजाति आयोग अनुच्छेद 338A द्वारा स्थापित है। बाकी संसद के अधिनियमों से बने: NCPCR बाल अधिकार संरक्षण आयोग अधिनियम, 2005 से, NGT राष्ट्रीय हरित अधिकरण अधिनियम, 2010 से, और CIC सूचना का अधिकार अधिनियम, 2005 से; इसीलिए उनकी शक्तियाँ और कार्यकाल सामान्य कानून से बदले जा सकते हैं।",
  f"{COI}, Article 338A; Commissions for Protection of Child Rights Act, 2005; National Green Tribunal Act, 2010; Right to Information Act, 2005.",
  "bodies-constitutional-ncst")

M(BO, "medium", "The Chairman and members of the Union Public Service Commission hold office for six years or until they attain the age of:",
  "संघ लोक सेवा आयोग के अध्यक्ष और सदस्य छह वर्ष तक या कितनी आयु प्राप्त करने तक पद पर रहते हैं?",
  ["65 years", "62 years", "60 years", "70 years"],
  ["65 वर्ष", "62 वर्ष", "60 वर्ष", "70 वर्ष"],
  0,
  "Under Article 316(2), UPSC members serve for six years or until 65, whichever is earlier; members of a State Public Service Commission retire at 62. The difference mirrors that between Supreme Court and High Court judges, which is why 62 is the natural trap.",
  "अनुच्छेद 316(2) के तहत UPSC के सदस्य छह वर्ष या 65 वर्ष की आयु तक, जो पहले हो, पद पर रहते हैं; राज्य लोक सेवा आयोग के सदस्य 62 वर्ष पर सेवानिवृत्त होते हैं। यह अंतर उच्चतम न्यायालय और उच्च न्यायालय के न्यायाधीशों के अंतर जैसा है, इसीलिए 62 स्वाभाविक जाल है।",
  f"{COI}, Article 316(2).",
  "bodies-upsc-tenure-age")

M(BO, "hard", "The Central Vigilance Commission was set up in 1964 on the recommendation of the:",
  "केंद्रीय सतर्कता आयोग 1964 में किसकी सिफ़ारिश पर स्थापित किया गया?",
  ["K. Santhanam Committee", "First Administrative Reforms Commission", "A.D. Gorwala Committee", "Paul Appleby Committee"],
  ["के. संथानम समिति", "प्रथम प्रशासनिक सुधार आयोग", "ए.डी. गोरवाला समिति", "पॉल एपलबी समिति"],
  0,
  "The Committee on Prevention of Corruption (1962-64) under K. Santhanam recommended the CVC as the apex vigilance institution. The First Administrative Reforms Commission (1966) is the tempting option because it recommended the Lokpal and Lokayuktas; Gorwala (1951) and Appleby (1953) reported on public administration generally.",
  "के. संथानम की अध्यक्षता वाली भ्रष्टाचार निवारण समिति (1962-64) ने CVC को शीर्ष सतर्कता संस्था के रूप में सुझाया। प्रथम प्रशासनिक सुधार आयोग (1966) आकर्षक विकल्प है, क्योंकि उसने लोकपाल और लोकायुक्तों की सिफ़ारिश की; गोरवाला (1951) और एपलबी (1953) ने सामान्य रूप से लोक प्रशासन पर रिपोर्ट दी।",
  "Report of the Committee on Prevention of Corruption (1964); Central Vigilance Commission -- History.",
  "bodies-cvc-santhanam")

M(BO, "hard", "Under the Lokpal and Lokayuktas Act, 2013, which one of the following is NOT a member of the Selection Committee for the Chairperson and members of the Lokpal?",
  "लोकपाल और लोकायुक्त अधिनियम, 2013 के तहत निम्नलिखित में से कौन लोकपाल के अध्यक्ष और सदस्यों की चयन समिति का सदस्य नहीं है?",
  ["The Chairman of the Rajya Sabha", "The Speaker of the Lok Sabha", "The Leader of the Opposition in the Lok Sabha", "The Chief Justice of India"],
  ["राज्यसभा के सभापति", "लोकसभा के अध्यक्ष", "लोकसभा में विपक्ष के नेता", "भारत के मुख्य न्यायाधीश"],
  0,
  "Section 4 constitutes the Selection Committee of the Prime Minister, the Speaker of the Lok Sabha, the Leader of the Opposition in the Lok Sabha (or leader of the single largest opposition party), the Chief Justice of India or a judge nominated by him, and an eminent jurist nominated by the President on the others' recommendation. The Chairman of the Rajya Sabha has no role, although the Speaker does.",
  "धारा 4 चयन समिति में प्रधानमंत्री, लोकसभा अध्यक्ष, लोकसभा में विपक्ष के नेता (या सबसे बड़े विपक्षी दल के नेता), भारत के मुख्य न्यायाधीश या उनके द्वारा नामित न्यायाधीश, और बाकी सदस्यों की सिफ़ारिश पर राष्ट्रपति द्वारा नामित एक प्रतिष्ठित विधिवेत्ता को रखती है। राज्यसभा के सभापति की कोई भूमिका नहीं है, जबकि लोकसभा अध्यक्ष की है।",
  "Lokpal and Lokayuktas Act, 2013, section 4.",
  "bodies-lokpal-selection-committee")

A(BO, "medium",
  "The recommendations of the Law Commission of India are not binding on the Government.",
  "भारत के विधि आयोग की सिफ़ारिशें सरकार पर बाध्यकारी नहीं हैं।",
  "The Law Commission is reconstituted every few years, usually for a term of three years.",
  "विधि आयोग हर कुछ वर्षों में, प्रायः तीन वर्ष के कार्यकाल के लिए, फिर से गठित होता है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The recommendations are not binding because the Commission is an advisory body created by an executive order, with no statutory or constitutional power over the government; how long each Commission lasts has nothing to do with that. Many of its reports -- on the Evidence Act, criminal procedure and electoral reform -- have nonetheless shaped legislation.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। सिफ़ारिशें इसलिए बाध्यकारी नहीं हैं कि आयोग एक कार्यकारी आदेश से बना सलाहकारी निकाय है, जिसके पास सरकार पर कोई वैधानिक या संवैधानिक शक्ति नहीं है; हर आयोग कितने समय तक रहता है, इससे इसका कोई संबंध नहीं है। फिर भी साक्ष्य अधिनियम, दांडिक प्रक्रिया और चुनाव सुधार पर उसकी कई रिपोर्टों ने कानूनों को आकार दिया है।",
  "Ministry of Law and Justice -- Law Commission of India.",
  "bodies-law-commission-nonbinding")

A(BO, "hard",
  "The National Human Rights Commission cannot itself punish those responsible for a violation of human rights.",
  "राष्ट्रीय मानवाधिकार आयोग मानवाधिकार उल्लंघन के ज़िम्मेदार लोगों को स्वयं दंडित नहीं कर सकता।",
  "The Commission's functions are recommendatory; after an inquiry it can recommend prosecution, compensation or other action to the government concerned.",
  "आयोग के कार्य सिफ़ारिशी हैं; जाँच के बाद वह संबंधित सरकार को अभियोजन, मुआवज़ा या अन्य कार्रवाई की सिफ़ारिश कर सकता है।",
  1,
  "Both Statements II and III are correct, but only Statement II explains Statement I. The Commission cannot punish because the Act makes its role recommendatory: it can recommend and, if needed, approach the Supreme Court or a High Court. "
  "Statement III is true but concerns how it gathers evidence during an inquiry -- summoning witnesses and requisitioning records like a civil court -- which does not give it any power to punish.",
  "कथन II और III दोनों सही हैं, पर केवल कथन II कथन I की व्याख्या करता है। आयोग दंड नहीं दे सकता क्योंकि अधिनियम उसकी भूमिका सिफ़ारिशी बनाता है: वह सिफ़ारिश कर सकता है और ज़रूरत पड़ने पर उच्चतम न्यायालय या उच्च न्यायालय जा सकता है। "
  "कथन III सही है पर इस बारे में है कि वह जाँच के दौरान साक्ष्य कैसे जुटाता है, यानी सिविल न्यायालय की तरह गवाहों को बुलाना और रिकॉर्ड मँगाना; इससे उसे दंड देने की कोई शक्ति नहीं मिलती।",
  "Protection of Human Rights Act, 1993, sections 13 and 18.",
  "bodies-nhrc-recommendatory",
  s3="While inquiring into complaints, the Commission has the powers of a civil court trying a suit.",
  s3_hi="शिकायतों की जाँच करते समय आयोग के पास वाद की सुनवाई करने वाले सिविल न्यायालय की शक्तियाँ होती हैं।")

S(BO, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Staff Selection Commission is a constitutional body.",
   "NITI Aayog replaced the Planning Commission."],
  ["कर्मचारी चयन आयोग एक संवैधानिक निकाय है।",
   "नीति आयोग ने योजना आयोग का स्थान लिया।"],
  T2, 1,
  "Only statement 2 is correct: NITI Aayog was set up on 1 January 2015 by a Cabinet resolution in place of the Planning Commission of 1950. Statement 1 is wrong: the Staff Selection Commission is an attached office of the Department of Personnel and Training, created by executive resolution; only the UPSC and the State Public Service Commissions are constitutional recruiting bodies.",
  "केवल कथन 2 सही है: नीति आयोग 1 जनवरी 2015 को एक मंत्रिमंडलीय संकल्प द्वारा 1950 के योजना आयोग के स्थान पर बना। कथन 1 गलत है: कर्मचारी चयन आयोग कार्मिक और प्रशिक्षण विभाग का एक संबद्ध कार्यालय है, जो कार्यकारी संकल्प से बना; केवल UPSC और राज्य लोक सेवा आयोग संवैधानिक भर्ती निकाय हैं।",
  f"Department of Personnel and Training -- Staff Selection Commission; NITI Aayog -- Cabinet Resolution (2015); {COI}, Article 315.",
  "bodies-ssc-niti-easy")

P(BO, "medium", "Consider the following pairs of offices or bodies and the Articles of the Constitution that provide for them:",
  "पदों या निकायों और उनका प्रावधान करने वाले संविधान के अनुच्छेदों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Union Public Service Commission : Article 315", "Advocate General of a State : Article 165",
   "Comptroller and Auditor-General of India : Article 148", "Special Officer for Linguistic Minorities : Article 350A"],
  ["संघ लोक सेवा आयोग : अनुच्छेद 315", "राज्य का महाधिवक्ता : अनुच्छेद 165",
   "भारत के नियंत्रक-महालेखापरीक्षक : अनुच्छेद 148", "भाषाई अल्पसंख्यकों के लिए विशेष अधिकारी : अनुच्छेद 350A"],
  2,
  "Three pairs are correct. Pair 4 is wrong by one letter: the Special Officer is in Article 350B; Article 350A is the directive on instruction in the mother tongue at the primary stage, which the Special Officer is meant to watch over.",
  "तीन युग्म सही हैं। युग्म 4 एक अक्षर से गलत है: विशेष अधिकारी अनुच्छेद 350B में है; अनुच्छेद 350A प्राथमिक स्तर पर मातृभाषा में शिक्षा का निदेश है, जिस पर नज़र रखना विशेष अधिकारी का काम है।",
  f"{COI}, Articles 148, 165, 315, 350A and 350B.",
  "bodies-articles-pairs")

P(BO, "hard", "Consider the following pairs of committees or commissions and the subject of their reports:",
  "समितियों या आयोगों और उनकी रिपोर्टों के विषय के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Punchhi Commission (2010) : Centre-State relations", "Hota Committee (2004) : Judicial appointments",
   "Dinesh Goswami Committee (1990) : Electoral reforms", "Kothari Committee (1976) : Police reforms"],
  ["पुंछी आयोग (2010) : केंद्र-राज्य संबंध", "होता समिति (2004) : न्यायिक नियुक्तियाँ",
   "दिनेश गोस्वामी समिति (1990) : चुनाव सुधार", "कोठारी समिति (1976) : पुलिस सुधार"],
  1,
  "Only pairs 1 and 3 are correct. "
  "Pair 2 is wrong: the P.C. Hota Committee reported on civil services reforms -- performance appraisal, tenure and training. Pair 4 is wrong: the D.S. Kothari Committee reviewed the UPSC's recruitment and selection methods, which led to the three-stage civil services examination of 1979; police reforms were the subject of the National Police Commission (1977-81).",
  "केवल युग्म 1 और 3 सही हैं। "
  "युग्म 2 गलत है: पी.सी. होता समिति ने सिविल सेवा सुधारों, जैसे कार्य-मूल्यांकन, कार्यकाल और प्रशिक्षण, पर रिपोर्ट दी। युग्म 4 गलत है: डी.एस. कोठारी समिति ने UPSC की भर्ती और चयन पद्धतियों की समीक्षा की, जिससे 1979 की तीन-चरणीय सिविल सेवा परीक्षा बनी; पुलिस सुधार राष्ट्रीय पुलिस आयोग (1977-81) का विषय थे।",
  "Commission on Centre-State Relations (2010); Committee on Civil Services Reforms (2004); Committee on Electoral Reforms (1990); Committee on Recruitment Policy and Selection Methods (1976).",
  "bodies-committees-subjects-pairs")

if __name__ == "__main__":
    write("pol_l2_t3_institutions.sql")
