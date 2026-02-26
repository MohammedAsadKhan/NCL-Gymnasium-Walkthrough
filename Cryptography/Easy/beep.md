# Cryptography Easy - Beep (Morse Code)

> **Category:** Cryptography
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge gives you a message encoded in **Morse Code** and asks you to decode it. Paste it into a tool and you're done in under a minute.

> 💡 Morse Code is one of the easiest encodings to identify on sight. Once you know what to look for, you'll spot it instantly in future challenges.

---

## 🛠️ Tools Needed

- **[Morse Code Translator](https://morsecode.world/international/translator.html)** - dedicated tool, works great
- **[CyberChef](https://gchq.github.io/CyberChef/)** - search for "From Morse Code"

---

## 📋 Step-by-Step Walkthrough

### Step 1 - How to Recognize Morse Code

Morse Code is one of the easiest encodings to identify because of its binary nature. There are only two symbols: a dot `.` and a dash `-`. If you see a message made entirely of dots, dashes, spaces, and forward slashes, it's almost certainly Morse Code.

The `/` character is used to separate words. Individual letters within a word are separated by spaces.

> 📡 Fun fact: Morse Code was invented in the 1830s for telegraph machines and was the internet of its day. People sent entire news articles and business transactions one beep at a time across continents. "Beep boop beep" was genuinely how the stock market moved. We've come a long way.

---

### Step 2 - Decode the Message

You're given:
```
.... . / ... . -.-. .-. . - / --- ..-. / --. . - - .. -. --. / .- .... . .- -.. / .. ... / --. . - - .. -. --. / ... - .- .-. - . -.. / ... -.- -.-- / -.. -.- ...- -... / ----. ---.. .---- -....
```

**In Morse Code Translator:**
1. Go to [morsecode.world/international/translator.html](https://morsecode.world/international/translator.html)
2. Paste the Morse Code into the input box
3. Click translate and read the output

**In CyberChef:**
1. Paste the Morse Code into the Input box
2. Search for **"From Morse Code"** and drag it into the Recipe
3. Read the output

Your answer will be a full sentence followed by what looks like a flag, all smashed together with no spaces or dashes. Submit the **entire decoded output exactly as it appears**, including both the sentence and the flag portion at the end.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit just the flag portion.** The full decoded output, sentence and flag together with no spaces, is your answer. Copy-paste the entire thing.
- ✅ **The `/` separates words, spaces separate letters.** If your tool gives you garbled output, check that it's recognizing the `/` as a word separator.
- ✅ **Verify with a second tool** if your output looks off. CyberChef and the Morse Code Translator should give you the same result.

---

## 🧠 Why This Works

Morse Code shows up in CTFs more often than you'd expect, sometimes hidden in audio files as actual beeps, sometimes in text form like here, and sometimes embedded in images as visual patterns. Recognizing it on sight and knowing which tool to reach for quickly is the skill this challenge is building. The audio variant is trickier and worth practicing separately before the Individual game.

---

## 🔗 Resources

- [Morse Code Translator](https://morsecode.world/international/translator.html)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Morse Code - Wikipedia](https://en.wikipedia.org/wiki/Morse_code)

---

*Written by: Mo | Last updated: February 2026*
