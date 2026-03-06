# Log Analysis Easy - VSFTPD

> **Category:** Log Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a VSFTPD (FTP server) log file and asked to analyze user activity, file uploads, downloads, and identify a suspicious login. This challenge teaches the `awk` command which is essential for more advanced log parsing.

> 💡 VSFTPD stands for "Very Secure FTP Daemon." It's a common Linux FTP server. The logs record every login, upload, download, and command run by each user, which makes them very useful for forensic analysis.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `grep`, `awk`, `sort`, `uniq`, `head`, `tail` (all pre-installed on Kali)
- The `vsftpd.log` file downloaded from the challenge

---

## 📚 Understanding the Log Format

Peek at the log first:

```bash
head vsftpd.log
```

Each line contains a timestamp, process ID, event type, username, IP address, and other details. The fields aren't cleanly tab-separated like the Login challenge, so this one uses `awk` with custom delimiters to extract specific pieces.

Key event types you'll see:
- `OK LOGIN` - successful login
- `OK UPLOAD` - successful file upload
- `OK DOWNLOAD` - successful file download
- `MKD` or `mkdir` - directory creation

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Find ftpuser's First Login IP

Search all entries for ftpuser and look for the login event:

```bash
cat vsftpd.log | grep ftpuser | head -20
```

Look for the line containing `OK LOGIN` or the initial connection. The IP address is visible in that entry.

> 💡 **What the answer looks like:** A private network IP address starting with `10.x.x.x`.

---

### Step 2 - Q2: First Directory ftpuser Created

```bash
cat vsftpd.log | grep ftpuser | grep -i mkdir | head -n 1
```

What each part does:
- `grep ftpuser`: filter to ftpuser's activity only
- `grep -i mkdir`: find directory creation events (case-insensitive)
- `head -n 1`: show only the first result

The directory name is visible in that line. Your answer is just the directory name, not the full path.

> 💡 **What the answer looks like:** A software application name that sounds like it measures file sizes.

---

### Step 3 - Q3: Last Directory ftpuser Created

Same command but use `tail` instead of `head`:

```bash
cat vsftpd.log | grep ftpuser | grep -i mkdir | tail -n 1
```

> 💡 **What the answer looks like:** A mix of numbers and uppercase letters, looks like a model or product code.

---

### Step 4 - Q4: Most Used File Extension by ftpuser

This one uses `awk` with custom delimiters to isolate the file extension from upload entries:

```bash
cat vsftpd.log | grep ftpuser | grep 'OK UPLOAD' | awk -F ',' '{print $2}' | awk -F '.' '{print $2}' | sort | uniq -c | sort
```

Breaking it down:
- `grep 'OK UPLOAD'`: filter to only successful uploads
- `awk -F ',' '{print $2}'`: use comma as delimiter and extract the file path (second field)
- `awk -F '.' '{print $2}'`: use period as delimiter and extract the file extension (after the dot)
- `sort | uniq -c | sort`: count each extension and sort by frequency

The extension with the highest count is your answer. Submit it in uppercase.

> 💡 **What the answer looks like:** A very common image file format. Three letters.

---

### Step 5 - Q5: Find the Other Username

Extract the 8th column from all log entries to see all usernames:

```bash
cat vsftpd.log | awk '{print $8}' | sort | uniq
```

You'll see a short list of values. One of them is a real username that isn't `ftpuser`. That's your answer.

> 💡 **What the answer looks like:** A common first name.

---

### Step 6 - Q6: Other User's Login IP

Now that you have the username, grep for their entries:

```bash
cat vsftpd.log | grep jimmy | head -10
```

Look for the `OK LOGIN` line which will show the IP address they connected from.

> 💡 **What the answer looks like:** Another private `10.x.x.x` address, different from ftpuser's.

---

### Step 7 - Q7: Total Bytes Uploaded by the Other User

```bash
cat vsftpd.log | grep jimmy | grep 'OK UPLOAD' | awk -F ',' '{print $3}' | awk '{s+=$1} END {print s}'
```

What the new parts do:
- `awk -F ',' '{print $3}'`: extracts the byte count field (third comma-delimited field)
- `awk '{s+=$1} END {print s}'`: adds up all the byte values into a running total and prints the sum at the end

> 💡 **What the answer looks like:** A 9-digit number in the hundreds of millions.

---

### Step 8 - Q8: Total Bytes Uploaded by ftpuser

Same command but for ftpuser:

```bash
cat vsftpd.log | grep ftpuser | grep 'OK UPLOAD' | awk -F ',' '{print $3}' | awk '{s+=$1} END {print s}'
```

> 💡 **What the answer looks like:** An 11-digit number. ftpuser uploaded a LOT more than jimmy.

---

### Step 9 - Q9: Total Bytes Downloaded by ftpuser

Same pattern but switch `OK UPLOAD` to `OK DOWNLOAD`:

```bash
cat vsftpd.log | grep ftpuser | grep 'OK DOWNLOAD' | awk -F ',' '{print $3}' | awk '{s+=$1} END {print s}'
```

> 💡 **What the answer looks like:** A 7-digit number. Much less than the upload total.

---

### Step 10 - Q10: Find the Suspicious Login IP

Find all successful logins and their IP addresses:

```bash
cat vsftpd.log | grep 'OK LOGIN' | awk -F '"' '{print $2}' | sort | uniq -c
```

What this does:
- `grep 'OK LOGIN'`: filter to successful logins only
- `awk -F '"' '{print $2}'`: use double quote as delimiter and extract the IP address
- `sort | uniq -c`: count how many times each IP logged in

You'll see a few IPs with many logins and one IP that only appears once with no other activity in the log. That single-login-no-activity IP is the suspicious one.

> 💡 **What the answer looks like:** A `10.3.x.x` address that you'll only see one time in the entire log. Every other IP has lots of subsequent activity. This one logs in and nothing else happens, which is exactly what a reconnaissance login or a failed intrusion attempt looks like.

---

## ⚠️ Accuracy Tips

- ❌ **Don't include extra spaces or quotes** when submitting byte counts or IP addresses. Copy directly from terminal output.
- ❌ **Don't confuse upload and download** for Q8 and Q9. Double check you used `OK UPLOAD` vs `OK DOWNLOAD` for the right question.
- ✅ **The `awk '{s+=$1} END {print s}'` pattern** is your best friend for summing numbers in log files. Memorize it.
- ✅ **For Q10**, the suspicious IP stands out because it has exactly 1 login and nothing else. All legitimate users have uploads, downloads, or directory creation activity following their login.

---

## 🧠 Why This Works

FTP logs are a goldmine for forensic investigators. This challenge demonstrates several real-world analysis techniques: identifying user activity patterns, calculating data exfiltration volumes (how many bytes were uploaded), and detecting suspicious logins that don't match normal behavior. The single-login-no-activity pattern in Q10 is a classic indicator of credential testing, where an attacker verifies that stolen credentials work before launching a larger attack. Security teams monitor for exactly this pattern using SIEM tools that automate the same `grep` and `awk` logic you just ran manually.

---

## 🔗 Resources

- [awk command guide](https://linux.die.net/man/1/awk)
- [VSFTPD Documentation](https://security.appspot.com/vsftpd.html)

---

*Written by: Mo | Last updated: February 2026*
