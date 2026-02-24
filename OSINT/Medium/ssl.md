# OSINT Medium - SSL

> **Category:** OSINT
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

This challenge has you inspecting the **SSL certificate chain** on the Cyber Skyline website and pulling specific details from it. SSL certificates are what make the little padlock appear in your browser. You've seen them a thousand times, now you're actually going to look inside one.

> 💡 No tools to install, no commands to run. This entire challenge is solved through your browser's built-in certificate viewer. We'll walk through exactly where to click.

---

## 🛠️ Tools Needed

- Google Chrome (recommended, the walkthrough uses Chrome)
- Any modern browser will work, the menus just look slightly different

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Open the Certificate Viewer

Go to **[cyberskyline.com](https://cyberskyline.com)** in Chrome.

Look at the address bar. To the left of the URL you'll see a small icon (a tune/settings icon or padlock depending on your Chrome version). Click it.

A dropdown appears. Click **"Connection is secure."**

Then click **"Certificate is valid."**

This opens the **Certificate Viewer**, a popup with two tabs: General and Details. This is where all your answers live.

---

### Step 2 - Q1: Who Issued the Certificate?

You're looking for the **issuer** of Cyber Skyline's SSL certificate. The issuer is the Certificate Authority (CA) that verified Cyber Skyline's identity and signed their certificate.

Stay on the **General tab** in the Certificate Viewer.

Look for the **"Issued By"** section. Your answer is the value next to **"Common Name"** under that section.

> 🏦 Think of a Certificate Authority like a notary public. They don't own the website, they just verified it's legit and stamped it. This question is asking who did the stamping.

Your answer will be a company name with some extra technical identifiers after it.

---

### Step 3 - Q2: How Many Bits is the SSL Key?

You're looking for the **bit length of the public key** used in this certificate. Bit length is a measure of how strong the encryption is.

Click over to the **Details tab** in the Certificate Viewer.

You'll see a tree structure under **"Certificate Fields."** Expand the following path:

`*.cyberskyline.com → Certificate → Subject Public Key Info → Subject's Public Key`

The bit length will be listed right there in the description of the public key.

> 💡 If you can't expand the tree by clicking, try clicking directly on the field label. Your answer will be a number followed by the word "bits." You just need the number.

Your answer is a common RSA key size you'll see everywhere in security.

---

### Step 4 - Q3: How Many Certificates Are in the Chain?

You're looking for the **total number of certificates in the certificate chain**. A certificate chain (also called a chain of trust) links the website's certificate back to a trusted root authority through one or more intermediate certificates.

Stay on the **Details tab** and look near the top for **"Certificate Hierarchy."**

Count how many certificates are listed there. Each one is a link in the chain.

> 🔗 Picture a chain of people vouching for each other. "I trust this website because this company vouches for it, and I trust that company because this root authority vouches for them." Each person in that chain is one certificate. How many people are vouching here?

Your answer is a single digit.

---

## ⚠️ Accuracy Tips

- ❌ **Don't mix up "Issued By" and "Issued To."** The General tab shows both. You want "Issued By" for Q1, that's the CA, not the website owner.
- ❌ **Don't just count intermediate certificates for Q3.** Count all of them including the end certificate and the root. The hierarchy shows the full chain.
- ✅ **Use Chrome if possible.** Other browsers show the same info but the menu path is slightly different. Firefox calls it "More Information → Security → View Certificate."
- ✅ **The Details tab tree is clickable.** If you don't see sub-fields at first, click the arrows or field names to expand them.

---

## 🧠 Why This Works

SSL certificates are everywhere and being able to inspect them is a fundamental security skill. In real-world scenarios, you'd check certificates to verify a site's legitimacy, investigate phishing domains using fake certificates, or audit an organization's certificate setup during a security assessment. Certificate chains are also a common source of misconfiguration issues in the wild, so understanding how they work (and how to read them) matters beyond just this challenge.

---

## 🔗 Resources

- [What is an SSL Certificate? - Cloudflare](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)
- [Certificate Chain of Trust - Wikipedia](https://en.wikipedia.org/wiki/Chain_of_trust)
- [How to View SSL Certificates in Chrome - SSL Shopper](https://www.sslshopper.com/article-how-to-view-ssl-certificate-details-in-chrome.html)

---

*Written by: Mo | Last updated: February 2026*
