# Password Cracking Medium - Windows (NTLM)

> **Category:** Password Cracking
> **Difficulty:** Medium
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given 10 Windows NTLM password hashes and asked to crack them. This challenge introduces a completely different tool from the previous ones: **ophcrack**, which uses precomputed rainbow tables to crack NTLM hashes fast.

> 💡 This one has more setup than previous challenges. If you get stuck at any point, follow along with the official NCL YouTube walkthrough: [NCL Summer Live - Cracking Password Hashes](https://www.youtube.com/watch?v=ll0xcqWF_AM&t=3384s). It covers this exact challenge step by step.

---

## 🛠️ Tools Needed

- **[ophcrack](https://ophcrack.sourceforge.io/download.php)** - works on both Windows and Linux
- **XP Special rainbow table** from [ophcrack tables page](https://ophcrack.sourceforge.io/tables.php)
- A folder to store the table files

> 💡 The **XP Special** table is the one you want. It includes everything in the XP Free Fast and XP Free tables, plus support for special characters. Since several passwords here contain symbols, the other tables won't crack all of them. Download XP Special and save yourself the headache.

---

## 📋 The Hashes

```
21259DD63B980471AAD3B435B51404EE:1E43E37B818AB5EDB066EB58CCDC1823
11CB3F697332AE4C4A3B108F3FA6CB6D:13B29964CC2480B4EF454C59562E675C
65711C079DC4CD3CC2265B23734E0DAC:47F747C5190DC0F0B921AA4A07F06285
FBBDA33FC12E83FB0C240E84A183686E:DDE9DC6E34E2E6E11EF9E51C6B27ED96
21C4E7C2EFE8E8D1C00B70065ED76AA7:A7A0F9AFD4A78F531A1CF4C42E531BBF
E85B4B634711A266AAD3B435B51404EE:FD134459FE4D3A6DB4034C4E52403F16
BA756FB317B622DBAAD3B435B51404EE:C8405270B10B13AE8A24612BB853567A
199C926FA387EAB7AAD3B435B51404EE:F196F77BF8BB15781BA8364C649C5FD4
FE4AACAAAD7D986AAAD3B435B51404EE:3928E16F614E2316CA51C336FA5B3011
3613F7EC15407F56AAD3B435B51404EE:C82E164316183AA3AF3EA6BAA642A237
```

> ⚠️ Each hash is in the format `LM:NT`. The left side is the LM hash, the right side is the NT hash. ophcrack handles both automatically. **Always submit the password from the NT Pwd column** in ophcrack, not the LM column, as NT preserves the correct lowercase characters.

> 🚫 **Do NOT guess passwords.** Several of these are special character passwords that look random. A wrong submission hurts your accuracy score more than skipping it. Only submit what ophcrack gives you.

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Download ophcrack

Go to [ophcrack.sourceforge.io/download.php](https://ophcrack.sourceforge.io/download.php) and download the version for your OS.

> ⚠️ If you're on Windows, your antivirus may flag ophcrack because it functions similarly to credential-dumping malware. This is a false positive. You may need to whitelist it or temporarily disable your AV to install it. On Kali this is not an issue.

Before installing, verify your download matches the MD5 checksum listed on the site. This confirms the file wasn't tampered with:

```bash
md5sum ophcrack-file-you-downloaded
```

---

### Step 2 - Download the XP Special Table

Go to [ophcrack.sourceforge.io/tables.php](https://ophcrack.sourceforge.io/tables.php) and download the **XP Special** table.

It will come as multiple files. Download ALL of them and save them together in a single folder named something like `xp_special`. Do not mix files from different tables in the same folder.

Check the downloaded files against the `md5sum.txt` included in the download to make sure everything is intact:

```bash
md5sum -c md5sum.txt
```

---

### Step 3 - Load the Table into ophcrack

1. Open ophcrack
2. Click **Tables** in the top menu
3. Find **XP Special** in the list
4. Click **Install** and navigate to the folder where you saved the table files
5. When done correctly, the red indicator next to the table name will turn **green**

If it stays red, ophcrack can't find the files. Double check you're pointing to the right folder and that all files are present.

---

### Step 4 - Load the Hashes

Save the hashes to a file called `hashes.txt`, one per line exactly as shown above.

In ophcrack:
1. Click **Load**
2. Select **PWDUMP file**
3. Navigate to your `hashes.txt` file

All 10 hashes will load into the table.

> 💡 You can also use **Load > Single Hash** to add them one at a time if you prefer.

---

### Step 5 - Crack

Click **Crack** and let ophcrack run. With the XP Special table, it should crack most or all of the hashes within a few minutes depending on your machine.

---

### Step 6 - Read the Results

When cracking finishes, look at the **NT Pwd** column for each hash. This is your answer for each question. The LM Pwd column may show uppercase only, but NT Pwd preserves the correct mixed case and special characters.

Match each cracked password back to the correct hash before submitting.

---

## 💡 Hints (Without Giving It Away)

Some of these are real word passwords with character substitutions, others are completely random-looking special character strings. Don't try to guess either type:

- `21259DD6...` - Looks like an animal name where letters have been swapped for numbers. Think fox, but cooler.
- `11CB3F69...` - A classic "I'm being clever with my password" substitution. You've definitely seen this format before.
- `65711C07...` - A sport followed by a number substitution. The number replaces a letter that looks similar.
- `FBBDA33F...` - Starts with a number, then a phrase meaning "trust no one." A classic paranoid password.
- `21C4E7C2...` - A sci-fi/gaming reference followed by numbers. Ghostly vibes.
- `E85B4B63...` - A short random-looking string with special characters. Don't guess this one, just let ophcrack find it.
- `BA756FB3...` - Another short special character string. Same advice, let the tool do the work.
- `199C926F...` - Special characters and numbers mixed. ophcrack handles it.
- `FE4AACAA...` - Starts with a dollar sign. ophcrack handles it.
- `3613F7EC...` - Starts with a caret symbol. ophcrack handles it.

---

## ⚠️ Accuracy Tips

- ❌ **Never guess.** The special character passwords look random and guessing them is essentially impossible. If ophcrack doesn't crack it, skip it rather than guess.
- ❌ **Don't use the LM Pwd column.** LM hashes are case-insensitive and uppercase only. NT Pwd is what you want.
- ❌ **Don't download only part of the table.** If any table files are missing, ophcrack won't load it correctly and the red indicator will stay red.
- ✅ **Use the XP Special table.** The other tables won't crack the special character passwords.
- ✅ **Verify your download checksums.** Corrupt table files will cause cracking failures that are hard to diagnose.

---

## 🧠 Why This Works

NTLM is the password hashing algorithm used by Windows for local account authentication. Rainbow tables are precomputed databases of hash-to-password mappings, essentially a giant lookup table that trades storage space for cracking speed. ophcrack uses these tables to crack NTLM hashes in seconds without having to brute-force anything. This is why modern systems use salted hashes, salt values make rainbow tables useless since the same password hashed with different salts produces completely different results. NTLM has no salting, which is one of several reasons it's considered a weak hashing algorithm by modern standards.

---

## 🔗 Resources

- [ophcrack Download](https://ophcrack.sourceforge.io/download.php)
- [ophcrack Tables](https://ophcrack.sourceforge.io/tables.php)
- [NCL Tutorial Video - Cracking Password Hashes](https://www.youtube.com/watch?v=ll0xcqWF_AM&t=3384s)
- [NTLM - Wikipedia](https://en.wikipedia.org/wiki/NT_LAN_Manager)

---

*Written by: Mo | Last updated: February 2026*
