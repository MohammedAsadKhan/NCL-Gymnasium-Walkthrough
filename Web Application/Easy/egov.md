# Web Application Easy - egov

> **Category:** Web Application
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Conduct a security audit on a government login panel. Bypass authentication by manipulating a browser cookie and access the admin panel to retrieve the flag.

> ⚠️ **Scope:** This challenge is limited to HTTPS only. Do not attack any other ports on the server.

> 🚨 **The flag is dynamically generated.** Every player gets a different flag. Don't compare yours with anyone else's. It will still follow the standard `SKY-XXXX-XXXX` format.

---

## 🛠️ Tools Needed

- **Firefox** (highly recommended for web application challenges)
- Browser Developer Tools (built into Firefox, press **F12**)
- The egov challenge URL from your NCL challenge prompt

> 💡 **Why Firefox?** Firefox has some of the best built-in developer tools for web application security work. The cookie editor, console, and network inspector are clean and easy to use. It's a favorite among web security professionals and works great for NCL web challenges. Open the challenge in a separate Firefox window to avoid confusion between the NCL platform and the challenge site.

---

## 📚 Background: What Are Cookies?

Cookies are small pieces of data that websites store in your browser. They're used for things like keeping you logged in, remembering preferences, and tracking sessions. The problem is that cookies are stored client-side, meaning they live in your browser and you have full control over them. If a website trusts a cookie value without verifying it server-side, you can just change it to whatever you want.

This is exactly the vulnerability in this challenge. The website uses a cookie called `admin` to decide if you're an admin or not. It's set to `false` by default. All you have to do is change it to `true`.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Open the Challenge and Trigger the Cookie

Open the egov URL from your challenge prompt in a **new Firefox window**.

Press **F12** to open Developer Tools.

Submit anything on the login form, it doesn't matter what. This triggers the server to set the `admin` cookie in your browser.

---

### Step 2 - Find and Inspect the Cookie

In the Developer Tools panel, click the **Application** tab (Chrome) or **Storage** tab (Firefox).

Click on **Cookies** in the left sidebar, then click on the website URL below it.

You'll see a cookie named **admin** with a value of **false**. That's your target.

---

### Step 3 - Change the Cookie Value

**Method A: Direct Edit (Easiest)**

In the cookie table, double-click on the **false** value next to the `admin` cookie. Type `true` and press Enter.

**Method B: Browser Console**

Click the **Console** tab in Developer Tools and run:

```javascript
document.cookie = 'admin=true'
```

Press Enter. Then verify it worked by checking the Application/Storage tab again. The value should now show `true`.

---

### Step 4 - Navigate to the Admin Panel

Look at the JavaScript source for clues. In Developer Tools, go to the **Sources** tab and find `login.js`. You'll see it redirects successful logins to `/admin`.

Now add `/admin` to the end of your challenge URL in the browser address bar:

```
https://[challenge-url]/admin
```

Refresh the page if needed. If the cookie is set correctly, you'll be taken to the admin panel and the flag will be displayed.

> 💡 **Alternative method:** With the admin cookie set to true, go back to the login form and submit any password with `admin` as the username. You'll be redirected to the admin panel automatically.

---

## 💡 Hints (Without Giving It Away)

- **Step 1:** Submit any username and password first to trigger the cookie being set. Without submitting, the cookie won't exist yet.
- **Step 2:** F12 → Application or Storage tab → Cookies. Look for the `admin` cookie.
- **Step 3:** Double-click the cookie value and type `true`, or use `document.cookie = 'admin=true'` in the console.
- **Step 4:** Navigate to `/admin` on the challenge URL. The flag is on that page.

---

## ⚠️ Accuracy Tips

- ❌ **Don't forget to submit the login form first.** The `admin` cookie won't appear until the server has sent a response.
- ❌ **Don't compare flags with teammates.** The flag is dynamically generated and unique to each player.
- ✅ **Refresh the page** after changing the cookie to confirm the change stuck.
- ✅ **Use Firefox** for the cleanest developer tools experience. The Storage tab makes cookie editing straightforward.
- ✅ **Flag format is `SKY-XXXX-XXXX`** as usual. If you see something in that format on the admin page, that's your answer.

---

## 🧠 Why This Works

This challenge demonstrates one of the most fundamental web security mistakes: trusting client-side data for authorization decisions. Cookies live in the browser. The user controls them. If the server doesn't verify on its end whether a user is actually an admin, a cookie value of `admin=true` is completely meaningless as a security control. Real authentication systems use session tokens stored server-side and tied to verified user accounts. When you present a session token, the server looks it up in its database to confirm who you are and what you're allowed to do. The cookie value itself never says "I am admin", it just says "here's my session ID, go look me up." This egov site skips that step entirely, which makes it trivially bypassable.

---

## 🔗 Resources

- [NCL Web Cookies Tutorial Video](https://www.youtube.com/watch?v=vrq2K9BrOKk&t=511s)
- [JavaScript Cookies - W3Schools](https://www.w3schools.com/js/js_cookies.asp)
- [OWASP - Insecure Direct Object Reference](https://owasp.org/www-community/attacks/Insecure_Direct_Object_Reference)

---

*Written by: Mo | Last updated: March 2026*
