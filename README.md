# Attack & Defense Cybersecurity Lab

A practical cybersecurity lab demonstrating vulnerability discovery,
security testing, remediation, and defensive security monitoring
using a deliberately vulnerable Flask web application.

## Project Overview

This project simulates a real-world attack-and-defense workflow
against a Python Flask web application.

The project was initially developed with intentionally vulnerable
components for authorized security testing. Each vulnerability was
then analyzed, remediated, and validated through subsequent changes.

## Security Testing & Vulnerabilities

The initial vulnerable baseline included:

- Reflected Cross-Site Scripting (XSS)
- SQL Injection
- OS Command Injection
- Weak File Upload Validation

## Security Remediation

The vulnerabilities were addressed through:

- Reflected XSS mitigation
- Parameterized SQL queries
- Command allowlisting and `shell=False`
- Secure filename handling and file extension validation

## Security Evolution

The project follows a clear vulnerability remediation lifecycle:

1. Initial vulnerable baseline
2. Vulnerability identification
3. Security testing
4. Remediation
5. Validation and re-testing

## Technology Stack

- Python
- Flask
- SQLite
- HTML
- Linux
- Git
- Kali Linux

## Project Structure

```text
attack-defense-cybersecurity-lab/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── search.html
│   ├── command.html
│   └── upload.html
│
├── .gitignore
└── README.md
