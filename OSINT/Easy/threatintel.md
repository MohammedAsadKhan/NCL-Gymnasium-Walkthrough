# OSINT Easy - Threat Intel

> **Category:** OSINT
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge has you researching some of the most well-known vulnerabilities and incidents in cybersecurity history. All 6 questions can be solved with a quick Google search and a Wikipedia page.

> 💡 Seriously, these are all one Google search away. We're going through it in detail so you actually learn what each of these are, because you'll see them come up again in harder challenges.

---

## 🛠️ Tools Needed

- A web browser
- Google (or any search engine)
- Wikipedia
- That's it

> 💡 Pro tip: once you're on a Wikipedia page, use **CTRL + F** to search for a keyword within the page instead of reading the whole thing. Saves a lot of time.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: The POODLE Attack CVE

You're looking for the **CVE identifier** of the original POODLE attack.

A CVE (Common Vulnerabilities and Exposures) is a standardized ID assigned to known security vulnerabilities. They follow the format `CVE-YEAR-NUMBER`.

**Where to look:** Google "POODLE attack CVE" and head to the Wikipedia page for POODLE. The CVE number is right there. You're looking for the *original* POODLE, not any of its variants that came later.

Your answer will follow the CVE format and include the year it was discovered.

---

### Step 2 - Q2: VSFTPD Smiley Face Backdoor Version

You're looking for the **specific version number of VSFTPD** that contained a malicious backdoor hidden in the source code.

VSFTPD is a popular FTP server for Unix-like systems. In one particular version, someone sneaked a backdoor into the source code that would open a shell if a smiley face `:)` was appended to the username during login. Yes, really.

**Where to look:** Google "VSFTPD smiley face backdoor" and find the Wikipedia article or any reputable security source. You're looking for the exact version number in the format `X.X.X`.

---

### Step 3 - Q3: First OpenSSL Version NOT Vulnerable to Heartbleed

This one is slightly trickier to read carefully. You're looking for the **first 1.0.1 version of OpenSSL that patched Heartbleed**, meaning it was NOT vulnerable.

Heartbleed (CVE-2014-0160) was a catastrophic bug in OpenSSL that let attackers read memory from servers, potentially leaking passwords, private keys, and more.

**Where to look:** Google "Heartbleed OpenSSL versions affected Wikipedia." On the Wikipedia page, look for the table or section that lists which versions were vulnerable vs. patched. You want the first version in the 1.0.1 branch that came out *after* the fix.

Your answer will be in the format `1.0.1X` where X is a letter.

---

### Step 4 - Q4: Original RFC Number for Telnet

You're looking for the **RFC number that originally described the Telnet protocol**.

Telnet is one of the oldest internet protocols, used for remote terminal access. Like all internet standards, it was defined in an RFC document.

**Where to look:** Google "Telnet RFC Wikipedia." On the Wikipedia page for Telnet, look for references to the original RFC. Note that the question asks for the *original* RFC, so if you see multiple RFC numbers, trace back to the first one. You may need to click through to a linked page to confirm.

Your answer will be in the format `RFC XXX`.

---

### Step 5 - Q5: SQL Slammer Worm Size in Bytes

You're looking for the **size of the SQL Slammer worm in bytes**.

SQL Slammer (2003) was one of the fastest-spreading worms in history. It was notable for being incredibly tiny, which is part of why it spread so fast. It fit entirely within a single UDP packet.

**Where to look:** Google "SQL Slammer worm Wikipedia." The size in bytes is mentioned early in the article and is a fun fact that sticks with you once you read it.

Your answer is a 3-digit number.

---

### Step 6 - Q6: "Samy is my..."

Complete the sentence: **"Samy is my ___"**

This one is a classic piece of internet security history. Samy Kamkar created one of the first major XSS (Cross-Site Scripting) worms in 2005, which spread across MySpace at an absurd rate. The worm added Samy as a friend and displayed a phrase on every infected profile.

**Where to look:** Google "Samy worm MySpace Wikipedia." The phrase is literally in the article.

> 🦇 Did I ever tell you how much I love Batman? He's my absolute... well, you know. 

---

## ⚠️ Accuracy Tips

- ❌ **Don't mix up POODLE variants.** There was an original POODLE and later a "POODLE for TLS" variant with a different CVE. The question asks for the *original*.
- ❌ **Read carefully on Heartbleed.** The question asks for the first version that was NOT vulnerable, not the last one that was. Those are different answers.
- ✅ **Wikipedia is your best friend here.** All 6 answers are on Wikipedia pages. Use CTRL + F to find keywords fast.
- ✅ **Cross-check your answers.** If you find it on Wikipedia, a quick secondary search to confirm never hurts your confidence before submitting.

---

## 🧠 Why This Works

These aren't random trivia questions. POODLE, Heartbleed, SQL Slammer, the VSFTPD backdoor, and the Samy worm are all landmark events in cybersecurity history. Understanding what they are, when they happened, and why they mattered gives you context that makes harder vulnerability research challenges much easier. You'll see references to CVEs, RFC numbers, and historical exploits constantly in real security work.

---

## 🔗 Resources

- [POODLE - Wikipedia](https://en.wikipedia.org/wiki/POODLE)
- [Heartbleed - Wikipedia](https://en.wikipedia.org/wiki/Heartbleed)
- [SQL Slammer - Wikipedia](https://en.wikipedia.org/wiki/SQL_Slammer)
- [Samy (computer worm) - Wikipedia](https://en.wikipedia.org/wiki/Samy_(computer_worm))
- [Telnet - Wikipedia](https://en.wikipedia.org/wiki/Telnet)

---

*Written by: Mo | Last updated: February 2026*
