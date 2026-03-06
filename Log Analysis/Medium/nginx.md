# Log Analysis Medium - Nginx

> **Category:** Log Analysis
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given an Nginx web server access log and asked to analyze traffic patterns, identify specific visitors, detect attack attempts, and parse raw byte sequences. This challenge introduces `awk`, `egrep`, and escape sequences.

> 💡 If you want a video walkthrough alongside this guide, the official NCL tutorial covers this challenge: [NCL Summer Live - Log Analysis 1](https://www.youtube.com/watch?v=log-analysis-1)

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `cat`, `cut`, `grep`, `egrep`, `awk`, `sort`, `uniq`, `wc` (all pre-installed on Kali)
- The `access.log` file downloaded from the challenge

---

## 📚 Understanding the Nginx Log Format

Peek at the log first:

```bash
head access.log
```

Each line looks like this:

```
192.168.1.1 - - [11/Oct/2023:10:12:00 +0000] "GET /index.html HTTP/1.1" 200 512 "-" "Mozilla/5.0"
```

Key fields from left to right:
- Field 1: **IP address**
- Fields 2-3: identifiers (usually `-`)
- Field 4: **timestamp** in brackets
- Field 5: **HTTP request** in quotes (method, path, protocol)
- Field 6: **HTTP status code**
- Field 7: bytes sent
- Field 8: referrer in quotes
- Field 9: **user agent** in quotes

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Count Unique IP Addresses

```bash
cat access.log | cut -d " " -f 1 | sort | uniq | wc -l
```

- `cut -d " " -f 1`: uses space as delimiter and extracts the first field (IP address)
- `sort | uniq`: deduplicates
- `wc -l`: counts unique IPs

---

### Step 2 - Q2 and Q3: Count Requests by Status Code

Extract the HTTP status codes and count each one:

```bash
cat access.log | cut -d '"' -f 3 | cut -d ' ' -f 2 | sort | uniq -c | sort -rn
```

What each part does:
- `cut -d '"' -f 3`: uses double quote as delimiter and extracts the third field, which is everything after the HTTP request (status code and bytes)
- `cut -d ' ' -f 2`: splits by space and takes the second field, which is the status code
- `sort | uniq -c | sort -rn`: counts each code and sorts highest first

Look through the output for `200` and `400` counts for your Q2 and Q3 answers.

> 💡 **What the answers look like:** Both are small two digit numbers. More requests got 400 errors than 200 success responses, which is unusual and worth noting.

---

### Step 3 - Q4: Find the IP That "Rang the Doorbell"

```bash
cat access.log | grep "bell"
```

One log entry contains the word "bell" in the request URL. The IP address at the start of that line is your answer.

---

### Step 4 - Q5: Find the Googlebot Version

```bash
cat access.log | grep "Googlebot"
```

Find the line that mentions Googlebot in the user agent. The version number follows `Googlebot/`. Your answer is just the version number.

> 💡 **What the answer looks like:** Two numbers separated by a period.

---

### Step 5 - Q6: Find the Shellshock Attack IP

Shellshock was a critical bash vulnerability where attackers injected commands using this character sequence: `() { :; };`

Search for it:

```bash
cat access.log | grep '() { :; };'
```

The IP address at the start of the matching line is your answer.

> 💡 Shellshock exploits work by injecting the `() { :; };` payload into HTTP headers. When a vulnerable server processes the request, bash executes the injected commands. It was one of the most serious vulnerabilities of 2014 and is still found in older systems.

---

### Step 6 - Q7: Most Popular Firefox Version

```bash
cat access.log | egrep -o "Firefox/.*" | sort | uniq -c | sort -rn
```

What each part does:
- `egrep -o "Firefox/.*"`: the `-o` flag prints ONLY the matching part of each line, not the whole line. This extracts just `Firefox/version` from the user agent strings
- `sort | uniq -c | sort -rn`: counts each version and sorts highest first

The version number at the top of the output (after `Firefox/`) is your answer.

> 💡 **What the answer looks like:** A two digit number followed by `.0`.

---

### Step 7 - Q8 and Q9: Most Common HTTP Methods

```bash
cat access.log | awk -F " " '{print $6}' | sort | uniq -c | sort -rn
```

What each part does:
- `awk -F " " '{print $6}'`: uses whitespace as delimiter and prints the 6th field, which is the HTTP method (GET, POST, CONNECT, etc.) from inside the request string

The top result is Q8, the second result is Q9.

> 💡 **Why awk instead of cut here?** `awk` treats any amount of whitespace as a single delimiter by default, which handles the log format more reliably than `cut` when fields have variable spacing.

---

### Step 8 - Q10: Count Requests for a Raw Byte Sequence

This one requires careful escaping. The sequence `\x04\x01\x00P\xC6\xCE\x0Eu0\x00` contains backslashes that need to be escaped so the shell passes them to grep correctly:

```bash
cat access.log | grep '\\x04\\x01\\x00P\\xC6\\xCE\\x0Eu0\\x00' | wc -l
```

> ⚠️ Each backslash in the original sequence needs to be doubled (`\\`) in the grep command. Without this, the shell interprets `\x04` as an escape sequence and converts it to the ASCII character `A` before grep even sees it. The double backslash tells the shell to pass a literal backslash to grep.

The line count is your answer.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Less than 50 unique IPs. A small server.
- **Q2:** Less than 20 successful requests. Fewer than you'd expect.
- **Q3:** More than double the 200 count. Something was hammering this server with bad requests.
- **Q4:** The URL path in that request literally contains the word "doorbell." One specific IP made that request.
- **Q5:** A version number you'd see on an older browser. Two parts separated by a dot.
- **Q6:** The Shellshock payload is distinctive. One IP, one attempt.
- **Q7:** A popular Firefox version from around 2014. Two digit version number.
- **Q8:** The most common HTTP method on any web server is always the same one.
- **Q9:** A less common method used by proxies and tunneling tools.
- **Q10:** A single digit number. Not many of these requests made it through.

---

## ⚠️ Accuracy Tips

- ❌ **Don't forget to double the backslashes in Q10.** Single backslashes will give you a wrong count because grep searches for the wrong pattern.
- ❌ **Don't include the `Firefox/` prefix in Q7.** Just the version number.
- ❌ **Don't include quotes in Q8 and Q9.** The method names are plain text like `GET` and `CONNECT`.
- ✅ **Use `sort -rn` to put the highest counts first** so you don't have to scroll to the bottom.
- ✅ **For Q6**, Google "Shellshock vulnerability" if you're curious about what it is. Understanding the attack makes it easier to spot in logs.

---

## 🧠 Why This Works

Nginx access logs are one of the most commonly analyzed log types in security operations. Web servers are internet-facing and constantly receive probes, scans, and attack attempts alongside legitimate traffic. The techniques here, counting status codes, identifying attack signatures, parsing user agents, detecting anomalous requests, are the same ones used in real SOC (Security Operations Center) workflows. The Shellshock exploit detection in Q6 is a real attack pattern that security tools still scan for because many older systems never got patched.

---

## 🔗 Resources

- [Nginx Log Format Documentation](https://nginx.org/en/docs/http/ngx_http_log_module.html)
- [Shellshock Vulnerability - Wikipedia](https://en.wikipedia.org/wiki/Shellshock_(software_bug))
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

---

*Written by: Mo | Last updated: February 2026*
