# -*- coding: utf-8 -*-
"""Current Affairs · Test 2 (April to June 2026) -- part H: Current Affairs (national, international, defence,
indices, sports and awards; the second half of the subject).

Events of April-June 2026: the new chiefs of the armed forces, the US-Iran 'Islamabad memorandum', SIPRI's
military-expenditure data, the Global Peace Index and the IMD competitiveness ranking, the G7 at Evian, CISF and the
fishing harbours, the Abhigyan app, the JANANI platform, the State elections and Assam's first poll on its new
constituencies, the UN elections of June, NFHS-6, ESIC's health check for workers, DRDO's tests, the Indus Waters
pondage award, the Kailash Manasarovar Yatra, Kerala's department for senior citizens, the Women's T20 World Cup,
International Day of Yoga, Samadhan Didi and the Goldman Prize. Every fact was searched in the whole UPSC bank and is
one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t2_format import FORMAT, POS

d.SUBJECT = "Current Affairs"
d.REQUIRE_CRAFT = True
IN, NA, DF, SC, SP = "International", "National", "Defence", "Schemes & Indices", "Sports"

# ================================================================ DEFENCE
S(DF, "medium", "In May-June 2026 India got a new Chief of Defence Staff, a new Chief of the Naval Staff and a new Chief of the Army Staff. Consider the following statements:",
  "मई-जून 2026 में भारत को नया चीफ़ ऑफ़ डिफ़ेंस स्टाफ़, नया नौसेनाध्यक्ष और नया थलसेनाध्यक्ष मिला। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The new Chief of Defence Staff was appointed after retiring from the Army, which the rules have permitted since 2022.",
   "General Dhiraj Seth took over as Chief of the Army Staff from General Anil Chauhan.",
   "A Chief of Defence Staff can hold office only until the age of 62, like the service chiefs."],
  ["नए चीफ़ ऑफ़ डिफ़ेंस स्टाफ़ सेना से सेवानिवृत्त होने के बाद नियुक्त हुए, जिसकी अनुमति नियम 2022 से देते हैं।",
   "जनरल धीरज सेठ ने जनरल अनिल चौहान से थलसेनाध्यक्ष का पद संभाला।",
   "चीफ़ ऑफ़ डिफ़ेंस स्टाफ़ सेनाध्यक्षों की तरह केवल 62 वर्ष की आयु तक पद पर रह सकते हैं।"],
  C3, 0,
  "Only statement 1 is correct. Lt Gen N.S. Raja Subramani (retd), earlier Vice Chief of the Army Staff and Military Adviser in the National Security Council Secretariat, succeeded Gen Anil Chauhan at the end of May 2026 as the third CDS; rules amended in 2022 let serving or retired Lieutenant Generals, Air Marshals and Vice Admirals below 62 be appointed. "
  "Statement 2 is wrong: General Dhiraj Seth, who took over the Army on 30 June 2026, succeeded General Upendra Dwivedi; General Anil Chauhan was the outgoing CDS. Admiral Krishna Swaminathan became the 27th Chief of the Naval Staff on 31 May. "
  "Statement 3 is wrong: the CDS may serve until the age of 65, while the three service chiefs serve until 62 or for three years, whichever is earlier.",
  "केवल कथन 1 सही है। पहले थलसेना के उप-प्रमुख और राष्ट्रीय सुरक्षा परिषद सचिवालय में सैन्य सलाहकार रहे लेफ़्टिनेंट जनरल एन.एस. राजा सुब्रमणि (सेवानिवृत्त) मई 2026 के अंत में जनरल अनिल चौहान के बाद तीसरे सीडीएस बने; 2022 में संशोधित नियम 62 वर्ष से कम आयु के सेवारत या सेवानिवृत्त लेफ़्टिनेंट जनरल, एयर मार्शल और वाइस एडमिरल की नियुक्ति की अनुमति देते हैं। "
  "कथन 2 ग़लत है: 30 जून 2026 को थलसेना की कमान संभालने वाले जनरल धीरज सेठ जनरल उपेंद्र द्विवेदी के उत्तराधिकारी बने; जनरल अनिल चौहान निवर्तमान सीडीएस थे। एडमिरल कृष्ण स्वामीनाथन 31 मई को 27वें नौसेनाध्यक्ष बने। "
  "कथन 3 ग़लत है: सीडीएस 65 वर्ष की आयु तक सेवा कर सकते हैं, जबकि तीनों सेनाध्यक्ष 62 वर्ष तक या तीन वर्ष के लिए, जो पहले हो, पद पर रहते हैं।",
  "Ministry of Defence and PIB, appointments of the Chief of Defence Staff and the Chief of the Naval Staff (May 2026) and of the Chief of the Army Staff (June 2026); Ministry of Defence, amendments to the eligibility rules for the CDS (June 2022).",
  "ca-t2-ca-cds-retired-eligible-65-new-chiefs", craft="precision")

S(DF, "medium", "In June 2026 DRDO flight-tested RudraM-II and the Long Range Land Attack Cruise Missile (LRLACM). Consider the following statements:",
  "जून 2026 में डीआरडीओ ने रुद्रम-II और लॉन्ग रेंज लैंड अटैक क्रूज़ मिसाइल (एलआरएलएसीएम) का उड़ान परीक्षण किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["RudraM-II is a surface-to-air missile meant to shoot down hostile aircraft.",
   "The LRLACM is a cruise missile meant to strike targets on land at long range.",
   "Both missiles were developed by the Indo-Russian BrahMos joint venture."],
  ["रुद्रम-II शत्रु विमानों को मार गिराने के लिए बनी सतह-से-हवा मिसाइल है।",
   "एलआरएलएसीएम लंबी दूरी पर स्थल लक्ष्यों पर प्रहार के लिए बनी क्रूज़ मिसाइल है।",
   "दोनों मिसाइलें भारत-रूस संयुक्त उद्यम ब्रह्मोस ने विकसित कीं।"],
  C3, 0,
  "Only statement 2 is correct. The LRLACM, tested from Dr APJ Abdul Kalam Island on 15 June, is an indigenous subsonic cruise missile that flies low, close to the ground, to strike land targets far inside enemy territory. "
  "Statement 1 is wrong: RudraM-II, tested with the Air Force at the Integrated Test Range at Chandipur in early June 2026, is an air-to-surface missile -- launched from a fighter to strike ground targets, including enemy radars and air defences -- not a surface-to-air one. In the same weeks DRDO also tested an Advanced Agni missile and a multi-layered ballistic missile defence. "
  "Statement 3 is wrong: both are DRDO's own designs; BrahMos Aerospace, the joint venture with Russia, builds the supersonic BrahMos cruise missile.",
  "केवल कथन 2 सही है। 15 जून को डॉ. एपीजे अब्दुल कलाम द्वीप से परखी गई एलआरएलएसीएम स्वदेशी अवध्वनिक क्रूज़ मिसाइल है जो शत्रु क्षेत्र में दूर तक स्थल लक्ष्यों पर प्रहार के लिए धरती के पास, नीची उड़ान भरती है। "
  "कथन 1 ग़लत है: जून 2026 के आरंभ में वायुसेना के साथ चांदीपुर के एकीकृत परीक्षण रेंज में परखी गई रुद्रम-II हवा-से-सतह मिसाइल है -- जिसे लड़ाकू विमान से शत्रु के राडार और वायु-रक्षा सहित भूमि लक्ष्यों पर प्रहार के लिए दागा जाता है -- सतह-से-हवा नहीं। उन्हीं सप्ताहों में डीआरडीओ ने एक उन्नत अग्नि मिसाइल और बहुस्तरीय बैलिस्टिक मिसाइल रक्षा का भी परीक्षण किया। "
  "कथन 3 ग़लत है: दोनों डीआरडीओ के अपने डिज़ाइन हैं; रूस के साथ संयुक्त उद्यम ब्रह्मोस एयरोस्पेस पराध्वनिक ब्रह्मोस क्रूज़ मिसाइल बनाता है।",
  "Ministry of Defence and PIB, flight tests of RudraM-II (June 2026) and the Long Range Land Attack Cruise Missile (15 June 2026).",
  "ca-t2-ca-rudram-ii-lrlacm-drdo-not-brahmos", craft="precision")

# ================================================================ INTERNATIONAL
S(IN, "hard", "On 18 June 2026 a US-Iran memorandum of understanding, signed in the wake of talks in Islamabad, entered into force. Consider the following statements:",
  "18 जून 2026 को इस्लामाबाद में हुई वार्ताओं के बाद हस्ताक्षरित एक अमेरिका-ईरान समझौता ज्ञापन लागू हुआ। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pakistan acted as a mediator between the two sides.",
   "It provided for Iran to reopen the Strait of Hormuz and for the United States to lift its naval blockade.",
   "It left the question of Iran's nuclear programme to later negotiations."],
  ["पाकिस्तान ने दोनों पक्षों के बीच मध्यस्थ की भूमिका निभाई।",
   "इसमें ईरान द्वारा होर्मुज़ जलडमरूमध्य फिर खोलने और संयुक्त राज्य अमेरिका द्वारा अपनी नौसैनिक नाकेबंदी हटाने का प्रावधान था।",
   "इसने ईरान के परमाणु कार्यक्रम का प्रश्न बाद की वार्ताओं पर छोड़ दिया।"],
  C3, 2,
  "All three statements are correct. With Pakistan as mediator, the memorandum -- signed electronically by the two Presidents and endorsed by Pakistan -- was to end the confrontation that had shut the Strait of Hormuz: Iran was to reopen the strait and the US to lift its naval blockade, with safe, toll-free passage for 60 days while a final agreement was negotiated. "
  "It was an interim arrangement: the nuclear question was left to later talks, which stalled amid charges of non-implementation. The last comprehensive deal, the Joint Comprehensive Plan of Action of 2015 between Iran and the five permanent members of the Security Council plus Germany, was endorsed by Security Council resolution 2231; the US withdrew from it in 2018.",
  "तीनों कथन सही हैं। पाकिस्तान की मध्यस्थता में समझौता ज्ञापन -- जिस पर दोनों राष्ट्रपतियों ने इलेक्ट्रॉनिक रूप से हस्ताक्षर किए और पाकिस्तान ने समर्थन दिया -- को होर्मुज़ जलडमरूमध्य को बंद करने वाले टकराव का अंत करना था: ईरान को जलडमरूमध्य फिर खोलना और अमेरिका को अपनी नौसैनिक नाकेबंदी हटानी थी, अंतिम समझौते की वार्ता तक 60 दिनों के सुरक्षित, शुल्क-मुक्त आवागमन के साथ। "
  "यह एक अंतरिम व्यवस्था थी: परमाणु प्रश्न बाद की वार्ताओं पर छोड़ा गया, जो क्रियान्वयन न होने के आरोपों के बीच अटक गईं। पिछला व्यापक समझौता, ईरान और सुरक्षा परिषद के पाँच स्थायी सदस्यों तथा जर्मनी के बीच 2015 की संयुक्त व्यापक कार्ययोजना, सुरक्षा परिषद के संकल्प 2231 से समर्थित था; अमेरिका 2018 में उससे अलग हो गया।",
  "Ministry of External Affairs, statements on the West Asia situation (June 2026); United Nations Security Council resolution 2231 (2015).",
  "ca-t2-ca-islamabad-mou-hormuz-interim-jcpoa", craft="linkage")

S(IN, "medium", "From 15 to 17 June 2026 the 52nd G7 summit was held at Evian, France, with India among the invited countries. Consider the following statements:",
  "15 से 17 जून 2026 तक फ़्रांस के एवियाँ में 52वाँ जी7 शिखर सम्मेलन हुआ, जिसमें आमंत्रित देशों में भारत भी था। निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is not a member of the G7 but has repeatedly been invited to its summits.",
   "Russia's participation in the group was suspended in 2014 after it annexed Crimea.",
   "The European Union takes part in the summits, but the presidency rotates only among the seven member countries."],
  ["भारत जी7 का सदस्य नहीं है, पर उसे बार-बार इसके शिखर सम्मेलनों में आमंत्रित किया गया है।",
   "क्रीमिया के विलय के बाद 2014 में समूह में रूस की भागीदारी निलंबित कर दी गई।",
   "यूरोपीय संघ शिखर सम्मेलनों में भाग लेता है, पर अध्यक्षता केवल सात सदस्य देशों में घूमती है।"],
  C3, 2,
  "All three statements are correct. The G7 is the United States, Canada, the United Kingdom, France, Germany, Italy and Japan; the 2026 summit, under the French presidency, was India's thirteenth as an invitee and the Prime Minister's seventh in a row. The group was the G8 from 1997 until Russia was suspended in March 2014 over Crimea. "
  "The European Union takes part in all G7 work as a 'non-enumerated' participant, but it does not hold the presidency, which passes in turn among the seven.",
  "तीनों कथन सही हैं। जी7 में संयुक्त राज्य अमेरिका, कनाडा, यूनाइटेड किंगडम, फ़्रांस, जर्मनी, इटली और जापान हैं; फ़्रांसीसी अध्यक्षता में 2026 का शिखर सम्मेलन आमंत्रित के रूप में भारत का तेरहवाँ और प्रधानमंत्री का लगातार सातवाँ था। समूह 1997 से जी8 था, जब तक मार्च 2014 में क्रीमिया के कारण रूस को निलंबित नहीं किया गया। "
  "यूरोपीय संघ जी7 के सारे कार्य में ‘अगणित’ भागीदार के रूप में शामिल होता है, पर अध्यक्षता उसके पास नहीं आती, जो बारी-बारी से सात देशों में घूमती है।",
  "Ministry of External Affairs, Prime Minister's participation in the G7 Summit at Evian (June 2026); G7 presidency of France, 2026.",
  "ca-t2-ca-g7-evian-india-invitee-russia-2014-eu", craft="precision")

S(IN, "medium", "On 3 June 2026 the UN General Assembly elected five non-permanent members of the Security Council for 2027-2028. Consider the following statements:",
  "3 जून 2026 को संयुक्त राष्ट्र महासभा ने 2027-2028 के लिए सुरक्षा परिषद के पाँच अस्थायी सदस्य चुने। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pakistan's present term on the Council ends in 2026.",
   "A candidate needs only a simple majority of the members present and voting.",
   "Germany was among the countries elected."],
  ["परिषद में पाकिस्तान का वर्तमान कार्यकाल 2026 में समाप्त होता है।",
   "किसी प्रत्याशी को उपस्थित और मत देने वाले सदस्यों का केवल साधारण बहुमत चाहिए।",
   "चुने गए देशों में जर्मनी था।"],
  C3, 0,
  "Only statement 1 is correct. Austria, Kyrgyzstan, Portugal, Trinidad and Tobago and Zimbabwe were elected to take the seats of Denmark, Greece, Pakistan, Panama and Somalia, whose two-year terms end on 31 December 2026. Under Article 23 of the Charter the ten non-permanent members are elected for two years, five each year, by the General Assembly. "
  "Statement 2 is wrong: Article 18 makes their election an 'important question', needing a two-thirds majority of those present and voting even for an unopposed candidate. Statement 3 is wrong: Germany lost its bid in the Western European and Others group. India, last on the Council in 2021-22, is a candidate for 2028-29.",
  "केवल कथन 1 सही है। ऑस्ट्रिया, किर्गिस्तान, पुर्तगाल, त्रिनिदाद और टोबैगो तथा ज़िम्बाब्वे डेनमार्क, ग्रीस, पाकिस्तान, पनामा और सोमालिया के स्थान लेने के लिए चुने गए, जिनके दो वर्ष के कार्यकाल 31 दिसंबर 2026 को समाप्त होते हैं। चार्टर के अनुच्छेद 23 के अंतर्गत दस अस्थायी सदस्य महासभा द्वारा दो वर्ष के लिए, हर वर्ष पाँच, चुने जाते हैं। "
  "कथन 2 ग़लत है: अनुच्छेद 18 उनके चुनाव को ‘महत्त्वपूर्ण प्रश्न’ बनाता है, जिसके लिए निर्विरोध प्रत्याशी को भी उपस्थित और मत देने वालों का दो-तिहाई बहुमत चाहिए। कथन 3 ग़लत है: पश्चिमी यूरोपीय और अन्य समूह में जर्मनी की दावेदारी विफल रही। 2021-22 में अंतिम बार परिषद में रहा भारत 2028-29 के लिए प्रत्याशी है।",
  "United Nations General Assembly, election of non-permanent members of the Security Council (3 June 2026); Charter of the United Nations, Articles 18 and 23.",
  "ca-t2-ca-unsc-election-2027-28-two-thirds-pakistan", craft="precision")

S(IN, "easy", "On 2 June 2026 Bangladesh's Foreign Minister Khalilur Rahman was elected President of the 81st session of the UN General Assembly. Consider the following statements:",
  "2 जून 2026 को बांग्लादेश के विदेश मंत्री ख़लीलुर रहमान संयुक्त राष्ट्र महासभा के 81वें सत्र के अध्यक्ष चुने गए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The presidency of the 81st session was due by rotation to the Asia-Pacific group.",
   "The President of the General Assembly is elected for a term of two years."],
  ["81वें सत्र की अध्यक्षता बारी के अनुसार एशिया-प्रशांत समूह को मिलनी थी।",
   "महासभा का अध्यक्ष दो वर्ष के कार्यकाल के लिए चुना जाता है।"],
  T2, 0,
  "Only statement 1 is correct. The presidency rotates among the five regional groups, and in 2026 it fell to Asia-Pacific; unusually, the post was contested, and Rahman defeated Cyprus's candidate in a secret ballot. He succeeds Annalena Baerbock of Germany, President of the 80th session. "
  "Statement 2 is wrong: the President is elected for one session, a single year beginning in September; Rahman's term began on 8 September 2026.",
  "केवल कथन 1 सही है। अध्यक्षता पाँच क्षेत्रीय समूहों में घूमती है, और 2026 में यह एशिया-प्रशांत को मिली; असामान्य रूप से इस पद के लिए मुक़ाबला हुआ, और रहमान ने गुप्त मतदान में साइप्रस के प्रत्याशी को हराया। वे 80वें सत्र की अध्यक्ष जर्मनी की अन्नालेना बेयरबॉक के उत्तराधिकारी हैं। "
  "कथन 2 ग़लत है: अध्यक्ष एक सत्र, यानी सितंबर से शुरू होने वाले एक वर्ष, के लिए चुना जाता है; रहमान का कार्यकाल 8 सितंबर 2026 को शुरू हुआ।",
  "United Nations General Assembly, election of the President of the 81st session (2 June 2026); Rules of Procedure of the General Assembly.",
  "ca-t2-ca-pga-81-asia-pacific-one-year", craft="precision")

S(IN, "medium", "On 15 May 2026 the Court of Arbitration under the Indus Waters Treaty issued an award on pondage, which India rejected the next day. Consider the following statements:",
  "15 मई 2026 को सिंधु जल संधि के अंतर्गत मध्यस्थता न्यायालय ने जलसंग्रह (पॉन्डेज) पर एक निर्णय दिया, जिसे भारत ने अगले दिन अस्वीकार कर दिया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was the first award issued by the Court of Arbitration in the dispute.",
   "India rejected it, holding that the Court of Arbitration had been illegally constituted.",
   "The Court of Arbitration had been set up at India's request."],
  ["यह विवाद में मध्यस्थता न्यायालय द्वारा दिया गया पहला निर्णय था।",
   "भारत ने यह मानते हुए इसे अस्वीकार किया कि मध्यस्थता न्यायालय अवैध रूप से गठित हुआ था।",
   "मध्यस्थता न्यायालय भारत के अनुरोध पर गठित हुआ था।"],
  C3, 0,
  "Only statement 2 is correct. The Ministry of External Affairs rejected the award as 'null and void', said India had never recognised the Court, and recalled that the treaty has been held in abeyance since 23 April 2025, after the Pahalgam attack. "
  "Statement 1 is wrong: the award, on maximum pondage -- the water a run-of-the-river plant may store to follow daily changes in demand -- supplemented the Court's earlier award on the general interpretation of the treaty. "
  "Statement 3 is wrong: the Court of Arbitration was set up at Pakistan's request in its dispute over the Kishanganga and Ratle projects; India had asked instead for a neutral expert, the treaty's mechanism for technical differences, and the World Bank's decision to start both processes at once is the root of India's objection.",
  "केवल कथन 2 सही है। विदेश मंत्रालय ने निर्णय को ‘अमान्य और शून्य’ बताकर अस्वीकार किया, कहा कि भारत ने न्यायालय को कभी मान्यता नहीं दी, और याद दिलाया कि पहलगाम हमले के बाद 23 अप्रैल 2025 से संधि स्थगित है। "
  "कथन 1 ग़लत है: अधिकतम जलसंग्रह पर -- वह जल जिसे प्रवाह-आधारित परियोजना माँग के दैनिक उतार-चढ़ाव के अनुसार रख सकती है -- यह निर्णय संधि की सामान्य व्याख्या पर न्यायालय के पहले के निर्णय का पूरक था। "
  "कथन 3 ग़लत है: मध्यस्थता न्यायालय किशनगंगा और रतले परियोजनाओं पर पाकिस्तान के विवाद में उसके अनुरोध पर गठित हुआ; भारत ने इसके बजाय तटस्थ विशेषज्ञ माँगा था, जो तकनीकी मतभेदों के लिए संधि का तंत्र है, और विश्व बैंक द्वारा दोनों प्रक्रियाएँ एक साथ शुरू करना ही भारत की आपत्ति का मूल है।",
  "Ministry of External Affairs, statement on the 'award' of the Court of Arbitration (16 May 2026); Indus Waters Treaty, 1960, Article IX and Annexures F and G.",
  "ca-t2-ca-iwt-pondage-award-coa-pakistan-request", craft="linkage")

# ================================================================ INDICES
S(SC, "hard", "Several international rankings and data sets released in April-June 2026 placed India as follows. Consider the following statements:",
  "अप्रैल-जून 2026 में जारी कई अंतरराष्ट्रीय रैंकिंग और आँकड़ों ने भारत को इस प्रकार रखा। निम्नलिखित कथनों पर विचार कीजिए:",
  ["SIPRI's data on military expenditure placed India fifth among the world's biggest military spenders in 2025.",
   "India ranked as more peaceful in the Global Peace Index 2026 than in the 2025 edition.",
   "Germany spent more on its military in 2025 than India did.",
   "India improved its position in the IMD World Competitiveness Ranking 2026."],
  ["सिपरी के सैन्य व्यय आँकड़ों ने 2025 में भारत को विश्व के सबसे बड़े सैन्य व्यय करने वालों में पाँचवें स्थान पर रखा।",
   "वैश्विक शांति सूचकांक 2026 में भारत 2025 के संस्करण की तुलना में अधिक शांतिपूर्ण आँका गया।",
   "2025 में जर्मनी ने अपनी सेना पर भारत से अधिक व्यय किया।",
   "आईएमडी विश्व प्रतिस्पर्धात्मकता रैंकिंग 2026 में भारत की स्थिति सुधरी।"],
  C4, 1,
  "Statements 1 and 3 are correct. SIPRI's figures, released in April 2026, put India's military spending at $92.1 billion, up 8.9 per cent, fifth after the United States, China, Russia and Germany -- the five together accounting for 58 per cent of the world's $2.9 trillion -- with India moving up from sixth after the conflict with Pakistan in May 2025. "
  "Statement 2 is wrong: in the Global Peace Index of the Institute for Economics and Peace India fell from 115th to 127th of 163 countries, as South Asia recorded the sharpest decline of any region. Statement 4 is wrong: in the ranking by IMD, the Lausanne business school, India slipped to 44th of 70 economies, from 41st in 2025.",
  "कथन 1 और 3 सही हैं। अप्रैल 2026 में जारी सिपरी के आँकड़ों ने भारत के सैन्य व्यय को 8.9 प्रतिशत बढ़कर 92.1 अरब डॉलर बताया, संयुक्त राज्य अमेरिका, चीन, रूस और जर्मनी के बाद पाँचवाँ -- ये पाँच मिलकर विश्व के 2.9 खरब डॉलर का 58 प्रतिशत -- और मई 2025 में पाकिस्तान के साथ संघर्ष के बाद भारत छठे से ऊपर आया। "
  "कथन 2 ग़लत है: इंस्टीट्यूट फ़ॉर इकोनॉमिक्स एंड पीस के वैश्विक शांति सूचकांक में भारत 163 देशों में 115वें से गिरकर 127वें स्थान पर आया, क्योंकि दक्षिण एशिया में किसी भी क्षेत्र की तुलना में सबसे तीव्र गिरावट दर्ज हुई। कथन 4 ग़लत है: लॉज़ान के बिज़नेस स्कूल आईएमडी की रैंकिंग में भारत 70 अर्थव्यवस्थाओं में 2025 के 41वें से फिसलकर 44वें स्थान पर आया।",
  "Stockholm International Peace Research Institute, Trends in World Military Expenditure, 2025 (April 2026); Institute for Economics and Peace, Global Peace Index 2026; IMD World Competitiveness Center, World Competitiveness Ranking 2026.",
  "ca-t2-ca-sipri-milex-5th-gpi-127-imd-44", craft="multi")

# ================================================================ NATIONAL
MX(NA, "medium", "The results of the Assembly elections held in April 2026 were declared on 4 May 2026. Match List-I (State or Union territory) with List-II (party or alliance that formed the government):",
   "अप्रैल 2026 में हुए विधानसभा चुनावों के परिणाम 4 मई 2026 को घोषित हुए। सूची-I (राज्य या संघ राज्यक्षेत्र) का सूची-II (सरकार बनाने वाला दल या गठबंधन) से मिलान कीजिए:",
   ["West Bengal", "Tamil Nadu", "Kerala", "Puducherry"],
   ["पश्चिम बंगाल", "तमिलनाडु", "केरल", "पुदुचेरी"],
   ["Congress-led United Democratic Front", "Bharatiya Janata Party", "Tamilaga Vettri Kazhagam", "All India N.R. Congress-led alliance"],
   ["कांग्रेस-नेतृत्व वाला संयुक्त लोकतांत्रिक मोर्चा", "भारतीय जनता पार्टी", "तमिलगा वेट्री कड़गम", "ऑल इंडिया एन.आर. कांग्रेस-नेतृत्व वाला गठबंधन"],
   (2, 3, 1, 4), POS.get("ca-t2-ca-state-elections-2026-match", 1),
   "The correct code is A-2, B-3, C-1, D-4. In West Bengal the BJP won about 207 of 294 seats, ending fifteen years of Trinamool rule, and Suvendu Adhikari became the State's first BJP Chief Minister on 9 May. In Tamil Nadu the Tamilaga Vettri Kazhagam of the actor Vijay emerged as the largest party, short of a majority on its own, formed the government with outside support and won a trust vote -- the first government since 1967 led by neither the DMK nor the AIADMK; the outgoing Chief Minister, M.K. Stalin, lost his own seat. "
   "In Kerala the Congress-led UDF replaced the Left Democratic Front after ten years, with V.D. Satheesan as Chief Minister, and in Puducherry the alliance led by N. Rangasamy's All India N.R. Congress, with the BJP, retained power. In Assam the BJP-led alliance won a third term.",
   "सही कूट A-2, B-3, C-1, D-4 है। पश्चिम बंगाल में भाजपा ने 294 में से लगभग 207 सीटें जीतकर तृणमूल के पंद्रह वर्षों के शासन का अंत किया, और 9 मई को सुवेंदु अधिकारी राज्य के पहले भाजपा मुख्यमंत्री बने। तमिलनाडु में अभिनेता विजय का तमिलगा वेट्री कड़गम अपने बल पर बहुमत से कम पर सबसे बड़े दल के रूप में उभरा, बाहरी समर्थन से सरकार बनाई और विश्वास मत जीता -- 1967 के बाद पहली सरकार जिसका नेतृत्व न द्रमुक कर रहा है न अन्नाद्रमुक; निवर्तमान मुख्यमंत्री एम.के. स्टालिन अपनी ही सीट हार गए। "
   "केरल में कांग्रेस-नेतृत्व वाले यूडीएफ़ ने दस वर्ष बाद वाम लोकतांत्रिक मोर्चे का स्थान लिया, वी.डी. सतीशन मुख्यमंत्री बने, और पुदुचेरी में एन. रंगासामी की ऑल इंडिया एन.आर. कांग्रेस के नेतृत्व वाले, भाजपा सहित, गठबंधन ने सत्ता बनाए रखी। असम में भाजपा-नेतृत्व वाले गठबंधन ने तीसरा कार्यकाल जीता।",
   "Election Commission of India, results of the general elections to the Legislative Assemblies of Assam, Kerala, Tamil Nadu, West Bengal and Puducherry (4 May 2026).",
   "ca-t2-ca-state-elections-2026-match", "precision")

S(NA, "hard", "The Assam Assembly election of April 2026 was the first held on the constituencies redrawn in 2023. Consider the following statements about that delimitation:",
  "अप्रैल 2026 का असम विधानसभा चुनाव 2023 में पुनर्निर्धारित निर्वाचन क्षेत्रों पर हुआ पहला चुनाव था। उस परिसीमन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was carried out by the Election Commission of India rather than by a Delimitation Commission.",
   "It was based on the population figures of the 2011 Census.",
   "It changed the total number of seats in the Assam Legislative Assembly."],
  ["इसे परिसीमन आयोग के बजाय भारत निर्वाचन आयोग ने किया।",
   "यह 2011 की जनगणना के जनसंख्या आँकड़ों पर आधारित था।",
   "इसने असम विधानसभा की कुल सीटों की संख्या बदल दी।"],
  C3, 0,
  "Only statement 1 is correct. Assam's delimitation, held back in 2008 for security reasons when other States were redrawn, was entrusted to the Election Commission under section 8A of the Representation of the People Act, 1950, rather than to a Delimitation Commission under the Delimitation Act, 2002. The final order of August 2023 redrew the boundaries and raised the seats reserved for Scheduled Castes and Scheduled Tribes. "
  "Statement 2 is wrong: as the Constitution requires for any readjustment within a State until the first census after 2026, it used the population figures of the 2001 Census, not those of 2011. "
  "Statement 3 is wrong: the totals stayed fixed -- 126 Assembly seats and 14 Lok Sabha seats -- because the number of seats allotted to each State is frozen until after the first census taken after 2026; delimitation within a State only redraws boundaries and reservations.",
  "केवल कथन 1 सही है। 2008 में अन्य राज्यों के पुनर्निर्धारण के समय सुरक्षा कारणों से रोका गया असम का परिसीमन परिसीमन अधिनियम, 2002 के अंतर्गत परिसीमन आयोग के बजाय लोक प्रतिनिधित्व अधिनियम, 1950 की धारा 8क के अंतर्गत निर्वाचन आयोग को सौंपा गया। अगस्त 2023 के अंतिम आदेश ने सीमाएँ फिर खींचीं और अनुसूचित जातियों तथा अनुसूचित जनजातियों के लिए आरक्षित सीटें बढ़ाईं। "
  "कथन 2 ग़लत है: 2026 के बाद की पहली जनगणना तक किसी राज्य के भीतर किसी भी पुनर्समायोजन के लिए संविधान की अपेक्षा के अनुसार इसमें 2001 की जनगणना के जनसंख्या आँकड़ों का उपयोग हुआ, 2011 के नहीं। "
  "कथन 3 ग़लत है: कुल संख्या स्थिर रही -- 126 विधानसभा और 14 लोकसभा सीटें -- क्योंकि प्रत्येक राज्य को आवंटित सीटों की संख्या 2026 के बाद की पहली जनगणना तक स्थिर है; किसी राज्य के भीतर परिसीमन केवल सीमाएँ और आरक्षण फिर से तय करता है।",
  "Election Commission of India, Delimitation Order for Assam (August 2023); Representation of the People Act, 1950, section 8A; Constitution of India, Articles 82 and 170.",
  "ca-t2-ca-assam-delimitation-eci-8a-2001-126", craft="application")

S(NA, "medium", "In May 2026 the Centre was reported to be bringing about 1,200 fishing harbours and fish-landing centres under the security oversight of the Central Industrial Security Force (CISF). Consider the following statements:",
  "मई 2026 में बताया गया कि केंद्र लगभग 1,200 मत्स्य बंदरगाहों और मछली-उतराई केंद्रों को केंद्रीय औद्योगिक सुरक्षा बल (सीआईएसएफ़) की सुरक्षा निगरानी में ला रहा है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The CISF functions under the Ministry of Home Affairs.",
   "The attackers of 26 November 2008 reached Mumbai on a hijacked Indian fishing trawler.",
   "At airports the CISF is the regulator that lays down the standards of aviation security."],
  ["सीआईएसएफ़ गृह मंत्रालय के अधीन कार्य करता है।",
   "26 नवंबर 2008 के हमलावर एक अपहृत भारतीय मछली पकड़ने वाली नौका से मुंबई पहुँचे थे।",
   "हवाई अड्डों पर सीआईएसएफ़ ही वह नियामक है जो विमानन सुरक्षा के मानक तय करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The CISF, a central armed police force under the Ministry of Home Affairs, guards airports, ports, atomic and space installations and other critical infrastructure, and has been made the security authority for seaports; the plan would extend uniform procedures and surveillance to fishing harbours, which the 26/11 attackers exploited when they sailed from Karachi and hijacked the trawler Kuber to reach Mumbai. "
  "Statement 3 is wrong: the regulator for civil aviation security is the Bureau of Civil Aviation Security under the Ministry of Civil Aviation -- which in 2026 was running trials of full-body scanners at four major airports -- while the CISF provides the security staff that enforce its standards.",
  "कथन 1 और 2 सही हैं। गृह मंत्रालय के अधीन केंद्रीय सशस्त्र पुलिस बल सीआईएसएफ़ हवाई अड्डों, बंदरगाहों, परमाणु और अंतरिक्ष प्रतिष्ठानों तथा अन्य महत्त्वपूर्ण अवसंरचना की रक्षा करता है, और उसे समुद्री बंदरगाहों का सुरक्षा प्राधिकारी बनाया गया है; योजना एकरूप प्रक्रियाओं और निगरानी को उन मत्स्य बंदरगाहों तक ले जाएगी जिनका 26/11 के हमलावरों ने लाभ उठाया, जब वे कराची से चलकर कुबेर नाम की नौका का अपहरण कर मुंबई पहुँचे। "
  "कथन 3 ग़लत है: नागर विमानन सुरक्षा का नियामक नागर विमानन मंत्रालय के अधीन नागर विमानन सुरक्षा ब्यूरो है -- जो 2026 में चार प्रमुख हवाई अड्डों पर फ़ुल-बॉडी स्कैनरों का परीक्षण करा रहा था -- जबकि सीआईएसएफ़ उसके मानकों को लागू करने वाले सुरक्षा कर्मी देता है।",
  "Ministry of Home Affairs, plan for the security of fishing harbours under CISF oversight (May 2026); Bureau of Civil Aviation Security, Ministry of Civil Aviation.",
  "ca-t2-ca-cisf-fishing-harbours-26-11-bcas", craft="linkage")

S(NA, "medium", "On 19 June 2026 the Centre launched Abhigyan, a mobile application that lets the police check fingerprints on the spot. Consider the following statements:",
  "19 जून 2026 को केंद्र ने अभिज्ञान नाम का मोबाइल ऐप्लिकेशन शुरू किया, जिससे पुलिस मौक़े पर ही उँगलियों के निशान जाँच सकती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The app matches fingerprints against the National Automated Fingerprint Identification System maintained by the National Crime Records Bureau.",
   "The Criminal Procedure (Identification) Act, 2022 allows such records of measurements to be kept for 75 years.",
   "The 2022 Act replaced the Identification of Prisoners Act, 1920."],
  ["ऐप उँगलियों के निशानों का मिलान राष्ट्रीय अपराध रिकॉर्ड ब्यूरो द्वारा रखे जाने वाले राष्ट्रीय स्वचालित फ़िंगरप्रिंट पहचान तंत्र से करता है।",
   "दंड प्रक्रिया (पहचान) अधिनियम, 2022 माप के ऐसे अभिलेखों को 75 वर्ष तक रखने की अनुमति देता है।",
   "2022 के अधिनियम ने बंदी पहचान अधिनियम, 1920 का स्थान लिया।"],
  C3, 2,
  "All three statements are correct. Built by the NCRB for the use of police and investigating agencies, the app queries the National Automated Fingerprint Identification System (NAFIS), which holds the prints of more than 1.3 crore arrested persons, convicts and prisoners, and returns a match in well under a minute. "
  "The Criminal Procedure (Identification) Act, 2022, which replaced the colonial Identification of Prisoners Act, 1920, widened the 'measurements' police may take -- from finger and foot prints to iris and retina scans, photographs and biological samples -- and lets the NCRB store them for 75 years.",
  "तीनों कथन सही हैं। पुलिस और जाँच एजेंसियों के उपयोग के लिए एनसीआरबी द्वारा बनाया गया ऐप राष्ट्रीय स्वचालित फ़िंगरप्रिंट पहचान तंत्र (नेफ़िस) से पूछताछ करता है, जिसमें 1.3 करोड़ से अधिक गिरफ़्तार व्यक्तियों, सिद्धदोषों और बंदियों के निशान हैं, और एक मिनट से बहुत कम में मिलान देता है। "
  "औपनिवेशिक बंदी पहचान अधिनियम, 1920 का स्थान लेने वाले दंड प्रक्रिया (पहचान) अधिनियम, 2022 ने पुलिस द्वारा लिए जा सकने वाले ‘मापों’ का दायरा बढ़ाया -- उँगलियों और पैरों के निशानों से लेकर आइरिस और रेटिना स्कैन, फ़ोटो और जैविक नमूनों तक -- और एनसीआरबी को उन्हें 75 वर्ष तक रखने की अनुमति दी।",
  "Ministry of Home Affairs and National Crime Records Bureau, launch of the Abhigyan app (19 June 2026); Criminal Procedure (Identification) Act, 2022.",
  "ca-t2-ca-abhigyan-nafis-identification-act-75-years", craft="linkage")

M(NA, "easy",
  "In May 2026 the Ministry of Health and Family Welfare launched JANANI. It is:",
  "मई 2026 में स्वास्थ्य और परिवार कल्याण मंत्रालय ने जननी शुरू किया। यह है:",
  ["a digital platform that replaces the RCH portal and follows mothers from pregnancy, and children up to the age of five",
   "a cash-assistance scheme for institutional deliveries that replaces the Janani Suraksha Yojana for poor pregnant women",
   "a scheme of take-home rations for pregnant women and nursing mothers, delivered through anganwadi centres in every district",
   "a programme to train community midwives in every block so that home deliveries in tribal and hilly areas become safer"],
  ["एक डिजिटल मंच जो आरसीएच पोर्टल का स्थान लेता है और माताओं को गर्भावस्था से तथा बच्चों को पाँच वर्ष की आयु तक ट्रैक करता है",
   "संस्थागत प्रसव के लिए नकद-सहायता की एक योजना जो निर्धन गर्भवती महिलाओं के लिए जननी सुरक्षा योजना का स्थान लेती है",
   "गर्भवती महिलाओं और स्तनपान कराने वाली माताओं के लिए हर ज़िले में आंगनवाड़ी केंद्रों के माध्यम से दिए जाने वाले घर ले जाने योग्य राशन की योजना",
   "हर प्रखंड में सामुदायिक दाइयों को प्रशिक्षित करने का कार्यक्रम ताकि जनजातीय और पहाड़ी क्षेत्रों में घर पर होने वाले प्रसव सुरक्षित बनें"],
  0,
  "JANANI -- Journey of Antenatal, Natal and Neonatal Integrated Care -- is a service-oriented upgrade of the Reproductive and Child Health (RCH) portal: it records antenatal care, delivery preparedness, institutional delivery, postnatal and newborn care and family planning, issues QR-enabled cards, and exchanges data with U-WIN, the vaccination platform, and with the POSHAN nutrition systems, so that a mother and child can be followed across facilities and States. "
  "It is not a cash or nutrition scheme: the Janani Suraksha Yojana (2005), the conditional cash transfer for institutional delivery under the National Health Mission, continues, and take-home rations for pregnant women and nursing mothers come through anganwadis under Saksham Anganwadi and Poshan 2.0.",
  "जननी -- जर्नी ऑफ़ एंटीनेटल, नेटल एंड नियोनेटल इंटीग्रेटेड केयर -- प्रजनन और शिशु स्वास्थ्य (आरसीएच) पोर्टल का सेवा-केंद्रित उन्नयन है: यह प्रसव-पूर्व देखभाल, प्रसव की तैयारी, संस्थागत प्रसव, प्रसवोत्तर और नवजात देखभाल तथा परिवार नियोजन दर्ज करता है, क्यूआर-युक्त कार्ड जारी करता है, और टीकाकरण मंच यू-विन तथा पोषण प्रणालियों से आँकड़ों का आदान-प्रदान करता है, ताकि माँ और बच्चे पर विभिन्न सुविधाओं और राज्यों में नज़र रखी जा सके। "
  "यह नकद या पोषण योजना नहीं है: राष्ट्रीय स्वास्थ्य मिशन के अंतर्गत संस्थागत प्रसव के लिए सशर्त नकद हस्तांतरण, जननी सुरक्षा योजना (2005), चलती रहती है, और गर्भवती महिलाओं तथा स्तनपान कराने वाली माताओं के लिए घर ले जाने योग्य राशन सक्षम आंगनवाड़ी और पोषण 2.0 के अंतर्गत आंगनवाड़ियों से मिलता है।",
  "Ministry of Health and Family Welfare and PIB, launch of the JANANI digital platform (May 2026); National Health Mission, Janani Suraksha Yojana.",
  "ca-t2-ca-janani-replaces-rch-mother-child-five", pos=POS.get("ca-t2-ca-janani-replaces-rch-mother-child-five", 2), craft="precision")

S(NA, "medium", "In May-June 2026 the Ministry of Health and Family Welfare released the findings of the sixth National Family Health Survey (NFHS-6, 2023-24). Consider the following statements:",
  "मई-जून 2026 में स्वास्थ्य और परिवार कल्याण मंत्रालय ने छठे राष्ट्रीय परिवार स्वास्थ्य सर्वेक्षण (एनएफ़एचएस-6, 2023-24) के निष्कर्ष जारी किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The share of women who are obese fell compared with NFHS-5.",
   "The share of births by caesarean section was above the range of 10-15 per cent that WHO has suggested.",
   "The survey is conducted by the National Statistics Office."],
  ["मोटापे से ग्रस्त महिलाओं का हिस्सा एनएफ़एचएस-5 की तुलना में घटा।",
   "शल्य-प्रसव (सिज़ेरियन) से जन्मों का हिस्सा डब्ल्यूएचओ द्वारा सुझाई गई 10-15 प्रतिशत की सीमा से ऊपर था।",
   "यह सर्वेक्षण राष्ट्रीय सांख्यिकी कार्यालय करता है।"],
  C3, 0,
  "Only statement 2 is correct. Caesarean births climbed from 21.5 per cent in NFHS-5 to 27.2 per cent, far above the range WHO has suggested and much higher in private facilities, even as institutional deliveries rose from 88.6 to 90.6 per cent. "
  "Statement 1 is wrong: obesity rose sharply, from about 24 to about 31 per cent of women and from about 23 to 27 per cent of men. Critics noted that blood-based testing for anaemia was dropped from this round. "
  "Statement 3 is wrong: the NFHS is conducted for the Ministry of Health and Family Welfare by the International Institute for Population Sciences, Mumbai, as the nodal agency, through field agencies.",
  "केवल कथन 2 सही है। सिज़ेरियन जन्म एनएफ़एचएस-5 के 21.5 प्रतिशत से बढ़कर 27.2 प्रतिशत हो गए, जो डब्ल्यूएचओ द्वारा सुझाई सीमा से बहुत ऊपर और निजी सुविधाओं में कहीं अधिक है, जबकि संस्थागत प्रसव 88.6 से बढ़कर 90.6 प्रतिशत हुए। "
  "कथन 1 ग़लत है: मोटापा तेज़ी से बढ़ा, महिलाओं में लगभग 24 से लगभग 31 प्रतिशत और पुरुषों में लगभग 23 से 27 प्रतिशत। आलोचकों ने बताया कि इस दौर में रक्त-आधारित रक्ताल्पता परीक्षण हटा दिया गया। "
  "कथन 3 ग़लत है: एनएफ़एचएस स्वास्थ्य और परिवार कल्याण मंत्रालय के लिए अंतरराष्ट्रीय जनसंख्या विज्ञान संस्थान, मुंबई, नोडल एजेंसी के रूप में, क्षेत्रीय एजेंसियों के माध्यम से करता है।",
  "Ministry of Health and Family Welfare, National Family Health Survey (NFHS-6), 2023-24, national fact sheet; International Institute for Population Sciences, Mumbai.",
  "ca-t2-ca-nfhs-6-institutional-90-csection-iips", craft="precision")

S(NA, "easy", "On 7 May 2026 the Employees' State Insurance Corporation (ESIC) launched a nationwide free annual health check-up for insured workers aged 40 and above. Consider the following statements:",
  "7 मई 2026 को कर्मचारी राज्य बीमा निगम (ईएसआईसी) ने 40 वर्ष और अधिक आयु के बीमित श्रमिकों के लिए देशव्यापी निःशुल्क वार्षिक स्वास्थ्य जाँच शुरू की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The check-up follows from the Occupational Safety, Health and Working Conditions Code, 2020, which provides for annual health check-ups of workers.",
   "ESIC functions under the Ministry of Health and Family Welfare."],
  ["यह जाँच व्यावसायिक सुरक्षा, स्वास्थ्य और कार्य-दशा संहिता, 2020 से निकलती है, जो श्रमिकों की वार्षिक स्वास्थ्य जाँच का प्रावधान करती है।",
   "ईएसआईसी स्वास्थ्य और परिवार कल्याण मंत्रालय के अधीन कार्य करता है।"],
  T2, 0,
  "Only statement 1 is correct. With the labour codes in force since November 2025, the OSH Code's provision for a free annual check-up of workers above a prescribed age is being delivered through ESIC hospitals and dispensaries, covering clinical examination and baseline tests for about a crore of the scheme's 3.8 crore insured persons who are over 40. "
  "Statement 2 is wrong: ESIC, set up under the Employees' State Insurance Act, 1948, is a statutory body under the Ministry of Labour and Employment, whose minister launched the programme.",
  "केवल कथन 1 सही है। नवंबर 2025 से श्रम संहिताओं के लागू होने के साथ, निर्धारित आयु से ऊपर के श्रमिकों की निःशुल्क वार्षिक जाँच का ओएसएच संहिता का प्रावधान ईएसआईसी के अस्पतालों और औषधालयों के माध्यम से दिया जा रहा है, जिसमें योजना के 3.8 करोड़ बीमित व्यक्तियों में से 40 से ऊपर के लगभग एक करोड़ लोगों की नैदानिक जाँच और आधारभूत परीक्षण शामिल हैं। "
  "कथन 2 ग़लत है: कर्मचारी राज्य बीमा अधिनियम, 1948 के अंतर्गत स्थापित ईएसआईसी श्रम और रोज़गार मंत्रालय के अधीन एक सांविधिक निकाय है, जिसके मंत्री ने कार्यक्रम शुरू किया।",
  "Ministry of Labour and Employment and PIB, launch of the nationwide free annual health check-up through ESIC (7 May 2026); Occupational Safety, Health and Working Conditions Code, 2020; Employees' State Insurance Act, 1948.",
  "ca-t2-ca-esic-health-check-40-osh-code-labour", craft="precision")

S(NA, "medium", "On 18 May 2026 the new Kerala government decided to set up a separate Department of Senior Citizens, the first such department in the country. Consider the following statements:",
  "18 मई 2026 को केरल की नई सरकार ने वरिष्ठ नागरिकों का एक अलग विभाग बनाने का निर्णय लिया, जो देश में अपनी तरह का पहला विभाग है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kerala has the highest proportion of people aged 60 and above among the major States.",
   "A National Policy on Older Persons was adopted by the Central Government in 1999.",
   "'Old age pensions' figure in the Concurrent List of the Seventh Schedule."],
  ["बड़े राज्यों में 60 वर्ष और अधिक आयु के लोगों का अनुपात केरल में सबसे अधिक है।",
   "केंद्र सरकार ने 1999 में वृद्धजनों पर राष्ट्रीय नीति अपनाई।",
   "‘वृद्धावस्था पेंशन’ सातवीं अनुसूची की समवर्ती सूची में है।"],
  C3, 2,
  "All three statements are correct. An early fall in fertility and long life expectancy have made Kerala the oldest State: the Ministry of Statistics and Programme Implementation's 'Elderly in India 2021' projected that about 16.5 per cent of its people were 60 or above in 2021, against about 10 per cent nationally. "
  "The National Policy on Older Persons of 1999 committed the State to support the financial security, health care, shelter and welfare of people aged 60 and above; the Maintenance and Welfare of Parents and Senior Citizens Act, 2007 later made their maintenance a legal duty of children and heirs. The Constitution places 'invalidity and old age pensions', with the welfare of labour, in Entry 24 of the Concurrent List, and Article 41 directs the State to provide public assistance in old age within the limits of its economic capacity.",
  "तीनों कथन सही हैं। प्रजनन दर में जल्दी आई गिरावट और लंबी जीवन-प्रत्याशा ने केरल को सबसे बुज़ुर्ग राज्य बना दिया है: सांख्यिकी और कार्यक्रम कार्यान्वयन मंत्रालय की ‘एल्डरली इन इंडिया 2021’ ने अनुमान लगाया कि 2021 में उसके लगभग 16.5 प्रतिशत लोग 60 या अधिक आयु के थे, जबकि राष्ट्रीय स्तर पर लगभग 10 प्रतिशत। "
  "1999 की वृद्धजनों पर राष्ट्रीय नीति ने 60 वर्ष और अधिक आयु के लोगों की वित्तीय सुरक्षा, स्वास्थ्य देखभाल, आवास और कल्याण में सहयोग के लिए राज्य को प्रतिबद्ध किया; बाद में माता-पिता और वरिष्ठ नागरिकों का भरण-पोषण तथा कल्याण अधिनियम, 2007 ने उनका भरण-पोषण संतानों और उत्तराधिकारियों का विधिक दायित्व बनाया। संविधान ‘अशक्तता और वृद्धावस्था पेंशन’ को श्रमिकों के कल्याण के साथ समवर्ती सूची की प्रविष्टि 24 में रखता है, और अनुच्छेद 41 राज्य को अपनी आर्थिक सामर्थ्य की सीमाओं में वृद्धावस्था में लोक सहायता देने का निर्देश देता है।",
  "Government of Kerala, Cabinet decision on a Department of Senior Citizens (18 May 2026); Ministry of Statistics and Programme Implementation, Elderly in India 2021; Ministry of Social Justice and Empowerment, National Policy on Older Persons (1999); Constitution of India, Seventh Schedule, List III, Entry 24.",
  "ca-t2-ca-kerala-senior-citizens-dept-oldest-state-entry-24", craft="linkage")

M(NA, "easy",
  "On 30 May 2026 the Department of Administrative Reforms and Public Grievances launched 'Samadhan Didi'. It is:",
  "30 मई 2026 को प्रशासनिक सुधार और लोक शिकायत विभाग ने ‘समाधान दीदी’ शुरू की। यह है:",
  ["an AI voice chatbot through which citizens can lodge grievances on CPGRAMS",
   "a scheme to train women of self-help groups as para-legal volunteers for Lok Adalats",
   "a toll-free helpline for women facing harassment at the workplace",
   "a mobile app for women farmers to sell produce on e-NAM"],
  ["एक एआई वॉइस चैटबॉट जिसके माध्यम से नागरिक सीपीग्राम्स पर शिकायतें दर्ज कर सकते हैं",
   "लोक अदालतों के लिए स्वयं सहायता समूहों की महिलाओं को अर्ध-विधिक स्वयंसेवक के रूप में प्रशिक्षित करने की योजना",
   "कार्यस्थल पर उत्पीड़न झेल रही महिलाओं के लिए एक निःशुल्क हेल्पलाइन",
   "ई-नाम पर उपज बेचने के लिए महिला किसानों का एक मोबाइल ऐप"],
  0,
  "Samadhan Didi, developed by the Department of Administrative Reforms and Public Grievances with Bhashini, the national language-translation platform, lets a citizen describe a problem by speaking in any of more than twenty Indian languages; it asks clarifying questions, identifies the right ministry and category, and files the grievance on the Centralised Public Grievance Redress and Monitoring System (CPGRAMS), the online platform for grievances against Central government bodies. "
  "The other options describe no such scheme; workplace sexual harassment is handled by internal and local committees under the 2013 Act, and e-NAM is the online agricultural market.",
  "समाधान दीदी, जिसे प्रशासनिक सुधार और लोक शिकायत विभाग ने राष्ट्रीय भाषा-अनुवाद मंच भाषिणी के साथ विकसित किया, नागरिक को बीस से अधिक भारतीय भाषाओं में बोलकर अपनी समस्या बताने देती है; यह स्पष्ट करने वाले प्रश्न पूछती है, सही मंत्रालय और श्रेणी पहचानती है, और केंद्रीकृत लोक शिकायत निवारण और निगरानी प्रणाली (सीपीग्राम्स) पर शिकायत दर्ज करती है, जो केंद्र सरकार के निकायों के विरुद्ध शिकायतों का ऑनलाइन मंच है। "
  "अन्य विकल्प ऐसी किसी योजना का वर्णन नहीं करते; कार्यस्थल पर यौन उत्पीड़न 2013 के अधिनियम के अंतर्गत आंतरिक और स्थानीय समितियाँ देखती हैं, और ई-नाम ऑनलाइन कृषि बाज़ार है।",
  "Department of Administrative Reforms and Public Grievances, launch of the CPGRAMS AI-enabled voice chatbot 'Samadhan Didi' (30 May 2026) and monthly CPGRAMS report.",
  "ca-t2-ca-samadhan-didi-cpgrams-bhashini", pos=POS.get("ca-t2-ca-samadhan-didi-cpgrams-bhashini", 3), craft="precision")

S(NA, "medium", "The Kailash Manasarovar Yatra was held from June to August 2026, with pilgrims crossing into Tibet by two routes. Consider the following statements:",
  "कैलाश मानसरोवर यात्रा जून से अगस्त 2026 तक हुई, जिसमें तीर्थयात्री दो मार्गों से तिब्बत गए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The yatra is organised by the Ministry of Home Affairs.",
   "Its resumption followed the understanding reached by India and China in October 2024 on patrolling along the Line of Actual Control.",
   "The 2026 yatra was the first to be held since it was suspended in 2020."],
  ["यात्रा का आयोजन गृह मंत्रालय करता है।",
   "इसका फिर से शुरू होना वास्तविक नियंत्रण रेखा पर गश्त के बारे में अक्टूबर 2024 में भारत और चीन के बीच बनी सहमति के बाद हुआ।",
   "2026 की यात्रा 2020 में इसके निलंबन के बाद होने वाली पहली यात्रा थी।"],
  C3, 0,
  "Only statement 2 is correct. After the October 2024 understanding on patrolling ended the standoff at Depsang and Demchok, the two governments agreed in early 2025 to resume the pilgrimage along with other steps to normalise ties. "
  "Statement 1 is wrong: the Ministry of External Affairs runs the yatra with the Chinese side, selecting pilgrims by a computerised draw; in 2026, twenty batches of fifty went through Lipulekh and Nathu La. "
  "Statement 3 is wrong: the yatra, halted in 2020 by the pandemic and the border crisis, resumed in the summer of 2025; 2026 was its second season since.",
  "केवल कथन 2 सही है। अक्टूबर 2024 की गश्त-सहमति से देपसांग और देमचोक का गतिरोध समाप्त होने के बाद दोनों सरकारों ने 2025 के आरंभ में संबंधों को सामान्य करने के अन्य क़दमों के साथ तीर्थयात्रा फिर शुरू करने पर सहमति दी। "
  "कथन 1 ग़लत है: विदेश मंत्रालय चीनी पक्ष के साथ यात्रा चलाता है और कंप्यूटरीकृत ड्रॉ से तीर्थयात्रियों का चयन करता है; 2026 में पचास-पचास के बीस जत्थे लिपुलेख और नाथू ला से गए। "
  "कथन 3 ग़लत है: महामारी और सीमा संकट के कारण 2020 में रुकी यात्रा 2025 की गर्मियों में फिर शुरू हुई; 2026 उसके बाद का दूसरा मौसम था।",
  "Ministry of External Affairs, Kailash Manasarovar Yatra 2026 (announcement and draw, May 2026); MEA, India-China Foreign Secretary-Vice Minister mechanism (January 2025).",
  "ca-t2-ca-kmy-mea-2024-patrolling-resumed-2025", craft="linkage")

# ================================================================ SPORTS, DAYS, AWARDS
M(SP, "easy",
  "With reference to the ICC Women's T20 World Cup 2026, which one of the following statements is NOT correct?",
  "आईसीसी महिला टी20 विश्व कप 2026 के संदर्भ में निम्नलिखित में से कौन-सा कथन सही नहीं है?",
  ["India entered the tournament as the defending champions.",
   "It was the first edition of the tournament to have twelve teams.",
   "It was held in England and Wales.",
   "Its final was scheduled at Lord's in London."],
  ["भारत गत विजेता के रूप में प्रतियोगिता में उतरा।",
   "यह बारह टीमों वाला प्रतियोगिता का पहला संस्करण था।",
   "यह इंग्लैंड और वेल्स में हुआ।",
   "इसका फ़ाइनल लंदन के लॉर्ड्स में निर्धारित था।"],
  0,
  "The incorrect statement is that India were the defending champions: New Zealand won the 2024 edition, in the UAE, while India's women won the 50-over ICC Women's World Cup in November 2025, their first global title -- a near miss of the kind such statements use. "
  "The 2026 tournament, held in England and Wales from 12 June to 5 July, grew from ten to twelve teams, with the final at Lord's.",
  "ग़लत कथन यह है कि भारत गत विजेता था: 2024 का संस्करण यूएई में न्यूज़ीलैंड ने जीता था, जबकि भारत की महिलाओं ने नवंबर 2025 में 50 ओवर का आईसीसी महिला विश्व कप जीता, जो उनका पहला वैश्विक ख़िताब था -- ऐसे कथनों में प्रयुक्त होने वाली निकट-भूल। "
  "12 जून से 5 जुलाई तक इंग्लैंड और वेल्स में हुई 2026 की प्रतियोगिता दस से बढ़कर बारह टीमों की हो गई, और इसका फ़ाइनल लॉर्ड्स में था।",
  "International Cricket Council, ICC Women's T20 World Cup 2026: schedule and venues; ICC Women's T20 World Cup 2024 and ICC Women's World Cup 2025 results.",
  "ca-t2-ca-womens-t20-wc-2026-12-teams-lords", pos=POS.get("ca-t2-ca-womens-t20-wc-2026-12-teams-lords", 1), craft="precision")

M(SC, "medium",
  "International Day of Yoga was observed for the twelfth time on 21 June 2026. With reference to the day, which one of the following statements is NOT correct?",
  "21 जून 2026 को बारहवीं बार अंतरराष्ट्रीय योग दिवस मनाया गया। इस दिवस के संदर्भ में निम्नलिखित में से कौन-सा कथन सही नहीं है?",
  ["It was first observed in 2014, the year India proposed it at the United Nations.",
   "It was proclaimed, on India's proposal, by a resolution of the UN General Assembly adopted in December 2014.",
   "Its main national event in 2026 was held at Red Road in Kolkata.",
   "Its theme for 2026 was 'Yoga for Healthy Ageing'."],
  ["यह पहली बार 2014 में मनाया गया, जिस वर्ष भारत ने संयुक्त राष्ट्र में इसका प्रस्ताव रखा।",
   "इसकी घोषणा भारत के प्रस्ताव पर दिसंबर 2014 में स्वीकृत संयुक्त राष्ट्र महासभा के एक संकल्प द्वारा हुई।",
   "2026 में इसका मुख्य राष्ट्रीय आयोजन कोलकाता के रेड रोड पर हुआ।",
   "2026 के लिए इसका विषय ‘स्वस्थ वृद्धावस्था के लिए योग’ था।"],
  0,
  "The incorrect statement is that the day was first observed in 2014. The Prime Minister proposed the day at the UN General Assembly in September 2014, and resolution 69/131 of 11 December 2014, co-sponsored by a record 175 countries, proclaimed 21 June as International Day of Yoga -- so the first observance came on 21 June 2015, with the main event at Rajpath in New Delhi. "
  "For the twelfth edition the Ministry of Ayush chose 'Yoga for Healthy Ageing', with the main national event at Red Road in Kolkata; 'Yoga for One Earth, One Health' was the theme of 2025.",
  "ग़लत कथन यह है कि यह दिवस पहली बार 2014 में मनाया गया। प्रधानमंत्री ने सितंबर 2014 में संयुक्त राष्ट्र महासभा में इस दिवस का प्रस्ताव रखा, और रिकॉर्ड 175 देशों द्वारा सह-प्रायोजित 11 दिसंबर 2014 के संकल्प 69/131 ने 21 जून को अंतरराष्ट्रीय योग दिवस घोषित किया -- इसलिए पहला आयोजन 21 जून 2015 को हुआ, जिसका मुख्य कार्यक्रम नई दिल्ली के राजपथ पर था। "
  "बारहवें संस्करण के लिए आयुष मंत्रालय ने ‘स्वस्थ वृद्धावस्था के लिए योग’ विषय चुना, जिसका मुख्य राष्ट्रीय आयोजन कोलकाता के रेड रोड पर हुआ; ‘एक पृथ्वी, एक स्वास्थ्य के लिए योग’ 2025 का विषय था।",
  "Ministry of Ayush, International Day of Yoga 2026 and 2025; United Nations General Assembly resolution 69/131 (11 December 2014).",
  "ca-t2-ca-idy-2026-healthy-ageing-69-131-2015", pos=POS.get("ca-t2-ca-idy-2026-healthy-ageing-69-131-2015", 3), craft="precision")

M(SC, "easy",
  "With reference to the Goldman Environmental Prize 2026, announced on 20 April 2026, which one of the following statements is NOT correct?",
  "20 अप्रैल 2026 को घोषित गोल्डमैन पर्यावरण पुरस्कार 2026 के संदर्भ में निम्नलिखित में से कौन-सा कथन सही नहीं है?",
  ["The prize is awarded by the United Nations Environment Programme.",
   "For the first time in the prize's history, all the winners in a year were women.",
   "Its winner for Asia in 2026 was from South Korea.",
   "It is given to grassroots environmental activists."],
  ["यह पुरस्कार संयुक्त राष्ट्र पर्यावरण कार्यक्रम देता है।",
   "पुरस्कार के इतिहास में पहली बार किसी वर्ष के सभी विजेता महिलाएँ थीं।",
   "2026 में एशिया से इसकी विजेता दक्षिण कोरिया की थीं।",
   "यह ज़मीनी स्तर के पर्यावरण कार्यकर्ताओं को दिया जाता है।"],
  0,
  "The incorrect statement is the one about UNEP: the prize, often called the 'Green Nobel', is given by the Goldman Environmental Foundation of San Francisco; UNEP's own honour is the 'Champions of the Earth' award. "
  "The 2026 winners -- among them Borim Kim of South Korea, the winner for Asia -- were all women, a first in the prize's 37 years. The prize goes each year to grassroots activists from the world's six inhabited continental regions, and each receives $200,000.",
  "ग़लत कथन यूएनईपी वाला है: अक्सर ‘हरित नोबेल’ कहा जाने वाला यह पुरस्कार सैन फ़्रांसिस्को का गोल्डमैन एनवायरनमेंटल फ़ाउंडेशन देता है; यूएनईपी का अपना सम्मान ‘चैंपियंस ऑफ़ द अर्थ’ पुरस्कार है। "
  "2026 के विजेता -- जिनमें एशिया से विजेता दक्षिण कोरिया की बोरिम किम हैं -- सभी महिलाएँ थीं, जो पुरस्कार के 37 वर्षों में पहली बार हुआ। यह पुरस्कार हर वर्ष विश्व के छह बसे हुए महाद्वीपीय क्षेत्रों के ज़मीनी कार्यकर्ताओं को दिया जाता है, और हर विजेता को 2,00,000 डॉलर मिलते हैं।",
  "Goldman Environmental Foundation, 2026 Goldman Environmental Prize recipients (20 April 2026); United Nations Environment Programme, Champions of the Earth.",
  "ca-t2-ca-goldman-2026-all-women-not-unep", pos=POS.get("ca-t2-ca-goldman-2026-all-women-not-unep", 0), craft="precision")

finish("ca_t2_h.sql", FORMAT, "2026-Q2", update="--update" in sys.argv)
