# 🕸️ Web Application Exploitation Walkthroughs

Finding and exploiting vulnerabilities in web applications through cookie manipulation, SQL injection, authentication bypasses, and more.

---

## A Word Before You Start

Web Application Exploitation is one of the most practical and in-demand categories in cybersecurity. Nearly every organization has a web presence, and web vulnerabilities are consistently among the most commonly exploited attack vectors in real breaches. The skills you build here directly translate to real penetration testing work.

If you're new to web security, start with the easy challenges. They teach foundational concepts like cookies and client-side trust that everything else builds on. By the time you get to Hard, you'll be looking at SQL injection and more advanced authentication bypasses.

> 💡 **Use Firefox** for all web application challenges. It has the best built-in developer tools for web security work. Open each challenge in a separate Firefox window so you don't confuse the NCL platform with the challenge site.

> ⚠️ Only interact with the challenge URLs provided. Never attempt to exploit real websites without explicit written permission.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [egov.md](easy/egov.md) | Cookie manipulation and authentication bypass |
| [never-winter-bank.md](easy/never-winter-bank.md) | Web application reconnaissance |

### 🟡 Medium
| File | Topic |
|---|---|
| [metro-lottery.md](medium/metro-lottery.md) | Web application exploitation |
| [todo.md](medium/todo.md) | Web application vulnerability analysis |

### 🔴 Hard
| File | Topic |
|---|---|
| [leek.md](hard/leek.md) | Advanced web exploitation |
| [metro-clinic.md](hard/metro-clinic.md) | Advanced web application security |

---

## Web App Quick Reference

**Open Developer Tools in Firefox:**
```
F12  or  Right-click → Inspect Element
```

**Useful Developer Tools tabs:**
- **Console** — run JavaScript, read errors
- **Network** — see all HTTP requests and responses
- **Storage/Application** — view and edit cookies, localStorage
- **Sources** — read JavaScript files loaded by the page
- **Inspector** — view and edit the page HTML

**Manipulate a cookie in the console:**
```javascript
document.cookie = 'cookiename=newvalue'
```

**View all cookies:**
```javascript
document.cookie
```

**Common web vulnerabilities covered:**
- Cookie manipulation — trusting client-side values for authorization
- SQL Injection — injecting SQL code through user input fields
- Insecure Direct Object Reference — accessing resources by guessing IDs
- JavaScript source review — finding hidden endpoints and logic in client-side code
- Authentication bypass — circumventing login mechanisms

---

*Written by: Mo | Last updated: March 2026*
