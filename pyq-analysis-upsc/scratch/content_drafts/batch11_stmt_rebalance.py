# -*- coding: utf-8 -*-
"""Rebalance the History statement_based answer key: flip true statements to false traps so the
'how many correct' answers stop clustering on 'Only two'. Each UPDATE is guarded on the old text."""
import json, os

def q(s):
    return "'" + s.replace("'", "''") + "'"

OPTS = ["Only one", "Only two", "All three", "None"]
def opts_json(i):
    return json.dumps([{"id": "abcd"[k], "body": b, "isCorrect": k == i} for k, b in enumerate(OPTS)])

ONE, TWO, ALL, NONE = 0, 1, 2, 3

# cg -> (answer_idx, [(stmt_idx, old_prefix, new_text)], explanation)
R = {}

# ---------------- HARD: Only two -> Only one ----------------
R["ancient-gandhara-mathura-art-schools"] = (ONE, [(1, "The Mathura school of art developed", "The Mathura school of art is generally considered to show stronger Hellenistic influence than the Gandhara school.")],
 "Only statement 1 is correct: Gandhara art, which flourished under Kushan patronage, shows strong Hellenistic/Greco-Roman influence in its depiction of the Buddha. Statement 2 reverses the comparison: it is the Mathura school that developed largely indigenously and shows more native Indian stylistic elements, while Gandhara is the more Hellenistic of the two. Statement 3 is incorrect: the schools used different materials -- Gandhara sculptures were typically carved from grey or bluish-grey schist, Mathura sculptures from red sandstone.")
R["ancient-harsha-religious-patronage"] = (ONE, [(1, "He also convened a quinquennial", "He also convened a quinquennial (once-in-five-years) assembly at Nalanda for the distribution of charity.")],
 "Only statement 1 is correct: Harsha convened the Kannauj assembly associated with Mahayana Buddhism, as recorded by Xuanzang. Statement 2 misplaces the venue: the quinquennial charity assembly was held at Prayaga (Allahabad), not Nalanda. Statement 3 is incorrect: Harsha's patronage was eclectic, extending to Shaivism and other Brahmanical traditions as well as Buddhism -- reflected even in his own plays, which invoke Shaiva themes.")
R["ancient-mauryan-decline-shunga"] = (ONE, [(1, "The last Mauryan ruler, Brihadratha", "The last Mauryan ruler, Brihadratha, was assassinated by his own commander-in-chief, Pushyamitra Shunga, who then founded the Kanva dynasty.")],
 "Only statement 1 is correct: the empire weakened after Ashoka and reportedly fragmented among successors including Dasaratha and Samprati. Statement 2 names the wrong dynasty: after assassinating Brihadratha, Pushyamitra Shunga founded the Shunga dynasty -- the Kanva dynasty came later, succeeding the Shungas. Statement 3 is incorrect: Pushyamitra is traditionally associated with a Brahmanical revival, and some Buddhist sources (such as the Divyavadana) allege hostility toward Buddhism under his rule.")
R["medieval-akbar-sulh-i-kul-ibadat-khana"] = (ONE, [(1, "The Ain-i-Akbari, part of the Akbarnama", "The Ain-i-Akbari, a detailed administrative and statistical account of Akbar's empire, was compiled by Abdul Qadir Badauni.")],
 "Only statement 1 is correct: Sulh-i-Kul and Din-i-Ilahi are related but distinct. Statement 2 misattributes the work: the Ain-i-Akbari was compiled by Abul Fazl as part of the Akbarnama, whereas Abdul Qadir Badauni wrote the Muntakhab-ut-Tawarikh, a separate and often critical chronicle. Statement 3 is incorrect: Akbar personally took part in the interfaith discussions at the Ibadat Khana in Fatehpur Sikri.")
