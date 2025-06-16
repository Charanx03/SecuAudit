import subprocess
import os

# 🧾 Report Header
print(f"""
🔐 SecuAudit - Linux Hardening Audit Tool
👤 Author: Charan
""")

# Function to print section headers
def section(title):
    print(f"\n\033[1;34m🔹 {title}\033[0m")
    print("-" * 60)

# 1. Check firewall status (UFW)
section("Firewall Status (UFW)")
fw = subprocess.getoutput("sudo ufw status")
print(fw)

# 2. Check unused enabled services
section("Enabled System Services")
services = subprocess.getoutput("systemctl list-unit-files --type=service --state=enabled")
print(services)

# 3. Check SSH settings
section("SSH Configuration (/etc/ssh/sshd_config)")
try:
    with open("/etc/ssh/sshd_config", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "PermitRootLogin" in line or "PasswordAuthentication" in line:
                print(line.strip())
except Exception as e:
    print(f"❌ Could not read SSH config: {e}")

# 4. Check file permissions
section("File Permissions")
shadow_perm = subprocess.getoutput("ls -l /etc/shadow")
passwd_perm = subprocess.getoutput("ls -l /etc/passwd")
print(f"/etc/shadow: {shadow_perm}")
print(f"/etc/passwd: {passwd_perm}")

# 5. Rootkit check using chkrootkit
section("Rootkit Scan (chkrootkit)")
rootkits = subprocess.getoutput("sudo chkrootkit")
print(rootkits)

# 6. Security Score
section("CIS-style Compliance Score")
score = 0
total = 5

try:
    ssh_config = open("/etc/ssh/sshd_config").read()
    if "Status: active" in fw:
        score += 1
    if "PermitRootLogin no" in ssh_config:
        score += 1
    if "PasswordAuthentication no" in ssh_config:
        score += 1
    if "-rw-r-----" in shadow_perm:
        score += 1
    if "-rw-r--r--" in passwd_perm:
        score += 1
except Exception as e:
    print(f"❌ Error reading configuration: {e}")

color = "\033[92m" if score == total else "\033[93m"
print(f"{color}📊 Compliance Score: {score}/{total}\033[0m")

# 7. Hardening Recommendations
section("Hardening Recommendations")

if "inactive" in fw:
    print("🔧 UFW is inactive. Run: sudo ufw enable")
if "PermitRootLogin yes" in ssh_config:
    print("🔧 Disable root SSH login: set PermitRootLogin to no")
if "PasswordAuthentication yes" in ssh_config:
    print("🔧 Disable password-based SSH login: set PasswordAuthentication to no")

print("\n✅ \033[1;32mAudit Completed Successfully.\033[0m")
