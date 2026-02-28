# Cryptography Medium - Fencing (Rail Fence Cipher)

> **Category:** Cryptography
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given two encrypted messages and asked to decode them using the **Rail Fence cipher**, a transposition cipher that rearranges letters in a zig-zag pattern across a set number of "rails."

> 💡 Don't let the medium difficulty scare you. Once you understand what the Rail Fence cipher does, both questions are solved with a single tool call each.

---

## 🛠️ Tools Needed

- **[dCode.fr Rail Fence Cipher](https://www.dcode.fr/rail-fence-cipher)** - best tool for this, has a "Keep punctuation and spaces" option which is critical
- **[CyberChef](https://gchq.github.io/CyberChef/)** - alternative, search for "Rail Fence Cipher"

---

## 📋 Step-by-Step Walkthrough

### Step 1 - How the Rail Fence Cipher Works

Instead of substituting letters like Caesar or Atbash, the Rail Fence cipher **moves letters around** by writing them in a zig-zag pattern across multiple "rails" (rows), then reading across each row to produce the ciphertext.

Here's a simple example with 4 rails:

```
Plaintext: THIS IS A SECRET

T           A           R
 H       S   S       E   E
  I   I       E   C
   S               T
```

Reading left to right across each rail gives you the ciphertext. To decode, you reverse the process.

The number of rails used is the **key**. Without knowing the key, you'd have to try different values until the output makes sense. For this challenge, the keys are given to you.

> 🚧 The name "Rail Fence" comes from the pattern looking like a zig-zag fence when drawn out. Someone named this cipher after looking at a fence and thinking "yeah, cryptography." Solid inspiration.

---

### Step 2 - Q1: 3 Rails

You're given: `Cair eruSA-0org sgaeudrpesr K-II98.ue cn seYQ3`

This uses the standard **3 rails**.

**Option 1 - dCode.fr:**
1. Go to [dcode.fr/rail-fence-cipher](https://www.dcode.fr/rail-fence-cipher)
2. Paste the ciphertext into the decryption box
3. Set the number of rails to **3**
4. Make sure **"Keep punctuation and spaces"** is checked — this is critical, without it the output will be garbled
5. Hit decode

**Option 2 - CyberChef (personally recommended):**
1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Paste the ciphertext into the Input box
3. Search for **"Rail Fence Cipher Decode"** and drag it into the Recipe
4. Set the key to **3**
5. Read the output

Your answer is a well known quote about composure and elegance under pressure, followed by a flag in `SKY-ABCD-1234` format. Submit the full output, phrase and flag together.

---

### Step 3 - Q2: 5 Rails

You're given: `F daS-eefn  n KZ3eheadty.YI8lta oiwy-Q0. r aI2`

This uses a non-standard **5 rails**.

Same process as Q1, but change the rail count to **5**.

**Option 1 - dCode.fr:**
1. Paste the ciphertext into the decryption box
2. Set the number of rails to **5**
3. Keep **"Keep punctuation and spaces"** checked
4. Hit decode

**Option 2 - CyberChef (personally recommended):**
1. Paste the ciphertext into the Input box
2. Search for **"Rail Fence Cipher Decode"** and drag it into the Recipe
3. Set the key to **5**
4. Read the output

Your answer is a motivational phrase about pushing through fear, followed by a flag. Again, submit the whole thing.

> ⚠️ Note the double space in the ciphertext (`n  K`). Make sure you copy it exactly including that extra space, otherwise the decoding will be off.

---

## ⚠️ Accuracy Tips

- ❌ **Do not remove spaces or punctuation before pasting.** The Rail Fence cipher encodes spaces and punctuation as part of the message. Changing anything shifts every letter in the output.
- ❌ **Don't forget to check "Keep punctuation and spaces" on dCode.** Without it, the tool strips them out and your decoded output will look completely wrong.
- ✅ **Copy-paste the ciphertext exactly as given.** Double spaces, periods, dashes — all of it matters.
- ✅ **Submit the full decoded output**, the quote and the flag together, exactly as it appears.

---

## 🧠 Why This Works

The Rail Fence cipher is a transposition cipher, which means it doesn't change *what* the letters are, only *where* they appear. This is fundamentally different from substitution ciphers like Caesar or Atbash. In real cryptanalysis, recognizing whether a cipher is transposition-based vs substitution-based is an important early step since they require completely different approaches to crack. Rail Fence specifically is simple enough to break by hand if you know the key, but it shows up in CTFs regularly as a building block for more complex challenges.

---

## 🔗 Resources

- [dCode.fr Rail Fence Cipher](https://www.dcode.fr/rail-fence-cipher)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Rail Fence Cipher - Wikipedia](https://en.wikipedia.org/wiki/Rail_fence_cipher)

---

*Written by: Mo | Last updated: February 2026*
