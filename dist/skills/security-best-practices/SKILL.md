---
name: Security Best Practices
description: Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go).
source: openai-skills (MIT license, https://github.com/openai/skills)
category: software-development
tags: [software-development, security, best-practices, review, secure-coding, vulnerability]
type: Playbook
---

# Security Best Practices

## Overview

This skill provides a description of how to identify the language and frameworks used by the current context, and then to load information from this skill's references directory about the security best practices for this language and or frameworks.

This information can be used to write new secure by default code, or to passively detect major issues within existing code, or (if requested by the user) provide a vulnerability report and suggest fixes.

## When to Use

- The user explicitly requests security best practices guidance
- The user wants a security review or report
- The user wants secure-by-default coding help
- You're writing code that handles authentication, authorization, or sensitive data
- You're reviewing code for security issues

**Supported languages:** Python, JavaScript/TypeScript, Go

## Workflow

### 1. Identify Languages and Frameworks

Identify ALL languages and ALL frameworks which you are being asked to use or already exist in the scope of the project. Focus on the primary core frameworks. Often you will need to identify both frontend and backend languages and frameworks.

### 2. Load Security Reference Documentation

Check the references directory for relevant security documentation. The format of the filenames is `<language>-<framework>-<stack>-security.md`. Also check for `<language>-general-<stack>-security.md` which is agnostic to the framework.

If working on a web application which includes a frontend and a backend, make sure you have checked for reference documents for BOTH the frontend and backend.

### 3. Apply Security Knowledge

From there it can operate in a few ways:

1. **Primary mode:** Use the information to write secure by default code from this point forward. This is useful for starting a new project or when writing new code.

2. **Secondary mode:** Passively detect vulnerabilities while working in the project and writing code. Critical or very important vulnerabilities or major issues going against security guidance can be flagged and the user told about them. This passive mode should focus on the largest impact vulnerabilities and secure defaults.

3. **Review mode:** If the user explicitly requests a security review, systematically check the codebase against the loaded security best practices and produce a report.

## Key Security Areas

### Authentication & Authorization
- Use established auth libraries (don't roll your own)
- Implement proper session management
- Use secure password hashing (bcrypt, argon2)
- Implement proper RBAC/ABAC
- Validate tokens on every request

### Input Validation
- Validate all user input on the server side
- Use parameterized queries (prevent SQL injection)
- Sanitize output (prevent XSS)
- Validate file uploads (type, size, content)
- Use allowlists, not denylists

### Data Protection
- Encrypt sensitive data at rest and in transit
- Never log secrets, tokens, or PII
- Use environment variables for secrets (never hardcode)
- Implement proper key management
- Follow the principle of least privilege

### Infrastructure
- Keep dependencies updated
- Use security headers (CSP, HSTS, X-Frame-Options)
- Implement rate limiting
- Use HTTPS everywhere
- Configure CORS properly

## Red Flags

- Hardcoded secrets or credentials
- SQL queries built with string concatenation
- User input rendered without sanitization
- Missing authentication on API endpoints
- Overly permissive CORS configuration
- Outdated dependencies with known vulnerabilities
- Missing rate limiting on auth endpoints
- Logging of sensitive data
