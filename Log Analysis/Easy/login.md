# Log Analysis Easy - Login

> **Category:** Log Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a custom application login log in tab-delimited format. Using Linux command line tools, you'll answer questions about user behavior, login frequency, and suspicious patterns.

> 💡 This challenge is basically a tutorial on piping Linux commands together. Every question builds on the last one. By the end you'll have a solid toolkit for analyzing any log file.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `cat`, `head`, `tail`, `cut`, `sort`, `uniq`, `wc` (all pre-installed on Kali)
- The `login.log` file downloaded from the challenge

---

## 📚 Understanding the Log Format

First, peek at the log to understand its structure:

```bash
head login.log
```

The log uses **tab-delimited columns**, meaning each field is separated by a tab character. The columns are:

| Column | Field |
|---|---|
| 1 | Date and Time |
| 2 | IP Address |
| 3 | Username |

The `cut` command's default delimiter is a tab, which makes it perfect for extracting specific columns from this file.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Count Total Login Attempts

Each line in the log is one login attempt. Count the lines:

```bash
cat login.log | wc -l
```

`wc -l` counts lines in the input. That number is your answer.

---

### Step 2 - Q2: Count Unique Usernames

Extract the username column, sort it, deduplicate, and count:

```bash
cat login.log | cut -f 3 | sort | uniq | wc -l
```

What each part does:
- `cut -f 3`: extracts field 3 (the username column)
- `sort`: alphabetically sorts the usernames so identical ones are next to each other
- `uniq`: removes consecutive duplicates, leaving one of each
- `wc -l`: counts how many unique usernames remain

> ⚠️ Always `sort` before `uniq`. The `uniq` command only removes consecutive duplicates. If the same username appears on line 1 and line 500, `uniq` without `sort` won't catch it.

---

### Step 3 - Q3 and Q4: Username with Most Login Attempts

Get a frequency count of each username sorted by how many times they appear:

```bash
cat login.log | cut -f 3 | sort | uniq -c | sort -n
```

What each part does:
- `uniq -c`: counts how many times each consecutive entry appears
- `sort -n`: sorts numerically so the highest count is at the bottom

The last line of the output is the username with the most attempts. The number on the left is the count (Q4) and the word on the right is the username (Q3).

> 💡 **What the answers look like:** Q3 is a short username that looks like a first name abbreviation. Q4 is a three digit number.

---

### Step 4 - Q5: Date with Most Login Attempts

Extract the date from the first column, count by date, and sort:

```bash
cat login.log | cut -f 1 | cut -d " " -f 1 | sort | uniq -c | sort -n
```

What each part does:
- `cut -f 1`: extracts the first column (date and time combined)
- `cut -d " " -f 1`: splits by space and takes just the date part, dropping the time
- `sort | uniq -c | sort -n`: same frequency count pattern as before

The last line shows the date with the most activity. Your answer is in `YYYY-MM-DD` format.

---

### Step 5 - Q6: Username with Most Unique IP Addresses

This one is more complex. You want to find which user logged in from the most different IP addresses:

```bash
cat login.log | cut -f 2,3 | sort | uniq | cut -f 2 | sort | uniq -c | sort -n
```

Breaking it down step by step:
- `cut -f 2,3`: extracts IP address and username together as pairs
- `sort | uniq`: gets unique IP/username pairs (same IP and same user counts as one)
- `cut -f 2`: from those unique pairs, extract just the username
- `sort | uniq -c | sort -n`: count how many unique IPs each username had, sort by frequency

The last line is the username with the most unique IP addresses. This is a potential indicator of a compromised account being accessed from many different locations.

> 💡 **What the answer looks like:** A username that looks like a mix of letters and numbers, similar to an auto-generated account name.

---

## ⚠️ Accuracy Tips

- ❌ **Never use `uniq` without `sort` before it.** You'll get wrong counts every time.
- ❌ **Don't confuse Q3 and Q4.** The number is Q4, the username is Q3.
- ✅ **The highest value is always at the bottom** when using `sort -n`. Scroll to the end of the output.
- ✅ **Copy usernames exactly** from the terminal output. Case matters.
- ✅ **Add `| tail -5`** to the end of any command to just see the top 5 results instead of scrolling through everything:
```bash
cat login.log | cut -f 3 | sort | uniq -c | sort -n | tail -5
```

---

## 🧠 Why This Works

The pipe (`|`) chain pattern used in this challenge is one of the most powerful concepts in Linux. Instead of writing a custom program, you chain simple single-purpose tools together where each one does one thing well. `cut` extracts, `sort` orders, `uniq` deduplicates, `wc` counts. This is the Unix philosophy in action and it's the same approach security analysts use to process gigabyte-sized log files without specialized software. Learning to build these pipelines fluently is a skill that transfers to every log analysis challenge in NCL and in real security work.

---

## 🔗 Resources

- [Linux cut command](https://linux.die.net/man/1/cut)
- [Linux uniq command](https://linux.die.net/man/1/uniq)
- [Linux sort command](https://linux.die.net/man/1/sort)

---

*Written by: Mo | Last updated: February 2026*
