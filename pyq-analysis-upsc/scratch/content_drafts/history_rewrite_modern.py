# -*- coding: utf-8 -*-
"""History audit rewrite, part 3: Modern India (same rules as part 1, see
history_rewrite_ancient.py). Rewritten in place, with Hindi; none of these rows is in a
published test. Also re-tags four difficulty labels the audit found wrong."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rewrite_common import S, M, C, P, write, OUT, CODE
from polity_common import C3

SPEC = "Bipan Chandra, History of Modern India (Orient BlackSwan)"
FS = "Bipan Chandra et al., India's Struggle for Independence"
THEMES3 = "NCERT Class XII, Themes in Indian History Part III"

S("10188259-abec-4802-867f-08149ba2cab6", "Modern", "medium",
  "Consider the following statements regarding the Swadeshi movement that followed the partition of Bengal:",
  "बंगाल विभाजन के बाद चले स्वदेशी आंदोलन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The boycott of British goods was formally proclaimed at a meeting in the Calcutta Town Hall on 7 August 1905.",
   "'Vande Mataram', which became the movement's rallying cry, was composed by Rabindranath Tagore.",
   "The National Council of Education, set up during the movement, promoted Western-style education under government control."],
  ["7 अगस्त 1905 को कलकत्ता टाउन हॉल की एक सभा में ब्रिटिश माल के बहिष्कार की औपचारिक घोषणा की गई।",
   "आंदोलन का नारा बना 'वंदे मातरम्' रवींद्रनाथ टैगोर ने रचा था।",
   "आंदोलन के दौरान स्थापित राष्ट्रीय शिक्षा परिषद ने सरकारी नियंत्रण में पश्चिमी ढंग की शिक्षा को बढ़ावा दिया।"],
  C3, 0,
  "Only statement 1 is correct. The Swadeshi movement was formally launched at the Calcutta Town Hall meeting of 7 August 1905, where the boycott resolution was passed, before the partition took effect on 16 October 1905. "
  "Statement 2 is incorrect: 'Vande Mataram' was written by Bankim Chandra Chattopadhyay (in the novel Anandamath); Tagore wrote 'Amar Sonar Bangla' for the movement. "
  "Statement 3 is incorrect: the National Council of Education (1906) was set up to give education on national lines, independent of government control, and led to the Bengal National College with Aurobindo Ghosh as principal.",
  "केवल कथन 1 सही है। स्वदेशी आंदोलन की औपचारिक शुरुआत 7 अगस्त 1905 को कलकत्ता टाउन हॉल की सभा में हुई, जहाँ बहिष्कार का प्रस्ताव पारित हुआ; यह 16 अक्टूबर 1905 को विभाजन लागू होने से पहले की बात है। "
  "कथन 2 गलत है: 'वंदे मातरम्' बंकिम चंद्र चट्टोपाध्याय ने (उपन्यास आनंदमठ में) लिखा; टैगोर ने आंदोलन के लिए 'आमार सोनार बांग्ला' लिखा। "
  "कथन 3 गलत है: राष्ट्रीय शिक्षा परिषद (1906) की स्थापना सरकारी नियंत्रण से स्वतंत्र, राष्ट्रीय ढंग की शिक्षा देने के लिए हुई, और इसी से बंगाल नेशनल कॉलेज बना, जिसके प्राचार्य अरविंद घोष थे।",
  f"{FS} -- chapter on the Swadeshi movement; {SPEC} -- chapter on the struggle of 1905-1918.",
  "modern-swadeshi-movement-1905")

S("50adc376-18cb-44f2-a82d-ff758c54250b", "Modern", "medium",
  "Consider the following statements regarding the Ilbert Bill controversy (1883):",
  "इल्बर्ट बिल विवाद (1883) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bill, which sought to let Indian judges try Europeans in criminal cases, was introduced during the viceroyalty of Lord Curzon.",
   "The compromise finally enacted allowed a European accused to claim trial by a jury of which at least half the members were Europeans.",
   "The organised European agitation against the Bill is regarded as one of the lessons that led Indian leaders towards an all-India political organisation."],
  ["भारतीय न्यायाधीशों को आपराधिक मामलों में यूरोपीयों की सुनवाई का अधिकार देने वाला यह बिल लॉर्ड कर्ज़न के वायसराय काल में लाया गया।",
   "अंततः पारित समझौते के अनुसार यूरोपीय अभियुक्त ऐसी जूरी द्वारा सुनवाई की माँग कर सकता था जिसके कम से कम आधे सदस्य यूरोपीय हों।",
   "बिल के विरुद्ध यूरोपीयों के संगठित आंदोलन को उन सबकों में गिना जाता है जिन्होंने भारतीय नेताओं को अखिल भारतीय राजनीतिक संगठन की ओर प्रेरित किया।"],
  C3, 1,
  "Statements 2 and 3 are correct. The Bill was introduced in 1883 under Lord Ripon, not Curzon (1899-1905), and the 'White Mutiny' of the European community forced a compromise in 1884: a European could demand a jury at least half of whose members were Europeans. "
  "Indian leaders drew the lesson that organised agitation works, which fed into the founding of the Indian National Congress in 1885.",
  "कथन 2 और 3 सही हैं। बिल 1883 में लॉर्ड रिपन के समय लाया गया था, कर्ज़न (1899-1905) के समय नहीं, और यूरोपीय समुदाय के 'श्वेत विद्रोह' ने 1884 में समझौता करवाया: यूरोपीय अभियुक्त ऐसी जूरी की माँग कर सकता था जिसके कम से कम आधे सदस्य यूरोपीय हों। "
  "भारतीय नेताओं ने यह सबक लिया कि संगठित आंदोलन कारगर होता है, और इसने 1885 में भारतीय राष्ट्रीय कांग्रेस की स्थापना में योगदान दिया।",
  f"{SPEC} -- chapter on the rise of the national movement; {FS} -- chapter on the foundation of the Congress.",
  "modern-ilbert-bill-1883")

S("c786c04e-3f63-4ca2-a510-590b8db74ac1", "Modern", "medium",
  "Consider the following statements regarding Direct Action Day (16 August 1946):",
  "प्रत्यक्ष कार्रवाई दिवस (16 अगस्त 1946) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was called by the Muslim League to press its demand for Pakistan.",
   "It led to large-scale communal violence, the worst of it in Bombay.",
   "It was called after the Muslim League withdrew its earlier acceptance of the Cabinet Mission Plan."],
  ["इसका आह्वान मुस्लिम लीग ने पाकिस्तान की अपनी माँग पर ज़ोर देने के लिए किया था।",
   "इससे बड़े पैमाने पर सांप्रदायिक हिंसा हुई, जिसका सबसे बुरा रूप बंबई में दिखा।",
   "इसका आह्वान मुस्लिम लीग द्वारा कैबिनेट मिशन योजना की अपनी पहले की स्वीकृति वापस लेने के बाद किया गया।"],
  C3, 1,
  "Statements 1 and 3 are correct. The League had accepted the Cabinet Mission Plan in June 1946, but withdrew its acceptance on 29 July, after Nehru's statement that the Congress would be free to change the plan in the Constituent Assembly, and called for 'direct action' to achieve Pakistan. "
  "Statement 2 is incorrect: the worst violence was in Calcutta (the 'Great Calcutta Killings'), where thousands died in a few days, followed by Noakhali and Bihar.",
  "कथन 1 और 3 सही हैं। लीग ने जून 1946 में कैबिनेट मिशन योजना स्वीकार की थी, पर नेहरू के इस बयान के बाद कि कांग्रेस संविधान सभा में योजना बदलने के लिए स्वतंत्र होगी, उसने 29 जुलाई को स्वीकृति वापस ले ली और पाकिस्तान पाने के लिए 'प्रत्यक्ष कार्रवाई' का आह्वान किया। "
  "कथन 2 गलत है: सबसे भयानक हिंसा कलकत्ता में हुई ('ग्रेट कलकत्ता किलिंग्स'), जहाँ कुछ ही दिनों में हज़ारों लोग मारे गए; इसके बाद नोआखाली और बिहार में हिंसा हुई।",
  f"{FS} -- chapter on the freedom and partition; {THEMES3} -- 'Understanding Partition'.",
  "modern-direct-action-day-1946")

S("fe9c4cf8-c1c2-4810-b6ad-ec19779da805", "Modern", "medium",
  "Consider the following statements regarding the Communal Award (1932):",
  "सांप्रदायिक पंचाट (1932) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was announced by the British Prime Minister, Ramsay MacDonald.",
   "It extended separate electorates to the Depressed Classes, in addition to the communities that already had them.",
   "Gandhi began a fast unto death in Yerawada jail against separate electorates for the Depressed Classes."],
  ["इसकी घोषणा ब्रिटिश प्रधानमंत्री रैम्से मैकडोनाल्ड ने की थी।",
   "इसने पृथक निर्वाचन मंडल उन समुदायों के अलावा, जिन्हें यह पहले से मिला था, दलित वर्गों (Depressed Classes) तक भी बढ़ा दिया।",
   "गांधीजी ने दलित वर्गों के लिए पृथक निर्वाचन के विरोध में यरवदा जेल में आमरण अनशन शुरू किया।"],
  C3, 2,
  "All three statements are correct. Ramsay MacDonald announced the Award in August 1932 after the Second Round Table Conference failed to agree on minority representation. "
  "It extended separate electorates to the Depressed Classes. Gandhi, then in Yerawada jail, began a fast unto death on 20 September 1932, which ended with the Poona Pact: separate electorates were replaced by reserved seats within joint electorates. "
  "A solver who remembers only Gandhi's opposition may wrongly assume the Award was announced by the Viceroy.",
  "तीनों कथन सही हैं। दूसरे गोलमेज़ सम्मेलन के अल्पसंख्यक प्रतिनिधित्व पर सहमति न बना पाने के बाद रैम्से मैकडोनाल्ड ने अगस्त 1932 में यह पंचाट घोषित किया। "
  "इसने दलित वर्गों को पृथक निर्वाचन दिया। उस समय यरवदा जेल में बंद गांधीजी ने 20 सितंबर 1932 को आमरण अनशन शुरू किया, जिसका अंत पूना समझौते से हुआ: पृथक निर्वाचन की जगह संयुक्त निर्वाचन के भीतर आरक्षित सीटें आईं। "
  "जो विद्यार्थी केवल गांधीजी का विरोध याद रखता है, वह भूल से मान सकता है कि पंचाट वायसराय ने घोषित किया था।",
  f"{FS} -- chapter on the Civil Disobedience movement; {SPEC} -- chapter on the struggle of 1927-1947.",
  "modern-communal-award-1932")

S("9ce15a08-1206-421a-9011-65ad41ae13b0", "Modern", "medium",
  "Consider the following statements regarding the Cabinet Mission (1946):",
  "कैबिनेट मिशन (1946) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It proposed a Union with limited powers at the Centre and the grouping of provinces into sections.",
   "It accepted the demand for a separate, sovereign Pakistan.",
   "It was led by Stafford Cripps, who was then the Secretary of State for India."],
  ["इसने केंद्र में सीमित शक्तियों वाले संघ और प्रांतों को समूहों (सेक्शन) में बाँटने का प्रस्ताव रखा।",
   "इसने अलग, संप्रभु पाकिस्तान की माँग स्वीकार कर ली।",
   "इसका नेतृत्व स्टैफ़र्ड क्रिप्स ने किया, जो उस समय भारत के विदेश मंत्री (Secretary of State for India) थे।"],
  C3, 0,
  "Only statement 1 is correct. The plan of 16 May 1946 gave the Union only defence, foreign affairs and communications, and grouped the provinces into sections A, B and C. "
  "Statement 2 is incorrect: the Mission rejected a sovereign Pakistan as unworkable. "
  "Statement 3 is incorrect: the Mission was led by Lord Pethick-Lawrence, the Secretary of State for India; its other members were Stafford Cripps (President of the Board of Trade) and A.V. Alexander. Cripps is tempting because he led the earlier mission of 1942.",
  "केवल कथन 1 सही है। 16 मई 1946 की योजना ने संघ को केवल रक्षा, विदेश मामले और संचार दिए, और प्रांतों को A, B और C सेक्शनों में बाँटा। "
  "कथन 2 गलत है: मिशन ने संप्रभु पाकिस्तान को अव्यावहारिक मानकर अस्वीकार किया। "
  "कथन 3 गलत है: मिशन का नेतृत्व भारत के विदेश मंत्री लॉर्ड पेथिक-लॉरेंस ने किया; इसके अन्य सदस्य स्टैफ़र्ड क्रिप्स (बोर्ड ऑफ़ ट्रेड के अध्यक्ष) और ए.वी. अलेक्ज़ेंडर थे। क्रिप्स का नाम इसलिए आकर्षक लगता है क्योंकि उन्होंने 1942 के पहले वाले मिशन का नेतृत्व किया था।",
  f"{FS} -- chapter on the post-war upsurge and the Cabinet Mission; {SPEC} -- chapter on the struggle of 1927-1947.",
  "modern-cabinet-mission-1946")

S("bace8f90-c902-4062-a9fc-9edc2af60e26", "Modern", "medium",
  "Consider the following statements regarding the August Offer (1940):",
  "अगस्त प्रस्ताव (1940) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was made by the Viceroy, Lord Linlithgow.",
   "It named Dominion Status as the objective and offered to expand the Viceroy's Executive Council with more Indians.",
   "It assured the minorities that no future constitution would be adopted without their consent."],
  ["यह वायसराय लॉर्ड लिनलिथगो ने दिया था।",
   "इसमें डोमिनियन स्टेटस को लक्ष्य बताया गया और वायसराय की कार्यकारी परिषद में अधिक भारतीयों को शामिल करने का प्रस्ताव रखा गया।",
   "इसने अल्पसंख्यकों को आश्वासन दिया कि उनकी सहमति के बिना कोई भावी संविधान नहीं अपनाया जाएगा।"],
  C3, 2,
  "All three statements are correct. Linlithgow made the offer on 8 August 1940 to win Indian support in the war: Dominion Status as the objective, an expanded Executive Council, a war advisory council, and a body to frame a constitution after the war. "
  "Its assurance that no constitution would be adopted without the consent of the minorities was read as a veto for the Muslim League. The Congress rejected the offer and launched the Individual Satyagraha. "
  "The Viceroy is the most common trap here (Wavell came in 1943).",
  "तीनों कथन सही हैं। युद्ध में भारतीय समर्थन पाने के लिए लिनलिथगो ने 8 अगस्त 1940 को यह प्रस्ताव दिया: लक्ष्य के रूप में डोमिनियन स्टेटस, विस्तारित कार्यकारी परिषद, एक युद्ध सलाहकार परिषद, और युद्ध के बाद संविधान बनाने के लिए एक निकाय। "
  "अल्पसंख्यकों की सहमति के बिना संविधान न अपनाने के आश्वासन को मुस्लिम लीग के लिए वीटो माना गया। कांग्रेस ने प्रस्ताव अस्वीकार कर व्यक्तिगत सत्याग्रह शुरू किया। "
  "यहाँ सबसे आम जाल वायसराय का नाम है (वेवेल 1943 में आए)।",
  f"{FS} -- chapter on the struggle during the Second World War; {SPEC} -- chapter on the struggle of 1927-1947.",
  "modern-august-offer-1940")

S("9aef3cbf-dbf1-414d-8654-2cceff9a14c3", "Modern", "medium",
  "Consider the following statements regarding the Rowlatt Act (1919):",
  "रौलट एक्ट (1919) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It allowed the government to imprison persons without trial for up to two years.",
   "It was based on the recommendations of a committee headed by Sir John Simon.",
   "Muhammad Ali Jinnah supported the Bill in the Imperial Legislative Council."],
  ["इसने सरकार को लोगों को बिना मुकदमे के दो वर्ष तक जेल में रखने का अधिकार दिया।",
   "यह सर जॉन साइमन की अध्यक्षता वाली समिति की सिफ़ारिशों पर आधारित था।",
   "मुहम्मद अली जिन्ना ने इंपीरियल लेजिस्लेटिव काउंसिल में इस बिल का समर्थन किया।"],
  C3, 0,
  "Only statement 1 is correct. The Anarchical and Revolutionary Crimes Act, 1919 allowed detention without trial for up to two years and trial by special courts without appeal. "
  "Statement 2 is incorrect: it followed the report of the Sedition Committee headed by Justice Sidney Rowlatt; Sir John Simon headed the 1927 statutory commission. "
  "Statement 3 is incorrect: every elected Indian member opposed the Bill, and Jinnah, Madan Mohan Malaviya and Mazharul Haque resigned from the Council in protest. The Act triggered Gandhi's first all-India satyagraha in April 1919.",
  "केवल कथन 1 सही है। अराजक और क्रांतिकारी अपराध अधिनियम, 1919 ने बिना मुकदमे के दो वर्ष तक हिरासत और बिना अपील के विशेष अदालतों में सुनवाई की अनुमति दी। "
  "कथन 2 गलत है: यह न्यायमूर्ति सिडनी रौलट की अध्यक्षता वाली राजद्रोह समिति की रिपोर्ट पर आधारित था; सर जॉन साइमन 1927 के वैधानिक आयोग के अध्यक्ष थे। "
  "कथन 3 गलत है: हर निर्वाचित भारतीय सदस्य ने बिल का विरोध किया, और जिन्ना, मदन मोहन मालवीय तथा मज़हरुल हक ने विरोध में काउंसिल से इस्तीफ़ा दे दिया। इसी अधिनियम ने अप्रैल 1919 में गांधीजी के पहले अखिल भारतीय सत्याग्रह को जन्म दिया।",
  f"{FS} -- chapter on the Rowlatt satyagraha; {SPEC} -- chapter on the struggle of 1918-1922.",
  "modern-rowlatt-act-1919")

S("172710c4-97fb-412d-9fd5-3b0c34590e62", "Modern", "medium",
  "Consider the following statements regarding the Lucknow Pact (1916):",
  "लखनऊ समझौते (1916) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was an agreement between the Indian National Congress and the All India Muslim League.",
   "Under it, the Congress rejected separate electorates and the League agreed to joint electorates.",
   "The Lucknow session of 1916 also saw the Moderates and the Extremists reunite in the Congress."],
  ["यह भारतीय राष्ट्रीय कांग्रेस और अखिल भारतीय मुस्लिम लीग के बीच एक समझौता था।",
   "इसके तहत कांग्रेस ने पृथक निर्वाचन अस्वीकार कर दिया और लीग संयुक्त निर्वाचन पर सहमत हो गई।",
   "1916 के लखनऊ अधिवेशन में नरमपंथी और गरमपंथी कांग्रेस में फिर से एक हो गए।"],
  C3, 1,
  "Statements 1 and 3 are correct. At Lucknow in December 1916 the Congress and the League, meeting at the same time, agreed on a joint scheme of reforms; the same session readmitted Tilak and the Extremists, who had been out since Surat (1907). "
  "Statement 2 reverses the bargain: the Congress accepted separate electorates for Muslims, with weightage in the provinces where they were a minority, which critics later saw as legitimising communal representation.",
  "कथन 1 और 3 सही हैं। दिसंबर 1916 में लखनऊ में एक साथ अधिवेशन कर रहीं कांग्रेस और लीग सुधारों की एक संयुक्त योजना पर सहमत हुईं; इसी अधिवेशन में तिलक और गरमपंथियों को फिर शामिल किया गया, जो सूरत (1907) से बाहर थे। "
  "कथन 2 सौदे को उलट देता है: कांग्रेस ने मुसलमानों के लिए पृथक निर्वाचन स्वीकार किया, और जिन प्रांतों में वे अल्पसंख्यक थे वहाँ उन्हें अधिक प्रतिनिधित्व (weightage) दिया; आलोचकों ने बाद में इसे सांप्रदायिक प्रतिनिधित्व को वैधता देना माना।",
  f"{FS} -- chapter on the Home Rule movement and the Lucknow Pact; {SPEC} -- chapter on the struggle of 1905-1918.",
  "modern-lucknow-pact-1916")

S("c5aa97b7-b9cb-47e8-beea-c62c517a8a72", "Modern", "medium",
  "Consider the following statements regarding the Quit India movement (1942):",
  "भारत छोड़ो आंदोलन (1942) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was launched after the failure of the Cripps Mission.",
   "Gandhi gave the call 'Do or Die' at the Lahore session of the Congress.",
   "The Quit India resolution was first passed at the Congress Working Committee's Wardha meeting, and the movement began the same month, in July 1942."],
  ["यह क्रिप्स मिशन की विफलता के बाद शुरू किया गया।",
   "गांधीजी ने 'करो या मरो' का नारा कांग्रेस के लाहौर अधिवेशन में दिया।",
   "भारत छोड़ो प्रस्ताव पहले कांग्रेस कार्यसमिति की वर्धा बैठक में पारित हुआ, और आंदोलन उसी महीने, जुलाई 1942 में शुरू हो गया।"],
  C3, 0,
  "Only statement 1 is correct. The Cripps Mission (March-April 1942) failed, and the Japanese advance to Burma added urgency. "
  "Statement 2 is incorrect: 'Do or Die' was given in Gandhi's speech at the Gowalia Tank maidan in Bombay on 8 August 1942, when the AICC ratified the resolution. "
  "Statement 3 is incorrect: the Working Committee adopted the resolution at Wardha on 14 July 1942, but the movement began only after the AICC's Bombay session of 8 August and the arrest of the leaders on 9 August -- hence 'August Kranti'.",
  "केवल कथन 1 सही है। क्रिप्स मिशन (मार्च-अप्रैल 1942) विफल रहा, और बर्मा तक जापान के बढ़ने से स्थिति और गंभीर हो गई। "
  "कथन 2 गलत है: 'करो या मरो' का नारा गांधीजी ने 8 अगस्त 1942 को बंबई के गोवालिया टैंक मैदान में दिए भाषण में दिया, जब अखिल भारतीय कांग्रेस समिति (AICC) ने प्रस्ताव की पुष्टि की। "
  "कथन 3 गलत है: कार्यसमिति ने 14 जुलाई 1942 को वर्धा में प्रस्ताव स्वीकार किया, पर आंदोलन 8 अगस्त के AICC के बंबई अधिवेशन और 9 अगस्त को नेताओं की गिरफ़्तारी के बाद ही शुरू हुआ, इसीलिए इसे 'अगस्त क्रांति' कहते हैं।",
  f"{FS} -- chapter on the Quit India movement; {THEMES3} -- 'Mahatma Gandhi and the Nationalist Movement'.",
  "modern-quit-india-1942")

S("9e19ca0c-fe87-4688-a084-a3c193a61f8b", "Modern", "medium",
  "Consider the following statements regarding the Doctrine of Lapse:",
  "व्यपगत के सिद्धांत (Doctrine of Lapse) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the doctrine applied by Lord Dalhousie, a dependent state whose ruler died without a natural heir passed to the Company.",
   "Satara, Jhansi and Nagpur were among the states annexed under it.",
   "Awadh was annexed under the Doctrine of Lapse in 1856."],
  ["लॉर्ड डलहौज़ी द्वारा लागू इस सिद्धांत के अनुसार, जिस आश्रित राज्य का शासक बिना प्राकृतिक उत्तराधिकारी के मर जाता, वह कंपनी के अधीन आ जाता।",
   "सतारा, झाँसी और नागपुर उन राज्यों में थे जिनका इसके तहत विलय किया गया।",
   "अवध का विलय 1856 में व्यपगत के सिद्धांत के तहत किया गया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under the doctrine, a ruler without a natural heir could not adopt one to succeed him without the Company's consent. Satara (1848), Jaitpur and Sambalpur (1849), Udaipur (1852), Jhansi (1853) and Nagpur (1854) were annexed this way. "
  "Statement 3 is incorrect: Awadh had rulers and heirs; it was annexed in 1856 on the ground of misgovernment, and Wajid Ali Shah was deposed. The distinction explains why Awadh's taluqdars and sepoys were so prominent in 1857.",
  "कथन 1 और 2 सही हैं। इस सिद्धांत के अनुसार, बिना प्राकृतिक उत्तराधिकारी वाला शासक कंपनी की सहमति के बिना दत्तक उत्तराधिकारी नहीं बना सकता था। सतारा (1848), जैतपुर और संबलपुर (1849), उदयपुर (1852), झाँसी (1853) और नागपुर (1854) का विलय इसी तरह हुआ। "
  "कथन 3 गलत है: अवध के शासक और उत्तराधिकारी मौजूद थे; उसका विलय 1856 में कुशासन के आधार पर हुआ, और वाजिद अली शाह को हटाया गया। यही अंतर बताता है कि 1857 में अवध के तालुकदार और सिपाही इतने आगे क्यों थे।",
  f"{SPEC} -- chapter on the expansion and consolidation of British power; {THEMES3} -- 'Rebels and the Raj'.",
  "modern-doctrine-of-lapse")

S("f8dc62d0-2148-4f64-9d41-e9e362b1e634", "Modern", "medium",
  "Consider the following statements regarding the founding of the Indian National Congress (1885):",
  "भारतीय राष्ट्रीय कांग्रेस की स्थापना (1885) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A.O. Hume, a retired British civil servant, took a leading part in founding it.",
   "Its first session was held in Bombay, with Womesh Chandra Bonnerjee as president.",
   "The first session was originally planned for Poona but was moved to Bombay because of an outbreak of cholera."],
  ["सेवानिवृत्त ब्रिटिश अधिकारी ए.ओ. ह्यूम ने इसकी स्थापना में प्रमुख भूमिका निभाई।",
   "इसका पहला अधिवेशन बंबई में हुआ, जिसके अध्यक्ष व्योमेश चंद्र बनर्जी थे।",
   "पहला अधिवेशन पहले पूना में होना था, पर वहाँ हैज़ा फैलने के कारण इसे बंबई ले जाया गया।"],
  C3, 2,
  "All three statements are correct. Hume worked with Indian leaders to bring together the regional associations; the first session met at the Gokuldas Tejpal Sanskrit College, Bombay, on 28 December 1885, with 72 delegates and W.C. Bonnerjee in the chair. "
  "It had been planned for Poona, where the Sarvajanik Sabha was to host it, but was shifted because of cholera there. "
  "(The 'safety valve' view of Hume's motives is contested by historians such as Bipan Chandra.)",
  "तीनों कथन सही हैं। ह्यूम ने क्षेत्रीय संगठनों को एक साथ लाने में भारतीय नेताओं के साथ काम किया; पहला अधिवेशन 28 दिसंबर 1885 को बंबई के गोकुलदास तेजपाल संस्कृत कॉलेज में हुआ, जिसमें 72 प्रतिनिधि थे और अध्यक्षता डब्ल्यू.सी. बनर्जी ने की। "
  "यह पूना में होना था, जहाँ सार्वजनिक सभा इसकी मेज़बानी करती, पर वहाँ हैज़ा फैलने के कारण इसे स्थानांतरित किया गया। "
  "(ह्यूम के उद्देश्यों के बारे में 'सेफ़्टी वाल्व' के मत को बिपन चंद्र जैसे इतिहासकार चुनौती देते हैं।)",
  f"{FS} -- chapter on the foundation of the Indian National Congress.",
  "modern-inc-founding-1885")

S("a8dee269-c994-4491-9062-9c3495d50780", "Modern", "medium",
  "Consider the following statements regarding the Revolt of 1857:",
  "1857 के विद्रोह के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The sepoys at Meerut rose on 10 May 1857 and marched to Delhi.",
   "At Kanpur the revolt was led by Nana Saheb, the adopted son of the last Peshwa, Baji Rao II.",
   "In Bihar, the revolt was led by Kunwar Singh, a zamindar of Jagdishpur."],
  ["मेरठ के सिपाहियों ने 10 मई 1857 को विद्रोह किया और दिल्ली की ओर कूच किया।",
   "कानपुर में विद्रोह का नेतृत्व अंतिम पेशवा बाजीराव द्वितीय के दत्तक पुत्र नाना साहब ने किया।",
   "बिहार में विद्रोह का नेतृत्व जगदीशपुर के ज़मींदार कुँवर सिंह ने किया।"],
  C3, 2,
  "All three statements are correct. After the court-martial of 85 sepoys who refused the new cartridges, the Meerut troops rose on 10 May and reached Delhi on 11 May, proclaiming Bahadur Shah Zafar emperor. "
  "Nana Saheb, denied Baji Rao II's pension, led the rising at Kanpur, with Tantia Tope. Kunwar Singh, an elderly zamindar of Jagdishpur near Arrah, led the revolt in Bihar. "
  "Leaders and centres are the standard traps in 1857 questions: Begum Hazrat Mahal led at Lucknow, and Rani Lakshmibai at Jhansi.",
  "तीनों कथन सही हैं। नए कारतूस लेने से इनकार करने वाले 85 सिपाहियों के कोर्ट-मार्शल के बाद मेरठ की सेना ने 10 मई को विद्रोह किया और 11 मई को दिल्ली पहुँचकर बहादुर शाह ज़फ़र को बादशाह घोषित किया। "
  "बाजीराव द्वितीय की पेंशन से वंचित नाना साहब ने तात्या टोपे के साथ कानपुर में विद्रोह का नेतृत्व किया। आरा के पास जगदीशपुर के बुज़ुर्ग ज़मींदार कुँवर सिंह ने बिहार में विद्रोह की अगुवाई की। "
  "1857 के प्रश्नों में नेता और केंद्र ही मानक जाल होते हैं: लखनऊ में बेगम हज़रत महल और झाँसी में रानी लक्ष्मीबाई ने नेतृत्व किया।",
  f"{THEMES3} -- 'Rebels and the Raj: The Revolt of 1857 and its Representations'; {SPEC} -- chapter on the Revolt of 1857.",
  "modern-revolt-of-1857")

S("9e1d875a-82ad-4561-9724-64d8870e14d6", "Modern", "medium",
  "Consider the following statements regarding the Jallianwala Bagh massacre (13 April 1919):",
  "जलियाँवाला बाग हत्याकांड (13 अप्रैल 1919) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The crowd had gathered in the Bagh at Amritsar on the day of Baisakhi.",
   "The Hunter Committee, which inquired into it, held General Dyer guilty and recommended his prosecution.",
   "Michael O'Dwyer, who gave the order to fire on the crowd, was later assassinated in London by Udham Singh."],
  ["भीड़ बैसाखी के दिन अमृतसर के बाग में इकट्ठा हुई थी।",
   "इसकी जाँच करने वाली हंटर समिति ने जनरल डायर को दोषी ठहराया और उस पर मुकदमा चलाने की सिफ़ारिश की।",
   "भीड़ पर गोली चलाने का आदेश देने वाले माइकल ओ'डायर की बाद में लंदन में ऊधम सिंह ने हत्या कर दी।"],
  C3, 0,
  "Only statement 1 is correct: a crowd, many of them villagers in Amritsar for the Baisakhi fair, had gathered to protest against the arrest of Dr Satyapal and Dr Saifuddin Kitchlew. "
  "Statement 2 is incorrect: the Hunter Committee censured Dyer's conduct, and he was relieved of his command, but no penal action was taken; the Congress set up its own inquiry. "
  "Statement 3 is incorrect: the firing was ordered by Brigadier-General Reginald Dyer. Michael O'Dwyer was the Lieutenant-Governor of Punjab who endorsed it; Udham Singh shot O'Dwyer in London in 1940.",
  "केवल कथन 1 सही है: डॉ. सत्यपाल और डॉ. सैफ़ुद्दीन किचलू की गिरफ़्तारी के विरोध में भीड़ इकट्ठा हुई थी, जिनमें बहुत-से गाँव वाले बैसाखी मेले के लिए अमृतसर आए थे। "
  "कथन 2 गलत है: हंटर समिति ने डायर के आचरण की निंदा की और उसे कमान से हटाया गया, पर कोई दंडात्मक कार्रवाई नहीं हुई; कांग्रेस ने अपनी अलग जाँच समिति बनाई। "
  "कथन 3 गलत है: गोली चलाने का आदेश ब्रिगेडियर-जनरल रेजिनाल्ड डायर ने दिया था। माइकल ओ'डायर पंजाब का लेफ़्टिनेंट-गवर्नर था जिसने इसका समर्थन किया; ऊधम सिंह ने 1940 में लंदन में ओ'डायर को गोली मारी।",
  f"{FS} -- chapter on the Rowlatt satyagraha and Jallianwala Bagh; {SPEC} -- chapter on the struggle of 1918-1922.",
  "modern-jallianwala-bagh-1919")

S("a34b1ef3-3827-451b-9a9f-831113b64a79", "Modern", "medium",
  "Consider the following statements regarding the Arya Samaj:",
  "आर्य समाज के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was founded by Swami Dayanand Saraswati in 1875.",
   "Its first unit was set up at Lahore.",
   "Dayanand's principal work, the Satyarth Prakash, was written in Sanskrit."],
  ["इसकी स्थापना स्वामी दयानंद सरस्वती ने 1875 में की।",
   "इसकी पहली इकाई लाहौर में स्थापित हुई।",
   "दयानंद का प्रमुख ग्रंथ सत्यार्थ प्रकाश संस्कृत में लिखा गया।"],
  C3, 0,
  "Only statement 1 is correct. The Arya Samaj was founded in 1875 at Bombay; the Lahore Arya Samaj followed in 1877, and Punjab became its main base (the DAV movement). "
  "Statement 3 is incorrect: the Satyarth Prakash (1875) was written in Hindi, so that it could reach ordinary people -- itself a mark of the Samaj's reforming method, alongside the call 'Back to the Vedas' and its rejection of idol worship.",
  "केवल कथन 1 सही है। आर्य समाज की स्थापना 1875 में बंबई में हुई; लाहौर आर्य समाज 1877 में बना, और पंजाब इसका मुख्य आधार बना (डीएवी आंदोलन)। "
  "कथन 3 गलत है: सत्यार्थ प्रकाश (1875) हिंदी में लिखा गया ताकि यह आम लोगों तक पहुँच सके; 'वेदों की ओर लौटो' के आह्वान और मूर्ति-पूजा के खंडन के साथ यह भी समाज के सुधार के तरीके की पहचान थी।",
  f"{SPEC} -- chapter on social and cultural awakening; NCERT Class VIII, Our Pasts III -- 'Women, Caste and Reform'.",
  "modern-arya-samaj-1875")

S("6f624f64-a2fe-4b7c-9cf6-38f49b69c893", "Modern", "hard",
  "Consider the following statements regarding the Second Round Table Conference (1931):",
  "दूसरे गोलमेज़ सम्मेलन (1931) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["B.R. Ambedkar attended it.",
   "It reached agreement on the representation of the minorities, resolving most of the outstanding disputes.",
   "Gandhi was the sole representative of the Indian National Congress at the Conference."],
  ["बी.आर. आंबेडकर इसमें शामिल हुए।",
   "इसमें अल्पसंख्यकों के प्रतिनिधित्व पर सहमति बन गई और अधिकांश विवाद सुलझ गए।",
   "सम्मेलन में गांधीजी भारतीय राष्ट्रीय कांग्रेस के एकमात्र प्रतिनिधि थे।"],
  C3, 1,
  "Statements 1 and 3 are correct. Under the Gandhi-Irwin Pact the Congress took part, and Gandhi went to London as its sole representative (Sarojini Naidu also attended the conference); Ambedkar attended all three conferences, speaking for the Depressed Classes. "
  "Statement 2 is incorrect: the conference deadlocked on minority representation, and Gandhi returned empty-handed in December 1931. MacDonald's Communal Award followed in August 1932.",
  "कथन 1 और 3 सही हैं। गांधी-इरविन समझौते के तहत कांग्रेस ने भाग लिया और गांधीजी उसके एकमात्र प्रतिनिधि के रूप में लंदन गए (सरोजिनी नायडू भी सम्मेलन में शामिल हुईं); आंबेडकर तीनों सम्मेलनों में दलित वर्गों की ओर से शामिल हुए। "
  "कथन 2 गलत है: सम्मेलन अल्पसंख्यक प्रतिनिधित्व पर गतिरोध में फँस गया, और गांधीजी दिसंबर 1931 में खाली हाथ लौटे। अगस्त 1932 में मैकडोनाल्ड का सांप्रदायिक पंचाट आया।",
  f"{FS} -- chapter on the Civil Disobedience movement; {SPEC} -- chapter on the struggle of 1927-1947.",
  "modern-second-round-table-conference-1931")

S("e1bc7862-963f-4118-8e0d-99e004d2c0d6", "Modern", "hard",
  "Consider the following statements regarding the Gandhi-Irwin Pact (March 1931):",
  "गांधी-इरविन समझौते (मार्च 1931) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Congress agreed to suspend the Civil Disobedience movement and to boycott the Second Round Table Conference.",
   "The government agreed to hold a public inquiry into police excesses during the movement.",
   "People living near the coast were allowed to make salt for their own use without paying duty."],
  ["कांग्रेस सविनय अवज्ञा आंदोलन स्थगित करने और दूसरे गोलमेज़ सम्मेलन का बहिष्कार करने पर सहमत हुई।",
   "सरकार आंदोलन के दौरान पुलिस की ज़्यादतियों की सार्वजनिक जाँच कराने पर सहमत हुई।",
   "तट के पास रहने वाले लोगों को बिना कर दिए अपने उपयोग के लिए नमक बनाने की अनुमति दी गई।"],
  C3, 0,
  "Only statement 3 is correct: people in coastal villages could collect or make salt for domestic use. The government also agreed to release non-violent political prisoners and to return confiscated property not yet sold. "
  "Statement 1 is incorrect: the Congress agreed to suspend civil disobedience and to take part in the Second Round Table Conference. "
  "Statement 2 is incorrect: Gandhi's demand for an inquiry into police excesses was rejected, as was the plea to commute the death sentences of Bhagat Singh and his comrades.",
  "केवल कथन 3 सही है: तटीय गाँवों के लोग घरेलू उपयोग के लिए नमक इकट्ठा कर सकते थे या बना सकते थे। सरकार अहिंसक राजनीतिक बंदियों को छोड़ने और ज़ब्त संपत्ति, जो बेची न गई हो, लौटाने पर भी सहमत हुई। "
  "कथन 1 गलत है: कांग्रेस सविनय अवज्ञा स्थगित करने और दूसरे गोलमेज़ सम्मेलन में भाग लेने पर सहमत हुई थी। "
  "कथन 2 गलत है: पुलिस ज़्यादतियों की जाँच की गांधीजी की माँग ठुकरा दी गई, और भगत सिंह तथा उनके साथियों की फाँसी की सज़ा घटाने की अपील भी।",
  f"{FS} -- chapter on the Civil Disobedience movement; {SPEC} -- chapter on the struggle of 1927-1947.",
  "modern-gandhi-irwin-pact-1931")

S("66e55285-d15f-4682-be2f-8a415c5d2f8a", "Modern", "hard",
  "Consider the following statements regarding the Cripps Mission (1942):",
  "क्रिप्स मिशन (1942) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It offered India Dominion Status with immediate effect, including full Indian control of defence.",
   "Its proposals were accepted by the Congress and rejected only by the Muslim League.",
   "It was sent by the Labour government of Clement Attlee."],
  ["इसने भारत को तत्काल प्रभाव से डोमिनियन स्टेटस देने का प्रस्ताव रखा, जिसमें रक्षा पर पूरा भारतीय नियंत्रण शामिल था।",
   "इसके प्रस्ताव कांग्रेस ने स्वीकार कर लिए और केवल मुस्लिम लीग ने अस्वीकार किए।",
   "इसे क्लीमेंट एटली की लेबर सरकार ने भेजा था।"],
  C3, 3,
  "None of the statements is correct. Cripps offered Dominion Status only after the war, with a constitution-making body and the right of any province to stay out; defence was to remain under British control during the war. "
  "Both the Congress and the Muslim League rejected the proposals -- the Congress over the delayed transfer of power, defence and the provincial option, the League because Pakistan was not conceded outright. "
  "The Mission was sent in March 1942 by Churchill's wartime coalition government (Cripps was a Labour member of it); Attlee's Labour government, elected in 1945, sent the Cabinet Mission of 1946.",
  "कोई भी कथन सही नहीं है। क्रिप्स ने डोमिनियन स्टेटस केवल युद्ध के बाद देने की बात कही, साथ में संविधान बनाने वाला निकाय और किसी भी प्रांत को अलग रहने का अधिकार; युद्ध के दौरान रक्षा ब्रिटिश नियंत्रण में रहनी थी। "
  "कांग्रेस और मुस्लिम लीग, दोनों ने प्रस्ताव अस्वीकार किए: कांग्रेस ने सत्ता हस्तांतरण में देरी, रक्षा और प्रांतीय विकल्प के कारण, और लीग ने इसलिए कि पाकिस्तान सीधे स्वीकार नहीं किया गया। "
  "मिशन मार्च 1942 में चर्चिल की युद्धकालीन गठबंधन सरकार ने भेजा था (क्रिप्स उसमें लेबर पार्टी के सदस्य थे); 1945 में चुनी गई एटली की लेबर सरकार ने 1946 का कैबिनेट मिशन भेजा।",
  f"{FS} -- chapter on the Cripps Mission and the Quit India movement; {SPEC} -- chapter on the struggle of 1927-1947.",
  "modern-cripps-mission-1942")

S("ff930b92-b153-4656-834a-bf00f3c2f6c3", "Modern", "hard",
  "With reference to the Indian Independence Act, 1947, consider the following statements:",
  "भारतीय स्वतंत्रता अधिनियम, 1947 के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It provided for a Governor-General for each of the two new dominions, to be appointed by the British Crown.",
   "It empowered the Constituent Assembly of each dominion to function also as its legislature.",
   "It abolished the office of the Secretary of State for India."],
  ["इसमें दोनों नए डोमिनियनों में से प्रत्येक के लिए एक गवर्नर-जनरल का प्रावधान था, जिसकी नियुक्ति ब्रिटिश सम्राट को करनी थी।",
   "इसने प्रत्येक डोमिनियन की संविधान सभा को उसके विधानमंडल के रूप में भी काम करने का अधिकार दिया।",
   "इसने भारत के विदेश मंत्री (Secretary of State for India) का पद समाप्त कर दिया।"],
  C3, 2,
  "All three statements are correct. The Act created the dominions of India and Pakistan from 15 August 1947, each with a Governor-General appointed by the Crown (Mountbatten for India, Jinnah for Pakistan). "
  "Until a new constitution was framed, each Constituent Assembly was to act also as the dominion legislature, and the Government of India Act, 1935 governed each dominion with modifications. "
  "The office of Secretary of State for India was abolished, and British paramountcy over the princely states lapsed.",
  "तीनों कथन सही हैं। अधिनियम ने 15 अगस्त 1947 से भारत और पाकिस्तान के डोमिनियन बनाए, जिनमें से प्रत्येक का गवर्नर-जनरल सम्राट द्वारा नियुक्त होना था (भारत के लिए माउंटबेटन, पाकिस्तान के लिए जिन्ना)। "
  "नया संविधान बनने तक प्रत्येक संविधान सभा को डोमिनियन के विधानमंडल के रूप में भी काम करना था, और भारत शासन अधिनियम, 1935 संशोधनों के साथ हर डोमिनियन पर लागू रहा। "
  "भारत के विदेश मंत्री का पद समाप्त कर दिया गया, और रियासतों पर ब्रिटिश सर्वोच्चता (paramountcy) समाप्त हो गई।",
  "Indian Independence Act, 1947 (10 & 11 Geo. 6, c. 30); M. Laxmikanth, Indian Polity -- historical background.",
  "modern-indian-independence-act-1947")

M("6b3a414c-4536-41a9-9776-e09ad4911faf", "Modern", "hard",
  "At its Calcutta session (1906), the Congress passed four resolutions that the Extremists feared the Moderates would dilute, leading to the split at Surat in 1907. Which one of the following was NOT one of them?",
  "कलकत्ता अधिवेशन (1906) में कांग्रेस ने चार प्रस्ताव पारित किए, जिनके बारे में गरमपंथियों को डर था कि नरमपंथी उन्हें कमज़ोर कर देंगे, और इसी से 1907 में सूरत में फूट पड़ी। निम्नलिखित में से कौन-सा उनमें नहीं था?",
  ["Swaraj", "Swadeshi", "Boycott", "Passive resistance"],
  ["स्वराज", "स्वदेशी", "बहिष्कार", "निष्क्रिय प्रतिरोध"],
  3,
  "The Calcutta session, presided over by Dadabhai Naoroji, adopted resolutions on Swaraj, Swadeshi, Boycott and National Education. "
  "Passive resistance was the Extremists' method, not one of the four resolutions. The Extremists feared that the Moderate-led session planned for Nagpur, then shifted to Surat, would drop these resolutions, and the Congress split at Surat in December 1907.",
  "दादाभाई नौरोजी की अध्यक्षता में हुए कलकत्ता अधिवेशन ने स्वराज, स्वदेशी, बहिष्कार और राष्ट्रीय शिक्षा पर प्रस्ताव पारित किए। "
  "निष्क्रिय प्रतिरोध गरमपंथियों की पद्धति थी, चार प्रस्तावों में से एक नहीं। गरमपंथियों को डर था कि नरमपंथियों के नेतृत्व वाला अधिवेशन, जो पहले नागपुर में होना था और फिर सूरत ले जाया गया, इन प्रस्तावों को छोड़ देगा, और दिसंबर 1907 में सूरत में कांग्रेस में फूट पड़ गई।",
  f"{FS} -- chapter on the Swadeshi movement and the Surat split.",
  "modern-calcutta-1906-resolutions-surat")

M("8c00713e-9ff9-4bfa-95f4-3772c8d46af1", "Modern", "medium",
  "'Vande Mataram', adopted in 1950 as India's National Song, was published as part of which novel of Bankim Chandra Chattopadhyay?",
  "1950 में भारत के राष्ट्रीय गीत के रूप में अपनाया गया 'वंदे मातरम्' बंकिम चंद्र चट्टोपाध्याय के किस उपन्यास के अंश के रूप में प्रकाशित हुआ?",
  ["Anandamath", "Durgeshnandini", "Kapalkundala", "Rajmohan's Wife"],
  ["आनंदमठ", "दुर्गेशनंदिनी", "कपालकुंडला", "राजमोहन्स वाइफ़"],
  0,
  "Bankim Chandra composed 'Vande Mataram' in the 1870s and included it in Anandamath (1882), a novel set against the Sannyasi rebellion. It became the slogan of the Swadeshi movement, and the Constituent Assembly adopted its first two stanzas as the National Song on 24 January 1950. "
  "Durgeshnandini (1865) and Kapalkundala (1866) are his earlier Bengali novels, and Rajmohan's Wife his only English novel. The song's 150th year was marked from 7 November 2025.",
  "बंकिम चंद्र ने 1870 के दशक में 'वंदे मातरम्' रचा और इसे संन्यासी विद्रोह की पृष्ठभूमि वाले उपन्यास आनंदमठ (1882) में शामिल किया। यह स्वदेशी आंदोलन का नारा बना, और संविधान सभा ने 24 जनवरी 1950 को इसके पहले दो छंदों को राष्ट्रीय गीत के रूप में अपनाया। "
  "दुर्गेशनंदिनी (1865) और कपालकुंडला (1866) उनके पहले के बांग्ला उपन्यास हैं, और राजमोहन्स वाइफ़ उनका एकमात्र अंग्रेज़ी उपन्यास है। 7 नवंबर 2025 से इस गीत का 150वाँ वर्ष मनाया गया।",
  "Constituent Assembly of India Debates, 24 January 1950 (statement on the National Anthem and National Song); Ministry of Culture -- 150 years of Vande Mataram (2025).",
  "modern-vande-mataram-anandamath")

M("cf8dc53b-9134-4407-b1d4-76ce611272c8", "Modern", "medium",
  "Dadabhai Naoroji set out his theory of the 'drain of wealth' from India most fully in:",
  "दादाभाई नौरोजी ने भारत से 'धन के निष्कासन' (drain of wealth) का अपना सिद्धांत सबसे विस्तार से किस ग्रंथ में रखा?",
  ["Poverty and Un-British Rule in India", "The Economic History of India", "Hind Swaraj", "Gita Rahasya"],
  ["पॉवर्टी एंड अन-ब्रिटिश रूल इन इंडिया", "द इकोनॉमिक हिस्ट्री ऑफ़ इंडिया", "हिंद स्वराज", "गीता रहस्य"],
  0,
  "Naoroji's Poverty and Un-British Rule in India (1901) brought together his papers arguing that India's wealth was being drained to Britain through 'home charges', salaries, pensions and profits, without an equal return. "
  "R.C. Dutt's The Economic History of India (1901-03) developed the economic critique further; Gandhi's Hind Swaraj (1909) is a critique of modern civilisation, and Tilak's Gita Rahasya a commentary on the Bhagavad Gita written in Mandalay jail.",
  "नौरोजी की पॉवर्टी एंड अन-ब्रिटिश रूल इन इंडिया (1901) में उनके वे लेख संकलित हैं जिनमें उन्होंने तर्क दिया कि 'होम चार्जेज़', वेतन, पेंशन और मुनाफ़े के ज़रिए भारत का धन बिना बराबर वापसी के ब्रिटेन जा रहा था। "
  "आर.सी. दत्त की द इकोनॉमिक हिस्ट्री ऑफ़ इंडिया (1901-03) ने आर्थिक आलोचना को और आगे बढ़ाया; गांधीजी का हिंद स्वराज (1909) आधुनिक सभ्यता की आलोचना है, और तिलक का गीता रहस्य मांडले जेल में लिखी गई भगवद्गीता की टीका है।",
  f"{FS} -- chapter on the economic critique of colonialism; {SPEC} -- chapter on the economic impact of British rule.",
  "modern-drain-theory-naoroji")

S("a56615f0-ee7b-4e5c-8bdb-62d9a7391096", "Modern", "medium",
  "During the Quit India movement, parallel governments were set up in which of the following places?",
  "भारत छोड़ो आंदोलन के दौरान निम्नलिखित में से किन स्थानों पर समानांतर सरकारें स्थापित की गईं?",
  ["Ballia", "Tamluk", "Satara"],
  ["बलिया", "तामलुक", "सतारा"],
  None, 3,
  "All three are correct. Chittu Pande set up a short-lived parallel government at Ballia (August 1942); the Tamralipta Jatiya Sarkar at Tamluk in Midnapore lasted from December 1942 to 1944; and the 'Prati Sarkar' at Satara, led by Nana Patil, was the longest-lasting, continuing into 1945. "
  "These show that the movement went beyond protest to underground administration in some districts.",
  "तीनों सही हैं। चित्तू पांडे ने बलिया में अल्पकालिक समानांतर सरकार बनाई (अगस्त 1942); मिदनापुर के तामलुक में ताम्रलिप्त जातीय सरकार दिसंबर 1942 से 1944 तक चली; और नाना पाटिल के नेतृत्व में सतारा की 'प्रति सरकार' सबसे लंबे समय तक, 1945 तक, चली। "
  "इससे पता चलता है कि कुछ ज़िलों में आंदोलन विरोध से आगे बढ़कर भूमिगत प्रशासन तक पहुँचा।",
  f"{FS} -- chapter on the Quit India movement.",
  "modern-quit-india-parallel-governments",
  opts=["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], closing=CODE)

M("1624becd-d451-412b-b18e-220a3a1dae97", "Modern", "medium",
  "Which organisation did Gandhi set up in 1932, soon after the Poona Pact, to work for the removal of untouchability?",
  "पूना समझौते के तुरंत बाद 1932 में गांधीजी ने छुआछूत मिटाने के लिए कौन-सा संगठन बनाया?",
  ["Harijan Sevak Sangh", "Depressed Classes Mission", "Bahishkrit Hitakarini Sabha", "Servants of India Society"],
  ["हरिजन सेवक संघ", "डिप्रेस्ड क्लासेज़ मिशन", "बहिष्कृत हितकारिणी सभा", "सर्वेंट्स ऑफ़ इंडिया सोसाइटी"],
  0,
  "Gandhi founded the All India Anti-Untouchability League in September 1932, soon renamed the Harijan Sevak Sangh, and started the weekly Harijan in 1933. "
  "The Depressed Classes Mission was founded by V.R. Shinde (1906), the Bahishkrit Hitakarini Sabha by B.R. Ambedkar (1924), and the Servants of India Society by G.K. Gokhale (1905).",
  "गांधीजी ने सितंबर 1932 में अखिल भारतीय छुआछूत विरोधी लीग बनाई, जिसका नाम जल्दी ही हरिजन सेवक संघ कर दिया गया, और 1933 में साप्ताहिक हरिजन शुरू किया। "
  "डिप्रेस्ड क्लासेज़ मिशन की स्थापना वी.आर. शिंदे (1906) ने, बहिष्कृत हितकारिणी सभा की बी.आर. आंबेडकर (1924) ने, और सर्वेंट्स ऑफ़ इंडिया सोसाइटी की जी.के. गोखले (1905) ने की।",
  f"{FS} -- chapter on the Civil Disobedience movement; {SPEC} -- chapter on social reform.",
  "modern-harijan-sevak-sangh-1932")

M("4c2aaef5-57df-4dcd-bd92-909265371adf", "Modern", "hard",
  "The Karachi session of the Indian National Congress (1931) is chiefly remembered for:",
  "भारतीय राष्ट्रीय कांग्रेस का कराची अधिवेशन (1931) मुख्य रूप से किस बात के लिए याद किया जाता है?",
  ["the adoption of Purna Swaraj as the goal of the Congress",
   "its resolutions on Fundamental Rights and a National Economic Programme",
   "the launch of the Non-Cooperation programme",
   "the reunion of the Moderates and the Extremists"],
  ["कांग्रेस के लक्ष्य के रूप में पूर्ण स्वराज को अपनाने के लिए",
   "मौलिक अधिकारों और राष्ट्रीय आर्थिक कार्यक्रम पर अपने प्रस्तावों के लिए",
   "असहयोग कार्यक्रम की शुरुआत के लिए",
   "नरमपंथियों और गरमपंथियों के पुनर्मिलन के लिए"],
  1,
  "The Karachi session (March 1931), presided over by Vallabhbhai Patel, endorsed the Gandhi-Irwin Pact and adopted resolutions on Fundamental Rights and a National Economic Programme -- the first statement of what freedom would mean for ordinary people, and a forerunner of Parts III and IV of the Constitution. "
  "Purna Swaraj was adopted at Lahore (1929), the Non-Cooperation programme at the special Calcutta session and Nagpur (1920), and the Moderates and Extremists reunited at Lucknow (1916).",
  "कराची अधिवेशन (मार्च 1931), जिसकी अध्यक्षता वल्लभभाई पटेल ने की, ने गांधी-इरविन समझौते का अनुमोदन किया और मौलिक अधिकारों तथा राष्ट्रीय आर्थिक कार्यक्रम पर प्रस्ताव पारित किए; यह इस बात का पहला वक्तव्य था कि आम लोगों के लिए स्वतंत्रता का क्या अर्थ होगा, और संविधान के भाग III और IV का अग्रदूत था। "
  "पूर्ण स्वराज लाहौर (1929) में, असहयोग कार्यक्रम कलकत्ता के विशेष अधिवेशन और नागपुर (1920) में अपनाया गया, और नरमपंथी तथा गरमपंथी लखनऊ (1916) में फिर एक हुए।",
  f"{FS} -- chapter on the Civil Disobedience movement; M. Laxmikanth, Indian Polity -- historical background.",
  "modern-karachi-resolution-1931")

P("cc8cadd7-7b98-41e3-9d31-81ed1d1faf36", "Modern", "medium",
  "Consider the following pairs of revolutionaries and the organisations they founded or led:",
  "क्रांतिकारियों और उनके द्वारा स्थापित या नेतृत्व किए गए संगठनों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bhagat Singh : Naujawan Bharat Sabha", "Surya Sen : Indian Republican Army, Chittagong branch", "V.D. Savarkar : Abhinav Bharat", "Lala Har Dayal : Anushilan Samiti"],
  ["भगत सिंह : नौजवान भारत सभा", "सूर्य सेन : इंडियन रिपब्लिकन आर्मी, चटगाँव शाखा", "वी.डी. सावरकर : अभिनव भारत", "लाला हरदयाल : अनुशीलन समिति"],
  2,
  "Three pairs are correct. Bhagat Singh helped found the Naujawan Bharat Sabha at Lahore in 1926; Surya Sen's group carried out the Chittagong armoury raid (April 1930) as the 'Indian Republican Army, Chittagong Branch'; V.D. and Ganesh Savarkar founded the Abhinav Bharat (1904). "
  "Pair 4 is wrong: Lala Har Dayal was a founder of the Ghadar Party in San Francisco (1913); the Anushilan Samiti was a Bengal society associated with Pramathanath Mitra and Barindra Kumar Ghosh.",
  "तीन युग्म सही हैं। भगत सिंह ने 1926 में लाहौर में नौजवान भारत सभा की स्थापना में भाग लिया; सूर्य सेन के दल ने 'इंडियन रिपब्लिकन आर्मी, चटगाँव शाखा' के नाम से चटगाँव शस्त्रागार पर हमला (अप्रैल 1930) किया; वी.डी. और गणेश सावरकर ने अभिनव भारत (1904) की स्थापना की। "
  "युग्म 4 गलत है: लाला हरदयाल सैन फ़्रांसिस्को में ग़दर पार्टी (1913) के संस्थापकों में थे; अनुशीलन समिति बंगाल का संगठन था, जो प्रमथनाथ मित्र और बारींद्र कुमार घोष से जुड़ा था।",
  f"{FS} -- chapters on the revolutionary movements; {SPEC} -- chapter on revolutionary nationalism.",
  "modern-revolutionaries-organisations-pairs")

P("8041d0f9-c660-432d-b835-8cdc27ddcc46", "Modern", "medium",
  "Consider the following pairs of Acts and what they provided:",
  "अधिनियमों और उनके प्रावधानों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Indian Councils Act, 1909 : Separate electorates for Muslims", "Government of India Act, 1919 : A bicameral central legislature",
   "Government of India Act, 1935 : A Federal Court", "Indian Independence Act, 1947 : Lapse of British paramountcy over the princely states"],
  ["भारतीय परिषद अधिनियम, 1909 : मुसलमानों के लिए पृथक निर्वाचन", "भारत शासन अधिनियम, 1919 : द्विसदनीय केंद्रीय विधानमंडल",
   "भारत शासन अधिनियम, 1935 : संघीय न्यायालय", "भारतीय स्वतंत्रता अधिनियम, 1947 : रियासतों पर ब्रिटिश सर्वोच्चता की समाप्ति"],
  3,
  "All four pairs are correct. The Morley-Minto Act (1909) introduced separate electorates for Muslims; the Montagu-Chelmsford Act (1919) created a bicameral central legislature (the Legislative Assembly and the Council of State); the 1935 Act set up the Federal Court (1937); and the Indian Independence Act (1947) ended British paramountcy over the princely states. "
  "Because Acts are usually tested by their best-known features, the less familiar ones here are the ones solvers doubt.",
  "चारों युग्म सही हैं। मॉर्ले-मिंटो अधिनियम (1909) ने मुसलमानों के लिए पृथक निर्वाचन शुरू किया; मॉन्टेग्यू-चेम्सफ़ोर्ड अधिनियम (1919) ने द्विसदनीय केंद्रीय विधानमंडल (लेजिस्लेटिव असेंबली और काउंसिल ऑफ़ स्टेट) बनाया; 1935 के अधिनियम से संघीय न्यायालय (1937) बना; और भारतीय स्वतंत्रता अधिनियम (1947) ने रियासतों पर ब्रिटिश सर्वोच्चता समाप्त की। "
  "चूँकि अधिनियमों को प्रायः उनकी सबसे प्रसिद्ध विशेषताओं से परखा जाता है, इसलिए यहाँ कम परिचित विशेषताओं पर ही विद्यार्थी संदेह करते हैं।",
  "M. Laxmikanth, Indian Polity -- historical background (the Acts of 1909, 1919, 1935 and 1947).",
  "modern-constitutional-acts-pairs")

P("8081e650-87d2-4fb8-98f6-e872fb0c25f1", "Modern", "hard",
  "Consider the following pairs of Viceroys and events of their tenure:",
  "वायसरायों और उनके कार्यकाल की घटनाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Lord Curzon : Partition of Bengal", "Lord Hardinge II : Transfer of the capital to Delhi", "Lord Chelmsford : Appointment of the Simon Commission", "Lord Mayo : Creation of the Statutory Civil Service"],
  ["लॉर्ड कर्ज़न : बंगाल विभाजन", "लॉर्ड हार्डिंग द्वितीय : राजधानी का दिल्ली स्थानांतरण", "लॉर्ड चेम्सफ़ोर्ड : साइमन आयोग की नियुक्ति", "लॉर्ड मेयो : वैधानिक सिविल सेवा (Statutory Civil Service) का गठन"],
  1,
  "Two pairs are correct: Curzon partitioned Bengal in 1905, and the transfer of the capital from Calcutta to Delhi was announced at the Delhi Durbar of 1911, in Hardinge's viceroyalty. "
  "Pair 3 is wrong: the Simon Commission was appointed in 1927, under Lord Irwin (Chelmsford's tenure, 1916-21, saw the 1919 reforms). "
  "Pair 4 is wrong: the Statutory Civil Service was created in 1879 under Lord Lytton; Mayo (1869-72) is known for financial decentralisation.",
  "दो युग्म सही हैं: कर्ज़न ने 1905 में बंगाल का विभाजन किया, और कलकत्ता से दिल्ली राजधानी ले जाने की घोषणा 1911 के दिल्ली दरबार में हार्डिंग के वायसराय काल में हुई। "
  "युग्म 3 गलत है: साइमन आयोग 1927 में लॉर्ड इरविन के समय नियुक्त हुआ (चेम्सफ़ोर्ड के कार्यकाल, 1916-21, में 1919 के सुधार आए)। "
  "युग्म 4 गलत है: वैधानिक सिविल सेवा 1879 में लॉर्ड लिटन के समय बनी; मेयो (1869-72) वित्तीय विकेंद्रीकरण के लिए जाने जाते हैं।",
  f"{SPEC} -- chapters on administrative policies and the struggle of 1905-1918.",
  "modern-viceroys-events-pairs")

P("215de858-d33c-45fd-a523-fbe6cb2a46ac", "Modern", "medium",
  "Consider the following pairs of leaders and the newspapers or journals they edited:",
  "नेताओं और उनके द्वारा संपादित समाचार-पत्रों या पत्रिकाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bal Gangadhar Tilak : Mahratta", "Mahatma Gandhi : Harijan", "Annie Besant : Kesari", "Surendranath Banerjee : Bengalee"],
  ["बाल गंगाधर तिलक : मराठा", "महात्मा गांधी : हरिजन", "एनी बेसेंट : केसरी", "सुरेंद्रनाथ बनर्जी : बंगाली"],
  2,
  "Three pairs are correct. Tilak ran the Mahratta in English and the Kesari in Marathi; Gandhi edited Harijan from 1933 (after Young India and Navajivan); Surendranath Banerjee edited the Bengalee. "
  "Pair 3 is wrong: the Kesari was Tilak's Marathi paper; Annie Besant published New India and the Commonweal during the Home Rule movement. "
  "The pairing tests whether the solver knows that Tilak had two papers, not one.",
  "तीन युग्म सही हैं। तिलक अंग्रेज़ी में मराठा और मराठी में केसरी चलाते थे; गांधीजी ने 1933 से हरिजन का संपादन किया (यंग इंडिया और नवजीवन के बाद); सुरेंद्रनाथ बनर्जी ने बंगाली का संपादन किया। "
  "युग्म 3 गलत है: केसरी तिलक का मराठी पत्र था; एनी बेसेंट ने होम रूल आंदोलन के दौरान न्यू इंडिया और कॉमनवील प्रकाशित किए। "
  "यह युग्म परखता है कि विद्यार्थी जानता है कि तिलक के एक नहीं, दो पत्र थे।",
  f"{SPEC} -- chapter on the rise of the national movement (the press).",
  "modern-leaders-newspapers-pairs")

P("058988f4-8802-4646-9982-7fd6ea0d8d08", "Modern", "hard",
  "Consider the following pairs of sessions of the Indian National Congress and their presidents:",
  "भारतीय राष्ट्रीय कांग्रेस के अधिवेशनों और उनके अध्यक्षों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Surat, 1907 : Rash Behari Ghosh", "Lucknow, 1916 : Ambika Charan Mazumdar", "Nagpur, 1920 : Lala Lajpat Rai", "Karachi, 1931 : Jawaharlal Nehru"],
  ["सूरत, 1907 : रासबिहारी घोष", "लखनऊ, 1916 : अंबिका चरण मजूमदार", "नागपुर, 1920 : लाला लाजपत राय", "कराची, 1931 : जवाहरलाल नेहरू"],
  1,
  "Two pairs are correct: Rash Behari Ghosh was the Moderates' president at Surat, and Ambika Charan Mazumdar presided at Lucknow in 1916. "
  "Pair 3 is wrong: the Nagpur session (December 1920) was presided over by C. Vijayaraghavachariar; Lala Lajpat Rai presided over the special Calcutta session of September 1920, which first approved Non-Cooperation. "
  "Pair 4 is wrong: Vallabhbhai Patel presided at Karachi; Nehru had presided at Lahore in 1929. Both wrong names presided over a neighbouring session, which is the trap.",
  "दो युग्म सही हैं: सूरत में नरमपंथियों के अध्यक्ष रासबिहारी घोष थे, और 1916 में लखनऊ की अध्यक्षता अंबिका चरण मजूमदार ने की। "
  "युग्म 3 गलत है: नागपुर अधिवेशन (दिसंबर 1920) की अध्यक्षता सी. विजयराघवाचारियर ने की; लाला लाजपत राय ने सितंबर 1920 के कलकत्ता विशेष अधिवेशन की अध्यक्षता की, जिसने पहली बार असहयोग को स्वीकृति दी। "
  "युग्म 4 गलत है: कराची की अध्यक्षता वल्लभभाई पटेल ने की; नेहरू ने 1929 में लाहौर की अध्यक्षता की थी। दोनों गलत नाम पास के किसी अधिवेशन के अध्यक्ष थे, और यही जाल है।",
  f"{FS} -- chapters on the national movement (Congress sessions).",
  "modern-inc-sessions-presidents-pairs")

C("047a92a4-016f-4909-bde4-f877bca4d319", "Modern", "medium",
  "Consider the following events:",
  "निम्नलिखित घटनाओं पर विचार कीजिए:",
  ["Lucknow Pact between the Congress and the Muslim League", "Montagu's August Declaration", "Passing of the Rowlatt Act", "Founding of Tilak's Home Rule League"],
  ["कांग्रेस और मुस्लिम लीग के बीच लखनऊ समझौता", "मॉन्टेग्यू की अगस्त घोषणा", "रौलट एक्ट का पारित होना", "तिलक की होम रूल लीग की स्थापना"],
  ["4-1-2-3", "1-4-2-3", "4-2-1-3", "1-2-4-3"], 0,
  "The order is 4-1-2-3: Tilak founded his Home Rule League at Belgaum in April 1916 (Annie Besant's followed in September); the Lucknow Pact was concluded in December 1916; Montagu declared the goal of 'responsible government' on 20 August 1917; and the Rowlatt Act was passed in March 1919. "
  "The sequence matters because the Home Rule agitation and the Lucknow Pact together pushed the British towards the August Declaration.",
  "सही क्रम 4-1-2-3 है: तिलक ने अप्रैल 1916 में बेलगाम में अपनी होम रूल लीग बनाई (एनी बेसेंट की लीग सितंबर में बनी); लखनऊ समझौता दिसंबर 1916 में हुआ; मॉन्टेग्यू ने 20 अगस्त 1917 को 'उत्तरदायी शासन' का लक्ष्य घोषित किया; और रौलट एक्ट मार्च 1919 में पारित हुआ। "
  "यह क्रम इसलिए महत्त्वपूर्ण है कि होम रूल आंदोलन और लखनऊ समझौते ने मिलकर अंग्रेज़ों को अगस्त घोषणा की ओर धकेला।",
  f"{FS} -- chapters on the Home Rule movement and the Rowlatt satyagraha.",
  "modern-1916-1919-chronology")

if __name__ == "__main__":
    # Difficulty labels the audit found wrong (content unchanged).
    for fid, d in [("07500f01-6631-4dde-809c-0592c9595c09", "medium"), ("6f46e193-9f72-450e-a3fe-294118d62920", "easy"),
                   ("d50264bf-02f2-48f7-985d-5e26f53d0ac0", "easy"), ("cc567df3", "easy")]:
        cond = f"id = '{fid}'" if len(fid) > 8 else f"id::text like '{fid}%'"
        OUT.append(f"update public.questions set difficulty = '{d}', updated_at = now() where {cond} and exam_category = 'upsc' returning id;")
    write("history_rewrite_modern.sql")
