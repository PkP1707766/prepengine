/* ============================================================================
   Legal pages — Privacy Policy, Terms & Conditions, Refund Policy, Contact.
   ============================================================================

   These are not decoration. Razorpay will not activate a merchant account
   without a reachable Privacy Policy, Terms & Conditions, a Refund /
   Cancellation Policy and a Contact page, and Indian consumer rules require a
   refund policy on any online sale. The site was taking payments with none of
   them.

   ┌──────────────────────────────────────────────────────────────────────────┐
   │  YOU MUST FILL THIS IN BEFORE LAUNCH.                                    │
   │                                                                          │
   │  I have deliberately NOT invented a legal entity name, a registered       │
   │  address, a GSTIN or a jurisdiction — putting made-up company details on  │
   │  a legal page is worse than having no page, and Razorpay checks them      │
   │  against your KYC documents.                                             │
   │                                                                          │
   │  Every value below marked TODO shows on the live site as a visible        │
   │  "[ to be filled ]" marker, so an unfilled one cannot ship unnoticed.     │
   └──────────────────────────────────────────────────────────────────────────┘ */

export const COMPANY = {
  brand:      "JUNOONIAS",
  legalName:  "",            // TODO e.g. "Junoonias Edutech Private Limited"
  address:    "",            // TODO full registered address with PIN
  city:       "",            // TODO
  state:      "",            // TODO — also the jurisdiction for disputes
  email:      "junoonias123@gmail.com",
  phone:      "",            // TODO a number you will actually answer
  gstin:      "",            // TODO if registered; leave blank if not
  cin:        "",            // TODO if a private limited company
};

/** Anything still unfilled renders as an obvious marker rather than a blank,
 *  so a missing detail is visible on the page instead of silently absent. */
export const val = (v, lang = "en") =>
  (v && String(v).trim()) ? v : (lang === "hi" ? "[ भरा जाना बाकी ]" : "[ to be filled ]");

export const LEGAL_KEYS = ["privacy", "terms", "refund", "contact"];

/* Social profiles. Empty by default and only rendered when filled — a footer
   icon that opens a 404, or somebody else's account, is worse than no icon.
   Fill in the full https:// URL of each profile you actually run. */
export const SOCIAL_LINKS = {
  instagram: "",   // TODO
  youtube:   "",   // TODO
  telegram:  "",   // TODO
  whatsapp:  "",   // TODO e.g. https://whatsapp.com/channel/... or a wa.me link
  linkedin:  "",   // TODO
  x:         "",   // TODO
};

/* Each page is a list of { h, p[] } blocks so the renderer stays dumb and the
   copy stays readable here. */
