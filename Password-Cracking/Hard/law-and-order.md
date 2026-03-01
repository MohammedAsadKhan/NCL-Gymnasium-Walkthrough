# Password Cracking Hard - Law & Order SVU

> **Category:** Password Cracking
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given 5 MD5 hashed passwords based on Law & Order: SVU episode titles, each followed by 2 digits. The challenge is building a wordlist from all 434+ episode titles, formatting it correctly, then running a hybrid attack to crack them.

> 🚨 "In the criminal justice system, cybersecurity-based offenses are considered especially serious. The dedicated detectives who investigate these password hashes are members of an elite squad known as the NCL. These are their walkthroughs."

> This one is called Hard but it's really just time consuming. The actual cracking command is simple. 90% of the work is building the wordlist correctly.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `hashcat` (pre-installed on Kali)
- `curl`, `grep`, `sed` (pre-installed on Kali)
- Wikipedia (source for episode list)

> 💡 If you get stuck at any point, follow the official NCL YouTube walkthrough: [Making Custom Wordlists for Password Cracking](https://www.youtube.com/watch?v=yr2wpxSQKKw&t=1031s). It covers the scraping and cracking process step by step.

---

## 📋 The Hashes

```
6475c851b56004eb96ab1404252c3a34
abe6591e06aafc3cf1b0783b120f685e
1e1612db8bdeebc7e8d56f8f30b39456
3dd9dd0e352df4433aadf2273e269287
08038f679de74982bfb9bac43d46271a
```

> 💡 **What the answers look like:** Each password is a single word from an SVU episode title (no spaces) in **all lowercase**, followed by exactly **2 digits**. For example, a password might look like `witness47` or `identity83`. Nothing uppercase, no special characters, just word + two numbers.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Confirm the Hash Type

All 5 are 32-character hex strings, so **MD5** (mode `-m 0`).

```bash
hashid 6475c851b56004eb96ab1404252c3a34
```

---

### Step 2 - Save the Hashes

```bash
cat > hash.txt << 'EOF'
6475c851b56004eb96ab1404252c3a34
abe6591e06aafc3cf1b0783b120f685e
1e1612db8bdeebc7e8d56f8f30b39456
3dd9dd0e352df4433aadf2273e269287
08038f679de74982bfb9bac43d46271a
EOF
```

---

### Step 3 - Build the SVU Episode Wordlist

This is the main challenge. You need a list of every word from every Law & Order: SVU episode title across all 25 seasons (434+ episodes total).

> ⚠️ AI-generated lists were tested and found to be incomplete. For the best results, use the included scraper script which pulls directly from Wikipedia.

A ready-to-run scraper script is included in this folder: `svu_scraper.py`

> 💡 If you need help getting the scraper set up and running, follow the official NCL YouTube walkthrough: [Making Custom Wordlists for Password Cracking](https://www.youtube.com/watch?v=yr2wpxSQKKw&t=1031s). It covers this exact process step by step.

Run the script:

```bash
python3 svu_scraper.py
```

The script will scrape all 25 seasons from Wikipedia and save the word list to `svu.txt`. When it finishes, you'll see a summary showing how many episodes were collected and how many unique words were written.

---

### Step 4 - Verify the Wordlist Was Created

Before running the crack, make sure the file actually got created and has content:

```bash
# Check the file exists and see how many words are in it
wc -l svu.txt
```

You should see several hundred words. If it shows 0 or the file doesn't exist, the scraper had an issue, re-run it or check your internet connection.

Peek at the contents to make sure it looks right:

```bash
# View the first 20 words
head -20 svu.txt

# View the last 20 words
tail -20 svu.txt

# Or scroll through the whole thing
cat svu.txt
```

You should see lowercase single words with no spaces or punctuation, things like `hooked`, `manhunt`, `philadelphia`, `resilience`. If you see full sentences or uppercase letters, something went wrong with the formatting step.

> 💡 Also verify that a few of the hint words are actually in your list before cracking. For example:
> ```bash
> grep "hooked" svu.txt
> grep "manhunt" svu.txt
> ```
> If both come back with results, your wordlist is good to go.

---

### Step 5 - Run the Hybrid Attack

This challenge uses a **hybrid attack** which combines a wordlist with a mask. Hashcat takes each word from your list and tries every 2-digit combination appended to it.

```bash
hashcat hash.txt -m 0 -a 6 svu.txt ?d?d
```

What each part does:
- `-m 0`: MD5 hash mode
- `-a 6`: hybrid attack mode (wordlist + mask)
- `svu.txt`: your episode word list
- `?d?d`: appends two digits (00 through 99) to every word

This tries combinations like `hooked00`, `hooked01`... `hooked99`, then moves to the next word. With a few hundred words and 100 digit combinations each, it runs through everything in seconds.

---

### Step 6 - View the Results

```bash
hashcat hash.txt -m 0 --show
```

Match each cracked password to its hash before submitting.

---

### Alternative - John the Ripper

John can do hybrid attacks too using the `--rule` option:

```bash
john --format=raw-md5 --wordlist=svu.txt --rule='Az"[0-9][0-9]"' hash.txt
john --show --format=raw-md5 hash.txt
```

---

## 💡 Hints (Without Giving It Away)

- `6475c851...` - Something a fish does, or what happens when someone gets addicted to something. Two digits in the 30s.
- `abe6591e...` - A word meaning a large organized search operation. Two digits in the 70s.
- `1e1612db...` - A city known for cheesesteaks and the Liberty Bell. Two digits in the 50s.
- `3dd9dd0e...` - A word meaning the ability to recover from hardship. Two digits, starts with 0.
- `08038f67...` - A word meaning unconventional or unusual. Two digits in the teens.

---

## ⚠️ Accuracy Tips

- ❌ **Don't use AI to generate the episode list.** It will miss episodes and some hashes won't crack. Scrape Wikipedia directly for completeness.
- ❌ **Don't skip the lowercase conversion.** Passwords are all lowercase and MD5 is case-sensitive. A capitalized word won't match.
- ❌ **Don't forget to remove spaces.** Episode titles have spaces but the passwords are single words. The `tr ' ' '\n'` step splits them properly.
- ✅ **Verify your wordlist has enough words** before cracking. A good scrape of the full series should give you 400+ unique words.
- ✅ **Match hash to password carefully** before submitting. Output order is not question order.

---

## 🧠 Why This Works

This challenge combines two skills: targeted wordlist creation and hybrid attacks. In real penetration testing, if you discover a company uses a naming convention like `[product_name][number]` for their passwords, you build a product list and run a hybrid attack exactly like this. The combination of a themed wordlist and a mask dramatically reduces the search space compared to brute force while still covering all the likely passwords. A generic wordlist would never crack these, but a domain-specific one with a mask cracks them in seconds.

---

## 🔗 Resources

- [NCL Tutorial Video - Custom Wordlists](https://www.youtube.com/watch?v=yr2wpxSQKKw&t=1031s)
- [Law & Order SVU Episodes - Wikipedia](https://en.wikipedia.org/wiki/Law_%26_Order:_Special_Victims_Unit)
- [Hashcat Hybrid Attack Documentation](https://hashcat.net/wiki/doku.php?id=hybrid_attack)

---

*Written by: Mo | Last updated: February 2026*