R["medieval-shivaji-maratha-administration"] = (ONE, [(0, "Shivaji's coronation in 1674", "Shivaji's coronation in 1674 at Raigad involved a formal Vedic ceremony, presided over by the Peshwa Moropant Pingle.")],
 "Only statement 2 is correct: Aurangzeb's prolonged Deccan campaigns are widely regarded as having drained Mughal resources. Statement 1 names the wrong officiant: Shivaji's 1674 Raigad coronation was presided over by the Brahmin scholar Gaga Bhatt, not by the Peshwa Moropant Pingle. Statement 3 is incorrect: Ashtapradhan positions were generally appointive rather than hereditary, made at the king's discretion on merit.")
R["modern-cripps-mission-1942"] = (ONE, [(0, "The Cripps Mission offered Dominion Status", "The Cripps Mission offered Dominion Status to India with immediate effect, along with full Indian control of the defence portfolio.")],
 "Only statement 3 is correct: Gandhi described the Cripps proposals as 'a post-dated cheque on a crashing bank.' Statement 1 is incorrect: the Mission offered Dominion Status after the war, not with immediate effect, and the British retained control of defence during the war -- the refusal to transfer defence was a key sticking point. Statement 2 is incorrect: the Congress also rejected the proposals, chiefly over the provincial opt-out clause and the defence question.")
R["modern-gandhi-irwin-pact-1931"] = (ONE, [(0, "Under the Pact, the Congress agreed", "Under the Pact, the Congress agreed to suspend the Civil Disobedience Movement and boycott the Second Round Table Conference.")],
 "Only statement 3 is correct: the Pact permitted limited duty-free salt manufacture for personal consumption near the coast. Statement 1 is incorrect: under the Pact the Congress agreed to suspend Civil Disobedience and to participate in the Second Round Table Conference, not boycott it. Statement 2 is incorrect: the release of prisoners did not extend to those convicted of violent revolutionary acts -- Bhagat Singh, Sukhdev and Rajguru were executed in March 1931.")

# ---------------- HARD: Only two -> None ----------------
R["ancient-sangam-polity-economy"] = (NONE, [
 (0, "Alongside the three major Sangam", "The Velir were the three major crowned dynasties of the Sangam Age, ruling the Chera, Chola and Pandya kingdoms."),
 (1, "The Sangam-age economy is understood", "The Sangam-age economy was largely isolated from overseas trade, with no material evidence of contact with the Roman world.")],
 "None of the statements is correct. Statement 1 confuses the categories: the three major dynasties were the Cheras, Cholas and Pandyas, while the Velir were minor chieftains existing alongside them. Statement 2 is contradicted by the evidence: Indo-Roman trade was significant, attested by Roman coins at sites such as Arikamedu. Statement 3 is incorrect: Sangam society had its own distinct social classifications rather than a rigid, uniform four-fold varna order.")
R["modern-interim-government-1946"] = (NONE, [
 (0, "The Interim Government was formed in September 1946", "The Interim Government was formed in September 1946, with Sardar Vallabhbhai Patel as Vice-President of the Executive Council."),
 (2, "Liaquat Ali Khan, of the Muslim League", "Liaquat Ali Khan, of the Muslim League, held the home portfolio in the Interim Government after the League joined it.")],
 "None of the statements is correct. Statement 1 swaps the officeholder: Jawaharlal Nehru, not Vallabhbhai Patel, was Vice-President of the Executive Council of the Interim Government (September 1946). Statement 2 is incorrect: the Muslim League initially refused to join, entering only in October 1946, and adopted an obstructionist stance. Statement 3 swaps the portfolio: Liaquat Ali Khan held Finance, while Home was held by Patel.")
R["modern-revolutionary-movements-hsra"] = (NONE, [
 (0, "The Anushilan Samiti had its origins", "The Anushilan Samiti had its origins in Punjab, and the Jugantar group was a breakaway faction based in Lahore."),
 (1, "The Chittagong Armoury Raid (1930)", "The Chittagong Armoury Raid (1930) was led by Chandrashekhar Azad and aimed to seize government armouries in Bengal.")],
 "None of the statements is correct. Statement 1 misplaces the origins: the Anushilan Samiti originated in Bengal and split into the Calcutta and Jugantar factions. Statement 2 misattributes the raid: the 1930 Chittagong Armoury Raid was led by Surya Sen, not Chandrashekhar Azad. Statement 3 reverses the actual sequence: the organisation was founded in 1924 as the Hindustan Republican Association and renamed the Hindustan Socialist Republican Association only in 1928.")
