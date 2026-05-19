import re
import json

with open('invocations.html', 'r') as f:
    html = f.read()

days = ['dimanche', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']

for day in days:
    # Find the block for the day
    m = re.search(r'    '+day+r': \{(.*?)\n    \},', html, re.DOTALL)
    if not m:
        print(f"Could not find {day}")
        continue
    block = m.group(1)
    
    # Extract the French text lines
    verses = re.findall(r"\{t:'v',n:\d+, tx:'(.*?)'\},", block)
    print(f"\n--- {day.upper()} ---")
    for i, v in enumerate(verses):
        print(f"V{i+1}: {v}")

