# Cryptography Easy - Strings

> **Category:** Cryptography
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

A flag has been hidden inside an image file using steganography. Your job is to find it using basic Linux command line tools.

> 🐉 If you don't have a Linux environment set up yet, now is the time. Install **Kali Linux**: it comes pre-loaded with every tool you'll need for NCL and beyond. Welcome to the cool side.
>
> ```
>        .--. 
>       |o_o |
>       |:_/ |
>      //   \ \
>     (|     | )
>    /'\_   _/`\
>    \___)=(___/
> ```

---

## 🛠️ Tools Needed

- **Kali Linux** (or any Linux/WSL terminal)
- `strings` command (built into Linux)
- `grep` command (built into Linux)
- The `Steg1.jpg` file downloaded from the challenge

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Download the Image

Download `Steg1.jpg` from the challenge prompt window to your machine. If you're on Kali or WSL, note the path where you saved it.

---

### Step 2 - Understand What's Going On

The image has a flag hidden in its raw binary data. This is a technique called **steganography**: hiding data inside other files. The flag isn't visible when you open the image normally, but it's sitting in the file's binary as plain text characters.

The `strings` command extracts any sequences of readable text characters from a binary file. Since the flag is plain text hiding inside binary image data, `strings` will pull it right out.

> 🔍 Think of it like this: the image file is a massive wall of 0s and 1s. Most of it is pixel data that doesn't translate to readable text. But somewhere in there is the flag written as normal characters. `strings` skips all the noise and shows you only the parts that look like real text.

---

### Step 3 - Run the Command

Open your terminal, navigate to where you saved the image, and run:

```bash
strings Steg1.jpg | grep SKY
```

Here's what each part does:

- `strings Steg1.jpg`: extracts all readable text from the image file
- `|`: the pipe character, passes the output of `strings` directly into `grep`
- `grep SKY`: filters the output and shows only lines containing "SKY"

Your flag will appear in the terminal output in `SKY-ABCD-1234` format.

> 💡 If the file is in a different directory than where your terminal is, either `cd` into that folder first or include the full path: `strings /path/to/Steg1.jpg | grep SKY`

---

## ⚠️ Accuracy Tips

- ❌ **Don't open the image in an image viewer and try to find the flag visually.** It's hidden in the binary, not visible in the actual picture.
- ✅ **Copy-paste the flag exactly** from the terminal output. Don't retype it manually.
- ✅ **If grep returns nothing**, double check the filename matches exactly including capitalization and the `.jpg` extension.

---

## 🧠 Why This Works

`strings` and `grep` are two of the most used tools in a security professional's daily workflow. You'll use `strings` constantly when analyzing malware, suspicious files, and CTF challenges to quickly extract readable data without needing a full disassembler. `grep` is equally essential for searching through logs, command output, and file contents. Piping commands together with `|` is a core Linux skill that lets you chain tools into powerful one-liners. This challenge is your first taste of real Linux forensics work.

---

## 🔗 Resources

- [Kali Linux Download](https://www.kali.org/get-kali/)
- [strings command - Linux man page](https://linux.die.net/man/1/strings)
- [grep command - Linux man page](https://linux.die.net/man/1/grep)
- [Steganography - Wikipedia](https://en.wikipedia.org/wiki/Steganography)

---

*Written by: Mo | Last updated: February 2026*
