# -*- coding: utf-8 -*-
"""Compare a batch's local checksum manifest with the md5s read back from the DB.
Usage: python compare_md5.py <manifest.json> <db_md5.json>"""
import json, sys
local = json.load(open(sys.argv[1])); db = json.load(open(sys.argv[2]))
same = [k for k in local if db.get(k) == local[k]]
diff = [k for k in local if k in db and db[k] != local[k]]
missing = [k for k in local if k not in db]
print(f"rows in batch: {len(local)} | identical in DB: {len(same)} | differ: {len(diff)} {diff} | missing: {len(missing)} {missing}")
sys.exit(0 if len(same) == len(local) else 1)
