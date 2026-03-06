# Log Analysis Easy - SSH

> **Category:** Log Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given an SSH authentication log file and asked to identify a brute force attack in progress. No special tools needed for this one, just `grep` and the ability to read log entries.

> 💡 This is a great first Log Analysis challenge because SSH logs are clean and readable. Once you understand the format, the answers jump out at you quickly.

---

## 🛠️ Tools Needed

- Kali Linux terminal or any text editor
- `grep` (pre-installed on Kali)
- The `auth.log` file downloaded from the challenge

---

## 📚 Understanding SSH Log Format

Before diving in, here's how to read an SSH log entry:

```
Oct 11 10:12:25 myraptor sshd[29465]: Failed password for harvey from 169.139.243.218 port 57273 ssh2
```

Breaking it down:
- `Oct 11 10:12:25` - timestamp
- `myraptor` - the hostname of the server
- `sshd[29465]` - the SSH daemon process and its PID
- `Failed password for harvey` - the event (failed login attempt for user harvey)
- `from 169.139.243.218` - the IP address the attempt came from
- `port 57273 ssh2` - the port and protocol used

A successful login looks like:
```
Oct 11 10:36:59 myraptor sshd[30003]: Accepted password for harvey from 30.167.206.91 port 55326 ssh2
```

Same format, but `Accepted password` instead of `Failed password`.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Find the Hostname

Download `auth.log` and open it or run:

```bash
head -5 auth.log
```

The hostname is the word that appears directly after the timestamp on every single line. It's the name of the server that recorded these logs. Your answer is one word.

---

### Step 2 - Q2, Q3, Q4: Find the Attacking IP Addresses

Search for all failed password attempts:

```bash
grep "Failed password" auth.log
```

You'll see a large number of failed login attempts coming in rapid succession from multiple IP addresses. This is a classic **brute force attack**, where an attacker tries thousands of password combinations hoping one works.

Look at the IP addresses in the `from` field. The first IP to appear is Q2, the second unique IP is Q3, and the third unique IP is Q4.

To see just the IP addresses in order:

```bash
grep "Failed password" auth.log | awk '{print $11}' | uniq
```

This extracts just the IP column and removes consecutive duplicates so you can see the order they appeared clearly.

> 💡 Notice how the same IP sends hundreds of attempts before switching to a new one. That's the signature of an automated brute force tool cycling through IPs to avoid detection.

---

### Step 3 - Q5: Find the Targeted User

Look at any `Failed password` line and find the username in the `for` field:

```bash
grep "Failed password" auth.log | head -1
```

Every failed attempt targets the same user. That's your answer for Q5.

---

### Step 4 - Q6: Find the Successful Login IP

Search for the line where the attacker finally got in:

```bash
grep "Accepted password" auth.log
```

You'll see exactly one line with `Accepted password`. The IP address in that line is your answer for Q6.

> 💡 Notice anything interesting about Q6's answer compared to Q2, Q3, and Q4? The attacker eventually succeeded from one of the same IPs that was brute forcing. That's how brute force attacks work: keep trying until one password works, then log in from that same session.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** It's an animal name. Look at the second word on any log line after the timestamp.
- **Q2:** The first failed attempt happens within seconds of the server starting. It's a 12-digit IP address in the 169.x.x.x range.
- **Q3:** The second wave of attacks comes from a different IP in the 56.x.x.x range.
- **Q4:** The third IP is in the 30.x.x.x range. You may recognize it from somewhere else in the challenge.
- **Q5:** A first name. The kind of name a person on a TV show about lawyers might have.
- **Q6:** Look at Q4 again. The attacker who eventually got in was already in the failed attempts list.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit IP addresses with typos.** Copy them directly from the log output, don't retype.
- ❌ **Don't confuse the attacking IPs with the server's own IP.** You're looking for the `from` field, not the server address.
- ✅ **The `uniq` command** in the grep pipeline removes consecutive duplicates making it easy to see when the IP switched.
- ✅ **There is only one `Accepted password` line** in the entire log. That's your Q6 answer.

---

## 🧠 Why This Works

This challenge simulates a real SSH brute force attack, one of the most common attack types seen in the wild. Any SSH server exposed to the internet will see thousands of brute force attempts daily. Security teams monitor auth logs exactly like this to detect compromised accounts and block attacking IPs. Tools like `fail2ban` automate this process by watching for multiple failed attempts from the same IP and automatically blocking them. Understanding what a brute force attack looks like in logs is a fundamental defensive security skill.

---

## 🔗 Resources

- [SSH Log Analysis Guide](https://www.loggly.com/use-cases/ssh-log-analysis/)
- [fail2ban Documentation](https://www.fail2ban.org/wiki/index.php/Main_Page)

---

*Written by: Mo | Last updated: February 2026*
