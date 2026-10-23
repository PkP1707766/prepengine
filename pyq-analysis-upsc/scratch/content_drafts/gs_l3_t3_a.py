# -*- coding: utf-8 -*-
"""Level 3 · Test 3 (GS Integrated Test 3) -- part A: Polity (15) (upsc_l3_cell_targets.mjs 3).
Same cell plan as Tests 1 and 2.
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Tests 1-2, and is one none of them
tests: Sheela Barse, Nilabati Behera, Sakal Papers and Kharak Singh; Article 269; Article 35; Keisham Meghachandra
Singh and the Speaker's deadline; the National Statistical Commission; the OBC 'triple test' for local bodies; Tele-Law;
expunction of words from debates; the Aspirational Blocks Programme; the Fugitive Economic Offenders Act; filling a
vacancy in the President's office (Articles 62 and 65); Scheduled Caste and Tribe lists (Articles 341 and 342); MPs'
salaries (Article 106); the Ladakh hill councils; Article 19(6). MCQ keys are pinned (pos)."""
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

# ---------------------------------------------------------------- Judicial-Verdicts (e-pairs)
P("Judicial-Verdicts", "easy", "Consider the following pairs of Supreme Court judgments and what they decided:",
  "सर्वोच्च न्यायालय के निर्णयों और उनमें तय की गई बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sheela Barse (1983) : Safeguards for women held in police lock-ups",
   "Nilabati Behera (1993) : The State must pay compensation for a death in police custody",
   "Sakal Papers (1962) : A law fixing the number of pages a newspaper could print for its price was struck down",
   "Kharak Singh (1963) : Night-time domiciliary visits by the police were upheld as reasonable"],
  ["शीला बार्से (1983) : पुलिस हवालात में रखी महिलाओं के लिए सुरक्षाएँ",
   "नीलाबती बेहेरा (1993) : पुलिस हिरासत में मृत्यु के लिए राज्य को प्रतिकर देना होगा",
   "सकाल पेपर्स (1962) : किसी समाचार-पत्र द्वारा उसके दाम के अनुसार छापे जा सकने वाले पृष्ठों की संख्या तय करने वाला क़ानून रद्द किया गया",
   "खड़क सिंह (1963) : पुलिस द्वारा रात में घर पर निगरानी-दौरों को युक्तियुक्त मानकर बनाए रखा गया"],
  2,
  "The first three pairs are correct. Sheela Barse, begun by a journalist's letter, led to separate lock-ups for women, interrogation in the presence of women police and legal aid for women prisoners; Nilabati Behera held that sovereign immunity is no defence when the State violates the right to life, and awarded compensation to a mother whose son died in custody; Sakal Papers treated a price-and-page order as a curb on the circulation, and so the freedom, of the press. "
  "The fourth pair is wrong: Kharak Singh struck down night-time domiciliary visits as a violation of personal liberty under Article 21, though the majority upheld other forms of surveillance -- Justice Subba Rao's dissent on privacy was vindicated in Puttaswamy (2017).",
  "पहले तीन युग्म सही हैं। एक पत्रकार के पत्र से शुरू हुए शीला बार्से से महिलाओं के लिए अलग हवालात, महिला पुलिस की उपस्थिति में पूछताछ और महिला क़ैदियों के लिए विधिक सहायता की व्यवस्था हुई; नीलाबती बेहेरा ने माना कि जब राज्य जीवन के अधिकार का उल्लंघन करे तो संप्रभु उन्मुक्ति कोई बचाव नहीं है, और हिरासत में बेटे की मृत्यु पर माँ को प्रतिकर दिलाया; सकाल पेपर्स ने दाम-और-पृष्ठ आदेश को प्रेस के प्रसार, और इसलिए स्वतंत्रता, पर अंकुश माना। "
  "चौथा युग्म ग़लत है: खड़क सिंह ने रात में घर पर निगरानी-दौरों को अनुच्छेद 21 के अंतर्गत दैहिक स्वतंत्रता का उल्लंघन मानकर रद्द किया, यद्यपि बहुमत ने निगरानी के अन्य रूपों को बनाए रखा -- निजता पर न्यायमूर्ति सुब्बा राव की असहमति पुट्टस्वामी (2017) में सही सिद्ध हुई।",
  f"{SC}: Sheela Barse v. State of Maharashtra (1983); Nilabati Behera v. State of Orissa (1993); Sakal Papers v. Union of India (1962); Kharak Singh v. State of U.P. (1963).",
  "l3-t3-pol-verdicts-barse-behera-sakal-kharak", craft="recall")

