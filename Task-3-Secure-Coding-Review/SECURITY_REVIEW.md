# Secure Coding Review

## 1. Vulnerability Identified

The original code contains a **SQL Injection** vulnerability.

### Vulnerable Pattern

User-controlled input is directly concatenated into a SQL query:

`"SELECT * FROM users WHERE username = '" + username + "'"`

This can allow an attacker to manipulate the SQL statement.

## 2. Security Impact

SQL Injection may allow an attacker to:

- Bypass application logic
- Access unauthorized database records
- Modify or delete database information
- Potentially compromise sensitive data

## 3. Remediation

The vulnerable query was replaced with a parameterized SQL query using a placeholder:

`SELECT * FROM users WHERE username = ?`

The user input is supplied separately as a parameter.

## 4. Secure Coding Practices

- Use parameterized queries.
- Validate and sanitize user input where appropriate.
- Apply least-privilege database permissions.
- Avoid exposing sensitive error messages.
- Keep dependencies updated.
- Never trust user-controlled input.

## 5. Before vs After

| Area | Vulnerable Code | Secure Code |
|---|---|---|
| SQL Query | String concatenation | Parameterized query |
| User Input | Directly inserted | Passed as parameter |
| SQL Injection Risk | High | Significantly reduced |
| Security Practice | Unsafe | Recommended |

## Conclusion

The code review identified a SQL Injection vulnerability and demonstrated how parameterized queries can be used to reduce the risk.

The example is intentionally created for authorized cybersecurity education and secure coding practice.