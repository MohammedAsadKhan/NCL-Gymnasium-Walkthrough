# 🔬 Forensics Walkthroughs

Digging through files, images, and artifacts to uncover hidden data and reconstruct what happened.

---

## A Word Before You Start

Forensics is, in Mo's opinion, the hardest category in the entire NCL Gymnasium. Not because any single concept is impossibly difficult, but because the tools are more complex, the steps are less obvious, and small mistakes can send you in completely the wrong direction.

**Be patient with yourself on this one.** If you're stuck, don't just guess and tank your accuracy. Instead:

- Re-read the walkthrough carefully from the beginning
- Check the NCL Discord `#ctf-help` channel and ask for help
- Watch the official NCL YouTube walkthroughs linked in each challenge
- Come back to it with fresh eyes if you've been staring at it for a while

A wrong answer hurts your score more than no answer. When in doubt, ask.

---

## What to Expect in NCL Forensics

NCL Forensics challenges ask you to extract information from files, analyze metadata, recover deleted data, examine file structures, and interpret artifacts left behind by programs and operating systems. You'll work with tools like Autopsy, Wireshark, hex editors, and file carving utilities.

> 💡 Screenshots are included throughout these walkthroughs to show you exactly what things should look like at each step. If your screen doesn't match the screenshot, something went wrong and you should go back and check your steps before continuing.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [version-control.md](easy/version-control.md) | Analyzing Git version control history |
| [pdf-examination.md](easy/pdf-examination.md) | Examining PDF file structure and metadata |

### 🟡 Medium
| File | Topic |
|---|---|
| [file-carving.md](medium/file-carving.md) | Recovering files from raw disk images |
| [magic-bytes.md](medium/magic-bytes.md) | Identifying and correcting file magic bytes |
| [docter.md](medium/docter.md) | Extracting hidden files from Word documents |

### 🔴 Hard
| File | Topic |
|---|---|
| [the-book.md](hard/the-book.md) | Windows memory forensics with Volatility3 |

---

## Forensics Quick Reference

**Common file signatures (magic bytes):**
```
FF D8 FF      JPEG image
89 50 4E 47   PNG image
50 4B 03 04   ZIP archive
25 50 44 46   PDF document
47 49 46 38   GIF image
```

**Useful commands:**
```bash
file suspicious.bin          # Identify file type
xxd suspicious.bin | head    # View hex dump
strings suspicious.bin       # Extract readable text
exiftool file.jpg            # View metadata
binwalk file.bin             # Scan for embedded files
foremost -i disk.img         # Carve files from image
```

**Tools you'll need:**
- **Autopsy** - GUI forensic analysis suite
- **Wireshark** - Network packet analysis
- **ExifTool** - File metadata extraction
- **Binwalk** - Firmware/file analysis
- **Foremost** - File carving
- **xxd / hexdump** - Hex editors

---

*Written by: Mo | Last updated: February 2026*
