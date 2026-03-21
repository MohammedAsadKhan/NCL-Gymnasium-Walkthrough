# 🛡️ NCL Gymnasium Walkthroughs

> **Maintained by Mo | Texas A&M University - Corpus Christi**

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

Each category has its own folder containing individual `.md` files for each challenge along with an `images/` folder for screenshots used in the walkthroughs. Every category covers easy, medium, and hard challenges where applicable.

```
ics-ncl-walkthroughs/
├── OSINT/
├── Cryptography/
├── Password-Cracking/
├── Forensics/
├── Log-Analysis/
├── Enumeration-and-Exploitation/
├── Scanning/
├── Network-Traffic-Analysis/
├── Web-Application/
├── Wireless-Access-Exploitation/
├── templates/
│   └── challenge-template.md   ← Use this when writing new walkthroughs
└── resources/
    └── tools.md                ← Recommended tools per category
```

---

## 🗂️ Categories

| Category | Status | Challenges Covered |
|---|---|---|
| 🔍 OSINT | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: N/A |
| 🔐 Cryptography | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 🔑 Password Cracking | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 🕵️ Forensics | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 📋 Log Analysis | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 🔎 Scanning & Recon | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 📡 Wireless Access Exploitation | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 💻 Enumeration & Exploitation | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 🌐 Network Traffic Analysis | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |
| 🕸️ Web Application | ✅ Complete | Easy: ✅ \| Medium: ✅ \| Hard: ✅ |

---

## 🚀 How to Use This Repo

**As a competitor:**
1. Open the folder for the category you're working on
2. Start with the easy challenges and work up — don't skip difficulty levels
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
| Password Cracking | Hashcat, John the Ripper, CrackStation |
| Forensics | Wireshark, Volatility3, Binwalk, ExifTool, strings, sqlite3 |
| Log Analysis | grep, awk, cut, sort, uniq, sqlite3, LibreOffice Calc |
| Scanning & Recon | Nmap, Netcat, curl, dig, git |
| Wireless Access Exploitation | aircrack-ng, Wireshark |
| Enumeration & Exploitation | GDB, Ghidra, uncompyle6, JD-GUI, Python |
| Network Traffic Analysis | Wireshark, tshark, CyberChef |
| Web Application | Firefox DevTools, Burp Suite (Community), curl, CyberChef |

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

Reach out in the ICS Discord `#ncl` channel.

---

*This repository is for educational use by ICS members. Do not post flags or solutions to active (non-Gymnasium) NCL challenges.*
