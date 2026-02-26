# Cryptography Easy - Number Bases

> **Category:** Cryptography
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge gives you four encoded strings and asks you to decode them into readable text. Each one uses a different number base or encoding format. No cryptography knowledge needed, just knowing which tool to use and how to use it.

> 💡 All four questions can be solved in CyberChef. If you're not familiar with it yet, this is a great challenge to get comfortable because you'll use it constantly throughout the Cryptography category.

---

## 🛠️ Tools Needed

- **[CyberChef](https://gchq.github.io/CyberChef/)** - handles all four questions
- **[RapidTables](https://www.rapidtables.com/)** - good alternative for hex and binary
- **[Base64Decode.org](https://www.base64decode.org/)** - quick option for Q2

---

## 📋 Step-by-Step Walkthrough

### Before You Start - How to Identify Encodings

The trick with number bases challenges is recognizing *what you're looking at* before trying to decode it. Here's a quick cheat sheet:

- Starts with `0x` and uses letters A-F mixed with numbers? **Hexadecimal**
- Only contains `0` and `1` separated by spaces? **Binary**
- Mix of uppercase, lowercase, numbers, and ends with `=`? **Base64**
- Dots and dashes? Morse code (not in this challenge but good to know)

Once you know the encoding, decoding it is just a tool call away.

---

### Step 1 - Q1: Hexadecimal to ASCII

You're given: `0x73636f7270696f6e`

This is **hexadecimal** (base 16). The `0x` at the start is just a notation flag telling you it's hex — don't include it when you decode.

**In CyberChef:**
1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Paste `73636f7270696f6e` into the Input box (leave out the `0x`)
3. In the Operations search bar, search for **"From Hex"** and drag it into the Recipe
4. Your decoded answer appears in the Output box

Your answer will be a common English word, an animal to be specific.

> ⚠️ Don't include the `0x` prefix when decoding. It's just a label, not part of the actual hex value.

---

### Step 2 - Q2: Base64 to ASCII

You're given: `c2NyaWJibGU=`

This is **Base64** encoding. You can tell because it uses a mix of uppercase and lowercase letters, numbers, and ends with `=` (Base64 uses `=` as padding at the end).

**In CyberChef:**
1. Paste `c2NyaWJibGU=` into the Input box
2. Search for **"From Base64"** and drag it into the Recipe
3. Read the output

Your answer is a word that means writing messily or drawing random lines.

---

### Step 3 - Q3: Binary to ASCII

You're given: `01110011 01100101 01100011 01110101 01110010 01100101 01101100 01111001`

This is **binary** (base 2). Each group of 8 digits (called a byte) represents one character.

**In CyberChef:**
1. Paste the full binary string into the Input box
2. Search for **"From Binary"** and drag it into the Recipe
3. Read the output

Your answer is an adverb you'd use to describe doing something safely.

> 💡 Each space-separated group of 8 bits = one letter. So 8 groups = 8 letters. That's a useful sanity check to make sure you got the right number of characters in your answer.

---

### Step 4 - Q4: Binary + Base64 (Double Encoded)

You're given: `01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101`

This one is **doubly encoded** - binary on the outside, Base64 on the inside. To decode it you have to peel back the layers in the right order: binary first, then Base64.

**In CyberChef (the slick way - do both steps in one recipe):**
1. Paste the binary string into the Input box
2. Add **"From Binary"** as the first operation
3. Add **"From Base64"** as the second operation right below it
4. Read the final output

CyberChef will run both operations in sequence automatically. The output after step one will look like garbled Base64 text, which is normal. After step two it'll decode into the final readable word.

Your answer is something you'd find on a stick at a carnival.

> 🍭 I'll be honest, I really like candy. Especially the kind that's been a childhood classic for decades and comes in a curved shape... on a stick... and is very sweet. You know the one.

---

## ⚠️ Accuracy Tips

- ❌ **Don't include `0x` when decoding Q1.** Strip it before pasting into your tool.
- ❌ **Don't decode Q4 in the wrong order.** Binary first, then Base64. Doing it backwards gives you nonsense.
- ✅ **Use CyberChef's Magic operation if you're ever unsure** what encoding you're looking at. Paste the text in and let it figure it out.
- ✅ **Count the binary groups in Q3 and Q4** to sanity check your answer length before submitting.

---

## 🧠 Why This Works

Understanding number bases is foundational to everything in cybersecurity. Hex shows up constantly when reading memory dumps, shellcode, and network packets. Binary is how computers actually store everything. Base64 is used all over the web to safely transmit binary data as text, you'll see it in JWTs, cookies, and encoded payloads. Recognizing these on sight and decoding them quickly is a skill you'll use in almost every CTF category, not just Cryptography.

---

## 🔗 Resources

- [CyberChef](https://gchq.github.io/CyberChef/)
- [RapidTables - Hex to ASCII](https://www.rapidtables.com/convert/number/hex-to-ascii.html)
- [Base64Decode.org](https://www.base64decode.org/)
- [Number Bases - Khan Academy](https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-factors-and-multiples/cc-6th-number-bases/a/number-systems-review)

---

*Written by: Mo | Last updated: February 2026*
