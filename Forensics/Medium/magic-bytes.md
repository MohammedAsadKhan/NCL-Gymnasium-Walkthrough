# Forensics Medium - Magic Bytes

> **Category:** Forensics
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a file called `flag.jpeg` that refuses to open. It's been tampered with. Your job is to figure out what the file actually is, fix its magic bytes using a hex editor, and recover the flag inside.

> 💡 This one is highly visual. The official NCL YouTube walkthrough is excellent for this challenge and walks through every step: [Magic Bytes Tutorial](https://www.youtube.com/watch?v=t3Ek_VMRzRM&t=1s)

---

## 🛠️ Tools Needed

- **[CyberChef](https://gchq.github.io/CyberChef/)** - to inspect the raw hex and run Strings
- **[HexEd.it](https://hexed.it/)** - to edit the magic bytes directly
- The `flag.jpeg` file downloaded from the challenge

---

## 📚 Quick Primer: What Are Magic Bytes?

Before diving in, here's what you need to know.

**What is hex?**

Hex (hexadecimal) is a base-16 number system that uses digits 0-9 and letters A-F. Each byte of data is represented as two hex characters. For example, the decimal number 255 is `FF` in hex, and 0 is `00`.

When you open a file in a hex editor, you see the raw contents of the file as hex values rather than what the program normally shows you. The left column is the byte offset (where you are in the file), the middle is the hex values, and the right side shows the ASCII text equivalent where readable.

**What are magic bytes?**

Every file format has a unique sequence of bytes at the very beginning of the file that identifies what type it is. These are called **magic bytes** or a **file signature**. Programs use these to know how to read the file, before even looking at the file extension.

Here are some common ones you'll see in CTF challenges:

| File Type | Magic Bytes (Hex) |
|---|---|
| JPEG | `FF D8 FF E0` |
| PNG | `89 50 4E 47 0D 0A 1A 0A` |
| PDF | `25 50 44 46` |
| ZIP | `50 4B 03 04` |
| GIF | `47 49 46 38` |

If the magic bytes are wrong or corrupted, the file won't open even if the extension is correct. This is exactly what happened to `flag.jpeg`.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Try to Open the File

Download `flag.jpeg` and try to open it in any image viewer. It will fail. The file is broken.

This is your first clue that something has been tampered with.

---

### Step 2 - Inspect the Hex in CyberChef

1. Go to [CyberChef](https://gchq.github.io/CyberChef/)
2. Load `flag.jpeg` into the Input box
3. Search for **"View Bit"** or use the **"To Hex"** recipe to see the raw hex values

Look at the very first bytes of the file. A valid JPEG with EXIF data starts with:

```
FF D8 FF E0 00 10 4A 46 49 46 00 01
```

The file's bytes are close to this but not quite right. One byte near the end of that sequence doesn't match. That's the tampering.

---

### Step 3 - Run Strings to Find the True File Type

Still in CyberChef:

1. Search for the **"Strings"** recipe and drag it into the Recipe
2. Run it on the file

Scan through the output for recognizable text strings embedded in the file. You're looking for two specific ones: `IHDR` and `IDAT`.

These strings are not part of the JPEG format. Search online for what file format uses `IHDR` and `IDAT` and you'll find your answer for Q1.

> 💡 `IHDR` is the PNG image header chunk and `IDAT` is the PNG image data chunk. Their presence confirms this file is actually a PNG that has been disguised with broken JPEG magic bytes.

---

### Step 4 - Fix the Magic Bytes in HexEd.it

Now you know the file is really a PNG. The correct PNG magic bytes are:

```
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D
```

That's 12 bytes total. You need to replace the first 12 bytes of the file with exactly these values.

1. Go to [HexEd.it](https://hexed.it/)
2. Click **Open File** and load `flag.jpeg`
3. Click on the very first byte in the hex view (top left, offset `00000000`)
4. Carefully replace the first 12 bytes one by one with the PNG signature values above

The bytes to enter are:
```
89  50  4E  47  0D  0A  1A  0A  00  00  00  0D
```

> 💡 In HexEd.it you click on a byte and type the new hex value directly. Take it slow and double check each value as you go. One wrong byte and the file still won't open.

---

### Step 5 - Export and Open the Fixed File

Once all 12 bytes are corrected:

1. Click **Export** in HexEd.it to download the modified file
2. Rename the downloaded file from `flag.jpeg` to `flag.png`
3. Open `flag.png` in any image viewer

The image will open and the flag will be visible right on it in `SKY-ABCD-1234` format.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Look for two specific chunk identifiers in the Strings output. One is 4 letters starting with I, the other is 4 letters also starting with I. Google either one and the file format will be immediately obvious.
- **Q2:** The PNG magic bytes are exactly 12 bytes long. Replace all 12 starting from byte 0. Don't miss the last 4 bytes (`00 00 00 0D`) or the file will still fail to open.

---

## ⚠️ Accuracy Tips

- ❌ **Don't just rename the file to `.png` without fixing the hex.** The extension change alone won't fix it. The magic bytes inside the file have to be corrected first.
- ❌ **Don't miss any of the 12 bytes.** The PNG signature is 8 bytes (`89 50 4E 47 0D 0A 1A 0A`) plus 4 more (`00 00 00 0D`). All 12 must be correct.
- ✅ **Go slowly in HexEd.it.** Click each byte, type the value, confirm it updated, move to the next one.
- ✅ **Export from HexEd.it before renaming.** The rename step comes after you've downloaded the corrected file.

---

## 🧠 Why This Works

Attackers and CTF challenge designers corrupt or swap magic bytes to hide what a file really is. A JPEG extension and broken JPEG magic bytes would fool most casual observers and many automated tools. But the actual file content, the PNG chunk headers like `IHDR` and `IDAT`, can't be faked without breaking the file entirely. This is why forensic analysts never trust file extensions alone and always verify magic bytes when analyzing suspicious files. It's also why the `file` command on Linux reads magic bytes rather than the extension to identify files.

---

## 🔗 Resources

- [NCL Tutorial Video - Magic Bytes](https://www.youtube.com/watch?v=t3Ek_VMRzRM&t=1s)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [HexEd.it](https://hexed.it/)
- [File Signatures Reference](https://www.garykessler.net/library/file_sigs.html)
- [PNG File Format Specification](https://en.wikipedia.org/wiki/PNG#File_format)

---

*Written by: Mo | Last updated: February 2026*
