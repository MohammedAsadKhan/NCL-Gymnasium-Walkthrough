# OSINT Easy - Lookup

> **Category:** OSINT
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge tests your ability to research technical questions about the **Domain Name System (DNS)** using authoritative sources. You won't need any special tools, just knowing *where* to look and how to read a technical specification document.

> 💡 Honestly, these questions are pretty easy. A quick Google search will get you the answer for each one. That said, we'll go through it in detail so you understand *why* the answer is what it is, not just what to submit.

---

## 🛠️ Tools Needed

- A web browser
- **[IETF RFC Search](https://www.rfc-editor.org/)**, the authoritative source for DNS specifications
- No software installs needed

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Understand What You're Looking For

Before you start Googling, understand this: **DNS has many different record types**, each serving a specific purpose. This challenge asks you to identify which record type handles specific jobs. The answers are not opinions, they are defined in official specification documents published by the **Internet Engineering Task Force (IETF)**.

The IETF publishes these specs as **RFCs (Request for Comments)**, which are numbered documents that define how internet technologies work. When NCL says "use an authoritative source," they mean go to the RFC directly, not a random blog post.

> 💡 You can search RFCs at [rfc-editor.org](https://www.rfc-editor.org/) or just Google `RFC [number]` and click the IETF result.

---

### Step 2 - Q1: DNSSEC Public Signing Key Record

You're looking for the DNS record type that **holds the public signing key used by DNSSEC**.

DNSSEC (DNS Security Extensions) adds a layer of authentication to DNS to prevent tampering. It uses cryptographic keys to sign DNS records, and those keys have to be stored somewhere in DNS itself.

**Where to look:** Search for **RFC 4034**. This RFC defines DNSSEC and its record types. Head to **Section 2**, which describes the record type that stores the public key used for signing.

Your answer will be a short uppercase abbreviation, the kind of thing you'd see in a DNS configuration file. Think along the lines of how other DNS records are named (A, MX, TXT, etc.) but specific to key storage.

---

### Step 3 - Q2: IPv6 Address Mapping Record

You're looking for the DNS record type that **maps a hostname to an IPv6 address**.

You probably already know that a regular **A record** maps a hostname to an IPv4 address (ex: `192.168.1.1`). IPv6 addresses are longer and look different (ex: `2001:0db8:85a3::8a2e:0370:7334`), so DNS needed a new record type to handle them.

**Where to look:** Search for **RFC 3596**, titled "DNS Extensions to Support IP Version 6." Go to **Section 2**, which defines the record type created specifically for IPv6.

Your answer will be a very short uppercase abbreviation. If you know anything about IPv6 addresses, the name of this record type will make immediate sense once you see it.

---

### Step 4 - Q3: DNS Zone Delegation Record

You're looking for the DNS record type used to **delegate a DNS zone**.

This one requires a little more reading to understand. A DNS "zone" is a portion of the DNS namespace that a specific organization manages. When you delegate a zone, you're telling the internet "this other name server is responsible for answering questions about this part of the namespace."

**Where to look:** Search for **RFC 1035**, one of the original DNS specification documents. Look through it for the record type that points to an **authoritative name server** for a zone. Delegation works by pointing to the name server that has authority, so that's your clue for what to look for.

Your answer will be a 2-letter uppercase abbreviation.

> 💡 If you're unsure after reading the RFC, try Googling "DNS zone delegation record type" and you'll find many sources that confirm it. Just make sure you verify against the RFC before submitting.

---

## ⚠️ Accuracy Tips

- ❌ **Don't trust random blog posts as your only source.** They can be wrong or outdated. Always verify against the RFC.
- ❌ **Don't confuse similar record types.** There's a record for IPv4 and a separate one for IPv6, make sure you're answering about the right one.
- ✅ **Do read the specific section referenced.** The RFCs are long, but each question points you to a specific section. You don't need to read the whole thing.
- ✅ **All answers are short uppercase abbreviations.** If you're writing out a full word or phrase, you're probably looking at the wrong thing.

---

## 🧠 Why This Works

DNS is one of the most fundamental protocols on the internet. Every time you visit a website, DNS is working behind the scenes to translate a domain name into an IP address. There are over 30 different DNS record types, each with a specific job. As a cybersecurity professional, knowing these record types is essential because DNS is frequently targeted in attacks like DNS spoofing, cache poisoning, and zone transfers. Understanding the spec helps you recognize when something is wrong.

Reading RFCs is a skill in itself. They're dense, but learning to navigate them quickly is something that separates strong CTF competitors from the rest.

---

## 🔗 Resources

- [RFC Editor](https://www.rfc-editor.org/)
- [RFC 4034 - DNSSEC](https://www.rfc-editor.org/rfc/rfc4034)
- [RFC 3596 - DNS IPv6 Extensions](https://www.rfc-editor.org/rfc/rfc3596)
- [RFC 1035 - Original DNS Specification](https://www.rfc-editor.org/rfc/rfc1035)
- [DNS Record Types Overview - Cloudflare](https://www.cloudflare.com/learning/dns/dns-records/)

---

*Written by: Mo | Last updated: February 2026*
