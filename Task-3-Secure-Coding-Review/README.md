# Secure Coding Review

A practical secure-coding project demonstrating the identification and remediation of a SQL Injection vulnerability.

## Objectives

- Identify insecure coding patterns
- Understand SQL Injection
- Demonstrate secure remediation
- Compare vulnerable and secure implementations
- Document secure coding practices

## Files

- `vulnerable_code.py` — intentionally vulnerable example
- `secure_code.py` — remediated implementation
- `SECURITY_REVIEW.md` — vulnerability analysis and remediation
- `screenshots/` — project evidence

## Vulnerability

**SQL Injection**

The vulnerable version directly concatenates user input into a SQL query.

## Remediation

The secure version uses a **parameterized SQL query**, preventing user input from being interpreted as part of the SQL statement.

## Security Practices

- Parameterized queries
- Input validation
- Least privilege
- Secure error handling
- Dependency management

## Disclaimer

This project is created strictly for educational and authorized secure-coding practice.