import csv

findings = []

with open("users.csv", newline="") as file:
    reader = csv.DictReader(file)

    for user in reader:

        # Check for privileged Administrator accounts without MFA
        if user["role"] == "Administrator" and user["mfa_enabled"] == "No":
            print("WARNING:", user["username"], "is an Administrator without MFA!")
            findings.append({
                "username": user["username"],
                "severity": "High",
                "finding": "Administrator without MFA"
            })

        # Check for active accounts that have been dormant for over 90 days
        if int(user["last_login_days"]) > 90 and user["account_status"] == "Active":
            print("WARNING:", user["username"], "has an active account but has not logged in for over 90 days!")
            findings.append({
                "username": user["username"],
                "severity": "Medium",
                "finding": "Active account dormant for over 90 days"
            })

        # Check regular human users for missing MFA
        if user["mfa_enabled"] == "No" and user["account_status"] == "Active" and user["role"] not in ["Administrator", "Service Account"]:
            print("REVIEW:", user["username"], "has an active account without MFA.")
            findings.append({
                "username": user["username"],
                "severity": "Medium",
                "finding": "Active user account without MFA"
            })

# Create a CSV report containing the security findings
with open("security_findings.csv", "w", newline="") as report_file:
    fieldnames = ["username", "severity", "finding"]
    writer = csv.DictWriter(report_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(findings)