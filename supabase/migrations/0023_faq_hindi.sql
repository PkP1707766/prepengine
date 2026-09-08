-- ============================================================================
-- FAQ Hindi translations.
--
-- faqs.question/answer had no Hindi counterpart at all -- toggling the site
-- to Hindi left the FAQ page's own content (as opposed to its chrome, fixed
-- separately) sitting in English. Nullable columns, same opt-in shape as
-- every other bilingual field in this schema (plans.name_hi, tests.title_hi,
-- ...): a row without a translation falls back to English rather than
-- showing blank, so publishing a new FAQ in English-only is never blocked
-- on someone writing the Hindi first.
--
-- The eleven rows that exist today are backfilled with real translations
-- (not placeholders) so the feature is immediately visible rather than
-- landing dark until an admin fills every row in by hand.
-- ============================================================================

alter table public.faqs
  add column if not exists question_hi text,
  add column if not exists answer_hi   text;

-- access
update public.faqs set
  question_hi = 'क्या JUNOONIAS हिन्दी में इस्तेमाल कर सकते हैं?',
  answer_hi   = 'हाँ। ऊपर हेडर में भाषा बदलने का बटन है, वहाँ से English और हिन्दी में बदल सकते हैं। आपकी पसंद अगली बार भी याद रहती है।'
where question = 'Can I use JUNOONIAS in Hindi?';

update public.faqs set
  question_hi = 'क्या यह फ़ोन पर ठीक से चलता है?',
  answer_hi   = 'हाँ — पूरा प्लेटफ़ॉर्म, एग्ज़ाम स्क्रीन समेत, फ़ोन और टैबलेट पर उतना ही अच्छे से चलता है जितना डेस्कटॉप पर।'
where question = 'Does it work properly on a phone?';

update public.faqs set
  question_hi = 'टेस्ट के बीच में इंटरनेट चला जाए तो मेरे नतीजों का क्या होगा?',
  answer_hi   = 'जब तक आप लिख रहे हैं, आपके जवाब ब्राउज़र में ही सुरक्षित रहते हैं। सबमिट करते ही रिपोर्ट बनती है, और उसके तुरंत बाद अटेम्प्ट आपके खाते में सेव हो जाता है — अगर किसी वजह से सेव न हो पाए, तो स्क्रीन पर साफ़ बता दिया जाता है, चुपचाप नाकाम नहीं होता।'
where question = 'What happens to my results if I lose connection mid-test?';

-- payments
update public.faqs set
  question_hi = 'आप कौन-कौन से भुगतान के तरीक़े स्वीकार करते हैं?',
  answer_hi   = 'भुगतान Razorpay संभालता है — UPI, डेबिट-क्रेडिट कार्ड और नेटबैंकिंग। JUNOONIAS आपके कार्ड की जानकारी कभी देखता या रखता नहीं है।'
where question = 'Which payment methods do you accept?';

update public.faqs set
  question_hi = 'क्या एक परीक्षा की सीरीज़ ख़रीदने से बाक़ी परीक्षाएँ भी अनलॉक हो जाती हैं?',
  answer_hi   = 'नहीं। हर परीक्षा की टेस्ट सीरीज़ अलग बंडल है, अपनी अलग क़ीमत के साथ, और सिर्फ़ अपने ही टेस्ट अनलॉक करती है। आप सिर्फ़ उसी परीक्षा के लिए भुगतान करते हैं जिसकी तैयारी कर रहे हैं।'
where question = "Does buying one exam's series unlock the others?";

update public.faqs set
  question_hi = 'मेरी एक्सेस कितने दिन चलती है?',
  answer_hi   = 'हर बंडल पर वैधता भुगतान से पहले ही दिखा दी जाती है, और जुड़ने के बाद डैशबोर्ड पर भी दिखती रहती है। ज़्यादातर सीरीज़ ख़रीद की तारीख़ से 12 महीने चलती हैं।'
where question = 'How long does my access last?';

update public.faqs set
  question_hi = 'मैंने भुगतान कर दिया लेकिन एक्सेस अभी तक चालू नहीं हुई। क्या करूँ?',
  answer_hi   = 'आमतौर पर भुगतान के कुछ ही सेकंड में एक्सेस चालू हो जाती है। अगर नहीं हुई, तो एक बार पेज को रीफ़्रेश कीजिए — फिर भी न हो, तो Razorpay रसीद में मिला पेमेंट रेफ़रेंस लेकर junoonias123@gmail.com पर ईमेल कीजिए, हम इसे ख़ुद चालू कर देंगे।'
where question = 'I paid but my access has not activated. What do I do?';

-- tests
update public.faqs set
  question_hi = 'क्या टेस्ट सीरीज़ देखने के लिए खाता बनाना ज़रूरी है?',
  answer_hi   = 'नहीं। पूरा कैटलॉग, हर बंडल में क्या-क्या मिलेगा और उसकी क़ीमत — यह सब सबके लिए खुला है। खाता सिर्फ़ तभी चाहिए जब आप जुड़ने का फ़ैसला करते हैं।'
where question = 'Do I need an account to browse the test series?';

update public.faqs set
  question_hi = 'मॉक टेस्ट किस तरह बने होते हैं?',
  answer_hi   = 'हर पेपर असली परीक्षा की तरह सेक्शन में बँटा होता है, वही अंकन योजना और वही नेगेटिव मार्किंग के साथ। सही और ग़लत जवाब पर ठीक कितने अंक मिलेंगे, यह शुरू करने से पहले निर्देश वाली स्क्रीन पर दिखा दिया जाता है।'
where question = 'How are the mock tests structured?';

update public.faqs set
  question_hi = 'क्या मैं टेस्ट दोबारा दे सकता/सकती हूँ?',
  answer_hi   = 'हाँ। हर प्रयास अलग से सेव होता है, तो आप देख सकते हैं कि दूसरी बार पहली बार के मुक़ाबले कैसा किया।'
where question = 'Can I re-attempt a test?';

update public.faqs set
  question_hi = 'मेरी रैंक कैसे तय होती है?',
  answer_hi   = 'आपका पर्सेंटाइल और अखिल भारतीय रैंक उन सबके मुक़ाबले निकाला जाता है जिन्होंने वही पेपर दिया है। अगर आप वह टेस्ट देने वाले पहले व्यक्ति हैं, तो तुलना तब तक छुपी रहती है जब तक बाक़ी लोग न दें — हम कोई बनावटी बेंचमार्क नहीं दिखाते।'
where question = 'How is my rank calculated?';