R["modern-second-round-table-conference-1931"] = (NONE, [
 (0, "Mahatma Gandhi attended the Second Round", "Mahatma Gandhi attended the Second Round Table Conference in London alongside Jawaharlal Nehru and Sardar Patel as Congress delegates."),
 (2, "The Conference ultimately failed largely", "The Conference ultimately collapsed because Mahatma Gandhi walked out of it over the question of the salt tax.")],
 "None of the statements is correct. Statement 1 is incorrect: Gandhi attended as the sole representative of the Congress, not alongside Nehru and Patel. Statement 2 is incorrect: the Conference failed to resolve the communal question. Statement 3 is incorrect: the Conference broke down chiefly over that unresolved communal question, not because Gandhi walked out over the salt tax.")

# ---------------- MEDIUM: All three -> Only one ----------------
R["modern-dandi-march-1930"] = (ONE, [
 (0, "Mahatma Gandhi began the Dandi March", "Mahatma Gandhi began the Dandi March from Sevagram Ashram, Wardha."),
 (2, "The movement was formally suspended", "The movement was formally suspended after the Poona Pact of 1932, following which the Congress participated in the First Round Table Conference.")],
 "Only statement 2 is correct: the march covered roughly 240 miles over 24 days, from 12 March to 6 April 1930. Statement 1 is incorrect: Gandhi began from Sabarmati Ashram, not Sevagram (the Wardha ashram he settled in later). Statement 3 is incorrect on both counts: the movement was suspended after the Gandhi-Irwin Pact of 1931, not the Poona Pact of 1932, and Gandhi then attended the Second, not the First, Round Table Conference.")
R["medieval-vijayanagara-empire"] = (ONE, [
 (0, "The Vijayanagara Empire was founded", "The Vijayanagara Empire was founded in 1436 by Harihara and Bukka, traditionally said to have been guided by the sage Vidyaranya."),
 (2, "The Vijayanagara Empire suffered", "The Vijayanagara Empire suffered a decisive defeat at the Battle of Talikota (1565) at the hands of the Mughal emperor Akbar.")],
 "Only statement 2 is correct: the Vijayanagara Empire reached its zenith under Krishnadevaraya of the Tuluva dynasty. Statement 1 gives the wrong date: the empire was founded in 1336 by Harihara and Bukka, not 1436. Statement 3 names the wrong victors: the defeat at Talikota (1565) was inflicted by a confederacy of Deccan Sultanates, not by the Mughals.")
R["modern-lucknow-pact-1916"] = (ONE, [
 (1, "Under the Pact, the Congress accepted", "Under the Pact, the Congress rejected the principle of separate electorates for Muslims, and the League accepted joint electorates."),
 (2, "The Pact was signed at joint sessions", "The Pact was signed at joint sessions of both parties held at Bombay, marking a rare period of Hindu-Muslim political unity before independence.")],
 "Only statement 1 is correct: the Lucknow Pact (1916) was an agreement between the Congress and the Muslim League. Statement 2 reverses the terms: the Congress accepted the League's demand for separate electorates for Muslims. Statement 3 misplaces the venue: the joint sessions were held at Lucknow, not Bombay.")

# ---------------- MEDIUM: Only two -> Only one ----------------
R["modern-rowlatt-act-1919"] = (ONE, [(1, "It was passed based on the recommendations", "It was passed based on the recommendations of a committee headed by Sir John Simon.")],
 "Only statement 1 is correct: the Rowlatt Act allowed detention without trial for suspected political offenders. Statement 2 names the wrong chairman: the committee was headed by Sir Sidney Rowlatt, not Sir John Simon (whose Commission came later, in 1927-28). Statement 3 is incorrect: every elected Indian member of the Imperial Legislative Council voted against the Bill; it passed only because of the official (British) majority.")
