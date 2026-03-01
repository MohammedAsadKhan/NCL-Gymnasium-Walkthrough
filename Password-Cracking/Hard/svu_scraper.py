#!/usr/bin/env python3
# SVU Episode Wordlist Generator
# Run this on Kali: python3 svu_scraper.py
# Requires: pip install requests beautifulsoup4 --break-system-packages

import requests
from bs4 import BeautifulSoup
import time
import re
import sys

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

season_urls = [
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_1",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_2",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_3",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_4",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_5",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_6",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_7",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_8",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_9",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_10",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_11",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_12",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_13",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_14",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_15",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_16",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_17",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_18",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_19",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_20",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_21",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_22",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_23",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_24",
    "https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit_season_25",
]

all_titles = []
total_episodes = 0

print("Scraping SVU episode titles from Wikipedia...")
print("=" * 50)

for url in season_urls:
    season_num = url.split("season_")[1]
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Episode titles sit in td.summary inside the wikiepisodetable
        titles = soup.select('td.summary')
        season_titles = []
        for t in titles:
            title = t.get_text(strip=True)
            # Strip surrounding quotes (Wikipedia uses " and ")
            title = title.strip('"').strip('\u201c').strip('\u201d').strip('"').strip("'").strip()
            if title and len(title) > 1:
                season_titles.append(title)

        all_titles.extend(season_titles)
        total_episodes += len(season_titles)
        print(f"Season {season_num:>2}: {len(season_titles)} episodes scraped")
        time.sleep(0.4)  # be polite to Wikipedia

    except Exception as ex:
        print(f"Season {season_num:>2}: ERROR - {ex}", file=sys.stderr)

print("=" * 50)
print(f"Total episodes collected: {total_episodes}")

# Now build the wordlist:
# Split each title into individual words, lowercase, remove punctuation, deduplicate
words = set()
for title in all_titles:
    # Split on spaces and hyphens
    parts = re.split(r'[\s\-]+', title)
    for word in parts:
        # Strip punctuation from word edges
        word = re.sub(r"[^a-zA-Z0-9]", "", word)
        word = word.lower()
        if len(word) > 1:  # skip single letters like 'a', 'i'
            words.add(word)

# Sort and write to file
sorted_words = sorted(words)
with open("svu.txt", "w") as f:
    for word in sorted_words:
        f.write(word + "\n")

print(f"Unique words written to svu.txt: {len(sorted_words)}")
print("\nDone! Now run:")
print("  hashcat hash.txt -m 0 -a 6 svu.txt ?d?d")