# ---------------------------------------------------------------- Federalism & Special Provisions (h-MCQ, m-stmt)
M("Federalism & Special Provisions", "hard",
  "Which one of the following taxes is levied and collected by the Government of India but assigned in full to the States under Article 269?",
  "निम्नलिखित में से कौन-सा कर भारत सरकार द्वारा उद्गृहीत और संगृहीत किया जाता है, पर अनुच्छेद 269 के अंतर्गत पूरा का पूरा राज्यों को सौंप दिया जाता है?",
  ["Stamp duties on bills of exchange, cheques and promissory notes",
   "Corporation tax on the profits of companies",
   "Taxes on the inter-State sale of goods other than newspapers",
   "Basic customs duties levied on goods imported into India"],
  ["विनिमय-पत्रों, चेकों और वचन-पत्रों जैसे लिखतों पर स्टांप शुल्क",
   "कंपनियों के लाभ पर निगम कर",
   "समाचार-पत्रों के अलावा वस्तुओं की अंतर-राज्यीय बिक्री पर कर",
   "भारत में आयातित वस्तुओं पर लगने वाला मूल सीमा शुल्क"],
  2,
  "Article 269 covers taxes on the sale or purchase of goods, other than newspapers, in the course of inter-State trade, and taxes on the consignment of goods; they are levied by the Union but their proceeds go wholly to the States, under principles Parliament lays down. Since the GST, inter-State supplies of goods under GST fall under Article 269A, so Article 269 now matters chiefly for goods outside GST, such as petroleum products, through the Central Sales Tax. "
  "Stamp duties on bills of exchange are the trap: under Article 268 they are levied by the Union but collected and kept by the States. Corporation tax goes into the divisible pool, and customs duties stay with the Union.",
  "अनुच्छेद 269 अंतर-राज्यीय व्यापार के दौरान समाचार-पत्रों के अलावा वस्तुओं की बिक्री या ख़रीद पर करों, और वस्तुओं के परेषण पर करों को शामिल करता है; इन्हें संघ उद्गृहीत करता है पर इनकी आय संसद द्वारा तय सिद्धांतों के अनुसार पूरी राज्यों को जाती है। GST के बाद GST के अंतर्गत वस्तुओं की अंतर-राज्यीय आपूर्ति अनुच्छेद 269A में आती है, इसलिए अनुच्छेद 269 अब मुख्यतः GST से बाहर की वस्तुओं, जैसे पेट्रोलियम उत्पादों, के लिए केंद्रीय बिक्री कर के माध्यम से महत्त्वपूर्ण है। "
  "विनिमय-पत्रों पर स्टांप शुल्क जाल है: अनुच्छेद 268 के अंतर्गत इन्हें संघ उद्गृहीत करता है पर राज्य संगृहीत करते और रखते हैं। निगम कर विभाज्य पूल में जाता है, और सीमा शुल्क संघ के पास रहता है।",
  f"{COI}, Articles 268, 269 and 269A; Constitution (One Hundred and First Amendment) Act, 2016.",
  "l3-t3-pol-art269-inter-state-sale-tax", pos=2, craft="precision")

S("Federalism & Special Provisions", "medium", "Consider the following statements about Ladakh:",
  "लद्दाख के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Autonomous Hill Development Councils of Leh and Kargil are statutory bodies.",
   "Ladakh has been brought under the Sixth Schedule of the Constitution."],
  ["लेह और कारगिल की स्वायत्त पहाड़ी विकास परिषदें वैधानिक निकाय हैं।",
   "लद्दाख को संविधान की छठी अनुसूची के अंतर्गत लाया जा चुका है।"],
  T2, 0,
  "Only statement 1 is correct. The Ladakh Autonomous Hill Development Councils were set up under a law of 1995 -- first for Leh, then for Kargil in 2003 -- with powers over local planning, land use and development, and they continue under the Union Territory created in 2019, which has no legislature. "
  "Statement 2 is wrong: the Sixth Schedule applies only to tribal areas of Assam, Meghalaya, Tripura and Mizoram. Groups in Ladakh, where most people belong to Scheduled Tribes, have campaigned for Sixth Schedule status and for statehood, arguing that the hill councils lack the legislative powers that district councils under that Schedule enjoy.",
  "केवल कथन 1 सही है। लद्दाख स्वायत्त पहाड़ी विकास परिषदें 1995 के एक क़ानून के अंतर्गत बनीं -- पहले लेह के लिए, फिर 2003 में कारगिल के लिए -- जिनके पास स्थानीय योजना, भूमि उपयोग और विकास की शक्तियाँ हैं, और वे 2019 में बने बिना विधानमंडल वाले केंद्रशासित प्रदेश के अंतर्गत बनी हुई हैं। "
  "कथन 2 ग़लत है: छठी अनुसूची केवल असम, मेघालय, त्रिपुरा और मिज़ोरम के जनजातीय क्षेत्रों पर लागू होती है। लद्दाख के समूह, जहाँ अधिकांश लोग अनुसूचित जनजातियों के हैं, छठी अनुसूची के दर्जे और राज्य के दर्जे के लिए आंदोलन करते रहे हैं, यह तर्क देते हुए कि पहाड़ी परिषदों के पास उस अनुसूची की ज़िला परिषदों जैसी विधायी शक्तियाँ नहीं हैं।",
  f"Ladakh Autonomous Hill Development Council Act, 1995; Jammu and Kashmir Reorganisation Act, 2019; {COI}, Article 244(2) and Sixth Schedule.",
  "l3-t3-pol-ladakh-hill-councils", craft="linkage")

