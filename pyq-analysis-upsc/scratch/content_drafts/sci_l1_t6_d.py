# -*- coding: utf-8 -*-
"""Level 1 · Test 6 (Science & Technology, NCERT Foundation) -- part D: IT, Communication & Emerging Technologies (22)
(upsc_l1_cell_targets.mjs 6): easy MCQ 2, easy statement 4, easy Statement-I/II 1, medium MCQ 3, medium statement 8,
medium Statement-I/II 1, hard MCQ 1, hard statement 2.
The angle is NCERT Computer Science and Informatics Practices XI-XII: number systems, encoding, logic gates,
memory, translators, generations of computers, networks (types, topologies, devices, addressing, packets, DNS),
email protocols, cloud service models, malware, digital footprints, intellectual property and software licences.
Level-2 S&T facts are not repeated (bits and values, RAM and SSD, the Web and the internet, Wi-Fi and email basics,
IPv6 length, ICANN, undersea cables, open-source commercial use, cryptography, ransomware, phishing and SIM swap,
incognito mode, chips and Moore's law, AI, quantum, 5G/6G, DPI); nor CERT-In, in Level-2 Polity. MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
IT = "IT, Communication & Emerging Technologies"
CS11 = "NCERT Class XI, Computer Science"
CS12 = "NCERT Class XII, Computer Science"
IP12 = "NCERT Class XII, Informatics Practices"

# ---------------------------------------------------------------- easy MCQ (2)
M(IT, "easy", "The binary number 1011 is equal to the decimal number",
  "द्विआधारी (binary) संख्या 1011 दशमलव में किसके बराबर है?",
  ["11", "13", "9", "1011"],
  ["11", "13", "9", "1011"],
  0,
  "In binary each place is worth twice the one to its right -- 8, 4, 2 and 1 for a four-digit number -- so 1011 = 8 + 0 + 2 + 1 = 11. "
  "Computers use binary because their circuits have two stable states, on and off, which stand for 1 and 0; every number, letter and image is ultimately stored as such patterns of bits.",
  "द्विआधारी में हर स्थान अपने दाएँ वाले स्थान का दोगुना होता है -- चार अंकों की संख्या में 8, 4, 2 और 1 -- इसलिए 1011 = 8 + 0 + 2 + 1 = 11। "
  "कंप्यूटर द्विआधारी का उपयोग इसलिए करते हैं कि उनके परिपथों की दो स्थिर अवस्थाएँ होती हैं, चालू और बंद, जो 1 और 0 को दर्शाती हैं; हर संख्या, अक्षर और चित्र अंततः बिटों के ऐसे ही प्रतिरूपों के रूप में संचित होता है।",
  f"{CS11} (Encoding Schemes and Number System).",
  "l1-sci-binary-1011-decimal", pos=0, craft="application")

M(IT, "easy", "Which device connects different networks, such as a home network and the internet, and directs data packets between them using IP addresses?",
  "कौन-सा उपकरण विभिन्न नेटवर्कों, जैसे घरेलू नेटवर्क और इंटरनेट, को जोड़ता है और IP पतों का उपयोग करके उनके बीच डेटा पैकेट भेजता है?",
  ["router", "repeater", "hub", "modem"],
  ["राउटर", "रिपीटर", "हब", "मॉडेम"],
  0,
  "A router reads the destination IP address of each packet and forwards it towards the right network, choosing a path; the home 'Wi-Fi router' usually combines a router, a switch and a wireless access point in one box. "
  "A modem converts digital data to signals that can travel over a telephone, cable or fibre line and back; a hub and a repeater work within a single network.",
  "राउटर हर पैकेट का गंतव्य IP पता पढ़कर उसे सही नेटवर्क की ओर भेजता है और मार्ग चुनता है; घर का 'वाई-फ़ाई राउटर' सामान्यतः राउटर, स्विच और बेतार पहुँच-बिंदु को एक ही डिब्बे में जोड़ता है। "
  "मॉडेम डिजिटल डेटा को टेलीफ़ोन, केबल या फ़ाइबर लाइन पर जाने लायक़ संकेतों में और फिर वापस बदलता है; हब और रिपीटर एक ही नेटवर्क के भीतर काम करते हैं।",
  f"{CS12} (Computer Networks).",
  "l1-sci-router-ip-packets", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (4)
S(IT, "easy", "Consider the following statements about encoding text in computers:",
  "कंप्यूटरों में पाठ के कूटन (encoding) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["ASCII uses 7 bits and can represent 128 characters.",
   "Unicode aims to represent the characters of all the world's writing systems, including Devanagari.",
   "ASCII can represent the letters of the Devanagari script."],
  ["ASCII 7 बिटों का उपयोग करता है और 128 वर्णों को दर्शा सकता है।",
   "यूनिकोड का उद्देश्य विश्व की सभी लिपियों, देवनागरी सहित, के वर्णों को दर्शाना है।",
   "ASCII देवनागरी लिपि के अक्षरों को दर्शा सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: ASCII covers only the English alphabet, digits, punctuation and control characters, which is why Indian languages once needed separate, incompatible encodings and fonts. "
  "Statement 3 is wrong for that reason: Devanagari and other Indian scripts are represented in Unicode, which lets a document in Hindi, Tamil and English be stored and shared correctly on any device.",
  "कथन 1 और 2 सही हैं: ASCII केवल अंग्रेज़ी वर्णमाला, अंक, विराम-चिह्न और नियंत्रण वर्णों को कवर करता है, इसीलिए भारतीय भाषाओं को कभी अलग, असंगत कूटनों और फ़ॉन्टों की आवश्यकता होती थी। "
  "इसी कारण कथन 3 गलत है: देवनागरी और अन्य भारतीय लिपियाँ यूनिकोड में दर्शाई जाती हैं, जो हिंदी, तमिल और अंग्रेज़ी के किसी दस्तावेज़ को किसी भी उपकरण पर सही ढंग से संचित और साझा करने देता है।",
  f"{CS11} (Encoding Schemes and Number System).",
  "l1-sci-ascii-unicode-devanagari", craft="precision")

S(IT, "easy", "Consider the following statements about language translators:",
  "भाषा अनुवादकों (translators) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A compiler translates the whole program into machine code before it is run.",
   "An interpreter translates and executes a program line by line, stopping at the first error it meets.",
   "Programs in Python are usually run with an interpreter."],
  ["कंपाइलर पूरे प्रोग्राम को चलाने से पहले मशीन कोड में अनूदित करता है।",
   "इंटरप्रेटर प्रोग्राम को पंक्ति-दर-पंक्ति अनूदित और निष्पादित करता है, और पहली त्रुटि मिलते ही रुक जाता है।",
   "पाइथन के प्रोग्राम सामान्यतः इंटरप्रेटर से चलाए जाते हैं।"],
  C3, 2,
  "All three statements are correct. Computers understand only machine language, so programs written in high-level languages must be translated; a compiled program, once translated, runs fast without the compiler, while interpretation makes it easier to test and correct a program step by step. "
  "An assembler does the same job for assembly language.",
  "तीनों कथन सही हैं। कंप्यूटर केवल मशीनी भाषा समझते हैं, इसलिए उच्च-स्तरीय भाषाओं में लिखे प्रोग्रामों का अनुवाद आवश्यक है; एक बार अनूदित होने पर संकलित प्रोग्राम कंपाइलर के बिना तेज़ी से चलता है, जबकि इंटरप्रेटर से प्रोग्राम को कदम-दर-कदम जाँचना और सुधारना आसान होता है। "
  "असेंबलर यही काम असेंबली भाषा के लिए करता है।",
  f"{CS11} (Computer System).",
  "l1-sci-compiler-interpreter", craft="recall")

S(IT, "easy", "Consider the following statements about intellectual property:",
  "बौद्धिक संपदा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Copyright protects the expression of an idea -- such as a book, a song or a computer program -- rather than the idea itself.",
   "A patent gives its owner exclusive rights over an invention, generally for 20 years.",
   "A trademark protects a brand's name, logo or symbol, which distinguishes its goods from others'."],
  ["कॉपीराइट किसी विचार की अभिव्यक्ति -- जैसे पुस्तक, गीत या कंप्यूटर प्रोग्राम -- की रक्षा करता है, स्वयं विचार की नहीं।",
   "पेटेंट अपने स्वामी को किसी आविष्कार पर, सामान्यतः 20 वर्ष के लिए, अनन्य अधिकार देता है।",
   "ट्रेडमार्क किसी ब्रांड के नाम, लोगो या प्रतीक की रक्षा करता है, जो उसकी वस्तुओं को दूसरों से अलग पहचान देता है।"],
  C3, 2,
  "All three statements are correct. Copyright arises automatically when a work is created, while patents and trademarks must be applied for and registered; using someone's work without permission or credit can infringe these rights, and presenting it as one's own is plagiarism. "
  "In exchange for a patent's monopoly, the inventor must disclose the invention publicly, so that others can build on it once the patent expires.",
  "तीनों कथन सही हैं। कॉपीराइट किसी कृति के बनते ही स्वतः उत्पन्न होता है, जबकि पेटेंट और ट्रेडमार्क के लिए आवेदन और पंजीकरण करना पड़ता है; किसी की कृति का बिना अनुमति या श्रेय के उपयोग इन अधिकारों का उल्लंघन हो सकता है, और उसे अपनी बताना साहित्यिक चोरी है। "
  "पेटेंट के एकाधिकार के बदले आविष्कारक को आविष्कार सार्वजनिक रूप से प्रकट करना होता है, ताकि पेटेंट समाप्त होने पर दूसरे उस पर आगे काम कर सकें।",
  f"{IP12} (Societal Impacts).",
  "l1-sci-copyright-patent-trademark", craft="recall")

S(IT, "easy", "Consider the following statements about types of computer networks:",
  "कंप्यूटर नेटवर्कों के प्रकारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A local area network (LAN) connects devices within a limited area such as a building or a campus.",
   "A wide area network (WAN) is limited to a single building."],
  ["स्थानीय क्षेत्र नेटवर्क (LAN) किसी भवन या परिसर जैसे सीमित क्षेत्र के उपकरणों को जोड़ता है।",
   "विस्तृत क्षेत्र नेटवर्क (WAN) एक ही भवन तक सीमित होता है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: a WAN spreads across cities, countries or continents, usually linking many smaller networks, and the internet is the largest WAN of all. "
  "Between the two lies the metropolitan area network (MAN), covering a city, while a personal area network (PAN) links the devices of one person within a few metres.",
  "केवल कथन 1 सही है। कथन 2 गलत है: WAN नगरों, देशों या महाद्वीपों में फैला होता है और सामान्यतः कई छोटे नेटवर्कों को जोड़ता है, और इंटरनेट सबसे बड़ा WAN है। "
  "इन दोनों के बीच किसी नगर को कवर करने वाला महानगरीय क्षेत्र नेटवर्क (MAN) है, जबकि व्यक्तिगत क्षेत्र नेटवर्क (PAN) एक व्यक्ति के उपकरणों को कुछ मीटर के भीतर जोड़ता है।",
  f"{CS12} (Computer Networks).",
  "l1-sci-lan-wan-scale", craft="precision")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(IT, "easy",
  "Websites that ask for passwords or payment details should use HTTPS rather than HTTP.",
  "पासवर्ड या भुगतान का विवरण माँगने वाली वेबसाइटों को HTTP के बजाय HTTPS का उपयोग करना चाहिए।",
  "HTTPS encrypts the data travelling between the browser and the website, so that others on the network cannot read it.",
  "HTTPS ब्राउज़र और वेबसाइट के बीच जाने वाले डेटा को कूटबद्ध (encrypt) करता है, ताकि नेटवर्क पर दूसरे उसे पढ़ न सकें।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Without encryption, anyone on the same Wi-Fi or along the route could read or alter what is sent; HTTPS uses the TLS protocol to encrypt the connection and a certificate to show that the site is genuine. "
  "The padlock in the address bar shows only that the connection is encrypted -- a fraudulent site can also use HTTPS, so it is not proof that a site is trustworthy.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। कूटबद्धता के बिना उसी वाई-फ़ाई पर या मार्ग में कोई भी भेजा गया डेटा पढ़ या बदल सकता है; HTTPS संपर्क को कूटबद्ध करने के लिए TLS प्रोटोकॉल और साइट के असली होने को दिखाने के लिए प्रमाणपत्र का उपयोग करता है। "
  "पता-पट्टी में ताले का चिह्न केवल यह दिखाता है कि संपर्क कूटबद्ध है -- धोखेबाज़ साइट भी HTTPS का उपयोग कर सकती है, इसलिए यह साइट के विश्वसनीय होने का प्रमाण नहीं है।",
  f"{CS12} (Computer Networks); {IP12} (Societal Impacts).",
  "l1-sci-https-encryption", craft="inference")

# ---------------------------------------------------------------- medium MCQ (3)
M(IT, "medium", "When a user types a website's name, such as ncert.nic.in, the system that finds the numerical IP address of that site is the",
  "जब उपयोगकर्ता किसी वेबसाइट का नाम, जैसे ncert.nic.in, टाइप करता है, तो उस साइट का संख्यात्मक IP पता खोजने वाली प्रणाली कौन-सी है?",
  ["Domain Name System", "File Transfer Protocol", "Dynamic Host Configuration Protocol", "Hypertext Markup Language"],
  ["डोमेन नेम सिस्टम (DNS)", "फ़ाइल ट्रांसफ़र प्रोटोकॉल (FTP)", "डायनेमिक होस्ट कॉन्फ़िगरेशन प्रोटोकॉल (DHCP)", "हाइपरटेक्स्ट मार्कअप लैंग्वेज (HTML)"],
  0,
  "Computers on the internet locate each other by IP addresses, which are hard to remember; the DNS works like a telephone directory, translating names into addresses through a worldwide hierarchy of servers. "
  "FTP transfers files; DHCP automatically assigns an IP address to a device when it joins a network; and HTML is the language in which web pages are written.",
  "इंटरनेट पर कंप्यूटर एक-दूसरे को IP पतों से खोजते हैं, जिन्हें याद रखना कठिन है; DNS टेलीफ़ोन निर्देशिका की तरह काम करता है और सर्वरों के विश्वव्यापी पदानुक्रम के माध्यम से नामों को पतों में बदलता है। "
  "FTP फ़ाइलें भेजता है; DHCP किसी उपकरण के नेटवर्क से जुड़ने पर उसे स्वतः IP पता देता है; और HTML वह भाषा है जिसमें वेब पेज लिखे जाते हैं।",
  f"{CS12} (Computer Networks).",
  "l1-sci-dns-names-to-ip", pos=0, craft="application")

M(IT, "medium", "A software licence that lets anyone use, study, modify and share a program, but requires every modified version to be released under the same terms, is described as",
  "वह सॉफ़्टवेयर लाइसेंस जो किसी को भी प्रोग्राम का उपयोग, अध्ययन, संशोधन और साझा करने देता है, पर हर संशोधित संस्करण को उन्हीं शर्तों पर जारी करना अनिवार्य करता है, क्या कहलाता है?",
  ["copyleft", "freeware", "shareware", "adware"],
  ["कॉपीलेफ़्ट", "फ़्रीवेयर", "शेयरवेयर", "ऐडवेयर"],
  0,
  "Copyleft, used by the GNU General Public License (GPL), turns copyright around: instead of restricting copies, it uses the author's rights to keep the software and all its derivatives free for everyone. "
  "Freeware is given away at no cost but usually without its source code, shareware may be tried free but must be paid for later, and adware is paid for by the advertisements it displays.",
  "GNU जनरल पब्लिक लाइसेंस (GPL) द्वारा प्रयुक्त कॉपीलेफ़्ट कॉपीराइट को उलट देता है: प्रतियों को रोकने के बजाय यह लेखक के अधिकारों का उपयोग सॉफ़्टवेयर और उसके सभी व्युत्पन्नों को सबके लिए मुक्त रखने में करता है। "
  "फ़्रीवेयर बिना मूल्य दिया जाता है पर प्रायः स्रोत कोड के बिना, शेयरवेयर मुफ़्त आज़माया जा सकता है पर बाद में भुगतान करना होता है, और ऐडवेयर का ख़र्च उसके दिखाए विज्ञापनों से निकलता है।",
  f"{IP12} (Societal Impacts).",
  "l1-sci-copyleft-gpl", pos=3, craft="precision")

M(IT, "medium", "The output of a NAND gate is 0 only when",
  "NAND गेट का आउटपुट केवल कब 0 होता है?",
  ["all its inputs are 1", "all its inputs are 0", "any one input is 1", "its two inputs differ"],
  ["उसके सभी इनपुट 1 हों", "उसके सभी इनपुट 0 हों", "कोई एक इनपुट 1 हो", "उसके दोनों इनपुट भिन्न हों"],
  0,
  "NAND is 'NOT AND': an AND gate gives 1 only when all its inputs are 1, and the NAND gate inverts that result, so it gives 0 in exactly that case and 1 in every other. "
  "NAND is called a universal gate, because NOT, AND and OR -- and so any logic circuit -- can be built from NAND gates alone.",
  "NAND का अर्थ है 'NOT AND': AND गेट केवल तब 1 देता है जब सभी इनपुट 1 हों, और NAND गेट उस परिणाम को उलट देता है, इसलिए वह ठीक उसी स्थिति में 0 और बाक़ी सब में 1 देता है। "
  "NAND को सार्वभौमिक गेट कहते हैं, क्योंकि NOT, AND और OR -- और इसलिए कोई भी तार्किक परिपथ -- केवल NAND गेटों से बनाए जा सकते हैं।",
  f"{CS11} (Introduction to Boolean Logic, earlier editions).",
  "l1-sci-nand-gate-output", pos=2, craft="precision")

# ---------------------------------------------------------------- medium statement (8)
S(IT, "medium", "Consider the following statements about network topologies:",
  "नेटवर्क टोपोलॉजी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In a star topology, the failure of one computer or its cable does not affect the others.",
   "In a bus topology, a break in the main backbone cable can bring down the whole network.",
   "A mesh topology has the least redundancy of all topologies."],
  ["स्टार टोपोलॉजी में एक कंप्यूटर या उसके केबल की ख़राबी दूसरों को प्रभावित नहीं करती।",
   "बस टोपोलॉजी में मुख्य बैकबोन केबल के टूटने से पूरा नेटवर्क ठप हो सकता है।",
   "मेश टोपोलॉजी में सभी टोपोलॉजियों में सबसे कम अतिरेक (redundancy) होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: in a star, each device has its own link to a central switch, though the network fails if the switch itself fails; in a bus, all devices share one cable. "
  "Statement 3 is wrong: in a mesh, devices are linked to many others, so data can take another route if one link fails -- the most redundancy, at the cost of the most cabling, which is why the internet's backbone is mesh-like.",
  "कथन 1 और 2 सही हैं: स्टार में हर उपकरण का केंद्रीय स्विच से अपना संपर्क होता है, यद्यपि स्विच के ख़राब होने पर नेटवर्क ठप हो जाता है; बस में सभी उपकरण एक ही केबल साझा करते हैं। "
  "कथन 3 गलत है: मेश में उपकरण कई अन्य से जुड़े होते हैं, इसलिए एक संपर्क टूटने पर डेटा दूसरा मार्ग ले सकता है -- सबसे अधिक अतिरेक, सबसे अधिक केबल की कीमत पर, इसीलिए इंटरनेट की रीढ़ मेश जैसी है।",
  f"{CS12} (Computer Networks).",
  "l1-sci-star-bus-mesh-topology", craft="inference")

S(IT, "medium", "Consider the following statements about network devices:",
  "नेटवर्क उपकरणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A hub sends the data it receives to all the devices connected to it.",
   "A switch sends data only to the device for which it is meant.",
   "A repeater regenerates a weakened signal so that it can travel over a longer cable."],
  ["हब प्राप्त डेटा को अपने से जुड़े सभी उपकरणों को भेज देता है।",
   "स्विच डेटा केवल उसी उपकरण को भेजता है जिसके लिए वह है।",
   "रिपीटर कमज़ोर हुए संकेत को फिर से बनाता है ताकि वह लंबे केबल पर जा सके।"],
  C3, 2,
  "All three statements are correct. Because a hub broadcasts everything, devices compete for the same channel and the network slows as it grows; a switch learns the hardware (MAC) address of each connected device and forwards data only to its port, using the network more efficiently. "
  "Signals weaken as they travel along a cable, so repeaters are placed at intervals on long links.",
  "तीनों कथन सही हैं। चूँकि हब सब कुछ प्रसारित करता है, उपकरण एक ही चैनल के लिए प्रतिस्पर्धा करते हैं और नेटवर्क बढ़ने के साथ धीमा होता है; स्विच हर जुड़े उपकरण का हार्डवेयर (MAC) पता जान लेता है और डेटा केवल उसके पोर्ट पर भेजता है, जिससे नेटवर्क का अधिक कुशल उपयोग होता है। "
  "केबल पर चलते हुए संकेत कमज़ोर होते हैं, इसलिए लंबे संपर्कों पर अंतराल पर रिपीटर लगाए जाते हैं।",
  f"{CS12} (Computer Networks).",
  "l1-sci-hub-switch-repeater", craft="recall")

S(IT, "medium", "Consider the following statements about malicious software:",
  "दुर्भावनापूर्ण सॉफ़्टवेयर (malware) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A worm can copy itself and spread across networks on its own, without attaching to another program.",
   "A Trojan horse disguises itself as useful or harmless software to get installed.",
   "Spyware secretly collects information about a user's activities.",
   "A computer virus can spread without attaching itself to any host program or file."],
  ["वर्म स्वयं की प्रतियाँ बनाकर किसी अन्य प्रोग्राम से जुड़े बिना अपने आप नेटवर्कों में फैल सकता है।",
   "ट्रोजन हॉर्स स्थापित होने के लिए स्वयं को उपयोगी या हानिरहित सॉफ़्टवेयर के रूप में छिपाता है।",
   "स्पाइवेयर गुप्त रूप से उपयोगकर्ता की गतिविधियों की जानकारी इकट्ठा करता है।",
   "कंप्यूटर वायरस किसी मेज़बान प्रोग्राम या फ़ाइल से जुड़े बिना फैल सकता है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Statement 4 is wrong: that is what distinguishes a worm; a virus attaches itself to a host program or file and spreads when that host is run or shared. "
  "Keeping software updated, using antivirus tools, and not opening unknown attachments or installing programs from untrusted sources are the main defences.",
  "कथन 1, 2 और 3 सही हैं। कथन 4 गलत है: यही वर्म की पहचान है; वायरस किसी मेज़बान प्रोग्राम या फ़ाइल से जुड़ता है और उस मेज़बान के चलाए या साझा किए जाने पर फैलता है। "
  "सॉफ़्टवेयर अद्यतन रखना, एंटीवायरस उपकरणों का उपयोग करना, और अज्ञात संलग्नक न खोलना या अविश्वसनीय स्रोतों से प्रोग्राम स्थापित न करना मुख्य बचाव हैं।",
  f"{IP12} (Societal Impacts); {CS11} (Computer System).",
  "l1-sci-worm-trojan-spyware-virus", craft="precision")

S(IT, "medium", "Consider the following statements about digital footprints:",
  "डिजिटल पदचिह्नों (digital footprints) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["An active digital footprint includes data we share on purpose, such as posts, comments and emails.",
   "A passive digital footprint includes data collected without our deliberate input, such as browsing history, location and the IP address of our device.",
   "Deleting a post removes every copy of it from the internet."],
  ["सक्रिय डिजिटल पदचिह्न में वह डेटा है जो हम जान-बूझकर साझा करते हैं, जैसे पोस्ट, टिप्पणियाँ और ईमेल।",
   "निष्क्रिय डिजिटल पदचिह्न में हमारे सचेत इनपुट के बिना इकट्ठा किया गया डेटा है, जैसे ब्राउज़िंग इतिहास, स्थान और हमारे उपकरण का IP पता।",
   "किसी पोस्ट को हटाने से इंटरनेट से उसकी हर प्रति मिट जाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is wrong: copies, screenshots, shares, archives and server backups may survive long after a post is deleted, which is why NCERT advises thinking before posting -- digital footprints can be used to profile, target or embarrass a person years later. "
  "Footprints are also used, legitimately or not, for advertising and for checking a person's background.",
  "कथन 1 और 2 सही हैं। कथन 3 गलत है: पोस्ट हटाए जाने के बहुत बाद तक उसकी प्रतियाँ, स्क्रीनशॉट, साझा किए गए रूप, अभिलेखागार और सर्वर बैकअप बचे रह सकते हैं, इसीलिए NCERT पोस्ट करने से पहले सोचने की सलाह देता है -- डिजिटल पदचिह्नों से वर्षों बाद किसी व्यक्ति की रूपरेखा बनाई, उसे निशाना बनाया या शर्मिंदा किया जा सकता है। "
  "पदचिह्नों का उपयोग, वैध या अवैध रूप से, विज्ञापन और किसी व्यक्ति की पृष्ठभूमि जाँचने में भी होता है।",
  f"{IP12} (Societal Impacts).",
  "l1-sci-digital-footprint-active-passive", craft="inference")

S(IT, "medium", "Consider the following statements about computer memory:",
  "कंप्यूटर स्मृति (memory) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["ROM is non-volatile and holds the firmware a computer needs to start up.",
   "Cache memory is slower than RAM.",
   "Secondary storage, such as a hard disk, is faster than RAM."],
  ["ROM अवाष्पशील (non-volatile) है और उस फ़र्मवेयर को रखती है जिसकी कंप्यूटर को चालू होने के लिए आवश्यकता होती है।",
   "कैश मेमोरी RAM से धीमी होती है।",
   "द्वितीयक भंडारण, जैसे हार्ड डिस्क, RAM से तेज़ होता है।"],
  C3, 0,
  "Only statement 1 is correct. Memory forms a hierarchy: registers and cache, inside or next to the processor, are the fastest and smallest; RAM is larger but slower; and secondary storage is the largest and cheapest per byte but the slowest. "
  "Statements 2 and 3 reverse this order: cache holds frequently used data precisely because it is faster than RAM, and programs are loaded from disk into RAM because RAM is faster.",
  "केवल कथन 1 सही है। स्मृति एक पदानुक्रम बनाती है: प्रोसेसर के भीतर या उसके पास रजिस्टर और कैश सबसे तेज़ और सबसे छोटे होते हैं; RAM बड़ी पर धीमी है; और द्वितीयक भंडारण सबसे बड़ा और प्रति बाइट सबसे सस्ता, पर सबसे धीमा है। "
  "कथन 2 और 3 यह क्रम उलट देते हैं: कैश बार-बार प्रयुक्त डेटा ठीक इसलिए रखती है कि वह RAM से तेज़ है, और प्रोग्राम डिस्क से RAM में इसलिए लाए जाते हैं कि RAM तेज़ है।",
  f"{CS11} (Computer System).",
  "l1-sci-memory-hierarchy-rom-cache", craft="precision")

S(IT, "medium", "Consider the following statements about email:",
  "ईमेल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Recipients in the 'Bcc' field are hidden from the other recipients of the message.",
   "IMAP keeps messages on the mail server, so the same mailbox can be seen in step on several devices.",
   "POP3 usually downloads messages to a single device.",
   "SMTP is the protocol used to send email."],
  ["'Bcc' क्षेत्र के प्राप्तकर्ता संदेश के अन्य प्राप्तकर्ताओं से छिपे रहते हैं।",
   "IMAP संदेशों को मेल सर्वर पर रखता है, इसलिए वही मेलबॉक्स कई उपकरणों पर एक-सा दिख सकता है।",
   "POP3 सामान्यतः संदेशों को एक ही उपकरण पर डाउनलोड करता है।",
   "SMTP ईमेल भेजने के लिए प्रयुक्त प्रोटोकॉल है।"],
  C4, 3,
  "All four statements are correct. Using Bcc for a large list protects people's addresses from being exposed to everyone; IMAP suits people who read mail on a phone and a laptop, while POP3 suits a single computer with limited server space. "
  "Sending and receiving use different protocols: SMTP carries mail from the sender to the recipient's server, and IMAP or POP3 brings it from that server to the reader.",
  "चारों कथन सही हैं। बड़ी सूची के लिए Bcc का उपयोग लोगों के पतों को सबके सामने आने से बचाता है; IMAP उनके लिए उपयुक्त है जो फ़ोन और लैपटॉप पर मेल पढ़ते हैं, जबकि POP3 सीमित सर्वर स्थान वाले एक ही कंप्यूटर के लिए। "
  "भेजने और पाने के प्रोटोकॉल अलग हैं: SMTP मेल को प्रेषक से प्राप्तकर्ता के सर्वर तक ले जाता है, और IMAP या POP3 उसे उस सर्वर से पाठक तक लाता है।",
  f"{CS12} (Computer Networks); {IP12} (Internet and Web, earlier editions).",
  "l1-sci-email-bcc-imap-pop3-smtp", craft="application")

S(IT, "medium", "Consider the following statements about cloud computing service models:",
  "क्लाउड कंप्यूटिंग के सेवा मॉडलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Software as a Service (SaaS), users use an application over the internet without installing it, as with web-based email.",
   "In Infrastructure as a Service (IaaS), users rent virtual machines, storage and networks.",
   "In Platform as a Service (PaaS), developers get the tools and environment to build and run applications without managing the servers beneath."],
  ["सॉफ़्टवेयर एज़ अ सर्विस (SaaS) में उपयोगकर्ता किसी अनुप्रयोग को स्थापित किए बिना इंटरनेट पर उपयोग करते हैं, जैसे वेब-आधारित ईमेल।",
   "इन्फ़्रास्ट्रक्चर एज़ अ सर्विस (IaaS) में उपयोगकर्ता आभासी मशीनें, भंडारण और नेटवर्क किराए पर लेते हैं।",
   "प्लेटफ़ॉर्म एज़ अ सर्विस (PaaS) में डेवलपरों को नीचे के सर्वरों का प्रबंधन किए बिना अनुप्रयोग बनाने और चलाने के उपकरण और परिवेश मिलते हैं।"],
  C3, 2,
  "All three statements are correct. The three models differ in how much the provider manages: in IaaS the customer looks after the operating system and everything above it, in PaaS only the application and its data, and in SaaS nothing but the use of the software. "
  "Cloud services let organisations pay for computing as they use it and scale up quickly, at the cost of depending on the provider and the network.",
  "तीनों कथन सही हैं। तीनों मॉडल इसमें भिन्न हैं कि प्रदाता कितना प्रबंधन करता है: IaaS में ग्राहक ऑपरेटिंग सिस्टम और उसके ऊपर सब कुछ देखता है, PaaS में केवल अनुप्रयोग और उसका डेटा, और SaaS में केवल सॉफ़्टवेयर का उपयोग। "
  "क्लाउड सेवाएँ संगठनों को उपयोग के अनुसार कंप्यूटिंग का भुगतान करने और तेज़ी से विस्तार करने देती हैं, प्रदाता और नेटवर्क पर निर्भरता की कीमत पर।",
  "Ministry of Electronics and Information Technology (cloud computing; MeghRaj); NCERT Class XI, Computer Science (Emerging Trends).",
  "l1-sci-saas-iaas-paas", craft="precision")

S(IT, "medium", "Consider the following statements about software and its use:",
  "सॉफ़्टवेयर और उसके उपयोग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Work released under a Creative Commons 'BY' licence may be reused, provided the creator is credited.",
   "Works in the public domain may be used by anyone without permission.",
   "'Free software' refers to the freedom to run, study, change and share it, not necessarily to its price.",
   "The source code of proprietary software is usually not available to its users."],
  ["क्रिएटिव कॉमन्स 'BY' लाइसेंस के अंतर्गत जारी कृति का पुनः उपयोग किया जा सकता है, बशर्ते रचनाकार को श्रेय दिया जाए।",
   "सार्वजनिक क्षेत्र (public domain) की कृतियों का उपयोग कोई भी बिना अनुमति के कर सकता है।",
   "'मुक्त सॉफ़्टवेयर' का संबंध उसे चलाने, अध्ययन करने, बदलने और साझा करने की स्वतंत्रता से है, आवश्यक नहीं कि उसकी कीमत से।",
   "स्वामित्व वाले (proprietary) सॉफ़्टवेयर का स्रोत कोड सामान्यतः उसके उपयोगकर्ताओं को उपलब्ध नहीं होता।"],
  C4, 3,
  "All four statements are correct. Creative Commons licences let creators choose which uses they allow -- with or without commercial use, modifications or share-alike terms -- while works enter the public domain when copyright expires or is given up. "
  "'Free' in free software means 'free as in freedom'; such software can be sold, and many companies earn money by supporting it.",
  "चारों कथन सही हैं। क्रिएटिव कॉमन्स लाइसेंस रचनाकारों को चुनने देते हैं कि वे कौन-से उपयोग अनुमत करें -- व्यावसायिक उपयोग, संशोधन या समान शर्तों पर साझा करने के साथ या बिना -- जबकि कृतियाँ कॉपीराइट समाप्त होने या छोड़ दिए जाने पर सार्वजनिक क्षेत्र में आती हैं। "
  "मुक्त सॉफ़्टवेयर में 'मुक्त' का अर्थ 'स्वतंत्रता' है; ऐसा सॉफ़्टवेयर बेचा जा सकता है, और कई कंपनियाँ उसकी सहायता सेवाएँ देकर कमाती हैं।",
  f"{IP12} (Societal Impacts).",
  "l1-sci-creative-commons-free-software", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(IT, "medium",
  "Data sent over the internet is broken into small packets.",
  "इंटरनेट पर भेजा गया डेटा छोटे पैकेटों में तोड़ा जाता है।",
  "Each packet carries the address of its destination.",
  "हर पैकेट अपने गंतव्य का पता लेकर चलता है।",
  1,
  "Both statements are correct, but Statement-II is not the correct explanation for Statement-I. Data is split into packets so that many users can share the same links at once and so that, if a link fails, packets can be sent another way; only lost packets need be sent again. "
  "Carrying the destination address is how each packet finds its way, not the reason the data is divided in the first place.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की सही व्याख्या नहीं है। डेटा पैकेटों में इसलिए बाँटा जाता है कि अनेक उपयोगकर्ता एक साथ एक ही संपर्कों को साझा कर सकें और कोई संपर्क टूटने पर पैकेट दूसरे मार्ग से भेजे जा सकें; केवल खोए पैकेट दोबारा भेजने पड़ते हैं। "
  "गंतव्य का पता ले चलना वह तरीक़ा है जिससे हर पैकेट अपना रास्ता पाता है, डेटा को बाँटने का कारण नहीं।",
  f"{CS12} (Computer Networks).",
  "l1-sci-packet-switching", craft="inference")

# ---------------------------------------------------------------- hard MCQ (1)
M(IT, "hard", "A 1.5 GB file is downloaded over a steady 100 Mbps connection. Taking 1 GB as 1,000 MB, the download takes about",
  "1.5 GB की एक फ़ाइल स्थिर 100 Mbps कनेक्शन पर डाउनलोड की जाती है। 1 GB को 1,000 MB मानते हुए, डाउनलोड में लगभग कितना समय लगेगा?",
  ["about 2 minutes", "about 15 seconds", "about 15 minutes", "about 20 minutes"],
  ["लगभग 2 मिनट", "लगभग 15 सेकंड", "लगभग 15 मिनट", "लगभग 20 मिनट"],
  0,
  "File sizes are measured in bytes (B) but connection speeds in bits per second (b), and one byte is eight bits. 1.5 GB = 1,500 MB = 12,000 megabits; at 100 megabits per second that takes 120 seconds, or 2 minutes. "
  "Forgetting the factor of eight gives 15 seconds -- the most common mistake when people judge how fast a connection really is.",
  "फ़ाइल का आकार बाइट (B) में पर कनेक्शन की गति बिट प्रति सेकंड (b) में मापी जाती है, और एक बाइट आठ बिट है। 1.5 GB = 1,500 MB = 12,000 मेगाबिट; 100 मेगाबिट प्रति सेकंड पर इसमें 120 सेकंड, यानी 2 मिनट लगते हैं। "
  "आठ का गुणक भूल जाने पर 15 सेकंड आता है -- यह जाँचने में सबसे आम भूल है कि कोई कनेक्शन वास्तव में कितना तेज़ है।",
  f"{CS11} (Encoding Schemes and Number System); {CS12} (Computer Networks).",
  "l1-sci-download-time-bits-bytes", pos=3, craft="application")

# ---------------------------------------------------------------- hard statement (2)
S(IT, "hard", "Consider the following statements about network addresses:",
  "नेटवर्क पतों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A MAC address is a hardware address assigned to a device's network interface.",
   "A device's IP address can change when it joins a different network.",
   "IP addresses are needed only by websites, not by users' own devices."],
  ["MAC पता किसी उपकरण के नेटवर्क इंटरफ़ेस को दिया गया हार्डवेयर पता है।",
   "किसी उपकरण का IP पता उसके किसी दूसरे नेटवर्क से जुड़ने पर बदल सकता है।",
   "IP पतों की आवश्यकता केवल वेबसाइटों को होती है, उपयोगकर्ताओं के अपने उपकरणों को नहीं।"],
  C3, 1,
  "Statements 1 and 2 are correct: the MAC address identifies a network card within a local network, while the IP address is a logical address that identifies where a device is on the internet, so a laptop taken from home to an office gets a new IP address. "
  "Statement 3 is wrong: every device that communicates over the internet needs an IP address, because replies must be sent back to it; many home devices share one public address through the router.",
  "कथन 1 और 2 सही हैं: MAC पता स्थानीय नेटवर्क के भीतर नेटवर्क कार्ड की पहचान करता है, जबकि IP पता एक तार्किक पता है जो बताता है कि उपकरण इंटरनेट पर कहाँ है, इसलिए घर से कार्यालय ले जाए गए लैपटॉप को नया IP पता मिलता है। "
  "कथन 3 गलत है: इंटरनेट पर संचार करने वाले हर उपकरण को IP पता चाहिए, क्योंकि उत्तर उसी को वापस भेजने होते हैं; घर के कई उपकरण राउटर के माध्यम से एक ही सार्वजनिक पता साझा करते हैं।",
  f"{CS12} (Computer Networks).",
  "l1-sci-mac-vs-ip-address", craft="precision")

S(IT, "hard", "Consider the following statements about the generations of computers:",
  "कंप्यूटरों की पीढ़ियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["First-generation computers used vacuum tubes.",
   "Second-generation computers used transistors in place of vacuum tubes.",
   "Third-generation computers were built with integrated circuits.",
   "Fourth-generation computers are based on microprocessors."],
  ["पहली पीढ़ी के कंप्यूटर निर्वात नलिकाओं (vacuum tubes) का उपयोग करते थे।",
   "दूसरी पीढ़ी के कंप्यूटरों में निर्वात नलिकाओं के स्थान पर ट्रांज़िस्टर प्रयुक्त हुए।",
   "तीसरी पीढ़ी के कंप्यूटर एकीकृत परिपथों (integrated circuits) से बने थे।",
   "चौथी पीढ़ी के कंप्यूटर माइक्रोप्रोसेसरों पर आधारित हैं।"],
  C4, 3,
  "All four statements are correct. Each step made computers smaller, cheaper, more reliable and less power-hungry: vacuum-tube machines such as ENIAC filled rooms and failed often, transistors and then integrated circuits shrank them, and the microprocessor -- a whole processor on one chip -- made personal computers possible. "
  "The steady growth in the number of transistors on a chip is what has driven computing ever since.",
  "चारों कथन सही हैं। हर चरण ने कंप्यूटरों को छोटा, सस्ता, अधिक विश्वसनीय और कम बिजली वाला बनाया: ENIAC जैसी निर्वात-नलिका मशीनें पूरे कमरे भरती थीं और अक्सर ख़राब होती थीं, ट्रांज़िस्टरों और फिर एकीकृत परिपथों ने उन्हें छोटा किया, और माइक्रोप्रोसेसर -- एक ही चिप पर पूरा प्रोसेसर -- ने निजी कंप्यूटर संभव बनाए। "
  "चिप पर ट्रांज़िस्टरों की संख्या में निरंतर वृद्धि ही तब से कंप्यूटिंग को आगे बढ़ाती रही है।",
  f"{CS11} (Computer System, earlier editions).",
  "l1-sci-computer-generations", craft="recall")

write("sci_l1_t6_d.sql")
