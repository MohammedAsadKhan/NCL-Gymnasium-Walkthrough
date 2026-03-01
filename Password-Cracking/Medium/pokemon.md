# Password Cracking Medium - Pokemon

> **Category:** Password Cracking
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given 5 MD5 hashed passwords that are all Pokémon names. Simple enough concept, except there are over 1000 Pokémon and you need to build your own wordlist to crack them.

> 🎮 Yes. The hackers used Pokémon names as their passwords. These are the people we're up against. Truly terrifying adversaries.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `hashcat` (pre-installed on Kali)
- `curl`, `grep`, `sed` (all pre-installed on Kali)
- Your favorite AI (for generating the Pokémon name list, more on this below)

---

## 📋 The Hashes

```
a532443f3e04a9e00295a8cd2a75e080
54c10b9736b70e75c6e505f340b6e2f1
b8a24794813a47521b4be55747e0665a
83b020b0a7b3c353e1c11b1647b53cda
999cae1e22fe69d89d6f56e3050f18cb
```

> 💡 **What the answers look like:** All 5 passwords are **lowercase** Pokémon names. No numbers, no symbols, just the name in all lowercase. Think water types, psychic types, mythical Pokémon, the kind of names a 2009 forum user would absolutely use as a password.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Confirm the Hash Type

All 5 hashes are 32 hex characters long, so they're **MD5** (mode `-m 0`).

```bash
hashid a532443f3e04a9e00295a8cd2a75e080
```

---

### Step 2 - Save the Hashes

```bash
cat > hash.txt << 'EOF'
a532443f3e04a9e00295a8cd2a75e080
54c10b9736b70e75c6e505f340b6e2f1
b8a24794813a47521b4be55747e0665a
83b020b0a7b3c353e1c11b1647b53cda
999cae1e22fe69d89d6f56e3050f18cb
EOF
```

---

### Step 3 - Build Your Pokémon Wordlist

This is the main challenge here. You need a list of all Pokémon names to use as your wordlist. There are a few ways to get it.

---

**Option 1 - Ask an AI (easiest, personally recommended):**

Open your favorite AI (Claude, ChatGPT, whatever you use) and ask:

> "Give me a complete list of all Pokémon names from every generation, one name per line, all lowercase."

The AI will generate the full list for you. Copy the output, paste it into a file called `pokemon.txt`, and you're ready. This is what worked best in practice and gave a list of 2200+ names covering every generation.

---

**Option 2 - Scrape it from Bulbapedia:**

If you want to do it the command line way, this curl command scrapes the Pokémon list directly from Bulbapedia:

```bash
curl -s -A "Mozilla/5.0" \
  "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number" \
  | grep 'href="/wiki/.*(Pok' \
  | sed 's/.*">//; s/<\/a.*//;' \
  | sort -u \
  > pokemon.txt
```

What each part does:
- `curl -s -A "Mozilla/5.0"`: fetches the webpage silently and pretends to be a browser so the site doesn't block it
- `grep 'href="/wiki/.*(Pok'`: finds every line that contains a Pokémon link
- `sed 's/.*">//; s/<\/a.*//;'`: strips out all the HTML and leaves just the name
- `sort -u`: removes duplicates
- `> pokemon.txt`: saves everything to a file

---

### Step 4 - Convert the Wordlist to Lowercase

Since MD5 is case-sensitive, you need to make sure your wordlist matches the format of the passwords. All answers here are lowercase, so convert the whole list:

```bash
tr 'A-Z' 'a-z' < pokemon.txt > pokemon_lower.txt
```

Or do it inline when running Hashcat (next step).

---

### Step 5 - Run Hashcat

**If you already converted to lowercase:**
```bash
hashcat hash.txt -m 0 -a 0 pokemon_lower.txt
```

**Or convert on the fly:**
```bash
tr 'A-Z' 'a-z' < pokemon.txt | hashcat hash.txt -m 0 -a 0
```

---

### Step 6 - View the Results

```bash
hashcat hash.txt -m 0 --show
```

Match each cracked password back to its hash before submitting.

---

### Alternative - John the Ripper

```bash
tr 'A-Z' 'a-z' < pokemon.txt > pokemon_lower.txt
john --format=raw-md5 --wordlist=pokemon_lower.txt hash.txt
john --show --format=raw-md5 hash.txt
```

---

## 💡 Hints (Without Giving It Away)

Here's a nudge for each hash if you're stuck:

- `a532443f...` - A golden colored duck Pokémon. Not the cute baby one, the evolved one.
- `54c10b97...` - A fish Pokémon that has multiple forms depending on which region it's found in.
- `b8a24794...` - A fan-favorite electric Pokémon that can possess household appliances.
- `83b020b0...` - A mythical forest Pokémon from Gen 2 that can travel through time.
- `999cae1e...` - Another golden fish Pokémon. Apparently these hackers really like gold-colored fish.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit with uppercase letters.** All answers are fully lowercase. `Golduck` is wrong, `golduck` is correct.
- ❌ **Don't skip the lowercase conversion.** If your wordlist has capitalized names and you don't convert, Hashcat won't find the matches.
- ✅ **If some hashes don't crack**, your wordlist might be missing some Pokémon. Try adding more generations or use the AI method to get a more complete list.
- ✅ **Cross-check hash to password** before submitting. Output order is not the same as question order.

---

## 🧠 Why This Works

This challenge teaches one of the most important skills in password cracking: **building targeted wordlists**. In real penetration testing, if you know a company has a theme for their passwords (their team name, their product names, their industry terms), you build a custom wordlist around that theme. A generic wordlist like RockYou would never crack "golduck" efficiently, but a Pokémon-specific list cracks it instantly. Knowing how to scrape, format, and feed custom wordlists into Hashcat is what separates basic crackers from skilled ones.

---

## 🔗 Resources

- [Bulbapedia Pokémon List](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number)
- [Hashcat Documentation](https://hashcat.net/wiki/)
- [hashes.com Hash Identifier](https://hashes.com/en/tools/hash_identifier)

---

*Written by: Mo | Last updated: February 2026*
