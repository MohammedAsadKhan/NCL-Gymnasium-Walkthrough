# Password Cracking Medium - PDF Cracking

> **Category:** Password Cracking
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given an encrypted PDF file and asked to crack its password, then open it to find the flag inside. This involves extracting the password hash from the PDF, cracking it with a wordlist, and then opening the file.

> 💡 This one has a few more steps than previous challenges. If you get stuck at any point, the official NCL YouTube walkthrough covers this exact challenge: [Cyber Skyline Live: PDF Password Cracking](https://www.youtube.com/watch?v=dd0uBmDwvC0&t=295s). Highly recommended if anything below is unclear.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `pdf2john` (pre-installed on Kali)
- `john` (pre-installed on Kali) - personally recommended for this challenge
- `hashcat` (optional alternative)
- RockYou wordlist at `/usr/share/wordlists/rockyou.txt`
- A PDF viewer (any browser or document app works)

---

## 📋 The Challenge Files

Download `encrypted.pdf` from the challenge prompt window and save it to your working directory on Kali.

> 💡 **What the answers look like:**
> - The password is a celebrity name followed by a year. 🕶️ What if I told you... the password is the name of an actor who once dodged bullets in slow motion, followed by the year 2008. All lowercase, no spaces. There is no spoon, but there is definitely a password.
> - The flag follows the standard `SKY-ABCD-1234` format and is inside the PDF once you open it with the correct password.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Extract the Hash from the PDF

Before you can crack the password, you need to pull the password hash out of the PDF file. `pdf2john` does this for you:

```bash
pdf2john encrypted.pdf > hash.txt
```

This extracts the encrypted password hash and saves it to `hash.txt`. Open the file and you'll see a long string starting with the filename followed by a colon and the hash.

---

### Step 2 - Crack the Password

You have two options. The personally recommended method is John since it handles the pdf2john output format directly without any cleanup needed.

---

**Option 1 - John the Ripper (recommended):**

John can read the hash.txt output from pdf2john directly with no modifications needed:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

> ⚠️ This challenge's password is almost halfway through the RockYou wordlist, so it may take a few minutes to crack. Let it run, don't cancel early.

View the cracked password when done:

```bash
john --show hash.txt
```

---

**Option 2 - Hashcat:**

Hashcat doesn't accept the filename prefix that pdf2john adds, so you need to clean the hash first:

```bash
cat hash.txt | cut -d ":" -f 2- > clean.txt
```

This strips the `encrypted.pdf:` part from the front and saves the clean hash to `clean.txt`.

Then crack it with PDF hash mode (`-m 10700`):

```bash
hashcat clean.txt -O -m 10700 -a 0 /usr/share/wordlists/rockyou.txt
```

The `-O` flag enables optimized kernels which speeds things up. This will still take a few minutes.

View the result:

```bash
hashcat clean.txt -m 10700 --show
```

---

### Step 3 - Open the PDF

Once you have the password, open `encrypted.pdf` in any PDF viewer (browser, document viewer, whatever you have). When prompted for a password, enter the cracked password exactly as shown.

The flag is inside the PDF. Submit it in the standard `SKY-ABCD-1234` format.

---

## ⚠️ Accuracy Tips

- ❌ **Don't cancel the crack early.** The password is deep in the RockYou list. Let it finish.
- ❌ **Don't skip the hash cleanup step if using Hashcat.** The filename prefix will cause Hashcat to error. John doesn't need this step.
- ✅ **Copy the password exactly** when opening the PDF. It is case sensitive.
- ✅ **Use John if you want the simpler path.** No cleanup required, just point it at hash.txt and go.

---

## 🧠 Why This Works

PDF encryption stores a hash of the password inside the file itself, which is what `pdf2john` extracts. Once you have the hash, it's the same dictionary attack process as any other password cracking challenge. This technique works against any PDF encrypted with a weak or common password. PDFs protected with long, random passwords are effectively uncrackable this way, which is why using strong unique passwords even for document encryption actually matters.

---

## 🔗 Resources

- [NCL Tutorial Video - PDF Password Cracking](https://www.youtube.com/watch?v=dd0uBmDwvC0&t=295s)
- [John the Ripper GitHub](https://github.com/openwall/john)
- [Hashcat Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)

---

*Written by: Mo | Last updated: February 2026*
