# Network Traffic Analysis Easy - FTP Traffic

> **Category:** Network Traffic Analysis
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a packet capture of FTP traffic to identify login attempts, server software, commands executed, files transferred, and what an anonymous user downloaded.

> 💡 FTP (File Transfer Protocol) is one of the oldest file transfer protocols on the internet. It has one massive problem: **it sends everything in plaintext**, including usernames, passwords, and file contents. Anyone capturing the network traffic can read it all. This challenge shows exactly why FTP is considered insecure.

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali) or the web-based **CloudShark** tool if provided
- The `FTP.pcap` file downloaded from the challenge

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1 & Q2: First Login Attempt and Server Software

Open the PCAP in Wireshark:

```bash
wireshark FTP.pcap
```

Right-click on the **first packet** in the capture and select **Follow → TCP Stream**.

This opens the full conversation between the client and the FTP server from the very beginning. The first line of the stream shows the server banner which includes the **FTP server software name and version**, that's your Q2 answer.

Look for the lines starting with `USER` and `PASS` (shown in blue). The first `USER` line is the first username attempted and the first `PASS` line is the first password attempted. Combine them as `username:password` for your Q1 answer.

> 💡 **Q1 hint:** The first attempt uses a generic-sounding username and a well-known cybersecurity brand as the password.
> 💡 **Q2 hint:** The server software is a well-known FTP server application. The answer includes the name, version number, and the word "beta".

---

### Step 2 - Q3, Q4, Q5, Q6: Successful Login and Commands

Apply this filter to find the successful authentication packet:

```
ftp.response.code == 230
```

Code 230 means "Login successful." Right-click the **first result** and select **Follow → TCP Stream**.

This stream shows the full session after successful login. From here you can find:

**Q3 - First successful username:password:**
Look at the `USER` and `PASS` lines in this stream. This is a different password than the first attempt from Q1.

> ⚠️ **Common mistake:** The first login attempt from Q1 fails. The first *successful* login uses the same username but a different password. Don't submit the same answer as Q1.

**Q4 - First command the user executes:**
After the successful login, look at the first command sent by the client (blue text). This is not `USER` or `PASS`, those are authentication commands. Look for the first command the user runs once they're actually logged in.

> 💡 **Q4 hint:** The first thing most people do after logging into an FTP server is look at what files are there. The command for listing directory contents is three capital letters.

**Q5 - File deleted:**
Scroll through the stream and look for a `DELE` command. The filename following it is what was deleted.

> 💡 **Q5 hint:** The deleted file is a packet capture file. Its extension gives away what it is.

**Q6 - File uploaded:**
Look for a `STOR` command in the stream. The filename following it is the file that was uploaded.

> 💡 **Q6 hint:** The uploaded file is a compressed archive. Common archive extension.

---

### Step 3 - Q7: File Size of the Uploaded File

Apply the `ftp-data` filter to see the actual file transfer packets:

```
ftp-data
```

Look at the packets and find the one associated with the STOR command (the upload). Use the **Time** column to group them, packets that are very close in time are part of the same transfer.

Find packet No. 65 at approximately 152 seconds which shows a directory listing after the upload. Follow its TCP stream to see the directory listing with the uploaded file included. The file size is shown in one of the columns of that listing.

> ⚠️ **Submit the number with a comma** as it appears in the directory listing. It's a 5-digit number.

---

### Step 4 - Q8: File Downloaded by Anonymous User

Apply the filter again:

```
ftp.response.code == 230
```

This time follow the **second TCP stream** in the results (not the first one from Step 2). This stream shows a session from a user named `anonymous`. Look through the stream for a `RETR` command, that's the FTP download command. The filename following it is what the anonymous user downloaded.

> 💡 **Q8 hint:** The anonymous user downloads the same file that was uploaded in Q6. Someone left the door open.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** TCP Stream 0, look at the first `USER` and `PASS` lines. The password is a cybersecurity company name.
- **Q2:** Server banner is the very first line of TCP Stream 0. It includes a name, version number, and the word beta.
- **Q3:** Use `ftp.response.code == 230` filter. Same username as Q1, different password. Don't submit Q1's answer again.
- **Q4:** First command after login. Think about what you'd do first on an FTP server. Three capital letters, very common FTP command.
- **Q5:** Look for `DELE` in the TCP stream. The filename ends in `.cap`.
- **Q6:** Look for `STOR` in the TCP stream. The filename ends in `.zip`.
- **Q7:** Follow the ftp-data stream around 152 seconds. The file size is a 5-digit number with a comma.
- **Q8:** Second TCP stream from the `ftp.response.code == 230` filter. Look for `RETR`.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit the same answer for Q1 and Q3.** The first attempt fails. Q3 asks for the first *successful* login which uses a different password.
- ❌ **Don't submit `USER` for Q4.** `USER` is an authentication step, not a command the user executes on the server. The question asks for the first command run after login.
- ❌ **Don't forget the comma in Q7.** Submit the file size exactly as shown in the directory listing.
- ✅ **Follow TCP streams** rather than reading individual packets. FTP conversations are split across many packets and the stream view assembles them for you.
- ✅ **Use `ftp.response.code == 230`** to jump straight to successful logins without manually hunting through all the failed attempts.

---

## 🧠 Why This Works

FTP was designed in 1971, long before security was a consideration. Everything is sent in plaintext over the wire: the username, the password, every command, and every byte of every file transferred. Anyone on the same network running a packet capture tool can read all of it. This is why FTP has been largely replaced by SFTP (SSH File Transfer Protocol) and FTPS (FTP over TLS) in modern environments. When you see FTP still in use today, it's a significant security finding. This challenge demonstrates exactly how easy it is to extract credentials and files from an unencrypted FTP session.

---

## 🔗 Resources

- [NCL FTP Tutorial Video](https://www.youtube.com/watch?v=qgM-HLy8BJk&t=1100s)
- [Wikipedia - File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [Wireshark Documentation](https://www.wireshark.org/docs/)

---

*Written by: Mo | Last updated: March 2026*
