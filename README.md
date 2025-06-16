# Project:

# 🔐 SecuAudit - Linux Hardening Audit Tool

A beginner-friendly Python script that audits a Linux system's security posture using basic hardening checks and CIS-inspired benchmarks. Ideal for learning, internships, and improving personal Linux setups.

---

## 🧠 What It Does

SecuAudit performs an automated security audit on a Linux machine by:

-  Checking UFW (firewall) status
-  Listing enabled/active services
-  Auditing SSH config (`PermitRootLogin`, `PasswordAuthentication`)
-  Validating sensitive file permissions (`/etc/shadow`, `/etc/passwd`)
-  Detecting rootkits using `chkrootkit`
-  Scoring the system’s security (CIS-style)
-  Giving actionable hardening recommendations

---

## ⚙️ How to Use

### 🔧 Requirements

- Linux system (Debian/Ubuntu recommended)
- Python 3.x
- `chkrootkit` installed (run `sudo apt install chkrootkit` if needed)
- UFW (Uncomplicated Firewall)

### 🚀 Run the Script
```bash
git clone https://github.com/Charanx03/SecuAudit.git
cd SecuAudit
python3 SecuAudit.py
```
