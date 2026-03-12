# Scanning & Recon Medium - Net Track

> **Category:** Scanning & Recon
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

A strange server is running on a non-standard port. nmap can't figure out what it is. Your job is to manually probe it using netcat, interact with its custom command interface, and extract a hidden flag.

> 💡 This challenge teaches you that not everything can be automated. Sometimes you have to connect manually and poke around to see what a service does.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `nmap` (pre-installed on Kali)
- `nc` / netcat (pre-installed on Kali)
- The hostname and port number from the challenge prompt

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Scan the Port with nmap

First try a basic scan:

```bash
nmap net-track.services.cityinthe.cloud -p 8090
```

Output shows the port is open:

```
PORT     STATE  SERVICE
8090/tcp open   opsmessaging
```

Now try with version detection:

```bash
nmap net-track.services.cityinthe.cloud -p 8090 -sV
```

Strangely, this shows the port as closed:

```
PORT     STATE  SERVICE      VERSION
8090/tcp closed opsmessaging
```

> 💡 This is the server actively rejecting nmap's version detection probes. It's not a standard service so it doesn't respond the way nmap expects. This is your cue to stop using automated tools and go manual.

---

### Step 2 - Connect with Netcat

Connect to the server using `nc`:

```bash
nc net-track.services.cityinthe.cloud 8090
```

> ⚠️ **Important:** Once the connection is successful, nc will NOT print anything or give you a prompt. The screen will just look like it's hanging. It's not frozen. The connection is live and waiting for your input. Just start typing.

Type anything to test it, for example `hello`:

```
hello
```

The server responds:

```
Use help to get a list of supported commands
```

---

### Step 3 - Q1: Get the Software Name and Version

Type `help` to see what commands are available:

```
help
```

Response:

```
Here is a list of commands
version
list
get
help
```

Now run the `version` command:

```
version
```

The server will respond with the software name and version number. That's your Q1 answer. Submit the full name and version exactly as it appears.

> 💡 **What the answer looks like:** A made-up software name followed by a `v` and a version number.

---

### Step 4 - Q2: Find the Flag

Run the `list` command to see what files are on the server:

```
list
```

You'll get a directory listing of files. Now use the `get` command to read each file one by one:

```
get [filename]
```

Replace `[filename]` with each file from the listing. Go through all of them until you find the one containing the flag in `SKY-ABCD-1234` format.

> ⚠️ **Common mistake:** The flag is NOT in the first file you try. Check every single file in the listing before giving up. One of them has it.

---

### Step 5 - Q3: Find the Largest File Size

Using the same `get` command, read every file and count the characters in each response. Each character is 1 byte, so the character count equals the file size in bytes.

Go through every file and track the length of each response. The largest one is your answer.

> 💡 **What the answer looks like:** A double digit number ending in 0. Don't overthink it, just count the characters carefully.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Run `version` after connecting with netcat. The software has a dramatic name and a single digit version number.
- **Q2:** Use `list` first, then `get` each file. The flag is in one of them in standard `SKY-ABCD-1234` format. Check all files.
- **Q3:** Count characters carefully. The answer ends in 0 and is a two digit number.

---

## ⚠️ Accuracy Tips

- ❌ **Don't assume nc is frozen** when nothing appears after connecting. It's waiting for your input. Just start typing.
- ❌ **Don't skip any files for Q3.** You need to check every file to find the largest one.
- ❌ **Q3 answer ends in 0.** If your count doesn't end in 0, recount the characters in that file.
- ✅ **Submit Q1 exactly as the server outputs it**, including the `v` before the version number.
- ✅ **If your connection drops**, just run the `nc` command again to reconnect and continue where you left off.

---

## 🧠 Why This Works

This challenge simulates discovering and interacting with an unknown custom service, something penetration testers encounter regularly when probing internal network services that don't follow standard protocols. When automated tools like nmap fail to fingerprint a service, manual interaction with netcat is the next step. The ability to connect to a raw TCP port and interact with whatever protocol it speaks is a fundamental skill. In real engagements, unknown services on unusual ports are often the most interesting targets since they're custom-built and frequently contain vulnerabilities that automated scanners will never detect.

---

## 🔗 Resources

- [Netcat Guide](https://linux.die.net/man/1/nc)
- [nmap Documentation](https://nmap.org/docs.html)

---

*Written by: Mo | Last updated: February 2026*
