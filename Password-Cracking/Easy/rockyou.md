# Password Cracking Easy - Rockyou

> **Category:** Password Cracking
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given 5 MD5 hashed passwords and asked to crack them. The passwords all come from the infamous **RockYou breach**, meaning they're in the RockYou wordlist that comes pre-installed on Kali Linux.

> ⏱️ In competition, every second counts. So we're giving you two ways to do this: the **proper way** using Hashcat (recommended for learning and practice), and the **fast way** using online tools for when you need to move quickly. A real hacker knows when to type commands and when to just use the shortcut. Know both.

---

## 🛠️ Tools Needed

**Long way (recommended for practice):**
- Kali Linux terminal
- `hashcat` (pre-installed on Kali)
- `hashid` (pre-installed on Kali)
- RockYou wordlist at `/usr/share/wordlists/rockyou.txt`

**Short way (fast during competition):**
- **[CrackStation](https://crackstation.net/)**
- **[hashes.com](https://hashes.com/en/decrypt/hash)**

---

## 📋 The Hashes

```
68a96446a5afb4ab69a2d15091771e39
ec5f0b1826389df8622133014e88afde
32e5f63b189b78dccf0b97ac41f0d228
2233287f476ba63323e60addca1f6b64
6539bbb84fe2de2628fc5e4f2a31f23a
```

> 💡 **What the answers look like:** All 5 passwords are lowercase strings with no spaces. Some are names with numbers attached, some look like made-up words or nicknames, and they range from about 6 to 9 characters long. If your cracked result looks like a real person's username or a word you could imagine someone using as a password in 2009, you're on the right track.

---

## 🚀 The Fast Way (Competition Mode)

> 🏎️ You're 45 minutes into the Individual game, you have 12 categories left, and your teammate is yelling about the log analysis challenges. This is when you use CrackStation.

**Using CrackStation:**
1. Go to [crackstation.net](https://crackstation.net/)
2. Paste all 5 hashes into the box, one per line
3. Complete the CAPTCHA and hit **Crack Hashes**
4. CrackStation will identify the hash type and return the plaintext for each one

**Using hashes.com:**
1. Go to [hashes.com/en/decrypt/hash](https://hashes.com/en/decrypt/hash)
2. Paste the hashes in and hit decrypt
3. Same result, different interface

> ⚠️ Online tools only work for common passwords already in their databases. If a hash doesn't crack online, you'll need Hashcat. For this challenge all 5 are common enough that the online tools handle them fine.

---

## 🧠 The Long Way (Recommended for Practice)

This is the method you should get comfortable with. Online tools won't always work, especially for harder challenges, so knowing Hashcat is essential.

---

### Step 1 - Decompress the RockYou Wordlist

If this is your first time using the RockYou wordlist on Kali, it comes compressed by default and needs to be extracted before Hashcat can use it.

```bash
tar -xvzf /usr/share/wordlists/rockyou.txt.gz
```

What each flag does:
- `-x`: extract files
- `-v`: verbose output so you can see it working
- `-z`: decompress using gzip
- `-f`: specify the filename

> 💡 You only need to do this once. After extraction, the file stays at `/usr/share/wordlists/rockyou.txt` permanently.

---

### Step 2 - Save the Hashes to a File

Create a file called `hash.txt` with all 5 hashes, one per line, no extra spaces:

```bash
cat > hash.txt << 'EOF'
68a96446a5afb4ab69a2d15091771e39
ec5f0b1826389df8622133014e88afde
32e5f63b189b78dccf0b97ac41f0d228
2233287f476ba63323e60addca1f6b64
6539bbb84fe2de2628fc5e4f2a31f23a
EOF
```

---

### Step 3 - Identify the Hash Type

Use `hashid` to identify what type of hash you're looking at:

```bash
hashid 68a96446a5afb4ab69a2d15091771e39
```

All 5 hashes here are **MD5**. You can tell because they are exactly 32 characters long and only use hexadecimal characters (0-9, a-f). In Hashcat, MD5 is mode `-m 0`.

> 💡 When in doubt, also cross-check at [hashes.com/en/tools/hash_identifier](https://hashes.com/en/tools/hash_identifier). Multiple tools confirming the same type means you can crack with confidence.

---

### Step 4 - Run Hashcat

```bash
hashcat hash.txt -m 0 -a 0 /usr/share/wordlists/rockyou.txt
```

What each part does:
- `hash.txt`: the file containing your hashes
- `-m 0`: hash mode 0 (MD5)
- `-a 0`: attack mode 0 (dictionary attack)
- `/usr/share/wordlists/rockyou.txt`: the wordlist to use

Hashcat will chew through the RockYou list and crack the hashes. When finished, results appear in the terminal.

---

### Step 5 - View the Results

If the output scrolled past, run this to see cracked results:

```bash
hashcat hash.txt -m 0 --show
```

This prints each hash alongside its cracked plaintext password.

> ⚠️ Hashcat does NOT preserve your original hash order. It cracks them in whatever order it finds matches. Always match each cracked password back to its original hash before submitting. Getting the right passwords in the wrong order will tank your accuracy score.

---

### Alternative - John the Ripper

Some challenges can only be solved with John, so it's worth knowing how to use it. John is also pre-installed on Kali.

```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

What each part does:
- `--format=raw-md5`: tells John the hash type is MD5. If you're unsure of the format name, run `john --list=formats | grep -i md5` to find it
- `--wordlist=`: the wordlist to use
- `hash.txt`: your file of hashes

To view cracked results after John finishes:

```bash
john --show --format=raw-md5 hash.txt
```

> 💡 John automatically saves cracked passwords to `~/.john/john.pot`. If you run John again on the same hashes it skips already-cracked ones, which is handy. To force a re-crack, delete the pot file first with `rm ~/.john/john.pot`

---

## ⚠️ Accuracy Tips

- ❌ **Don't assume output order matches question order.** Always cross-reference hash to password before submitting.
- ❌ **Don't forget to decompress rockyou.txt.gz first.** Hashcat cannot read a compressed file and will error out.
- ✅ **Copy-paste passwords exactly.** They are case sensitive.
- ✅ **Use `--show` after cracking** to cleanly review all results at once.

---

## 🧠 Why This Works

The RockYou breach happened in 2009 when hackers dumped 32 million plaintext passwords from the RockYou social media platform. That list became the most famous password wordlist in cybersecurity and ships with Kali Linux by default. Dictionary attacks work by hashing every word in a wordlist and comparing it to the target hash. When someone reuses a password that was already breached, their hash cracks instantly. This is why password reuse is one of the most dangerous habits in security.

---

## 🔗 Resources

- [CrackStation](https://crackstation.net/)
- [hashes.com Decrypt](https://hashes.com/en/decrypt/hash)
- [hashes.com Hash Identifier](https://hashes.com/en/tools/hash_identifier)
- [Hashcat Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)
- [Hash Analyzer - TunnelsUp](https://www.tunnelsup.com/hash-analyzer/)

---

*Written by: Mo | Last updated: February 2026*
