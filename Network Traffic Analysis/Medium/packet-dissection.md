# Network Traffic Analysis Medium - Packet Dissection

> **Category:** Network Traffic Analysis
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Read a raw binary IPv4 packet header and extract the header checksum, TTL, source IP, and destination IP by following the IPv4 specification and converting binary fields using CyberChef.

> ⚠️ **Heads up:** This challenge is more tedious than difficult. You're not cracking anything, you're just carefully reading binary data and converting it. If you find yourself confused, go watch the tutorial video first. It will save you a lot of frustration.

---

## 🔗 Tutorial Video

[NCL Packet Dissection Tutorial](https://www.youtube.com/watch?v=fq9RRx8rmNQ&t=5s), Watch this if anything below doesn't click.

---

## 🛠️ Tools Needed

- [CyberChef](https://gchq.github.io/CyberChef/), for binary to hex and IP format conversions
- The raw binary data provided in the challenge

---

## 📚 Background: The IPv4 Header

Every IP packet starts with a header that contains metadata about the packet. The header follows a strict format defined in RFC 791. Here is the layout, measured in bits from the start of the packet:

```
Bits 0-3:    Version
Bits 4-7:    IHL (Internet Header Length)
Bits 8-15:   DSCP + ECN
Bits 16-31:  Total Length
Bits 32-47:  Identification
Bits 48-50:  Flags
Bits 51-63:  Fragment Offset
Bits 64-71:  Time to Live (TTL)       ← 1 byte, offset 8
Bits 72-79:  Protocol
Bits 80-95:  Header Checksum          ← 2 bytes, offset 10
Bits 96-127: Source IP Address        ← 4 bytes, offset 12
Bits 128-159: Destination IP Address  ← 4 bytes, offset 16
```

The raw binary data for this challenge is:

```
Offset 0:  01000101  00000000  00000000  00111100
Offset 4:  10101001  10011010  01000000  00000000
Offset 8:  01000000  00000110  01001111  10010011
Offset 12: 11000000  10101000  10000000  10000000
Offset 16: 10011111  11001011  01100000  10011010
```

Each row is 4 bytes. Offsets count from 0.

---

## 📋 Step-by-Step Walkthrough

### Q1 - Header Checksum (Hex)

The header checksum is **2 bytes** starting at **byte offset 10**.

Count through the bytes:
- Offset 0, 1, 2, 3 = row 1
- Offset 4, 5, 6, 7 = row 2
- Offset 8, 9, **10, 11** = row 3 (last two bytes)

The bytes at offset 10 and 11 are:

```
01001111  10010011
```

**Convert in CyberChef:**

Use this direct link: [CyberChef Binary to Hex](https://cyberchef.io/#recipe=From_Binary('Space',8)To_Hex('Space',0))

Paste the two bytes into the Input with a space between them:

```
01001111 10010011
```

The output gives you the hex representation. Remove the space between the two hex bytes and that's your answer.

> 💡 **What it looks like:** 4 uppercase hex characters.

---

### Q2 - TTL (Decimal)

The TTL is **1 byte** starting at **byte offset 8**.

The byte at offset 8 is the first byte of row 3:

```
01000000
```

**Convert in CyberChef:**

Use From Binary, set output to decimal. Or just calculate manually: `01000000` in binary = 64 in decimal.

> 💡 **What it looks like:** A common round number. TTL of 64 is the default on many Linux systems.

---

### Q3 - Source IP Address

The source IP is **4 bytes** starting at **byte offset 12**.

Offset 12, 13, 14, 15 are the entire 4th row:

```
11000000  10101000  10000000  10000000
```

**Convert in CyberChef:**

Use this direct link: [CyberChef Binary to IP](https://cyberchef.io/#recipe=From_Binary('Space',8)To_Hex('Space',0)Change_IP_format('Hex','Dotted%20Decimal'))

Paste all four bytes with spaces between them:

```
11000000 10101000 10000000 10000000
```

The output is the IP address in dotted decimal notation.

> 💡 **What it looks like:** A private IP address starting with `192.168.`

---

### Q4 - Destination IP Address

The destination IP is **4 bytes** starting at **byte offset 16**.

Offset 16, 17, 18, 19 are the entire 5th row:

```
10011111  11001011  01100000  10011010
```

**Convert in CyberChef** using the same IP recipe as Q3:

```
10011111 11001011 01100000 10011010
```

> 💡 **What it looks like:** A public IP address. Not in any private range.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Bytes at offset 10 and 11. That's the 11th and 12th bytes (remember offset starts at 0). They're in the third row of the data table, last two bytes. Convert binary to hex with CyberChef.
- **Q2:** Byte at offset 8. First byte of the third row. Binary to decimal. Very common Linux default TTL value.
- **Q3:** Bytes at offset 12-15. The entire fourth row. Use the CyberChef IP conversion link above. Private IP range.
- **Q4:** Bytes at offset 16-19. The entire fifth row. Same CyberChef recipe as Q3. Public IP.

---

## ⚠️ Accuracy Tips

- ❌ **Don't forget offset starts at 0.** Offset 10 is the 11th byte, not the 10th.
- ❌ **Don't include spaces in the Q1 hex answer.** The two bytes convert to a 4-character hex string with no space in the middle.
- ✅ **Use the CyberChef links provided above.** They have the correct recipe pre-loaded so you just need to paste the binary.
- ✅ **Put spaces between bytes** when pasting into CyberChef so it knows where each byte boundary is.
- ✅ **Double check your byte selection.** Counting bytes is where most mistakes happen. Use the offset table to verify you have the right ones.

---

## 🧠 Why This Works

Every IP packet that crosses the internet follows this exact same header format defined in RFC 791, published in 1981. Routers, firewalls, and network devices all read these fields in real time to determine where to send packets, whether to drop them, and how to prioritize them. Understanding the raw binary structure of a packet is the foundation of network security work. Tools like Wireshark do this parsing automatically for you, but knowing how to do it manually means you can read and interpret network data even without a tool, which matters when you're in a restricted environment or analyzing unusual traffic.

---

## 🔗 Resources

- [NCL Packet Dissection Tutorial](https://www.youtube.com/watch?v=fq9RRx8rmNQ&t=5s)
- [CyberChef Binary to Hex](https://cyberchef.io/#recipe=From_Binary('Space',8)To_Hex('Space',0))
- [CyberChef Binary to IP](https://cyberchef.io/#recipe=From_Binary('Space',8)To_Hex('Space',0)Change_IP_format('Hex','Dotted%20Decimal'))
- [RFC 791 - IPv4 Specification](https://datatracker.ietf.org/doc/html/rfc791)
- [IPv4 Header Format - Wikipedia](https://en.wikipedia.org/wiki/IPv4#Packet_structure)

---

*Written by: Mo | Last updated: March 2026*
