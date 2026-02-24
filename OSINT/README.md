# 🔍 OSINT Walkthroughs

Open Source Intelligence — finding information using publicly available sources.

---

## What to Expect in NCL OSINT

NCL OSINT challenges test your ability to gather information from public sources: social media, websites, DNS records, image metadata, geolocation, and more. The key skill is knowing *where* to look and *how* to pivot from one piece of info to the next.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [meta.md](easy/meta.md) | Extracting metadata from an image using EXIF tools |
| [lookup.md](easy/lookup.md) | Researching DNS record types using IETF RFCs |
| [threatintel.md](easy/threatintel.md) | Researching well-known CVEs and security incidents |
| [http-headers.md](easy/http-headers.md) | Identifying HTTP request headers and their purposes |
| [whois.md](easy/whois.md) | Performing a WHOIS lookup on a domain name |
| [pgplookup.md](easy/pgplookup.md) | Querying public PGP key databases |

### 🟡 Medium
| File | Topic |
|---|---|
| [ssl.md](medium/ssl.md) | Inspecting SSL certificate chains in the browser |
| [barcode.md](medium/barcode.md) | Decoding a barcode to extract a hidden flag |

> ⚠️ There are no Hard OSINT challenges in the NCL Gymnasium.

---

## OSINT Quick Reference

**Google Dork operators:**
```
site:example.com          # Limit to one site
filetype:pdf              # Find specific file types
intitle:"index of"        # Find open directories
inurl:admin               # Find admin pages
"exact phrase"            # Search exact phrase
```

**Image metadata check:**
```bash
exiftool image.jpg        # View all metadata
```

**DNS recon:**
```bash
whois domain.com
nslookup domain.com
dig domain.com ANY
```

---

*Written by: Mo | Last updated: February 2026*
