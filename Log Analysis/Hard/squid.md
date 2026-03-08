# Log Analysis Hard - Squid

> **Category:** Log Analysis
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a Squid proxy log and asked to analyze request timing, count unique clients, identify HTTP methods, and track down an antivirus update URL. The tricky part is that the timestamps are in epoch format and the log structure is different from anything you've seen in the previous challenges.

> 💡 If you get stuck, the official NCL YouTube tutorial walks through this challenge in detail: [NCL Summer Live - Log Analysis 2](https://www.youtube.com/watch?v=i2n9qMdLvHM)

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `awk`, `sort`, `uniq`, `grep`, `wc`, `cat` (all pre-installed on Kali)
- `date` command (pre-installed on Kali) or [Epoch Converter](https://www.epochconverter.com/)
- The `squid_access.log` file downloaded from the challenge

---

## 📚 Understanding the Squid Log Format

Peek at the log first:

```bash
head squid_access.log
```

Each line looks something like this:

```
1285043050.857    532 192.168.0.105 TCP_MISS/200 5298 GET http://example.com/ - DIRECT/1.2.3.4 text/html
```

The fields map to:

| Field | Content |
|---|---|
| 1 | Epoch timestamp (seconds since Jan 1, 1970) |
| 2 | Time spent processing the request (milliseconds) |
| 3 | Client IP address |
| 4 | Squid result code / HTTP status |
| 5 | Bytes transferred |
| 6 | HTTP method (GET, POST, etc.) |
| 7 | Requested URL |
| 8 | Username (usually `-`) |
| 9 | Peer connection info |
| 10 | Content type |

> 💡 The full Squid log format reference is at [wiki.squid-cache.org](https://wiki.squid-cache.org/Features/LogFormat) if you want to dig deeper.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: What Year Was This Log Saved?

The first field is an epoch timestamp, a number representing seconds elapsed since January 1, 1970. It looks weird but is easy to convert.

Grab a timestamp from the log:

```bash
head -1 squid_access.log | awk '{print $1}'
```

Then convert it using the `date` command:

```bash
date -d @1285043050
```

Replace `1285043050` with the actual timestamp from your log. The output gives you the full human-readable date. Your answer is just the year.

Or paste the number into [Epoch Converter](https://www.epochconverter.com/) if you prefer a web tool.

> 💡 **What the answer looks like:** A year in the early 2010s. A simpler time before Bitcoin was worth anything.

---

### Step 2 - Q2 and Q3: Fastest and Slowest Request

The second field is the request processing time in milliseconds. Extract it and sort numerically:

```bash
cat squid_access.log | awk '{print $2}' | sort -n
```

- The **first number** at the top is the fastest request in milliseconds (Q2)
- The **last number** at the bottom is the slowest request in milliseconds (Q3)

> 💡 `sort -n` sorts numerically instead of alphabetically. Without the `-n` flag, `10` would sort before `9` because it starts with a `1`. Always use `-n` when sorting numbers.

Add `| head -1` or `| tail -1` to just see the answer without scrolling:

```bash
cat squid_access.log | awk '{print $2}' | sort -n | head -1
cat squid_access.log | awk '{print $2}' | sort -n | tail -1
```

---

### Step 3 - Q4: Count Unique Client IP Addresses

Extract field 3 (client IP), deduplicate, and count:

```bash
cat squid_access.log | awk '{print $3}' | sort | uniq | wc -l
```

> 💡 **What the answer looks like:** A single digit. This is a small internal network proxy, not a public server.

---

### Step 4 - Q5 and Q6: Count GET and POST Requests

Extract field 6 (HTTP method), sort, and count each unique value:

```bash
cat squid_access.log | awk '{print $6}' | sort | uniq -c
```

The output will show a count next to each HTTP method. Read off the GET count for Q5 and the POST count for Q6.

> ⚠️ If you copy the command from some sources you may see `uniq -c` with a different dash character that looks similar but isn't. If the command errors, retype it manually rather than copying and pasting.

---

### Step 5 - Q7: Find the Antivirus Company

Filter all log entries from the specific IP address mentioned in the question:

```bash
cat squid_access.log | grep "192.168.0.224"
```

Scroll through the URLs in the output. You'll see requests going to a domain associated with a major antivirus company. The company name is visible directly in the URLs being requested.

> 💡 **What the answer looks like:** One of the biggest names in antivirus software from the 2000s and 2010s. A household name in corporate security.

---

### Step 6 - Q8: Find the Antivirus Update URL

Still using the same grep output from Step 5, look through the URLs for one that contains words related to virus definitions. It will be a `.zip` file download URL.

```bash
cat squid_access.log | grep "192.168.0.224" | grep -i "virus"
```

The full URL is in field 7. To extract just the URL:

```bash
cat squid_access.log | grep "192.168.0.224" | grep -i "virus" | awk '{print $7}'
```

Submit the full URL exactly as it appears in the log including the `http://` prefix.

> ⚠️ **The URL contains `$20` sequences which represent URL-encoded spaces.** Submit the URL exactly as it appears in the log. Do not decode the `$20` to spaces or the answer will be wrong.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Convert any epoch timestamp from the log. They all fall in the same year. A year that starts with `2`.
- **Q2:** A single digit number. Some requests were extremely fast.
- **Q3:** A 5-digit number in the tens of thousands. Some requests were very slow.
- **Q4:** Less than 10 unique IPs. Small internal network.
- **Q5:** Less than 50 GET requests.
- **Q6:** More POST requests than GET requests. Unusual for most web traffic.
- **Q7:** The company name appears repeatedly in the domain names of the URLs being requested from `192.168.0.224`. One of the most recognized antivirus brands ever.
- **Q8:** Look for a URL with "virus" and "definitions" in it. It's a `.zip` file. The full URL is long. Copy it exactly.

---

## ⚠️ Accuracy Tips

- ❌ **Don't decode `$20` in the URL for Q8.** Submit it exactly as it appears in the log with the `$20` sequences intact.
- ❌ **Don't use alphabetical sort for Q2 and Q3.** Always use `sort -n` for numeric fields or you'll get wrong results.
- ✅ **Use `| head -1` and `| tail -1`** after `sort -n` to quickly grab the min and max without scrolling.
- ✅ **For Q7 and Q8**, grepping for the specific IP first and then piping to another grep for "virus" saves a lot of scrolling.

---

## 🧠 Why This Works

Squid is one of the most widely deployed proxy servers in enterprise networks. Proxy logs like this one are invaluable for security teams because every outbound request from every machine on the network passes through the proxy and gets logged. This means you can reconstruct exactly what websites each machine visited, how much data was transferred, and when. In this challenge, the antivirus update traffic from `192.168.0.224` is completely benign, but the same technique of grepping for a specific IP and analyzing its URLs is how SOC analysts identify compromised machines calling back to command-and-control servers, employees visiting unauthorized sites, or malware downloading payloads.

---

## 🔗 Resources

- [NCL Summer Live - Log Analysis 2](https://www.youtube.com/watch?v=i2n9qMdLvHM)
- [Epoch Converter](https://www.epochconverter.com/)
- [Squid Log Format Reference](https://wiki.squid-cache.org/Features/LogFormat)

---

*Written by: Mo | Last updated: February 2026*