# ---------------------------------------------------------------- Constitutional Framework (h-stmt, m-stmt)
S("Constitutional Framework", "hard", "With reference to Article 35 of the Constitution, consider the following statements:",
  "संविधान के अनुच्छेद 35 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It gives Parliament, and not the State legislatures, the power to make laws prescribing punishment for acts declared to be offences under Part III, such as the practice of untouchability.",
   "Under this power Parliament has enacted laws that punish the practice of untouchability.",
   "A State legislature may also enact its own law prescribing punishment for the practice of untouchability."],
  ["यह राज्य विधानमंडलों को नहीं, बल्कि संसद को भाग III के अंतर्गत अपराध घोषित कृत्यों, जैसे अस्पृश्यता के आचरण, के लिए दंड निर्धारित करने वाले क़ानून बनाने की शक्ति देता है।",
   "इस शक्ति के अंतर्गत संसद ने अस्पृश्यता के आचरण को दंडित करने वाले क़ानून बनाए हैं।",
   "कोई राज्य विधानमंडल भी अस्पृश्यता के आचरण के लिए दंड निर्धारित करने वाला अपना क़ानून बना सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Article 35 reserves to Parliament the power to legislate on certain fundamental-rights matters -- prescribing punishments for offences under Part III (Article 17 on untouchability and Article 23 on forced labour, for instance), and laws under Articles 16(3), 32(3), 33 and 34 -- so that these rules are uniform across the country. "
  "Parliament has used it for the Untouchability (Offences) Act, 1955, later renamed the Protection of Civil Rights Act. Statement 3 is wrong: the power is exclusive, so a State law prescribing punishment for untouchability would be beyond the State's competence, whatever the Seventh Schedule lists say.",
  "कथन 1 और 2 सही हैं। अनुच्छेद 35 कुछ मौलिक-अधिकार विषयों पर क़ानून बनाने की शक्ति संसद के लिए आरक्षित करता है -- भाग III के अपराधों (जैसे अस्पृश्यता पर अनुच्छेद 17 और बलात् श्रम पर अनुच्छेद 23) के लिए दंड निर्धारित करना, और अनुच्छेद 16(3), 32(3), 33 और 34 के अंतर्गत क़ानून -- ताकि ये नियम पूरे देश में एक समान हों। "
  "संसद ने इसका उपयोग अस्पृश्यता (अपराध) अधिनियम, 1955 के लिए किया, जिसका नाम बाद में सिविल अधिकार संरक्षण अधिनियम हुआ। कथन 3 ग़लत है: यह शक्ति अनन्य है, इसलिए अस्पृश्यता के लिए दंड निर्धारित करने वाला राज्य क़ानून राज्य की क्षमता से बाहर होगा, सातवीं अनुसूची की सूचियाँ चाहे जो कहें।",
  f"{COI}, Articles 17, 23 and 35.",
  "l3-t3-pol-art35-parliament-exclusive", craft="inference")

S("Constitutional Framework", "medium", "Consider the following statements about the lists of Scheduled Castes and Scheduled Tribes:",
  "अनुसूचित जातियों और अनुसूचित जनजातियों की सूचियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The President, after consulting the Governor, specifies by public notification the Scheduled Castes and Scheduled Tribes of each State.",
   "Once such a notification has been issued, a community can be added to or removed from the list only by a law of Parliament.",
   "A State legislature may add a community to the Scheduled Tribes list of that State by its own law."],
  ["राष्ट्रपति, राज्यपाल से परामर्श के बाद, सार्वजनिक अधिसूचना द्वारा हर राज्य की अनुसूचित जातियाँ और अनुसूचित जनजातियाँ निर्दिष्ट करते हैं।",
   "ऐसी अधिसूचना जारी होने के बाद किसी समुदाय को सूची में केवल संसद के क़ानून द्वारा जोड़ा या उससे हटाया जा सकता है।",
   "कोई राज्य विधानमंडल अपने क़ानून द्वारा उस राज्य की अनुसूचित जनजाति सूची में किसी समुदाय को जोड़ सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under Articles 341 and 342 the first lists were notified by presidential orders in 1950; after that, clause (2) of each Article lets only Parliament include or exclude communities, which is why changes come through Constitution (Scheduled Tribes) Order (Amendment) Acts for particular States. "
  "Statement 3 is wrong: a State cannot alter the lists, though it may recommend changes, which are examined by the Registrar General and the national commissions before Parliament acts. The courts, too, have held that they cannot add to or subtract from the lists.",
  "कथन 1 और 2 सही हैं। अनुच्छेद 341 और 342 के अंतर्गत पहली सूचियाँ 1950 में राष्ट्रपति के आदेशों से अधिसूचित हुईं; उसके बाद हर अनुच्छेद का खंड (2) केवल संसद को समुदायों को शामिल करने या बाहर करने देता है, इसीलिए परिवर्तन विशेष राज्यों के लिए संविधान (अनुसूचित जनजातियाँ) आदेश (संशोधन) अधिनियमों से आते हैं। "
  "कथन 3 ग़लत है: राज्य सूचियाँ नहीं बदल सकता, यद्यपि वह परिवर्तनों की सिफ़ारिश कर सकता है, जिनकी जाँच संसद के क़दम उठाने से पहले महापंजीयक और राष्ट्रीय आयोग करते हैं। न्यायालयों ने भी माना है कि वे सूचियों में कुछ जोड़ या घटा नहीं सकते।",
  f"{COI}, Articles 341 and 342.",
  "l3-t3-pol-art341-342-lists", craft="precision")

