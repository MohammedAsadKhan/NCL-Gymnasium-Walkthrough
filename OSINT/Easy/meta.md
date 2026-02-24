# OSINT Easy — Meta

> **Category:** OSINT
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge gives you an image file and asks you to extract information that is hidden inside the file itself — not visible in the photo, but stored in its **metadata**. You'll answer 6 questions about the image using nothing but a metadata viewer.

---

## 🛠️ Tools Needed

- **[Metadata2go](https://www.metadata2go.com/)** — easy browser-based metadata viewer, no install needed
- **[ExifTool](https://exiftool.org/)** — more powerful command-line tool, great for verification
- **Your favorite AI (ChatGPT, Claude, etc.)** — for converting GPS coordinates to the right format (more on this in Step 4)

> 💡 It's good habit to run your image through **two tools** and compare results. If both tools agree, you can be confident in your answer — which protects your accuracy score.

---

## 📋 Step-by-Step Walkthrough

### Step 1 — Download the Image

In the NCL challenge window, there will be a prompt with an image attached. **Download that image** to your computer. Don't just right-click and save from a preview — make sure you're downloading the actual file so the metadata stays intact.

---

### Step 2 — Upload to a Metadata Viewer

Go to **[metadata2go.com](https://www.metadata2go.com/)**.

Click **"Choose File"** and select the image you just downloaded. Hit **"Show Meta Data"**.

You'll get a table with a long list of fields and their values. This is the metadata — information your camera automatically embedded into the photo when it was taken. Things like the date, camera model, settings, and even GPS location can all be stored here without you ever knowing.

> 💡 If you want to double-check your answers, open a second tab and run the same image through **ExifTool** (online version at [exif.tools](https://exif.tools/)) and compare. Both should give you the same values.

---

### Step 3 — Answer Questions 1–5

Now just find the right field in the table for each question. Here's what to look for:

**Q1 — When was the image created?**
Look for the **"Create Date"** field. The answer will be a date and time — you'll need to round it down to the nearest minute, so ignore the seconds. Your answer should look something like a date followed by an hour and minute (think: `YYYY-MM-DD HH:MM`).

**Q2 — What are the dimensions of the image?**
Look for the **"Image Size"** field. The answer will be in the format `WIDTHxHEIGHT` — two numbers separated by an x (ex: `800x600`). Yours will be a common photo resolution.

**Q3 — What is the make of the camera?**
Look for the **"Make"** field. This is the **brand** of the device that took the photo. It'll be a single word — a brand name you'd recognize.

**Q4 — What is the model of the camera?**
Look for the **"Model"** field. This is more specific than the make — it tells you the exact device. Your answer will be a brand name followed by a specific product name.

**Q5 — What is the exposure time?**
Look for the **"Exposure Time"** field. This is a camera setting shown as a fraction (ex: `1/200`). The faster the shutter speed, the smaller the number on the bottom.

---

### Step 4 — Answer Q6: GPS Coordinates

This one takes an extra step, so read carefully.

Look for the **"GPS Position"** field in the metadata. You'll likely see something in **DMS format** — that stands for Degrees, Minutes, Seconds, and it looks like this:

```
51 deg 30' 26.00" N, 0 deg 7' 39.00" W
```

The problem is NCL wants the answer in **decimal format** with 4 decimal places, like this:

```
51.5072N, 0.1275W
```

Those are two different ways of writing the same location — you need to convert.

**The easiest way: paste the DMS coordinates into your favorite AI** (ChatGPT, Claude, etc.) and say:

> *"Convert these GPS coordinates from DMS to decimal format with 4 decimal places: [paste your coordinates here]"*

It'll give you the converted values instantly. Your final answer should have a **North (N)** and **East (E)** value, both positive, each with exactly 4 decimal places.

> ⚠️ Make sure you keep the **N** and **E** direction letters in your answer — don't just submit raw numbers.

---

## ⚠️ Accuracy Tips

- ❌ **Don't round the time up** — the question says round *down* to the nearest minute. Drop the seconds entirely.
- ❌ **Don't flip the image dimensions** — double check which number is width and which is height. The format is `WIDTHxHEIGHT`.
- ❌ **Don't submit GPS in DMS format** — NCL wants decimal format. If your metadata viewer already shows decimals, verify they have exactly 4 decimal places.
- ✅ **Do verify with a second tool** — metadata2go and ExifTool should agree on every field. If they don't, investigate why before submitting.
- ✅ **Do keep the direction letters (N, E)** in your GPS answer.

---

## 🧠 Why This Works

Every photo taken on a modern smartphone or camera stores **EXIF data** (Exchangeable Image File Format) inside the image file. This data is invisible when you look at the photo normally, but it's embedded in the file itself. It includes camera settings, timestamps, software info, and — if location services were on — GPS coordinates.

In real OSINT investigations, EXIF data can reveal where and when a photo was taken, what device was used, and sometimes even the exact location of a person. This is why privacy-conscious people strip metadata from photos before posting them online.

---

## 🔗 Resources

- [Metadata2go](https://www.metadata2go.com/)
- [ExifTool (online)](https://exif.tools/)
- [What is EXIF data? — Simple explanation](https://www.howtogeek.com/773303/what-is-exif-data-and-how-do-you-remove-it/)

---

*Written by: Mo | Last updated: February 2026*
