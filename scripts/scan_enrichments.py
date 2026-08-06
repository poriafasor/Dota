#!/usr/bin/env python3
"""Scan enrichments.ts for invalid item/hero refs."""
import re, json, sys

# --- item ids ---
items_txt = open('src/data/items.ts', encoding='utf-8').read()
item_ids = set(re.findall(r"I\(\s*'([a-z_0-9]+)'", items_txt))
print(f"Items: {len(item_ids)}")

# --- hero ids ---
heroes_txt = open('src/data/heroes.ts', encoding='utf-8').read()
hero_ids = set(re.findall(r"id:\s*\"([a-z_0-9]+)\"", heroes_txt))
print(f"Heroes: {len(hero_ids)}")

# --- enrichments.ts ---
enr_txt = open('src/data/enrichments.ts', encoding='utf-8').read()

# role build arrays: "item_id" inside starting/early/mid/late/situational
# find all double-quoted tokens inside the file (enrichments uses double quotes)
all_tokens = set(re.findall(r'"([a-z_0-9]+)"', enr_txt))
# filter out non-id tokens (pure words like nothing match since regex requires lowercase+underscore+digits)
# we need to distinguish item ids vs hero ids vs other string literals (none expected in arrays)
# The support build arrays contain item ids; counters/goodAgainst contain hero ids.

bad_items = []
bad_heroes = []

# Parse support build arrays: starting/early/mid/late/situational: ["id","id",...]
for m in re.finditer(r'(starting|early|mid|late|situational):\s*\[([^\]]*)\]', enr_txt):
    arr = m.group(2)
    for tok in re.findall(r'"([a-z_0-9]+)"', arr):
        if tok not in item_ids:
            bad_items.append(tok)

# Parse counters/goodAgainst arrays
for m in re.finditer(r'(counters|goodAgainst):\s*\[([^\]]*)\]', enr_txt):
    arr = m.group(2)
    for tok in re.findall(r'"([a-z_0-9]+)"', arr):
        if tok not in hero_ids:
            bad_heroes.append(tok)

print(f"\nBad item refs in support builds: {len(bad_items)}")
if bad_items:
    from collections import Counter
    for tok, cnt in Counter(bad_items).most_common():
        print(f"  {tok} x{cnt}")
print(f"\nBad hero refs in counters/goodAgainst: {len(bad_heroes)}")
if bad_heroes:
    from collections import Counter
    for tok, cnt in Counter(bad_heroes).most_common():
        print(f"  {tok} x{cnt}")

sys.exit(1 if (bad_items or bad_heroes) else 0)