# ---------------------------------------------------------------- Parliament & State Legislature (h-stmt, m-MCQ, m-stmt)
S("Parliament & State Legislature", "hard", "Consider the following statements about the Supreme Court's decisions of 2020 in the Keisham Meghachandra Singh case:",
  "कीशम मेघचंद्र सिंह मामले में सर्वोच्च न्यायालय के 2020 के निर्णयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Court said that a Speaker should ordinarily decide a disqualification petition under the Tenth Schedule within three months.",
   "The Court suggested that Parliament consider entrusting such decisions to an independent tribunal instead of the Speaker.",
   "When the petition against a Manipur minister remained undecided, the Court used Article 142 to bar him from entering the Assembly until further orders."],
  ["न्यायालय ने कहा कि अध्यक्ष को सामान्यतः दसवीं अनुसूची के अंतर्गत निरर्हता याचिका का निर्णय तीन महीने के भीतर करना चाहिए।",
   "न्यायालय ने सुझाव दिया कि संसद ऐसे निर्णय अध्यक्ष के बजाय किसी स्वतंत्र अधिकरण को सौंपने पर विचार करे।",
   "जब मणिपुर के एक मंत्री के विरुद्ध याचिका अनिर्णीत रही, तो न्यायालय ने अनुच्छेद 142 का प्रयोग कर उन्हें अगले आदेश तक विधानसभा में प्रवेश से रोक दिया।"],
  C3, 2,
  "All three statements are correct. The Tenth Schedule sets no deadline, and Speakers had sat on petitions against defectors who had joined the ruling side; in January 2020 the Court read in a 'reasonable period' of three months, absent exceptional circumstances, and asked Parliament to think about a permanent tribunal or another independent mechanism. "
  "In March 2020, with the Manipur Speaker still not deciding, the Court invoked its power to do 'complete justice' under Article 142 to restrain the minister from the Assembly -- an unusual step that shows how far the Court has gone since Kihoto Hollohan (1992), which made the Speaker's decisions open to judicial review.",
  "तीनों कथन सही हैं। दसवीं अनुसूची कोई समय-सीमा तय नहीं करती, और अध्यक्ष सत्तारूढ़ पक्ष में शामिल हुए दलबदलुओं के विरुद्ध याचिकाओं को लटकाए रहे थे; जनवरी 2020 में न्यायालय ने असाधारण परिस्थितियों के अभाव में तीन महीने की 'युक्तियुक्त अवधि' पढ़ी, और संसद से स्थायी अधिकरण या किसी अन्य स्वतंत्र तंत्र पर विचार करने को कहा। "
  "मार्च 2020 में, जब मणिपुर के अध्यक्ष ने तब भी निर्णय नहीं किया, न्यायालय ने अनुच्छेद 142 के अंतर्गत 'पूर्ण न्याय' करने की अपनी शक्ति का प्रयोग कर मंत्री को विधानसभा से रोक दिया -- यह असामान्य क़दम दिखाता है कि किहोतो होलोहन (1992), जिसने अध्यक्ष के निर्णयों को न्यायिक पुनर्विलोकन के अधीन किया, के बाद से न्यायालय कितना आगे गया है।",
  f"{SC}: Keisham Meghachandra Singh v. Speaker, Manipur Legislative Assembly (2020); {COI}, Tenth Schedule and Article 142.",
  "l3-t3-pol-meghachandra-speaker-deadline", craft="linkage")

M("Parliament & State Legislature", "medium",
  "In the Lok Sabha, who may order that words used in a debate which are defamatory, indecent, unparliamentary or undignified be expunged from the proceedings?",
  "लोकसभा में बहस के दौरान प्रयुक्त मानहानिकारक, अशोभनीय, असंसदीय या गरिमाहीन शब्दों को कार्यवाही से निकाल देने का आदेश कौन दे सकता है?",
  ["The Committee of Privileges, after an inquiry into the remarks",
   "The Leader of the House, in consultation with the Leader of the Opposition",
   "The Supreme Court, on a petition by the person defamed",
   "The Speaker, under the Rules of Procedure of the House"],
  ["विशेषाधिकार समिति, टिप्पणियों की जाँच के बाद",
   "सदन के नेता, विपक्ष के नेता से परामर्श करके",
   "सर्वोच्च न्यायालय, मानहानि झेलने वाले व्यक्ति की याचिका पर",
   "अध्यक्ष, सदन के प्रक्रिया नियमों के अंतर्गत"],
  3,
  "Rule 380 of the Lok Sabha's Rules of Procedure lets the Speaker, in the Speaker's discretion, order the expunction of such words; the Rajya Sabha's Chairman has a similar power, and the Lok Sabha Secretariat compiles lists of expressions ruled unparliamentary over the years. "
  "Expunged words disappear from the official record, and reporting them is not protected. Courts do not step in, since Article 122 bars them from inquiring into the validity of Parliament's proceedings, and Article 105 shields members from court proceedings for what they say in the House.",
  "लोकसभा के प्रक्रिया नियमों का नियम 380 अध्यक्ष को अपने विवेक से ऐसे शब्दों को निकालने का आदेश देने देता है; राज्यसभा के सभापति के पास भी ऐसी ही शक्ति है, और लोकसभा सचिवालय वर्षों में असंसदीय ठहराई गई अभिव्यक्तियों की सूचियाँ संकलित करता है। "
  "निकाले गए शब्द आधिकारिक रिकॉर्ड से हट जाते हैं, और उनकी रिपोर्टिंग संरक्षित नहीं होती। न्यायालय हस्तक्षेप नहीं करते, क्योंकि अनुच्छेद 122 उन्हें संसद की कार्यवाही की वैधता की जाँच से रोकता है, और अनुच्छेद 105 सदस्यों को सदन में कही गई बातों के लिए न्यायालयी कार्यवाही से बचाता है।",
  f"Rules of Procedure and Conduct of Business in Lok Sabha, Rule 380; {COI}, Articles 105 and 122.",
  "l3-t3-pol-expunction-rule-380", pos=3, craft="precision")

