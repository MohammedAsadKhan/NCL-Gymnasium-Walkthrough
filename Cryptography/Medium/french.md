# Cryptography Medium - French (Vigenère Cipher)

> **Category:** Cryptography
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given an encrypted message and a key, and asked to decode it using the **Vigenère cipher**, a polyalphabetic substitution cipher that uses a repeating keyword to shift letters.

> 💡 The challenge is called "French" because the Vigenère cipher is named after French cryptographer Blaise de Vigenère. Speaking of the French... they invented one of history's most famous ciphers, which is more than can be said for their track record in other strategic endeavors. 🏳️

---

## 🛠️ Tools Needed

- **[dCode.fr Vigenère Cipher](https://www.dcode.fr/vigenere-cipher)** - great for this, handles the key input cleanly
- **[CyberChef](https://gchq.github.io/CyberChef/)** - search for "Vigenère Decode"

---

## 📋 Step-by-Step Walkthrough

### Step 1 - How the Vigenère Cipher Works

Unlike Caesar or Atbash which use a single fixed shift, the Vigenère cipher uses a **keyword** to apply a different shift to each letter. The key repeats over and over until the entire message is encrypted.

For example, with the key `CAT`:
- The first letter is shifted by C (2 positions)
- The second letter is shifted by A (0 positions)
- The third letter is shifted by T (19 positions)
- The fourth letter starts over at C again, and so on

This makes it much harder to crack by hand than a simple Caesar shift since every letter in the message could have a different shift value depending on where the key lands.

For this challenge, the key is: `qizkwcgqbs`

---

### Step 2 - Spot the Clue in the Ciphertext

You're given: `Y ln xkv lubj swlzqvkht, A vmzb pjk bbua we ddgs ILQ-GQYU-8026`

Notice at the end it says `ILQ-GQYU-8026`. That looks like a flag format but doesn't start with `SKY`. This is your confirmation that you're dealing with a substitution cipher that encrypted the flag letters themselves, not a transposition that just rearranged them. The structure is preserved but the letters are scrambled.

---

### Step 3 - Decode the Message

The key is: `qizkwcgqbs`

**Option 1 - dCode.fr:**
1. Go to [dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)
2. Paste the ciphertext into the decryption box
3. Enter `qizkwcgqbs` as the key
4. Hit decrypt and read the output

**Option 2 - CyberChef (personally recommended):**
1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Paste the ciphertext into the Input box
3. Search for **"Vigenère Decode"** and drag it into the Recipe
4. Enter `qizkwcgqbs` as the key
5. Read the output

Your answer is a famous quote about technology and fear, followed by the decrypted flag in `SKY-ABCD-1234` format. Submit the full output exactly as decoded.

> 💡 You'll notice the numbers in the flag (`8026`) stay the same in both the ciphertext and plaintext. Vigenère only encrypts letters, not numbers or punctuation, so those pass through unchanged.

---

## ⚠️ Accuracy Tips

- ❌ **Don't mix up the key and the ciphertext.** The key goes in the key field, the encoded message goes in the ciphertext field. Swapping them gives you complete gibberish.
- ✅ **Numbers and punctuation are not encrypted.** If your decoded output has the numbers and dashes in the right place but the letters look wrong, double check your key.
- ✅ **The key repeats.** It's only 10 characters but the message is longer. The tool handles this automatically, but good to understand why.
- ✅ **Submit the full decoded output**, quote and flag together exactly as it appears.

---

## 🧠 Why This Works

The Vigenère cipher was considered unbreakable for over 300 years and was nicknamed "le chiffre indéchiffrable" (the indecipherable cipher) by the French. It was finally cracked in the 19th century using frequency analysis once analysts realized the key repeats. Today it's trivially broken with any computer, but understanding how polyalphabetic ciphers work builds the foundation for understanding modern encryption schemes like AES, which use far more complex key scheduling to avoid the same weaknesses.

---

## 🔗 Resources

- [dCode.fr Vigenère Cipher](https://www.dcode.fr/vigenere-cipher)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Vigenère Cipher - Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

---

*Written by: Mo | Last updated: February 2026*
