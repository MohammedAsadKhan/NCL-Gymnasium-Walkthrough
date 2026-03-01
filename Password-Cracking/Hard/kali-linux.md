# Password Cracking Hard - Kali Linux (yescrypt)

> **Category:** Password Cracking
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a real `/etc/shadow` file from a Kali Linux machine. Your job is to identify the only real user account, analyze the password hash, and crack it. This one uses **yescrypt**, a modern hashing algorithm that requires a specific approach.

> ⚠️ **Use John the Ripper ONLY for this challenge.** Hashcat does not support yescrypt at the time of writing and will not crack this hash regardless of what you try. John on Kali can handle it natively using `--format=crypt`. Save yourself the frustration and go straight to John.

---

## 🛠️ Tools Needed

- **Kali Linux** terminal (required, this MUST be run on Kali or another system using yescrypt natively)
- `john` (pre-installed on Kali)
- RockYou wordlist at `/usr/share/wordlists/rockyou.txt`

> ⚠️ Running John with `--format=crypt` works by using your system's own crypt function to verify hashes. This only works if your system natively supports yescrypt, which Kali does. Running this on Windows or an older Linux distro will not work.

---

## 📋 The Shadow File

Save the following line to a file called `passwords.txt`. You only need the one line that has an actual hash in it, everything else has `*`, `!`, or `!!` which means no password is set.

```
hollie:$y$j9T$/WzixhAsn8sdXhCquYzh01$KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4:18934:0:99999:7:::
```

```bash
echo 'hollie:$y$j9T$/WzixhAsn8sdXhCquYzh01$KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4:18934:0:99999:7:::' > passwords.txt
```

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Find the Username

Look through the shadow file. Every entry has the format:

```
username:password_field:last_changed:...
```

The password field is the second column separated by colons. Most entries show `*`, `!`, or `!!` which means the account is locked or has no password. Only one entry has an actual hash starting with `$y$`. That username is your answer.

---

### Step 2 - Q2: When Was the Password Last Changed?

The third field in the shadow file is a number representing the **number of days since January 1, 1970** (Unix epoch) when the password was last changed.

For the hollie entry, that number is `18934`.

To convert it to a real date, multiply by 86400 (seconds in a day) and use an epoch converter:

1. Go to [epochconverter.com](https://www.epochconverter.com/)
2. Calculate: `18934 * 86400 = 1635897600`
3. Paste `1635897600` into the converter
4. Read the resulting date

Your answer will be a date in `YYYY-MM-DD` format.

---

### Step 3 - Q3 and Q4: Read the Hash Structure

The full hash for hollie is:

```
$y$j9T$/WzixhAsn8sdXhCquYzh01$KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4
```

The yescrypt format breaks down like this:

```
$y$   =  algorithm identifier (yescrypt)
j9T   =  params (cost parameters)
$     =  separator
/WzixhAsn8sdXhCquYzh01   =  SALT
$     =  separator
KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4   =  HASH DIGEST
```

So:
- **Q3 (salt):** the section between the second and third `$` signs, right after the params
- **Q4 (hash digest):** everything after the final `$`

---

### Step 4 - Q5: Crack the Password

Now here's where it gets interesting. You have two options.

---

**Option 1 - The Brute Force Way (slow, but it works):**

Just point John at the RockYou wordlist and let it run. yescrypt is deliberately slow to compute so this will take a long time, potentially hours depending on your hardware:

```bash
john --format=crypt --wordlist=/usr/share/wordlists/rockyou.txt passwords.txt
```

Go make a coffee. Or three.

---

**Option 2 - The Smart Way (think like an attacker):**

Before you commit to a multi-hour crack, stop and think about what you already know.

> 🧠 As an attacker, one of the first things you do is look for low-hanging fruit. Humans are lazy with passwords, most of us have done it too. What if the user just used their username as the base of their password?

The username is `hollie`. What if the password is just... `hollie` with something added to it?

Now look back at the previous challenges in this category. Notice a pattern? RockYou passwords had numbers appended. The SVU passwords had 2 digits appended. The mask challenge used a fixed format with digits at the end.

**What if hollie did the same thing? `hollie` + 2 digits?**

That's only 100 combinations: `hollie00` through `hollie99`. Instead of cracking the full RockYou list, you can target just this pattern using a John rule.

**Create a targeted wordlist with just the username:**

```bash
echo "hollie" > hollie.txt
```

**Run John with a rule that appends 2 digits:**

John needs the rule to be defined in its config file first. Add it with this command:

```bash
sudo sh -c 'echo "[List.Rules:AppendTwoDigits]" >> /etc/john/john.conf'
sudo sh -c 'echo "Az\"[0-9][0-9]\"" >> /etc/john/john.conf'
```

Then run John using that rule:

```bash
john --format=crypt --wordlist=hollie.txt --rules=AppendTwoDigits passwords.txt
```

What this does:
- `--wordlist=hollie.txt`: uses only the word "hollie" as the base
- `--rule='Az"[0-9][0-9]"'`: the `Az` rule appends characters after the word, `[0-9][0-9]` means try every digit combination for each position

John will try `hollie00`, `hollie01`, `hollie02`... all the way to `hollie99`. On yescrypt this still takes a minute since each attempt is computationally expensive, but it's dramatically faster than running the full RockYou list.

View the result:

```bash
john --show passwords.txt
```

The output will look something like this:

```
username:PASSWORD:18934:0:99999:7:::
```

The cracked password is the value between the **first and second colon**. That's the part you submit. Everything after the second colon is just the rest of the shadow file fields, ignore all of that.

---

## ⚠️ Accuracy Tips

- ❌ **Do not use Hashcat.** It does not support yescrypt. It will either error out or silently fail to crack anything.
- ❌ **Do not run this on anything other than Kali.** The `--format=crypt` option relies on the system's native crypt support. It will not work on Windows or older Linux distros.
- ❌ **Do not guess the password.** Even if you think you know it, submit only what John confirms.
- ✅ **Try the smart approach first.** The targeted rule attack takes minutes instead of hours and the pattern points strongly to it.
- ✅ **Double check the salt and hash digest** by counting `$` delimiters carefully. One wrong character means a wrong answer.
- ✅ **For the date, verify your epoch calculation** before submitting. Off-by-one errors are common.

---

## 🧠 Why This Works

This challenge teaches two important things. First, yescrypt is a modern memory-hard hashing function designed to be slow and expensive to crack, which is why targeting a small likely password space beats brute force every time. Second, people reuse patterns. A username with digits appended is one of the most common weak password patterns in the real world. As a penetration tester, checking `username + digits` before running a full wordlist attack is standard practice because it saves hours and often works. Attackers rely on human laziness. Defenders need to enforce password policies that prevent it.

---

## 🔗 Resources

- [Epoch Converter](https://www.epochconverter.com/)
- [John the Ripper GitHub](https://github.com/openwall/john)
- [yescrypt - Wikipedia](https://en.wikipedia.org/wiki/Yescrypt)
- [John the Ripper Rules Documentation](https://www.openwall.com/john/doc/RULES.shtml)

---

*Written by: Mo | Last updated: February 2026*
