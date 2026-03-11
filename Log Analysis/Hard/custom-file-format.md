# Log Analysis Hard - Custom File Format

> **Category:** Log Analysis
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a binary log file in a custom format called SKY. Unlike every other challenge in this category, this file isn't plain text. It's raw binary data. You're given the file format specification and your job is to parse it using CyberChef and Linux command line tools to extract the data hidden inside.

> 💡 This is the hardest challenge in Log Analysis. Don't skip the file format spec. Read it carefully before touching any tool. The spec tells you exactly where every field is and how long it is. Without that, you're flying blind.

---

## 🛠️ Tools Needed

- **[CyberChef](https://cyberchef.io)** - for parsing binary fields from the file
- Kali Linux terminal with `cut`, `paste`, `awk`, `sort` (all pre-installed)
- The `Custom File Format.sky` file downloaded from the challenge

---

## 📚 Understanding the File Format

Before doing anything, read the spec. Here's the quick reference table for the header fields:

| Field | Offset | Length | Type |
|---|---|---|---|
| Magic Bytes | 0 | 8 bytes | Identifier |
| Version | 8 | 1 byte | Byte |
| Creation Timestamp | 9 | 4 bytes | Unix timestamp |
| Hostname Length | 13 | 4 bytes | Int |
| Hostname | 17 | 14 bytes | String |
| Flag Length | 31 | 4 bytes | Int |
| Flag | 35 | 20 bytes | String (Base64) |
| Number of Entries | 55 | 4 bytes | Int |
| Body (all entries) | 59 | 2592 bytes | Records |

Each entry in the body is exactly **16 bytes long** with this structure:

| Field | Offset from entry start | Length | Type |
|---|---|---|---|
| Source IP | 0 | 4 bytes | Int (IPv4) |
| Destination IP | 4 | 4 bytes | Int (IPv4) |
| Timestamp | 8 | 4 bytes | Unix timestamp |
| Bytes Transferred | 12 | 4 bytes | Int |

> 💡 All fields are Big-Endian. All integers are 32 bits (4 bytes). All timestamps are 32-bit Unix timestamps.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Find the Hostname

The hostname length is a 4-byte integer at offset 13. First find out how long it is:

**CyberChef recipe:**
```
https://cyberchef.io/#recipe=Take_bytes(13,4,false)To_Binary('None',8)From_Base(2)
```

Load the `.sky` file into CyberChef using "Open file as input" and run that recipe. The output tells you the hostname is 14 bytes long.

Now extract the hostname itself (14 bytes starting at offset 17):

**CyberChef recipe:**
```
https://cyberchef.io/#recipe=Take_bytes(17,14,false)
```

The output is the hostname as plain text.

> 💡 `Take_bytes(offset, length, false)` is the core CyberChef operation for this entire challenge. `offset` is where to start reading, `length` is how many bytes to read.

---

### Step 2 - Q2: Find the Plaintext Flag

The flag is stored Base64-encoded. The flag length field at offset 31 tells you it's 20 bytes long. Extract the flag at offset 35 and decode it:

**CyberChef recipe for flag length:**
```
https://cyberchef.io/#recipe=Take_bytes(31,4,false)To_Binary('None',8)From_Base(2)
```

**CyberChef recipe to extract and decode the flag:**

Load the file, take 20 bytes starting at offset 35, then apply From Base64:

1. Go to [CyberChef](https://cyberchef.io)
2. Load the `.sky` file as input
3. Add recipe: `Take_bytes(35, 20, false)`
4. Add recipe: `From Base64`
5. The output is the plaintext flag in `SKY-ABCD-1234` format

---

### Step 3 - Q3: Find the Creation Date

The creation timestamp is a 4-byte Unix timestamp at offset 9. Convert it to a human-readable date:

**CyberChef recipe:**
```
https://cyberchef.io/#recipe=Take_bytes(9,4,false)To_Binary('None',8)From_Base(2)From_UNIX_Timestamp('Seconds%20(s)')
```

This extracts the 4 bytes, converts them to a binary integer, then converts the Unix timestamp to a readable date. Your answer is the date in `YYYY-MM-DD` format.

---

### Step 4 - Q4: Count the Entries

The number of entries is a 4-byte integer at offset 55:

**CyberChef recipe:**
```
https://cyberchef.io/#recipe=Take_bytes(55,4,false)To_Binary('None',8)From_Base(2)
```

The output is the number of log entries in the body.

---

### Step 5 - Q5: Total Bytes Transferred

This recipe extracts all entries, splits them into 16-byte lines, pulls the bytes-transferred field from each, and sums them all:

**CyberChef recipe:**
```
https://cyberchef.io/#recipe=Take_bytes(59,2592,false)To_Hex('Space',16)Fork('%5C%5Cn','%5C%5Cn',false)From_Hex('Space')Take_bytes(12,4,false)To_Hex('None',0)From_Base(16)Merge()Sum('Line%20feed')
```

The output is the total bytes transferred across all log entries.

---

### Step 6 - Q6: Count Unique IP Addresses

This recipe extracts both source and destination IPs from every entry, converts them to dotted decimal format, deduplicates, and counts:

**CyberChef recipe:**
```
https://cyberchef.io/#recipe=Take_bytes(59,2592,false)To_Hex('Space',16)Fork('%5C%5Cn','%5C%5Cn',false)From_Hex('Space')Take_bytes(0,8,false)To_Hex('None',4)Change_IP_format('Hex','Dotted%20Decimal')Merge()Unique('Line%20feed',false)Regular_expression('IPv4%20address','(?:(?:%5C%5Cd%7C%5B01%5D?%5C%5Cd%5C%5Cd%7C2%5B0-4%5D%5C%5Cd%7C25%5B0-5%5D)%5C%5C.)%7B3%7D(?:25%5B0-5%5D%7C2%5B0-4%5D%5C%5Cd%7C%5B01%5D?%5C%5Cd%5C%5Cd%7C%5C%5Cd)(?:%5C%5C/%5C%5Cd%7B1,2%7D)?',true,true,false,false,false,true,'List%20matches')
```

Count the IP addresses in the output for your answer.

---

### Step 7 - Build the Human-Readable Log (Required for Q7, Q8, Q9)

The last three questions require a merged human-readable log. This takes several steps. Do them in order.

**First**, use this CyberChef recipe to create a column-formatted hex version of all entries and save the output as `hex.log`:

Extract body bytes, split into 16-byte lines, split those into 4-byte columns:

1. Load the `.sky` file in CyberChef
2. Run: `Take_bytes(59, 2592, false)` then `To_Hex('Space', 16)`
3. Copy the entire output into a file called `hex.log`

**Then extract and convert each column individually:**

**Column 1 - Source IPs:**
```bash
cat hex.log | cut -d " " -f 1 > col1_hex.txt
```
Paste `col1_hex.txt` contents into CyberChef and convert hex to IPv4 addresses. Save as `col1.log`.

**Column 2 - Destination IPs:**
```bash
cat hex.log | cut -d " " -f 2 > col2_hex.txt
```
Same conversion as Column 1. Save as `col2.log`.

**Column 3 - Timestamps:**
```bash
cat hex.log | cut -d " " -f 3 > col3_hex.txt
```
Paste into CyberChef and convert to dates. Save as `col3.log`.

**Column 4 - Bytes Transferred:**
```bash
cat hex.log | cut -d " " -f 4 > col4_hex.txt
```
Paste into CyberChef and convert hex to integers. Save as `col4.log`.

**Finally, merge all columns into one readable log:**
```bash
paste col1.log col2.log col3.log col4.log > merged.log
```

`merged.log` now has one entry per line with source IP, destination IP, date, and bytes transferred separated by tabs.

---

### Step 8 - Q7 and Q8: IP That Sent the Most Data

Use `awk` to sum bytes transferred per source IP and sort:

```bash
awk '{sums[$1]+=$4} END {for (ip in sums) print sums[ip], ip}' merged.log | sort -n
```

What this does:
- `sums[$1]+=$4`: builds a running total of bytes (column 4) grouped by source IP (column 1)
- `END`: after processing all lines, print the results
- `sort -n`: sorts numerically, highest total at the bottom

The last line shows the IP that sent the most data (Q7) and the total bytes it sent (Q8).

---

### Step 9 - Q9: Busiest Day

Same pattern but group by date instead of IP:

```bash
awk '{sums[$3]+=$4} END {for (date in sums) print sums[date], date}' merged.log | sort -n
```

The last line shows the date with the highest total bytes transferred. Your answer is in `YYYY-MM-DD` format.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** A hostname that follows the `sky-server-XXX` naming convention.
- **Q2:** The flag is Base64 encoded in the file. Decode it in CyberChef after extracting it and you'll see the standard `SKY-ABCD-1234` format.
- **Q3:** A date in early 2018. Use the Unix timestamp recipe to convert it.
- **Q4:** A three digit number. Not a huge log file.
- **Q5:** A 6-digit number in the hundreds of thousands of bytes.
- **Q6:** Less than 20 unique IPs. A small internal network.
- **Q7:** An IP in the `229.x.x.x` range.
- **Q8:** A 6-digit number in the hundreds of thousands.
- **Q9:** A date in March 2018.

---

## ⚠️ Accuracy Tips

- ❌ **Don't try to read the file as text.** It's binary. Opening it in a text editor will show garbled output. Use CyberChef with "Open file as input".
- ❌ **Don't manually calculate offsets.** Use the quick reference table at the top and double-check your offset before running any recipe.
- ✅ **Copy the CyberChef recipe URLs exactly** and paste them directly into your browser address bar. They will load the recipe automatically.
- ✅ **Save intermediate files as you go.** The `hex.log`, `col1.log` through `col4.log`, and `merged.log` files all build on each other. Don't skip steps.
- ✅ **For Q3**, submit the date in `YYYY-MM-DD` format, not the full timestamp.

---

## 🧠 Why This Works

Custom binary file formats are everywhere in the real world, firmware images, network captures, proprietary database files, malware payloads. Unlike text logs, binary formats pack data efficiently but require you to understand the structure before you can extract anything useful. This challenge teaches the fundamental skill of reading a format specification and translating it into actual parsing operations, which is exactly what malware analysts do when reverse engineering unknown file formats, and what forensic investigators do when recovering data from proprietary applications. The CyberChef approach here is the same technique used by security researchers to quickly prototype parsers without writing code.

---

## 🔗 Resources

- [CyberChef](https://cyberchef.io)
- [Epoch Converter](https://www.epochconverter.com/)
- [Big-Endian vs Little-Endian](https://en.wikipedia.org/wiki/Endianness)

---

*Written by: Mo | Last updated: February 2026*
