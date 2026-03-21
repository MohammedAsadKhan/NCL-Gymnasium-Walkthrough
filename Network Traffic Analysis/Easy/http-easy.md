# Network Traffic Analysis Easy - HTTP

> **Category:** Network Traffic Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a packet capture of HTTP traffic to identify the download tool used, the web server software, the IP addresses involved, and calculate the MD5 checksum of the downloaded file.

> 💡 HTTP (Hypertext Transfer Protocol) is the foundation of the World Wide Web. It's how your browser asks for web pages and how servers send them back. Like FTP, traditional HTTP sends everything in plaintext. Every request, every response, every image, every file, all readable by anyone on the network. HTTPS adds encryption on top, but plain HTTP? Open book.

---

## 📖 A Brief History and a Warning

HTTP was invented by Tim Berners-Lee in 1989 as part of his proposal for the World Wide Web. He built it to share research documents between scientists. He probably didn't anticipate that one day it would also be used to stream cat videos and online banking.

The fun part for you is that Wireshark can read every single byte of an unencrypted HTTP session. Every file downloaded, every page requested, every cookie sent. It's like being the world's nosiest neighbor, except instead of peeking through curtains you're just running a packet capture. Welcome to network forensics.

> ⚠️ A reminder: using Wireshark on networks you don't own or have permission to capture is illegal. In NCL you're working with provided PCAP files in a controlled environment. Real networks require explicit permission.

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali) or the web-based **CloudShark** tool if provided
- **CyberChef**, for MD5 calculation from hex data
- OR the `md5sum` command on Linux
- The `HTTP.pcap` file downloaded from the challenge

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: What Linux Tool Was Used to Download the File?

Open the PCAP in Wireshark:

```bash
wireshark HTTP.pcap
```

Apply the HTTP request filter:

```
http.request
```

Click on the filtered packet and expand the **Hypertext Transfer Protocol** section in the packet details panel. Look for the **User-Agent** field.

The User-Agent field identifies the software that made the HTTP request. Web browsers, command line tools, and scripts all report different User-Agent strings.

> 💡 **What the answer looks like:** A common Linux command line download tool. One word, starts with a W. Developers and sysadmins use it constantly to grab files from the command line.

---

### Step 2 - Q2, Q3, Q4: Server Software and IP Addresses

Apply the HTTP response filter:

```
http.response
```

Click on the filtered packet. In the packet details panel:

**Q2 - Server software:** Expand the **Hypertext Transfer Protocol** section and look for the **Server** field. This identifies the web server software that handled the request.

> 💡 **Q2 hint:** One of the most widely deployed web servers in the world. You've seen it before in this repo.

**Q3 & Q4 - IP Addresses:** Expand the **Internet Protocol Version 4** section and look at the **Source** and **Destination** fields.

> 💡 **Key concept:** This is a *response* packet, meaning the server is sending data back to the client. So:
> - **Source** = the server's IP address (Q4)
> - **Destination** = the client's IP address that made the request (Q3)

If you go back to the request packet from Step 1, you'll notice the source and destination are flipped. That's because the request travels from client to server and the response travels back the other way.

> 💡 **Q3 hint:** A private IP address in the `192.168.1.X` range.
> 💡 **Q4 hint:** A public IP address. Not in the 192.168 range.

---

### Step 3 - Q5: MD5 Sum of the Downloaded File

**Method A: Wireshark Export (Easiest)**

In Wireshark, go to **File → Export Objects → HTTP**

This shows all files transferred via HTTP in the capture. Select the file and save it to your computer. Then calculate its MD5:

```bash
md5sum [filename]
```

**Method B: CyberChef from Hex Data**

1. Apply the `http` filter and find packet 36 which has `(PNG)` in the Info column
2. In the packet details, click on **PNG Signature** to highlight the start of the image data
3. Right-click the highlighted hex data and copy it
4. Open [CyberChef](https://gchq.github.io/CyberChef/)
5. Paste the hex data into the Input section
6. Add **From Hex** to the Recipe
7. Click the magic wand icon to render the image and verify it looks correct
8. Add **MD5** to the Recipe
9. The output is your MD5 hash

> ⚠️ **Be patient when copying hex data in CloudShark.** It can take a moment before the copy option appears. Don't click away.

> 💡 **What the answer looks like:** A 32-character uppercase hexadecimal string. Standard MD5 hash format.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** `http.request` filter, look at the User-Agent field. It's a command line download tool, not a browser.
- **Q2:** `http.response` filter, look at the Server field. Popular web server, one word.
- **Q3:** Destination IP in the response packet. Private IP, starts with `192.168.1.`
- **Q4:** Source IP in the response packet. Public IP, four octets, nothing like a private range.
- **Q5:** Export via File → Export Objects → HTTP, then run `md5sum` on the file. 32 hex characters, all uppercase.

---

## ⚠️ Accuracy Tips

- ❌ **Don't confuse source and destination for Q3 and Q4.** In a response packet the source is the server and the destination is the client. It's the opposite of what you might expect.
- ❌ **Don't submit the MD5 in lowercase.** Submit it in uppercase exactly as `md5sum` or CyberChef outputs it.
- ✅ **File → Export Objects → HTTP** is the fastest way to get the file for Q5. No hex copying needed.
- ✅ **Verify your image renders correctly** in CyberChef before calculating the MD5. If the image looks broken, your hex data is incomplete.

---

## 🧠 Why This Works

HTTP without TLS (HTTPS) is completely transparent to anyone capturing network traffic. This is why the industry shifted hard to HTTPS, by 2024 over 95% of web traffic is encrypted. But unencrypted HTTP still exists in legacy systems, IoT devices, internal networks, and misconfigured servers. When a pentester or forensic analyst finds HTTP traffic in a capture, they can reconstruct every file downloaded, every form submitted, every cookie sent, and every page visited. The File → Export Objects feature in Wireshark makes this trivially easy. This challenge is a perfect demonstration of why "HTTP is fine for internal traffic" is not a safe assumption.

---

## 🔗 Resources

- [NCL HTTP Tutorial Video](https://www.youtube.com/watch?v=WpSarp1Ozns&t=850s)
- [MDN - HTTP Basics](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Wireshark Export Objects Guide](https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html)

---

*Written by: Mo | Last updated: March 2026*
