# Scanning & Recon Hard - Metadata

> **Category:** Scanning & Recon
> **Difficulty:** Hard
> **NCL Section:** Gymnasium

---

## 🎯 Objective

A server is running at `metadata.services.cityinthe.cloud:1338`. Your job is to figure out what it is, enumerate its endpoints, and extract information about the cloud instance it's running on, including a hidden flag buried deep in the metadata tree.

> ⚠️ Your scope is limited to port 1338 on this host. Do not scan other ports.

---

## 🛠️ Tools Needed

- A web browser OR
- `curl` (pre-installed on Kali)
- Google (for looking up the AMI ID)
- [Ubuntu EC2 AMI Locator](https://cloud-images.ubuntu.com/locator/ec2/) - for Q4

---

## 📚 What Is This Service?

Start by just visiting the server in your browser:

```
http://metadata.services.cityinthe.cloud:1338/
```

It returns a single word:

```
latest
```

That's a clue. Append it to the URL:

```
http://metadata.services.cityinthe.cloud:1338/latest
```

You get back:

```
dynamic
meta-data
user-data
```

Google any of those three keywords together and you'll immediately find AWS documentation for the **EC2 Instance Metadata Service**. This is a built-in HTTP service that runs on every AWS virtual machine and exposes information about the instance to applications running on it.

> 💡 This is a real AWS feature. In the real world, misconfigured cloud applications have accidentally exposed this service to the internet, leaking sensitive credentials and configuration data. The famous 2019 Capital One breach exploited exactly this service.

The base URL for everything from here is:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/
```

You can use either your browser or `curl` for all requests:

```bash
curl http://metadata.services.cityinthe.cloud:1338/latest/meta-data/
```

---

## 📋 Step-by-Step Walkthrough

### Step 1 - Q1: Find the Availability Zone

Access the placement endpoint:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/placement/availability-zone
```

Or with curl:

```bash
curl http://metadata.services.cityinthe.cloud:1338/latest/meta-data/placement/availability-zone
```

The response is the availability zone name. Your answer is the full zone identifier.

> 💡 **What the answer looks like:** An AWS region code followed by a single letter. Format: `us-region-#letter`.

---

### Step 2 - Q2: Find the Security Credentials Role Name

Access the IAM credentials endpoint:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/iam/security-credentials
```

The response is the name of the IAM role attached to this instance. That's your answer.

> 💡 **What the answer looks like:** A hyphenated name that sounds like it belongs to a hacktivist group you may have encountered earlier in the NCL challenges.

---

### Step 3 - Q3: Find the Instance Type

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/instance-type
```

The response is the EC2 instance type. Submit it exactly as returned.

> 💡 **What the answer looks like:** A letter followed by a number, a letter, a dot, and a size descriptor. A very large instance type.

---

### Step 4 - Q4: Find the Operating System Name and Version

First get the AMI ID:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/ami-id
```

An AMI (Amazon Machine Image) is essentially the OS image used to launch the instance. Copy the AMI ID from the response.

Now look it up:

1. Go to [cloud-images.ubuntu.com/locator/ec2](https://cloud-images.ubuntu.com/locator/ec2/)
2. Search for the AMI ID you got
3. The result will show you the Ubuntu version associated with that image

OR simply Google the AMI ID directly. The first result will usually tell you exactly which Ubuntu version it corresponds to.

Your answer is the full OS name and version number including the LTS designation.

> 💡 **What the answer looks like:** `Ubuntu XX.XX LTS` where XX.XX is the version number.

---

### Step 5 - Q5: Find the Hidden Flag

This is the most involved step. You need to enumerate the network interface endpoints to find the flag.

First get the list of available endpoints at the base metadata path:

```bash
curl http://metadata.services.cityinthe.cloud:1338/latest/meta-data/
```

Navigate to the network interfaces endpoint:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/network/interfaces/macs/
```

This returns a MAC address. Copy it exactly including the trailing slash if present. Then enumerate further:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/network/interfaces/macs/[MAC_ADDRESS]/
```

You'll get a list of sub-endpoints. Work through them one by one. The flag is hiding at:

```
http://metadata.services.cityinthe.cloud:1338/latest/meta-data/network/interfaces/macs/[MAC_ADDRESS]/vpc-ipv4-cidr-blocks
```

Replace `[MAC_ADDRESS]` with the actual MAC address returned in the previous step.

> 💡 Using curl makes this much faster than clicking through the browser. First get your MAC address:
> ```bash
> curl http://metadata.services.cityinthe.cloud:1338/latest/meta-data/network/interfaces/macs/
> ```
> Then plug it into the final command:
> ```bash
> curl http://metadata.services.cityinthe.cloud:1338/latest/meta-data/network/interfaces/macs/[YOUR_MAC_ADDRESS]/vpc-ipv4-cidr-blocks
> ```
> For example, if your MAC address is `0e:49:61:0f:c3:11` the command would look like:
> ```bash
> curl http://metadata.services.cityinthe.cloud:1338/latest/meta-data/network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv4-cidr-blocks
> ```

---

## 💡 Hints (Without Giving It Away)

- **Q1:** Navigate to `placement/availability-zone`. The answer is a standard AWS region and zone identifier on the US west coast.
- **Q2:** Navigate to `iam/security-credentials`. The role name will feel familiar if you've done other NCL challenges.
- **Q3:** Navigate to `instance-type`. It's one of the larger compute-optimized instance types AWS offers.
- **Q4:** Get the AMI ID from `ami-id` then Google it. It's an Ubuntu LTS release from the mid-2010s.
- **Q5:** The path is `network/interfaces/macs/[YOUR_MAC]/vpc-ipv4-cidr-blocks`. Get your MAC address from the macs endpoint first, then append it to the path.

---

## ⚠️ Accuracy Tips

- ❌ **Don't scan other ports.** Your scope is limited to port 1338 only.
- ❌ **Don't forget to include the MAC address** in the Q5 path. The endpoint won't work without it.
- ✅ **Copy the MAC address exactly** as it appears in the response, including colons.
- ✅ **Use curl for efficiency.** Clicking through the browser works but curl lets you copy and paste paths much faster.
- ✅ **For Q4**, the AMI lookup on Google is faster than the Ubuntu locator. Just search the AMI ID directly.

---

## 🧠 Why This Works

The AWS Instance Metadata Service (IMDS) is one of the most abused services in cloud security. It's designed to be accessible only from within the EC2 instance itself, but misconfigured applications (especially those with Server Side Request Forgery vulnerabilities) have repeatedly allowed attackers to reach it from the outside. The 2019 Capital One breach exposed over 100 million customer records using exactly this technique. AWS has since released IMDSv2 which requires a token-based authentication flow to mitigate SSRF attacks. This challenge demonstrates why cloud security isn't just about firewalls and passwords but about understanding the metadata and configuration services that underpin your infrastructure.

---

## 🔗 Resources

- [AWS Instance Metadata Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-categories.html)
- [Ubuntu EC2 AMI Locator](https://cloud-images.ubuntu.com/locator/ec2/)
- [Capital One Breach - IMDS Exploitation](https://krebsonsecurity.com/2019/07/capital-one-data-theft-impacts-106m-people/)
- [AWS IMDSv2 Security](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)

---

*Written by: Mo | Last updated: February 2026*
