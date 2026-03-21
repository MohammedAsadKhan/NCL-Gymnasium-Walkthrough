# Network Traffic Analysis Easy - DNS

> **Category:** Network Traffic Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a packet capture containing DNS traffic. You'll identify the type of DNS query, the domain requested, and extract details from the DNS response including record count, TTL, and IP addresses.

> 💡 DNS (Domain Name System) is what lets you type `google.com` instead of memorizing an IP address. It's basically the internet's phone book. This challenge teaches you how DNS queries and responses look at the packet level.

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali) or the web-based **CloudShark** tool if provided in your challenge
- The PCAP file downloaded from the challenge

---

## 📚 Background: How DNS Works

When your computer wants to reach a website, it sends a **DNS query** asking "what is the IP address for this domain?" A **DNS server** responds with one or more **DNS records** containing the answer.

Key terms you'll see in this challenge:

- **Query type:** The type of DNS record being requested (A, MX, AXFR, etc.)
- **AXFR:** A special DNS query type that requests a full **zone transfer**, meaning it asks for ALL DNS records for a domain at once. This is normally restricted but when misconfigured it leaks everything.
- **TTL (Time to Live):** How many seconds a DNS record should be cached before it expires. This is separate from the IP packet TTL.
- **Answer section:** The part of the DNS response containing the actual records returned.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Open the PCAP in Wireshark

```bash
wireshark [filename].pcap
```

Or drag and drop the file into Wireshark.

Filter to show only DNS traffic:

```
dns
```

You'll see a small number of packets. Look at the **Info** column to identify which packets are queries and which are responses.

---

### Q1 - Type of DNS Query Requested

Find the packet with **"Standard query"** in the Info column. This is packet 4 in the capture.

Click on it and expand the **Domain Name System (DNS)** section in the packet details panel. Look for the **Type** field under the **Queries** section.

> 💡 **What the answer looks like:** A 4-letter uppercase abbreviation for a DNS record type. This particular type is not a standard A or MX lookup. It's a special query that requests every DNS record for an entire domain at once. Think of it as asking for the whole filing cabinet instead of one folder.

---

### Q2 - Domain That Was Requested

In the same packet and same **Queries** section, look for the **Name** field right above the Type field.

> 💡 **What the answer looks like:** A standard domain name ending in `.com`. It's short, two to four letters before the dot.

---

### Q3 - How Many Items Were in the Response

Find the packet with **"Standard query response"** in the Info column. This is packet 5 in the capture.

Click on it and expand the **Domain Name System (DNS)** section. Then expand the **Answers** section inside it. Count the number of entries listed under Answers.

> 💡 **What the answer looks like:** A single digit number under 10. Count each individual record entry in the Answers section.

---

### Q4 - TTL for All DNS Records

In the same response packet (packet 5), expand the **Answers** section. Click on any individual record and look for the **Time to live** field.

> ⚠️ **The question asks for the DNS record TTL, NOT the IP packet TTL.** These are two different fields. Make sure you're reading from inside the DNS section, not the IP section of the packet.

> 💡 **What the answer looks like:** A round number in seconds. A very common TTL value used by many DNS administrators. All records in this response share the same TTL.

---

### Q5 - IP Address of the "welcome" Subdomain

Still in the Answers section of packet 5, look through each record for one associated with the `welcome` subdomain. That record will have an IP address next to it.

> 💡 **What the answer looks like:** A very well known IP address. You might recognize it immediately.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** The query type is not a standard lookup. AXFR is a zone transfer request that asks for every single record in a DNS zone at once. It's considered a security misconfiguration when publicly accessible.
- **Q2:** Short domain name, ends in `.com`. Four letters total before the dot.
- **Q3:** Count the entries in the Answers section of packet 5. It's a small number, single digit.
- **Q4:** Look inside the DNS section not the IP header. The TTL is the same for every record in the response. It's a round number you'll recognize as a common cache duration.
- **Q5:** Expand the Answers and find the record for `welcome.[domain]`. The IP address tied to it is one of the most recognizable addresses on the internet.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit the IP packet TTL for Q4.** That's in the IP header section, not DNS. The question specifically says "DNS record TTL."
- ❌ **Don't count the query packet as a response.** Q3 asks about the response (packet 5), not the query (packet 4).
- ✅ **Filter by `dns`** to cut through the noise and see only relevant packets.
- ✅ **Expand all sections** in the packet details panel. The answers are nested inside DNS > Answers.

---

## 🧠 Why This Works

AXFR (zone transfer) queries are designed for DNS administrators to replicate DNS records between servers. When a DNS server is misconfigured to allow AXFR from any IP address, an attacker can request every single DNS record for a domain in one query, instantly mapping out all subdomains, mail servers, and internal hostnames. This is one of the most common DNS misconfigurations and a goldmine for reconnaissance. Real-world security assessments always check whether zone transfers are publicly accessible.

---

## 🔗 Resources

- [NCL DNS Tutorial Video](https://www.youtube.com/watch?v=FFFLW7nBzpk&t=89s)
- [Cloudflare - What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [AWS - What is DNS?](https://aws.amazon.com/route53/what-is-dns/)
- [Wireshark Documentation](https://www.wireshark.org/docs/)

---

*Written by: Mo | Last updated: March 2026*
