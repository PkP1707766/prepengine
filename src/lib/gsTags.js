/* ============================================================
   GS THEMES: cross-cutting tags beside the syllabus

   A syllabus topic files each GS question in one place. A theme
   cuts across papers and topics: every question on Article 21,
   on women, on climate change or on China, wherever the
   syllabus puts it. Themes are read from the question's own
   words, so a new PYQ joins its themes the moment it is added,
   with no tagging to keep up.

   Each pattern is tested on the English question. Patterns are
   kept tight on purpose: a theme that catches stray words
   ("power", "space", "learn") is worse than one that misses.
   ============================================================ */

export const GS_TAGS = [
  // Polity and governance
  { id: "fundamental-rights", en: "Fundamental Rights", hi: "मौलिक अधिकार", re: /fundamental rights?|article (1[4-9]|2[0-9]|3[0-2])\b|right to (equality|privacy|life|freedom)|freedom of (speech|expression|religion)|right of movement/i },
  { id: "constitution-amendments", en: "Amendments & Basic Structure", hi: "संविधान संशोधन एवं मूल ढाँचा", re: /amendment|basic structure|article 368/i },
  { id: "supreme-court", en: "Courts & Landmark Judgments", hi: "न्यायालय एवं ऐतिहासिक निर्णय", re: /supreme court|high courts?|judgement|judgment|judicial (review|activism|legislation|independence)|collegium|judges|judiciary|tribunals?\b|public interest (litigation|petitions?)/i },
  { id: "parliament", en: "Parliament & Legislatures", hi: "संसद एवं विधानमंडल", re: /parliament|lok sabha|rajya sabha|legislative councils?|state legislature|speaker\b|ordinances?\b|standing committees?|estimates committee|public accounts committee/i },
  { id: "elections", en: "Elections & Political Parties", hi: "चुनाव एवं राजनीतिक दल", re: /election|electoral|representation of (the )?peoples?'? act|model code of conduct|political part(y|ies)|party system|evm\b|electronic voting/i },
  { id: "federalism", en: "Centre-State Relations", hi: "केंद्र-राज्य संबंध", re: /federal|centre-state|centre and (the )?states?|governor|state autonomy|finance commission|inter-state|article 370/i },
  { id: "local-government", en: "Panchayats & Cities", hi: "पंचायत एवं नगरीय निकाय", re: /panchayat|local (self-)?government|local bodies|local institutions|municipal|73rd|74th|gram sabha/i },
  { id: "civil-services", en: "Civil Services & Bureaucracy", hi: "सिविल सेवा एवं नौकरशाही", re: /civil serv|bureaucra|public servants?|public officials?|permanent executive|administrative reforms/i },
  { id: "transparency", en: "Transparency & Accountability", hi: "पारदर्शिता एवं जवाबदेही", re: /right to information|\brti\b|transparen|accountab|citizens'? charter|social audit|whistle-?blow|official secrets/i },
  { id: "corruption-probity", en: "Corruption & Probity", hi: "भ्रष्टाचार एवं सत्यनिष्ठा", re: /corrupt|bribe|probity|integrity|conflict of interest|nepotism/i },
  { id: "regulators-bodies", en: "Commissions & Regulators", hi: "आयोग एवं नियामक", re: /commission for|commission of india|\bcag\b|comptroller|attorney-general|human rights commission|\bncw\b|\bncsc\b|niti aayog|election commission|cbi\b|central bureau/i },

  // Society
  { id: "women", en: "Women & Gender", hi: "महिलाएँ एवं लैंगिक मुद्दे", re: /women|woman|gender|girls?\b|feminis|patriarch|sexual harassment/i },
  { id: "children", en: "Children & Youth", hi: "बच्चे एवं युवा", re: /child|juvenile|young people|youth|adolescent/i },
  { id: "tribals", en: "Tribals & Adivasis", hi: "जनजातियाँ एवं आदिवासी", re: /tribal|scheduled tribes?|adivasi|\bsts\b/i },
  { id: "caste", en: "Caste & Social Justice", hi: "जाति एवं सामाजिक न्याय", re: /caste|scheduled castes?|dalit|backward class|reservation|social justice/i },
  { id: "secularism-communalism", en: "Religion, Secularism & Communalism", hi: "धर्म, पंथनिरपेक्षता एवं सांप्रदायिकता", re: /secular|communal|religio|minorit|sect\b/i },
  { id: "population-demography", en: "Population & Migration", hi: "जनसंख्या एवं प्रवासन", re: /population|demographic|migra(nt|tion)|ageing|elderly|senior citizens|life expectancy/i },
  { id: "poverty-hunger", en: "Poverty, Hunger & Nutrition", hi: "गरीबी, भुखमरी एवं पोषण", re: /poverty|poor\b|hunger|malnutrition|food security|public distribution|food grain distribution|\bpds\b|welfare schemes?/i },
  { id: "health", en: "Health", hi: "स्वास्थ्य", re: /health|hospital|medic|pandemic|covid|vaccin|disease|stem cell|telemedicine/i },
  { id: "education-skills", en: "Education & Skills", hi: "शिक्षा एवं कौशल", re: /education|school|universit|college|skill|vocational|literacy|illiteracy|human (development|capital|resources?)/i },
  { id: "urbanisation", en: "Cities & Urbanisation", hi: "शहर एवं नगरीकरण", re: /urban|\bcit(y|ies)\b|smart cit|tier[- ]2|metropol/i },
  { id: "globalisation", en: "Globalisation & Culture", hi: "वैश्वीकरण एवं संस्कृति", re: /globali[sz]|cultural (diversity|values|identity|homogeni)|westerni[sz]/i },

  // History and culture
  { id: "freedom-struggle", en: "Freedom Struggle", hi: "स्वतंत्रता संग्राम", re: /freedom (struggle|movement)|national(ist)? movement|struggle for freedom|moderates|quit india|non-cooperation|civil disobedience|1857|uprising|indian national congress|swadeshi/i },
  { id: "colonial-rule", en: "Colonial Rule & Its Impact", hi: "औपनिवेशिक शासन एवं प्रभाव", re: /colonial|british|east india company|curzon|indentured|famines/i },
  { id: "art-architecture", en: "Art, Architecture & Literature", hi: "कला, स्थापत्य एवं साहित्य", re: /\bart\b|artform|architecture|sculpture|temple|stupa|painting|rock-cut|numismatic|literature|literary|heritage|monuments?/i },
  { id: "religion-philosophy", en: "Bhakti, Buddhism & Indian Thought", hi: "भक्ति, बौद्ध धर्म एवं भारतीय चिंतन", re: /bhakti|buddh|jain|sufi|vedic|upanishad|indian philosophy|chaitanya|renaissance/i },
  { id: "gandhi", en: "Mahatma Gandhi", hi: "महात्मा गांधी", re: /gandhi/i },

  // Geography, environment and disasters
  { id: "climate-change", en: "Climate Change", hi: "जलवायु परिवर्तन", re: /climate change|global warming|greenhouse|carbon|net[- ]zero|\bcop\s?-?2\d|kyoto|paris agreement|glaciers?|green grid/i },
  { id: "water", en: "Water & Rivers", hi: "जल एवं नदियाँ", re: /water|river|groundwater|irrigation|watershed|drought|wetland|interlinking|\bdams?\b/i },
  { id: "disasters", en: "Disasters", hi: "आपदाएँ", re: /disaster|landslide|earthquake|cyclone|flood|tsunami|cloudburst|\bndma\b|sendai|hyogo|volcan/i },
  { id: "environment", en: "Environment & Biodiversity", hi: "पर्यावरण एवं जैव विविधता", re: /biodiversity|forest|ramsar|wildlife|mangrove|coral|\beia\b|environment impact|pollution|smog|air quality|clean air|solid waste|desertification|ecolog|ecosystem/i },
  { id: "oceans", en: "Oceans & Coasts", hi: "महासागर एवं तट", re: /ocean|sea\b|marine|coast|salinity|straits?\b|isthmus|maritime|arctic|antarctic/i },
  { id: "energy", en: "Energy", hi: "ऊर्जा", re: /energy|solar|nuclear|renewable|\bcoal\b|\boil\b|petroleum|natural gas|electricity|hydrogen|\bleds?\b|\bfuels?\b/i },

  // Economy
  { id: "agriculture", en: "Agriculture & Farmers", hi: "कृषि एवं किसान", re: /agricultur|farm|crop|\bmsp\b|minimum support price|horticulture|millets|pulses|organic state|food processing|fisher|pisciculture|blue revolution/i },
  { id: "land", en: "Land & Land Reforms", hi: "भूमि एवं भूमि सुधार", re: /land reforms?|land ceiling|land acquisition|land records|land holdings?|tenancy|zamindari/i },
  { id: "fiscal-tax", en: "Budget, Taxes & GST", hi: "बजट, कर एवं जीएसटी", re: /budget|fiscal|\btax|\bgst\b|goods and services tax|public expenditure|finance commission|subsid/i },
  { id: "banking-money", en: "Banking, Money & Inflation", hi: "बैंकिंग, मुद्रा एवं मुद्रास्फीति", re: /bank|monetary|inflation|currency|financial inclusion|jan-dhan|micro-?financ|cryptocurrency|e-rupee|savings rate/i },
  { id: "growth-jobs", en: "Growth & Jobs", hi: "विकास एवं रोज़गार", re: /\bgdp\b|growth|employment|jobs?\b|labour|unemploy|gig economy|inclusive growth|informal/i },
  { id: "industry-infra", en: "Industry & Infrastructure", hi: "उद्योग एवं अवसंरचना", re: /industr|manufactur|infrastructure|public[- ]private|\bppp\b|railway|airports?|\broads?\b|\bports?\b|corridor|gati[- ]shakti|investment/i },
  { id: "trade", en: "Trade & the WTO", hi: "व्यापार एवं डब्ल्यूटीओ", re: /\btrade\b|\bwto\b|exports?|imports?|protectionism|doha/i },

  // Science and technology
  { id: "digital-cyber", en: "Digital India & Cyber", hi: "डिजिटल भारत एवं साइबर", re: /digital|e-governance|internet|online|cyber|social media|data (security|protection)|information and communication technology|\bict\b/i },
  { id: "space-defence-tech", en: "Space, Defence & Frontier Tech", hi: "अंतरिक्ष, रक्षा एवं उन्नत प्रौद्योगिकी", re: /space (station|mission|programme|science|technology|telescope)|isro|satellite|chandrayaan|moon mission|lunar|mars orbit|asteroid|navigation|nanotech|biotech|artificial intelligence|\bai\b|quantum|semiconductor|missile|s-400|drone/i },

  // Security and international relations
  { id: "terrorism-extremism", en: "Terrorism & Extremism", hi: "आतंकवाद एवं उग्रवाद", re: /terror|insurg|extremis|naxal|militan|left[- ]wing|\blwe\b|\buapa\b|radicali|over-ground workers|internal security/i },
  { id: "borders-crime", en: "Borders & Organised Crime", hi: "सीमाएँ एवं संगठित अपराध", re: /border|infiltrat|cross-border|smuggl|drug|narcotic|money laundering|organi[sz]ed crime|illicit/i },
  { id: "china", en: "China", hi: "चीन", re: /china|chinese|cpec|belt (and|one) road/i },
  { id: "neighbourhood", en: "Neighbourhood", hi: "पड़ोसी देश", re: /pakistan|nepal|bangladesh|sri lanka|bhutan|myanmar|maldives|afghanistan|saarc|bimstec|neighbour/i },
  { id: "usa-west", en: "USA, Europe & Russia", hi: "अमेरिका, यूरोप एवं रूस", re: /\busa\b|united states|america|washington|europe|russia|ukraine|indo-us|france|britain/i, cs: /\b(US|UK)\b/ },
  { id: "global-bodies", en: "UN & Global Groupings", hi: "संयुक्त राष्ट्र एवं वैश्विक समूह", re: /united nations|unesco|ecosoc|world bank|world health organi[sz]ation|brics|aukus|i2u2|asean|ashgabat|shanghai cooperation|quadrilateral security/i, cs: /\b(UN|WHO|IMF|G-?20|SCO|Quad|QUAD)\b/ },
  { id: "diaspora", en: "Indian Diaspora", hi: "भारतीय प्रवासी", re: /diaspora/i },

  // Ethics (GS IV)
  { id: "thinkers", en: "Thinkers & Leaders", hi: "चिंतक एवं नेता", re: /kautilya|gandhi|buddha|vivekanand|tagore|ambedkar|kalam|plato|aristotle|kant\b|socrates|rawls|weber|confucius|tirukkural|lincoln|napoleon|mandela|dalai lama|einstein/i },
  { id: "emotional-intelligence", en: "Emotional Intelligence", hi: "भावनात्मक बुद्धिमत्ता", re: /emotional intelligence|empathy|compassion|anger|stress/i },
  { id: "conscience-dilemmas", en: "Conscience & Ethical Dilemmas", hi: "अंतरात्मा एवं नैतिक दुविधाएँ", re: /conscience|ethical dilemma|dilemmas|moral (obligation|responsibility)|means and ends|ends justify/i },
  { id: "corporate-ethics", en: "Business & Corporate Ethics", hi: "व्यावसायिक एवं कॉर्पोरेट नैतिकता", re: /corporate|company|companies|\bcsr\b|business|industrialist/i },
];

const BY_ID = new Map(GS_TAGS.map((tg) => [tg.id, tg]));
export const gsTag = (id) => BY_ID.get(id) || null;

/** The theme ids a question belongs to, read from its English text. */
export function gsTagsOf(text) {
  const s = String(text || "");
  return GS_TAGS.filter((tg) => tg.re.test(s) || (tg.cs && tg.cs.test(s))).map((tg) => tg.id);
}
