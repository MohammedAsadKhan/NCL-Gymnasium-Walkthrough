# 📋 Log Analysis Walkthroughs

Parsing through logs to find suspicious activity, failed logins, intrusions, and attacker behavior.

---

## A Word Before You Start

Log Analysis is one of those categories that looks straightforward until you're staring at thousands of lines of raw log data trying to find the one thing that matters. The challenges here range from simple pattern matching to writing custom parsers for unusual log formats.

The key skill is learning to use `grep`, `awk`, `cut`, and other Linux text processing tools to filter the noise and isolate exactly what you need. Don't try to read logs manually line by line. Let the tools do the work.

> 💡 If you're stuck on a challenge, don't guess. A wrong answer in Log Analysis hurts your accuracy score more than skipping it. Take your time, re-read the log carefully, and ask for help in the NCL Discord if needed.

---

## What to Expect in NCL Log Analysis

You'll be given log files from various services (SSH, FTP, web servers, databases) and asked questions about what happened. You need to identify things like failed login attempts, successful intrusions, suspicious IP addresses, commands run by attackers, and more.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [ssh.md](easy/ssh.md) | Analyzing SSH authentication logs |
| [login.md](easy/login.md) | Analyzing system login logs |
| [vsftpd.md](easy/vsftpd.md) | Analyzing VSFTPD FTP server logs |

### 🟡 Medium
| File | Topic |
|---|---|
| [nginx.md](medium/nginx.md) | Analyzing Nginx web server access logs |
| [history.md](medium/history.md) | Analyzing bash command history logs |

### 🔴 Hard
| File | Topic |
|---|---|
| [squid.md](hard/squid.md) | Analyzing Squid proxy logs |
| [payments.md](hard/payments.md) | Analyzing payment transaction logs |
| [custom-file-format.md](hard/custom-file-format.md) | Parsing and analyzing a custom log format |

---

## Log Analysis Quick Reference

**Search for a pattern:**
```bash
grep "pattern" logfile.txt
```

**Search case-insensitively:**
```bash
grep -i "pattern" logfile.txt
```

**Count occurrences:**
```bash
grep -c "pattern" logfile.txt
```

**Show line numbers:**
```bash
grep -n "pattern" logfile.txt
```

**Extract a specific field (e.g. field 4, space-delimited):**
```bash
awk '{print $4}' logfile.txt
```

**Cut a specific column (e.g. column 2, colon-delimited):**
```bash
cut -d':' -f2 logfile.txt
```

**Sort and count unique occurrences:**
```bash
sort logfile.txt | uniq -c | sort -rn
```

**Combine tools with pipes:**
```bash
grep "Failed" logfile.txt | awk '{print $11}' | sort | uniq -c | sort -rn
```

---

*Written by: Mo | Last updated: February 2026*
