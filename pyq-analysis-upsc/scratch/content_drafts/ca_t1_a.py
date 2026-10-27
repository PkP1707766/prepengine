# -*- coding: utf-8 -*-
"""Current Affairs · Test 1 (January to March 2026) -- part A: Current Affairs proper (International, National,
Defence, Schemes & Indices, Sports).

Every question starts from an event of January-March 2026, or an anniversary that falls in those months, and asks
the static knowledge it points to, as the real paper does. Event facts were checked against official releases
(PIB, MEA, MHA, ISRO, the UN bodies) or several independent reports; the static facts are from the treaties,
Acts and NCERT. Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests.
Concept prefix ca-t1-."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t1_format import FORMAT, POS

d.SUBJECT = "Current Affairs"
d.REQUIRE_CRAFT = True
IN, NA, DF, SC, SP = "International", "National", "Defence", "Schemes & Indices", "Sports"

# ================================================================ INTERNATIONAL
S(IN, "medium", "With reference to the India–European Union Free Trade Agreement, consider the following statements:",
  "भारत–यूरोपीय संघ मुक्त व्यापार समझौते के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Negotiations on it were concluded at an India–EU Summit held in New Delhi in January 2026.",
   "Under the EU treaties, trade policy is an exclusive competence of the Union, so the European Commission negotiates such agreements on behalf of all the member states.",
   "Once its negotiations were concluded, the agreement entered into force at once, without any further approval within the EU."],
  ["इस पर वार्ता जनवरी 2026 में नई दिल्ली में आयोजित भारत–यूरोपीय संघ शिखर सम्मेलन में संपन्न हुई।",
   "यूरोपीय संघ की संधियों के अंतर्गत व्यापार नीति संघ की अनन्य क्षमता है, इसलिए ऐसे समझौतों पर सभी सदस्य देशों की ओर से यूरोपीय आयोग वार्ता करता है।",
   "वार्ता संपन्न होते ही यह समझौता यूरोपीय संघ के भीतर किसी और अनुमोदन के बिना तुरंत लागू हो गया।"],
  C3, 1,
  "Statements 1 and 2 are correct. The talks, launched in 2007, suspended in 2013 and relaunched in 2022, were concluded on 27 January 2026 at the 16th India–EU Summit in New Delhi -- the day after the leaders of the EU institutions had been the chief guests at the Republic Day parade. The EU treaties make the common commercial policy an exclusive competence of the Union: the Commission negotiates on a mandate from the Council of the EU, and the Council concludes the agreement with the consent of the European Parliament, which is why one negotiator speaks for all 27 members. "
  "Statement 3 is wrong: concluding negotiations is not entry into force. The text still has to be legally checked, translated, signed and approved by the Council and the European Parliament on the EU side, and the agreement takes effect only after both parties complete their procedures.",
  "कथन 1 और 2 सही हैं। 2007 में शुरू हुई, 2013 में रुकी और 2022 में फिर शुरू हुई वार्ता 27 जनवरी 2026 को नई दिल्ली में 16वें भारत–यूरोपीय संघ शिखर सम्मेलन में संपन्न हुई -- उससे एक दिन पहले यूरोपीय संघ की संस्थाओं के नेता गणतंत्र दिवस परेड के मुख्य अतिथि थे। यूरोपीय संघ की संधियाँ साझा वाणिज्यिक नीति को संघ की अनन्य क्षमता बनाती हैं: आयोग यूरोपीय संघ की परिषद से मिले अधिदेश पर वार्ता करता है, और परिषद यूरोपीय संसद की सहमति से समझौता संपन्न करती है, इसीलिए सभी 27 सदस्यों की ओर से एक ही वार्ताकार बोलता है। "
  "कथन 3 ग़लत है: वार्ता का संपन्न होना समझौते का लागू होना नहीं है। पाठ की अभी विधिक जाँच, अनुवाद और हस्ताक्षर होने हैं तथा यूरोपीय संघ की ओर से परिषद और यूरोपीय संसद का अनुमोदन चाहिए, और समझौता तभी प्रभावी होता है जब दोनों पक्ष अपनी प्रक्रियाएँ पूरी कर लें।",
  "Ministry of Commerce and Industry and European Commission, joint statements on the conclusion of the India–EU FTA (27 January 2026); Treaty on the Functioning of the European Union, Articles 3 and 207.",
  "ca-t1-ca-india-eu-fta-exclusive-competence", craft="linkage")

M(IN, "medium",
  "The President of the European Council was one of the chief guests at India's Republic Day in 2026. The European Council is best described as:",
  "यूरोपीय परिषद के अध्यक्ष 2026 में भारत के गणतंत्र दिवस के मुख्य अतिथियों में से एक थे। यूरोपीय परिषद का सबसे उपयुक्त वर्णन है:",
  ["the body of the EU member states' heads of state or government, which sets the Union's political direction",
   "the Union's legislature, whose members are elected directly by the citizens of the member states every five years",
   "the executive arm of the Union, which proposes new laws and negotiates the Union's trade agreements",
   "an organisation of European states, separate from the EU, whose court of human rights sits at Strasbourg"],
  ["सदस्य देशों के राष्ट्राध्यक्षों या शासनाध्यक्षों का निकाय, जो संघ की राजनीतिक दिशा तय करता है",
   "संघ का विधानमंडल, जिसके सदस्य हर पाँच वर्ष पर सदस्य देशों के नागरिकों द्वारा सीधे चुने जाते हैं",
   "संघ की कार्यकारी शाखा, जो नए क़ानून प्रस्तावित करती है और संघ के व्यापार समझौतों पर वार्ता करती है",
   "यूरोपीय संघ से अलग यूरोपीय देशों का एक संगठन, जिसका मानवाधिकार न्यायालय स्ट्रासबर्ग में बैठता है"],
  0,
  "The European Council brings together the heads of state or government of the 27 member states, with its own President (António Costa since December 2024) and the President of the European Commission; it defines the EU's general political direction and priorities but does not pass laws. "
  "The second option describes the European Parliament, the directly elected legislature. The third describes the European Commission (led by Ursula von der Leyen, the other chief guest), which proposes legislation and negotiates trade deals such as the one concluded with India the next day. The fourth describes the Council of Europe, a separate organisation founded in 1949 whose European Court of Human Rights sits at Strasbourg. Three similar names -- the European Council, the Council of the EU (ministers of the member states) and the Council of Europe -- are a classic trap.",
  "यूरोपीय परिषद 27 सदस्य देशों के राष्ट्राध्यक्षों या शासनाध्यक्षों को, अपने अध्यक्ष (दिसंबर 2024 से अंतोनियो कोस्टा) और यूरोपीय आयोग की अध्यक्ष के साथ, एक साथ लाती है; वह यूरोपीय संघ की सामान्य राजनीतिक दिशा और प्राथमिकताएँ तय करती है, पर क़ानून पारित नहीं करती। "
  "दूसरा विकल्प यूरोपीय संसद का वर्णन है, जो सीधे चुना गया विधानमंडल है। तीसरा यूरोपीय आयोग का वर्णन है (जिसकी प्रमुख उर्सुला फ़ॉन डेर लेयेन दूसरी मुख्य अतिथि थीं), जो विधान प्रस्तावित करता है और अगले दिन भारत के साथ संपन्न हुए जैसे व्यापार समझौतों पर वार्ता करता है। चौथा यूरोप परिषद (काउंसिल ऑफ़ यूरोप) का वर्णन है, जो 1949 में बना एक अलग संगठन है और जिसका यूरोपीय मानवाधिकार न्यायालय स्ट्रासबर्ग में बैठता है। तीन मिलते-जुलते नाम -- यूरोपीय परिषद, यूरोपीय संघ की परिषद (सदस्य देशों के मंत्री) और यूरोप परिषद -- एक पुराना जाल हैं।",
  "Treaty on European Union, Articles 13-17; Ministry of External Affairs, Republic Day 2026 chief guests; Council of Europe, Statute (1949).",
  "ca-t1-ca-european-council-three-councils", pos=POS.get("ca-t1-ca-european-council-three-councils", 1), craft="precision")

S(IN, "hard", "The United States' withdrawal from the Paris Agreement took effect in January 2026. With reference to withdrawal from international treaties and bodies, consider the following statements:",
  "जनवरी 2026 में पेरिस समझौते से संयुक्त राज्य अमेरिका का हटना प्रभावी हुआ। अंतरराष्ट्रीय संधियों और निकायों से हटने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Paris Agreement, a Party's withdrawal takes effect one year after the depositary receives its notification.",
   "A Party that withdraws from the UN Framework Convention on Climate Change still remains a Party to the Paris Agreement.",
   "The Constitution of the World Health Organization lays down a procedure under which any member may withdraw after giving one year's notice."],
  ["पेरिस समझौते के अंतर्गत किसी पक्षकार का हटना निक्षेपधारी को उसकी सूचना मिलने के एक वर्ष बाद प्रभावी होता है।",
   "जलवायु परिवर्तन पर संयुक्त राष्ट्र फ़्रेमवर्क अभिसमय से हटने वाला पक्षकार फिर भी पेरिस समझौते का पक्षकार बना रहता है।",
   "विश्व स्वास्थ्य संगठन का संविधान एक प्रक्रिया निर्धारित करता है जिसके अंतर्गत कोई भी सदस्य एक वर्ष की सूचना देकर हट सकता है।"],
  C3, 0,
  "Only statement 1 is correct. Under Article 28 of the Paris Agreement a Party may give notice only after three years from the Agreement's entry into force for it, and the withdrawal takes effect one year after the depositary (the UN Secretary-General) receives the notification -- which is why the notice given on 27 January 2025 took effect on 27 January 2026. "
  "Statement 2 is wrong: Article 28(3) provides that withdrawing from the UNFCCC is deemed to be withdrawal from the Paris Agreement as well, since the Agreement sits under the Convention. Statement 3 is wrong: the WHO Constitution has no general withdrawal clause at all; the United States joined in 1948 with a reservation, approved by Congress, that it could leave on one year's notice after paying its dues, and on that basis its exit, notified in January 2025, took effect on 22 January 2026. A presidential memorandum of 7 January 2026 also directed withdrawal from 66 other international organisations.",
  "केवल कथन 1 सही है। पेरिस समझौते के अनुच्छेद 28 के अंतर्गत कोई पक्षकार अपने लिए समझौता लागू होने के तीन वर्ष बाद ही सूचना दे सकता है, और हटना निक्षेपधारी (संयुक्त राष्ट्र महासचिव) को सूचना मिलने के एक वर्ष बाद प्रभावी होता है -- इसीलिए 27 जनवरी 2025 को दी गई सूचना 27 जनवरी 2026 को प्रभावी हुई। "
  "कथन 2 ग़लत है: अनुच्छेद 28(3) कहता है कि यूएनएफ़सीसीसी से हटना पेरिस समझौते से हटना भी माना जाएगा, क्योंकि समझौता अभिसमय के अधीन है। कथन 3 ग़लत है: विश्व स्वास्थ्य संगठन के संविधान में हटने का कोई सामान्य उपबंध ही नहीं है; संयुक्त राज्य अमेरिका 1948 में कांग्रेस द्वारा अनुमोदित इस आरक्षण के साथ शामिल हुआ था कि वह अपना अंशदान चुकाकर एक वर्ष की सूचना पर हट सकेगा, और इसी आधार पर जनवरी 2025 में सूचित उसका निकास 22 जनवरी 2026 को प्रभावी हुआ। 7 जनवरी 2026 के एक राष्ट्रपति ज्ञापन ने 66 अन्य अंतरराष्ट्रीय संगठनों से हटने का निर्देश भी दिया।",
  "Paris Agreement (2015), Article 28; UNFCCC (1992), Article 25; Constitution of the World Health Organization (1946); UNFCCC secretariat and WHO statements, January 2026.",
  "ca-t1-ca-paris-who-withdrawal-mechanics", craft="precision")

S(IN, "medium", "With reference to nuclear arms control between the United States and Russia, consider the following statements:",
  "संयुक्त राज्य अमेरिका और रूस के बीच परमाणु शस्त्र नियंत्रण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The New START Treaty, which expired in February 2026, limited each side to 1,550 deployed strategic nuclear warheads.",
   "The Intermediate-Range Nuclear Forces Treaty, which banned ground-launched missiles with ranges of 500 to 5,500 km, ceased to bind the two after the United States withdrew from it in 2019.",
   "Russia had announced in 2023 that it was suspending its participation in New START."],
  ["फ़रवरी 2026 में समाप्त हुई न्यू स्टार्ट संधि ने प्रत्येक पक्ष को 1,550 तैनात सामरिक परमाणु आयुधों तक सीमित किया था।",
   "500 से 5,500 किमी मारक दूरी वाली ज़मीन से छोड़ी जाने वाली मिसाइलों पर प्रतिबंध लगाने वाली मध्यम-दूरी परमाणु बल संधि 2019 में संयुक्त राज्य अमेरिका के उससे हटने के बाद दोनों पर बाध्यकारी नहीं रही।",
   "रूस ने 2023 में घोषणा की थी कि वह न्यू स्टार्ट में अपनी भागीदारी निलंबित कर रहा है।"],
  C3, 2,
  "All three statements are correct. New START, signed at Prague in 2010 and extended in 2021 for five years, capped each side at 1,550 deployed strategic warheads, 700 deployed intercontinental and submarine-launched ballistic missiles and heavy bombers, and 800 deployed and non-deployed launchers. It expired on 5 February 2026 with no successor, leaving the two largest arsenals without any treaty limit for the first time since the SALT agreements of 1972; Russia said it would keep to the old numbers only if the United States did. "
  "The INF Treaty of 1987 eliminated a whole class of missiles, but the United States withdrew in 2019 accusing Russia of violating it. Russia's 2023 suspension of New START had already ended data exchanges and inspections, so verification had lapsed well before the expiry.",
  "तीनों कथन सही हैं। 2010 में प्राग में हस्ताक्षरित और 2021 में पाँच वर्ष के लिए बढ़ाई गई न्यू स्टार्ट ने प्रत्येक पक्ष को 1,550 तैनात सामरिक आयुधों, 700 तैनात अंतरमहाद्वीपीय और पनडुब्बी-प्रक्षेपित बैलिस्टिक मिसाइलों और भारी बमवर्षकों, तथा 800 तैनात और अतैनात प्रक्षेपकों तक सीमित किया था। यह 5 फ़रवरी 2026 को बिना किसी उत्तराधिकारी संधि के समाप्त हो गई, जिससे 1972 के साल्ट समझौतों के बाद पहली बार दोनों सबसे बड़े शस्त्रागारों पर कोई संधि-सीमा नहीं रही; रूस ने कहा कि वह पुरानी संख्याओं का पालन तभी करेगा जब अमेरिका भी करे। "
  "1987 की आईएनएफ़ संधि ने मिसाइलों की एक पूरी श्रेणी समाप्त की थी, पर संयुक्त राज्य अमेरिका ने रूस पर उल्लंघन का आरोप लगाकर 2019 में उससे हटना तय किया। 2023 में रूस के न्यू स्टार्ट निलंबन ने आँकड़ों का आदान-प्रदान और निरीक्षण पहले ही बंद कर दिए थे, इसलिए सत्यापन समाप्ति से बहुत पहले ठप हो चुका था।",
  "Treaty on Measures for the Further Reduction and Limitation of Strategic Offensive Arms (New START, 2010), Article II; INF Treaty (1987); Ministry of Foreign Affairs of the Russian Federation, statement of 5 February 2026.",
  "ca-t1-ca-new-start-expiry-inf", craft="linkage")

S(IN, "medium", "India holds the chairship of BRICS in 2026. Consider the following statements:",
  "2026 में ब्रिक्स की अध्यक्षता भारत के पास है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The theme of India's chairship is 'Building for Resilience, Innovation, Cooperation and Sustainability'.",
   "BRICS has a permanent secretariat located in Shanghai.",
   "The category of 'partner countries' was created at the Kazan summit in 2024.",
   "The first summit of the BRIC leaders was held in 2006."],
  ["भारत की अध्यक्षता का विषय ‘लचीलेपन, नवाचार, सहयोग और स्थिरता के लिए निर्माण’ है।",
   "ब्रिक्स का शंघाई में एक स्थायी सचिवालय है।",
   "‘साझेदार देशों’ की श्रेणी 2024 के कज़ान शिखर सम्मेलन में बनाई गई।",
   "ब्रिक नेताओं का पहला शिखर सम्मेलन 2006 में हुआ था।"],
  C4, 1,
  "Statements 1 and 3 are correct. The External Affairs Minister released the theme, a lotus logo and the website on 13 January 2026; the theme spells out resilience, innovation, cooperation and sustainability. The Kazan summit of 2024 created a 'partner country' tier below full membership for states that had applied to join. "
  "Statement 2 is wrong: BRICS has no secretariat at all -- the chair rotates each year and runs the calendar. Shanghai is the headquarters of the New Development Bank, an institution the BRICS countries set up. Statement 4 is wrong: 2006 is when the foreign ministers of Brazil, Russia, India and China first met as a group, on the sidelines of the UN General Assembly, which is why 2026 is counted as BRICS's twentieth year; the first leaders' summit was held at Yekaterinburg in 2009.",
  "कथन 1 और 3 सही हैं। विदेश मंत्री ने 13 जनवरी 2026 को विषय, कमल वाला प्रतीक-चिह्न और वेबसाइट जारी की; विषय लचीलापन, नवाचार, सहयोग और स्थिरता को सामने रखता है। 2024 के कज़ान शिखर सम्मेलन ने सदस्यता के लिए आवेदन करने वाले देशों के लिए पूर्ण सदस्यता से नीचे ‘साझेदार देश’ का स्तर बनाया। "
  "कथन 2 ग़लत है: ब्रिक्स का कोई सचिवालय है ही नहीं -- अध्यक्षता हर वर्ष बदलती है और वही कार्यक्रम चलाती है। शंघाई न्यू डेवलपमेंट बैंक का मुख्यालय है, जिसे ब्रिक्स देशों ने बनाया। कथन 4 ग़लत है: 2006 में ब्राज़ील, रूस, भारत और चीन के विदेश मंत्री पहली बार संयुक्त राष्ट्र महासभा के अवसर पर एक समूह के रूप में मिले थे, इसीलिए 2026 को ब्रिक्स का बीसवाँ वर्ष माना जाता है; नेताओं का पहला शिखर सम्मेलन 2009 में येकातेरिनबर्ग में हुआ।",
  "Ministry of External Affairs, release on India's BRICS Chairship 2026 (13 January 2026); Kazan Declaration (2024).",
  "ca-t1-ca-brics-2026-chairship-no-secretariat", craft="precision")

S(IN, "medium", "The AI Impact Summit held in New Delhi in February 2026 was the fourth in a series of global summits on artificial intelligence. Consider the following statements about the series:",
  "फ़रवरी 2026 में नई दिल्ली में आयोजित एआई इम्पैक्ट शिखर सम्मेलन कृत्रिम बुद्धिमत्ता पर वैश्विक शिखर सम्मेलनों की शृंखला में चौथा था। इस शृंखला के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The New Delhi summit was the first of the series to be hosted in the Global South.",
   "The summit of 2024 was hosted jointly by the Republic of Korea and the United Kingdom.",
   "The series began with a summit hosted by France in 2023."],
  ["नई दिल्ली शिखर सम्मेलन शृंखला का पहला था जिसकी मेज़बानी वैश्विक दक्षिण में हुई।",
   "2024 के शिखर सम्मेलन की मेज़बानी कोरिया गणराज्य और यूनाइटेड किंगडम ने संयुक्त रूप से की।",
   "शृंखला 2023 में फ़्रांस द्वारा आयोजित एक शिखर सम्मेलन से शुरू हुई।"],
  C3, 1,
  "Statements 1 and 2 are correct. The AI Seoul Summit of May 2024 was co-hosted by the Republic of Korea and the United Kingdom, and New Delhi was the first host outside the developed world, using the summit to put access, development and the Global South at the centre of the agenda. "
  "Statement 3 is wrong: the series began with the AI Safety Summit hosted by the United Kingdom at Bletchley Park in November 2023, focused on the risks of frontier models. France hosted the third, the AI Action Summit of February 2025, which India co-chaired -- the shift in the summits' very names, from safety to action to impact, traces how the agenda widened.",
  "कथन 1 और 2 सही हैं। मई 2024 के एआई सोल शिखर सम्मेलन की सह-मेज़बानी कोरिया गणराज्य और यूनाइटेड किंगडम ने की, और नई दिल्ली विकसित देशों से बाहर पहला मेज़बान था, जिसने शिखर सम्मेलन में पहुँच, विकास और वैश्विक दक्षिण को एजेंडा के केंद्र में रखा। "
  "कथन 3 ग़लत है: शृंखला नवंबर 2023 में यूनाइटेड किंगडम द्वारा ब्लेचली पार्क में आयोजित एआई सुरक्षा शिखर सम्मेलन से शुरू हुई, जिसका ध्यान अग्रणी मॉडलों के जोखिमों पर था। फ़्रांस ने तीसरे, फ़रवरी 2025 के एआई एक्शन शिखर सम्मेलन, की मेज़बानी की, जिसकी सह-अध्यक्षता भारत ने की -- शिखर सम्मेलनों के नामों का ही बदलना, सुरक्षा से कार्रवाई और फिर प्रभाव तक, दिखाता है कि एजेंडा कैसे व्यापक हुआ।",
  "Ministry of Electronics and Information Technology, IndiaAI, AI Impact Summit 2026 releases (February 2026); Government of the United Kingdom, AI Safety Summit (2023) and AI Seoul Summit (2024); Élysée and MEA, AI Action Summit, Paris (February 2025).",
  "ca-t1-ca-ai-summit-series-hosts", craft="recall")

S(IN, "hard", "Nepal elected a new House of Representatives in March 2026. With reference to Nepal's Constitution of 2015, consider the following statements:",
  "मार्च 2026 में नेपाल ने नई प्रतिनिधि सभा चुनी। नेपाल के 2015 के संविधान के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Of the 275 members of the House of Representatives, 165 are elected from single-member constituencies and 110 by proportional representation.",
   "The President of Nepal is elected directly by the people.",
   "Nepal's federal Parliament is unicameral."],
  ["प्रतिनिधि सभा के 275 सदस्यों में से 165 एकल-सदस्यीय निर्वाचन क्षेत्रों से और 110 आनुपातिक प्रतिनिधित्व से चुने जाते हैं।",
   "नेपाल के राष्ट्रपति सीधे जनता द्वारा चुने जाते हैं।",
   "नेपाल की संघीय संसद एकसदनीय है।"],
  C3, 0,
  "Only statement 1 is correct. Nepal uses a mixed system: of the 275 members of the House of Representatives, 165 are elected by first-past-the-post in single-member constituencies and 110 by proportional representation, with the national vote for parties deciding the second share. Statement 2 is wrong: the President is elected indirectly, by an electoral college of the members of the federal Parliament and of the seven Provincial Assemblies. Statement 3 is wrong: the federal Parliament is bicameral, with the 59-member National Assembly as its upper house. "
  "The March 2026 election, the first after the youth-led protests of September 2025 brought down the previous government, gave the Rastriya Swatantra Party a clear majority, and Balendra Shah, a former mayor of Kathmandu, became Prime Minister.",
  "केवल कथन 1 सही है। नेपाल मिश्रित प्रणाली अपनाता है: प्रतिनिधि सभा के 275 सदस्यों में से 165 एकल-सदस्यीय निर्वाचन क्षेत्रों से सर्वाधिक-मत प्रणाली से और 110 आनुपातिक प्रतिनिधित्व से चुने जाते हैं, जिनका बँटवारा दलों को मिले राष्ट्रीय मतों से तय होता है। कथन 2 ग़लत है: राष्ट्रपति अप्रत्यक्ष रूप से, संघीय संसद और सात प्रांतीय सभाओं के सदस्यों के निर्वाचक मंडल द्वारा चुने जाते हैं। कथन 3 ग़लत है: संघीय संसद द्विसदनीय है, जिसका उच्च सदन 59 सदस्यीय राष्ट्रीय सभा है। "
  "मार्च 2026 का चुनाव, जो सितंबर 2025 के युवा-नेतृत्व वाले आंदोलनों से पिछली सरकार गिरने के बाद पहला था, राष्ट्रीय स्वतंत्र पार्टी को स्पष्ट बहुमत दे गया, और काठमांडू के पूर्व महापौर बालेन्द्र शाह प्रधानमंत्री बने।",
  "Constitution of Nepal (2015), Articles 62, 76, 84 and 86; Election Commission of Nepal, results of the House of Representatives election (March 2026).",
  "ca-t1-ca-nepal-mixed-system-indirect-president", craft="precision")

S(IN, "medium", "Bangladesh held a general election and a referendum on the same day in February 2026. Consider the following statements:",
  "फ़रवरी 2026 में बांग्लादेश ने एक ही दिन आम चुनाव और जनमत-संग्रह कराया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bangladesh's Parliament, the Jatiya Sangsad, is unicameral, with 300 directly elected seats and 50 seats reserved for women.",
   "The 'July Charter' that was put to the referendum proposes, among other reforms, an upper house of Parliament."],
  ["बांग्लादेश की संसद, जातीय संसद, एकसदनीय है, जिसमें 300 सीधे चुनी गई सीटें और महिलाओं के लिए आरक्षित 50 सीटें हैं।",
   "जनमत-संग्रह में रखा गया ‘जुलाई चार्टर’ अन्य सुधारों के साथ संसद के एक उच्च सदन का प्रस्ताव करता है।"],
  T2, 2,
  "Both statements are correct. The Jatiya Sangsad has a single house of 350: 300 members elected from territorial constituencies and 50 women's seats filled by the parties in proportion to their strength. The July National Charter -- named after the uprising of July 2024 that ended Sheikh Hasina's government -- bundles reforms such as a 100-member upper house filled by proportional representation and term limits for the Prime Minister; voters backed it in the referendum held alongside the election of 12 February 2026. "
  "The election itself gave the Bangladesh Nationalist Party a large majority, and Tarique Rahman became Prime Minister -- the setting for the 'reset' in India–Bangladesh relations that followed.",
  "दोनों कथन सही हैं। जातीय संसद 350 सदस्यों का एक ही सदन है: 300 सदस्य प्रादेशिक निर्वाचन क्षेत्रों से चुने जाते हैं और महिलाओं की 50 सीटें दल अपनी संख्या के अनुपात में भरते हैं। जुलाई राष्ट्रीय चार्टर -- जिसका नाम जुलाई 2024 के उस विद्रोह पर है जिसने शेख़ हसीना की सरकार समाप्त की -- आनुपातिक प्रतिनिधित्व से भरे जाने वाले 100 सदस्यीय उच्च सदन और प्रधानमंत्री के कार्यकाल की सीमा जैसे सुधारों को एक साथ रखता है; 12 फ़रवरी 2026 के चुनाव के साथ हुए जनमत-संग्रह में मतदाताओं ने इसका समर्थन किया। "
  "चुनाव ने स्वयं बांग्लादेश नेशनलिस्ट पार्टी को बड़ा बहुमत दिया, और तारिक़ रहमान प्रधानमंत्री बने -- यही उसके बाद भारत–बांग्लादेश संबंधों में आए ‘नए आरंभ’ की पृष्ठभूमि है।",
  "Constitution of the People's Republic of Bangladesh, Article 65; Bangladesh Election Commission, results of the 13th parliamentary election and referendum (February 2026); Ministry of External Affairs statements.",
  "ca-t1-ca-bangladesh-jatiya-sangsad-july-charter", craft="linkage")

S(IN, "medium", "The process of selecting the next Secretary-General of the United Nations, who takes office in 2027, began in late 2025. Consider the following statements:",
  "संयुक्त राष्ट्र के अगले महासचिव, जो 2027 में पदभार ग्रहण करेंगे, के चयन की प्रक्रिया 2025 के अंत में शुरू हुई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Secretary-General is appointed by the General Assembly on the recommendation of the Security Council.",
   "The UN Charter fixes the Secretary-General's term at five years, renewable once.",
   "By a rule of the Charter, the post rotates among the UN's regional groups, and the 2027 term is reserved for Latin America."],
  ["महासचिव की नियुक्ति सुरक्षा परिषद की सिफ़ारिश पर महासभा करती है।",
   "संयुक्त राष्ट्र चार्टर महासचिव का कार्यकाल पाँच वर्ष तय करता है, जिसे एक बार बढ़ाया जा सकता है।",
   "चार्टर के एक नियम के अनुसार यह पद संयुक्त राष्ट्र के क्षेत्रीय समूहों में बारी-बारी से जाता है, और 2027 का कार्यकाल लैटिन अमेरिका के लिए आरक्षित है।"],
  C3, 0,
  "Only statement 1 is correct. Article 97 of the Charter says the Secretary-General is 'appointed by the General Assembly upon the recommendation of the Security Council'; the Council's recommendation is subject to the veto, so each permanent member can block a candidate. Statement 2 is wrong: the Charter says nothing about the term -- a five-year term was set by a General Assembly resolution of 1946, and re-appointment has been by practice. "
  "Statement 3 is wrong: the Charter does not provide for regional rotation. Many members argue that it is Latin America's 'turn' and that a woman should be chosen for the first time, and General Assembly resolutions encourage regional diversity and gender balance, but these are expectations, not rules. Candidates nominated by member states up to March 2026 included Rafael Grossi, Director General of the IAEA, Michelle Bachelet, a former President of Chile, and Rebeca Grynspan, the Secretary-General of UN Trade and Development.",
  "केवल कथन 1 सही है। चार्टर का अनुच्छेद 97 कहता है कि महासचिव ‘सुरक्षा परिषद की सिफ़ारिश पर महासभा द्वारा नियुक्त’ किए जाते हैं; परिषद की सिफ़ारिश पर वीटो लागू होता है, इसलिए हर स्थायी सदस्य किसी उम्मीदवार को रोक सकता है। कथन 2 ग़लत है: चार्टर कार्यकाल के बारे में कुछ नहीं कहता -- पाँच वर्ष का कार्यकाल 1946 के महासभा के एक संकल्प से तय हुआ, और पुनर्नियुक्ति परिपाटी से होती आई है। "
  "कथन 3 ग़लत है: चार्टर क्षेत्रीय बारी का कोई प्रावधान नहीं करता। अनेक सदस्यों का तर्क है कि अब लैटिन अमेरिका की ‘बारी’ है और पहली बार किसी महिला को चुना जाना चाहिए, और महासभा के संकल्प क्षेत्रीय विविधता और लैंगिक संतुलन को प्रोत्साहित करते हैं, पर ये अपेक्षाएँ हैं, नियम नहीं। मार्च 2026 तक सदस्य देशों द्वारा नामित उम्मीदवारों में आईएईए के महानिदेशक राफ़ेल ग्रोसी, चिली की पूर्व राष्ट्रपति मिशेल बाचेलेट और संयुक्त राष्ट्र व्यापार और विकास की महासचिव रेबेका ग्रिंसपैन शामिल थे।",
  "Charter of the United Nations, Article 97; General Assembly resolutions 11(I) (1946) and 79/327 (2025); joint letter of the Presidents of the General Assembly and the Security Council (25 November 2025).",
  "ca-t1-ca-unsg-selection-article-97", craft="precision")

S(IN, "easy", "January 2026 marked eighty years since the first session of the UN General Assembly. Consider the following statements:",
  "जनवरी 2026 में संयुक्त राष्ट्र महासभा के पहले सत्र के अस्सी वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first session of the General Assembly opened in London.",
   "India was among the original members of the United Nations although it was not yet independent.",
   "The first woman to preside over the General Assembly was an Indian."],
  ["महासभा का पहला सत्र लंदन में शुरू हुआ था।",
   "भारत, स्वतंत्र न होते हुए भी, संयुक्त राष्ट्र के मूल सदस्यों में था।",
   "महासभा की अध्यक्षता करने वाली पहली महिला एक भारतीय थीं।"],
  C3, 2,
  "All three statements are correct. The first session of the General Assembly opened on 10 January 1946 at the Methodist Central Hall in London, with 51 members; the Security Council met for the first time in London a week later, and the UN moved to New York only afterwards. "
  "India had signed the Declaration by United Nations in 1942 and the Charter at San Francisco on 26 June 1945, so it became an original member while still under British rule. In 1953 Vijaya Lakshmi Pandit was elected President of the eighth session, the first woman to hold the office.",
  "तीनों कथन सही हैं। महासभा का पहला सत्र 10 जनवरी 1946 को लंदन के मेथोडिस्ट सेंट्रल हॉल में 51 सदस्यों के साथ शुरू हुआ; सुरक्षा परिषद की पहली बैठक एक सप्ताह बाद लंदन में हुई, और संयुक्त राष्ट्र उसके बाद ही न्यूयॉर्क गया। "
  "भारत ने 1942 में संयुक्त राष्ट्र घोषणा पर और 26 जून 1945 को सैन फ़्रांसिस्को में चार्टर पर हस्ताक्षर किए थे, इसलिए ब्रिटिश शासन के अधीन रहते हुए ही वह मूल सदस्य बना। 1953 में विजयलक्ष्मी पंडित आठवें सत्र की अध्यक्ष चुनी गईं, यह पद संभालने वाली पहली महिला।",
  "United Nations, history of the General Assembly and list of Presidents of the General Assembly; Charter of the United Nations, Article 3.",
  "ca-t1-ca-unga-eighty-years-first-session", craft="recall")

S(IN, "medium", "India joined 'Pax Silica' in February 2026. Consider the following statements about it:",
  "भारत फ़रवरी 2026 में ‘पैक्स सिलिका’ में शामिल हुआ। इसके बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a United States-led initiative to build secure supply chains for semiconductors, artificial intelligence and critical minerals.",
   "India was one of its founding members when it was launched in December 2025.",
   "It is a treaty-based military alliance with a mutual-defence clause, modelled on NATO."],
  ["यह सेमीकंडक्टर, कृत्रिम बुद्धिमत्ता और महत्त्वपूर्ण खनिजों की सुरक्षित आपूर्ति शृंखलाएँ बनाने की संयुक्त राज्य अमेरिका के नेतृत्व वाली पहल है।",
   "दिसंबर 2025 में इसकी शुरुआत के समय भारत इसके संस्थापक सदस्यों में था।",
   "यह नाटो की तर्ज़ पर बना, पारस्परिक रक्षा उपबंध वाला संधि-आधारित सैन्य गठबंधन है।"],
  C3, 0,
  "Only statement 1 is correct. The United States launched Pax Silica in December 2025 to coordinate trusted supply chains for chips, AI infrastructure and the critical minerals they depend on, with a first group of mostly high-income allies. Statement 2 is wrong: India was not among them -- the US announced in January 2026 that India would join, and India signed on 20 February 2026 on the sidelines of the AI Impact Summit in New Delhi, the first developing country in the group. "
  "Statement 3 is wrong: Pax Silica is a declaration of economic and technological cooperation, not a defence treaty; India presented its joining as consistent with its strategic autonomy.",
  "केवल कथन 1 सही है। संयुक्त राज्य अमेरिका ने दिसंबर 2025 में पैक्स सिलिका की शुरुआत चिप, एआई अवसंरचना और उन पर निर्भर महत्त्वपूर्ण खनिजों की विश्वसनीय आपूर्ति शृंखलाओं के समन्वय के लिए की, जिसमें पहला समूह अधिकतर उच्च-आय वाले सहयोगियों का था। कथन 2 ग़लत है: भारत उनमें नहीं था -- अमेरिका ने जनवरी 2026 में घोषणा की कि भारत शामिल होगा, और भारत ने 20 फ़रवरी 2026 को नई दिल्ली में एआई इम्पैक्ट शिखर सम्मेलन के अवसर पर हस्ताक्षर किए, इस समूह का पहला विकासशील देश बनकर। "
  "कथन 3 ग़लत है: पैक्स सिलिका आर्थिक और प्रौद्योगिकीय सहयोग की घोषणा है, रक्षा संधि नहीं; भारत ने अपने शामिल होने को अपनी सामरिक स्वायत्तता के अनुरूप बताया।",
  "Ministry of Electronics and Information Technology, release on India joining Pax Silica (20 February 2026); US Department of State, Pax Silica Declaration (December 2025).",
  "ca-t1-ca-pax-silica-india-joins", craft="precision")

S(IN, "hard", "With reference to the 14th Ministerial Conference (MC14) of the World Trade Organization, held in March 2026, consider the following statements:",
  "मार्च 2026 में आयोजित विश्व व्यापार संगठन के 14वें मंत्रिस्तरीय सम्मेलन (एमसी14) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was held in Yaoundé, Cameroon.",
   "The moratorium on customs duties on electronic transmissions, in place since 1998, lapsed after members failed to agree on extending it.",
   "India has long pressed for that moratorium to be made permanent."],
  ["यह कैमरून के याउंडे में आयोजित हुआ।",
   "इलेक्ट्रॉनिक प्रसारणों पर सीमा-शुल्क की रोक, जो 1998 से चली आ रही थी, सदस्यों के उसे बढ़ाने पर सहमत न होने के बाद समाप्त हो गई।",
   "भारत लंबे समय से उस रोक को स्थायी बनाने पर ज़ोर देता रहा है।"],
  C3, 1,
  "Statements 1 and 2 are correct. MC14 met at Yaoundé from 26 to 29 March 2026, the second Ministerial Conference held in Africa after Nairobi in 2015. The moratorium on duties on electronic transmissions -- downloads, streamed content, software sent online -- dates from the 1998 Declaration on Global Electronic Commerce and had been renewed at successive conferences; at MC14 members could not agree on its length, and it lapsed on 30 March 2026, although a group of members pursuing a plurilateral e-commerce agreement pledged not to impose such duties among themselves. "
  "Statement 3 is wrong: India, with countries such as South Africa and Indonesia, has questioned the moratorium, arguing that it costs developing countries customs revenue and policy space as more goods move in digital form; it has accepted short extensions rather than sought a permanent one.",
  "कथन 1 और 2 सही हैं। एमसी14 26 से 29 मार्च 2026 तक याउंडे में हुआ, 2015 में नैरोबी के बाद अफ़्रीका में होने वाला दूसरा मंत्रिस्तरीय सम्मेलन। इलेक्ट्रॉनिक प्रसारणों -- डाउनलोड, स्ट्रीम की गई सामग्री, ऑनलाइन भेजा गया सॉफ़्टवेयर -- पर शुल्क की रोक 1998 की वैश्विक इलेक्ट्रॉनिक वाणिज्य घोषणा से चली आ रही थी और लगातार सम्मेलनों में बढ़ाई जाती रही; एमसी14 में सदस्य उसकी अवधि पर सहमत नहीं हो सके, और वह 30 मार्च 2026 को समाप्त हो गई, यद्यपि बहुपक्षीय ई-वाणिज्य समझौते पर आगे बढ़ रहे सदस्यों के एक समूह ने आपस में ऐसे शुल्क न लगाने का वचन दिया। "
  "कथन 3 ग़लत है: भारत ने दक्षिण अफ़्रीका और इंडोनेशिया जैसे देशों के साथ इस रोक पर प्रश्न उठाए हैं, यह तर्क देते हुए कि जैसे-जैसे अधिक वस्तुएँ डिजिटल रूप में चलती हैं, इससे विकासशील देशों का सीमा-शुल्क राजस्व और नीतिगत गुंजाइश घटती है; उसने स्थायी रोक के बजाय छोटे विस्तार ही स्वीकार किए हैं।",
  "World Trade Organization, MC14 outcome documents (March 2026); WTO Declaration on Global Electronic Commerce (1998); Ministry of Commerce and Industry statements on MC14.",
  "ca-t1-ca-wto-mc14-ecommerce-moratorium", craft="linkage")

S(IN, "hard", "In February 2026 the Supreme Court of the United States held that the International Emergency Economic Powers Act does not authorise the President to impose tariffs. In this context, consider the following statements:",
  "फ़रवरी 2026 में संयुक्त राज्य अमेरिका के सर्वोच्च न्यायालय ने निर्णय दिया कि अंतरराष्ट्रीय आपातकालीन आर्थिक शक्तियाँ अधिनियम राष्ट्रपति को टैरिफ़ लगाने का अधिकार नहीं देता। इस संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Court reasoned that tariffs are a form of taxation, a power the US Constitution gives to Congress.",
   "In India, the Customs Tariff Act, 1975 allows the Central Government, when immediate action is needed, to raise import duty by notification, which must then be laid before Parliament."],
  ["न्यायालय का तर्क था कि टैरिफ़ कराधान का एक रूप हैं, जो शक्ति अमेरिकी संविधान कांग्रेस को देता है।",
   "भारत में सीमा-शुल्क टैरिफ़ अधिनियम, 1975 केंद्र सरकार को, तत्काल कार्रवाई आवश्यक होने पर, अधिसूचना द्वारा आयात शुल्क बढ़ाने की अनुमति देता है, जिसे बाद में संसद के समक्ष रखा जाना होता है।"],
  T2, 2,
  "Both statements are correct. In Learning Resources v. Trump, decided on 20 February 2026 by six votes to three, the Court held that the 1977 emergency-powers law, which lets the President 'regulate' imports, does not clearly delegate the taxing power that the Constitution vests in Congress; both the 'reciprocal' tariffs of April 2025 and the fentanyl-linked tariffs fell, and the administration moved to other statutes. "
  "India's arrangement is different. Article 265 requires every tax to have the authority of law, but the law itself delegates: section 8A of the Customs Tariff Act lets the Central Government raise the duty on an article by notification when circumstances require immediate action, and every such notification must be laid before each House of Parliament, which keeps the final control. The ruling also mattered to India, since part of the tariffs on Indian goods rested on the struck-down authority.",
  "दोनों कथन सही हैं। 20 फ़रवरी 2026 को छह के मुक़ाबले तीन मतों से तय लर्निंग रिसोर्सेज़ बनाम ट्रम्प मामले में न्यायालय ने कहा कि 1977 का आपात-शक्तियों वाला क़ानून, जो राष्ट्रपति को आयात ‘विनियमित’ करने देता है, वह कराधान-शक्ति स्पष्ट रूप से नहीं सौंपता जो संविधान कांग्रेस में निहित करता है; अप्रैल 2025 के ‘पारस्परिक’ टैरिफ़ और फ़ेंटेनिल से जुड़े टैरिफ़ दोनों गिर गए, और प्रशासन ने अन्य क़ानूनों का सहारा लिया। "
  "भारत की व्यवस्था भिन्न है। अनुच्छेद 265 हर कर के लिए विधि का प्राधिकार माँगता है, पर विधि स्वयं शक्ति सौंपती है: सीमा-शुल्क टैरिफ़ अधिनियम की धारा 8क केंद्र सरकार को, परिस्थितियाँ तत्काल कार्रवाई माँगें तो, अधिसूचना द्वारा किसी वस्तु पर शुल्क बढ़ाने देती है, और ऐसी हर अधिसूचना संसद के प्रत्येक सदन के समक्ष रखी जानी होती है, जिससे अंतिम नियंत्रण संसद के पास रहता है। यह निर्णय भारत के लिए भी महत्त्वपूर्ण था, क्योंकि भारतीय वस्तुओं पर लगे टैरिफ़ का एक भाग उसी निरस्त प्राधिकार पर टिका था।",
  "Supreme Court of the United States, Learning Resources, Inc. v. Trump (20 February 2026); Constitution of India, Article 265; Customs Tariff Act, 1975, section 8A.",
  "ca-t1-ca-ieepa-ruling-customs-tariff-8a", craft="linkage")

S(IN, "medium", "On 1 January 2026 India and Pakistan exchanged lists, as they do every year. Consider the following statements:",
  "1 जनवरी 2026 को भारत और पाकिस्तान ने, हर वर्ष की तरह, सूचियों का आदान-प्रदान किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under an agreement signed in 1988, the two countries exchange lists of their nuclear installations and facilities on 1 January every year, and undertake not to attack them.",
   "Lists of each other's nationals held in prison are exchanged under the same 1988 agreement."],
  ["1988 में हस्ताक्षरित एक समझौते के अंतर्गत दोनों देश हर वर्ष 1 जनवरी को अपने परमाणु प्रतिष्ठानों और सुविधाओं की सूचियों का आदान-प्रदान करते हैं, और उन पर हमला न करने का वचन देते हैं।",
   "एक-दूसरे के जेलों में बंद नागरिकों की सूचियों का आदान-प्रदान उसी 1988 के समझौते के अंतर्गत होता है।"],
  T2, 0,
  "Only statement 1 is correct. The Agreement on the Prohibition of Attack against Nuclear Installations and Facilities was signed in December 1988 and came into force in 1991; the first lists were exchanged on 1 January 1992, and the exchange has continued every year since, through war scares and the suspension of most other ties. "
  "Statement 2 is wrong: the prisoners' lists are exchanged under a separate Agreement on Consular Access of 2008, twice a year, on 1 January and 1 July. The two exchanges falling on the same day is exactly what makes the agreements easy to confuse.",
  "केवल कथन 1 सही है। परमाणु प्रतिष्ठानों और सुविधाओं पर हमले के निषेध का समझौता दिसंबर 1988 में हस्ताक्षरित होकर 1991 में लागू हुआ; पहली सूचियाँ 1 जनवरी 1992 को बदली गईं, और युद्ध की आशंकाओं और अधिकांश अन्य संबंध स्थगित रहने के बावजूद यह आदान-प्रदान तब से हर वर्ष चलता आया है। "
  "कथन 2 ग़लत है: क़ैदियों की सूचियाँ 2008 के एक अलग कांसुलर पहुँच समझौते के अंतर्गत वर्ष में दो बार, 1 जनवरी और 1 जुलाई को, बदली जाती हैं। दोनों आदान-प्रदान एक ही दिन पड़ना ही इन समझौतों को उलझाने वाला बनाता है।",
  "Ministry of External Affairs, press releases on the exchange of lists of nuclear installations and of prisoners (1 January 2026); India–Pakistan Agreement on the Prohibition of Attack against Nuclear Installations and Facilities (1988).",
  "ca-t1-ca-india-pakistan-nuclear-lists-1988", craft="precision")

S(IN, "medium", "India began a new three-year term on the UN Human Rights Council in January 2026. Consider the following statements:",
  "जनवरी 2026 में भारत ने संयुक्त राष्ट्र मानवाधिकार परिषद में तीन वर्ष का नया कार्यकाल शुरू किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Members of the Council are chosen by the Security Council on the recommendation of the General Assembly.",
   "A member that has served two consecutive terms is not eligible for immediate re-election.",
   "The Council is one of the principal organs of the United Nations named in the UN Charter."],
  ["परिषद के सदस्य महासभा की सिफ़ारिश पर सुरक्षा परिषद द्वारा चुने जाते हैं।",
   "लगातार दो कार्यकाल पूरे कर चुका सदस्य तुरंत पुनर्निर्वाचन के लिए पात्र नहीं होता।",
   "परिषद संयुक्त राष्ट्र चार्टर में नामित संयुक्त राष्ट्र के प्रमुख अंगों में से एक है।"],
  C3, 0,
  "Only statement 2 is correct, and India's own record shows it: a member since the Council was created in 2006, India had to sit out 2011, 2018 and 2025 after two straight terms each time, and was elected in October 2025 for 2026–28, its seventh term. "
  "Statement 1 is wrong: the 47 members are elected directly by the General Assembly, by secret ballot, each needing an absolute majority of the Assembly's members, with seats shared among the regional groups; the Security Council has no role. Statement 3 is wrong: the Council is a subsidiary body of the General Assembly, created by resolution 60/251 of 2006 to replace the Commission on Human Rights; the Charter's principal organs are the General Assembly, the Security Council, ECOSOC, the Trusteeship Council, the International Court of Justice and the Secretariat.",
  "केवल कथन 2 सही है, और भारत का अपना अनुभव यही दिखाता है: 2006 में परिषद बनने से ही सदस्य रहे भारत को हर बार लगातार दो कार्यकाल के बाद 2011, 2018 और 2025 में बाहर बैठना पड़ा, और अक्टूबर 2025 में वह 2026–28 के लिए अपने सातवें कार्यकाल हेतु चुना गया। "
  "कथन 1 ग़लत है: 47 सदस्य सीधे महासभा द्वारा गुप्त मतदान से चुने जाते हैं, प्रत्येक को महासभा के सदस्यों का पूर्ण बहुमत चाहिए, और सीटें क्षेत्रीय समूहों में बँटी हैं; सुरक्षा परिषद की कोई भूमिका नहीं है। कथन 3 ग़लत है: परिषद महासभा का सहायक निकाय है, जो मानवाधिकार आयोग की जगह 2006 के संकल्प 60/251 से बनी; चार्टर के प्रमुख अंग महासभा, सुरक्षा परिषद, आर्थिक और सामाजिक परिषद, न्यासिता परिषद, अंतरराष्ट्रीय न्यायालय और सचिवालय हैं।",
  "UN General Assembly resolution 60/251 (2006); Charter of the United Nations, Article 7; Ministry of External Affairs, release on India's election to the Human Rights Council for 2026–28 (October 2025).",
  "ca-t1-ca-hrc-india-two-term-rule", craft="application")

S(IN, "medium", "The US operation in Venezuela in January 2026 revived debate over the Monroe Doctrine. Consider the following statements:",
  "जनवरी 2026 में वेनेज़ुएला में अमेरिकी कार्रवाई ने मनरो सिद्धांत पर बहस फिर छेड़ दी। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Declared in 1823, it warned European powers against further colonisation of, or intervention in, the Americas.",
   "The 'Roosevelt Corollary' of 1904 gave up any claim by the United States to intervene in the affairs of Latin American states.",
   "It was a treaty that the United States signed with the newly independent states of Latin America."],
  ["1823 में घोषित यह सिद्धांत यूरोपीय शक्तियों को अमेरिकी महाद्वीपों में और उपनिवेश बनाने या हस्तक्षेप करने के विरुद्ध चेतावनी देता था।",
   "1904 के ‘रूज़वेल्ट उपसिद्धांत’ ने लैटिन अमेरिकी देशों के मामलों में हस्तक्षेप के संयुक्त राज्य अमेरिका के किसी भी दावे को छोड़ दिया।",
   "यह एक संधि थी जिस पर संयुक्त राज्य अमेरिका ने लैटिन अमेरिका के नव-स्वतंत्र देशों के साथ हस्ताक्षर किए।"],
  C3, 0,
  "Only statement 1 is correct. President James Monroe set out the doctrine in his message to Congress in December 1823, as Spain's colonies were winning independence: the Americas were closed to new European colonisation, and the United States would treat European interference there as hostile, while staying out of Europe's affairs. "
  "Statement 2 reverses the Roosevelt Corollary: Theodore Roosevelt claimed in 1904 that the United States could act as an 'international police power' in the hemisphere, which was used to justify interventions in the Caribbean and Central America. Statement 3 is wrong: the doctrine was a unilateral statement of policy, never a treaty. Its open revival to justify action in Venezuela, including the capture of President Maduro on 3 January 2026, is why the term was back in the news.",
  "केवल कथन 1 सही है। राष्ट्रपति जेम्स मनरो ने दिसंबर 1823 में कांग्रेस को अपने संदेश में, जब स्पेन के उपनिवेश स्वतंत्रता पा रहे थे, यह सिद्धांत रखा: अमेरिकी महाद्वीप नए यूरोपीय उपनिवेशों के लिए बंद थे, और संयुक्त राज्य वहाँ यूरोपीय हस्तक्षेप को शत्रुतापूर्ण मानेगा, जबकि स्वयं यूरोप के मामलों से दूर रहेगा। "
  "कथन 2 रूज़वेल्ट उपसिद्धांत को उलट देता है: थियोडोर रूज़वेल्ट ने 1904 में दावा किया कि संयुक्त राज्य इस गोलार्ध में ‘अंतरराष्ट्रीय पुलिस शक्ति’ की तरह काम कर सकता है, जिससे कैरिबियन और मध्य अमेरिका में हस्तक्षेपों को उचित ठहराया गया। कथन 3 ग़लत है: यह सिद्धांत नीति का एकपक्षीय वक्तव्य था, कभी संधि नहीं। वेनेज़ुएला में कार्रवाई, जिसमें 3 जनवरी 2026 को राष्ट्रपति मादुरो को पकड़ा गया, को उचित ठहराने के लिए इसका खुला पुनरुत्थान ही इसे फिर चर्चा में लाया।",
  "NCERT, Themes in World History (Class XI), on the Americas; US Department of State, Office of the Historian, Monroe Doctrine (1823) and Roosevelt Corollary (1904).",
  "ca-t1-ca-monroe-doctrine-roosevelt-corollary", craft="linkage")

S(IN, "medium", "US pressure over Greenland in early 2026 strained relations within NATO. Consider the following statements about NATO:",
  "2026 के आरंभ में ग्रीनलैंड को लेकर अमेरिकी दबाव ने नाटो के भीतर संबंधों पर तनाव डाला। नाटो के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["At its summit in The Hague in 2025, the allies committed to spend 5 per cent of GDP on core defence alone by 2030.",
   "Its collective-defence clause, Article 5, has been invoked only once, after the attacks of 11 September 2001.",
   "Finland and Sweden, which applied together after Russia's invasion of Ukraine, joined NATO in the same year."],
  ["2025 में हेग शिखर सम्मेलन में सहयोगियों ने 2030 तक केवल मूल रक्षा पर जीडीपी का 5 प्रतिशत ख़र्च करने का वचन दिया।",
   "इसके सामूहिक रक्षा उपबंध, अनुच्छेद 5, का प्रयोग केवल एक बार, 11 सितंबर 2001 के हमलों के बाद, हुआ है।",
   "रूस के यूक्रेन पर आक्रमण के बाद साथ-साथ आवेदन करने वाले फ़िनलैंड और स्वीडन एक ही वर्ष में नाटो में शामिल हुए।"],
  C3, 0,
  "Only statement 2 is correct. Article 5, under which an armed attack on one ally is an attack on all, has been invoked once, after the attacks of 11 September 2001 on the United States. "
  "Statement 1 is wrong: the Hague summit of June 2025 set a target of 5 per cent of GDP by 2035, split into at least 3.5 per cent for core defence and up to 1.5 per cent for related needs such as infrastructure, cyber defence and civil preparedness -- not 5 per cent on core defence, and not by 2030. Statement 3 is wrong: both applied in May 2022, but Finland joined in April 2023 and Sweden, after Turkey and Hungary delayed ratifying, only in March 2024, as the 32nd member. Greenland is a self-governing part of the Kingdom of Denmark, a founding member of the alliance, and hosts the US Pituffik Space Base -- which is why a US claim on the island set one ally against another.",
  "केवल कथन 2 सही है। अनुच्छेद 5, जिसके अंतर्गत एक सहयोगी पर सशस्त्र हमला सब पर हमला है, का प्रयोग एक बार, संयुक्त राज्य अमेरिका पर 11 सितंबर 2001 के हमलों के बाद हुआ। "
  "कथन 1 ग़लत है: जून 2025 के हेग शिखर सम्मेलन ने 2035 तक जीडीपी के 5 प्रतिशत का लक्ष्य रखा, जिसमें कम से कम 3.5 प्रतिशत मूल रक्षा के लिए और अधिकतम 1.5 प्रतिशत अवसंरचना, साइबर रक्षा और नागरिक तैयारी जैसी संबंधित आवश्यकताओं के लिए है -- न कि केवल मूल रक्षा पर 5 प्रतिशत, और न 2030 तक। कथन 3 ग़लत है: दोनों ने मई 2022 में आवेदन किया, पर फ़िनलैंड अप्रैल 2023 में शामिल हुआ और स्वीडन, तुर्किये और हंगरी द्वारा अनुसमर्थन में देरी के बाद, मार्च 2024 में 32वें सदस्य के रूप में। ग्रीनलैंड डेनमार्क राज्य का स्वशासित भाग है, जो गठबंधन का संस्थापक सदस्य है, और अमेरिकी पिटुफ़िक अंतरिक्ष अड्डे की मेज़बानी करता है -- इसीलिए द्वीप पर अमेरिकी दावे ने एक सहयोगी को दूसरे के सामने खड़ा कर दिया।",
  "North Atlantic Treaty (1949), Article 5; NATO, The Hague Summit Declaration (25 June 2025).",
  "ca-t1-ca-nato-hague-five-percent-article-5", craft="precision")

S(IN, "hard", "The strikes on Iran that began on 28 February 2026 were debated in terms of the UN Charter. Consider the following statements:",
  "28 फ़रवरी 2026 को शुरू हुए ईरान पर हमलों पर संयुक्त राष्ट्र चार्टर के संदर्भ में बहस हुई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 2(4) of the Charter obliges members to refrain from the threat or use of force against the territorial integrity or political independence of any state.",
   "Article 51 recognises the inherent right of self-defence if an armed attack occurs, until the Security Council has taken the measures necessary to maintain peace.",
   "Measures taken by a member in exercise of the right of self-defence must be reported immediately to the Security Council."],
  ["चार्टर का अनुच्छेद 2(4) सदस्यों को किसी भी राज्य की प्रादेशिक अखंडता या राजनीतिक स्वतंत्रता के विरुद्ध बल के प्रयोग या धमकी से बचने का दायित्व देता है।",
   "अनुच्छेद 51 सशस्त्र हमला होने पर आत्मरक्षा के अंतर्निहित अधिकार को, तब तक मान्यता देता है जब तक सुरक्षा परिषद शांति बनाए रखने के लिए आवश्यक उपाय न कर ले।",
   "आत्मरक्षा के अधिकार के प्रयोग में किसी सदस्य द्वारा किए गए उपायों की सूचना तुरंत सुरक्षा परिषद को दी जानी चाहिए।"],
  C3, 2,
  "All three statements are correct. The Charter allows force in only two cases: when the Security Council authorises it under Chapter VII, and in self-defence under Article 51. Article 51 is conditional -- it needs an armed attack, it lasts only until the Council acts, and the measures must be reported to the Council at once. "
  "The dispute over the February 2026 strikes turned on these words: whether a feared future attack counts as an 'armed attack' (the doctrine of anticipatory or pre-emptive self-defence, which many states reject), and whether reporting to the Council was made. The General Assembly, by contrast, can only recommend; its resolutions on such matters are not binding.",
  "तीनों कथन सही हैं। चार्टर बल का प्रयोग केवल दो स्थितियों में अनुमत करता है: जब सुरक्षा परिषद अध्याय VII के अंतर्गत अधिकृत करे, और अनुच्छेद 51 के अंतर्गत आत्मरक्षा में। अनुच्छेद 51 सशर्त है -- इसके लिए सशस्त्र हमला चाहिए, यह केवल परिषद के कार्रवाई करने तक चलता है, और उपायों की सूचना परिषद को तुरंत देनी होती है। "
  "फ़रवरी 2026 के हमलों पर विवाद इन्हीं शब्दों पर टिका था: क्या भविष्य के आशंकित हमले को ‘सशस्त्र हमला’ माना जा सकता है (पूर्वानुमानित या निवारक आत्मरक्षा का सिद्धांत, जिसे अनेक राज्य नहीं मानते), और क्या परिषद को सूचना दी गई। इसके विपरीत महासभा केवल सिफ़ारिश कर सकती है; ऐसे मामलों पर उसके संकल्प बाध्यकारी नहीं होते।",
  "Charter of the United Nations, Articles 2(4), 10-14, 39-42 and 51.",
  "ca-t1-ca-un-charter-2-4-article-51", craft="application")

S(IN, "hard", "Consider the following statements about Pakistan's 27th Constitutional Amendment of November 2025:",
  "नवंबर 2025 के पाकिस्तान के 27वें संविधान संशोधन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The amendment created a Federal Constitutional Court to hear constitutional cases, taking them away from Pakistan's Supreme Court.",
   "It created the post of Chief of Defence Forces, held by the army chief, and abolished the post of Chairman of the Joint Chiefs of Staff Committee.",
   "It lets an officer holding a five-star rank, such as Field Marshal, keep the rank and its privileges for life, with immunity from criminal prosecution."],
  ["संशोधन ने संवैधानिक मामलों की सुनवाई के लिए एक संघीय संवैधानिक न्यायालय बनाया, उन्हें पाकिस्तान के सर्वोच्च न्यायालय से हटाकर।",
   "इसने सेना प्रमुख द्वारा धारित रक्षा बलों के प्रमुख का पद बनाया, और संयुक्त सेना प्रमुख समिति के अध्यक्ष का पद समाप्त किया।",
   "यह फ़ील्ड मार्शल जैसे पाँच-सितारा पद वाले अधिकारी को वह पद और उसके विशेषाधिकार आजीवन, आपराधिक अभियोजन से उन्मुक्ति के साथ, रखने देता है।"],
  C3, 2,
  "All three statements are correct. The amendment, passed in November 2025, set up a Federal Constitutional Court with its own judges for constitutional matters, reducing the Supreme Court largely to an appellate court, and rewrote Article 243 so that the Chief of Army Staff also holds the new post of Chief of Defence Forces over all three services, while the post of Chairman of the Joint Chiefs of Staff Committee was abolished. It also lets five-star officers keep their rank, privileges and uniform for life, with lifelong immunity from criminal prosecution -- which critics read as placing the army chief beyond the reach of the courts. "
  "India's arrangements differ on each count. Constitutional cases stay with the Supreme Court. The Chief of Defence Staff, created in 2019, chairs the Chiefs of Staff Committee and heads the Department of Military Affairs but by design has no operational command over the services. India's two Field Marshals, Sam Manekshaw and K. M. Cariappa, held a ceremonial rank for life, and the Constitution shields only the President and the Governors from criminal proceedings, and only during their term of office (Article 361).",
  "तीनों कथन सही हैं। नवंबर 2025 में पारित संशोधन ने संवैधानिक मामलों के लिए अपने न्यायाधीशों वाला एक संघीय संवैधानिक न्यायालय बनाया, जिससे सर्वोच्च न्यायालय मुख्यतः अपीलीय न्यायालय रह गया, और अनुच्छेद 243 को बदलकर थल सेना प्रमुख को तीनों सेनाओं पर नए रक्षा बल प्रमुख का पद भी दिया, जबकि संयुक्त सेना प्रमुख समिति के अध्यक्ष का पद समाप्त कर दिया। यह पाँच-सितारा अधिकारियों को अपना पद, विशेषाधिकार और वर्दी आजीवन रखने देता है, आपराधिक अभियोजन से आजीवन उन्मुक्ति के साथ -- जिसे आलोचक सेना प्रमुख को न्यायालयों की पहुँच से बाहर रखना मानते हैं। "
  "भारत की व्यवस्थाएँ हर बिंदु पर भिन्न हैं। संवैधानिक मामले सर्वोच्च न्यायालय के पास ही रहते हैं। 2019 में बना चीफ़ ऑफ़ डिफ़ेंस स्टाफ़ चीफ़्स ऑफ़ स्टाफ़ कमेटी का अध्यक्ष और सैन्य मामलों के विभाग का प्रमुख है, पर योजनाबद्ध रूप से उसके पास सेनाओं पर कोई परिचालन कमान नहीं है। भारत के दो फ़ील्ड मार्शल, सैम मानेकशॉ और के. एम. करियप्पा, आजीवन एक औपचारिक पद पर रहे, और संविधान केवल राष्ट्रपति और राज्यपालों को, और केवल उनके कार्यकाल में, आपराधिक कार्यवाही से संरक्षण देता है (अनुच्छेद 361)।",
  "Constitution of the Islamic Republic of Pakistan, Article 243 as amended by the Constitution (Twenty-seventh Amendment) Act, 2025; Ministry of Defence (India), notification on the creation of the post of Chief of Defence Staff (December 2019); Constitution of India, Article 361.",
  "ca-t1-ca-pakistan-27th-amendment-fcc-cdf-immunity", craft="linkage")

S(IN, "medium", "The Ganga Water Treaty between India and Bangladesh, signed in December 1996, comes up for renewal in 2026. Consider the following statements:",
  "दिसंबर 1996 में हस्ताक्षरित भारत और बांग्लादेश के बीच गंगा जल संधि 2026 में नवीनीकरण के लिए सामने है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was signed for a period of thirty years.",
   "It governs the sharing of the Ganga's waters at Farakka during the lean season, from January to May.",
   "Like the Indus Waters Treaty, it provides for the World Bank to appoint a neutral expert to settle differences."],
  ["इस पर तीस वर्ष की अवधि के लिए हस्ताक्षर हुए थे।",
   "यह शुष्क मौसम में, जनवरी से मई तक, फ़रक्का पर गंगा के जल के बँटवारे को नियंत्रित करती है।",
   "सिंधु जल संधि की तरह, यह मतभेद सुलझाने के लिए विश्व बैंक द्वारा तटस्थ विशेषज्ञ की नियुक्ति का प्रावधान करती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The treaty, signed on 12 December 1996, runs for thirty years and expires in December 2026, which is why renewal talks began in 2026 alongside the reset with Bangladesh's new government. It divides the flow at Farakka in ten-day periods between 1 January and 31 May by a formula -- equal shares when the flow falls below 70,000 cusecs, for example -- with a review every five years. "
  "Statement 3 is wrong: the Ganga treaty is purely bilateral; a Joint Committee monitors the flows and differences go to the Indo-Bangladesh Joint Rivers Commission and then to the two governments. The neutral expert and the court of arbitration with a World Bank role belong to the Indus Waters Treaty of 1960 with Pakistan.",
  "कथन 1 और 2 सही हैं। 12 दिसंबर 1996 को हस्ताक्षरित संधि तीस वर्ष चलती है और दिसंबर 2026 में समाप्त होती है, इसीलिए बांग्लादेश की नई सरकार के साथ संबंधों के नए आरंभ के साथ 2026 में नवीनीकरण वार्ता शुरू हुई। यह 1 जनवरी से 31 मई के बीच दस-दिनी अवधियों में फ़रक्का पर प्रवाह को एक सूत्र से बाँटती है -- उदाहरण के लिए, प्रवाह 70,000 क्यूसेक से कम होने पर बराबर हिस्से -- और हर पाँच वर्ष पर समीक्षा होती है। "
  "कथन 3 ग़लत है: गंगा संधि पूरी तरह द्विपक्षीय है; एक संयुक्त समिति प्रवाह की निगरानी करती है और मतभेद भारत-बांग्लादेश संयुक्त नदी आयोग और फिर दोनों सरकारों के पास जाते हैं। विश्व बैंक की भूमिका वाले तटस्थ विशेषज्ञ और मध्यस्थता न्यायालय पाकिस्तान के साथ 1960 की सिंधु जल संधि के हैं।",
  "Treaty between India and Bangladesh on Sharing of the Ganga/Ganges Waters at Farakka (12 December 1996) and its Annexures; Indus Waters Treaty (1960), Article IX.",
  "ca-t1-ca-ganga-water-treaty-1996-renewal", craft="linkage")

# ================================================================ NATIONAL
A(NA, "medium",
  "The Union Government's drive to end Left Wing Extremism by 31 March 2026 relied on operations led by the State police forces, with the central armed police forces deployed in their support.",
  "31 मार्च 2026 तक वामपंथी उग्रवाद समाप्त करने का केंद्र सरकार का अभियान राज्य पुलिस बलों के नेतृत्व वाले अभियानों पर टिका था, जिनकी सहायता में केंद्रीय सशस्त्र पुलिस बल तैनात थे।",
  "'Police' and 'public order' are subjects in the State List of the Seventh Schedule.",
  "‘पुलिस’ और ‘लोक व्यवस्था’ सातवीं अनुसूची की राज्य सूची के विषय हैं।",
  1,
  "Statements II and III are both correct, but only Statement II explains Statement I. Public order and police are State subjects (Entries 1 and 2 of List II), so it is the States that lead operations against armed groups on their soil; the Union supports them with central armed police forces under Article 355's duty to protect States against internal disturbance, with funds for special infrastructure and the most affected districts, and with intelligence and coordination. "
  "Statement III is true -- the CRPF raised its Commando Battalions for Resolute Action from 2008 for jungle warfare in the Maoist-affected belt -- but it only names one of the supporting forces; it does not explain why the States lead. The number of districts counted as most affected had fallen to a handful by 2026, and the March 2026 deadline marked the drive to end armed Maoism.",
  "कथन II और III दोनों सही हैं, पर केवल कथन II कथन I की व्याख्या करता है। लोक व्यवस्था और पुलिस राज्य के विषय हैं (सूची II की प्रविष्टियाँ 1 और 2), इसलिए अपनी धरती पर सशस्त्र समूहों के विरुद्ध अभियानों का नेतृत्व राज्य करते हैं; केंद्र अनुच्छेद 355 के अंतर्गत राज्यों की आंतरिक अशांति से रक्षा के कर्तव्य के तहत केंद्रीय सशस्त्र पुलिस बलों से, विशेष अवसंरचना और सबसे अधिक प्रभावित ज़िलों के लिए धन से, और ख़ुफ़िया सूचना तथा समन्वय से उनकी सहायता करता है। "
  "कथन III सही है -- सीआरपीएफ़ ने माओवादी प्रभावित क्षेत्र में जंगल युद्ध के लिए 2008 से अपनी कमांडो बटालियन फ़ॉर रिज़ॉल्यूट एक्शन खड़ी कीं -- पर यह सहायक बलों में से केवल एक का नाम बताता है; यह नहीं बताता कि नेतृत्व राज्य क्यों करते हैं। 2026 तक सबसे अधिक प्रभावित माने जाने वाले ज़िलों की संख्या कुछ ही रह गई थी, और मार्च 2026 की समय-सीमा सशस्त्र माओवाद को समाप्त करने के अभियान का प्रतीक थी।",
  "Constitution of India, Seventh Schedule, List II, Entries 1 and 2, and Article 355; Ministry of Home Affairs, annual report on Left Wing Extremism.",
  "ca-t1-ca-lwe-state-police-si3",
  s3="CoBRA, a unit raised for jungle warfare against Left Wing Extremism, is part of the Central Reserve Police Force.",
  s3_hi="वामपंथी उग्रवाद के विरुद्ध जंगल युद्ध के लिए खड़ी की गई इकाई कोबरा केंद्रीय रिज़र्व पुलिस बल का भाग है।",
  craft="inference")

S(NA, "easy", "In February 2026 the Ministry of Home Affairs released a document named PRAHAAR. Consider the following statements:",
  "फ़रवरी 2026 में गृह मंत्रालय ने प्रहार नामक एक दस्तावेज़ जारी किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is India's first national counter-terrorism policy and strategy.",
   "It is a law enacted by Parliament in 2026, which repealed the earlier anti-terror laws."],
  ["यह भारत की पहली राष्ट्रीय आतंकवाद-रोधी नीति और रणनीति है।",
   "यह 2026 में संसद द्वारा बनाया गया क़ानून है, जिसने पहले के आतंकवाद-रोधी क़ानूनों को निरस्त कर दिया।"],
  T2, 0,
  "Only statement 1 is correct. PRAHAAR, released on 23 February 2026, brings counter-terrorism, counter-radicalisation and the response to cyber-enabled and drone threats into one national framework, on a whole-of-government and whole-of-society approach, with stress on intelligence-led prevention, swift and proportionate response and the rule of law. "
  "Statement 2 is wrong: it is a policy and strategy document of the executive, not a law. The legal framework against terrorism remains the Unlawful Activities (Prevention) Act, 1967, along with the National Investigation Agency Act, 2008 and the relevant provisions of the Bharatiya Nyaya Sanhita.",
  "केवल कथन 1 सही है। 23 फ़रवरी 2026 को जारी प्रहार आतंकवाद-रोध, कट्टरता-रोध और साइबर तथा ड्रोन ख़तरों के प्रत्युत्तर को सरकार-व्यापी और समाज-व्यापी दृष्टिकोण से एक राष्ट्रीय ढाँचे में लाता है, जिसमें ख़ुफ़िया-आधारित रोकथाम, त्वरित और आनुपातिक प्रत्युत्तर तथा विधि के शासन पर ज़ोर है। "
  "कथन 2 ग़लत है: यह कार्यपालिका का नीति और रणनीति दस्तावेज़ है, क़ानून नहीं। आतंकवाद के विरुद्ध विधिक ढाँचा विधिविरुद्ध क्रियाकलाप (निवारण) अधिनियम, 1967 ही है, साथ में राष्ट्रीय अन्वेषण अभिकरण अधिनियम, 2008 और भारतीय न्याय संहिता के संबंधित उपबंध।",
  "Ministry of Home Affairs, PRAHAAR: National Counter-Terrorism Policy and Strategy (23 February 2026); Unlawful Activities (Prevention) Act, 1967.",
  "ca-t1-ca-prahaar-counter-terror-policy", craft="recall")

# ================================================================ DEFENCE
S(DF, "medium", "In February 2026 India hosted the International Fleet Review together with Exercise MILAN at Visakhapatnam. Consider the following statements:",
  "फ़रवरी 2026 में भारत ने विशाखापत्तनम में मिलन अभ्यास के साथ अंतरराष्ट्रीय बेड़ा समीक्षा की मेज़बानी की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The fleet was reviewed by the President of India, the Supreme Commander of the armed forces.",
   "India's previous International Fleet Review, before the one of 2026, was held at Mumbai.",
   "MILAN began in 1995 as a gathering of regional navies hosted at Port Blair.",
   "The Eastern Naval Command has its headquarters at Visakhapatnam."],
  ["बेड़े की समीक्षा सशस्त्र सेनाओं की सर्वोच्च कमांडर, भारत की राष्ट्रपति ने की।",
   "2026 से पहले भारत की पिछली अंतरराष्ट्रीय बेड़ा समीक्षा मुंबई में हुई थी।",
   "मिलन 1995 में पोर्ट ब्लेयर में आयोजित क्षेत्रीय नौसेनाओं के एक जमावड़े के रूप में शुरू हुआ।",
   "पूर्वी नौसेना कमान का मुख्यालय विशाखापत्तनम में है।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct. Under Article 53(2) the supreme command of the Defence Forces vests in the President, and the fleet review is the ceremonial expression of it: President Droupadi Murmu reviewed the assembled ships from the presidential yacht on 18 February 2026. MILAN started in 1995 at Port Blair with a few navies of the Bay of Bengal region and has grown into a large multilateral exercise, now held at Visakhapatnam, the headquarters of the Eastern Naval Command. "
  "Statement 2 is wrong: this was India's third International Fleet Review; the first was at Mumbai in 2001, but the previous one was at Visakhapatnam in February 2016 -- so 2026 also marked ten years since the last one.",
  "कथन 1, 3 और 4 सही हैं। अनुच्छेद 53(2) के अंतर्गत रक्षा बलों की सर्वोच्च कमान राष्ट्रपति में निहित है, और बेड़ा समीक्षा उसकी औपचारिक अभिव्यक्ति है: राष्ट्रपति द्रौपदी मुर्मु ने 18 फ़रवरी 2026 को राष्ट्रपति नौका से एकत्र पोतों की समीक्षा की। मिलन 1995 में पोर्ट ब्लेयर में बंगाल की खाड़ी क्षेत्र की कुछ नौसेनाओं के साथ शुरू होकर एक बड़े बहुपक्षीय अभ्यास में बदल गया है, जो अब पूर्वी नौसेना कमान के मुख्यालय विशाखापत्तनम में होता है। "
  "कथन 2 ग़लत है: यह भारत की तीसरी अंतरराष्ट्रीय बेड़ा समीक्षा थी; पहली 2001 में मुंबई में हुई, पर पिछली फ़रवरी 2016 में विशाखापत्तनम में -- इसलिए 2026 पिछली समीक्षा के दस वर्ष पूरे होने का भी वर्ष था।",
  "Constitution of India, Article 53(2); Ministry of Defence (Indian Navy), releases on the International Fleet Review and MILAN 2026 (February 2026).",
  "ca-t1-ca-ifr-2026-milan-port-blair", craft="linkage")

MX(DF, "medium", "Match List-I (joint military exercise) with List-II (India's partner in it):",
   "सूची-I (संयुक्त सैन्य अभ्यास) का सूची-II (उसमें भारत का साझेदार) से मिलान कीजिए:",
   ["Dharma Guardian", "Vajra Prahar", "Desert Cyclone", "Ajeya Warrior"],
   ["धर्म गार्जियन", "वज्र प्रहार", "डेज़र्ट साइक्लोन", "अजेय वॉरियर"],
   ["United Arab Emirates", "Japan", "United Kingdom", "United States"],
   ["संयुक्त अरब अमीरात", "जापान", "यूनाइटेड किंगडम", "संयुक्त राज्य अमेरिका"],
   (2, 4, 1, 3), POS.get("ca-t1-ca-exercises-dharma-guardian-vajra-prahar", 1),
   "The correct code is A-2, B-4, C-1, D-3. The seventh Dharma Guardian, between the Indian Army and the Japan Ground Self-Defense Force, began at Chaubattia in Uttarakhand on 24 February 2026; the sixteenth Vajra Prahar, a special-forces exercise with the United States, ran at Bakloh in Himachal Pradesh from late February into March. "
   "Desert Cyclone is India's exercise with the United Arab Emirates, first held in Rajasthan in 2024 -- not to be confused with 'Cyclone', the exercise with Egypt -- and Ajeya Warrior is the Indian Army's exercise with the British Army. Near-identical names and familiar partners are exactly how such matching items trap a candidate.",
   "सही कूट A-2, B-4, C-1, D-3 है। भारतीय सेना और जापान ग्राउंड सेल्फ़-डिफ़ेंस फ़ोर्स के बीच सातवाँ धर्म गार्जियन 24 फ़रवरी 2026 को उत्तराखंड के चौबटिया में शुरू हुआ; संयुक्त राज्य अमेरिका के साथ विशेष बलों का सोलहवाँ वज्र प्रहार फ़रवरी के अंत से मार्च तक हिमाचल प्रदेश के बकलोह में चला। "
   "डेज़र्ट साइक्लोन संयुक्त अरब अमीरात के साथ भारत का अभ्यास है, जो पहली बार 2024 में राजस्थान में हुआ -- इसे मिस्र के साथ होने वाले ‘साइक्लोन’ से न मिलाएँ -- और अजेय वॉरियर भारतीय सेना का ब्रिटिश सेना के साथ अभ्यास है। लगभग एक जैसे नाम और जाने-पहचाने साझेदार ही ऐसे मिलान-प्रश्नों का जाल होते हैं।",
   "Ministry of Defence, releases on Exercise Dharma Guardian and Exercise Vajra Prahar (February 2026) and on Exercises Desert Cyclone, Cyclone and Ajeya Warrior.",
   "ca-t1-ca-exercises-dharma-guardian-vajra-prahar", "precision")

S(DF, "medium", "In January 2026 the Army Day parade was held in Jaipur, where the newly raised Bhairav battalions made their debut. Consider the following statements:",
  "जनवरी 2026 में सेना दिवस परेड जयपुर में हुई, जहाँ नई खड़ी की गई भैरव बटालियनों ने पहली बार भाग लिया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Army Day marks the day in 1949 when K.M. Cariappa took over as the first Indian Commander-in-Chief of the Indian Army.",
   "K.M. Cariappa is the only officer of the Indian Army to have held the rank of Field Marshal.",
   "The Bhairav battalions are light commando units meant to fill the gap between regular infantry and the special forces."],
  ["सेना दिवस 1949 के उस दिन की याद में है जब के.एम. करियप्पा भारतीय सेना के पहले भारतीय कमांडर-इन-चीफ़ बने।",
   "के.एम. करियप्पा भारतीय सेना के एकमात्र अधिकारी हैं जिन्होंने फ़ील्ड मार्शल का पद धारण किया।",
   "भैरव बटालियनें हल्की कमांडो इकाइयाँ हैं जो नियमित पैदल सेना और विशेष बलों के बीच का अंतर भरने के लिए हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. On 15 January 1949 Lieutenant General K.M. Cariappa succeeded General Sir Francis Butcher, the last British Commander-in-Chief; since 2023 the Army Day parade has moved around the country, to Bengaluru, Lucknow, Pune and, in 2026, Jaipur. The Bhairav light commando battalions, raised from 2025, are lean, quick-reacting units drawn from the infantry for raids and border tasks, between the regular battalions and the Para (Special Forces). "
  "Statement 2 is wrong: the Indian Army has had two Field Marshals -- Sam Manekshaw, promoted in 1973 after the 1971 war, and Cariappa, given the rank in 1986. (Arjan Singh held the equivalent rank of Marshal of the Indian Air Force.)",
  "कथन 1 और 3 सही हैं। 15 जनवरी 1949 को लेफ़्टिनेंट जनरल के.एम. करियप्पा ने अंतिम ब्रिटिश कमांडर-इन-चीफ़ जनरल सर फ़्रांसिस बुचर का स्थान लिया; 2023 से सेना दिवस परेड देश के विभिन्न शहरों -- बेंगलुरु, लखनऊ, पुणे और 2026 में जयपुर -- में होती आई है। 2025 से खड़ी की गई भैरव हल्की कमांडो बटालियनें पैदल सेना से ली गई छोटी, त्वरित-प्रतिक्रिया इकाइयाँ हैं जो छापों और सीमा-कार्यों के लिए नियमित बटालियनों और पैरा (विशेष बल) के बीच आती हैं। "
  "कथन 2 ग़लत है: भारतीय सेना में दो फ़ील्ड मार्शल हुए हैं -- 1971 के युद्ध के बाद 1973 में पदोन्नत सैम मानेकशॉ, और 1986 में यह पद पाने वाले करियप्पा। (अर्जन सिंह ने भारतीय वायु सेना के मार्शल का समकक्ष पद धारण किया।)",
  "Ministry of Defence, releases on Army Day 2026 and the 77th Republic Day parade; Indian Army, history of Army Day.",
  "ca-t1-ca-army-day-cariappa-bhairav", craft="precision")

# ================================================================ SCHEMES & INDICES
M(SC, "medium",
  "Which one of the following pairs of a report released in early 2026 and its publisher is NOT correctly matched?",
  "2026 के आरंभ में जारी किसी रिपोर्ट और उसके प्रकाशक का निम्नलिखित में से कौन-सा युग्म सही सुमेलित नहीं है?",
  ["Global Risks Report : World Bank",
   "Corruption Perceptions Index : Transparency International",
   "Democracy Index : Economist Intelligence Unit",
   "World Employment and Social Outlook : International Labour Organization"],
  ["ग्लोबल रिस्क्स रिपोर्ट : विश्व बैंक",
   "करप्शन परसेप्शन्स इंडेक्स : ट्रांसपेरेंसी इंटरनेशनल",
   "डेमोक्रेसी इंडेक्स : इकोनॉमिस्ट इंटेलिजेंस यूनिट",
   "वर्ल्ड एम्प्लॉयमेंट एंड सोशल आउटलुक : अंतरराष्ट्रीय श्रम संगठन"],
  0,
  "The Global Risks Report is published by the World Economic Forum each January, before the Davos meeting; the World Bank's flagships are the World Development Report and Global Economic Prospects. The other three pairs are correct: Transparency International, a Berlin-based NGO, publishes the Corruption Perceptions Index each February from expert and business surveys; the Economist Intelligence Unit's Democracy Index classifies countries as full democracies, flawed democracies, hybrid regimes or authoritarian regimes; and the International Labour Organization's World Employment and Social Outlook: Trends, in its January 2026 edition, projected global unemployment to stay near historic lows while warning about job quality. "
  "In a 'NOT correctly matched' item every option but one is true, so each pair must be checked on its own -- the familiar names of the other bodies are what make a wrong pairing look plausible.",
  "ग्लोबल रिस्क्स रिपोर्ट विश्व आर्थिक मंच हर जनवरी दावोस बैठक से पहले प्रकाशित करता है; विश्व बैंक की प्रमुख रिपोर्टें वर्ल्ड डेवलपमेंट रिपोर्ट और ग्लोबल इकोनॉमिक प्रॉस्पेक्ट्स हैं। अन्य तीन युग्म सही हैं: बर्लिन स्थित गैर-सरकारी संगठन ट्रांसपेरेंसी इंटरनेशनल विशेषज्ञ और व्यावसायिक सर्वेक्षणों से हर फ़रवरी करप्शन परसेप्शन्स इंडेक्स प्रकाशित करता है; इकोनॉमिस्ट इंटेलिजेंस यूनिट का डेमोक्रेसी इंडेक्स देशों को पूर्ण लोकतंत्र, दोषपूर्ण लोकतंत्र, संकर शासन या सत्तावादी शासन में वर्गीकृत करता है; और अंतरराष्ट्रीय श्रम संगठन की वर्ल्ड एम्प्लॉयमेंट एंड सोशल आउटलुक: ट्रेंड्स के जनवरी 2026 संस्करण ने रोज़गार की गुणवत्ता पर चेतावनी देते हुए वैश्विक बेरोज़गारी ऐतिहासिक निम्न स्तर के आसपास रहने का अनुमान लगाया। "
  "‘सही सुमेलित नहीं’ वाले प्रश्न में एक को छोड़कर हर विकल्प सही होता है, इसलिए हर युग्म को अलग से जाँचना होता है -- अन्य निकायों के परिचित नाम ही ग़लत युग्म को विश्वसनीय दिखाते हैं।",
  "World Economic Forum, Global Risks Report 2026; Transparency International, Corruption Perceptions Index 2025; Economist Intelligence Unit, Democracy Index; International Labour Organization, World Employment and Social Outlook: Trends 2026.",
  "ca-t1-ca-reports-not-correctly-matched", pos=POS.get("ca-t1-ca-reports-not-correctly-matched", 2), craft="precision")

S(SC, "easy", "The Union Budget 2026-27 allotted ₹67,600 crore to the Jal Jeevan Mission. Consider the following statements about the Mission:",
  "केंद्रीय बजट 2026-27 ने जल जीवन मिशन को ₹67,600 करोड़ दिए। मिशन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It aims to give a functional tap connection to every household, rural and urban alike.",
   "Its service-level benchmark is a supply of 135 litres per person per day.",
   "It was launched in 2014 together with the Swachh Bharat Mission."],
  ["इसका उद्देश्य हर परिवार को, ग्रामीण और शहरी दोनों को, कार्यशील नल कनेक्शन देना है।",
   "इसका सेवा-स्तर मानक प्रति व्यक्ति प्रति दिन 135 लीटर की आपूर्ति है।",
   "इसे 2014 में स्वच्छ भारत मिशन के साथ शुरू किया गया था।"],
  C3, 3,
  "None of the statements is correct. The Jal Jeevan Mission, launched on 15 August 2019 under the Ministry of Jal Shakti, aims at a functional household tap connection for every rural household; urban water supply is covered by AMRUT. Its benchmark is 55 litres per person per day of potable water of prescribed quality, supplied regularly -- 135 litres a day is the norm used for urban piped supply. "
  "Its original 2024 target was extended to 2028 in the Budget of 2025-26, with the focus shifting to the quality of infrastructure, operation and maintenance by the gram panchayats, and the reliability and source sustainability that later reviews flagged.",
  "कोई भी कथन सही नहीं है। जल शक्ति मंत्रालय के अंतर्गत 15 अगस्त 2019 को शुरू हुए जल जीवन मिशन का उद्देश्य हर ग्रामीण परिवार को कार्यशील घरेलू नल कनेक्शन देना है; शहरी जल आपूर्ति अमृत योजना के अंतर्गत आती है। इसका मानक निर्धारित गुणवत्ता का प्रति व्यक्ति प्रति दिन 55 लीटर पेयजल नियमित रूप से देना है -- प्रति दिन 135 लीटर शहरी पाइप आपूर्ति का मानक है। "
  "इसका मूल 2024 का लक्ष्य 2025-26 के बजट में 2028 तक बढ़ाया गया, और ज़ोर अवसंरचना की गुणवत्ता, ग्राम पंचायतों द्वारा संचालन और रखरखाव, तथा बाद की समीक्षाओं में उठाई गई विश्वसनीयता और स्रोत-स्थिरता पर चला गया।",
  "Ministry of Jal Shakti, Department of Drinking Water and Sanitation, Jal Jeevan Mission operational guidelines; Union Budget 2025-26 and 2026-27, Budget speeches.",
  "ca-t1-ca-jal-jeevan-55-lpcd-rural", craft="precision")

S(SC, "medium", "In January 2026 a gram panchayat in Rajasthan was certified as fully organic, ten years after Sikkim's declaration. Consider the following statements about organic certification in India:",
  "जनवरी 2026 में राजस्थान की एक ग्राम पंचायत को पूर्णतः जैविक प्रमाणित किया गया, सिक्किम की घोषणा के दस वर्ष बाद। भारत में जैविक प्रमाणन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The National Programme for Organic Production is run by the Ministry of Agriculture and Farmers' Welfare.",
   "Produce certified under the Participatory Guarantee System (PGS-India) can be exported as certified organic.",
   "Sikkim was declared India's first fully organic State in 2003."],
  ["जैविक उत्पादन का राष्ट्रीय कार्यक्रम कृषि और किसान कल्याण मंत्रालय चलाता है।",
   "सहभागी गारंटी प्रणाली (पीजीएस-इंडिया) के अंतर्गत प्रमाणित उपज को प्रमाणित जैविक के रूप में निर्यात किया जा सकता है।",
   "सिक्किम को 2003 में भारत का पहला पूर्णतः जैविक राज्य घोषित किया गया।"],
  C3, 3,
  "None of the statements is correct. India runs two systems. The National Programme for Organic Production, begun in 2001, belongs to the Ministry of Commerce and Industry, with APEDA as its secretariat; it uses third-party certification by accredited bodies and is recognised by importing markets, so it is the route for exports. PGS-India, run by the Ministry of Agriculture and Farmers' Welfare, is a cheaper peer-review system in which local groups of farmers certify one another; it is meant for the domestic market and its produce cannot be exported as certified organic. "
  "Sikkim resolved in 2003 to go organic but was declared India's first fully organic State only in January 2016, after phasing out chemical inputs -- which is why the 2026 certification was measured against its ten-year mark.",
  "कोई भी कथन सही नहीं है। भारत दो प्रणालियाँ चलाता है। 2001 में शुरू हुआ जैविक उत्पादन का राष्ट्रीय कार्यक्रम वाणिज्य और उद्योग मंत्रालय का है, जिसका सचिवालय एपीडा है; यह मान्यता-प्राप्त निकायों द्वारा तृतीय-पक्ष प्रमाणन अपनाता है और आयातक बाज़ार इसे मान्यता देते हैं, इसलिए निर्यात का यही मार्ग है। कृषि और किसान कल्याण मंत्रालय की पीजीएस-इंडिया एक सस्ती सहकर्मी-समीक्षा प्रणाली है जिसमें किसानों के स्थानीय समूह एक-दूसरे को प्रमाणित करते हैं; यह घरेलू बाज़ार के लिए है और इसकी उपज प्रमाणित जैविक के रूप में निर्यात नहीं की जा सकती। "
  "सिक्किम ने 2003 में जैविक बनने का संकल्प लिया, पर रासायनिक आदानों को चरणबद्ध रूप से हटाने के बाद उसे जनवरी 2016 में ही भारत का पहला पूर्णतः जैविक राज्य घोषित किया गया -- इसीलिए 2026 के प्रमाणन को उसके दस वर्ष के पड़ाव से जोड़कर देखा गया।",
  "Ministry of Commerce and Industry (APEDA), National Programme for Organic Production; Ministry of Agriculture and Farmers' Welfare, PGS-India operational manual; Government of Sikkim, State Organic Mission.",
  "ca-t1-ca-organic-npop-pgs-sikkim", craft="precision")

S(SC, "medium", "Startup India completed ten years on 16 January 2026, observed as National Startup Day. Consider the following statements:",
  "स्टार्टअप इंडिया ने 16 जनवरी 2026 को दस वर्ष पूरे किए, जिसे राष्ट्रीय स्टार्टअप दिवस के रूप में मनाया जाता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Startup India Seed Fund Scheme, money reaches startups through selected incubators rather than directly from the government.",
   "The Credit Guarantee Scheme for Startups is operated by the National Credit Guarantee Trustee Company.",
   "Recognition as a startup by the DPIIT is available to an entity of any age, so long as its turnover stays below the prescribed limit."],
  ["स्टार्टअप इंडिया सीड फ़ंड योजना के अंतर्गत धन स्टार्टअप तक सीधे सरकार से नहीं, बल्कि चयनित इनक्यूबेटरों के माध्यम से पहुँचता है।",
   "स्टार्टअप के लिए ऋण गारंटी योजना नेशनल क्रेडिट गारंटी ट्रस्टी कंपनी चलाती है।",
   "डीपीआईआईटी से स्टार्टअप के रूप में मान्यता किसी भी आयु की इकाई को मिल सकती है, बशर्ते उसका कारोबार निर्धारित सीमा से नीचे रहे।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Seed Fund Scheme of 2021 gives grants to selected incubators, which in turn fund early-stage startups for proof of concept, prototypes and market entry. The Credit Guarantee Scheme for Startups, notified in 2022, lets banks and other lenders give collateral-free loans to recognised startups, with guarantees run by the NCGTC under the Department of Financial Services. "
  "Statement 3 is wrong: recognition has an age limit as well as a turnover limit -- an entity counts as a startup only for a fixed number of years from its incorporation (ten years for most), and only while its turnover stays within the ceiling and it works on innovation or a scalable model. The idea is to support young firms, not to give any small firm a permanent label.",
  "कथन 1 और 2 सही हैं। 2021 की सीड फ़ंड योजना चयनित इनक्यूबेटरों को अनुदान देती है, जो आगे प्रारंभिक चरण के स्टार्टअप को अवधारणा-प्रमाण, प्रोटोटाइप और बाज़ार-प्रवेश के लिए धन देते हैं। 2022 में अधिसूचित स्टार्टअप ऋण गारंटी योजना बैंकों और अन्य ऋणदाताओं को मान्यता-प्राप्त स्टार्टअप को बिना संपार्श्विक ऋण देने देती है, जिसकी गारंटियाँ वित्तीय सेवा विभाग के अधीन एनसीजीटीसी चलाती है। "
  "कथन 3 ग़लत है: मान्यता के लिए कारोबार की सीमा के साथ आयु की सीमा भी है -- कोई इकाई अपने निगमन से निश्चित वर्षों तक ही स्टार्टअप मानी जाती है (अधिकांश के लिए दस वर्ष), और तभी तक जब तक उसका कारोबार सीमा के भीतर रहे और वह नवाचार या विस्तार-योग्य मॉडल पर काम करे। उद्देश्य युवा फ़र्मों को सहारा देना है, किसी भी छोटी फ़र्म को स्थायी ठप्पा देना नहीं।",
  "Department for Promotion of Industry and Internal Trade, notification on the definition of a startup (G.S.R. 127(E), 2019) and Startup India Seed Fund Scheme guidelines (2021); Credit Guarantee Scheme for Startups (2022).",
  "ca-t1-ca-startup-india-ten-years-seed-cgss", craft="precision")

S(SC, "easy", "Chhattisgarh and Puducherry were reported in January 2026 to have cut tuberculosis deaths by pairing cash support with early nutrition. Consider the following statements:",
  "जनवरी 2026 में बताया गया कि छत्तीसगढ़ और पुदुच्चेरी ने नक़द सहायता को शीघ्र पोषण से जोड़कर तपेदिक से मौतें घटाईं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Ni-kshay Poshan Yojana, TB patients receive direct benefit transfers to support their nutrition during treatment.",
   "The amount paid under it was raised to ₹1,000 a month in 2024.",
   "India's national target for ending TB was set for 2030, the same year as the Sustainable Development Goals."],
  ["नि-क्षय पोषण योजना के अंतर्गत टीबी रोगियों को उपचार के दौरान पोषण के लिए प्रत्यक्ष लाभ अंतरण मिलता है।",
   "इसके अंतर्गत दी जाने वाली राशि 2024 में बढ़ाकर ₹1,000 प्रति माह की गई।",
   "भारत ने टीबी समाप्त करने का राष्ट्रीय लक्ष्य 2030 रखा था, सतत विकास लक्ष्यों वाला ही वर्ष।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Ni-kshay Poshan Yojana, begun in 2018 at ₹500 a month, pays notified TB patients through direct benefit transfer for the duration of treatment, because undernutrition both raises the risk of TB and worsens its outcome; the payment was doubled to ₹1,000 a month from November 2024. "
  "Statement 3 is wrong: the National Strategic Plan set 2025 as India's target for ending TB, five years ahead of the SDG target of 2030; the 100-day intensified campaign of 2024-25 and the push for early nutrition were part of the drive toward it.",
  "कथन 1 और 2 सही हैं। 2018 में ₹500 प्रति माह से शुरू हुई नि-क्षय पोषण योजना अधिसूचित टीबी रोगियों को उपचार की पूरी अवधि के लिए प्रत्यक्ष लाभ अंतरण से भुगतान करती है, क्योंकि कुपोषण टीबी का जोखिम भी बढ़ाता है और उसके परिणाम भी बिगाड़ता है; नवंबर 2024 से यह भुगतान दोगुना कर ₹1,000 प्रति माह किया गया। "
  "कथन 3 ग़लत है: राष्ट्रीय रणनीतिक योजना ने टीबी समाप्त करने के लिए भारत का लक्ष्य 2025 रखा, 2030 के एसडीजी लक्ष्य से पाँच वर्ष पहले; 2024-25 का 100-दिवसीय सघन अभियान और शीघ्र पोषण पर ज़ोर उसी दिशा के प्रयास थे।",
  "Ministry of Health and Family Welfare, National TB Elimination Programme, Ni-kshay Poshan Yojana guidelines and the enhancement of support (November 2024); National Strategic Plan for TB Elimination 2017-25.",
  "ca-t1-ca-nikshay-poshan-tb-2025", craft="linkage")

# ================================================================ SPORTS
S(SP, "easy", "March 2026 marked seventy-five years since the first Asian Games. Consider the following statements:",
  "मार्च 2026 में पहले एशियाई खेलों के पचहत्तर वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first Asian Games were held in New Delhi in 1951.",
   "The idea of the Asian Games was put forward by G.D. Sondhi, India's member of the International Olympic Committee.",
   "Ahmedabad has been chosen to host the Commonwealth Games in 2030."],
  ["पहले एशियाई खेल 1951 में नई दिल्ली में आयोजित हुए थे।",
   "एशियाई खेलों का विचार अंतरराष्ट्रीय ओलंपिक समिति में भारत के सदस्य जी.डी. सोंधी ने रखा था।",
   "2030 में राष्ट्रमंडल खेलों की मेज़बानी के लिए अहमदाबाद को चुना गया है।"],
  C3, 2,
  "All three statements are correct. The first Asian Games were held at New Delhi's National Stadium from 4 to 11 March 1951, opened by President Rajendra Prasad, with about 500 athletes from eleven countries. Guru Dutt Sondhi proposed the idea during the London Olympics of 1948, and the Asian Games Federation was formed in 1949 to organise them. "
  "In November 2025 the Commonwealth Sport General Assembly awarded the 2030 Games -- the centenary edition -- to Ahmedabad; India last hosted them in Delhi in 2010.",
  "तीनों कथन सही हैं। पहले एशियाई खेल 4 से 11 मार्च 1951 तक नई दिल्ली के राष्ट्रीय स्टेडियम में हुए, जिनका उद्घाटन राष्ट्रपति राजेंद्र प्रसाद ने किया, और इनमें ग्यारह देशों के लगभग 500 खिलाड़ी आए। गुरु दत्त सोंधी ने 1948 के लंदन ओलंपिक के दौरान यह विचार रखा, और इन्हें आयोजित करने के लिए 1949 में एशियाई खेल महासंघ बना। "
  "नवंबर 2025 में राष्ट्रमंडल खेल महासभा ने 2030 के खेल -- शताब्दी संस्करण -- अहमदाबाद को दिए; भारत ने पिछली बार 2010 में दिल्ली में इनकी मेज़बानी की थी।",
  "Ministry of Youth Affairs and Sports; Olympic Council of Asia, history of the Asian Games; Commonwealth Sport, decision on the host of the 2030 Commonwealth Games (November 2025).",
  "ca-t1-ca-asian-games-1951-cwg-2030", craft="recall")

# ================================================================ AWARDS; DEFENCE (continued)
S("Awards & Appointments", "medium", "On the eve of Republic Day 2026, Group Captain Shubhanshu Shukla was awarded the Ashok Chakra. Consider the following statements:",
  "गणतंत्र दिवस 2026 की पूर्व संध्या पर ग्रुप कैप्टन शुभांशु शुक्ला को अशोक चक्र प्रदान किया गया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ashok Chakra is India's highest award for gallantry other than in the face of the enemy.",
   "It can be awarded only to members of the armed forces.",
   "Shubhanshu Shukla is the first astronaut to receive it."],
  ["अशोक चक्र शत्रु के सामने से भिन्न परिस्थितियों में वीरता के लिए भारत का सर्वोच्च पुरस्कार है।",
   "यह केवल सशस्त्र सेनाओं के सदस्यों को दिया जा सकता है।",
   "शुभांशु शुक्ला इसे पाने वाले पहले अंतरिक्ष यात्री हैं।"],
  C3, 0,
  "Only statement 1 is correct. Gallantry awards come in two series: the Param Vir Chakra, Maha Vir Chakra and Vir Chakra for valour in the face of the enemy, and the Ashok Chakra, Kirti Chakra and Shaurya Chakra for gallantry other than in the face of the enemy -- the Ashok Chakra heads the second series. Shukla's award recognised his role on the Axiom-4 mission of 2025. "
  "Statement 2 is wrong: the peacetime series is open to civilians as well as to members of the armed forces and the police, and can be awarded posthumously. Statement 3 is wrong: Rakesh Sharma, India's first person in space in 1984, was also awarded the Ashok Chakra, so Shukla is the second astronaut to receive it.",
  "केवल कथन 1 सही है। वीरता पुरस्कार दो शृंखलाओं में हैं: शत्रु के सामने वीरता के लिए परमवीर चक्र, महावीर चक्र और वीर चक्र, तथा शत्रु के सामने से भिन्न परिस्थितियों में वीरता के लिए अशोक चक्र, कीर्ति चक्र और शौर्य चक्र -- अशोक चक्र दूसरी शृंखला में सबसे ऊपर है। शुक्ला का पुरस्कार 2025 के एक्सिओम-4 मिशन में उनकी भूमिका के लिए था। "
  "कथन 2 ग़लत है: शांतिकालीन शृंखला सशस्त्र सेनाओं और पुलिस के सदस्यों के साथ नागरिकों के लिए भी खुली है, और मरणोपरांत भी दी जा सकती है। कथन 3 ग़लत है: 1984 में अंतरिक्ष जाने वाले पहले भारतीय राकेश शर्मा को भी अशोक चक्र मिला था, इसलिए शुक्ला इसे पाने वाले दूसरे अंतरिक्ष यात्री हैं।",
  "Ministry of Defence, release on gallantry awards on the eve of Republic Day 2026 (25 January 2026); Ministry of Defence, Ashoka Chakra series statutes.",
  "ca-t1-ca-ashok-chakra-peacetime-series", craft="precision")

S(DF, "medium", "In February 2026 the Assam Rifles inducted two indigenous dog breeds, the Tangkhul Hui and the Kombai, into its canine squads. Consider the following statements about the Assam Rifles:",
  "फ़रवरी 2026 में असम राइफ़ल्स ने अपने श्वान दस्तों में दो देशी नस्लों, तांगखुल हुई और कोम्बई, को शामिल किया। असम राइफ़ल्स के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the oldest of India's central paramilitary forces, raised in 1835 as the Cachar Levy.",
   "Its administrative control lies with the Ministry of Home Affairs, while its operational control lies with the Indian Army.",
   "It guards India's border with Myanmar.",
   "Its Directorate General is located at Shillong."],
  ["यह भारत के केंद्रीय अर्धसैनिक बलों में सबसे पुराना है, जिसे 1835 में कछार लेवी के रूप में खड़ा किया गया था।",
   "इसका प्रशासनिक नियंत्रण गृह मंत्रालय के पास है, जबकि परिचालन नियंत्रण भारतीय सेना के पास।",
   "यह म्यांमार के साथ भारत की सीमा की रक्षा करता है।",
   "इसका महानिदेशालय शिलांग में स्थित है।"],
  C4, 3,
  "All four statements are correct. The force traces its origin to the Cachar Levy raised by the British in 1835 to protect settlements and tea estates in the north-east, which makes it the oldest paramilitary force in the country. It works under a dual arrangement: the Ministry of Home Affairs is responsible for its administration, while the Army, whose officers command it, has operational control for counter-insurgency and border tasks. "
  "Under the 'one border, one force' policy the Assam Rifles guards the India–Myanmar border, while the border with Bangladesh is the Border Security Force's; its Directorate General is at Shillong, in keeping with its role across the north-east.",
  "चारों कथन सही हैं। यह बल अंग्रेज़ों द्वारा पूर्वोत्तर में बस्तियों और चाय बाग़ानों की रक्षा के लिए 1835 में खड़ी की गई कछार लेवी से अपना उद्गम मानता है, जिससे यह देश का सबसे पुराना अर्धसैनिक बल है। यह दोहरी व्यवस्था में काम करता है: इसके प्रशासन की ज़िम्मेदारी गृह मंत्रालय की है, जबकि सेना, जिसके अधिकारी इसकी कमान संभालते हैं, उग्रवाद-रोधी और सीमा-कार्यों के लिए परिचालन नियंत्रण रखती है। "
  "‘एक सीमा, एक बल’ नीति के अंतर्गत असम राइफ़ल्स भारत–म्यांमार सीमा की रक्षा करता है, जबकि बांग्लादेश की सीमा सीमा सुरक्षा बल के पास है; पूरे पूर्वोत्तर में इसकी भूमिका के अनुरूप इसका महानिदेशालय शिलांग में है।",
  "Ministry of Home Affairs, annual report (Assam Rifles and border guarding forces); Assam Rifles Act, 2006.",
  "ca-t1-ca-assam-rifles-dual-control", craft="precision")

# Rows renamed in the 2026-shape revision of 2026-10-27 (new concept id: old)
RENAMED = {
          "ca-t1-ca-reports-not-correctly-matched": "ca-t1-ca-reports-wef-ti-eiu-ilo",
          "ca-t1-ca-ai-summit-series-hosts": "ca-t1-ca-ai-impact-summit-sutras-declaration",
          "ca-t1-ca-lwe-state-police-si3": "ca-t1-ca-lwe-deadline-cobra-uapa",
          "ca-t1-ca-pakistan-27th-amendment-fcc-cdf-immunity": "ca-t1-ca-pakistan-27th-amendment-india-cds"}
finish("ca_t1_a.sql", FORMAT, "2026-Q1", update="--update" in sys.argv, replaces=RENAMED)
