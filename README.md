# Cloud IAM Access Review

## Overview

This project simulates an Identity and Access Management (IAM) access review using Python. The script analyzes sample user account data and identifies potential security concerns that may require review.

The goal of the project is to demonstrate basic IAM security concepts, including multi-factor authentication (MFA), privileged access, dormant accounts, and service account handling.

## Security Checks

The Python script checks for:

- Administrators who do not have MFA enabled
- Active user accounts that have not logged in for more than 90 days
- Active human user accounts that do not have MFA enabled
- Service accounts that should be handled differently from standard user accounts

## Technologies and Concepts

- Python
- Identity and Access Management (IAM)
- Multi-Factor Authentication (MFA)
- Privileged Access
- Least Privilege
- Access Reviews
- Security Auditing
- CSV Data Analysis

## Sample Findings

The script identifies findings such as:

```text
REVIEW: bwilliams has an active account without MFA.
WARNING: tlee is an Administrator without MFA!
REVIEW: tlee has an active account without MFA.
WARNING: rjohnson has an active account but has not logged in for over 90 days!
```

## Files
- access_review.py - Python script that performs the security checks
- users.csv - Sample IAM user account data
- README.md - Project documentation

## What I Learned
This project helped me practice using Python to automate a basic security review. I learned how to read CSV data, evaluate user account attributes, identify potentially risky access conditions, and apply different security logic based on account type.
It also reinforced the importance of MFA, privileged account monitoring, dormant account reviews, and treating service accounts differently from standard user accounts.

## Disclaimer
This project uses fictional sample data and is intended for educational and portfolio purposes only.
