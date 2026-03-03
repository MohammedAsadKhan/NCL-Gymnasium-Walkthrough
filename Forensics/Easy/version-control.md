# Forensics Easy - Version Control

> **Category:** Forensics
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

You're given a zip file that appears to contain only a simple README. But looks can be deceiving. Using Git version control commands, you'll dig through the repository's history to find compromised credentials and a hidden flag.

> 💡 This one is a great introduction to Forensics because it's all command line with no special tools needed. If you've never used Git before, don't worry, everything you need is explained step by step below.

---

## 🛠️ Tools Needed

- Kali Linux terminal
- `git` (pre-installed on Kali)
- `unzip` (pre-installed on Kali)
- The `git_backup.zip` file downloaded from the challenge

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Download and Unzip the File

Download `git_backup.zip` from the challenge prompt and save it to your working directory. Then unzip it:

```bash
unzip git_backup.zip
cd git_backup
```

---

### Step 2 - Look Closer at the Directory

At first glance the folder only has a README.md with nothing interesting in it. But run `ls` with the `-a` flag to show hidden files and directories:

```bash
ls -a
```

You'll see a `.git` folder. That dot at the front means it's hidden from normal `ls` output. The `.git` folder is what makes this a Git repository and it contains the entire history of every change ever made to this project.

> 💡 In Git, nothing is ever truly deleted. Every change, addition, and removal is stored in the repository history. This is exactly what makes it useful for forensics.

---

### Step 3 - Q1: Find the Employee's Email Address

Check the Git log to see all commits and who made them:

```bash
git log
```

You'll see a list of commits, each showing the author's name and email address. The answer to Q1 is right there.

Your answer will be an email address at an unusual domain. If you did the WHOIS challenge back in OSINT, the domain will look familiar.

---

### Step 4 - Q2: Find the Compromised Flag

Now inspect each commit individually to see what changes were made. Use the commit hash from the git log output:

```bash
git show <commit_hash>
```

Replace `<commit_hash>` with the actual hash shown in `git log`. Run this for each commit and look at the diff output. Lines starting with `+` were added in that commit, lines starting with `-` were removed.

You'll find the flag was added in one commit and then removed in a later commit. That's a classic "oops I accidentally committed sensitive data" scenario.

Your answer is a flag in `SKY-ABCD-1234` format.

> 💡 Don't worry if the flag appears to be deleted in the latest commit. Git keeps the full history so even deleted data is still recoverable by looking at past commits.

---

### Step 5 - Check for Other Branches

After looking through all commits on the current branch, check if any other branches exist:

```bash
git branch
```

You'll see you're on the `master` branch and there's at least one other branch available. Switch to it:

```bash
git checkout next
```

---

### Step 6 - Q3 and Q4: Find the Compromised Credentials

Once on the new branch, list the files:

```bash
ls -a
```

You'll find a file that wasn't visible on the master branch. Open it:

```bash
cat passwords.txt
```

This file contains the answers to Q3 and Q4. Q3 asks for the service provider name and Q4 asks for the password on that account.

> ⚠️ Make sure you're reading the right fields. The file will have a service name and a password listed separately. Submit each to the correct question.

---

## 💡 Hints (Without Giving It Away)

- **Q1 (email address):** The employee's first initial and last name combined, at a domain that belongs to a police department on a fictional hacker network. If you did the WHOIS challenge in OSINT, you've seen this domain before.
- **Q2 (compromised flag):** Look through the commit that has a message about backing up data. The flag was added there and removed in a follow-up commit. It follows the standard `SKY-ABCD-1234` format.
- **Q3 (service provider):** Check the `passwords.txt` file on the `next` branch. The service is one of the most visited websites on the planet. Everyone has an account there.
- **Q4 (password):** It's in the same file as Q3. A simple lowercase word followed by two digits. The kind of password you'd expect someone named Greg to use.

---

## ⚠️ Accuracy Tips

- ❌ **Don't stop after checking one branch.** The most interesting data is on a different branch. Always run `git branch` to see what else exists.
- ❌ **Don't skip any commits.** The flag exists in a commit that was later deleted. You have to check each one with `git show`.
- ✅ **Copy the email address exactly** including the full domain. It's longer than a typical email address.
- ✅ **Lines with `+` in `git show` output** are additions. That's what was added in that commit.

---

## 🧠 Why This Works

This challenge demonstrates one of the most common real-world security mistakes: accidentally committing sensitive data to a Git repository and then trying to delete it. Many developers don't realize that deleting a file and committing the deletion doesn't remove the data from the repository history. Tools like `git log` and `git show` make historical data fully recoverable. This is why services like GitHub offer secret scanning to alert users when credentials are accidentally pushed, and why the correct response to an accidental credential commit is to immediately rotate the credentials, not just delete the file.

---

## 🔗 Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Learning Resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources)

---

*Written by: Mo | Last updated: February 2026*
