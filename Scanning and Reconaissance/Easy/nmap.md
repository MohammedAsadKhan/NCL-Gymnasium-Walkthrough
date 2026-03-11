# Scanning & Recon Easy - NMAP

> **Category:** Scanning & Recon
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Use nmap to scan a target server and identify open ports, UDP services, and the software running on a specific port. This is one of the most fundamental skills in all of cybersecurity. If you're new to nmap, you're in the right place.

> 💡 If you get stuck, the official NCL tutorial walks through this: [NMAP Tutorial](https://www.youtube.com/watch?v=ipHEkIvNiAw)

---

## 📖 Fun Fact: The Nosy Neighbor of the Internet

Nmap (Network Mapper) was created by Gordon Lyon (known online as Fyodor) and first released in 1997 in a Phrack magazine article. His goal was simple: build a tool that could knock on every door of a network and see who answers.

Think of nmap as that one neighbor who walks up and down the street ringing every doorbell just to see who's home, what kind of lock they have on their door, and whether any windows are open. Except instead of being arrested for it, security professionals get paid to do exactly this.

It's now one of the most widely used tools in cybersecurity and was even featured in movies like The Matrix Reloaded and Die Hard 4. Hollywood discovered that a real terminal running nmap looks way more convincing than fake hacking screens.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `nmap` (pre-installed on Kali)
- Target: `ports.cityinthe.cloud`

---

## 📚 Key nmap Flags

Before diving in, here are the flags you'll need for this challenge:

| Flag | What It Does |
|---|---|
| `-p` | Specify port range (e.g. `-p 1-65535` for all ports) |
| `-sU` | UDP scan (scans UDP ports instead of TCP) |
| `-sV` | Version detection (identifies software running on each port) |
| `-Pn` | Skip ping check (use this if the server blocks pings) |

> 💡 By default nmap only scans the top 1000 most common ports. For this challenge you need to scan a wider range to find all open ports. Use `-p-` to scan all 65535 ports or specify a range with `-p 1-65535`.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1, Q2, Q3: Find the Three Lowest Open TCP Ports

Run a full TCP scan across all ports:

```bash
nmap -Pn -p- ports.cityinthe.cloud
```

This scans all 65535 TCP ports. It will take a few minutes. Once done, look through the output for ports marked as `open`. The three lowest numbered open ports are your answers for Q1, Q2, and Q3.

> 💡 **What the answers look like:** These are very low port numbers, all under 40. They correspond to some of the oldest internet protocols ever designed, services from the early days of ARPANET that almost nobody uses anymore but are still running here.

---

### Step 2 - Q4: Find the Lowest Open UDP Port

UDP scans require root/sudo and use a different flag:

```bash
sudo nmap -Pn -sU -p- ports.cityinthe.cloud
```

> ⚠️ UDP scans are significantly slower than TCP scans. To speed it up, scan a limited range first since the answer is a very low port number:

```bash
sudo nmap -Pn -sU -p 1-100 ports.cityinthe.cloud
```

Look for the lowest port marked as `open` or `open|filtered`. That's your Q4 answer.

> 💡 **Note from the walkthrough:** Your Internet Service Provider may intercept port 25 (mail) traffic and show it as open even when it isn't. If port 25 shows as open, don't submit it without verifying. The real answer is lower than 25.

---

### Step 3 - Q5: Identify Software on Port 16080

Use the version detection flag to identify what's running on a specific port:

```bash
nmap -Pn -sV -p 16080 ports.cityinthe.cloud
```

The output will show a `VERSION` column next to port 16080. The software name there is your Q5 answer.

> 💡 **Why `-sV` matters:** Without `-sV`, nmap just guesses the service based on the port number. Port 16080 isn't a standard port, so without version detection nmap might just say "unknown." The `-sV` flag actually connects and probes the service to identify what it really is.

---

## 💡 Hints (Without Giving It Away)

- **Q1, Q2, Q3:** All three answers are single or double digit port numbers. They're ancient protocols: one checks if a host is alive, one tells you the current time as a number, and one tells you the current time as a human-readable string. Look up "echo protocol", "daytime protocol", and "time protocol" if you're curious.
- **Q4:** The lowest UDP port matches the lowest TCP port. Same service, different protocol.
- **Q5:** One of the most widely used web servers in the world. You've seen it before in this repo.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit port 25 for Q4** without verifying. ISPs sometimes intercept SMTP traffic and make it look open when it isn't on the target.
- ❌ **Don't forget `-Pn`** if your scans are coming back with no results. Some servers block ping requests and nmap will assume the host is down without this flag.
- ✅ **Run the full port scan first** (`-p-`) to make sure you don't miss anything. The default top 1000 ports will miss port 16080.
- ✅ **For Q5**, submit just the software name in lowercase, not the version number.

---

## 🧠 Why This Works

Port scanning is the first step in almost every penetration test and network audit. Before you can exploit anything, you need to know what's running and where. nmap is the industry standard tool for this and has been for nearly 30 years. The flags you learned here, `-p`, `-sU`, `-sV`, and `-Pn`, are the same ones professional penetration testers use daily. Understanding what services are running on unusual ports (like port 16080 instead of the standard 80) is exactly the kind of thing that helps attackers and defenders alike understand a system's attack surface.

---

## 🔗 Resources

- [NCL NMAP Tutorial](https://www.youtube.com/watch?v=ipHEkIvNiAw)
- [nmap Official Documentation](https://nmap.org/docs.html)
- [nmap Cheat Sheet](https://www.stationx.net/nmap-cheat-sheet/)
- [Port Numbers Reference](https://www.iana.org/assignments/service-names-port-numbers/)

---

*Written by: Mo | Last updated: February 2026*
