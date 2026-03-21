# Web Application Medium - Never Winter Bank

> **Category:** Web Application
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You've been hired to pentest a bank's outdated web application. Find a logic vulnerability in the code that allows you to drain a user's account by exploiting inconsistent use of JavaScript's `parseInt()` function.

> 🚨 **The flag is dynamically generated.** Every player gets a different flag in `SKY-XXXX-XXXX` format. Don't compare yours with anyone else's.

> 💡 Open the challenge in a separate Firefox window to keep your developer tools clean.

**Challenge URL:** `https://0cc9533d2749b1187e08ad2d65b0318c-neverwinter-bank.web.cityinthe.cloud/`

---

## 🛠️ Tools Needed

- **Firefox** (recommended)
- Browser address bar, no special tools needed for this one
- Basic understanding of number bases (decimal vs octal)

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Find the Leaked File

A classic first step in web reconnaissance is checking `/robots.txt`. This file tells search engine crawlers which pages NOT to index, which ironically is often a treasure map of interesting pages the developer didn't want people to find.

Navigate to:

```
https://0cc9533d2749b1187e08ad2d65b0318c-neverwinter-bank.web.cityinthe.cloud/robots.txt
```

The file contains a `Disallow` entry pointing to a JavaScript file. That path is your **Q1 answer**.

---

### Step 2 - Read the Leaked JavaScript

Navigate to the path you found in Q1. Add it to the base URL:

```
https://0cc9533d2749b1187e08ad2d65b0318c-neverwinter-bank.web.cityinthe.cloud/dev/rel.js
```

You'll see commented source code with a TODO note saying the auditor flagged something wrong. Here's the relevant snippet:

```javascript
// TODO auditor says something is wrong with this code....
if (parseInt(amount) < account.amount) {
  if ((account.amount - parseInt(amount)) < account.minimum) {
    return res.status(400).send('Error: Account is not allowed to have a balance lower than 10');
  }
  var transferAmount = parseInt(amount, 10);
  account.amount -= transferAmount;
}
```

Spot the bug before reading further. Something is inconsistent about those three `parseInt` calls.

---

### Step 3 - Understand the Vulnerability

The bug is subtle. `parseInt` can be called two ways:

- `parseInt(string)`, no base specified, behavior depends on the string format
- `parseInt(string, 10)`, explicitly treats the string as base 10 (decimal)

In older JavaScript runtimes, if you pass a string starting with `0` to `parseInt` without a radix, it treats it as **octal (base 8)**.

So the same input string can produce two completely different numbers:

```javascript
parseInt('01000')     // treats as octal → returns 512
parseInt('01000', 10) // treats as decimal → returns 1000
```

In the bank code:
- The **balance checks** use `parseInt(amount)` (no radix), reads octal
- The **actual transfer** uses `parseInt(amount, 10)`, reads decimal

This means if you enter `01000`, the check thinks you're transferring 512 but the bank actually moves **1000**. Since the account has 1000 and only needs a minimum balance of 10, the check passes (1000 - 512 = 488, which is above 10) but the transfer drains far more than the check allowed.

---

### Step 4 - Q2: Get the Flag

Go to the bank application and find the transfer/withdrawal field. Enter a value that exploits the octal parsing bug.

Any octal string between `01000` and `01736` will work:

- `01000` in octal = 512 (what the check sees), but transfers 1000 in decimal
- `01736` in octal = 990 (max that keeps balance above 10 in the check), transfers 1774 in decimal

Enter `01000` in the amount field and submit. If successful, the flag will appear.

> 💡 **Why the range matters:** The check requires `account.amount - parseInt(amount) >= 10`. Since the account has 1000 and the check reads octal, you need the octal value to be at most 990. And the transfer needs to exceed the account balance to drain it, so the decimal value must be at least 1000. `01000` is the sweet spot that satisfies both.

> 💡 **What if it doesn't work?** Try other values in the `01000` to `01736` range. `01000` is the most straightforward.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Check `/robots.txt` first. The disallowed path is your answer. It's a JavaScript file in a `/dev/` directory.
- **Q2:** The bug is `parseInt` without a radix treating your input as octal. Enter a string starting with `0` that in octal is under 990 but in decimal is over 1000. Try `01000`.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit someone else's flag.** The flag is dynamically generated and unique to you.
- ❌ **Don't enter `00999`.** That's only 999 in decimal which doesn't exceed the balance. You need at least 1000.
- ✅ **Submit Q1 with the full path** including the leading slash: `/dev/rel.js`
- ✅ **The flag is `SKY-XXXX-XXXX` format** as usual even though it's randomly generated.

---

## 🧠 Why This Works

This vulnerability is a real class of bug called a **radix confusion** or **integer parsing bug**. The JavaScript specification actually changed in ES5 to remove the automatic octal interpretation of leading-zero strings, but older runtime environments still exhibit this behavior. It's a perfect example of how subtle inconsistencies in code, three calls to the same function, two with a radix and one without, can create exploitable logic flaws. The auditor in the TODO comment caught it but apparently nobody fixed it. In a real bank application this would be a critical finding leading to financial fraud. The broader lesson: always be explicit about your number base when parsing user input. Never assume.

---

## 🔗 Resources

- [parseInt() Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
- [Radix - Wikipedia](https://en.wikipedia.org/wiki/Radix)
- [Octal Number System](https://en.wikipedia.org/wiki/Octal)
- [OWASP - Business Logic Vulnerabilities](https://owasp.org/www-community/vulnerabilities/Business_logic_vulnerability)

---

*Written by: Mo | Last updated: March 2026*
