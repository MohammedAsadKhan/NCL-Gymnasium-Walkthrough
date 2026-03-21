# Network Traffic Analysis Easy - Telnet

> **Category:** Network Traffic Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a Telnet packet capture to extract login credentials, identify commands run on the remote machine, and determine system information about the host that was accessed.

> 💡 Telnet is basically SSH's embarrassing older sibling that never learned about encryption. Everything, your username, your password, every command you type, every response you get, travels across the network in plain unencrypted text. It was deprecated decades ago for exactly this reason, but it still shows up in legacy systems, IoT devices, and old network equipment.

---

## 📖 A Brief History

Telnet was developed in 1969, making it one of the oldest internet protocols still in existence. For years it was the standard way to remotely log into and administer computers. Then SSH came along in 1995 and did everything Telnet did but with actual encryption. The cybersecurity community's response was essentially "oh thank goodness" and slowly but surely Telnet was replaced. But slowly is the key word. Even today you'll find old routers, switches, and embedded systems still running Telnet because nobody got around to updating them. For a penetration tester, a Telnet service is essentially a neon sign flashing "come read my passwords."

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali) or the web-based **CloudShark** tool if provided
- The `Telnet.pcap` file downloaded from the challenge

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Follow the TCP Stream

Open the PCAP in Wireshark:

```bash
wireshark Telnet.pcap
```

Right-click on any packet and select **Follow → TCP Stream**.

This assembles the entire Telnet session into a readable conversation. Everything in **blue** is sent by the client (the person typing). Everything in **red** is the server's response.

> ⚠️ **Important:** Telnet echoes back everything you type. This means each character you type appears twice in the raw capture, once sent by the client and once echoed back by the server. The TCP Stream view handles this for you, but keep it in mind if anything looks duplicated.

> ⚠️ **Watch out for periods at the end of lines.** The login prompt and password prompt end with a period that is NOT part of the credential. Don't include trailing periods in your answers.

---

### Q1 - Username

In the TCP stream, look for the login prompt. The username is typed by the client (blue text) in response to the `login:` prompt.

> 💡 **What it looks like:** A short, simple test username. Four letters.

---

### Q2 - Password

Look for the `Password:` prompt in the stream. The password follows it.

> 💡 **Note:** Passwords are sometimes not echoed back in Telnet sessions, so they may only appear once in the stream rather than twice. Look carefully.
> 💡 **What it looks like:** A single common English word related to what this file is.

---

### Q3 - Command Executed After Login

After the successful login, look at what the user typed. This is the first command they ran on the remote machine.

> 💡 **What it looks like:** Two words separated by a space and a dash. A very common Linux command for checking system information. Look it up if you don't know it, understanding what it does will answer Q4, Q5, and Q6 automatically.

---

### Q4 - Year the Capture Was Created

Look at the output of the command from Q3 in the stream. The server's response contains detailed system information including a date. That date tells you when the system was built, which corresponds to when the capture was created.

> 💡 **What it looks like:** A 4-digit year in the early 2010s.

---

### Q5 - Hostname of the Remote Machine

The output of the Q3 command also includes the hostname of the machine. It's two parts: the OS name followed by the device identifier.

> 💡 **What it looks like:** Two words. The first is the operating system name and the second is an alphanumeric device identifier starting with `cm`.

---

### Q6 - CPU Architecture of the Remote Machine

Also in the Q3 command output. The CPU architecture is listed toward the end of the response line.

> 💡 **What it looks like:** A lowercase string starting with `arm`. This is an ARM processor, commonly found in embedded systems and older network devices. ARM architecture is what powers most smartphones and Raspberry Pis too.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Follow the TCP stream and look at the blue text after the `login:` prompt. Short username, all lowercase.
- **Q2:** Look after the `Password:` prompt. One word, all lowercase, related to packet captures.
- **Q3:** First command after login. Two parts separated by a dash flag. Google it to understand what information it returns.
- **Q4:** The command output includes a timestamp with the year. Early 2010s.
- **Q5:** Two words in the command output. OS name + device model number starting with `cm`.
- **Q6:** In the command output, look for the architecture field. Starts with `arm`, includes version info.

---

## ⚠️ Accuracy Tips

- ❌ **Don't include trailing periods** in your username or password answers. The prompts end with periods that are not part of the credentials.
- ❌ **Don't include just `Linux` for Q5.** The full hostname answer is two words.
- ✅ **Google the Q3 command** if you don't recognize it. Its output format directly answers Q4, Q5, and Q6.
- ✅ **Follow the TCP stream** rather than reading individual packets. Telnet spreads each character across separate packets which makes individual packet reading a nightmare.

---

## 🧠 Why This Works

Telnet has no encryption, no authentication beyond username and password, and no integrity checking. When you follow the TCP stream in Wireshark you are reading the session exactly as it happened, character by character. A real attacker on the same network could capture this in real time and have full credentials and system access within seconds of the Telnet session starting. SSH solves all of these problems with public key cryptography and encrypted transport. If you ever encounter a system still running Telnet during a pentest, it's an automatic critical finding.

---

## 🔗 Resources

- [NCL Telnet Tutorial Video](https://www.youtube.com/watch?v=Atny5Z3vQyo&t=800s)
- [Telnet - Wikipedia](https://en.wikipedia.org/wiki/Telnet)
- [uname command documentation](https://man7.org/linux/man-pages/man1/uname.1.html)

---

*Written by: Mo | Last updated: March 2026*
