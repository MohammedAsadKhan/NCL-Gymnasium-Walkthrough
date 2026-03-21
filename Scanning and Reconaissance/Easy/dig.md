# Scanning & Recon Easy - Dig

> **Category:** Scanning & Recon
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Use the `dig` command to query DNS records for `fortaigan.net` and extract information about its mail servers, name servers, responsible person, hidden flag, SIP service, and more.

> 💡 DNS (Domain Name System) is basically the internet's phone book. It doesn't just map domain names to IP addresses, it stores all kinds of records about a domain including mail servers, text notes, service locations, and more. This challenge teaches you how to read all of them.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `dig` (pre-installed on Kali)
- The resolver address provided in your challenge prompt (shown as `@resolver` in the commands below)

---

## 📚 DNS Record Types Quick Reference

| Record | What It Does |
|---|---|
| `A` | Maps a hostname to an IPv4 address |
| `MX` | Lists mail servers for a domain |
| `NS` | Lists the authoritative name servers |
| `TXT` | Stores arbitrary text, often used for flags, SPF records, verification tokens |
| `RP` | Responsible Person record, points to a contact |
| `SRV` | Service locator, used for SIP, XMPP, and other services |

---

## 📋 Step-by-Step Walkthrough

### Q1 - IPv4 Address of fortaigan.net

Query the A record:

```bash
dig @resolver A fortaigan.net
```

Look at the `ANSWER SECTION` of the output. The IP address at the end of the A record line is your answer.

---

### Q2 - How Many Mail Servers Does fortaigan.net Have?

Query the MX records:

```bash
dig @resolver MX fortaigan.net
```

Count how many lines appear in the `ANSWER SECTION`. Each line is one mail server.

---

### Q3 - Which Mail Server Has First Priority?

Use the same MX output from Q2. Look at the number before each mail server hostname. In MX records, **lower number = higher priority**. The mail server with the smallest priority number handles mail first.

> 💡 Don't be fooled by the names. `maila0` sounds like it should be first but the number is what matters, not the name.

---

### Q4 - IPv4 Address of the Name Server

This one takes two lookups. First get the name server hostname:

```bash
dig @resolver NS fortaigan.net
```

The `ANSWER SECTION` gives you a hostname, not an IP. Now look up that hostname's A record:

```bash
dig @resolver [hostname from above]
```

The IP address in that second answer is what you're after.

---

### Q5 - Full Name of the Responsible Person

Another two-step lookup. First query the RP record:

```bash
dig @resolver RP fortaigan.net
```

The RP record points to a hostname. Now query the TXT record on that hostname:

```bash
dig @resolver [hostname from above] TXT
```

> ⚠️ The output will have backslashes and extra quotation marks around the name. Those are just formatting artifacts in how dig displays TXT records. The actual name is the text inside, ignore the punctuation around it.

---

### Q6 - Text Flag in DNS Records

Query the TXT record on the domain itself:

```bash
dig @resolver TXT fortaigan.net
```

> ⚠️ Same as Q5, the flag will appear wrapped in backslashes and extra quotes like `"\"SKY-XXXX-XXXX\""`. Those are not part of the flag. Submit only the `SKY-XXXX-XXXX` portion.

---

### Q7 - Priority Number of the SIP Service (TCP)

SIP services are published using a specific SRV hostname format. Query it like this:

```bash
dig @resolver SRV _sip._tcp.fortaigan.net
```

SRV records follow the format: `priority weight port target`. The answer to this question is the very first number in the answer line.

---

### Q8 - IPv4 Address of the SIP Server

From Q7, the last field in the SRV answer is the SIP server hostname. Look up its A record:

```bash
dig @resolver [sipserver hostname from Q7]
```

The IP address in the answer is your answer for Q8.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** The A record answer is a standard IPv4 address in the format `XXX.XXX.XXX.X`.
- **Q2:** Count the lines in the MX answer section. It's a single digit number under 5.
- **Q3:** Compare the priority numbers. The winner has the lowest one. It's not the one you'd expect from its name.
- **Q4:** NS record gives hostname, then look up that hostname's A record. Two commands, two lookups.
- **Q5:** RP record gives a hostname, then look up that hostname's TXT record. The name inside is two words.
- **Q6:** Strip the backslashes and quotes from the TXT output. The flag follows the standard `SKY-XXXX-XXXX` format.
- **Q7:** SRV format is `priority weight port target`. You want the first number. It's a very high priority value.
- **Q8:** Take the hostname at the end of the SRV answer and look up its A record. Same pattern as Q4.

---

## ⚠️ Accuracy Tips

- ❌ **Don't include backslashes or extra quotes** in your Q5 or Q6 answers. Strip them out.
- ❌ **Don't confuse MX priority.** Lower number = higher preference. The name doesn't matter, the number does.
- ❌ **Don't stop at the NS hostname for Q4.** The question asks for the IP, so you need a second lookup.
- ✅ **Chain your lookups.** Q4, Q5, and Q8 all require two `dig` commands.
- ✅ **Replace `@resolver`** with the actual resolver address shown in your challenge prompt.

---

## 🧠 Why This Works

DNS is one of the most information-rich sources in reconnaissance. Beyond simple A records, a domain's DNS can reveal its entire mail infrastructure, responsible contacts, hidden text records, and even what services like SIP or XMPP the organization runs. In real penetration testing, DNS enumeration is one of the first steps in passive reconnaissance and can reveal subdomains, internal hostnames, and service providers without ever touching the target's servers directly. Tools like `dig`, `nslookup`, and `dnsx` are staples of every pentester's toolkit for exactly this reason.

---

## 🔗 Resources

- [dig Manual Page](https://linux.die.net/man/1/dig)
- [DNS Record Types Explained](https://www.cloudflare.com/learning/dns/dns-records/)
- [SRV Record Format](https://en.wikipedia.org/wiki/SRV_record)

---

*Written by: Mo | Last updated: March 2026*
