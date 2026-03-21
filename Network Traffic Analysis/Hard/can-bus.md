# Network Traffic Analysis Hard - CAN Bus

> **Category:** Network Traffic Analysis
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a CAN bus packet capture from a vehicle, extract speed data using the provided code snippet, and determine the number of unique IDs, speed message count, and maximum speed reached.

> 💡 This challenge is genuinely unique. Most CTFs don't touch automotive networks. CAN bus is the communication backbone of virtually every modern vehicle and understanding it is an increasingly valuable skill as cars become more connected and hackable.

---

## 📖 What Is CAN Bus?

CAN (Controller Area Network) bus was developed by Bosch in the 1980s and became the standard communication protocol for vehicles. Every modern car uses it. The engine control unit, transmission, brakes, airbags, dashboard, they all talk to each other over CAN bus.

CAN bus is intentionally simple. It just moves frames of data between nodes. It has no authentication, no encryption, and no access control. This is a significant security problem as researchers have demonstrated that attackers who gain physical or remote access to a vehicle's CAN bus can send fake messages to control brakes, steering, and acceleration. This is the exact type of audit Ohm Motors has asked for.

---

## 🛠️ Tools Needed

- **Wireshark** (pre-installed on Kali)
- **LibreOffice Calc** or Excel, for CSV analysis
- **Python**, for the speed calculation script
- The CAN bus PCAP file downloaded from the challenge

---

## 📚 Understanding the Code Snippet

```c
int speed_id = 589;
int speed_pos = 3;

if (frame.can_id == speed_id) {
    double speed = frame->data[speed_pos] << 8;
    speed += frame->data[speed_pos + 1];
    speed = speed / 100;
    speed = speed * 0.6213751;
    update_speed(speed);
}
```

Breaking this down line by line:

- `frame.can_id == speed_id`, only process frames with CAN ID **589**
- `frame->data[speed_pos] << 8`, take byte at position 3, left shift by 8 (multiply by 256)
- `+= frame->data[speed_pos + 1]`, add byte at position 4
- `/ 100`, the raw value is in kph × 100 (two decimal places of precision)
- `* 0.6213751`, convert kph to mph

So the formula to get speed in mph from a CAN frame with ID 589 is:

```
speed_mph = ((data[3] * 256) + data[4]) / 100 * 0.6213751
```

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Open the PCAP and Add Custom Columns

Open the PCAP in Wireshark:

```bash
wireshark [canbus].pcap
```

You'll see CAN bus frames. To make analysis easier, add the CAN ID and Data as visible columns:

1. Click on any CAN frame in the packet list
2. In the packet details panel, expand **CAN bus**
3. Right-click on **ID** and select **Apply as Column**
4. Expand the **Data** section
5. Right-click on **Data** and select **Apply as Column**

Now your packet list shows the CAN ID and raw data for every frame.

---

### Step 2 - Export to CSV

Go to **File → Export Packet Dissections → As CSV...**

Save the CSV file. This gives you all the frame data in a spreadsheet-friendly format.

---

### Q1 - How Many Unique CAN Bus IDs Are Present?

Open the CSV in LibreOffice Calc or Excel.

Find the ID column. Use a formula or filter to count the number of unique values:

**LibreOffice/Excel method:**
- Select the ID column
- Go to **Data → AutoFilter**
- Or use a pivot table / COUNTIF approach to count unique values

**Command line method:**
```bash
cat canbus.csv | cut -d ',' -f [ID_column_number] | sort -u | wc -l
```

> 💡 **What it looks like:** A two-digit number. Don't count the header row.

---

### Q2 - How Many Speed Update Messages Are Present?

Filter the CSV to only rows where the ID column equals **589**.

**LibreOffice/Excel:** Use AutoFilter on the ID column and select 589. The row count at the bottom is your answer.

**Command line:**
```bash
grep ",589," canbus.csv | wc -l
```

> 💡 **What it looks like:** A three-digit number in the hundreds.

---

### Q3 - Maximum Speed in mph

This requires parsing the Data column for all frames with ID 589, applying the speed formula, and finding the maximum.

**Python script:**

```python
import csv

max_speed = 0

with open('canbus.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Adjust column names to match your CSV headers
        if row['ID'].strip() == '589':
            data = row['Data'].strip().split(':')
            if len(data) >= 5:
                byte3 = int(data[3], 16)
                byte4 = int(data[4], 16)
                speed = ((byte3 * 256) + byte4) / 100 * 0.6213751
                if speed > max_speed:
                    max_speed = speed

print(f"Max speed: {max_speed:.2f} mph")
```

> 💡 **Note:** The column names in the CSV may differ depending on how Wireshark exported them. Open the CSV first and check the actual column headers, then adjust the script accordingly.

> 💡 **Note:** The Data field format may use colons or spaces between bytes. Check your CSV and adjust `split(':')` if needed.

Run the script:

```bash
python3 speed.py
```

> 💡 **What it looks like:** A decimal number under 25 mph. Round to the nearest hundredth.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Export to CSV, count unique values in the ID column. It's a two-digit number.
- **Q2:** Filter to ID = 589 only. Count those rows. Three digits, in the hundreds.
- **Q3:** Apply the formula from the code snippet to every ID 589 frame. `(byte3 * 256 + byte4) / 100 * 0.6213751`. Round to two decimal places. The car was not going very fast.

---

## ⚠️ Accuracy Tips

- ❌ **Don't apply the formula to all frames.** Only frames with CAN ID 589 contain speed data.
- ❌ **Don't forget the byte positions.** The formula uses `data[3]` and `data[4]`, which are the 4th and 5th bytes (index starts at 0).
- ❌ **Don't round early.** Do all the math first, then round to the nearest hundredth at the very end.
- ✅ **Check your CSV column names** before running the script. The headers vary by Wireshark version.
- ✅ **Check the Data field delimiter.** Bytes may be separated by colons, spaces, or other characters depending on how Wireshark exported them.

---

## 🧠 Why This Works

CAN bus was never designed with security in mind. There is no sender authentication, so any node on the bus can send any message. Researchers Charlie Miller and Chris Valasek famously demonstrated in 2015 that they could remotely take over a Jeep Cherokee via its internet-connected infotainment system, get onto the CAN bus, and control brakes and steering. The attack made headlines and led to a 1.4 million vehicle recall. Modern vehicles are adding security layers like intrusion detection systems and message authentication codes to CAN frames, but legacy vehicles remain vulnerable. This challenge gives you a taste of the forensic side: reading and interpreting real vehicle telemetry data from a bus capture.

---

## 🔗 Resources

- [NCL CAN Bus Tutorial Video](https://www.youtube.com/watch?v=6b7zpkkOLm0&t)
- [CAN Bus - Wikipedia](https://en.wikipedia.org/wiki/CAN_bus)
- [Miller & Valasek Jeep Hack Research](https://illmatics.com/Remote%20Car%20Hacking.pdf)

---

*Written by: Mo | Last updated: March 2026*
