# -*- coding: utf-8 -*-
"""Level 3 · Test 5 (GS Integrated Test 5) -- part E: Economy (17) (upsc_l3_cell_targets.mjs 5).
Same cell plan as Tests 1-4.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: the Clean Plant
Programme; makhana and the Makhana Board; NITI Aayog's Fiscal Health Index; the India-UK CETA and the Double
Contribution Convention; the WTO Investment Facilitation for Development Agreement; UPI Circle, UPI Lite and credit
lines on UPI; inflation-indexed bonds; insurance FDI, MF Lite and fortnightly
credit reporting; default loss guarantees, zero MDR and NPCI's status; Mission Vatsalya, PMGKAY, AMRUT 2.0
and PM-SURAJ; the 2025 shipbuilding package; supplier recourse under the Civil Liability for Nuclear Damage Act;
offshore mineral auctions; unexpected inflation and debtors; expected credit loss
provisioning; the RBI's 2025 rate, CRR and stance decisions; the GST Appellate Tribunal.
MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
FM = "Financial Markets, Instruments & Fintech"
MB = "Money, Banking & Monetary Policy"
IN = "Industry, Infrastructure, Energy & Services"
EX = "External Sector & International Institutions"
AG = "Agriculture & Food Economy"
RBI = "Reserve Bank of India"
SEBI = "Securities and Exchange Board of India"

# ---------------------------------------------------------------- Agriculture & Food Economy (m-MCQ, m-stmt)
M(AG, "medium",
  "The Clean Plant Programme approved by the Union government in 2024 aims mainly to:",
  "2024 में केंद्र सरकार द्वारा स्वीकृत स्वच्छ पौध कार्यक्रम (क्लीन प्लांट प्रोग्राम) का मुख्य उद्देश्य क्या है?",
  ["supply fruit growers with certified, disease-free planting material",
   "end the use of chemical pesticides on horticultural crops by 2030",
   "clean farmland of heavy metals by growing plants that absorb them",
   "promote the vertical farming of vegetables in and around large cities"],
  ["फल उत्पादकों को प्रमाणित, रोगमुक्त रोपण सामग्री उपलब्ध कराना",
   "2030 तक बागवानी फ़सलों पर रासायनिक कीटनाशकों का उपयोग समाप्त करना",
   "भारी धातुएँ सोखने वाले पौधे उगाकर खेतों को उनसे मुक्त करना",
   "बड़े शहरों में और उनके आसपास सब्ज़ियों की ऊर्ध्वाधर खेती बढ़ाना"],
  0,
  "Viruses and other pathogens carried in grafts, budwood and saplings spread through orchards and depress the yield and quality of fruit crops such as citrus, apple, grape and mango -- and since a fruit tree bears for decades, an infection planted at the start is costly for the grower's whole working life. The programme, approved in August 2024 with an outlay of about Rs 1,766 crore under the Mission for Integrated Development of Horticulture, is run by the National Horticulture Board with ICAR. "
  "It sets up a network of Clean Plant Centres for diagnosing and eliminating viruses and maintaining disease-free mother plants, a certification system for planting material backed by the Seeds Act, 1966, and support for nurseries to multiply clean stock. The other options describe natural farming, phytoremediation and urban vertical farming, which are separate efforts.",
  "कलम, कलिका-लकड़ी और पौधों के साथ आने वाले विषाणु और अन्य रोगजनक बागों में फैलते हैं और नींबू-वर्गीय फल, सेब, अंगूर और आम जैसी फल फ़सलों की उपज और गुणवत्ता घटाते हैं -- और चूँकि फल का वृक्ष दशकों तक फल देता है, शुरुआत में लगा संक्रमण उत्पादक के पूरे कामकाजी जीवन पर भारी पड़ता है। अगस्त 2024 में एकीकृत बागवानी विकास मिशन के अंतर्गत लगभग 1,766 करोड़ रुपये के परिव्यय से स्वीकृत यह कार्यक्रम राष्ट्रीय बागवानी बोर्ड आईसीएआर के साथ चलाता है। "
  "यह विषाणुओं के निदान और उन्मूलन तथा रोगमुक्त मातृ-पौधों के रखरखाव के लिए स्वच्छ पौध केंद्रों का जाल, बीज अधिनियम, 1966 पर आधारित रोपण सामग्री की प्रमाणन व्यवस्था, और स्वच्छ पौध सामग्री बढ़ाने के लिए नर्सरियों को सहायता देता है। अन्य विकल्प प्राकृतिक खेती, पादप-उपचार (फ़ाइटोरेमेडिएशन) और शहरी ऊर्ध्वाधर खेती का वर्णन करते हैं, जो अलग प्रयास हैं।",
  "Ministry of Agriculture and Farmers Welfare (PIB, August 2024); National Horticulture Board.",
  "l3-t5-eco-clean-plant-programme", pos=0, craft="inference")

S(AG, "medium", "With reference to makhana (fox nut), consider the following statements:",
  "मखाना (फ़ॉक्स नट) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the seed of an aquatic plant grown in ponds and wetlands.",
   "Bihar produces most of India's makhana, and 'Mithila Makhana' carries a geographical indication tag.",
   "The Makhana Board announced in the Union Budget for 2025-26 functions under the Ministry of Commerce and Industry."],
  ["यह तालाबों और आर्द्रभूमियों में उगाए जाने वाले एक जलीय पौधे का बीज है।",
   "भारत का अधिकांश मखाना बिहार में होता है, और ‘मिथिला मखाना’ को भौगोलिक संकेत (जीआई) टैग मिला है।",
   "2025-26 के केंद्रीय बजट में घोषित मखाना बोर्ड वाणिज्य और उद्योग मंत्रालय के अंतर्गत कार्य करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Makhana is the seed of Euryale ferox, a prickly water lily grown in shallow ponds, oxbow lakes and, increasingly, in waterlogged fields of north Bihar -- Darbhanga, Madhubani, Purnea and Katihar -- which together account for the bulk of India's output; 'Mithila Makhana' received a GI tag in 2022. The seeds are gathered from the pond floor by divers, mostly from the Mallah community, and then roasted and popped, a labour-intensive chain in which growers capture little of the final price. "
  "Statement 3 is wrong: the Board, set up in 2025 under the Ministry of Agriculture and Farmers Welfare, is meant to improve production, processing, value addition and marketing and to organise growers into farmer producer organisations. Makhana's growing demand as a health food makes it a test of whether such crop-specific boards can raise farmers' share of value.",
  "कथन 1 और 2 सही हैं। मखाना यूरिएल फ़ेरॉक्स नामक काँटेदार जल-कमल का बीज है, जो उत्तर बिहार -- दरभंगा, मधुबनी, पूर्णिया और कटिहार -- के उथले तालाबों, गोखुर झीलों और बढ़ते रूप में जलभराव वाले खेतों में उगाया जाता है, और यही क्षेत्र भारत के अधिकांश उत्पादन का स्रोत है; ‘मिथिला मखाना’ को 2022 में जीआई टैग मिला। बीज तालाब के तल से गोताख़ोर, अधिकतर मल्लाह समुदाय के लोग, इकट्ठा करते हैं और फिर उन्हें भूनकर फोड़ा जाता है -- एक श्रम-प्रधान शृंखला जिसमें उत्पादकों को अंतिम मूल्य का छोटा हिस्सा मिलता है। "
  "कथन 3 ग़लत है: 2025 में कृषि और किसान कल्याण मंत्रालय के अंतर्गत स्थापित बोर्ड का उद्देश्य उत्पादन, प्रसंस्करण, मूल्य संवर्धन और विपणन सुधारना तथा उत्पादकों को किसान उत्पादक संगठनों में संगठित करना है। स्वास्थ्यवर्धक भोजन के रूप में मखाने की बढ़ती माँग इसे इस बात की कसौटी बनाती है कि क्या ऐसे फ़सल-विशेष बोर्ड किसानों का मूल्य में हिस्सा बढ़ा सकते हैं।",
  "Union Budget 2025-26, Budget Speech; Ministry of Agriculture and Farmers Welfare; Geographical Indications Registry.",
  "l3-t5-eco-makhana-board-bihar", craft="precision")

# ---------------------------------------------------------------- Budget, Deficits & Public Debt (m-stmt)
S("Budget, Deficits & Public Debt", "medium", "With reference to the Fiscal Health Index released by NITI Aayog in 2025, consider the following statements:",
  "2025 में नीति आयोग द्वारा जारी राजकोषीय स्वास्थ्य सूचकांक के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It ranks major States on sub-indices that include the quality of expenditure, revenue mobilisation, fiscal prudence and debt sustainability.",
   "Odisha was ranked first among the major States covered."],
  ["यह प्रमुख राज्यों को व्यय की गुणवत्ता, राजस्व संग्रहण, राजकोषीय विवेक और ऋण संधारणीयता सहित उप-सूचकांकों पर क्रम देता है।",
   "शामिल प्रमुख राज्यों में ओडिशा प्रथम स्थान पर रहा।"],
  T2, 2,
  "Both statements are correct. The index, built on data for 2022-23 for eighteen major States that account for most of India's GDP and population, combines five sub-indices -- quality of expenditure, revenue mobilisation, fiscal prudence, the debt index and debt sustainability -- and groups States as achievers, front-runners, performers and aspirational. Odisha came first, helped by low deficits, a small debt burden and strong non-tax revenue from mining; Punjab came last. "
  "The exercise matters because the States now account for more than half of general government spending, including most spending on health, education and policing, so their fiscal health shapes both public services and the country's overall deficit and debt -- issues that the FRBM framework and the Finance Commissions address only in part.",
  "दोनों कथन सही हैं। यह सूचकांक 2022-23 के आँकड़ों पर उन अठारह प्रमुख राज्यों के लिए बना है जिनमें भारत के जीडीपी और जनसंख्या का अधिकांश भाग है, और यह पाँच उप-सूचकांकों -- व्यय की गुणवत्ता, राजस्व संग्रहण, राजकोषीय विवेक, ऋण सूचकांक और ऋण संधारणीयता -- को मिलाकर राज्यों को अचीवर, फ़्रंट-रनर, परफ़ॉर्मर और आकांक्षी समूहों में रखता है। कम घाटे, छोटे ऋण-भार और खनन से मज़बूत गैर-कर राजस्व के कारण ओडिशा प्रथम रहा; पंजाब अंतिम स्थान पर रहा। "
  "यह अभ्यास इसलिए महत्वपूर्ण है कि अब सामान्य सरकारी व्यय का आधे से अधिक हिस्सा राज्यों का है, जिसमें स्वास्थ्य, शिक्षा और पुलिस पर अधिकांश व्यय शामिल है, इसलिए उनका राजकोषीय स्वास्थ्य सार्वजनिक सेवाओं और देश के कुल घाटे तथा ऋण दोनों को प्रभावित करता है -- ऐसे प्रश्न जिन्हें एफ़आरबीएम ढाँचा और वित्त आयोग केवल आंशिक रूप से संबोधित करते हैं।",
  "NITI Aayog, Fiscal Health Index 2025.", "l3-t5-eco-niti-fiscal-health-index", craft="precision")

# ---------------------------------------------------------------- External Sector & International Institutions (e-SI, m-stmt)
A(EX, "easy",
  "Under the India-United Kingdom Comprehensive Economic and Trade Agreement signed in 2025, almost all Indian exports to the UK are to enter duty-free.",
  "2025 में हस्ताक्षरित भारत-यूनाइटेड किंगडम व्यापक आर्थिक और व्यापार समझौते के अंतर्गत यूके को होने वाला लगभग सारा भारतीय निर्यात शुल्क-मुक्त प्रवेश करेगा।",
  "A separate Double Contribution Convention exempts Indian workers temporarily posted to the UK from paying social security contributions there for up to three years.",
  "एक अलग दोहरा अंशदान अभिसमय यूके में अस्थायी रूप से तैनात भारतीय कर्मियों को वहाँ तीन वर्ष तक सामाजिक सुरक्षा अंशदान देने से छूट देता है।",
  1,
  "Both statements are correct, but Statement II does not explain Statement I. Under the agreement signed in London in July 2025, the UK removes duties on about 99 per cent of its tariff lines, covering nearly all of India's exports by value, which helps labour-intensive goods such as textiles and garments, leather and footwear, gems and jewellery and marine products; India cuts duties on about 90 per cent of tariff lines, phasing down the duty on Scotch whisky and opening a quota for cars. "
  "The Double Contribution Convention deals with a different problem: Indian professionals sent to the UK on short assignments used to pay into both countries' social security systems, and the convention spares them and their employers the UK contributions. Neither takes effect until the agreements are ratified and brought into force.",
  "दोनों कथन सही हैं, पर कथन II, कथन I की व्याख्या नहीं करता। जुलाई 2025 में लंदन में हस्ताक्षरित समझौते के अंतर्गत यूके अपनी लगभग 99 प्रतिशत टैरिफ़ लाइनों पर शुल्क हटाता है, जो मूल्य के हिसाब से भारत के लगभग सारे निर्यात को शामिल करती हैं; इससे वस्त्र और परिधान, चमड़ा और जूते, रत्न और आभूषण तथा समुद्री उत्पाद जैसी श्रम-प्रधान वस्तुओं को लाभ होता है; भारत लगभग 90 प्रतिशत टैरिफ़ लाइनों पर शुल्क घटाता है, स्कॉच व्हिस्की पर शुल्क चरणबद्ध रूप से कम करता है और कारों के लिए कोटा खोलता है। "
  "दोहरा अंशदान अभिसमय एक अलग समस्या से संबंधित है: छोटी अवधि के काम पर यूके भेजे गए भारतीय पेशेवर दोनों देशों की सामाजिक सुरक्षा प्रणालियों में अंशदान देते थे, और यह अभिसमय उन्हें और उनके नियोक्ताओं को यूके के अंशदान से बचाता है। दोनों में से कोई भी समझौतों के अनुसमर्थन और लागू होने से पहले प्रभावी नहीं होता।",
  "Ministry of Commerce and Industry, India-UK Comprehensive Economic and Trade Agreement (2025).",
  "l3-t5-eco-india-uk-ceta-dcc", craft="inference")

S(EX, "medium", "With reference to the Investment Facilitation for Development (IFD) Agreement negotiated by a group of WTO members, consider the following statements:",
  "डब्ल्यूटीओ सदस्यों के एक समूह द्वारा वार्ता किए गए विकास हेतु निवेश सुगमीकरण (आईएफ़डी) समझौते के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["India has opposed incorporating it into the WTO's rulebook.",
   "Adding it as a plurilateral agreement under Annex 4 of the Marrakesh Agreement requires the consensus of all WTO members.",
   "It sets out binding commitments on market access and on the protection of foreign investment, including investor-State dispute settlement."],
  ["भारत ने इसे डब्ल्यूटीओ की नियम-पुस्तिका में शामिल करने का विरोध किया है।",
   "इसे मराकेश समझौते के अनुलग्नक 4 के अंतर्गत बहुपक्षीय-सीमित (प्लूरिलैटरल) समझौते के रूप में जोड़ने के लिए सभी डब्ल्यूटीओ सदस्यों की सर्वसम्मति आवश्यक है।",
   "यह बाज़ार पहुँच और विदेशी निवेश के संरक्षण, जिसमें निवेशक-राज्य विवाद निपटान भी शामिल है, पर बाध्यकारी प्रतिबद्धताएँ तय करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The agreement began as a joint statement initiative in 2017 and was finalised by well over a hundred members; it seeks to make investment procedures more transparent and predictable, with single points of contact for investors and faster approvals. Because it was negotiated among a group of members rather than under a mandate of the whole membership, its supporters asked for it to be added to Annex 4, which under Article X:9 of the Marrakesh Agreement can be done only by consensus -- and India, with South Africa and a few others, blocked this at the Abu Dhabi ministerial conference in 2024, arguing that investment is not a trade issue the WTO was given to negotiate. "
  "Statement 3 is wrong: the text expressly leaves out market access, investment protection and investor-State dispute settlement, which remain the subject of bilateral investment treaties.",
  "कथन 1 और 2 सही हैं। यह समझौता 2017 में एक संयुक्त वक्तव्य पहल के रूप में शुरू हुआ और सौ से अधिक सदस्यों ने इसे अंतिम रूप दिया; यह निवेश प्रक्रियाओं को अधिक पारदर्शी और पूर्वानुमेय बनाने का प्रयास करता है, जिसमें निवेशकों के लिए एकल संपर्क बिंदु और तेज़ स्वीकृतियाँ हैं। चूँकि इसकी वार्ता पूरे सदस्य समुदाय के अधिदेश के बजाय सदस्यों के एक समूह ने की, इसके समर्थकों ने इसे अनुलग्नक 4 में जोड़ने को कहा, जो मराकेश समझौते के अनुच्छेद X:9 के अंतर्गत केवल सर्वसम्मति से हो सकता है -- और भारत ने, दक्षिण अफ़्रीका और कुछ अन्य देशों के साथ, 2024 के अबू धाबी मंत्रिस्तरीय सम्मेलन में इसे रोका, यह तर्क देते हुए कि निवेश ऐसा व्यापार विषय नहीं है जिस पर वार्ता का दायित्व डब्ल्यूटीओ को दिया गया हो। "
  "कथन 3 ग़लत है: पाठ स्पष्ट रूप से बाज़ार पहुँच, निवेश संरक्षण और निवेशक-राज्य विवाद निपटान को बाहर रखता है, जो द्विपक्षीय निवेश संधियों के विषय बने रहते हैं।",
  "World Trade Organization, Investment Facilitation for Development Agreement and MC13 (Abu Dhabi, 2024); Marrakesh Agreement, Article X:9.",
  "l3-t5-eco-wto-investment-facilitation", craft="linkage")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (e-stmt, h-stmt, m-stmt x2)
S(FM, "easy", "With reference to recent features of the Unified Payments Interface (UPI), consider the following statements:",
  "यूनिफ़ाइड पेमेंट्स इंटरफ़ेस (यूपीआई) की हाल की सुविधाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["UPI Circle lets a primary account holder allow a trusted person, such as a family member, to make UPI payments from the primary user's account.",
   "UPI Lite allows small-value payments without entering a UPI PIN for each transaction.",
   "Credit lines pre-sanctioned by banks can be linked to UPI and used to make payments."],
  ["यूपीआई सर्कल प्राथमिक खाताधारक को किसी विश्वसनीय व्यक्ति, जैसे परिवार के सदस्य, को अपने खाते से यूपीआई भुगतान करने की अनुमति देने देता है।",
   "यूपीआई लाइट हर लेन-देन पर यूपीआई पिन डाले बिना छोटे मूल्य के भुगतान की सुविधा देता है।",
   "बैंकों द्वारा पहले से स्वीकृत ऋण-सीमाएँ (क्रेडिट लाइन) यूपीआई से जोड़कर भुगतान के लिए प्रयोग की जा सकती हैं।"],
  C3, 2,
  "All three are correct. UPI Circle, launched in 2024, offers delegated payments: the primary user can either set a monthly limit within which a secondary user pays on his own, or approve each payment -- useful for elderly parents, students and others without their own bank accounts. UPI Lite keeps a small balance on the device from which low-value payments go through without a PIN and without loading the bank's core system, which makes everyday transactions faster and cuts failures. "
  "Credit lines on UPI let a borrower pay merchants from a pre-approved overdraft or loan account instead of a savings account, so UPI can carry small-ticket credit to people who have no credit card. Each extends the reach of the platform from a pure payment rail towards credit and household use.",
  "तीनों कथन सही हैं। 2024 में शुरू हुआ यूपीआई सर्कल प्रत्यायोजित भुगतान देता है: प्राथमिक उपयोगकर्ता या तो मासिक सीमा तय कर सकता है जिसके भीतर द्वितीयक उपयोगकर्ता स्वयं भुगतान करे, या हर भुगतान को स्वीकृत कर सकता है -- यह बुज़ुर्ग माता-पिता, विद्यार्थियों और बिना अपने बैंक खाते वाले लोगों के लिए उपयोगी है। यूपीआई लाइट उपकरण पर छोटी राशि रखता है जिससे कम मूल्य के भुगतान बिना पिन और बिना बैंक की मुख्य प्रणाली पर भार डाले हो जाते हैं, जिससे रोज़मर्रा के लेन-देन तेज़ होते हैं और विफलताएँ घटती हैं। "
  "यूपीआई पर क्रेडिट लाइन उधारकर्ता को बचत खाते के बजाय पहले से स्वीकृत ओवरड्राफ़्ट या ऋण खाते से व्यापारियों को भुगतान करने देती है, ताकि यूपीआई उन लोगों तक छोटे ऋण पहुँचा सके जिनके पास क्रेडिट कार्ड नहीं है। हर सुविधा मंच को केवल भुगतान माध्यम से आगे ऋण और घरेलू उपयोग की ओर ले जाती है।",
  RBI + ", Statements on Developmental and Regulatory Policies (2023-24); National Payments Corporation of India.",
  "l3-t5-eco-upi-circle-lite-credit-line", craft="recall")

S(FM, "hard", "With reference to inflation-indexed bonds, consider the following statements:",
  "मुद्रास्फीति-सूचकांकित बॉन्डों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["In a capital-indexed bond, the principal is adjusted for inflation and the interest is paid on the adjusted principal.",
   "The difference between the yield on an ordinary bond and that on an inflation-indexed bond of the same maturity is read as the market's expectation of inflation.",
   "Compared with an ordinary bond of the same maturity, such a bond does best for its holder when inflation turns out lower than expected.",
   "India's inflation-indexed bonds of 2013 were linked to the Wholesale Price Index, which reduced their appeal to savers facing higher consumer price inflation."],
  ["पूँजी-सूचकांकित बॉन्ड में मूलधन को मुद्रास्फीति के अनुसार समायोजित किया जाता है और ब्याज समायोजित मूलधन पर दिया जाता है।",
   "समान परिपक्वता के साधारण बॉन्ड और मुद्रास्फीति-सूचकांकित बॉन्ड के प्रतिफल के अंतर को बाज़ार की अपेक्षित मुद्रास्फीति माना जाता है।",
   "समान परिपक्वता के साधारण बॉन्ड की तुलना में ऐसा बॉन्ड धारक के लिए तब सबसे अच्छा रहता है जब मुद्रास्फीति अपेक्षा से कम निकले।",
   "भारत के 2013 के मुद्रास्फीति-सूचकांकित बॉन्ड थोक मूल्य सूचकांक से जुड़े थे, जिससे ऊँची उपभोक्ता मूल्य मुद्रास्फीति झेल रहे बचतकर्ताओं के लिए उनका आकर्षण घटा।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. Because the principal rises with the price index and the coupon is paid on that rising principal, the holder's real return is fixed -- which is why such bonds carry a lower 'real' yield than the nominal yield on ordinary bonds. The gap between the two yields, the 'breakeven' inflation rate, is watched by central banks as a market-based measure of inflation expectations. "
  "Statement 3 is the reverse of the truth: the indexed bond beats the ordinary one when inflation turns out higher than the breakeven rate, and loses when it turns out lower. In 2013 the RBI issued bonds linked to the WPI while households faced much higher CPI inflation, so they did little to protect savers; a CPI-linked retail series followed, but demand stayed thin. Such bonds also help a government signal its commitment to low inflation, since high inflation would raise its own debt service.",
  "कथन 1, 2 और 4 सही हैं। चूँकि मूलधन मूल्य सूचकांक के साथ बढ़ता है और कूपन उसी बढ़ते मूलधन पर मिलता है, धारक का वास्तविक प्रतिफल स्थिर रहता है -- इसीलिए ऐसे बॉन्ड पर साधारण बॉन्ड के नाममात्र प्रतिफल से कम ‘वास्तविक’ प्रतिफल होता है। दोनों प्रतिफलों का अंतर, ‘ब्रेकईवन’ मुद्रास्फीति दर, केंद्रीय बैंक मुद्रास्फीति अपेक्षाओं के बाज़ार-आधारित माप के रूप में देखते हैं। "
  "कथन 3 सत्य का उल्टा है: सूचकांकित बॉन्ड साधारण बॉन्ड से तब बेहतर रहता है जब मुद्रास्फीति ब्रेकईवन दर से अधिक निकले, और कम निकलने पर पीछे रहता है। 2013 में आरबीआई ने डब्ल्यूपीआई से जुड़े बॉन्ड जारी किए जबकि परिवार बहुत ऊँची सीपीआई मुद्रास्फीति झेल रहे थे, इसलिए उन्होंने बचतकर्ताओं की बहुत कम रक्षा की; बाद में सीपीआई से जुड़ी खुदरा शृंखला आई, पर माँग कमज़ोर रही। ऐसे बॉन्ड सरकार को कम मुद्रास्फीति के प्रति अपनी प्रतिबद्धता दिखाने में भी मदद करते हैं, क्योंकि ऊँची मुद्रास्फीति उसका अपना ऋण-भुगतान बढ़ाएगी।",
  RBI + ", press releases on Inflation Indexed Bonds (2013) and Inflation Indexed National Savings Securities.",
  "l3-t5-eco-inflation-indexed-bonds", craft="inference")

S(FM, "medium", "With reference to recent changes in the regulation of India's financial sector, consider the following statements:",
  "भारत के वित्तीय क्षेत्र के विनियमन में हाल के बदलावों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Union Budget for 2025-26 proposed raising the limit for foreign direct investment in insurance companies from 74 to 100 per cent, for companies that invest the entire premium in India.",
   "SEBI's 'MF Lite' framework relaxes entry and compliance norms for sponsors that run only passive funds such as index funds and exchange-traded funds.",
   "Lenders must now report credit information to credit information companies every fortnight rather than every month."],
  ["2025-26 के केंद्रीय बजट में बीमा कंपनियों में प्रत्यक्ष विदेशी निवेश की सीमा 74 से बढ़ाकर 100 प्रतिशत करने का प्रस्ताव था, उन कंपनियों के लिए जो पूरा प्रीमियम भारत में निवेश करें।",
   "सेबी का ‘एमएफ़ लाइट’ ढाँचा उन प्रायोजकों के लिए प्रवेश और अनुपालन मानदंड आसान करता है जो केवल इंडेक्स फ़ंड और एक्सचेंज-ट्रेडेड फ़ंड जैसे निष्क्रिय फ़ंड चलाते हैं।",
   "ऋणदाताओं को अब साख सूचना कंपनियों को साख सूचना मासिक के बजाय हर पखवाड़े देनी होती है।"],
  C3, 2,
  "All three are correct. The insurance proposal, which required amending the insurance laws, aims to bring in long-term foreign capital for a sector whose penetration remains low, with the condition that premiums stay invested in India. MF Lite lowers the net-worth, track-record and other requirements for asset managers that run only passive schemes, whose risks lie mainly in tracking an index, to encourage new entrants and cut costs for investors. "
  "And from January 2025 the RBI has required lenders to report to the credit bureaus on the fifteenth and the last day of each month, so that a borrower's repayment or default shows up in credit reports faster -- which helps lenders price risk and lets borrowers who repay see their scores improve sooner.",
  "तीनों कथन सही हैं। बीमा प्रस्ताव, जिसके लिए बीमा क़ानूनों में संशोधन आवश्यक था, उस क्षेत्र में दीर्घकालिक विदेशी पूँजी लाने का लक्ष्य रखता है जिसकी पैठ अब भी कम है, इस शर्त के साथ कि प्रीमियम भारत में ही निवेशित रहें। एमएफ़ लाइट केवल निष्क्रिय योजनाएँ चलाने वाले परिसंपत्ति प्रबंधकों के लिए निवल मालियत, पिछले रिकॉर्ड और अन्य अपेक्षाएँ घटाता है, जिनका जोखिम मुख्यतः किसी सूचकांक का अनुसरण करने में है, ताकि नए प्रवेशक आएँ और निवेशकों की लागत घटे। "
  "और जनवरी 2025 से आरबीआई ने ऋणदाताओं से हर महीने की पंद्रह तारीख़ और अंतिम दिन साख ब्यूरो को सूचना देने की अपेक्षा की है, ताकि उधारकर्ता का पुनर्भुगतान या चूक साख रिपोर्टों में जल्दी दिखे -- जिससे ऋणदाता जोखिम का बेहतर मूल्यांकन करते हैं और समय पर चुकाने वाले उधारकर्ताओं के स्कोर जल्दी सुधरते हैं।",
  "Union Budget 2025-26, Budget Speech; SEBI, board decisions on MF Lite (2024); RBI, directions on reporting of credit information (2024).",
  "l3-t5-eco-insurance-fdi-mf-lite-fortnightly-credit", craft="precision")

S(FM, "medium", "With reference to digital payments and digital lending in India, consider the following statements:",
  "भारत में डिजिटल भुगतान और डिजिटल ऋण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the RBI's rules, a default loss guarantee given by a fintech partner to a bank or NBFC in digital lending is capped at 5 per cent of the loan portfolio.",
   "No merchant discount rate is charged on UPI payments and on RuPay debit card transactions.",
   "The National Payments Corporation of India, which runs UPI, is a statutory body set up by an Act of Parliament."],
  ["आरबीआई के नियमों के अंतर्गत डिजिटल ऋण में किसी फ़िनटेक साझेदार द्वारा बैंक या एनबीएफ़सी को दी गई चूक हानि गारंटी ऋण पोर्टफ़ोलियो के 5 प्रतिशत तक सीमित है।",
   "यूपीआई भुगतानों और रुपे डेबिट कार्ड लेन-देन पर कोई मर्चेंट डिस्काउंट रेट नहीं लिया जाता।",
   "यूपीआई चलाने वाला भारतीय राष्ट्रीय भुगतान निगम संसद के अधिनियम द्वारा स्थापित सांविधिक निकाय है।"],
  C3, 1,
  "Statements 1 and 2 are correct. A default loss guarantee lets a lending app or other fintech share the first losses on loans it sources for a regulated lender; the RBI's 2023 guidelines allow it but cap it at 5 per cent of the portfolio and require it to be backed by cash, a fixed deposit or a bank guarantee, so that the fintech keeps 'skin in the game' without the lender passing on its credit risk entirely. Since 2020 the merchant discount rate on UPI and RuPay debit card payments has been set at zero, and the government compensates banks and other participants through an incentive scheme. "
  "Statement 3 is wrong: the NPCI was set up in 2008 as a not-for-profit company, promoted by banks under the guidance of the RBI and the Indian Banks' Association; it is regulated by the RBI under the Payment and Settlement Systems Act. It has also set a 30 per cent cap on the share of UPI volume any single third-party app may handle, though the deadline for compliance has been extended.",
  "कथन 1 और 2 सही हैं। चूक हानि गारंटी किसी ऋण ऐप या अन्य फ़िनटेक को किसी विनियमित ऋणदाता के लिए लाए गए ऋणों पर पहली हानियों में हिस्सा लेने देती है; आरबीआई के 2023 के दिशानिर्देश इसकी अनुमति देते हैं पर इसे पोर्टफ़ोलियो के 5 प्रतिशत तक सीमित करते हैं और नक़द, सावधि जमा या बैंक गारंटी से समर्थित होना अनिवार्य करते हैं, ताकि फ़िनटेक का दाँव बना रहे पर ऋणदाता अपना ऋण जोखिम पूरी तरह आगे न बढ़ा दे। 2020 से यूपीआई और रुपे डेबिट कार्ड भुगतानों पर मर्चेंट डिस्काउंट रेट शून्य है, और सरकार एक प्रोत्साहन योजना से बैंकों और अन्य भागीदारों की क्षतिपूर्ति करती है। "
  "कथन 3 ग़लत है: एनपीसीआई 2008 में आरबीआई और भारतीय बैंक संघ के मार्गदर्शन में बैंकों द्वारा प्रवर्तित एक गैर-लाभकारी कंपनी के रूप में स्थापित हुआ; यह भुगतान और निपटान प्रणाली अधिनियम के अंतर्गत आरबीआई द्वारा विनियमित है। इसने किसी एक तृतीय-पक्ष ऐप द्वारा संभाले जा सकने वाले यूपीआई लेन-देन के हिस्से पर 30 प्रतिशत की सीमा भी तय की है, हालाँकि अनुपालन की समय-सीमा बढ़ा दी गई है।",
  RBI + ", Guidelines on Default Loss Guarantee in Digital Lending (2023); Payment and Settlement Systems Act, 2007; National Payments Corporation of India.",
  "l3-t5-eco-dlg-zero-mdr-npci-status", craft="precision")

# ---------------------------------------------------------------- Inclusive Growth, Welfare & Demography (h-pairs)
P("Inclusive Growth, Welfare & Demography", "hard", "Consider the following pairs of schemes and the Ministries that run them:",
  "योजनाओं और उन्हें चलाने वाले मंत्रालयों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Mission Vatsalya : Ministry of Women and Child Development",
   "Pradhan Mantri Garib Kalyan Anna Yojana : Ministry of Consumer Affairs, Food and Public Distribution",
   "AMRUT 2.0 : Ministry of Housing and Urban Affairs",
   "PM-SURAJ portal : Ministry of Social Justice and Empowerment"],
  ["मिशन वात्सल्य : महिला और बाल विकास मंत्रालय",
   "प्रधानमंत्री ग़रीब कल्याण अन्न योजना : उपभोक्ता मामले, खाद्य और सार्वजनिक वितरण मंत्रालय",
   "अमृत 2.0 : आवास और शहरी कार्य मंत्रालय",
   "पीएम-सूरज पोर्टल : सामाजिक न्याय और अधिकारिता मंत्रालय"],
  3,
  "All four pairs are correct, though each invites a wrong guess. Mission Vatsalya is the umbrella scheme for child protection -- child care institutions, adoption, sponsorship and foster care, and the 1098 child helpline -- run by the Ministry of Women and Child Development, not the Social Justice Ministry. The PMGKAY, which gives free foodgrains to about 81 crore beneficiaries under the National Food Security Act and was extended for five years from January 2024, is run by the Department of Food and Public Distribution, not the Ministry of Rural Development. "
  "AMRUT 2.0, which aims at piped water supply in every statutory town and at sewerage in the larger cities, belongs to the Ministry of Housing and Urban Affairs even though it is about water. The PM-SURAJ portal, launched in 2024, offers credit support to Scheduled Castes, Other Backward Classes and sanitation workers through the Social Justice Ministry's finance corporations.",
  "चारों युग्म सही हैं, हालाँकि हर एक ग़लत अनुमान को न्योता देता है। मिशन वात्सल्य बाल संरक्षण की छत्र योजना है -- बाल देखभाल संस्थाएँ, दत्तक-ग्रहण, प्रायोजन और पालन-पोषण देखभाल, और 1098 चाइल्ड हेल्पलाइन -- जिसे सामाजिक न्याय मंत्रालय नहीं, महिला और बाल विकास मंत्रालय चलाता है। राष्ट्रीय खाद्य सुरक्षा अधिनियम के अंतर्गत लगभग 81 करोड़ लाभार्थियों को मुफ़्त अनाज देने वाली और जनवरी 2024 से पाँच वर्ष के लिए बढ़ाई गई पीएमजीकेएवाई को ग्रामीण विकास मंत्रालय नहीं, खाद्य और सार्वजनिक वितरण विभाग चलाता है। "
  "अमृत 2.0, जिसका लक्ष्य हर सांविधिक नगर में नल से जल आपूर्ति और बड़े शहरों में सीवरेज है, जल से संबंधित होने के बावजूद आवास और शहरी कार्य मंत्रालय की योजना है। 2024 में शुरू हुआ पीएम-सूरज पोर्टल सामाजिक न्याय मंत्रालय के वित्त निगमों के माध्यम से अनुसूचित जातियों, अन्य पिछड़े वर्गों और सफ़ाई कर्मियों को ऋण सहायता देता है।",
  "Ministries of Women and Child Development; Consumer Affairs, Food and Public Distribution; Housing and Urban Affairs; Social Justice and Empowerment (PIB releases).",
  "l3-t5-eco-schemes-vatsalya-pmgkay-amrut-suraj", craft="precision")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (e-stmt, m-MCQ, m-stmt)
S(IN, "easy", "With reference to recent measures to develop shipbuilding in India, consider the following statements:",
  "भारत में जहाज़ निर्माण के विकास के हाल के उपायों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["In 2025 the Union Cabinet approved a package for shipbuilding and maritime development that includes a Maritime Development Fund for long-term financing.",
   "Large ships above a specified size have been included in the Harmonised Master List of infrastructure, easing their access to long-term credit."],
  ["2025 में केंद्रीय मंत्रिमंडल ने जहाज़ निर्माण और समुद्री विकास के लिए एक पैकेज स्वीकृत किया जिसमें दीर्घकालिक वित्तपोषण के लिए समुद्री विकास कोष शामिल है।",
   "एक निर्धारित आकार से बड़े जहाज़ों को अवसंरचना की सुसंगत मास्टर सूची में शामिल किया गया है, जिससे उन्हें दीर्घकालिक ऋण आसानी से मिल सके।"],
  T2, 2,
  "Both statements are correct. India builds well under one per cent of the world's ships, a market dominated by China, South Korea and Japan, and most Indian cargo travels on foreign-owned vessels, so freight payments drain foreign exchange. The package approved in 2025 extends the Shipbuilding Financial Assistance Scheme, creates a Maritime Development Fund to provide long-term capital, and supports shipbuilding clusters and yard capacity. "
  "Ships are expensive, long-lived assets, and their inclusion in the infrastructure list lets lenders treat ship finance like infrastructure lending, with longer tenures and easier limits. Together these aim to build an Indian fleet and yards that can also serve defence needs, in line with the goals of the Maritime India Vision.",
  "दोनों कथन सही हैं। भारत विश्व के एक प्रतिशत से भी कम जहाज़ बनाता है, एक ऐसा बाज़ार जिस पर चीन, दक्षिण कोरिया और जापान का प्रभुत्व है, और अधिकांश भारतीय माल विदेशी स्वामित्व वाले जहाज़ों पर जाता है, इसलिए भाड़े के भुगतान से विदेशी मुद्रा बाहर जाती है। 2025 में स्वीकृत पैकेज जहाज़ निर्माण वित्तीय सहायता योजना को आगे बढ़ाता है, दीर्घकालिक पूँजी देने के लिए समुद्री विकास कोष बनाता है, और जहाज़ निर्माण क्लस्टरों तथा यार्ड क्षमता को सहायता देता है। "
  "जहाज़ महँगी, लंबी आयु वाली परिसंपत्तियाँ हैं, और अवसंरचना सूची में उनके शामिल होने से ऋणदाता जहाज़ वित्त को अवसंरचना ऋण की तरह, लंबी अवधि और आसान सीमाओं के साथ, मान सकते हैं। मिलकर इनका लक्ष्य एक भारतीय बेड़ा और ऐसे यार्ड बनाना है जो रक्षा ज़रूरतें भी पूरी कर सकें, मैरीटाइम इंडिया विज़न के लक्ष्यों के अनुरूप।",
  "Ministry of Ports, Shipping and Waterways (PIB, 2025); Union Budget 2025-26, Budget Speech; Department of Economic Affairs, Harmonised Master List of Infrastructure Sub-sectors.",
  "l3-t5-eco-shipbuilding-package-2025", craft="recall")

M(IN, "medium",
  "Foreign suppliers of nuclear reactors long hesitated to supply India mainly because of a provision of the Civil Liability for Nuclear Damage Act, 2010 that:",
  "परमाणु रिएक्टरों के विदेशी आपूर्तिकर्ता लंबे समय तक भारत को आपूर्ति करने में मुख्यतः परमाणु क्षति के लिए सिविल दायित्व अधिनियम, 2010 के किस उपबंध के कारण हिचकिचाते रहे?",
  ["barred foreign companies from owning even a minority share in any Indian nuclear plant operator",
   "set no upper limit at all on the liability of the operator of a nuclear power plant",
   "required every reactor in India to run only on uranium mined within the country",
   "let the operator claim recourse from a supplier whose faulty equipment caused the damage"],
  ["विदेशी कंपनियों को किसी भी भारतीय परमाणु संयंत्र संचालक में अल्पांश हिस्सेदारी रखने से भी रोकता था",
   "परमाणु बिजलीघर के संचालक के दायित्व पर कोई ऊपरी सीमा तय नहीं करता था",
   "भारत के हर रिएक्टर को केवल देश में खनित यूरेनियम पर चलाना अनिवार्य करता था",
   "संचालक को उस आपूर्तिकर्ता से क्षतिपूर्ति माँगने देता था जिसके दोषपूर्ण उपकरण से क्षति हुई"],
  3,
  "The Act channels liability for a nuclear accident to the operator -- strictly, without proof of fault, and up to a cap of Rs 1,500 crore, with the government covering further compensation. But section 17(b) gave the operator a right of recourse against a supplier where the accident resulted from patent or latent defects in equipment or substandard services, a departure from international practice under the Convention on Supplementary Compensation, which channels liability to the operator alone. Section 46 also left open claims under other laws. "
  "Suppliers feared open-ended exposure, so India set up the India Nuclear Insurance Pool in 2015 and ratified the Convention in 2016, but few new foreign projects followed. In 2025 Parliament passed the SHANTI Act, which opens nuclear power to private companies and recasts the liability framework. The cap in option (b) and the other options are not features of the 2010 Act.",
  "अधिनियम परमाणु दुर्घटना का दायित्व संचालक पर डालता है -- कठोरता से, दोष सिद्ध किए बिना, और 1,500 करोड़ रुपये की सीमा तक, जिसके आगे की क्षतिपूर्ति सरकार देती है। पर धारा 17(ख) ने संचालक को आपूर्तिकर्ता के विरुद्ध क्षतिपूर्ति माँगने का अधिकार दिया जहाँ दुर्घटना उपकरण के प्रकट या गुप्त दोषों या घटिया सेवाओं से हुई हो; यह अनुपूरक क्षतिपूर्ति अभिसमय की अंतरराष्ट्रीय प्रथा से भिन्न था, जो दायित्व केवल संचालक पर डालता है। धारा 46 ने अन्य क़ानूनों के अंतर्गत दावों का रास्ता भी खुला छोड़ा। "
  "आपूर्तिकर्ताओं को असीमित जोखिम का भय था, इसलिए भारत ने 2015 में इंडिया न्यूक्लियर इंश्योरेंस पूल बनाया और 2016 में अभिसमय का अनुसमर्थन किया, पर कुछ ही नई विदेशी परियोजनाएँ आईं। 2025 में संसद ने शांति (SHANTI) अधिनियम पारित किया, जो परमाणु ऊर्जा को निजी कंपनियों के लिए खोलता है और दायित्व ढाँचे को नए सिरे से तय करता है। विकल्प (ख) की बात और अन्य विकल्प 2010 के अधिनियम की विशेषताएँ नहीं हैं।",
  "Civil Liability for Nuclear Damage Act, 2010, sections 4, 6, 17 and 46; Department of Atomic Energy; Ministry of External Affairs, FAQs on the CLND Act (2015).",
  "l3-t5-eco-clnda-supplier-recourse", pos=3, craft="inference")

S(IN, "medium", "With reference to offshore mineral blocks in India, consider the following statements:",
  "भारत में अपतटीय खनिज ब्लॉकों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first tranche of auctions of offshore mineral blocks was launched in 2024 under the Offshore Areas Mineral (Development and Regulation) Act, 2002.",
   "Unlike most onshore mineral blocks, which State governments auction, offshore blocks are auctioned by the Union government.",
   "The first tranche offered blocks of construction sand off Kerala, lime mud off Gujarat and polymetallic nodules and crusts near the Andaman and Nicobar Islands.",
   "An amendment to the offshore law in 2023 made auction the only route for granting production rights in offshore areas."],
  ["अपतटीय खनिज ब्लॉकों की नीलामी की पहली खेप 2024 में अपतटीय क्षेत्र खनिज (विकास और विनियमन) अधिनियम, 2002 के अंतर्गत शुरू की गई।",
   "अधिकांश स्थलीय खनिज ब्लॉकों के विपरीत, जिनकी नीलामी राज्य सरकारें करती हैं, अपतटीय ब्लॉकों की नीलामी केंद्र सरकार करती है।",
   "पहली खेप में केरल के पास निर्माण रेत, गुजरात के पास चूना-पंक और अंडमान-निकोबार द्वीपसमूह के पास बहुधात्विक पिंडों और परतों के ब्लॉक रखे गए।",
   "2023 में अपतटीय क़ानून में संशोधन ने अपतटीय क्षेत्रों में उत्पादन अधिकार देने का एकमात्र मार्ग नीलामी बना दिया।"],
  C4, 3,
  "All four are correct. Minerals in India's territorial waters, continental shelf and exclusive economic zone belong to the Union, so the Ministry of Mines runs these auctions, whereas onshore major-mineral blocks are auctioned by the States, which also collect the royalty. The 2002 Act had long remained largely unused; the 2023 amendment made auction the only way to grant rights, capped the area a single company may hold, and set up a trust fund for exploration and for people affected by offshore mining. "
  "The first tranche, launched in November 2024, met protests from fishing communities in Kerala, who feared that dredging sand from the shallow sea floor would destroy fish breeding grounds -- the familiar trade-off between mineral supply and coastal ecology and livelihoods. Deep-sea nodules in international waters, by contrast, fall under the International Seabed Authority, not under this Act.",
  "चारों कथन सही हैं। भारत के प्रादेशिक जल, महाद्वीपीय मग्नतट और अनन्य आर्थिक क्षेत्र के खनिज संघ के हैं, इसलिए खान मंत्रालय ये नीलामियाँ करता है, जबकि स्थलीय प्रमुख खनिज ब्लॉकों की नीलामी राज्य करते हैं, जो रॉयल्टी भी लेते हैं। 2002 का अधिनियम लंबे समय तक लगभग अप्रयुक्त रहा; 2023 के संशोधन ने अधिकार देने का एकमात्र मार्ग नीलामी बनाया, एक कंपनी द्वारा रखे जा सकने वाले क्षेत्र की सीमा तय की, और अन्वेषण तथा अपतटीय खनन से प्रभावित लोगों के लिए एक न्यास निधि बनाई। "
  "नवंबर 2024 में शुरू हुई पहली खेप का केरल के मछुआरा समुदायों ने विरोध किया, जिन्हें भय था कि उथले समुद्र तल से रेत निकालने से मछलियों के प्रजनन स्थल नष्ट होंगे -- खनिज आपूर्ति और तटीय पारिस्थितिकी तथा आजीविका के बीच परिचित संतुलन। इसके विपरीत, अंतरराष्ट्रीय जल के गहरे समुद्री पिंड इस अधिनियम के नहीं, अंतरराष्ट्रीय समुद्र तल प्राधिकरण के अधीन आते हैं।",
  "Ministry of Mines, auction of offshore mineral blocks (2024); Offshore Areas Mineral (Development and Regulation) Amendment Act, 2023.",
  "l3-t5-eco-offshore-mineral-blocks", craft="linkage")

# ---------------------------------------------------------------- Macro Concepts, National Income & Inflation (e-SI)
A("Macro Concepts, National Income & Inflation", "easy",
  "Unexpectedly high inflation tends to benefit borrowers at the expense of lenders.",
  "अप्रत्याशित रूप से ऊँची मुद्रास्फीति उधारदाताओं की क़ीमत पर उधारकर्ताओं को लाभ पहुँचाती है।",
  "It reduces the real value of repayments that were fixed in money terms when the loan was made.",
  "यह उन पुनर्भुगतानों का वास्तविक मूल्य घटा देती है जो ऋण देते समय मुद्रा के रूप में तय किए गए थे।",
  0,
  "Both statements are correct and Statement II explains Statement I. A loan fixes repayments in rupees; if prices rise faster than both sides expected, each rupee repaid buys less, so the real interest rate -- roughly the nominal rate minus inflation -- turns out lower, and can even be negative. Savers in fixed deposits, pensioners on fixed incomes and other creditors lose, while debtors, including governments with large nominal debt, gain. "
  "The key word is 'unexpectedly': when inflation is anticipated, lenders build it into the nominal interest rate, so the redistribution happens mainly through surprises. This is one reason central banks try to anchor inflation expectations, and why some savers seek inflation-indexed instruments.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। ऋण पुनर्भुगतान को रुपयों में तय करता है; यदि क़ीमतें दोनों पक्षों की अपेक्षा से तेज़ बढ़ें, तो लौटाया गया हर रुपया कम ख़रीद पाता है, इसलिए वास्तविक ब्याज दर -- मोटे तौर पर नाममात्र दर घटा मुद्रास्फीति -- कम निकलती है, और ऋणात्मक भी हो सकती है। सावधि जमा वाले बचतकर्ता, स्थिर आय वाले पेंशनभोगी और अन्य लेनदार हारते हैं, जबकि देनदार, जिनमें बड़े नाममात्र ऋण वाली सरकारें भी हैं, लाभ पाते हैं। "
  "मुख्य शब्द ‘अप्रत्याशित’ है: जब मुद्रास्फीति का पूर्वानुमान हो, तो उधारदाता उसे नाममात्र ब्याज दर में जोड़ लेते हैं, इसलिए पुनर्वितरण मुख्यतः अचानक बदलावों से होता है। यह एक कारण है कि केंद्रीय बैंक मुद्रास्फीति अपेक्षाओं को स्थिर रखने का प्रयास करते हैं, और कुछ बचतकर्ता मुद्रास्फीति-सूचकांकित साधन चाहते हैं।",
  "NCERT Class XII, Introductory Macroeconomics; " + RBI + ", Monetary Policy Report.",
  "l3-t5-eco-unexpected-inflation-debtors", craft="application")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (m-MCQ, m-stmt)
M(MB, "medium",
  "Under the expected credit loss approach that the RBI is introducing for banks, provisions against loans are to be made on the basis of:",
  "आरबीआई द्वारा बैंकों के लिए लाई जा रही अपेक्षित ऋण हानि पद्धति के अंतर्गत ऋणों के विरुद्ध प्रावधान किस आधार पर किए जाने हैं?",
  ["losses recognised only after a loan has remained overdue for more than ninety days",
   "a flat percentage of every loan, the same whatever the risk of the borrower",
   "expected future losses, estimated from the day a loan is made",
   "the amount written off when a borrower is declared insolvent under the IBC"],
  ["केवल तब मान्य हानियाँ जब ऋण नब्बे दिनों से अधिक समय तक अतिदेय रहे",
   "हर ऋण का एक समान प्रतिशत, उधारकर्ता का जोखिम चाहे जो हो",
   "भावी अपेक्षित हानियाँ, ऋण देने के दिन से आकलित",
   "वह राशि जो किसी उधारकर्ता के आईबीसी के अंतर्गत दिवालिया घोषित होने पर बट्टे खाते में डाली जाए"],
  2,
  "Under the present 'incurred loss' approach, a bank provides mainly after a loan turns non-performing -- typically after ninety days overdue -- so provisions come late and bunch up in downturns, as the bad-loan crisis of the 2010s showed. The expected credit loss framework, aligned with Ind AS 109 and IFRS 9, requires provisions for expected losses from the start: loans are placed in three stages, with twelve-month expected losses for performing loans and lifetime expected losses once credit risk rises significantly or the loan is impaired. "
  "The RBI has proposed to apply it from April 2027, with a transition period to spread the one-time rise in provisions. Forward-looking provisioning makes banks build buffers in good times and recognise stress early, at the cost of more judgement in estimating losses. Options (a) and (d) describe today's backward-looking practice; (b) ignores risk altogether.",
  "वर्तमान ‘घटित हानि’ पद्धति में बैंक मुख्यतः तब प्रावधान करता है जब ऋण अनर्जक हो जाए -- सामान्यतः नब्बे दिन अतिदेय होने के बाद -- इसलिए प्रावधान देर से आते हैं और मंदी में इकट्ठे हो जाते हैं, जैसा 2010 के दशक के डूबत ऋण संकट ने दिखाया। इंड एएस 109 और आईएफ़आरएस 9 के अनुरूप अपेक्षित ऋण हानि ढाँचा शुरू से ही अपेक्षित हानियों के लिए प्रावधान माँगता है: ऋणों को तीन चरणों में रखा जाता है, अर्जक ऋणों के लिए बारह महीने की अपेक्षित हानि और ऋण जोखिम काफ़ी बढ़ने या ऋण के क्षतिग्रस्त होने पर पूरे जीवनकाल की अपेक्षित हानि। "
  "आरबीआई ने इसे अप्रैल 2027 से लागू करने का प्रस्ताव किया है, प्रावधानों में एकबारगी वृद्धि को फैलाने के लिए संक्रमण अवधि के साथ। भविष्योन्मुखी प्रावधान बैंकों को अच्छे समय में बफ़र बनाने और दबाव को जल्दी पहचानने के लिए बाध्य करता है, हानियों के आकलन में अधिक विवेक की क़ीमत पर। विकल्प (क) और (घ) आज की पश्चदर्शी प्रथा का वर्णन करते हैं; (ख) जोखिम को पूरी तरह अनदेखा करता है।",
  RBI + ", Draft Directions on Expected Credit Loss provisioning (2025); Ind AS 109.",
  "l3-t5-eco-expected-credit-loss", pos=2, craft="inference")

S(MB, "medium", "With reference to the monetary policy of the Reserve Bank of India in 2025, consider the following statements:",
  "2025 में भारतीय रिज़र्व बैंक की मौद्रिक नीति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The RBI raised the repo rate in several steps to bring down inflation, which stayed above its tolerance band through the year.",
   "In June 2025 it announced that the cash reserve ratio would be cut to 3 per cent of net demand and time liabilities, in instalments.",
   "In June 2025 it changed its policy stance from 'neutral' to 'accommodative'."],
  ["आरबीआई ने मुद्रास्फीति घटाने के लिए कई चरणों में रेपो दर बढ़ाई, जो पूरे वर्ष उसकी सहनशीलता सीमा से ऊपर रही।",
   "जून 2025 में उसने घोषणा की कि नकद आरक्षित अनुपात को किस्तों में शुद्ध माँग और सावधि देयताओं के 3 प्रतिशत तक घटाया जाएगा।",
   "जून 2025 में उसने अपना नीतिगत रुख़ ‘तटस्थ’ से ‘समायोजनकारी’ किया।"],
  C3, 0,
  "Only statement 2 is correct. With food prices falling, consumer price inflation dropped sharply in 2025 -- in some months below the 2 per cent lower edge of the 2-6 per cent tolerance band -- and the Monetary Policy Committee cut the repo rate in steps from 6.5 per cent, including a 'jumbo' cut of 50 basis points in June that took it to 5.5 per cent, and cut it further later in the year. Statement 1 is therefore wrong. The June package also cut the CRR by a full percentage point, from 4 to 3 per cent, in four instalments between September and November, releasing liquidity to help banks pass on lower rates. "
  "Statement 3 is the reverse of what happened: the stance had been changed to 'accommodative' in April, and in June, after the front-loaded cut, the RBI moved it back to 'neutral', signalling that the room for further easing was limited and that decisions would depend on incoming data.",
  "केवल कथन 2 सही है। खाद्य क़ीमतें गिरने से 2025 में उपभोक्ता मूल्य मुद्रास्फीति तेज़ी से घटी -- कुछ महीनों में 2-6 प्रतिशत की सहनशीलता सीमा के 2 प्रतिशत के निचले छोर से भी नीचे -- और मौद्रिक नीति समिति ने रेपो दर को 6.5 प्रतिशत से चरणों में घटाया, जिसमें जून की 50 आधार अंकों की ‘बड़ी’ कटौती शामिल थी जिसने इसे 5.5 प्रतिशत किया, और वर्ष में बाद में इसे और घटाया। इसलिए कथन 1 ग़लत है। जून के पैकेज ने सीआरआर में भी पूरे एक प्रतिशत अंक की कटौती की, 4 से 3 प्रतिशत, सितंबर और नवंबर के बीच चार किस्तों में, जिससे बैंकों को कम दरें आगे पहुँचाने के लिए तरलता मिली। "
  "कथन 3 जो हुआ उसका उल्टा है: रुख़ अप्रैल में ‘समायोजनकारी’ किया गया था, और जून में, आगे से की गई कटौती के बाद, आरबीआई ने इसे वापस ‘तटस्थ’ किया, यह संकेत देते हुए कि आगे ढील की गुंजाइश सीमित है और निर्णय आने वाले आँकड़ों पर निर्भर होंगे।",
  RBI + ", Monetary Policy Statements (February, April, June and December 2025).",
  "l3-t5-eco-rbi-2025-repo-crr-stance", craft="precision")

# ---------------------------------------------------------------- Taxation & Fiscal Federalism (h-SI)
A("Taxation & Fiscal Federalism", "hard",
  "For several years after GST was introduced, a taxpayer dissatisfied with an order of the GST appellate authority had to approach a High Court in writ jurisdiction.",
  "जीएसटी लागू होने के बाद कई वर्षों तक जीएसटी अपील प्राधिकारी के आदेश से असंतुष्ट करदाता को रिट अधिकारिता में उच्च न्यायालय जाना पड़ता था।",
  "The GST Appellate Tribunal, provided for in the Central GST Act, began functioning only in 2025.",
  "केंद्रीय जीएसटी अधिनियम में उपबंधित जीएसटी अपीलीय अधिकरण ने केवल 2025 में कार्य करना शुरू किया।",
  0,
  "Both statements are correct and Statement II explains Statement I. The CGST Act, 2017 provided for a second-level appellate tribunal, but it was not constituted for years: the Madras High Court in 2019 struck down provisions on its composition that let technical members outnumber judicial ones, and Parliament recast them in 2023, with a principal bench in New Delhi and State benches across the country. With no tribunal, taxpayers could only file writ petitions, which clogged the High Courts and produced conflicting rulings. "
  "The tribunal was formally launched in 2025 and began taking appeals online. Its fiscal-federal significance lies in its structure: it applies one interpretation of the shared GST laws for the Centre and the States alike, and its principal bench decides disputes over the place of supply -- which State gets the tax -- that no single State's bench could settle.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। सीजीएसटी अधिनियम, 2017 ने दूसरे स्तर के अपीलीय अधिकरण का उपबंध किया, पर वर्षों तक इसका गठन नहीं हुआ: 2019 में मद्रास उच्च न्यायालय ने इसकी संरचना के उन उपबंधों को निरस्त किया जो तकनीकी सदस्यों को न्यायिक सदस्यों से अधिक होने देते थे, और संसद ने 2023 में उन्हें नए सिरे से बनाया, नई दिल्ली में प्रधान पीठ और देश भर में राज्य पीठों के साथ। अधिकरण न होने से करदाता केवल रिट याचिकाएँ दायर कर सकते थे, जिससे उच्च न्यायालयों पर भार बढ़ा और परस्पर विरोधी निर्णय आए। "
  "अधिकरण 2025 में औपचारिक रूप से शुरू हुआ और ऑनलाइन अपीलें लेने लगा। इसका राजकोषीय-संघीय महत्व इसकी संरचना में है: यह केंद्र और राज्यों के साझा जीएसटी क़ानूनों की एक ही व्याख्या लागू करता है, और इसकी प्रधान पीठ आपूर्ति के स्थान -- कर किस राज्य को मिले -- से जुड़े उन विवादों का निर्णय करती है जिन्हें किसी एक राज्य की पीठ नहीं सुलझा सकती।",
  "Central Goods and Services Tax Act, 2017, sections 109-112 (as amended by the Finance Act, 2023); Ministry of Finance (PIB, 2025).",
  "l3-t5-eco-gst-appellate-tribunal", craft="linkage")

write("gs_l3_t5_e.sql")
