# OSINT Medium - Barcode

> **Category:** OSINT
> **Difficulty:** Medium (we use that term loosely here)
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a `.gif` image of a barcode and asked two questions about it. Scan the barcode, read the results. That's it. We're not sure who classified this one as medium, but here we are.

> 💡 This is genuinely one of the easiest challenges in the entire Gymnasium. Don't overthink it.

---

## 🛠️ Tools Needed

- **[online-barcode-reader.inliteresearch.com](https://online-barcode-reader.inliteresearch.com/)** - works great for this
- Or any barcode scanning app on your phone
- The barcode .gif file downloaded from the challenge

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Download the Barcode

In the NCL challenge window, download the provided `barcode.gif` file to your computer. Make sure you're saving the actual file, not just screenshotting it.

---

### Step 2 - Upload It to a Barcode Reader

Go to **[online-barcode-reader.inliteresearch.com](https://online-barcode-reader.inliteresearch.com/)**.

Click to upload your image and select the `barcode.gif` you just downloaded. Hit read/scan.

You'll get a results box showing two things: the **Type** (format) of the barcode, and the **Value** (what's encoded in it).

That's your whole challenge right there.

---

### Step 3 - Q1: What Format Is the Barcode?

Look at the **"Type"** field in the results.

> 📦 Fun fact: there are dozens of barcode formats out there. The one used here was invented in 1974 and is named after how many characters it can encode. It's the kind you'd see on ID badges and industrial equipment, not grocery store products. The name has a number in it... and that number isn't very high.

Your answer is the format name followed by that number.

---

### Step 4 - Q2: What Is the Flag?

Look at the **"Value"** field in the results. The barcode encodes the flag directly.

NCL flags follow the format `SKY-ABCD-1234`, four letters followed by four numbers. If your barcode reader gave you something in that format, you've got it.

> ⚠️ Make sure you're submitting the value exactly as shown. Capitalization matters and don't add or remove any characters.

---

## ⚠️ Accuracy Tips

- ❌ **Don't type the flag manually.** Copy-paste it directly from the barcode reader results to avoid typos.
- ✅ **If one barcode reader doesn't work, try another.** Some online tools handle `.gif` files better than others. Your phone's camera app scanning the screen also works in a pinch.
- ✅ **The format name and the value are two separate fields.** Don't submit the format name as the flag or vice versa.

---

## 🧠 Why This Works

Barcodes encode data in a machine-readable visual format. As a security professional you'll encounter barcodes and QR codes in physical security assessments, badge cloning research, and supply chain investigations. Knowing that barcodes have different formats (and that those formats have different capabilities) is genuinely useful context, even if this particular challenge is... not exactly a brain-buster.

---

## 🔗 Resources

- [Online Barcode Reader - Inlite](https://online-barcode-reader.inliteresearch.com/)
- [Code 39 - Wikipedia](https://en.wikipedia.org/wiki/Code_39)
- [Barcode Formats Overview - Scandit](https://www.scandit.com/resources/guides/barcode-types-and-formats/)

---

*Written by: Mo | Last updated: February 2026*
