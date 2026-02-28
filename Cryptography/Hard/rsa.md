# Cryptography Hard - RSA

> **Category:** Cryptography
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given an RSA-encrypted message and asked to crack it by working through the math step by step. This challenge sounds intimidating but every step is laid out clearly below. By the end you'll understand how RSA actually works, not just how to use it.

> 💡 Don't let "Hard" scare you. The math here is middle school level, the only reason this is classified Hard is because there are more steps than the other challenges. Take it one step at a time and you'll be fine.

---

## 🛠️ Tools Needed

- **[Prime Factorization Calculator](https://www.calculator.net/factor-calculator.html)** - for finding p and q
- **[RSA Calculator](https://www.tausquared.net/pages/ctf/rsa.html)** - for finding d and decrypting
- **Python 3 with gmpy2** (optional but elegant, covered at the end)
- An ASCII table (Google "ASCII table" and use any result)

---

## 📋 The Given Values

Before anything else, here's what you have:

```
n = 1079
e = 43
c = 996 894 379 631 894 82 379 852 631 677 677 194 893
```

`n` and `e` make up the **public key**. `c` is the **ciphertext**, split into 13 numbers, each representing one character of the message.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Understand What RSA Is (In Plain English)

RSA encryption works using a pair of keys: a **public key** that anyone can use to encrypt a message, and a **private key** that only the recipient has to decrypt it.

The security of RSA relies on one simple fact: **it's very easy to multiply two large prime numbers together, but extremely hard to figure out which two primes were used just from looking at the result.** That's the whole trick.

Think of it like this: if I tell you 15, you can quickly figure out it's 3 x 5. But if I tell you a number with 300 digits, good luck figuring out its factors. RSA uses numbers that massive in real life. In this challenge the numbers are tiny on purpose so you can practice the process.

The variables you'll work with:

| Variable | What it is |
|---|---|
| `p` and `q` | Two secret prime numbers |
| `n` | p times q (public, you have this) |
| `e` | Part of the public key (you have this) |
| `d` | Part of the private key (you need to find this) |
| `c` | The ciphertext (you have this) |
| `m` | The plaintext message (what you want) |

---

### Step 2 - Q1 and Q2: Find p and q

You know that `n = p * q` and `n = 1079`. You need to find which two prime numbers multiply together to make 1079.

Go to the **[Prime Factorization Calculator](https://www.calculator.net/factor-calculator.html)**, enter `1079`, and hit calculate.

It will give you exactly two prime factors. The **smaller one is p** and the **larger one is q**.

> 🔓 This is the attack. In real RSA, p and q are hundreds of digits long and factoring n would take longer than the age of the universe. Here they're small enough that a calculator cracks it in milliseconds. This is why key size matters so much in cryptography.

Submit the smaller number for Q1 and the larger for Q2.

---

### Step 3 - Calculate phi (φ)

Now that you have p and q, calculate **phi** (pronounced "fee"), which is used to find d.

The formula is:

```
phi = (p - 1) * (q - 1)
```

Plug in your values of p and q and do the arithmetic. This is a straightforward multiplication after subtracting 1 from each.

---

### Step 4 - Find d

`d` is the private key value that lets you decrypt the message. It's related to `e` and `phi` by this equation:

```
d * e ≡ 1 mod phi
```

This looks scary but in plain English it means: find a number `d` such that when you multiply `d * e` and divide by `phi`, the remainder is 1.

You don't need to solve this by hand. Use the **[RSA Calculator](https://www.tausquared.net/pages/ctf/rsa.html)**:
1. Enter your values of p, q, and e
2. The calculator will compute d for you

With the values from this challenge:
```
d = 595
```

---

### Step 5 - Q3: Decrypt the Message

Now you have everything you need:

```
n = 1079
d = 595
c = 996 894 379 631 894 82 379 852 631 677 677 194 893
```

The decryption formula for each number in the ciphertext is:

```
m = c^d mod n
```

This means: raise each ciphertext number to the power of d, then take the remainder when divided by n. Each result is an ASCII number that maps to a letter.

You need to do this for all 13 numbers. There are two ways to do it:

---

**Option 1 - RSA Calculator (easier):**

Use the [RSA Calculator](https://www.tausquared.net/pages/ctf/rsa.html) to compute `m = c^d mod n` for each ciphertext number one at a time, then look up each result on an ASCII table.

---

**Option 2 - Python Script (recommended, faster):**

If you have Python and gmpy2 installed (comes with Kali), paste this script and fill in p and q:

```python
import gmpy2

e = 43
p =    # fill in your p
q =    # fill in your q
n = p * q

c = [996, 894, 379, 631, 894, 82, 379, 852, 631, 677, 677, 194, 893]

phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)

for i in c:
    m = pow(i, d, n)
    print(chr(m), end='')

print("")
```

Run it and the flag prints directly to your terminal. No ASCII table lookups needed.

> 💡 `chr(m)` converts the number directly to its ASCII character. Python handles the whole ASCII table lookup for you.

Your answer is the full decrypted message in `SKY-ABCD-1234` format.

---

## ⚠️ Accuracy Tips

- ❌ **Don't mix up p and q.** NCL asks for the smaller prime as p and the larger as q. Double check before submitting.
- ❌ **Don't skip any ciphertext numbers.** There are 13 of them and each one is a character. Missing one shifts everything after it.
- ✅ **Use the Python script if you can.** Doing 13 individual RSA calculator lookups is tedious and error prone. The script does it all in one shot.
- ✅ **Verify your d value.** With the given values, d should come out to 595. If you got something different, recheck your p, q, and phi.

---

## 🧠 Why This Works

This challenge demonstrates a **real RSA attack**. When the primes p and q are too small, an attacker can factor n trivially and reconstruct the private key. This is not a theoretical vulnerability, it has happened in the real world when developers used weak key generation. Modern RSA uses primes that are 1024 to 4096 bits long, making factoring computationally infeasible with current hardware. Understanding why the math works here gives you intuition for why key size and proper random prime generation are so critical in real cryptographic implementations.

---

## 🔗 Resources

- [Prime Factorization Calculator](https://www.calculator.net/factor-calculator.html)
- [RSA Calculator](https://www.tausquared.net/pages/ctf/rsa.html)
- [ASCII Table](https://www.asciitable.com/)
- [RSA Encryption - Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [gmpy2 Documentation](https://gmpy2.readthedocs.io/)

---

*Written by: Mo | Last updated: February 2026*
