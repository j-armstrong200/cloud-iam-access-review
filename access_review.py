import csv

with open("users.csv", newline="") as file:
    reader = csv.DictReader(file)

    for user in reader:
        if user["role"] == "Administrator" and user["mfa_enabled"] == "No":
            print("WARNING:", user["username"], "is an Administrator without MFA!")

        if int(user["last_login_days"]) > 90 and user["account_status"] == "Active":
            print("WARNING:", user["username"], "has an active account but has not logged in for over 90 days!")

        if user["mfa_enabled"] == "No" and user["account_status"] == "Active" and user["role"] != "Service Account":
            print("REVIEW:", user["username"], "has an active account without MFA.")   