S("Parliament & State Legislature", "medium", "Consider the following statements about the salaries of Members of Parliament:",
  "संसद सदस्यों के वेतन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are fixed by the President on the recommendation of the Central Pay Commission.",
   "They can be changed only by an amendment of the Constitution."],
  ["इन्हें केंद्रीय वेतन आयोग की सिफ़ारिश पर राष्ट्रपति तय करते हैं।",
   "इन्हें केवल संविधान संशोधन द्वारा बदला जा सकता है।"],
  T2, 3,
  "Neither statement is correct. Article 106 lets Parliament fix members' salaries and allowances by law, which it does through the Salary, Allowances and Pension of Members of Parliament Act, 1954, an ordinary law amended by simple majority. "
  "Because MPs voting on their own pay drew criticism, the Finance Act, 2018 provided for automatic revision every five years in line with the cost inflation index. The Pay Commissions deal with government employees, not legislators.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 106 संसद को क़ानून द्वारा सदस्यों के वेतन और भत्ते तय करने देता है, जो वह संसद सदस्य वेतन, भत्ता और पेंशन अधिनियम, 1954 के माध्यम से करती है, जो साधारण बहुमत से संशोधित होने वाला सामान्य क़ानून है। "
  "चूँकि सांसदों द्वारा अपने ही वेतन पर मतदान की आलोचना होती थी, वित्त अधिनियम, 2018 ने लागत मुद्रास्फीति सूचकांक के अनुरूप हर पाँच वर्ष में स्वचालित संशोधन का उपबंध किया। वेतन आयोग सरकारी कर्मचारियों से संबंधित हैं, विधायकों से नहीं।",
  f"{COI}, Article 106; Salary, Allowances and Pension of Members of Parliament Act, 1954; Finance Act, 2018.",
  "l3-t3-pol-mp-salaries-art106", craft="precision")

# ---------------------------------------------------------------- Constitutional & Statutory Bodies (h-SI)
A("Constitutional & Statutory Bodies", "hard",
  "The recommendations of the National Statistical Commission are not binding on the government.",
  "राष्ट्रीय सांख्यिकी आयोग की सिफ़ारिशें सरकार पर बाध्यकारी नहीं हैं।",
  "The National Statistical Commission was set up in 2005 by an executive resolution, not by an Act of Parliament.",
  "राष्ट्रीय सांख्यिकी आयोग 2005 में संसद के अधिनियम से नहीं, बल्कि एक कार्यकारी संकल्प द्वारा स्थापित किया गया।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Commission was created on the recommendation of the Rangarajan Commission to act as the apex body setting priorities and standards for official statistics, but because it rests only on a government resolution it has no legal power to compel ministries to follow its advice. "
  "Its weakness was exposed in 2019, when two members resigned over the delay in releasing a labour force survey they had approved. A bill to give the Commission statutory status has been discussed but not enacted; the Chief Statistician of India serves as its Secretary.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। आयोग रंगराजन आयोग की सिफ़ारिश पर आधिकारिक सांख्यिकी की प्राथमिकताएँ और मानक तय करने वाली शीर्ष संस्था के रूप में बना, पर चूँकि वह केवल एक सरकारी संकल्प पर टिका है, उसके पास मंत्रालयों को अपनी सलाह मानने के लिए बाध्य करने की कोई विधिक शक्ति नहीं है। "
  "इसकी कमज़ोरी 2019 में उजागर हुई, जब दो सदस्यों ने उनके द्वारा स्वीकृत श्रम बल सर्वेक्षण को जारी करने में देरी पर त्यागपत्र दिया। आयोग को वैधानिक दर्जा देने वाले विधेयक पर चर्चा हुई है पर वह पारित नहीं हुआ; भारत के मुख्य सांख्यिकीविद् इसके सचिव हैं।",
  "Ministry of Statistics and Programme Implementation (resolution constituting the National Statistical Commission, 2005).",
  "l3-t3-pol-national-statistical-commission", craft="inference")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (h-SI)
