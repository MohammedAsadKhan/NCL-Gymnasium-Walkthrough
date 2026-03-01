# 🛡️ Islander Cyber Society — NCL Gymnasium Walkthroughs

> **Maintained by the ICS CTF Team | Texas A&M University - Corpus Christi**

This repository is the official study resource for ICS members competing in the [National Cyber League (NCL)](https://nationalcyberleague.org/). It contains step-by-step walkthroughs for every challenge in the **NCL Gymnasium** — designed to help you build accuracy, avoid common mistakes, and train for Individual and Team games.

---

## 🎯 Purpose

The NCL scores you on **accuracy, not just completion**. One wrong flag tanks your score more than a skipped challenge. These walkthroughs exist to:

- Walk you through each Gymnasium challenge methodically
- Flag common mistakes that hurt your accuracy
- Teach *why* the solution works, not just *what* the answer is
- Build a foundation for the Individual and Team game seasons

---

## 📁 Repository Structure

```
ics-ncl-walkthroughs/
├── OSINT/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Cryptography/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── Enumeration-and-Exploitation/
├── Log-Analysis/
├── Network-Traffic-Analysis/
├── Password-Cracking/
├── Scanning/
├── Web-Application/
├── templates/
│   └── challenge-template.md   ← Use this when writing new walkthroughs
└── resources/
    └── tools.md                ← Recommended tools per category
```

Each category folder contains individual `.md` files — one per challenge — organized by difficulty.

---

## 🗂️ Categories

| Category | Status | Challenges Covered |
|---|---|---|
| 🔍 OSINT | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: N/A |
| 🔐 Cryptography | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 💻 Enumeration & Exploitation | 🔲 Coming Soon | — |
| 📋 Log Analysis | 🔲 Coming Soon | — |
| 🌐 Network Traffic Analysis | 🔲 Coming Soon | — |
| 🔑 Password Cracking | 🔲 Coming Soon | — |
| 🔎 Scanning | 🔲 Coming Soon | — |
| 🕸️ Web Application | 🔲 Coming Soon | — |

---

## 🚀 How to Use This Repo

**As a competitor:**
1. Open the folder for the category you're working on
2. Start with `easy/` and work up — don't skip difficulty levels
3. Read the full walkthrough *before* re-attempting challenges you got wrong
4. Pay special attention to the ⚠️ **Accuracy Tips** section in each file

**As a contributor:**
1. Copy `templates/challenge-template.md`
2. Fill it out for a challenge not yet covered
3. Submit a pull request — see [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🛠️ Recommended Tools

| Category | Tools |
|---|---|
| OSINT | Google Dorking, Shodan, Maltego, ExifTool, Reverse Image Search, WHOIS |
| Cryptography | CyberChef, dCode.fr, Python, RsaCtfTool |
| Log Analysis | grep, awk, Splunk (free tier), Excel/Sheets |
| Network Traffic | Wireshark, tshark, NetworkMiner |
| Password Cracking | Hashcat, John the Ripper, CrackStation |
| Web Application | Burp Suite (Community), curl, browser DevTools |
| Scanning | Nmap, Gobuster, Nikto |

A full tools setup guide is in [`resources/tools.md`](resources/tools.md).

---

## 📌 NCL Gymnasium Tips (General)

- **Attempt every challenge** — unanswered challenges score 0, but wrong answers penalize accuracy
- **Verify before submitting** — double-check your flag format (`SKY-XXXX-XXXX`)
- **The Gymnasium is your practice ground** — grind it until every category is second nature
- **Track your accuracy** — aim for 90%+ before the Individual game opens

---

## 👥 Contributing

ICS members are encouraged to contribute walkthroughs! The more coverage we have, the stronger the whole team gets.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on writing and submitting walkthroughs.

---

## 📬 Questions?

Reach out to the **ICS CTF Coordinator** or post in the ICS Discord `#ctf-help` channel.

---

*This repository is for educational use by ICS members. Do not post flags or solutions to active (non-Gymnasium) NCL challenges.*
