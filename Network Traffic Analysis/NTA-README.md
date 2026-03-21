# 🌐 Network Traffic Analysis Walkthroughs

Capturing, filtering, and dissecting network packets to understand what's happening on a network.

---

## A Word Before You Start

Network Traffic Analysis is one of the most visual and satisfying categories in NCL. You're working with real packet captures (PCAPs) in Wireshark, watching actual conversations between computers happen right in front of you. If you've never used Wireshark before, don't worry. The walkthroughs walk you through every filter and every click.

The key skill here is learning to read packet captures like a story. Every packet has a source, a destination, a protocol, and a payload. Once you can follow that story, you can answer almost any question about what happened on a network.

> 💡 A note for the real world: capturing network traffic you don't own or have permission to capture is illegal. Everything in NCL uses provided PCAP files from controlled environments.

---

## Challenges

### 🟢 Easy
| File | Topic |
|---|---|
| [dns.md](easy/dns.md) | DNS query and response analysis |
| [ftp.md](easy/ftp.md) | FTP traffic analysis |
| [http.md](easy/http.md) | HTTP traffic analysis |
| [telnet.md](easy/telnet.md) | Telnet traffic analysis |

### 🟡 Medium
| File | Topic |
|---|---|
| [packet-dissection.md](medium/packet-dissection.md) | Deep packet inspection and dissection |
| [decrypt.md](medium/decrypt.md) | Decrypting captured traffic |

### 🔴 Hard
| File | Topic |
|---|---|
| [pandora.md](hard/pandora.md) | Advanced traffic analysis |
| [can-bus.md](hard/can-bus.md) | CAN Bus automotive network analysis |

---

## Wireshark Quick Reference

**Open a PCAP:**
```bash
wireshark filename.pcap
```

**Common display filters:**
```
dns           # DNS traffic only
ftp           # FTP traffic only
http          # HTTP traffic only
telnet        # Telnet traffic only
tcp           # All TCP traffic
udp           # All UDP traffic
ip.addr == 1.2.3.4    # Traffic to/from a specific IP
tcp.port == 80        # Traffic on a specific port
```

**Follow a TCP stream:**
Right-click any packet → Follow → TCP Stream

**Export objects from HTTP traffic:**
File → Export Objects → HTTP

**Common packet sections:**
- **Frame** — physical layer info, packet size
- **Ethernet** — MAC addresses
- **IP** — source and destination IP addresses, packet TTL
- **TCP/UDP** — ports, flags, sequence numbers
- **Application layer** — DNS, HTTP, FTP, Telnet payload

---

*Written by: Mo | Last updated: March 2026*
