# OSINT Easy - HTTP Headers

> **Category:** OSINT
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge has you researching HTTP request headers. These are small pieces of information your browser automatically sends to a web server every time you visit a page. You just need to match each description to the correct header name.

> 💡 All 3 answers are on the HTTP headers Wikipedia page. Google "HTTP headers Wikipedia," open the page, and CTRL + F your way through it. This one is fast.

---

## 🛠️ Tools Needed

- A web browser
- Google
- Wikipedia
- CTRL + F (seriously, use it)

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: The Header That Tells Where You Came From

You're looking for the HTTP request header that **tells the server which URI (web address) you came from** before clicking the link to get to the current page.

Think of it like this: if you're at a party and someone asks "hey how did you find out about this party?", you'd tell them who referred you. This header does exactly that for web requests, it tells the server "I got here from this other page."

**Where to look:** Google "HTTP headers Wikipedia" and CTRL + F for "address of the previous web page." You'll land right on it.

> ⚠️ Read the note on this one carefully. The header name has a spelling mistake baked into the official specification, and that wrong spelling is now the accepted standard. So the "correct" answer is technically the misspelled version. Make sure you submit it exactly as it appears in the spec, typo and all.

Your answer will look like a normal English word that means "someone who sent you here," just spelled a little off.

---

### Step 2 - Q2: The Header That Identifies the Client

You're looking for the HTTP request header that **identifies what software (browser, app, bot, etc.) is making the request**.

> 🤔 Okay so imagine you walk up to a customer service desk. The first thing they ask is "who are you and what are you using to contact us?" Your browser answers that question with this header every single time it talks to a server. It's literally called what it is... it's the header for the "user" and their "agent" (the software acting on their behalf). I wonder what it could be called...

**Where to look:** Google "HTTP headers Wikipedia" and CTRL + F for "user agent string." It'll be right there.

Your answer is two words joined by a hyphen and will feel very self-explanatory once you see it.

---

### Step 3 - Q3: The Header That Says What You'll Accept

You're looking for the HTTP request header that **tells the server what types of content the client is willing to receive back**.

> 🍕 Imagine you're ordering food and the waiter asks "what are you okay with eating?" You tell them what you'll accept. This header does that for web content, it tells the server "here's what I'll accept as a response." In fact, the header is named after exactly that action. What do you tell someone when you're okay with something? You...

**Where to look:** Google "HTTP headers Wikipedia" and CTRL + F for "content negotiation." The header name will be right next to it.

Your answer is a single common English word.

---

## ⚠️ Accuracy Tips

- ❌ **Don't correct the spelling on Q1.** This is the one case in this repo where the wrong spelling is the right answer. The spec made a typo decades ago and now everyone uses it. Submit it as-is.
- ❌ **Watch your capitalization and hyphens.** HTTP header names are specific. "user-agent" and "User-Agent" may or may not both be accepted but match the format you see in the official source.
- ✅ **Use CTRL + F.** The Wikipedia HTTP headers table is long. Don't scroll, just search.
- ✅ **Cross-check with MDN Web Docs** if you're unsure. MDN (developer.mozilla.org) has excellent HTTP header documentation as well.

---

## 🧠 Why This Works

HTTP headers are sent back and forth between your browser and web servers constantly, completely invisible to you. As a cybersecurity professional, headers matter a lot. Attackers manipulate them to bypass security controls, forge identities, and exploit vulnerabilities. Tools like Burp Suite let you intercept and modify headers in real time, which you'll use heavily in Web Application challenges. Knowing what each header does is foundational knowledge for that.

---

## 🔗 Resources

- [List of HTTP header fields - Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
- [HTTP Headers - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

---

*Written by: Mo | Last updated: February 2026*