R["modern-august-offer-1940"] = (ONE, [(0, "It was made by Viceroy", "It was made by Viceroy Lord Wavell.")],
 "Only statement 2 is correct: the August Offer promised eventual Dominion Status and an expanded, more representative Executive Council. Statement 1 names the wrong Viceroy: it was made by Lord Linlithgow, not Lord Wavell. Statement 3 is incorrect: the Congress rejected the Offer as inadequate, and the League's response was qualified rather than one of full acceptance.")
R["modern-cabinet-mission-1946"] = (ONE, [(1, "It categorically rejected", "It accepted the demand for a separate, sovereign state of Pakistan.")],
 "Only statement 1 is correct: the Plan proposed a weak Union (defence, foreign affairs, communications) with provinces grouped into three sections. Statement 2 is the opposite of the Plan's stance: it rejected a separate sovereign Pakistan, offering grouping and provincial autonomy instead. Statement 3 is incorrect: neither party accepted it without reservations -- the League later withdrew acceptance and called Direct Action Day, and Congress objected to the compulsory grouping clauses.")
R["modern-communal-award-1932"] = (ONE, [(0, "It was announced by British Prime Minister", "It was announced by Viceroy Lord Willingdon.")],
 "Only statement 2 is correct: the Award extended separate electorates to the Depressed Classes for the first time. Statement 1 names the wrong announcer: the Communal Award was announced by British Prime Minister Ramsay MacDonald in August 1932, not by the Viceroy. Statement 3 is incorrect: Gandhi strongly opposed separate electorates for the Depressed Classes and fasted against them, leading to the Poona Pact.")
R["modern-direct-action-day-1946"] = (ONE, [(1, "It led to widespread communal violence", "It led to widespread communal violence, most severely in Bombay, an event remembered as 'The Great Bombay Killings'.")],
 "Only statement 1 is correct: Direct Action Day (16 August 1946) was called by the Muslim League to press its Pakistan demand. Statement 2 misplaces the violence: it was worst in Calcutta -- the 'Great Calcutta Killings' -- not Bombay. Statement 3 reverses the sequence: it was the Muslim League that withdrew its earlier acceptance of the Cabinet Mission Plan, not a case of Congress rejecting the Plan.")
R["modern-ilbert-bill-1883"] = (ONE, [(0, "It sought to allow Indian judges", "It sought to allow Indian judges to try British subjects in criminal cases, and was introduced during the viceroyalty of Lord Curzon.")],
 "Only statement 3 is correct: European opposition to the Bill and the organised Indian response it provoked are cited among the factors behind the Congress's formation in 1885. Statement 1 names the wrong Viceroy: the Bill was introduced under Lord Ripon, not Lord Curzon. Statement 2 is incorrect: the Bill was passed in 1884 in a modified, compromise form, not withdrawn entirely.")
R["medieval-akbar-administration"] = (ONE, [(2, "Akbar abolished the pilgrimage tax", "Akbar reimposed the pilgrimage tax and the jizya (a tax on non-Muslims) in the later part of his reign.")],
 "Only statement 1 is correct: Akbar introduced the Mansabdari system of zat and sawar ranks. Statement 2 is incorrect: Din-i-Ilahi attracted only a small number of court nobles and never became a mass religion. Statement 3 reverses Akbar's policy: he abolished the pilgrimage tax and the jizya, rather than reimposing them.")
R["medieval-alauddin-khalji-market-reforms"] = (ONE, [(1, "He established a dedicated department", "He established a dedicated department, the Diwan-i-Bandagan, to oversee market regulation and enforcement.")],
 "Only statement 1 is correct: Alauddin Khalji's market controls kept prices low and stable, chiefly to support his large army. Statement 2 names the wrong department: market regulation was administered through the Diwan-i-Riyasat, whereas the Diwan-i-Bandagan was a department for slaves set up later, under Firuz Shah Tughlaq. Statement 3 is incorrect: the strict controls were specific to his reign and largely lapsed after his death.")
