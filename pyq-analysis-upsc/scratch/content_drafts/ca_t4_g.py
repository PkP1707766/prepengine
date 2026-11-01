# -*- coding: utf-8 -*-
"""Current Affairs · Test 4 (October to December 2026) -- part G: geography.

Each item takes a process in the news and asks why it happens: why glaciers that end in lakes shrink faster than those
that end on land. Written month by month: October 2026 first. No stem carries a date (design doc, section 7)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t4_format import FORMAT, POS

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
GM, CL = "Geomorphology", "Climatology"

# ---------------------------------------------------------------- October 2026

A(GM, "medium",
  "Glaciers that end in lakes tend to lose ice faster than comparable glaciers that end on land.",
  "झीलों में समाप्त होने वाले हिमनद प्रायः भूमि पर समाप्त होने वाले तुलनीय हिमनदों की अपेक्षा तेज़ी से बर्फ़ खोते हैं।",
  "Where a glacier ends in a lake, the water melts its front from below and blocks of ice break away into the lake.",
  "जहाँ कोई हिमनद झील में समाप्त होता है, वहाँ पानी उसके अग्रभाग को नीचे से पिघलाता है और बर्फ़ के खंड टूटकर झील में गिरते हैं।",
  0,
  "Both statements are correct, and Statement II explains Statement I. A glacier that ends on land loses ice mainly by melting at its surface. One that ends in a lake loses it in two more ways: lake water, warmer than the ice, melts the submerged front, and the undercut front breaks off in blocks -- calving -- into the lake; as the tongue thins it can begin to float, which speeds the break-up. Studies of the Himalaya have found lake-terminating glaciers thinning and retreating faster than land-terminating ones nearby. "
  "The process feeds itself, because a retreating glacier lengthens the lake in front of it, and it matters for hazards: the lakes, often dammed only by loose moraine, are the source of glacial lake outburst floods, so their growth is watched by satellite.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। भूमि पर समाप्त होने वाला हिमनद मुख्यतः अपनी सतह के पिघलने से बर्फ़ खोता है। झील में समाप्त होने वाला दो और तरीक़ों से खोता है: बर्फ़ से अधिक गर्म झील का पानी डूबे हुए अग्रभाग को पिघलाता है, और नीचे से कटा अग्रभाग खंडों में टूटकर -- हिमखंड-विच्छेदन, यानी काल्विंग -- झील में गिरता है; जीभ पतली होने पर वह तैरने लगती है, जिससे टूटना और तेज़ होता है। हिमालय के अध्ययनों में झील में समाप्त होने वाले हिमनद पास के भूमि पर समाप्त होने वालों से तेज़ी से पतले होते और पीछे हटते पाए गए हैं। "
  "यह प्रक्रिया स्वयं को बढ़ाती है, क्योंकि पीछे हटता हिमनद अपने आगे की झील को लंबा करता जाता है, और यह आपदाओं के लिए महत्त्वपूर्ण है: प्रायः ढीले हिमोढ़ से बँधी ये झीलें हिमनद झील विस्फोट बाढ़ों का स्रोत हैं, इसलिए उनकी वृद्धि पर उपग्रह से नज़र रखी जाती है।",
  "King, O. et al., 'Glacial lakes exacerbate Himalayan glacier mass loss', Scientific Reports 9 (2019); National Disaster Management Authority, Guidelines on Management of Glacial Lake Outburst Floods (2020); NCERT, Fundamentals of Physical Geography (Class XI), glaciers.",
  "ca-t4-geo-lake-terminating-glaciers-calving-faster-loss", craft="inference")

finish("ca_t4_g.sql", FORMAT, "2026-Q4", update="--update" in sys.argv)