A("Panchayati Raj & Local Governance", "hard",
  "Before reserving seats for Other Backward Classes in local bodies, a State must satisfy the 'triple test' laid down by the Supreme Court.",
  "स्थानीय निकायों में अन्य पिछड़े वर्गों के लिए सीटें आरक्षित करने से पहले राज्य को सर्वोच्च न्यायालय द्वारा तय 'त्रिस्तरीय परीक्षण' पूरा करना होता है।",
  "The triple test requires a dedicated commission to study backwardness, the fixing of reservation local body-wise on that basis, and a ceiling of 50 per cent on total reservation.",
  "त्रिस्तरीय परीक्षण में पिछड़ेपन के अध्ययन के लिए एक समर्पित आयोग, उसके आधार पर स्थानीय निकाय-वार आरक्षण तय करना और कुल आरक्षण पर 50 प्रतिशत की सीमा आवश्यक है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Statement-II describes what the test contains; the reason States must meet it lies in the Court's view, from K. Krishna Murthy (2010) onwards, that political backwardness in local bodies is not the same as the social and educational backwardness used for jobs and education, so it must be shown with fresh, local data. "
  "In Vikas Kishanrao Gawali (2021) the Court struck down OBC quotas in Maharashtra's local bodies that had not met the test, and in 2022 it told States not to hold back local elections indefinitely while they did so.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। कथन-II बताता है कि परीक्षण में क्या है; राज्यों को इसे पूरा क्यों करना होता है, इसका कारण न्यायालय का के. कृष्णमूर्ति (2010) से चला आ रहा यह मत है कि स्थानीय निकायों में राजनीतिक पिछड़ापन नौकरियों और शिक्षा के लिए प्रयुक्त सामाजिक और शैक्षिक पिछड़ेपन जैसा नहीं है, इसलिए उसे ताज़ा, स्थानीय आँकड़ों से सिद्ध करना होगा। "
  "विकास किशनराव गवली (2021) में न्यायालय ने महाराष्ट्र के स्थानीय निकायों में उन OBC कोटों को रद्द किया जिन्होंने परीक्षण पूरा नहीं किया था, और 2022 में उसने राज्यों से कहा कि ऐसा करते हुए वे स्थानीय चुनाव अनिश्चित काल तक न रोकें।",
  f"{SC}: K. Krishna Murthy v. Union of India (2010); Vikas Kishanrao Gawali v. State of Maharashtra (2021); {COI}, Article 243D(6).",
  "l3-t3-pol-obc-triple-test-local-bodies", craft="inference")

# ---------------------------------------------------------------- Governance (m-MCQ, m-stmt)
M("Governance", "medium",
  "The Tele-Law programme of the Department of Justice connects people in rural areas with:",
  "न्याय विभाग का टेली-लॉ कार्यक्रम ग्रामीण क्षेत्रों के लोगों को किससे जोड़ता है?",
  ["lawyers who give pre-litigation advice by video or phone at Common Service Centres",
   "judges who decide small civil disputes online, in place of the district courts",
   "police stations, so that first information reports can be lodged over the telephone",
   "a national database showing the status of every case pending in the High Courts"],
  ["उन वकीलों से जो कॉमन सर्विस सेंटरों पर वीडियो या फ़ोन से मुक़दमे से पहले सलाह देते हैं",
   "उन न्यायाधीशों से जो ज़िला न्यायालयों के स्थान पर छोटे दीवानी विवादों का ऑनलाइन निर्णय करते हैं",
   "पुलिस थानों से, ताकि प्रथम सूचना रिपोर्ट टेलीफ़ोन पर दर्ज कराई जा सके",
   "एक राष्ट्रीय डेटाबेस से जो उच्च न्यायालयों में लंबित हर मामले की स्थिति दिखाता है"],
  0,
  "Tele-Law, begun in 2017 and now part of the DISHA scheme, places a village-level entrepreneur at a Common Service Centre who links a person with a panel lawyer for advice by video conference or phone; it is free for those entitled to legal aid under the Legal Services Authorities Act, 1987. "
  "The aim is pre-litigation advice -- helping people understand their rights and settle problems early -- rather than adjudication. The last option describes the National Judicial Data Grid.",
  "2017 में शुरू हुआ और अब दिशा योजना का अंग टेली-लॉ कॉमन सर्विस सेंटर पर एक ग्राम-स्तरीय उद्यमी रखता है जो व्यक्ति को वीडियो कॉन्फ़्रेंस या फ़ोन पर सलाह के लिए पैनल वकील से जोड़ता है; यह विधिक सेवा प्राधिकरण अधिनियम, 1987 के अंतर्गत विधिक सहायता के हक़दार लोगों के लिए निःशुल्क है। "
  "उद्देश्य न्याय-निर्णय नहीं, मुक़दमे से पहले की सलाह है -- लोगों को अपने अधिकार समझने और समस्याएँ जल्दी सुलझाने में मदद करना। अंतिम विकल्प राष्ट्रीय न्यायिक डेटा ग्रिड का वर्णन है।",
  "Ministry of Law and Justice, Department of Justice (Tele-Law; DISHA scheme).",
  "l3-t3-pol-tele-law", pos=0, craft="precision")