export const LEGAL = {
  /* ---------------------------------------------------------------- privacy */
  privacy: {
    title: { en: "Privacy Policy", hi: "गोपनीयता नीति" },
    intro: {
      en: "This policy explains what we collect when you use JUNOONIAS, why we collect it, and what we do not do with it.",
      hi: "यह नीति बताती है कि JUNOONIAS का उपयोग करते समय हम क्या जानकारी लेते हैं, क्यों लेते हैं, और उसके साथ क्या नहीं करते।",
    },
    blocks: [
      {
        h: { en: "What we collect", hi: "हम क्या एकत्र करते हैं" },
        p: {
          en: [
            "Your name, email address and phone number when you create an account.",
            "Your answers, scores, time per question and rank for every test you attempt — this is the product; without it there is no analysis.",
            "Payment records: amount, date, plan and the Razorpay reference. We never see or store your card number, UPI PIN or bank credentials — those go directly to Razorpay.",
            "Basic technical information your browser sends, such as device type and screen size, which is how the site knows to lay itself out for a phone.",
          ],
          hi: [
            "खाता बनाते समय आपका नाम, ईमेल पता और फ़ोन नंबर।",
            "हर टेस्ट के आपके उत्तर, अंक, प्रति प्रश्न समय और रैंक — यही उत्पाद है; इसके बिना कोई विश्लेषण संभव नहीं।",
            "भुगतान रिकॉर्ड: राशि, तारीख़, प्लान और Razorpay संदर्भ। आपका कार्ड नंबर, UPI PIN या बैंक विवरण हम न देखते हैं न रखते हैं — वे सीधे Razorpay को जाते हैं।",
            "आपका ब्राउज़र जो सामान्य तकनीकी जानकारी भेजता है, जैसे डिवाइस का प्रकार और स्क्रीन का आकार — इसी से साइट फ़ोन के हिसाब से सजती है।",
          ],
        },
      },
      {
        h: { en: "What we do not do", hi: "हम क्या नहीं करते" },
        p: {
          en: [
            "We do not sell your data, and we do not share it with advertisers or data brokers.",
            "We do not show your email or phone number to other students. Someone who joins on your referral link sees only a shortened name.",
            "We do not read your answers for any purpose other than scoring, your own analysis, and the anonymous averages used to compute rank.",
          ],
          hi: [
            "हम आपका डेटा न बेचते हैं, न विज्ञापनदाताओं या डेटा ब्रोकर के साथ साझा करते हैं।",
            "हम आपका ईमेल या फ़ोन नंबर दूसरे छात्रों को नहीं दिखाते। आपके रेफ़रल लिंक से जुड़ने वाले को केवल संक्षिप्त नाम दिखता है।",
            "आपके उत्तर केवल मूल्यांकन, आपके अपने विश्लेषण, और रैंक निकालने के लिए उपयोग होने वाले अनाम औसत के लिए ही पढ़े जाते हैं।",
          ],
        },
      },
      {
        h: { en: "Who else touches your data", hi: "आपका डेटा और कौन देखता है" },
        p: {
          en: [
            "Supabase hosts our database and handles sign-in.",
            "Razorpay processes payments and holds the payment instrument details we never receive.",
            "Vercel serves the website itself.",
            "Each of these sees only what it needs to do its job.",
          ],
          hi: [
            "Supabase हमारा डेटाबेस होस्ट करता है और साइन-इन संभालता है।",
            "Razorpay भुगतान संसाधित करता है और भुगतान साधन का वह विवरण रखता है जो हम तक कभी नहीं आता।",
            "Vercel वेबसाइट को सर्व करता है।",
            "इनमें से हर एक को केवल उतना ही दिखता है जितना उसके काम के लिए ज़रूरी है।",
          ],
        },
      },
      {
        h: { en: "Your choices", hi: "आपके अधिकार" },
        p: {
          en: [
            "You can edit your name, city, target exam and photo yourself from the Profile screen.",
            "Write to us to request a copy of your data, or to have your account and attempts deleted. We will act within 30 days. Payment records are kept longer where tax law requires it.",
            "You can unsubscribe from emails using the link in any email we send.",
          ],
          hi: [
            "अपना नाम, शहर, लक्ष्य परीक्षा और फ़ोटो आप प्रोफ़ाइल स्क्रीन से स्वयं बदल सकते हैं।",
            "अपने डेटा की प्रति माँगने या खाता और प्रयास हटवाने के लिए हमें लिखिए। हम 30 दिनों के भीतर कार्रवाई करेंगे। कर-क़ानून जहाँ आवश्यक करे, भुगतान रिकॉर्ड अधिक समय तक रखे जाते हैं।",
            "हमारे किसी भी ईमेल में दिए लिंक से आप सदस्यता समाप्त कर सकते हैं।",
          ],
        },
      },
    ],
  },

  /* ------------------------------------------------------------------ terms */
  terms: {
    title: { en: "Terms & Conditions", hi: "नियम एवं शर्तें" },
    intro: {
      en: "By creating an account or buying a test series you agree to these terms.",
      hi: "खाता बनाकर या टेस्ट सीरीज़ खरीदकर आप इन शर्तों से सहमत होते हैं।",
    },
    blocks: [
      {
        h: { en: "Your account", hi: "आपका खाता" },
        p: {
          en: [
            "One account per person. Keep your password to yourself — everything done from your account is treated as done by you.",
            "You must be old enough to enter a contract, or have a parent or guardian agree on your behalf.",
          ],
          hi: [
            "एक व्यक्ति, एक खाता। अपना पासवर्ड अपने पास रखिए — आपके खाते से जो कुछ होता है, उसे आपका किया माना जाएगा।",
            "अनुबंध करने की आयु आपकी होनी चाहिए, अन्यथा माता-पिता या अभिभावक की सहमति आवश्यक है।",
          ],
        },
      },
      {
        h: { en: "What you are buying", hi: "आप क्या खरीद रहे हैं" },
        p: {
          en: [
            "Access to the papers listed in that specific series, for the period shown on its card, for your own preparation.",
            "Each series is sold on its own. Buying one does not unlock another, and we do not add charges you did not choose.",
            "Papers may be added to a series during your access period. We do not guarantee a fixed number beyond what the series page states at the time you buy.",
          ],
          hi: [
            "उसी सीरीज़ में सूचीबद्ध पेपरों तक, उसके कार्ड पर दिखाई गई अवधि के लिए, आपकी अपनी तैयारी हेतु पहुँच।",
            "हर सीरीज़ अलग बिकती है। एक खरीदने से दूसरी नहीं खुलती, और आपकी बिना पसंद के कोई शुल्क नहीं जोड़ा जाता।",
            "आपकी अवधि के दौरान सीरीज़ में पेपर जोड़े जा सकते हैं। खरीद के समय सीरीज़ पृष्ठ पर जो लिखा है, उससे अधिक संख्या की गारंटी नहीं है।",
          ],
        },
      },
      {
        h: { en: "What you may not do", hi: "क्या नहीं करना है" },
        p: {
          en: [
            "Do not share, sell, record, screenshot in bulk, or republish our questions and solutions. They are our work and the reason the series has value.",
            "Do not share your login. Access is for one person.",
            "Do not attempt to extract answer keys, interfere with scoring, or manipulate ranks. Attempts are scored on our servers and irregular activity is reviewed.",
            "We may suspend an account that does any of the above, without a refund.",
          ],
          hi: [
            "हमारे प्रश्न और समाधान साझा, बिक्री, रिकॉर्ड, थोक में स्क्रीनशॉट या पुनः प्रकाशित न करें। वे हमारी मेहनत हैं और सीरीज़ का मूल्य उन्हीं से है।",
            "अपना लॉगिन साझा न करें। पहुँच एक व्यक्ति के लिए है।",
            "उत्तर-कुंजी निकालने, मूल्यांकन में हस्तक्षेप करने या रैंक बदलने का प्रयास न करें। प्रयास हमारे सर्वर पर जाँचे जाते हैं और असामान्य गतिविधि की समीक्षा होती है।",
            "उपर्युक्त में से कुछ भी करने पर खाता निलंबित किया जा सकता है, बिना धन-वापसी के।",
          ],
        },
      },
      {
        h: { en: "Referral rewards", hi: "रेफ़रल इनाम" },
        p: {
          en: [
            "A referral bonus is credited only when the person you invited completes a genuine paid purchase.",
            "Self-referrals, duplicate accounts and any attempt to game the scheme are not counted, and a bonus is reversed if the underlying payment is refunded.",
            "Withdrawal requires the minimum balance shown on your wallet and one currently active course at the time you ask.",
          ],
          hi: [
            "रेफ़रल बोनस तभी मिलता है जब आपके बुलाए व्यक्ति की वास्तविक भुगतान वाली खरीद पूरी हो।",
            "सेल्फ़-रेफ़रल, डुप्लिकेट खाते और योजना से खिलवाड़ की कोई भी कोशिश नहीं गिनी जाती, और मूल भुगतान वापस होने पर बोनस भी वापस ले लिया जाता है।",
            "निकासी के लिए वॉलेट पर दिखाया गया न्यूनतम बैलेंस और माँगते समय एक चालू कोर्स होना ज़रूरी है।",
          ],
        },
      },
      {
        h: { en: "Honest limits", hi: "ईमानदार सीमाएँ" },
        p: {
          en: [
            "We prepare papers to the exam pattern to the best of our understanding. We are not affiliated with UPSC, BPSC, UPPCS or any examining body, and we do not claim to predict their papers.",
            "Ranks and percentiles are computed against the students who took the same paper here. They are a useful signal, not a forecast of your result.",
            "We aim to keep the site available, but we cannot promise uninterrupted service.",
          ],
          hi: [
            "हम अपनी समझ के अनुसार परीक्षा-पैटर्न पर पेपर बनाते हैं। हम UPSC, BPSC, UPPCS या किसी परीक्षा संस्था से संबद्ध नहीं हैं, और उनके पेपर की भविष्यवाणी का दावा नहीं करते।",
            "रैंक और पर्सेंटाइल यहीं वही पेपर देने वाले छात्रों के सामने निकाले जाते हैं। यह उपयोगी संकेत है, आपके परिणाम की भविष्यवाणी नहीं।",
            "हम साइट को चालू रखने का प्रयास करते हैं, पर निर्बाध सेवा का वादा नहीं कर सकते।",
          ],
        },
      },
    ],
  },

  /* ----------------------------------------------------------------- refund */
  refund: {
    title: { en: "Refund & Cancellation Policy", hi: "धन-वापसी एवं रद्दीकरण नीति" },
    intro: {
      en: "Written plainly, because a refund policy nobody can understand is not a policy.",
      hi: "सीधी भाषा में, क्योंकि जो नीति समझ ही न आए वह नीति नहीं है।",
    },
    blocks: [
      {
        h: { en: "The 7-day window", hi: "7 दिन की अवधि" },
        p: {
          en: [
            "Ask within 7 days of payment and we will refund you in full, provided you have attempted no more than one paper from the series.",
            "We would rather you tried a free paper first — every series lists which of its papers are free to attempt without paying.",
          ],
          hi: [
            "भुगतान के 7 दिनों के भीतर कहिए, और यदि आपने सीरीज़ का एक से अधिक पेपर नहीं दिया है तो पूरी राशि वापस कर दी जाएगी।",
            "बेहतर होगा कि पहले कोई निःशुल्क पेपर देख लें — हर सीरीज़ बताती है कि उसके कौन-से पेपर बिना भुगतान दिए जा सकते हैं।",
          ],
        },
      },
      {
        h: { en: "After 7 days, or after two papers", hi: "7 दिन बाद, या दो पेपर बाद" },
        p: {
          en: [
            "We do not refund once the series has genuinely been used, because the papers and solutions cannot be returned.",
            "If something is actually wrong — a broken paper, a wrong answer key, access you paid for but never received — tell us. That is not a refund question, it is a mistake on our side and we will fix it or refund you regardless of the window.",
          ],
          hi: [
            "सीरीज़ का वास्तविक उपयोग हो जाने के बाद धन-वापसी नहीं होती, क्योंकि पेपर और समाधान लौटाए नहीं जा सकते।",
            "यदि सचमुच कुछ ग़लत है — ख़राब पेपर, ग़लत उत्तर-कुंजी, भुगतान के बाद भी न मिली पहुँच — तो हमें बताइए। यह धन-वापसी का प्रश्न नहीं, हमारी ग़लती है; हम उसे ठीक करेंगे या अवधि देखे बिना पैसा लौटाएँगे।",
          ],
        },
      },
      {
        h: { en: "How to ask, and how long it takes", hi: "कैसे कहें, और कितना समय लगेगा" },
        p: {
          en: [
            "Write to us with the email you paid from and the payment reference. There is no form to hunt for and no queue to survive.",
            "We reply within 2 working days. An approved refund goes back to the original payment method through Razorpay, and usually reaches you in 5–7 working days depending on your bank.",
            "Referral bonus credited into your wallet is not cash and is not refundable; it is reversed if the purchase behind it is refunded.",
          ],
          hi: [
            "जिस ईमेल से भुगतान किया, उससे भुगतान संदर्भ के साथ लिखिए। न कोई फ़ॉर्म खोजना है, न क़तार में लगना है।",
            "हम 2 कार्य-दिवस में उत्तर देते हैं। स्वीकृत धन-वापसी Razorpay के माध्यम से उसी भुगतान माध्यम में जाती है और आपके बैंक के अनुसार सामान्यतः 5–7 कार्य-दिवस में पहुँचती है।",
            "वॉलेट में जमा रेफ़रल बोनस नक़द नहीं है और वापसी योग्य नहीं है; उसके पीछे की खरीद वापस होने पर वह भी वापस ले लिया जाता है।",
          ],
        },
      },
    ],
  },

  /* ---------------------------------------------------------------- contact */
  contact: {
    title: { en: "Contact Us", hi: "संपर्क करें" },
    intro: {
      en: "A real person reads these. Write in Hindi or English, whichever is easier.",
      hi: "इन्हें एक असली व्यक्ति पढ़ता है। हिन्दी या अंग्रेज़ी — जो आसान लगे, उसी में लिखिए।",
    },
    blocks: [
      {
        h: { en: "For anything at all", hi: "किसी भी बात के लिए" },
        p: {
          en: [
            "Payments, access, refunds, a wrong answer key, a paper that would not open, or a suggestion — the same address reaches us.",
            "Tell us the email you signed up with, and the test name if it is about a paper. It saves a round of questions.",
          ],
          hi: [
            "भुगतान, पहुँच, धन-वापसी, ग़लत उत्तर-कुंजी, न खुलने वाला पेपर, या कोई सुझाव — सब एक ही पते पर आते हैं।",
            "जिस ईमेल से साइन अप किया वह बताइए, और पेपर की बात हो तो टेस्ट का नाम। इससे एक दौर के सवाल बच जाते हैं।",
          ],
        },
      },
    ],
  },
};
