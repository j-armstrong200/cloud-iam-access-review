import csv

with open("users.csv", newline="") as file:
    reader = csv.DictReader(file)

    for user in reader:
        if user["role"] == "Administrator" and user["mfa_enabled"] == "No":
            print("WARNING:", user["username"], "is an Administrator without MFA!")