S("Governance", "medium", "Consider the following statements about the Aspirational Blocks Programme:",
  "आकांक्षी ब्लॉक कार्यक्रम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Launched in 2023, it covers about 500 blocks and is anchored by NITI Aayog.",
   "It ranks blocks only on the amount of central funds that they spend in a year."],
  ["2023 में शुरू हुआ यह कार्यक्रम लगभग 500 ब्लॉकों को शामिल करता है और नीति आयोग इसका आधार है।",
   "यह ब्लॉकों को केवल इस आधार पर श्रेणीबद्ध करता है कि वे एक वर्ष में कितनी केंद्रीय निधि ख़र्च करते हैं।"],
  T2, 0,
  "Only statement 1 is correct. The programme extends the approach of the Aspirational Districts Programme to the block level, picking blocks that lag on basic services. "
  "Statement 2 is wrong: blocks are ranked on their improvement in key outcome indicators -- health and nutrition, education, agriculture and water resources, basic infrastructure and social development -- with regular 'delta' rankings that set blocks to compete with one another. Its tools are convergence of existing schemes and closer monitoring, not a new pot of money.",
  "केवल कथन 1 सही है। यह कार्यक्रम आकांक्षी ज़िला कार्यक्रम के तरीक़े को ब्लॉक स्तर तक ले जाता है, उन ब्लॉकों को चुनते हुए जो बुनियादी सेवाओं में पीछे हैं। "
  "कथन 2 ग़लत है: ब्लॉकों को प्रमुख परिणाम संकेतकों -- स्वास्थ्य और पोषण, शिक्षा, कृषि और जल संसाधन, बुनियादी अवसंरचना और सामाजिक विकास -- में उनके सुधार पर श्रेणीबद्ध किया जाता है, नियमित 'डेल्टा' रैंकिंग के साथ जो ब्लॉकों को आपस में प्रतिस्पर्धा कराती है। इसके साधन मौजूदा योजनाओं का अभिसरण और निकट निगरानी हैं, कोई नई निधि नहीं।",
  "NITI Aayog (Aspirational Blocks Programme, 2023).",
  "l3-t3-pol-aspirational-blocks", craft="precision")

# ---------------------------------------------------------------- Statutory-Laws (m-stmt)
S("Statutory-Laws", "medium", "With reference to the Fugitive Economic Offenders Act, 2018, consider the following statements:",
  "भगोड़ा आर्थिक अपराधी अधिनियम, 2018 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A 'fugitive economic offender' is a person against whom an arrest warrant has been issued for a scheduled offence involving ₹100 crore or more and who has left India or refuses to return to face prosecution.",
   "A Special Court can order the confiscation of such a person's property only after the person has been convicted by a criminal court.",
   "The Act applies only to offenders who are citizens of India."],
  ["'भगोड़ा आर्थिक अपराधी' वह व्यक्ति है जिसके विरुद्ध ₹100 करोड़ या अधिक से जुड़े किसी अनुसूचित अपराध के लिए गिरफ़्तारी वारंट जारी हुआ हो और जो अभियोजन से बचने के लिए भारत छोड़ चुका हो या लौटने से इनकार करता हो।",
   "विशेष न्यायालय ऐसे व्यक्ति की संपत्ति ज़ब्त करने का आदेश केवल तभी दे सकता है जब किसी आपराधिक न्यायालय ने उसे दोषी ठहरा दिया हो।",
   "अधिनियम केवल उन अपराधियों पर लागू होता है जो भारत के नागरिक हैं।"],
  C3, 0,
  "Only statement 1 is correct. The Act was passed after several large defaulters left the country; on an application by the Director under the Prevention of Money-laundering Act, a Special Court can declare a person a fugitive economic offender and confiscate the proceeds of crime and other property, including benami property, in India or abroad, and the person can be barred from pursuing or defending civil claims in India. "
  "Statement 2 is wrong: the whole point of the Act is that confiscation does not wait for a conviction, which could never come while the accused stays abroad. Statement 3 is wrong: the Act applies to any individual who meets the definition, whatever the nationality. It aims to make fleeing costly rather than to replace criminal trial, which continues if the person returns or is extradited.",
  "केवल कथन 1 सही है। यह अधिनियम कई बड़े चूककर्ताओं के देश छोड़ने के बाद पारित हुआ; धन-शोधन निवारण अधिनियम के अंतर्गत निदेशक के आवेदन पर विशेष न्यायालय किसी व्यक्ति को भगोड़ा आर्थिक अपराधी घोषित कर भारत या विदेश में अपराध की आय और बेनामी संपत्ति सहित अन्य संपत्ति ज़ब्त कर सकता है, और उस व्यक्ति को भारत में दीवानी दावे करने या उनका बचाव करने से रोका जा सकता है। "
  "कथन 2 ग़लत है: अधिनियम का पूरा उद्देश्य यही है कि ज़ब्ती दोषसिद्धि की प्रतीक्षा नहीं करती, जो अभियुक्त के विदेश में रहते कभी हो ही नहीं सकती। कथन 3 ग़लत है: अधिनियम परिभाषा पर खरे उतरने वाले किसी भी व्यक्ति पर, उसकी राष्ट्रीयता चाहे जो हो, लागू होता है। इसका उद्देश्य आपराधिक मुक़दमे का स्थान लेना नहीं, भागने को महँगा बनाना है; व्यक्ति के लौटने या प्रत्यर्पित होने पर मुक़दमा चलता है।",
  "Fugitive Economic Offenders Act, 2018; Prevention of Money-laundering Act, 2002.",
  "l3-t3-pol-fugitive-economic-offenders-act", craft="precision")

