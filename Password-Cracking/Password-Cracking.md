# 🔑 Password Cracking Walkthroughs

Identifying hash types, cracking passwords, and understanding how authentication can be compromised.

---

## What to Expect in NCL Password Cracking

NCL Password Cracking challenges give you hashed passwords and ask you to recover the original plaintext. You'll need to identify the hash type, then use the right tool or wordlist to crack it. Challenges range from simple online lookups to running dedicated cracking tools with custom rules.

> 💡 Your two main tools for this category are **Hashcat** and **John the Ripper**. If you're on Kali Linux, both are already installed. If not, get them set up before the Individual game.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [rockyou.md](easy/rockyou.md) | Cracking hashes using the RockYou wordlist |

### 🟡 Medium
| File | Topic |
|---|---|
| [mask.md](medium/mask.md) | Cracking hashes using mask attacks |
| [pokemon.md](medium/pokemon.md) | Cracking hashes using a custom wordlist |
| [windows.md](medium/windows.md) | Cracking Windows NTLM hashes |
| [pdf-cracking.md](medium/pdf-cracking.md) | Cracking password protected PDFs |

### 🔴 Hard
| File | Topic |
|---|---|
| [law-and-order.md](hard/law-and-order.md) | Advanced hash cracking with rules |
| [kali-linux.md](hard/kali-linux.md) | Advanced hash cracking on Kali Linux |

---

## Password Cracking Quick Reference

**Identify a hash type:**
```bash
hash-identifier
# or
hashid 'paste_hash_here'
```

**Crack with Hashcat:**
```bash
# MD5
hashcat -m 0 'paste_hash_here' wordlist.txt

# SHA1
hashcat -m 100 'paste_hash_here' wordlist.txt

# SHA256
hashcat -m 1400 'paste_hash_here' wordlist.txt

# bcrypt
hashcat -m 3200 'paste_hash_here' wordlist.txt
```

**Crack with John the Ripper:**
```bash
# Save the hash to a text file first, then run:
echo 'paste_hash_here' > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

**Online hash lookup (fast for common hashes):**
- [CrackStation](https://crackstation.net/)
- [hashes.com](https://hashes.com/en/decrypt/hash)

---

*Written by: Mo | Last updated: February 2026*
