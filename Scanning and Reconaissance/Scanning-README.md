# 🔍 Scanning & Reconnaissance Walkthroughs

Mapping out targets, identifying open ports, enumerating services, and gathering intelligence before an attack.

---

## A Word Before You Start

Scanning and Reconnaissance is where every real penetration test begins. Before you can exploit anything, you need to know what's there. This category teaches you how to systematically gather information about a target: what ports are open, what services are running, what software versions are in use, and what metadata is hiding in files.

The skills here are foundational. If you're new to cybersecurity, this is one of the best categories to start with because the tools are straightforward and the results are immediately satisfying. Run a scan, see what's running. No guesswork.

> 💡 A word of caution for the real world: always make sure you have permission before scanning any system. Unauthorized port scanning is illegal in many jurisdictions. In NCL everything is a controlled environment and you have permission to scan the provided targets.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [nmap.md](easy/nmap.md) | Port scanning with nmap |
| [git.md](easy/git.md) | Enumerating a Git repository |

### 🟡 Medium
| File | Topic |
|---|---|
| [net-track.md](medium/net-track.md) | Network traffic analysis and tracking |

### 🔴 Hard
| File | Topic |
|---|---|
| [metadata.md](hard/metadata.md) | File metadata extraction and analysis |

---

## Scanning Quick Reference

**Basic TCP scan (top 1000 ports):**
```bash
nmap target.com
```

**Full TCP scan (all 65535 ports):**
```bash
nmap -p- target.com
```

**UDP scan:**
```bash
sudo nmap -sU target.com
```

**Version detection:**
```bash
nmap -sV target.com
```

**Skip ping check (use if host seems down):**
```bash
nmap -Pn target.com
```

**Aggressive scan (OS detection, version, scripts):**
```bash
nmap -A target.com
```

**Extract metadata from a file:**
```bash
exiftool filename
```

---

*Written by: Mo | Last updated: February 2026*
