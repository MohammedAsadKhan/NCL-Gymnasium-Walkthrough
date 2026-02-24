# 🛠️ Tools & Resources Guide

A setup guide for every tool you'll need across NCL categories. Install these before the Gymnasium opens.

---

## 🔍 OSINT

| Tool | Purpose | Link |
|---|---|---|
| **Google Dorking** | Advanced search operators to find hidden info | [Guide](https://www.exploit-db.com/google-hacking-database) |
| **Shodan** | Search engine for internet-connected devices | [shodan.io](https://www.shodan.io) |
| **ExifTool** | Extract metadata from images/files | [exiftool.org](https://exiftool.org) |
| **WHOIS Lookup** | Domain registration info | [whois.domaintools.com](https://whois.domaintools.com) |
| **Reverse Image Search** | Google Images, TinEye, Yandex | — |
| **Maltego (Community)** | Link analysis and data visualization | [maltego.com](https://www.maltego.com) |

---

## 🔐 Cryptography

| Tool | Purpose | Link |
|---|---|---|
| **CyberChef** | All-in-one encoding/decoding/crypto tool | [gchq.github.io/CyberChef](https://gchq.github.io/CyberChef) |
| **dCode.fr** | Cipher identifier and decoder | [dcode.fr](https://www.dcode.fr/en) |
| **RsaCtfTool** | RSA attack automation | [GitHub](https://github.com/RsaCtfTool/RsaCtfTool) |
| **Python 3** | Custom scripts for crypto challenges | — |

---

## 📋 Log Analysis

| Tool | Purpose | Link |
|---|---|---|
| **grep / awk / cut** | Command-line log parsing (Linux/Mac/WSL) | Built-in |
| **Splunk Free** | GUI-based log analysis | [splunk.com](https://www.splunk.com/en_us/download.html) |
| **Excel / Google Sheets** | Filtering and pivot tables for structured logs | — |

---

## 🌐 Network Traffic Analysis

| Tool | Purpose | Link |
|---|---|---|
| **Wireshark** | GUI packet capture and analysis | [wireshark.org](https://www.wireshark.org) |
| **tshark** | Command-line Wireshark | Bundled with Wireshark |
| **NetworkMiner** | Passive network forensics | [netresec.com](https://www.netresec.com/?page=NetworkMiner) |

---

## 🔑 Password Cracking

| Tool | Purpose | Link |
|---|---|---|
| **Hashcat** | GPU-accelerated hash cracking | [hashcat.net](https://hashcat.net) |
| **John the Ripper** | CPU-based hash cracking | [openwall.com/john](https://www.openwall.com/john/) |
| **CrackStation** | Online hash lookup | [crackstation.net](https://crackstation.net) |
| **hash-identifier** | Identify unknown hash types | [GitHub](https://github.com/blackploit/hash-identifier) |

---

## 🔎 Scanning

| Tool | Purpose | Link |
|---|---|---|
| **Nmap** | Port scanning and service enumeration | [nmap.org](https://nmap.org) |
| **Gobuster** | Directory/DNS brute forcing | [GitHub](https://github.com/OJ/gobuster) |
| **Nikto** | Web server vulnerability scanner | [cirt.net/Nikto2](https://cirt.net/Nikto2) |

---

## 🕸️ Web Application

| Tool | Purpose | Link |
|---|---|---|
| **Burp Suite Community** | Intercept and modify web requests | [portswigger.net](https://portswigger.net/burp) |
| **curl** | Command-line HTTP requests | Built-in on Linux/Mac |
| **Browser DevTools** | Inspect source, cookies, network | Built into all browsers |

---

## 💡 Setup Recommendation

If you're on Windows, install **WSL2 (Ubuntu)** — most CTF tools work best on Linux and this gives you a full Linux environment without dual-booting.

```bash
# WSL2 quick install (PowerShell as Admin)
wsl --install
```

---

*Last updated by ICS CTF Coordinator*