# ---------------------------------------------------------------- Union & State Executive (m-stmt)
S("Union & State Executive", "medium", "Consider the following statements about a vacancy in the office of the President caused by death or resignation:",
  "मृत्यु या त्यागपत्र से राष्ट्रपति के पद में हुई रिक्ति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["An election to fill the vacancy may be held at any time within one year.",
   "Until a new President takes office, the Chief Justice of India acts as President.",
   "A President elected to fill the vacancy holds office only for the rest of the predecessor's term."],
  ["रिक्ति भरने के लिए चुनाव एक वर्ष के भीतर कभी भी कराया जा सकता है।",
   "नए राष्ट्रपति के पद ग्रहण करने तक भारत के मुख्य न्यायाधीश राष्ट्रपति के रूप में कार्य करते हैं।",
   "रिक्ति भरने के लिए चुने गए राष्ट्रपति केवल पूर्ववर्ती के शेष कार्यकाल के लिए पद धारण करते हैं।"],
  C3, 3,
  "None of the statements is correct. Article 62(2) requires the election to be held as soon as possible and in no case later than six months from the date of the vacancy. "
  "Meanwhile, under Article 65, the Vice-President acts as President; the Chief Justice of India steps in only if the Vice-President's office is also vacant, as happened briefly in 1969. "
  "And the newly elected President serves a full term of five years from the date of entering office, not the remainder of the old term -- unlike some offices, such as a member elected to fill a casual vacancy in the Rajya Sabha.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 62(2) अपेक्षा करता है कि चुनाव यथाशीघ्र और किसी भी स्थिति में रिक्ति की तिथि से छह महीने के भीतर हो। "
  "इस बीच अनुच्छेद 65 के अंतर्गत उपराष्ट्रपति राष्ट्रपति के रूप में कार्य करते हैं; भारत के मुख्य न्यायाधीश तभी आगे आते हैं जब उपराष्ट्रपति का पद भी रिक्त हो, जैसा 1969 में थोड़े समय के लिए हुआ। "
  "और नए चुने गए राष्ट्रपति पद ग्रहण की तिथि से पाँच वर्ष का पूरा कार्यकाल पाते हैं, पुराने कार्यकाल का शेष भाग नहीं -- कुछ पदों के विपरीत, जैसे राज्यसभा में आकस्मिक रिक्ति भरने के लिए चुना गया सदस्य।",
  f"{COI}, Articles 62 and 65; President (Discharge of Functions) Act, 1969.",
  "l3-t3-pol-president-vacancy-art62-65", craft="precision")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (m-stmt)
S("Fundamental Rights, DPSP & Duties", "medium", "Consider the following statements about the freedom of profession, trade and business:",
  "वृत्ति, व्यापार और कारोबार की स्वतंत्रता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 19(6) permits the State to carry on any trade or business to the complete or partial exclusion of citizens.",
   "The right under Article 19(1)(g) to practise any profession is available only to citizens.",
   "The State may prescribe professional or technical qualifications for practising a profession or carrying on a trade."],
  ["अनुच्छेद 19(6) राज्य को नागरिकों को पूर्णतः या अंशतः बाहर रखकर कोई भी व्यापार या कारोबार चलाने की अनुमति देता है।",
   "अनुच्छेद 19(1)(g) के अंतर्गत कोई भी वृत्ति करने का अधिकार केवल नागरिकों को उपलब्ध है।",
   "राज्य किसी वृत्ति को करने या व्यापार चलाने के लिए वृत्तिक या तकनीकी योग्यताएँ निर्धारित कर सकता है।"],
  C3, 2,
  "All three statements are correct. Clause (6), amended by the First Amendment in 1951, protects laws that set professional or technical qualifications and laws under which the State runs a trade, industry or service as a monopoly -- which is how nationalisation of banks, insurance and road transport routes survived challenge. "
  "Like the other freedoms in Article 19, this right belongs to citizens only; foreigners and companies as such cannot claim it, though shareholders who are citizens may. Reasonable restrictions in the interests of the general public are also allowed.",
  "तीनों कथन सही हैं। 1951 के पहले संशोधन द्वारा संशोधित खंड (6) उन क़ानूनों की रक्षा करता है जो वृत्तिक या तकनीकी योग्यताएँ तय करते हैं और जिनके अंतर्गत राज्य किसी व्यापार, उद्योग या सेवा को एकाधिकार के रूप में चलाता है -- इसी से बैंकों, बीमा और सड़क परिवहन मार्गों का राष्ट्रीयकरण चुनौतियों से बचा। "
  "अनुच्छेद 19 की अन्य स्वतंत्रताओं की तरह यह अधिकार केवल नागरिकों का है; विदेशी और कंपनियाँ स्वयं इसका दावा नहीं कर सकतीं, यद्यपि नागरिक शेयरधारक कर सकते हैं। आम जनता के हित में युक्तियुक्त प्रतिबंध भी अनुमत हैं।",
  f"{COI}, Article 19(1)(g) and 19(6); Constitution (First Amendment) Act, 1951.",
  "l3-t3-pol-art19-6-state-monopoly", craft="linkage")

write("gs_l3_t3_a.sql")
