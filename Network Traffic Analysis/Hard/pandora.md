# Network Traffic Analysis Hard - Pandora's Box

> **Category:** Network Traffic Analysis
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a packet capture containing a custom binary protocol. Using the protocol specification provided, parse the raw TCP stream to extract server and client details, the magic ID, request lengths, hash sizes, hash values, and a hidden flag encoded in the data.

> 🚨 **This flag does NOT follow the usual `SKY-XXXX-XXXX` format.** This is an older challenge and the flag starts with `NCL-`. Submit it exactly as you find it.

> 💡 This is the most technically involved NTA challenge. Take it slow, use the hex dump view in Wireshark, and refer back to the protocol spec constantly. Watch the tutorial video first if anything feels unclear.

---

## 🔗 Tutorial Video

[NCL Pandora Tutorial](https://www.youtube.com/watch?v=70grYjg3fuE&t=49s), Highly recommended before starting.

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali)
- A hex-to-decimal converter (CyberChef or Python)
- A base64 decoder (CyberChef)
- The `pandora.pcap` file downloaded from the challenge

---

## 📚 Protocol Specification

The custom protocol has three message types:

**Initialization (Client → Server)**
- `N`, 4-byte integer (network byte order) = number of hash requests

**Hash Request (Client → Server)**
- `Check`, 2-byte magic integer (integrity check)
- `Len`, 4-byte integer = length of data in bytes
- `Data`, the actual data to be hashed

**Hash Response (Server → Client)**
- `Count`, length of response data in bytes
- `Hashes`, all hashes concatenated, same order as requests

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Filter Out the Noise

The capture contains SSH and HTTP traffic mixed in with the custom protocol. Apply this filter to isolate only the custom protocol packets:

```
tcp && !(tcp.port == 22) && !(tcp.port == 80)
```

This removes SSH (port 22) and HTTP (port 80), leaving only the custom protocol traffic.

---

### Q1 - Server IP Address

Look at the first filtered packet. In the packet details, expand **Internet Protocol Version 4**. The **Destination** is the server since the client is initiating the connection.

> 💡 **What it looks like:** A private IP in the `10.1.0.X` range.

---

### Q2 - Client IP Address

Same first packet. The **Source** IP is the client.

> 💡 **What it looks like:** Also a `10.1.0.X` address, different from Q1.

---

### Q3 - Server Port

Expand the **Transmission Control Protocol** section of the first packet. The **Destination Port** is the port the server is listening on.

> 💡 **What it looks like:** A 5-digit port number above 1024.

---

### Step 2 - Follow the TCP Stream as Hex Dump

Right-click any filtered packet and select **Follow → TCP Stream**.

In the bottom-left dropdown of the stream window, change the display format from **ASCII** to **Hex Dump**. This is critical, the data is binary and will look like garbage in ASCII view.

Now you can read the raw bytes of the protocol.

---

### Q4 - Magic 2-Byte ID (Decimal)

Per the protocol spec, after the 4-byte initialization `N` value, the next 2 bytes are the `Check` magic number that appears at the start of every Hash Request.

From the hex dump, the first 4 bytes are the N value (number of requests). The next 2 bytes are the magic check value.

> 💡 **What it looks like:** The hex value is `04 17`. Convert that to decimal for your answer. The question asks for it in decimal but the answer format looks like hex. Submit it as shown: `0x0417`.

---

### Q5 - Number of Encrypt Requests

The first 4 bytes of the stream (the `N` field) tell you how many requests were made. Convert those 4 bytes from hex to decimal.

> 💡 **What it looks like:** A single digit number under 10.

---

### Q6 - Length of the First Encrypt Request

After the magic check bytes, the next 4 bytes are the `Len` field for the first request. Convert from hex to decimal.

> 💡 The hex value for this length is `0x58`. Convert that to decimal.

---

### Q7 - Length of the Second Encrypt Request

Find the second instance of the magic check bytes `04 17` in the hex dump. The 4 bytes following it are the length of the second request. Convert from hex to decimal.

> 💡 The hex value for this length is `0x48`. Convert that to decimal.

---

### Q8 - Size of an Individual Hash

The server sends back all hashes in one response. Look at the server response in the hex dump (red text in the stream view). The first 4 bytes of the response are the `Count` field which tells you the total length of all hashes combined.

Divide the total response length by the number of requests to get the size of each individual hash:

```
Total response length ÷ number of requests = hash size
```

> 💡 The total response length is `0xa0` = 160 bytes. Divide by 5 requests.

---

### Q9 - First Hash Response (Hex)

Each hash is 32 bytes. The first hash starts right after the 4-byte `Count` field in the server response. Take the first 32 bytes and convert to uppercase hex.

> 💡 **What it looks like:** 64 uppercase hex characters (32 bytes × 2 hex chars per byte).

---

### Q10 - Second Hash Response (Hex)

The second hash starts immediately after the first 32 bytes. Take the next 32 bytes and convert to uppercase hex.

> 💡 Same format as Q9, 64 uppercase hex characters.

---

### Q11 - Hidden Flag

The flag is hidden inside the data of one of the hash requests. Each request's `Data` field is base64 encoded. Take the data from any of the requests, decode it from base64, and look for the flag.

In CyberChef:
1. Paste the hex bytes of the Data field
2. Add **From Hex** to the recipe
3. Add **From Base64** to the recipe
4. The output contains the flag

> 🚨 **The flag starts with `NCL-`** not `SKY-`. This is an older challenge. Submit it exactly as decoded.

---

## 💡 Hints (Without Giving It Away)

- **Q1 & Q2:** First filtered packet. Server = destination, client = source.
- **Q3:** Destination port in the TCP section. Five digits.
- **Q4:** Bytes 4 and 5 of the stream (after the 4-byte N field). Look for `04 17` repeating throughout the stream.
- **Q5:** First 4 bytes of the stream converted to decimal. Single digit.
- **Q6:** Hex `0x58` in decimal. Follows the first magic check bytes.
- **Q7:** Hex `0x48` in decimal. Follows the second `04 17`.
- **Q8:** Server sends `0xa0` = 160 bytes total. Divide by 5.
- **Q9 & Q10:** 32 bytes each, starting after the 4-byte count field in the server response. Uppercase hex.
- **Q11:** Take the Data bytes from any request, decode from Base64. Flag starts with `NCL-`.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit the flag as `SKY-`.** This one starts with `NCL-`. Older challenge format.
- ❌ **Don't read the stream in ASCII mode.** Switch to Hex Dump or you won't be able to parse the binary data.
- ❌ **Don't forget the 4-byte Count field** before the hashes in the server response. The hashes start after it.
- ✅ **Use the filter** `tcp && !(tcp.port == 22) && !(tcp.port == 80)` to cut the noise first.
- ✅ **Refer back to the protocol spec** constantly. Each field size is defined precisely.

---

## 🧠 Why This Works

Custom binary protocols are common in real malware and command-and-control (C2) frameworks. Attackers build their own protocols to avoid detection by network security tools that look for known protocol signatures. The ability to read raw hex dumps, follow a protocol specification, and extract meaningful data from binary streams is a critical skill in network forensics and malware analysis. This challenge mirrors exactly what a security analyst would do when reverse engineering an unknown protocol found in a network capture during an incident response.

---

## 🔗 Resources

- [NCL Pandora Tutorial Video](https://www.youtube.com/watch?v=70grYjg3fuE&t=49s)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Network Byte Order Explained](https://en.wikipedia.org/wiki/Endianness#Networking)

---

*Written by: Mo | Last updated: March 2026*
