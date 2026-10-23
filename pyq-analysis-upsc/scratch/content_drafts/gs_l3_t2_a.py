# -*- coding: utf-8 -*-
"""Level 3 · Test 2 (GS Integrated Test 2) -- part A: Polity (15) (upsc_l3_cell_targets.mjs 2).
Same cell plan as Test 1: Judicial-Verdicts e-pairs; Federalism h-MCQ, m-stmt; Constitutional Framework h-stmt,
m-stmt; Parliament h-stmt, m-MCQ, m-stmt; Bodies h-SI; Panchayati Raj h-SI; Governance m-MCQ, m-stmt;
Statutory-Laws m-stmt; Executive m-stmt; Rights m-stmt.
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Test 1, and is one none of them
tests: Sunil Batra, A.K. Kraipak, Rudul Sah and M.H. Hoskot; 'special category status'; Government contracts and suits
(Articles 299 and 300); the One Nation One Election Bill (129th Amendment) and the Kovind committee; the State Chief
Electoral Officer (RPA 1950 s.13A); two-child and other State disqualifications for panchayats (Article 243F, Javed,
Rajbala); the Saansad Adarsh Gram Yojana's funding; Article 361A; the Panchayat Advancement Index; the Epidemic
Diseases Act after 2020; the tribal welfare minister of Article 164(1); Articles 393, 394A and 395; the make-up of a
Legislative Council (Article 171(3)); Sikkim's special provisions (Article 371F); Article 51A(k) and the Verma
committee. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
COI = "Constitution of India"
POL11 = "NCERT Class XI, Political Science -- Indian Constitution at Work"
SC = "Supreme Court of India"
MOPR = "Ministry of Panchayati Raj"

# ---------------------------------------------------------------- Judicial-Verdicts (e-pairs)
P("Judicial-Verdicts", "easy", "Consider the following pairs of Supreme Court judgments and what they decided:",
  "सर्वोच्च न्यायालय के निर्णयों और उनमें तय की गई बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sunil Batra (1978) : Prisoners keep their fundamental rights, and solitary confinement and bar fetters were curbed",
   "A.K. Kraipak (1969) : The rules of natural justice apply to administrative inquiries too",
   "Rudul Sah (1983) : The Court can award compensation for unlawful detention in a writ petition",
   "M.H. Hoskot (1978) : Free legal aid for a poor accused is part of the right to life and personal liberty"],
  ["सुनील बत्रा (1978) : क़ैदियों के मौलिक अधिकार बने रहते हैं, और एकांत कारावास तथा बेड़ियों पर रोक लगाई गई",
   "ए.के. क्रैपक (1969) : नैसर्गिक न्याय के नियम प्रशासनिक जाँचों पर भी लागू होते हैं",
   "रुदुल साह (1983) : न्यायालय रिट याचिका में अवैध निरोध के लिए प्रतिकर दिला सकता है",
   "एम.एच. होसकोट (1978) : निर्धन अभियुक्त के लिए निःशुल्क विधिक सहायता जीवन और दैहिक स्वतंत्रता के अधिकार का अंग है"],
  3,
  "All four pairs are correct. In Sunil Batra the Court held that a prisoner does not shed fundamental rights at the prison gate, and restricted solitary confinement and the use of bar fetters; the second case began with a prisoner's letter, an early example of epistolary jurisdiction. "
  "A.K. Kraipak, arising from a selection board on which a candidate sat as a member, held that natural justice binds administrative as well as quasi-judicial bodies. "
  "In Rudul Sah, a man kept in jail for fourteen years after his acquittal was awarded compensation under Article 32, the start of public-law compensation for violations of Article 21. "
  "M.H. Hoskot read the right to free legal aid, and to a copy of the judgment for an appeal, into Article 21, in line with Article 39A.",
  "चारों युग्म सही हैं। सुनील बत्रा में न्यायालय ने माना कि क़ैदी जेल के दरवाज़े पर अपने मौलिक अधिकार नहीं छोड़ देता, और एकांत कारावास तथा बेड़ियों के प्रयोग को सीमित किया; दूसरा मामला एक क़ैदी के पत्र से शुरू हुआ, जो पत्र-आधारित क्षेत्राधिकार का आरंभिक उदाहरण है। "
  "ए.के. क्रैपक, जो एक ऐसे चयन बोर्ड से उठा जिसमें एक अभ्यर्थी स्वयं सदस्य था, ने माना कि नैसर्गिक न्याय अर्ध-न्यायिक के साथ प्रशासनिक निकायों को भी बाँधता है। "
  "रुदुल साह में बरी होने के बाद चौदह वर्ष जेल में रखे गए व्यक्ति को अनुच्छेद 32 के अंतर्गत प्रतिकर दिलाया गया, जो अनुच्छेद 21 के उल्लंघन पर लोक-विधि प्रतिकर की शुरुआत थी। "
  "एम.एच. होसकोट ने निःशुल्क विधिक सहायता, और अपील के लिए निर्णय की प्रति पाने के अधिकार, को अनुच्छेद 39A के अनुरूप अनुच्छेद 21 में पढ़ा।",
  f"{SC}: Sunil Batra v. Delhi Administration (1978); A.K. Kraipak v. Union of India (1969); Rudul Sah v. State of Bihar (1983); M.H. Hoskot v. State of Maharashtra (1978).",
  "l3-t2-pol-verdicts-batra-kraipak-rudul-hoskot", craft="recall")

# ---------------------------------------------------------------- Federalism & Special Provisions (h-MCQ, m-stmt)
M("Federalism & Special Provisions", "hard",
  "Which one of the following correctly describes the 'special category status' that some States have long sought?",
  "निम्नलिखित में से कौन-सा उस 'विशेष श्रेणी दर्जे' का सही वर्णन करता है जिसकी माँग कुछ राज्य लंबे समय से करते रहे हैं?",
  ["It is conferred by a constitutional amendment adding an Article for the State, which then gets a development board",
   "It is granted by the Finance Commission, and a State holding it is exempt from paying the Goods and Services Tax",
   "It means that the whole State is brought under the Sixth Schedule, with district councils in every district",
   "It has no basis in the Constitution; it began in 1969 as a planning-era category for hill and border States"],
  ["यह राज्य के लिए एक अनुच्छेद जोड़ने वाले संविधान संशोधन से मिलता है, जिसके बाद राज्य को एक विकास बोर्ड मिलता है",
   "यह वित्त आयोग देता है, और इसे पाने वाला राज्य वस्तु एवं सेवा कर चुकाने से मुक्त हो जाता है",
   "इसका अर्थ है कि पूरा राज्य छठी अनुसूची के अंतर्गत आ जाता है, और हर ज़िले में ज़िला परिषद बनती है",
   "संविधान में इसका आधार नहीं; यह 1969 में पहाड़ी व सीमावर्ती राज्यों की योजना-कालीन श्रेणी के रूप में शुरू हुआ"],
  3,
  "Special category status is not mentioned in the Constitution. It was adopted with the Gadgil formula for plan assistance in 1969, for States with hilly terrain, sparse population or a large tribal share, strategic border locations and weak finances; eleven States came to hold it, and they received central assistance on easier terms. "
  "After the Fourteenth Finance Commission (2015) stopped distinguishing between special and general category States in tax devolution, the difference survives mainly in the more generous 90:10 sharing of centrally sponsored schemes for the north-eastern and Himalayan States -- which is why States such as Bihar and Andhra Pradesh keep asking for it. "
  "Article-wise special provisions (Articles 371 to 371J), Sixth Schedule areas and GST rules are different things altogether.",
  "विशेष श्रेणी दर्जे का संविधान में उल्लेख नहीं है। इसे 1969 में योजना सहायता के गाडगिल सूत्र के साथ उन राज्यों के लिए अपनाया गया जिनका भूभाग पहाड़ी, जनसंख्या विरल या जनजातीय अंश बड़ा, स्थिति सामरिक सीमावर्ती और वित्त कमज़ोर थे; ग्यारह राज्यों को यह मिला, और उन्हें आसान शर्तों पर केंद्रीय सहायता मिली। "
  "चौदहवें वित्त आयोग (2015) द्वारा कर हस्तांतरण में विशेष और सामान्य श्रेणी के राज्यों का भेद बंद करने के बाद, अंतर मुख्यतः पूर्वोत्तर और हिमालयी राज्यों के लिए केंद्र प्रायोजित योजनाओं के अधिक उदार 90:10 बँटवारे में बचा है -- इसीलिए बिहार और आंध्र प्रदेश जैसे राज्य इसकी माँग करते रहते हैं। "
  "अनुच्छेद-वार विशेष उपबंध (अनुच्छेद 371 से 371J), छठी अनुसूची के क्षेत्र और GST के नियम बिल्कुल अलग बातें हैं।",
  "Report of the Fourteenth Finance Commission (2015); Ministry of Finance; NITI Aayog.",
  "l3-t2-pol-special-category-status", pos=3, craft="precision")

S("Federalism & Special Provisions", "medium", "Consider the following statements about the special provisions for Sikkim:",
  "सिक्किम के लिए विशेष उपबंधों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["One seat in the Sikkim Legislative Assembly is set apart for the Sangha, with an electorate drawn from the Buddhist monasteries.",
   "Seats in the Assembly are reserved for Sikkimese of Bhutia-Lepcha origin.",
   "The Governor has a special responsibility for peace and for an equitable arrangement for the social and economic advancement of the different sections of the population.",
   "The laws in force in Sikkim before it became a State continue until they are amended or repealed by a competent legislature."],
  ["सिक्किम विधानसभा में एक सीट संघ (संघा) के लिए अलग रखी गई है, जिसका निर्वाचक मंडल बौद्ध मठों से बनता है।",
   "विधानसभा में भूटिया-लेप्चा मूल के सिक्किमी लोगों के लिए सीटें आरक्षित हैं।",
   "राज्यपाल पर शांति और जनसंख्या के विभिन्न वर्गों की सामाजिक और आर्थिक उन्नति के लिए न्यायसंगत व्यवस्था का विशेष उत्तरदायित्व है।",
   "राज्य बनने से पहले सिक्किम में लागू क़ानून तब तक बने रहते हैं जब तक कोई सक्षम विधानमंडल उन्हें संशोधित या निरस्त न कर दे।"],
  C4, 3,
  "All four statements are correct. Article 371F, inserted when the 36th Amendment (1975) made Sikkim a State, lets Parliament reserve Assembly seats to protect the different sections of Sikkim's people: of the 32 seats, 12 are reserved for the Bhutia-Lepcha, 2 for the Scheduled Castes and 1 for the Sangha, elected by the monks of the recognised monasteries -- the only constituency in India with a religious electorate. "
  "Clause (g) gives the Governor the special responsibility described, to be discharged in the Governor's discretion under the President's directions, and clause (k) keeps Sikkim's earlier laws alive until changed -- which is why older Sikkimese laws on matters such as land and residence still apply.",
  "चारों कथन सही हैं। अनुच्छेद 371F, जो 36वें संशोधन (1975) द्वारा सिक्किम को राज्य बनाते समय जोड़ा गया, संसद को सिक्किम की जनता के विभिन्न वर्गों की रक्षा के लिए विधानसभा सीटें आरक्षित करने देता है: 32 सीटों में से 12 भूटिया-लेप्चा, 2 अनुसूचित जातियों और 1 संघ के लिए आरक्षित है, जिसे मान्यता-प्राप्त मठों के भिक्षु चुनते हैं -- भारत में धार्मिक निर्वाचक मंडल वाला एकमात्र निर्वाचन क्षेत्र। "
  "खंड (g) राज्यपाल को वर्णित विशेष उत्तरदायित्व देता है, जिसे राष्ट्रपति के निर्देशों के अधीन राज्यपाल अपने विवेक से निभाते हैं, और खंड (k) सिक्किम के पुराने क़ानूनों को बदले जाने तक जीवित रखता है -- इसीलिए भूमि और निवास जैसे विषयों पर पुराने सिक्किमी क़ानून अब भी लागू हैं।",
  f"{COI}, Article 371F; Constitution (Thirty-sixth Amendment) Act, 1975; Representation of the People Act, 1950, s.7(1A).",
  "l3-t2-pol-sikkim-371f", craft="precision")

# ---------------------------------------------------------------- Constitutional Framework (h-stmt, m-stmt)
S("Constitutional Framework", "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Contracts made in the exercise of the executive power of the Union are expressed to be made by the President.",
   "The President is personally liable on such contracts, though immune from criminal proceedings during the term of office.",
   "The Government of India may sue and be sued by the name of the Union of India."],
  ["संघ की कार्यपालिका शक्ति के प्रयोग में किए गए अनुबंध राष्ट्रपति द्वारा किए गए व्यक्त किए जाते हैं।",
   "राष्ट्रपति ऐसे अनुबंधों पर व्यक्तिगत रूप से दायी होते हैं, यद्यपि पद की अवधि में आपराधिक कार्यवाही से उन्हें उन्मुक्ति है।",
   "भारत सरकार 'भारत संघ' के नाम से वाद ला सकती है और उस पर वाद लाया जा सकता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Article 299(1) requires contracts of the Union or a State to be expressed as made by the President or the Governor and executed by persons authorised by them; the courts have held that a contract not made in this form cannot be enforced against the government. "
  "Statement 2 is wrong: Article 299(2) expressly says that neither the President nor a Governor, nor the person executing the contract, is personally liable on it. "
  "Article 300 lets the Government of India sue or be sued as the 'Union of India' and a State government in the name of the State -- so a citizen's claim on a broken government contract lies against the Union or the State, never against the head of state personally.",
  "कथन 1 और 3 सही हैं। अनुच्छेद 299(1) संघ या राज्य के अनुबंधों को राष्ट्रपति या राज्यपाल द्वारा किए गए व्यक्त करने और उनके द्वारा प्राधिकृत व्यक्तियों द्वारा निष्पादित करने की अपेक्षा करता है; न्यायालयों ने माना है कि इस रूप में न किया गया अनुबंध सरकार के विरुद्ध लागू नहीं कराया जा सकता। "
  "कथन 2 ग़लत है: अनुच्छेद 299(2) स्पष्ट कहता है कि न राष्ट्रपति, न राज्यपाल, न अनुबंध निष्पादित करने वाला व्यक्ति उस पर व्यक्तिगत रूप से दायी है। "
  "अनुच्छेद 300 भारत सरकार को 'भारत संघ' के रूप में और राज्य सरकार को राज्य के नाम से वाद लाने या वाद झेलने देता है -- इसलिए टूटे सरकारी अनुबंध पर नागरिक का दावा संघ या राज्य के विरुद्ध होता है, राज्य-प्रमुख के विरुद्ध व्यक्तिगत रूप से कभी नहीं।",
  f"{COI}, Articles 299 and 300.",
  "l3-t2-pol-art299-300-contracts-suits", craft="precision")

S("Constitutional Framework", "medium", "Consider the following statements about the closing Articles of the Constitution:",
  "संविधान के अंतिम अनुच्छेदों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 394A, inserted by the 58th Amendment in 1987, provides for an authoritative text of the Constitution in Hindi, published under the authority of the President.",
   "Article 395 repealed the Indian Independence Act, 1947, the Government of India Act, 1935 and the Abolition of Privy Council Jurisdiction Act, 1949.",
   "Article 393 gives the Constitution the short title 'the Constitution of the Republic of India'."],
  ["58वें संशोधन द्वारा 1987 में जोड़ा गया अनुच्छेद 394A राष्ट्रपति के प्राधिकार से प्रकाशित, हिंदी में संविधान के प्राधिकृत पाठ का उपबंध करता है।",
   "अनुच्छेद 395 ने भारतीय स्वतंत्रता अधिनियम, 1947, भारत शासन अधिनियम, 1935 और प्रिवी काउंसिल क्षेत्राधिकार उत्सादन अधिनियम, 1949 को निरस्त किया।",
   "अनुच्छेद 393 संविधान को 'भारत गणराज्य का संविधान' संक्षिप्त नाम देता है।"],
  C3, 0,
  "Only statement 1 is correct. Article 394A provides for Hindi translations of the Constitution and of its amendments, published under the President's authority, to count as authoritative texts. "
  "Statement 2 is wrong: Article 395 repealed the Indian Independence Act and the Government of India Act, 1935 with the Acts amending it, but expressly left out the Abolition of Privy Council Jurisdiction Act, 1949, which had already ended appeals to the Privy Council and given that work to the Federal Court and then the Supreme Court. "
  "Statement 3 is wrong: Article 393 says simply, 'This Constitution may be called the Constitution of India.'",
  "केवल कथन 1 सही है। अनुच्छेद 394A संविधान और उसके संशोधनों के हिंदी अनुवादों को, जो राष्ट्रपति के प्राधिकार से प्रकाशित हों, प्राधिकृत पाठ मानने का उपबंध करता है। "
  "कथन 2 ग़लत है: अनुच्छेद 395 ने भारतीय स्वतंत्रता अधिनियम और भारत शासन अधिनियम, 1935 को उसके संशोधक अधिनियमों सहित निरस्त किया, पर प्रिवी काउंसिल क्षेत्राधिकार उत्सादन अधिनियम, 1949 को स्पष्ट रूप से छोड़ दिया, जिसने पहले ही प्रिवी काउंसिल में अपीलें समाप्त कर वह काम फ़ेडरल न्यायालय और फिर सर्वोच्च न्यायालय को दे दिया था। "
  "कथन 3 ग़लत है: अनुच्छेद 393 बस इतना कहता है, 'इस संविधान का संक्षिप्त नाम भारत का संविधान है।'",
  f"{COI}, Articles 393, 394A and 395; Constitution (Fifty-eighth Amendment) Act, 1987.",
  "l3-t2-pol-art393-394a-395", craft="precision")

# ---------------------------------------------------------------- Parliament & State Legislature (h-stmt, m-MCQ, m-stmt)
S("Parliament & State Legislature", "hard", "With reference to the proposal for simultaneous elections, consider the following statements:",
  "एक साथ चुनाव कराने के प्रस्ताव के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The High-Level Committee chaired by Ram Nath Kovind recommended holding Lok Sabha and State Assembly elections together first, with municipal and panchayat elections following within 100 days.",
   "The Constitution (One Hundred and Twenty-Ninth Amendment) Bill, 2024 provides that if the Lok Sabha is dissolved early, the newly elected House will serve only for the rest of the original term.",
   "The Bill brings panchayat and municipal elections into the same cycle as Lok Sabha elections."],
  ["राम नाथ कोविंद की अध्यक्षता वाली उच्च-स्तरीय समिति ने पहले लोकसभा और राज्य विधानसभाओं के चुनाव एक साथ कराने, और उसके 100 दिनों के भीतर नगरपालिका और पंचायत चुनाव कराने की सिफ़ारिश की।",
   "संविधान (एक सौ उनतीसवाँ संशोधन) विधेयक, 2024 यह उपबंध करता है कि यदि लोकसभा समय से पहले भंग हो, तो नई चुनी गई सभा केवल मूल अवधि के शेष भाग के लिए कार्य करेगी।",
   "विधेयक पंचायत और नगरपालिका चुनावों को लोकसभा चुनावों के समान चक्र में लाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Kovind committee (report, March 2024) proposed a two-step plan and a single electoral roll for all three tiers. The Bill introduced in the Lok Sabha in December 2024 and sent to a Joint Parliamentary Committee would insert Article 82A: from an 'appointed date' notified after a general election, the terms of all Assemblies would end with that of the Lok Sabha, and a House elected after an early dissolution would serve only the unexpired term. "
  "Statement 3 is wrong: the Bill leaves out local bodies. Changing their elections would touch Parts IX and IXA and the State List, which would need ratification by half the States under Article 368(2) -- a hurdle the Bill avoids by dealing only with the Lok Sabha and the Assemblies.",
  "कथन 1 और 2 सही हैं। कोविंद समिति (रिपोर्ट, मार्च 2024) ने दो-चरणीय योजना और तीनों स्तरों के लिए एक ही मतदाता सूची प्रस्तावित की। दिसंबर 2024 में लोकसभा में पेश और संयुक्त संसदीय समिति को भेजा गया विधेयक अनुच्छेद 82A जोड़ेगा: आम चुनाव के बाद अधिसूचित 'नियत तिथि' से सभी विधानसभाओं का कार्यकाल लोकसभा के साथ समाप्त होगा, और समय से पहले विघटन के बाद चुनी गई सभा केवल शेष अवधि के लिए कार्य करेगी। "
  "कथन 3 ग़लत है: विधेयक स्थानीय निकायों को छोड़ देता है। उनके चुनाव बदलने से भाग IX और IXA तथा राज्य सूची प्रभावित होते, जिसके लिए अनुच्छेद 368(2) के अंतर्गत आधे राज्यों का अनुसमर्थन चाहिए होता -- विधेयक केवल लोकसभा और विधानसभाओं से निपटकर इस बाधा से बचता है।",
  "Report of the High-Level Committee on Simultaneous Elections (2024); Constitution (One Hundred and Twenty-Ninth Amendment) Bill, 2024; " + COI + ", Article 368(2).",
  "l3-t2-pol-simultaneous-elections-129th-bill", craft="inference")

M("Parliament & State Legislature", "medium",
  "A newspaper publishes a substantially true report of a Lok Sabha debate in which a member made a defamatory remark about a private citizen. Under Article 361A, the newspaper:",
  "एक समाचार-पत्र लोकसभा की उस बहस की सारतः सत्य रिपोर्ट छापता है जिसमें एक सदस्य ने किसी निजी नागरिक के बारे में मानहानिकारक टिप्पणी की थी। अनुच्छेद 361A के अंतर्गत समाचार-पत्र:",
  ["cannot be sued or prosecuted for it unless the report is proved to be malicious",
   "is protected only if the Speaker has given written permission for the report before it is printed",
   "has no protection, since the immunity under Article 105 belongs to members of Parliament alone",
   "is protected even for reports of secret sittings, as long as the report is accurate in substance"],
  ["उस पर इसके लिए वाद या अभियोजन नहीं चल सकता, जब तक रिपोर्ट द्वेषपूर्ण सिद्ध न हो",
   "केवल तभी सुरक्षित है जब अध्यक्ष ने छपने से पहले रिपोर्ट के लिए लिखित अनुमति दी हो",
   "को कोई सुरक्षा नहीं है, क्योंकि अनुच्छेद 105 की उन्मुक्ति केवल संसद सदस्यों की है",
   "गुप्त बैठकों की रिपोर्टों के लिए भी सुरक्षित है, जब तक रिपोर्ट सार में सटीक हो"],
  0,
  "Article 361A, inserted by the 44th Amendment (1978), protects from civil and criminal proceedings anyone who publishes in a newspaper, or broadcasts, a substantially true report of the proceedings of Parliament or a State Legislature, unless malice is proved; it does not cover secret sittings. "
  "It gave constitutional footing to the Parliamentary Proceedings (Protection of Publication) Act, 1956, moved by Feroze Gandhi, which had been repealed during the Emergency. Article 105 protects what members say in the House; Article 361A extends a narrower shield to those who report it.",
  "44वें संशोधन (1978) द्वारा जोड़ा गया अनुच्छेद 361A उस हर व्यक्ति को दीवानी और आपराधिक कार्यवाही से बचाता है जो संसद या राज्य विधानमंडल की कार्यवाही की सारतः सत्य रिपोर्ट समाचार-पत्र में छापता या प्रसारित करता है, जब तक द्वेष सिद्ध न हो; यह गुप्त बैठकों पर लागू नहीं होता। "
  "इसने फ़िरोज़ गांधी द्वारा प्रस्तुत संसदीय कार्यवाही (प्रकाशन संरक्षण) अधिनियम, 1956 को, जो आपातकाल के दौरान निरस्त कर दिया गया था, संवैधानिक आधार दिया। अनुच्छेद 105 सदस्यों द्वारा सदन में कही गई बातों की रक्षा करता है; अनुच्छेद 361A उसकी रिपोर्ट करने वालों को एक संकरी ढाल देता है।",
  f"{COI}, Articles 105 and 361A; Constitution (Forty-fourth Amendment) Act, 1978.",
  "l3-t2-pol-art361a-reports-of-proceedings", pos=2, craft="application")

S("Parliament & State Legislature", "medium", "With reference to the composition of a State Legislative Council, consider the following statements:",
  "किसी राज्य की विधान परिषद की संरचना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["About one-third of its members are elected by electorates of members of municipalities, district boards and other local authorities.",
   "One-twelfth are elected by persons residing in the State who have been graduates of a university for at least three years.",
   "About one-sixth are nominated by the Governor from persons with special knowledge or practical experience of literature, science, art, the cooperative movement and social service.",
   "One-third are elected by the members of the Legislative Assembly from among themselves."],
  ["उसके लगभग एक-तिहाई सदस्य नगरपालिकाओं, ज़िला बोर्डों और अन्य स्थानीय प्राधिकरणों के सदस्यों से बने निर्वाचक मंडल चुनते हैं।",
   "एक-बारहवाँ भाग राज्य में रहने वाले उन व्यक्तियों द्वारा चुना जाता है जो कम से कम तीन वर्ष से किसी विश्वविद्यालय के स्नातक हैं।",
   "लगभग एक-छठा भाग राज्यपाल साहित्य, विज्ञान, कला, सहकारी आंदोलन और समाज सेवा के विशेष ज्ञान या व्यावहारिक अनुभव वाले व्यक्तियों में से नामित करते हैं।",
   "एक-तिहाई सदस्य विधानसभा के सदस्य अपने में से ही चुनते हैं।"],
  C4, 2,
  "The first three statements are correct. Under Article 171(3), about one-third of a Council is elected by local-authority electorates, one-twelfth by graduates of three years' standing, one-twelfth by teachers of three years' standing in secondary schools and above, one-third by the Assembly, and the rest -- about one-sixth -- nominated by the Governor. "
  "Statement 4 is wrong: the Assembly elects its one-third from among persons who are not members of the Assembly, so that the Council brings in people outside it. All the elected members are chosen by proportional representation through the single transferable vote.",
  "पहले तीन कथन सही हैं। अनुच्छेद 171(3) के अंतर्गत परिषद का लगभग एक-तिहाई स्थानीय प्राधिकरणों के निर्वाचक मंडल, एक-बारहवाँ तीन वर्ष पुराने स्नातक, एक-बारहवाँ माध्यमिक और उससे ऊपर के विद्यालयों के तीन वर्ष से कार्यरत शिक्षक, एक-तिहाई विधानसभा चुनती है, और शेष -- लगभग एक-छठा -- राज्यपाल नामित करते हैं। "
  "कथन 4 ग़लत है: विधानसभा अपना एक-तिहाई उन व्यक्तियों में से चुनती है जो विधानसभा के सदस्य नहीं हैं, ताकि परिषद बाहर के लोगों को ला सके। सभी निर्वाचित सदस्य एकल संक्रमणीय मत द्वारा आनुपातिक प्रतिनिधित्व से चुने जाते हैं।",
  f"{COI}, Article 171(3).",
  "l3-t2-pol-legislative-council-composition", craft="precision")

# ---------------------------------------------------------------- Constitutional & Statutory Bodies (h-SI)
A("Constitutional & Statutory Bodies", "hard",
  "The Chief Electoral Officer of a State supervises the preparation and revision of electoral rolls and the conduct of elections in the State, subject to the superintendence, direction and control of the Election Commission of India.",
  "किसी राज्य का मुख्य निर्वाचन अधिकारी भारत निर्वाचन आयोग के अधीक्षण, निर्देशन और नियंत्रण के अधीन राज्य में मतदाता सूचियों की तैयारी और पुनरीक्षण तथा चुनावों के संचालन का पर्यवेक्षण करता है।",
  "The Chief Electoral Officer is chosen by the State government on its own, the Election Commission having no part in the selection.",
  "मुख्य निर्वाचन अधिकारी को राज्य सरकार अपने स्तर पर चुनती है, चयन में निर्वाचन आयोग की कोई भूमिका नहीं होती।",
  2,
  "Statement-I is correct and Statement-II is incorrect. Section 13A of the Representation of the People Act, 1950 provides for a Chief Electoral Officer in each State, who works under the Election Commission's superintendence, direction and control. "
  "The officer is an officer of the State government, but it is the Election Commission that designates or nominates the officer, in consultation with that government. During elections, the officers on election duty are deemed to be on deputation to the Commission (section 13CC), so that the Commission, which has no large staff of its own, can direct the State machinery.",
  "कथन-I सही है और कथन-II ग़लत है। लोक प्रतिनिधित्व अधिनियम, 1950 की धारा 13A हर राज्य में एक मुख्य निर्वाचन अधिकारी का उपबंध करती है, जो निर्वाचन आयोग के अधीक्षण, निर्देशन और नियंत्रण में काम करता है। "
  "वह अधिकारी राज्य सरकार का अधिकारी होता है, पर उसे उस सरकार के परामर्श से निर्वाचन आयोग ही पदाभिहित या नामित करता है। चुनावों के दौरान चुनाव ड्यूटी वाले अधिकारी आयोग में प्रतिनियुक्ति पर माने जाते हैं (धारा 13CC), ताकि आयोग, जिसका अपना बड़ा कर्मचारी-वर्ग नहीं है, राज्य की मशीनरी को निर्देश दे सके।",
  f"Representation of the People Act, 1950, ss.13A and 13CC; {COI}, Article 324.",
  "l3-t2-pol-chief-electoral-officer", craft="precision")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (h-SI)
A("Panchayati Raj & Local Governance", "hard",
  "Some States bar persons with more than two children from contesting panchayat elections, and the Supreme Court has upheld such a bar.",
  "कुछ राज्य दो से अधिक संतान वाले व्यक्तियों को पंचायत चुनाव लड़ने से रोकते हैं, और सर्वोच्च न्यायालय ने ऐसी रोक को सही ठहराया है।",
  "Article 243F allows a State Legislature to prescribe, by law, disqualifications for membership of a Panchayat.",
  "अनुच्छेद 243F राज्य विधानमंडल को क़ानून द्वारा पंचायत की सदस्यता के लिए निरर्हताएँ निर्धारित करने देता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Article 243F disqualifies a person from panchayat membership under the election laws of the State and also 'by or under any law made by the Legislature of the State', which is what lets States add conditions of their own. "
  "In Javed v. State of Haryana (2003) the Court upheld Haryana's two-child bar as a reasonable measure that did not violate Articles 14, 21 or 25, and in Rajbala v. State of Haryana (2015) it upheld minimum educational qualifications, a working toilet at home and the clearing of certain dues as conditions for contesting. Such conditions vary from State to State, and some States have since dropped the two-child rule.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। अनुच्छेद 243F किसी व्यक्ति को राज्य के निर्वाचन क़ानूनों के अंतर्गत और 'राज्य के विधानमंडल द्वारा बनाई गई किसी विधि द्वारा या उसके अधीन' भी पंचायत सदस्यता के लिए निरर्हित करता है, और यही राज्यों को अपनी शर्तें जोड़ने देता है। "
  "जावेद बनाम हरियाणा राज्य (2003) में न्यायालय ने हरियाणा की दो-संतान रोक को अनुच्छेद 14, 21 या 25 का उल्लंघन न करने वाला युक्तियुक्त उपाय मानकर बनाए रखा, और राजबाला बनाम हरियाणा राज्य (2015) में उसने न्यूनतम शैक्षिक योग्यता, घर में चालू शौचालय और कुछ बकायों के भुगतान को चुनाव लड़ने की शर्तों के रूप में बनाए रखा। ऐसी शर्तें राज्य-दर-राज्य भिन्न हैं, और कुछ राज्यों ने बाद में दो-संतान नियम हटा दिया है।",
  f"{COI}, Article 243F; {SC}: Javed v. State of Haryana (2003); Rajbala v. State of Haryana (2015).",
  "l3-t2-pol-art243f-two-child-qualifications", craft="linkage")

# ---------------------------------------------------------------- Governance (m-MCQ, m-stmt)
M("Governance", "medium",
  "Under the Saansad Adarsh Gram Yojana, each Member of Parliament adopts a gram panchayat to develop as a model village. How are the works in such a village mainly financed?",
  "सांसद आदर्श ग्राम योजना के अंतर्गत हर संसद सदस्य एक ग्राम पंचायत को आदर्श गाँव के रूप में विकसित करने के लिए गोद लेता है। ऐसे गाँव में काम मुख्यतः कैसे वित्तपोषित होते हैं?",
  ["Through existing schemes brought together, with MPLADS and CSR funds, and no separate allocation",
   "Through a dedicated central grant of ₹5 crore for each village, released directly to the Member of Parliament",
   "Through a share of the Goods and Services Tax collected in that village, returned to the gram panchayat",
   "Through long-term loans from NABARD that the gram panchayat repays from its own property tax income"],
  ["मौजूदा योजनाओं को एक साथ लाकर, MPLADS और CSR निधियों के साथ, बिना किसी अलग आवंटन के",
   "हर गाँव के लिए ₹5 करोड़ के एक समर्पित केंद्रीय अनुदान से, जो सीधे संसद सदस्य को जारी होता है",
   "उस गाँव में एकत्र वस्तु एवं सेवा कर के एक हिस्से से, जो ग्राम पंचायत को लौटाया जाता है",
   "नाबार्ड के दीर्घकालिक ऋणों से, जिन्हें ग्राम पंचायत अपनी संपत्ति कर की आय से चुकाती है"],
  0,
  "The Saansad Adarsh Gram Yojana (2014), run by the Ministry of Rural Development, has no funds of its own. The adopted village's plan is carried out by converging existing central and State schemes, with the MP's Local Area Development funds, the panchayat's own revenue and corporate social responsibility money filling gaps. "
  "The idea is that an MP's leadership and attention, not a new budget head, make the difference -- which is also why progress has varied widely from one MP's village to another.",
  "सांसद आदर्श ग्राम योजना (2014), जिसे ग्रामीण विकास मंत्रालय चलाता है, की अपनी कोई निधि नहीं है। गोद लिए गाँव की योजना मौजूदा केंद्रीय और राज्य योजनाओं के अभिसरण से पूरी की जाती है, और सांसद स्थानीय क्षेत्र विकास निधि, पंचायत की अपनी आय तथा कॉर्पोरेट सामाजिक उत्तरदायित्व का धन कमियाँ भरते हैं। "
  "विचार यह है कि नया बजट शीर्ष नहीं, बल्कि सांसद का नेतृत्व और ध्यान अंतर लाता है -- इसीलिए प्रगति एक सांसद के गाँव से दूसरे के गाँव तक बहुत भिन्न रही है।",
  "Ministry of Rural Development (Saansad Adarsh Gram Yojana guidelines, 2014).",
  "l3-t2-pol-sagy-convergence-funding", pos=1, craft="precision")

S("Governance", "medium", "Consider the following statements about the Panchayat Advancement Index:",
  "पंचायत उन्नति सूचकांक के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It assesses gram panchayats on themes of the localised Sustainable Development Goals.",
   "It is prepared by NITI Aayog.",
   "It ranks States, and does not grade individual gram panchayats."],
  ["यह स्थानीयकृत सतत विकास लक्ष्यों के विषयों पर ग्राम पंचायतों का आकलन करता है।",
   "इसे नीति आयोग तैयार करता है।",
   "यह राज्यों को श्रेणीबद्ध करता है, अलग-अलग ग्राम पंचायतों को ग्रेड नहीं देता।"],
  C3, 0,
  "Only statement 1 is correct. The Panchayat Advancement Index, brought out by the Ministry of Panchayati Raj, measures gram panchayats against hundreds of local indicators grouped under nine themes of the localised SDGs, such as a poverty-free village, a healthy village, a water-sufficient village and a village with good governance. "
  "It grades each gram panchayat -- as Achiever, Front Runner, Performer, Aspirant or Beginner -- so that panchayats can plan against their own gaps; in the baseline edition for 2022-23, covering over two lakh gram panchayats, none reached the top grade.",
  "केवल कथन 1 सही है। पंचायती राज मंत्रालय द्वारा जारी पंचायत उन्नति सूचकांक ग्राम पंचायतों को स्थानीयकृत SDG के नौ विषयों, जैसे ग़रीबी-मुक्त गाँव, स्वस्थ गाँव, जल-पर्याप्त गाँव और सुशासन वाला गाँव, के अंतर्गत समूहित सैकड़ों स्थानीय संकेतकों पर मापता है। "
  "यह हर ग्राम पंचायत को ग्रेड देता है -- अचीवर, फ़्रंट रनर, परफ़ॉर्मर, एस्पिरेंट या बिगिनर -- ताकि पंचायतें अपनी कमियों के अनुसार योजना बना सकें; 2022-23 के आधार संस्करण में, जिसमें दो लाख से अधिक ग्राम पंचायतें शामिल थीं, कोई भी शीर्ष ग्रेड तक नहीं पहुँची।",
  f"{MOPR} (Panchayat Advancement Index, baseline report 2022-23).",
  "l3-t2-pol-panchayat-advancement-index", craft="precision")

# ---------------------------------------------------------------- Statutory-Laws (m-stmt)
S("Statutory-Laws", "medium", "With reference to the Epidemic Diseases Act, 1897, consider the following statements:",
  "महामारी रोग अधिनियम, 1897 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["After its amendment in 2020, an act of violence against healthcare service personnel during an epidemic is a cognisable and non-bailable offence.",
   "It empowers the Union government to inspect ships, aircraft and other vehicles arriving or leaving, and to detain persons travelling in them.",
   "Its Schedule lists the diseases that count as 'epidemic diseases' for the purposes of the Act."],
  ["2020 में इसके संशोधन के बाद, महामारी के दौरान स्वास्थ्य सेवा कर्मियों के विरुद्ध हिंसा का कृत्य संज्ञेय और ग़ैर-ज़मानती अपराध है।",
   "यह संघ सरकार को आने या जाने वाले जहाज़ों, विमानों और अन्य वाहनों का निरीक्षण करने और उनमें यात्रा कर रहे व्यक्तियों को रोकने की शक्ति देता है।",
   "इसकी अनुसूची उन रोगों की सूची देती है जो अधिनियम के प्रयोजनों के लिए 'महामारी रोग' माने जाते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Epidemic Diseases (Amendment) Act, 2020, passed during COVID-19, made violence against healthcare workers and damage to their property cognisable and non-bailable, with up to five years' jail (seven for grievous hurt), and widened section 2A, under which the Union can inspect and detain any ship, aircraft, train, bus or goods vehicle and the persons on it. "
  "Statement 3 is wrong: the Act has no schedule and does not define 'epidemic disease'; it lets the State government take special measures and make regulations when it is satisfied that a dangerous epidemic disease threatens -- a gap that has led to calls for a modern public-health law.",
  "कथन 1 और 2 सही हैं। कोविड-19 के दौरान पारित महामारी रोग (संशोधन) अधिनियम, 2020 ने स्वास्थ्य कर्मियों के विरुद्ध हिंसा और उनकी संपत्ति को क्षति को संज्ञेय और ग़ैर-ज़मानती बनाया, जिसमें पाँच वर्ष तक (गंभीर चोट पर सात वर्ष तक) कारावास है, और धारा 2A का विस्तार किया, जिसके अंतर्गत संघ किसी भी जहाज़, विमान, रेल, बस या माल वाहन और उसमें सवार व्यक्तियों का निरीक्षण और निरोध कर सकता है। "
  "कथन 3 ग़लत है: अधिनियम में कोई अनुसूची नहीं है और वह 'महामारी रोग' को परिभाषित नहीं करता; वह राज्य सरकार को तब विशेष उपाय करने और विनियम बनाने देता है जब उसे विश्वास हो कि कोई ख़तरनाक महामारी रोग फैलने का ख़तरा है -- यही कमी एक आधुनिक लोक-स्वास्थ्य क़ानून की माँग का कारण बनी है।",
  "Epidemic Diseases Act, 1897; Epidemic Diseases (Amendment) Act, 2020.",
  "l3-t2-pol-epidemic-diseases-act-2020", craft="precision")

# ---------------------------------------------------------------- Union & State Executive (m-stmt)
S("Union & State Executive", "medium", "Consider the following statements about the Minister in charge of tribal welfare under Article 164(1):",
  "अनुच्छेद 164(1) के अंतर्गत जनजातीय कल्याण के प्रभारी मंत्री के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Constitution requires such a Minister in Chhattisgarh, Jharkhand, Madhya Pradesh and Odisha.",
   "The same Minister may also be put in charge of the welfare of the Scheduled Castes and backward classes, or of any other work.",
   "Bihar was named in the original provision, and was replaced by Chhattisgarh and Jharkhand through the 94th Amendment, 2006."],
  ["संविधान छत्तीसगढ़, झारखंड, मध्य प्रदेश और ओडिशा में ऐसे मंत्री की अपेक्षा करता है।",
   "उसी मंत्री को अनुसूचित जातियों और पिछड़े वर्गों के कल्याण, या किसी अन्य कार्य का प्रभार भी दिया जा सकता है।",
   "मूल उपबंध में बिहार का नाम था, जिसकी जगह 94वें संशोधन, 2006 द्वारा छत्तीसगढ़ और झारखंड रखे गए।"],
  C3, 2,
  "All three statements are correct. The proviso to Article 164(1) requires a Minister in charge of tribal welfare in these four States, all with large tribal populations, and allows that Minister to hold other charges too. "
  "The original text named Bihar, Madhya Pradesh and Orissa; after Jharkhand was carved out of Bihar and Chhattisgarh out of Madhya Pradesh in 2000, most of Bihar's tribal areas lay in Jharkhand, so the 94th Amendment dropped Bihar and added the two new States. "
  "The rule is narrower than the Fifth Schedule: several States with Scheduled Areas, such as Rajasthan, Gujarat and Maharashtra, are not covered by it.",
  "तीनों कथन सही हैं। अनुच्छेद 164(1) का परंतुक इन चार राज्यों में, जिन सबकी जनजातीय जनसंख्या बड़ी है, जनजातीय कल्याण के प्रभारी मंत्री की अपेक्षा करता है, और उस मंत्री को अन्य प्रभार भी रखने देता है। "
  "मूल पाठ में बिहार, मध्य प्रदेश और उड़ीसा के नाम थे; 2000 में बिहार से झारखंड और मध्य प्रदेश से छत्तीसगढ़ बनने के बाद बिहार के अधिकांश जनजातीय क्षेत्र झारखंड में चले गए, इसलिए 94वें संशोधन ने बिहार को हटाकर दोनों नए राज्य जोड़े। "
  "यह नियम पाँचवीं अनुसूची से संकरा है: अनुसूचित क्षेत्रों वाले कई राज्य, जैसे राजस्थान, गुजरात और महाराष्ट्र, इसके अंतर्गत नहीं आते।",
  f"{COI}, Article 164(1); Constitution (Ninety-fourth Amendment) Act, 2006.",
  "l3-t2-pol-art164-tribal-welfare-minister", craft="linkage")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (m-stmt)
S("Fundamental Rights, DPSP & Duties", "medium", "Consider the following statements about the Fundamental Duties:",
  "मौलिक कर्तव्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The duty of a parent or guardian to provide opportunities for education to a child between six and fourteen years was added by the same amendment that inserted Article 21A.",
   "The Justice J.S. Verma Committee (1999) found that laws already existed to give effect to some of the duties, such as the law against insults to the national flag and anthem.",
   "Like many of the Fundamental Rights, the Fundamental Duties apply to foreigners living in India as well as to citizens."],
  ["छह से चौदह वर्ष के बच्चे को शिक्षा के अवसर देने का माता-पिता या संरक्षक का कर्तव्य उसी संशोधन द्वारा जोड़ा गया जिसने अनुच्छेद 21A जोड़ा।",
   "न्यायमूर्ति जे.एस. वर्मा समिति (1999) ने पाया कि कुछ कर्तव्यों को लागू करने वाले क़ानून पहले से मौजूद थे, जैसे राष्ट्रीय ध्वज और राष्ट्रगान के अपमान के विरुद्ध क़ानून।",
   "कई मौलिक अधिकारों की तरह मौलिक कर्तव्य भी नागरिकों के साथ भारत में रहने वाले विदेशियों पर लागू होते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The 86th Amendment (2002) made elementary education a fundamental right in Article 21A, rewrote Article 45 for early childhood care, and added clause (k) to Article 51A, the eleventh duty. "
  "The Verma Committee, set up to suggest how the duties could be taught and made operational, pointed to laws such as the Prevention of Insults to National Honour Act, 1971 and the Protection of Civil Rights Act, 1955. "
  "Statement 3 is wrong: Article 51A begins 'It shall be the duty of every citizen of India', so the duties bind citizens only.",
  "कथन 1 और 2 सही हैं। 86वें संशोधन (2002) ने अनुच्छेद 21A में प्रारंभिक शिक्षा को मौलिक अधिकार बनाया, प्रारंभिक बाल्यावस्था देखभाल के लिए अनुच्छेद 45 को फिर से लिखा, और अनुच्छेद 51A में खंड (k), ग्यारहवाँ कर्तव्य, जोड़ा। "
  "कर्तव्यों को सिखाने और क्रियाशील बनाने के उपाय सुझाने के लिए गठित वर्मा समिति ने राष्ट्रीय गौरव अपमान निवारण अधिनियम, 1971 और सिविल अधिकार संरक्षण अधिनियम, 1955 जैसे क़ानूनों की ओर ध्यान दिलाया। "
  "कथन 3 ग़लत है: अनुच्छेद 51A 'भारत के प्रत्येक नागरिक का यह कर्तव्य होगा' से शुरू होता है, इसलिए कर्तव्य केवल नागरिकों पर लागू होते हैं।",
  f"{COI}, Articles 21A and 51A(k); Constitution (Eighty-sixth Amendment) Act, 2002; {POL11}.",
  "l3-t2-pol-duties-51a-k-verma-committee", craft="linkage")

write("gs_l3_t2_a.sql")