R["medieval-bhakti-movement"] = (ONE, [(1, "Guru Nanak, founder of Sikhism", "Guru Nanak, founder of Sikhism, upheld caste distinctions and prescribed idol worship.")],
 "Only statement 1 is correct: Kabir preached Nirguna devotion critical of ritualism. Statement 2 reverses Guru Nanak's teaching: he preached the oneness of God and rejected caste distinctions and idol worship. Statement 3 is incorrect: the Bhakti tradition has deep South Indian roots, with the Alvars and Nayanars composing devotional poetry centuries before the North Indian Bhakti saints.")
R["medieval-qutb-ud-din-aibak-delhi-sultanate"] = (ONE, [(2, "Iltutmish, Aibak", "Balban, Aibak's immediate successor, is credited with consolidating the Delhi Sultanate and organising the administrative system of Iqtas.")],
 "Only statement 1 is correct: Aibak, a former Mamluk of Muhammad Ghori, founded the Slave Dynasty. Statement 2 is incorrect: Aibak only began the Qutub Minar -- it was completed by Iltutmish. Statement 3 names the wrong ruler: the consolidation of the Sultanate and the organisation of the Iqta system are credited to Iltutmish; Balban ruled decades later (1266-87).")
R["ancient-ashoka-dhamma"] = (ONE, [(2, "The Ashokan edicts record", "The Rummindei pillar inscription commemorates Ashoka's visit to Bodh Gaya, the birthplace of the Buddha.")],
 "Only statement 1 is correct: Dhamma Mahamatras were special officers appointed to propagate and supervise Dhamma. Statement 2 is incorrect: Ashoka's Dhamma was a broad ethical code, not a demand for conversion to Buddhism. Statement 3 misplaces the site: the Rummindei pillar inscription commemorates Ashoka's visit to Lumbini, the Buddha's birthplace -- Bodh Gaya is where he attained enlightenment.")
R["ancient-harshavardhana"] = (ONE, [(0, "Harshavardhana's court was visited", "Harshavardhana's court was visited by the Chinese pilgrim Fa-Hien.")],
 "Only statement 3 is correct: Harsha's southward expansion was halted by Pulakeshin II of the Chalukyas at the Narmada. Statement 1 names the wrong pilgrim: it was Xuanzang who visited Harsha's court; Fa-Hien had visited India under Chandragupta II, about two centuries earlier. Statement 2 is incorrect: the Harshacharita was written by the court poet Banabhatta, not by Harsha, who is credited with plays such as Ratnavali, Priyadarshika and Nagananda.")
R["ancient-pallava-chalukya-architecture"] = (ONE, [(2, "The Chalukyas of Badami built", "The Chalukyas of Badami built temples at Aihole and Pattadakal exclusively in the Dravida style.")],
 "Only statement 1 is correct: the Pallavas pioneered the shift from rock-cut to structural temples, seen in the Shore Temple at Mahabalipuram. Statement 2 is incorrect: the Kailasanatha temple at Kanchipuram is associated with Narasimhavarman II (Rajasimha), not Narasimhavarman I. Statement 3 is incorrect: Aihole and Pattadakal are noted for showcasing both Nagara and Dravida styles, not the Dravida style exclusively.")

# ---------------- MEDIUM: Only two -> None ----------------
R["modern-swadeshi-movement-1905"] = (NONE, [
 (0, "It was launched as a direct reaction", "It was launched as a direct reaction to the Rowlatt Act of 1919."),
 (2, "The National Council of Education", "The National Council of Education was established during this movement to promote Western-style education under government control.")],
 "None of the statements is correct. Statement 1 names the wrong trigger: the movement was launched in 1905 in reaction to the partition of Bengal, not the Rowlatt Act of 1919. Statement 2 misattributes the song: 'Vande Mataram' was composed by Bankim Chandra Chatterjee in Anandamath, not by Tagore. Statement 3 reverses the purpose: the National Council of Education (1906) promoted technical and scientific education outside government control.")
