# Network Traffic Analysis Medium - Decrypt

> **Category:** Network Traffic Analysis
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Use a provided SSL key log file to decrypt HTTPS traffic in Wireshark, then extract the cipher suite, SSL certificate domain, and a hidden flag transferred over the encrypted connection.

> 💡 HTTPS encrypts your traffic so nobody snooping on the network can read it. But if you have the session keys, you can decrypt it after the fact. This is exactly what this challenge is about.

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali)
- The `SSL Decrypt.pcapng` file downloaded from the challenge
- The `sslkeylog.log` file downloaded from the challenge

---

## 📚 Background: How TLS Works and Why This Works

TLS (Transport Layer Security) protects HTTPS traffic by negotiating a shared secret between the client and server during a **handshake**. Once the handshake is complete, all data is encrypted with that session key.

Normally, without the session key, even if you capture all the packets you can't read the contents. But browsers and many applications can be configured to log these session keys to a file called an **SSL key log file** (or SSLKEYLOG). When you load this file into Wireshark, it can use those keys to decrypt the captured traffic.

> 💡 This is the same technique security researchers, developers, and corporate network monitors use to inspect HTTPS traffic on machines they control. It's not magic, it's just having the keys.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Load the SSL Key Log into Wireshark

Open the PCAP in Wireshark:

```bash
wireshark "SSL Decrypt.pcapng"
```

Now load the key log file:

1. Go to **Edit → Preferences**
2. In the left panel, expand **Protocols**
3. Scroll down and click **TLS** (may say SSL in older Wireshark versions)
4. Next to **(Pre)-Master-Secret log filename**, click Browse and select `sslkeylog.log`
5. Click OK

Wireshark will now decrypt the TLS traffic automatically. You'll see packets that previously showed as `TLS` or `Application Data` now showing HTTP content.

---

### Q1 - Cipher Suite Chosen by the Server

Find **packet 6** in the capture. This is the **TLS Server Hello** packet, it's where the server tells the client which cipher suite it has chosen for the session.

Click on packet 6 and expand the following in the packet details panel:

```
Transport Layer Security
  → TLSv1.2 Record Layer: Handshake Protocol: Server Hello
    → Handshake Protocol: Server Hello
      → Cipher Suite
```

The value next to **Cipher Suite** is your answer.

> 💡 **What it looks like:** A long uppercase string with underscores describing the specific encryption algorithms chosen. It starts with `TLS_`.

---

### Q2 - Domain Covered by the SSL Certificate

Still in **packet 6**, but this time look at the Certificate section:

```
Transport Layer Security
  → TLSv1.2 Record Layer: Handshake Protocol: Certificate
    → Handshake Protocol: Certificate
      → Certificates
        → Certificate
```

Expand into the certificate details and look for the **Common Name** field. This is the domain the SSL certificate was issued for.

> 💡 **What it looks like:** A standard domain name ending in `.com`. Sounds like a travel website.

---

### Q3 - Flag Transferred Over HTTPS

Find **packet 10** in the capture. This is the HTTP request for `/flag.txt`.

Right-click on packet 10 and select **Follow → TLS Stream**.

This shows the decrypted contents of the HTTPS session. The flag is in the server's response to the `/flag.txt` request.

> 💡 **What it looks like:** Standard `SKY-XXXX-XXXX` format.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Packet 6, Server Hello, expand deep into the TLS section. Look for `Cipher Suite`. Starts with `TLS_ECDHE`.
- **Q2:** Same packet 6, but dig into the Certificate section instead. Look for `Common Name`. It's a `.com` vacation domain.
- **Q3:** Packet 10, right-click, Follow TLS Stream. The flag is in the server's plaintext response after decryption. Standard flag format.

---

## ⚠️ Accuracy Tips

- ❌ **Don't forget to load the key log file first.** Without it, packet 10 will show encrypted gibberish and you won't see the flag.
- ❌ **Don't confuse the TLS and IP TTL sections.** Make sure you're reading from inside the TLS layer for Q1 and Q2.
- ✅ **Load the key log via Edit → Preferences → Protocols → TLS** not via any other menu.
- ✅ **Follow TLS Stream** on packet 10, not TCP stream. TLS Stream gives you the decrypted application data.

---

## 🧠 Why This Works

The SSL key log format was introduced specifically to allow debugging of TLS traffic. Applications like Chrome and Firefox can be configured to write session keys to a log file using the `SSLKEYLOGFILE` environment variable. Network defenders and security researchers use this to inspect their own encrypted traffic during incident response or testing. From an attacker's perspective, if they can get access to a machine's SSLKEYLOG file along with a packet capture, they can decrypt all past HTTPS sessions captured from that machine. This is why key log files should be treated with the same sensitivity as private keys.

---

## 🔗 Resources

- [NCL Decrypt Tutorial Video](https://www.youtube.com/watch?v=aQOBsJbS4jM)
- [Palo Alto - Wireshark Decrypting HTTPS](https://unit42.paloaltonetworks.com/wireshark-tutorial-decrypting-https-traffic/)
- [Wireshark TLS Documentation](https://wiki.wireshark.org/TLS)

---

*Written by: Mo | Last updated: March 2026*
