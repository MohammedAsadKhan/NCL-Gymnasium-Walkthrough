# OSINT Easy - PGP Lookup

> **Category:** OSINT
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge has you querying a **public PGP key database** to find information about specific public keys and their owners. You don't need to understand cryptography deeply to solve it, you just need to know how to search these databases and read the results.

> 💡 This one is a lookup challenge, just like WHOIS. You're plugging values into a database and reading what comes back. The slightly tricky part is knowing which columns to read, so we'll cover that.

---

## 🛠️ Tools Needed

- **[keyserver.ubuntu.com](https://keyserver.ubuntu.com/)** - primary source for this challenge
- **[keys.openpgp.org](https://keys.openpgp.org/)** - good for cross-checking
- **[pgp.mit.edu](https://pgp.mit.edu/)** - another option for verification
- A web browser

> 💡 There is no single authoritative PGP database. Different servers may have slightly different records, so it's good practice to check more than one if your results look off.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Understand What You're Looking At

A quick bit of context before jumping in. PGP (Pretty Good Privacy) uses a public/private key pair system. Your **public key** can be shared with anyone so they can encrypt messages that only you can read with your private key. Public key databases exist so people can look up someone's public key by their email address, and each key has a unique **fingerprint** - a long hexadecimal string that identifies it.

That's all you need to know to solve this challenge.

---

### Step 2 - Q1: Key Fingerprint for security@cpanel.net

You need to find the **key fingerprint** associated with the email address `security@cpanel.net`.

Go to **[keyserver.ubuntu.com](https://keyserver.ubuntu.com/)** and type `security@cpanel.net` into the search box.

In the results, look for the entry matching that email. The fingerprint is the long hexadecimal string that appears after `rsa4096/` in the results. It will be a 40-character string of uppercase letters and numbers.

> ⚠️ There may be multiple results. Look carefully for the one tied specifically to `security@cpanel.net` and verify by cross-checking on a second PGP server.

Your answer is a 40-character hexadecimal string.

---

### Step 3 - Q2: Email Address for a Given Fingerprint

This time it's the reverse. You're given a fingerprint and need to find **what email address it belongs to**.

The fingerprint to look up is: `7A39A56B73D1E097D57435CFCDE2DE1DCB2077F2`

Go to **[keyserver.ubuntu.com](https://keyserver.ubuntu.com/)** and paste that fingerprint into the search box.

In the results, look at the `uid` field. The email address will be listed to the right of it.

> 🤔 You know how when you look up a phone number and it tells you who it belongs to? This is exactly that but for encryption keys. You have the "number," now find the name... well, email.

Your answer will be an email address at an unusual domain. If you did the WHOIS challenge, the domain might look familiar.

---

### Step 4 - Q3: Expiry Date of That Key

Using the same results from Q2, you now need to find **when that key expires**.

In the results table, look for the column labeled **"key expir"** (key expiry). The date listed there is your answer.

> ⚠️ This is the most common mistake on this challenge. The results table shows two dates close together: "cr. time" (when the key was created) and "key expir" (when it expires). They are different dates. Read the column header carefully and make sure you're grabbing the expiry, not the creation date.

Your answer will be a date in `YYYY-MM-DD` format and it's quite far in the future, which should help you confirm you have the right one.

---

## ⚠️ Accuracy Tips

- ❌ **Don't confuse "cr. time" with "key expir."** They sit right next to each other in the results and grabbing the wrong one is an easy mistake. Always check the column header.
- ❌ **Don't assume the first result is always the right one.** For Q1 especially, scan all results for the correct email match.
- ✅ **Cross-check on a second PGP server** if anything looks off. Different servers can return slightly different results.
- ✅ **Copy fingerprints exactly.** They're 40 characters long and one wrong digit means a wrong answer. Copy-paste, don't type.

---

## 🧠 Why This Works

PGP key lookups are a real OSINT technique. Security researchers and investigators use public key databases to identify individuals, map relationships between email addresses and organizations, and verify identities. A fingerprint is meant to be a unique identifier for a key, so being able to look one up or reverse-search by email is a genuinely useful skill. You'll also encounter PGP in CTF challenges involving encrypted files and messages, so knowing your way around these databases is worth building early.

---

## 🔗 Resources

- [Ubuntu Keyserver](https://keyserver.ubuntu.com/)
- [OpenPGP Keyserver](https://keys.openpgp.org/)
- [MIT PGP Keyserver](https://pgp.mit.edu/)
- [PGP - Wikipedia](https://en.wikipedia.org/wiki/Pretty_Good_Privacy)
- [What is PGP Encryption? - Varonis](https://www.varonis.com/blog/pgp-encryption)

---

*Written by: Mo | Last updated: February 2026*