R["modern-quit-india-1942"] = (NONE, [
 (0, "It was launched following the rejection", "It was launched following the failure of the Simon Commission."),
 (1, "Mahatma Gandhi gave the call", "Mahatma Gandhi gave the call 'Do or Die' at the Lahore session of the Congress.")],
 "None of the statements is correct. Statement 1 is incorrect: Quit India followed the failure of the Cripps Mission (1942), not the Simon Commission (1927-28). Statement 2 misplaces the venue: Gandhi's 'Do or Die' call was given at the AICC session in Bombay (Gowalia Tank Maidan), not Lahore. Statement 3 collapses two separate events: the Working Committee approved the resolution at Wardha in July 1942, but the mass movement was launched in August 1942.")
R["modern-vernacular-press-act-1878"] = (NONE, [
 (0, "It was enacted during the viceroyalty", "It was enacted during the viceroyalty of Lord Ripon."),
 (1, "It empowered the government", "It empowered the government to confiscate press material only after a trial in a court of law, with a right of appeal.")],
 "None of the statements is correct. Statement 1 names the wrong Viceroy: the Act was passed under Lord Lytton (1878), and it was Lord Ripon who repealed it in 1882. Statement 2 reverses its harshness: the Act allowed confiscation of press material with no right of appeal. Statement 3 is incorrect: it applied only to vernacular-language newspapers, exempting English-language papers.")
R["modern-govt-of-india-act-1935"] = (NONE, [
 (0, "It provided for the establishment", "It abandoned the idea of a federation and provided instead for a unitary state."),
 (1, "It introduced provincial autonomy", "It introduced dyarchy in the provinces for the first time.")],
 "None of the statements is correct. Statement 1 is incorrect: the Act proposed an All India Federation of provinces and princely states rather than a unitary state. Statement 2 is incorrect: dyarchy was introduced in the provinces by the 1919 Act; the 1935 Act ended it there (introducing it at the Centre) and granted provincial autonomy. Statement 3 is incorrect: the Federation never came into force because too few princely states acceded; only provincial autonomy took effect, in 1937.")
R["medieval-muhammad-bin-tughlaq-experiments"] = (NONE, [
 (0, "Muhammad bin Tughlaq shifted", "Muhammad bin Tughlaq shifted his capital from Delhi to Lahore."),
 (1, "He introduced a token currency", "He introduced a token currency of paper notes backed by the imperial treasury.")],
 "None of the statements is correct. Statement 1 names the wrong city: Muhammad bin Tughlaq shifted his capital to Daulatabad in the Deccan, not Lahore. Statement 2 misdescribes the token currency: he issued copper/bronze tokens intended to circulate at par with silver coins, not paper notes. Statement 3 is incorrect: both measures are generally regarded as failed administrative experiments.")

assert len(R) == 32, len(R)
tally = {}
for cg, (a, _, _) in R.items():
    tally[OPTS[a]] = tally.get(OPTS[a], 0) + 1
print("rewrites:", len(R), tally)

stmts = []
for cg, (ans, edits, expl) in R.items():
    qd = "question_data"
    for idx, old, new in edits:
        qd = "jsonb_set(%s, '{statements,%d}', to_jsonb(%s::text))" % (qd, idx, q(new))
    guards = " and ".join("left(question_data->'statements'->>%d, %d) = %s" % (idx, len(old), q(old)) for idx, old, _ in edits)
    stmts.append(
        "update public.questions set question_data = %s, options = %s::jsonb, explanation = %s, updated_at = now() "
        "where exam_category='upsc' and subject='History' and type='statement_based' and concept_group_id = %s and %s;"
        % (qd, q(opts_json(ans)), q(expl), q(cg), guards))

out = os.path.join(os.path.dirname(__file__), "batch11_rebalance.sql")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(stmts) + "\n")
print("wrote", out, sum(len(s) for s in stmts), "chars")
