# Scanning & Recon Easy - Git

> **Category:** Scanning & Recon
> **Difficulty:** Easy
> **NCL Section:** Gymnasium

---

## 🎯 Objective

Analyze a Git repository to find 5 hidden flags scattered across commits, branches, and files. This challenge builds directly on the Version Control challenge from Forensics, but this time you're working with a live GitLab repository.

> 💡 We highly recommend doing this one through the **web browser** rather than the command line. The GitLab web interface makes it much easier to navigate branches, view commit history, and read files without needing to clone anything.

---

## 🛠️ Tools Needed

- A web browser
- OR Kali Linux terminal with `git` (pre-installed) if you prefer CLI

---

## 🔗 Repository

**Web URL (recommended):**
```
https://gitlab.com/cybergit4823/my-awesome-flag-project
```

**Clone URL (CLI):**
```bash
git clone git@gitlab.com:cybergit4823/my-awesome-flag-project.git
```

> ⚠️ Cloning via SSH may not work depending on your setup. If it fails, just use the web URL above. The browser interface gives you everything you need.

---

## 📚 Key Git Concepts

Before diving in, here's a quick refresher:

- **Commit:** A saved snapshot of changes. Every commit has a unique hash (like `f9714edd`).
- **Branch:** A separate line of development. Repos often have a `main`/`master` branch plus others.
- **Commit message:** A note the author wrote describing what changed in that commit.
- **Diff:** The actual changes made in a commit, shown as additions (+) and deletions (-).

---

## 📋 Step-by-Step Walkthrough

### Q1: Author Display Name

**Web:** Go to the repository and click **History**. Look at the Author column on any commit.

**CLI:**
```bash
git log
```
Look at the `Author:` field on any commit entry.

> 💡 **What the answer looks like:** Two words, both the same word repeated.

---

### Q2: Short Commit Hash of the Initial Commit

The initial commit is the very first one ever made, at the bottom of the commit history.

**Web:** Click **History** and scroll all the way to the bottom. The short hash is the 8-character code shown on the right side of the oldest commit.

**CLI:**
```bash
git log
```
Press `Shift+G` to jump to the end, or keep pressing Space to page down. The very last commit listed is the initial commit. Copy the first 8 characters of its hash.

> 💡 **What the answer looks like:** 8 hexadecimal characters. Submit in uppercase.

---

### Q3: Flag 1

Flag 1 is in the README.md file on the default branch.

**Web:** It's displayed automatically on the repository home page. Scroll down to see the README contents.

**CLI:**
```bash
cat README.md
```

---

### Q4: Flag 2

Flag 2 is on a separate branch called `flag2`.

**Web:** Click **Branches** (or look for "2 branches" in the sidebar). Click on the `flag2` branch. You'll see a new file called `flag2.txt`. Click it to read the contents.

**CLI:**
```bash
git branch
git checkout flag2
cat flag2.txt
git checkout master
```

---

### Q5: Flag 3

Flag 3 is in a file called `flag3.txt` on the main branch.

**Web:** It's visible in the file list on the main branch. Click `flag3.txt` to open it.

**CLI:**
```bash
cat flag3.txt
```

---

### Q6: Flag 4

Flag 4 was added in a commit and then removed in a later commit. It only exists in the commit history, not in the current files.

**Web:** Click **History** and find the commit with the message "Added flag4". Click on that commit to see the diff. Lines starting with `+` were added. The flag is there.

**CLI:**
```bash
git log
```
Find the commit hash for "Added flag4", then:
```bash
git show [commit_hash]
```
Look for the line starting with `+` that contains the flag.

---

### Q7: Flag 5

Flag 5 is hidden inside a commit message itself, not in any file.

**Web:** Click **History** and look through the commit messages. One of them is truncated. Click the **three dots (...)** icon next to it to expand the full message. The flag is in there.

**CLI:**
```bash
git log
```
Scroll through all the commit messages carefully. One of them contains the flag directly in the message text.

> 💡 **What the answer looks like:** All flags follow the standard `SKY-ABCD-1234` format.

---

## 💡 Hints (Without Giving It Away)

- **Q1:** The author's display name is two words. Both words are the same.
- **Q2:** Scroll all the way to the bottom of the commit history. The initial commit is the oldest one.
- **Q3:** It's right on the front page of the repo. Hard to miss.
- **Q4:** Check every branch. The flag is in a text file on a branch named after the flag number.
- **Q5:** Same as Q4 but on the default branch. Just open the file.
- **Q6:** The flag was added and then deleted. Check the diff of the commit that added it.
- **Q7:** One commit message is hiding something. Expand the truncated ones and read carefully.

---

## ⚠️ Accuracy Tips

- ❌ **Don't submit the full commit hash for Q2.** Only the first 8 characters. Submit in uppercase.
- ❌ **Don't look for flag 4 in the current files.** It was deleted. You can only find it in the commit diff.
- ✅ **Use the web interface.** Navigating branches and commit history is much easier in the browser than the CLI for this challenge.
- ✅ **All flags are in `SKY-XXXX-DDDD` format.** If what you found doesn't match that format, keep looking.

---

## 🧠 Why This Works

This challenge mirrors a very common real-world attack scenario: developers accidentally commit sensitive data (API keys, passwords, flags) and then try to delete them in a later commit. But in Git, nothing is ever truly gone. The full history is preserved forever. This is why major platforms like GitHub offer secret scanning tools that automatically detect when credentials are committed, and why the correct response to an accidental commit is to immediately rotate the credentials rather than just deleting the file. The delete commit doesn't protect you. Anyone with access to the repo history can still read the original commit.

---

## 🔗 Resources

- [GitLab Repository](https://gitlab.com/cybergit4823/my-awesome-flag-project)
- [Git Documentation](https://git-scm.com/doc)
- [GitLab Web Interface Guide](https://docs.gitlab.com/ee/user/project/repository/)

---

*Written by: Mo | Last updated: February 2026*
