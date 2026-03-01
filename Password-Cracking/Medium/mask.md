# Password Cracking Medium - Mask

> **Category:** Password Cracking
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given 5 MD5 hashed passwords. The twist here is that you already know the format: every password is `SKY-HQNT-` followed by exactly 4 digits. This is where **mask attacks** come in — instead of trying every word in a wordlist, you build a precise pattern and only try combinations that match it.

> 💡 This is where password cracking gets smarter. A dictionary attack would never find these since they're not in any wordlist. But a mask attack cracks all 5 in seconds because the search space is tiny — only 10,000 possible combinations (0000 through 9999).

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `hashcat` (pre-installed on Kali)
- `hashid` or [hashes.com](https://hashes.com/en/tools/hash_identifier) to confirm hash type

> ⚠️ Online tools like CrackStation won't work here. These passwords are too specific to be in any prebuilt database. You need Hashcat with a mask attack.

---

## 📋 The Hashes

```
71b816fe0b7b763d889ecc227eab400a
674291170dffcf620bda2a604a6820ea
06f03267f31077d2c4b5c728472070ae
d866f4b3b34b598375149fb7661113ab
d9053951a8d1c15254b46ec9fc974a6b
```

> 💡 **What the answers look like:** Every password follows the exact format `SKY-HQNT-XXXX` where XXXX is a 4-digit number. If your cracked result doesn't start with `SKY-HQNT-`, something went wrong with your mask.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Understand What a Mask Attack Is

A mask attack is like telling Hashcat "I know the password looks like *this*, just fill in the blanks."

Instead of a wordlist, you give Hashcat a **pattern** using special placeholder characters:

| Placeholder | Matches |
|---|---|
| `?d` | Any digit (0-9) |
| `?l` | Any lowercase letter (a-z) |
| `?u` | Any uppercase letter (A-Z) |
| `?a` | Any printable character |

So for a password like `SKY-HQNT-XXXX` where XXXX is 4 digits, the mask would be:

```
SKY-HQNT-?d?d?d?d
```

Hashcat will literally try `SKY-HQNT-0000`, `SKY-HQNT-0001`, `SKY-HQNT-0002`... all the way to `SKY-HQNT-9999`. That's only 10,000 attempts, which takes milliseconds.

---

### Step 2 - Confirm the Hash Type

All 5 hashes are 32 characters of hex, which means **MD5**. Confirm with:

```bash
hashid 71b816fe0b7b763d889ecc227eab400a
```

MD5 = hashcat mode `-m 0`.

---

### Step 3 - Save the Hashes to a File

```bash
cat > hash.txt << 'EOF'
71b816fe0b7b763d889ecc227eab400a
674291170dffcf620bda2a604a6820ea
06f03267f31077d2c4b5c728472070ae
d866f4b3b34b598375149fb7661113ab
d9053951a8d1c15254b46ec9fc974a6b
EOF
```

---

### Step 4 - Run the Mask Attack

```bash
hashcat hash.txt -m 0 -a 3 'SKY-HQNT-?d?d?d?d'
```

What each part does:
- `hash.txt`: your file of hashes
- `-m 0`: MD5 hash mode
- `-a 3`: attack mode 3, which is a mask attack (different from `-a 0` dictionary attack)
- `'SKY-HQNT-?d?d?d?d'`: the mask pattern, with `?d` representing each unknown digit

> 💡 Use single quotes around the mask so your terminal doesn't misinterpret any special characters in the pattern.

Hashcat will blaze through all 10,000 combinations and crack all 5 hashes almost instantly.

---

### Step 5 - View the Results

```bash
hashcat hash.txt -m 0 --show
```

Match each cracked password back to its original hash before submitting.

---

### Alternative - John the Ripper

John handles mask attacks too using its `--mask` option:

```bash
john --format=raw-md5 --mask='SKY-HQNT-?d?d?d?d' hash.txt
```

View results:

```bash
john --show --format=raw-md5 hash.txt
```

> 💡 John uses the same `?d`, `?l`, `?u` placeholder syntax as Hashcat for masks, so once you learn one, the other is easy.

---

## ⚠️ Accuracy Tips

- ❌ **Don't use a dictionary attack here.** `-a 0` with a wordlist won't find these passwords. You need `-a 3` with the mask.
- ❌ **Don't forget the single quotes** around the mask in your command. Without them the terminal may misinterpret the `?` characters.
- ❌ **Don't skip the hash-to-password matching step.** Hashcat output order is not guaranteed. Verify each one before submitting.
- ✅ **The mask must match exactly.** Every character in `SKY-HQNT-` needs to be in the mask literally, only the `?d?d?d?d` part is variable.

---

## 🧠 Why This Works

Mask attacks are incredibly powerful when you know something about the password format. In real-world penetration testing, if you know a company uses a default password scheme like `CompanyName2024!`, a mask attack cracks every account using that pattern in seconds. This is why password policies that just add a number at the end (like `Password1`) are still weak — the search space is tiny. Understanding mask attacks also helps you build better password policies to defend against them.

---

## 🔗 Resources

- [Hashcat Mask Attack Documentation](https://hashcat.net/wiki/doku.php?id=mask_attack)
- [Hashcat Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)
- [hashes.com Hash Identifier](https://hashes.com/en/tools/hash_identifier)

---

*Written by: Mo | Last updated: February 2026*
