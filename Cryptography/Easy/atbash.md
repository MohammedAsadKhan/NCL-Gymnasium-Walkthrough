# Cryptography Easy - @bash (Atbash)

> **Category:** Cryptography
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge gives you a message encoded with the **Atbash cipher** and asks you to decode it. Similar to the Shift challenge, but with a twist on how the alphabet is rearranged.

> 💡 One question, one tool call. You've got this.

---

## 🛠️ Tools Needed

- **[CyberChef](https://gchq.github.io/CyberChef/)** - search for "Atbash"
- **[rumkin.com](https://rumkin.com/tools/cipher/atbash/)** - has a dedicated Atbash tool

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Atbash vs Caesar, What's the Difference?

Last challenge was ROT-13, a Caesar cipher that shifts the alphabet by 13 positions. Atbash looks very similar at first glance, but it works differently.

Instead of *shifting* the alphabet forward by some number, Atbash completely **reverses** it. A becomes Z, B becomes Y, C becomes X, and so on all the way through. There's no shift value to guess, there's only one possible Atbash mapping.

```
Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext:  Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
```

So if you see a ciphertext letter, you find its position in the bottom row and replace it with the letter directly above it.

> 🪞 Atbash is basically the alphabet looking at itself in a mirror. The ancient Hebrews used it to encode the book of Jeremiah in the Bible. Which means this cipher is literally thousands of years old and we're still putting it in cybersecurity challenges. Respect.

---

### Step 2 - Decode the Message

You're given: `hzuvob lyerlfh xzev`

**In CyberChef:**
1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Paste `hzuvob lyerlfh xzev` into the Input box
3. Search for **"Atbash"** in the Operations bar and drag it into the Recipe
4. Read the output

**In rumkin.com:**
1. Go to [rumkin.com/tools/cipher/atbash](https://rumkin.com/tools/cipher/atbash/)
2. Paste the ciphertext and hit decode

Your answer is three words. Think of a location description that sounds like something out of an adventure game.

---

## ⚠️ Accuracy Tips

- ❌ **Don't confuse Atbash with Caesar.** They look similar but Caesar uses a shift value while Atbash reverses the entire alphabet. If you try ROT-13 on this you'll get gibberish.
- ✅ **Atbash is self-reversing**, just like ROT-13. Running it twice gets you back to the original, which is a handy way to verify your tool is working correctly.
- ✅ **Spaces are preserved.** The three words in the ciphertext are still three words in the plaintext.

---

## 🧠 Why This Works

Atbash is a monoalphabetic substitution cipher, meaning each letter always maps to the same other letter. This makes it easy to crack even without a tool since every letter has exactly one possible substitution. In CTFs, recognizing whether you're dealing with a shift cipher, a reversed alphabet, or something else entirely is a key skill. When a simple decode tool gives you gibberish, switching between Atbash and Caesar variants is usually the next step to try.

---

## 🔗 Resources

- [CyberChef](https://gchq.github.io/CyberChef/)
- [rumkin.com Atbash Tool](https://rumkin.com/tools/cipher/atbash/)
- [Atbash Cipher - Wikipedia](https://en.wikipedia.org/wiki/Atbash)

---

*Written by: Mo | Last updated: February 2026*
