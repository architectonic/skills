---
name: auth-implementation-patterns
description: Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC. Use when implementing auth systems, securing APIs, or debugging security issues. Covers JWT generation/verification, refresh token flows, session-based auth with Redis, OAuth2/social login with Passport.js, role-based access control (RBAC), permission-based access control, and resource ownership validation.
tags: [software-development, software-development, security, authentication, authorization, JWT, OAuth2, RBAC]
source: AgentSkillOS — data/skill_seeds/auth-implementation-patterns/SKILL.md (Apache-2.0 license)
type: Playbook
---

# Authentication & Authorization Implementation Patterns

Build secure, authentication and authorization systems using industry-standard patterns.

## When to Use

- Implementing user authentication systems
- Securing REST or GraphQL APIs
- Adding OAuth2/social login
- Implementing role-based access control (RBAC)
- Designing session management
- Migrating authentication systems
- Debugging auth issues
- Implementing SSO or multi-tenancy

## Core Concepts

### Authentication vs Authorization

**Authentication (AuthN)**: Who are you?
- Verifying identity (username/password, OAuth, biometrics)
- Issuing credentials (sessions, tokens)
- Managing login/logout

**Authorization (AuthZ)**: What can you do?
- Permission checking
- Role-based access control (RBAC)
- Resource ownership validation
- Policy enforcement

### Authentication Strategies

| Strategy | State | Scalability | Complexity |
|----------|-------|-------------|------------|
| Session-Based | Stateful (server) | Requires shared store | Simple |
| Token-Based (JWT) | Stateless | Horizontal | Medium |
| OAuth2/OpenID Connect | Delegated | Horizontal | High |

## JWT Authentication

### Access + Refresh Token Pattern

Use short-lived access tokens (15 min) and long-lived refresh tokens (7 days).

**Token generation:**
- Access token: contains userId, email, role — expires in 15 minutes
- Refresh token: contains only userId — expires in 7 days

**Refresh flow:**
1. Client sends refresh token to `/api/auth/refresh`
2. Server verifies JWT signature AND checks token exists in database
3. Server issues new access token
4. Optionally rotate refresh token

**Security:**
- Hash refresh tokens before storing in database
- Revoke all tokens on password change
- Revoke individual tokens on logout

### Middleware Pattern

Extract token from `Authorization: Bearer <token>` header, verify, attach user to request object. Return 401 on missing/invalid token, 403 on insufficient permissions.

## Session-Based Authentication

**Stack:** Express + express-session + Redis (connect-redis)

**Cookie settings:**
- `secure: true` in production (HTTPS only)
- `httpOnly: true` (no JavaScript access)
- `sameSite: 'strict'` (CSRF protection)
- `maxAge: 24 hours`

**Login:** Verify credentials → store userId and role in session → session persisted in Redis

**Logout:** Call `req.session.destroy()` → clear cookie

## OAuth2 / Social Login

**Stack:** Passport.js with strategy (Google, GitHub, etc.)

**Flow:**
1. User clicks login → redirect to OAuth provider
2. Provider authenticates → redirects back with code
3. Server exchanges code for profile
4. Find or create user in database
5. Issue JWT or establish session

**Key principle:** Never trust the OAuth profile alone — always link to a user record in your database.

## Authorization Patterns

### Role-Based Access Control (RBAC)

Define a role hierarchy where higher roles inherit lower permissions:

```
ADMIN → [ADMIN, MODERATOR, USER]
MODERATOR → [MODERATOR, USER]
USER → [USER]
```

Middleware: `requireRole(Role.ADMIN)` checks if user's role hierarchy includes the required role.

### Permission-Based Access Control

More granular than RBAC. Assign specific permissions to roles:

```
USER: [read:posts, write:posts]
MODERATOR: [read:posts, write:posts, read:users]
ADMIN: [all permissions]
```

Middleware: `requirePermission(Permission.READ_USERS)` checks if user's role has the required permission.

### Resource Ownership

Check if the authenticated user owns the resource they're trying to modify:

1. Skip ownership check for admins
2. Look up resource by ID
3. Compare `resource.userId` with `req.user.userId`
4. Return 403 if mismatch

## Security Checklist

- [ ] Use short-lived access tokens (15 min or less)
- [ ] Hash refresh tokens before storing
- [ ] Use `httpOnly`, `secure`, `sameSite` cookie flags
- [ ] Validate all tokens on every protected route
- [ ] Implement token revocation on logout/password change
- [ ] Use HTTPS in production
- [ ] Rate-limit auth endpoints
- [ ] Never expose sensitive data in JWT payload
- [ ] Use parameterized queries to prevent SQL injection in auth lookups
- [ ] Implement CSRF protection for session-based auth
