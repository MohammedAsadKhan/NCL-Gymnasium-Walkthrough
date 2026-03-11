# Log Analysis Hard - Payments

> **Category:** Log Analysis
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

A payment transaction log was compromised in a data breach. The log file is from a SOAP web server and contains raw XML payment data buried inside debug lines. You'll need to extract the XML, convert it to a spreadsheet, and analyze the payment data to answer questions about the breach.

> 💡 We've included the pre-extracted `requests.xml` and `responses.xml` files in the `hard/` folder for convenience. That said, we highly recommend doing the extraction yourself at least once. Understanding how to pull structured data out of a messy log file is a skill you'll use again and again.

---

## 🛠️ Tools Needed

- Kali Linux terminal with `sed` (pre-installed)
- **LibreOffice Calc** (install instructions below) or Excel or any CSV editor
- **[ConvertCSV](https://www.convertcsv.com/xml-to-csv.htm)** - to convert XML to CSV
- The `payments.log` file downloaded from the challenge

---

## ⚙️ Installing LibreOffice

If you don't have LibreOffice installed on Kali, install it with:

```bash
sudo apt update
sudo apt install libreoffice -y
```

Once installed, open a CSV file with:

```bash
libreoffice --calc filename.csv
```

> 💡 You can use Excel, Google Sheets, or any other spreadsheet editor instead of LibreOffice. The steps are the same regardless of which tool you use. LibreOffice is free and already available on most Linux systems.

---

## 📚 Understanding the Log Format

The log file is full of debug noise. Most lines are irrelevant. The only lines that matter are the ones that start with:

- `PPAPIService: Request:` - contains the payment request XML
- `PPAPIService: Response:` - contains the payment response XML

Each request contains the order details like the buyer's address, items, and total. Each response contains the transaction ID assigned by the payment processor.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Extract the XML from the Log

Use `sed` to pull out just the relevant lines and save them as separate XML files:

```bash
sed -nr 's/PPAPIService: Request: (.*)/\1/p' payments.log > requests.xml
sed -nr 's/PPAPIService: Response: <\?.*\?>(.*)/\1/p' payments.log > responses.xml
```

What each command does:
- `sed -nr`: runs sed in quiet mode (`-n`) with extended regex (`-r`)
- `s/PPAPIService: Request: (.*)/\1/p`: matches lines starting with `PPAPIService: Request:`, captures everything after it, and prints just that captured part
- The responses command also strips the opening XML declaration tag to keep the format clean

> ⚠️ **Before converting, you MUST wrap each XML file** with root tags or the converter will reject it. Add `<xml>` to the very first line and `</xml>` to the very last line of both files:

```bash
sed -i '1s/^/<xml>\n/' requests.xml && echo "</xml>" >> requests.xml
sed -i '1s/^/<xml>\n/' responses.xml && echo "</xml>" >> responses.xml
```

---

### Step 2 - Convert XML to CSV

1. Go to [ConvertCSV XML to CSV](https://www.convertcsv.com/xml-to-csv.htm)
2. Upload `requests.xml` and convert it, download as `requests.csv`
3. Upload `responses.xml` and convert it, download as `responses.csv`

---

### Step 3 - Open in LibreOffice

```bash
libreoffice --calc requests.csv
```

When LibreOffice asks about the delimiter, make sure **Comma** is selected. Click OK and the data will open as a properly formatted spreadsheet.

Do the same for `responses.csv`.

---

### Step 4 - Q1: Count the Transactions

Each row in the spreadsheet is one transaction. Count the rows of data (not including the header row).

From the command line you can also just count directly:

```bash
grep -c "PPAPIService: Request:" payments.log
```

> 💡 **What the answer looks like:** A three digit number under 200.

---

### Step 5 - Q2: Find the Transaction ID of the Largest Purchase

In `requests.csv`, find the column for the order total. It's column `F`.

**In LibreOffice:**
1. Click the column `F` header to select the whole column
2. Go to **Data > Sort** and sort column F from largest to smallest
3. The top row after sorting is the largest purchase, note the row number
4. Now open `responses.csv` and find the same row number
5. Look at column `Z` which contains the transaction ID

> ⚠️ **Don't submit the order total as the answer.** The question asks for the transaction ID, which is a UUID in the format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` found in the responses file.

---

### Step 6 - Q3: Which State Made the Most Purchases

In `requests.csv`, find the column for the ship-to state (the buyer's state).

**In LibreOffice:**
1. Right-click the column header for the ship-to state
2. Select **Column Statistics**
3. The most common value at the top is your answer

OR from the command line, find the state column number first, then:

```bash
cat requests.csv | cut -d ',' -f [column_number] | sort | uniq -c | sort -rn | head -5
```

The state with the highest count is your answer. It's a full state name, not an abbreviation.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Count the request lines directly with grep. Fast and accurate.
- **Q2:** Sort by the order total column descending. The transaction ID is a UUID with hyphens. It's in the responses file at the same row number as the largest order.
- **Q3:** A state in New England. Not the biggest state but apparently doing a lot of online shopping.

---

## ⚠️ Accuracy Tips

- ❌ **Don't forget to add `<xml>` and `</xml>` tags** before converting. Without them, the converter will throw an error or produce garbage output.
- ❌ **Don't confuse the requests and responses files.** Order totals are in requests. Transaction IDs are in responses. Match them by row number.
- ❌ **Don't submit the dollar amount for Q2.** The answer is the UUID transaction ID, not the price.
- ✅ **If LibreOffice doesn't parse the CSV correctly**, check that you selected comma as the delimiter when importing.
- ✅ **The pre-extracted `requests.xml` and `responses.xml` files** are in the `hard/` folder if you want to skip straight to the conversion step.

---

## 🧠 Why This Works

SOAP (Simple Object Access Protocol) is a messaging format used heavily in enterprise and financial systems to send structured data between services. Payment processors, banks, and e-commerce platforms all use SOAP or similar XML-based APIs. When these systems log their raw requests and responses for debugging, they can inadvertently store sensitive payment data in plaintext log files. This challenge demonstrates exactly how an attacker who gains access to a server's log files can extract complete payment records including addresses, order details, and transaction IDs, without ever touching the actual database. It's also why security-conscious organizations scrub or encrypt sensitive fields before writing to logs.

---

## 🔗 Resources

- [ConvertCSV XML to CSV](https://www.convertcsv.com/xml-to-csv.htm)
- [LibreOffice Download](https://www.libreoffice.org/download/download/)
- [SOAP Protocol - Wikipedia](https://en.wikipedia.org/wiki/SOAP)

---

*Written by: Mo | Last updated: February 2026*
