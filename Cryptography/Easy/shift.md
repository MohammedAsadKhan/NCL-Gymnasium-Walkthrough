# Cryptography Easy - Shift

> **Category:** Cryptography
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge gives you a message encoded with a **shift cipher** and asks you to decode it. One tool call and you're done.

> 💡 This might be the fastest challenge in the entire Gymnasium. Seriously.

---

## 🛠️ Tools Needed

- **[CyberChef](https://gchq.github.io/CyberChef/)** - easiest option
- **[rot13.com](https://rot13.com/)** - even faster for this specific challenge
- **[rumkin.com](https://rumkin.com/tools/cipher/)** - good for shift ciphers in general

---

## 📋 Step-by-Step Walkthrough

### Step 1 - A Quick History Lesson (and a Laugh)

The cipher used here is **ROT-13**, which is a Caesar Cipher with a shift of 13.

The Caesar Cipher is named after Julius Caesar, who reportedly used it to send secret messages to his generals. The idea is simple: shift every letter in the alphabet by a fixed number of positions. Caesar used a shift of 3, so A became D, B became E, and so on.

> 🏛️ So Julius Caesar, one of the greatest military minds in history, looked at the entire field of mathematics and cryptography and went: "What if... we just moved the letters over a bit?" And that was it. That was the plan. The Roman Empire's classified communications were protected by the intellectual equivalent of a combination lock where the combination is 1-2-3. To be fair, it worked great against people who couldn't read.

ROT-13 specifically shifts by 13, which is exactly half the alphabet (26 letters). This makes it self-reversing — encoding and decoding use the exact same operation, which is a neat property.

---

### Step 2 - Decode the Message

You're given: `iveghny ynxr`

This is ROT-13. Every letter has been shifted 13 positions forward in the alphabet.

**Option 1 - rot13.com (fastest):**
1. Go to [rot13.com](https://rot13.com/)
2. Paste `iveghny ynxr` into the box
3. The decoded text appears instantly

**Option 2 - CyberChef:**
1. Paste `iveghny ynxr` into the Input box
2. Search for **"ROT13"** and drag it into the Recipe
3. Read the output

Your answer is two words describing a body of water that exists in a digital world.

---

## ⚠️ Accuracy Tips

- ✅ **Spaces and punctuation are not shifted** in ROT-13. Only letters get rotated, so keep spaces where they are.
- ✅ **ROT-13 is self-reversing.** If you run it twice you get back to the original. If your decoded output looks like gibberish, just run it again.
- ❌ **Don't overthink it.** There is genuinely nothing more to this challenge than pasting text into a tool.

---

## 🧠 Why This Works

Shift ciphers are the simplest form of substitution cipher. While ROT-13 and Caesar ciphers are obviously not secure by modern standards, understanding them builds intuition for how more complex ciphers work. In CTFs you'll frequently encounter variations like ROT-47 (which also shifts numbers and symbols) or custom shift values, so knowing how to recognize and brute-force shift ciphers is a useful baseline skill.

---

## 🔗 Resources

- [rot13.com](https://rot13.com/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [rumkin.com Cipher Tools](https://rumkin.com/tools/cipher/)

---

*Written by: Mo | Last updated: February 2026*
