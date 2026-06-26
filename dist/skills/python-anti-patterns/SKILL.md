---
name: Python Anti-Patterns Checklist
description: Common Python anti-patterns to avoid. Use as a checklist when reviewing code, before finalizing implementations, or when debugging issues that might stem from known bad practices.
source: SWE-Skills-Bench (SWE-Skills-Bench/skills/python-anti-patterns/SKILL.md)
license: MIT
tags: [software-development, python, anti-patterns, code-review, best-practices, checklist]
type: Playbook
---

# Python Anti-Patterns Checklist

A reference checklist of common mistakes and anti-patterns in Python code. Review before finalizing implementations.

## When to Use This Skill

- Reviewing code before merge
- Debugging mysterious issues
- Teaching or learning Python best practices
- Establishing team coding standards
- Refactoring legacy code

## Infrastructure Anti-Patterns

### Scattered Timeout/Retry Logic

```python
# BAD: Timeout logic duplicated everywhere
def fetch_user(user_id):
    try:
        return requests.get(url, timeout=30)
    except Timeout:
        return None

# GOOD: Centralized retry logic
@retry(stop=stop_after_attempt(3), wait=wait_exponential())
def http_get(url: str) -> Response:
    return requests.get(url, timeout=30)
```

### Double Retry

```python
# BAD: Retrying at multiple layers
@retry(max_attempts=3)  # Application retry
def call_service():
    return client.request()  # Client also has retry configured!

# FIX: Retry at one layer only
```

### Hard-Coded Configuration

```python
# BAD: Secrets and config in code
DB_HOST = "prod-db.example.com"

# GOOD: Environment variables with typed settings
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    db_host: str = Field(alias="DB_HOST")
settings = Settings()
```

## Architecture Anti-Patterns

### Exposed Internal Types

```python
# BAD: Leaking ORM model to API
@app.get("/users/{id}")
def get_user(id: str) -> UserModel:  # SQLAlchemy model
    return db.query(UserModel).get(id)

# GOOD: Use DTOs/response models
@app.get("/users/{id}")
def get_user(id: str) -> UserResponse:
    user = db.query(UserModel).get(id)
    return UserResponse.from_orm(user)
```

### Mixed I/O and Business Logic

```python
# BAD: SQL embedded in business logic
def calculate_discount(user_id: str) -> float:
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    # Business logic mixed with data access

# GOOD: Repository pattern, keep business logic pure
def calculate_discount(user: User, orders: list[Order]) -> float:
    if len(orders) > 10:
        return 0.15
    return 0.0
```

## Error Handling Anti-Patterns

### Bare Exception Handling

```python
# BAD: Swallowing all exceptions
try:
    process()
except Exception:
    pass  # Silent failure

# GOOD: Catch specific exceptions
try:
    process()
except ConnectionError as e:
    logger.warning("Connection failed", error=str(e))
    raise
except ValueError as e:
    logger.error("Invalid input", error=str(e))
    raise BadRequestError(str(e))
```

### Ignored Partial Failures

```python
# BAD: Stops on first error
def process_batch(items):
    results = []
    for item in items:
        result = process(item)  # Raises on error - batch aborted
        results.append(result)
    return results

# GOOD: Capture both successes and failures
def process_batch(items) -> BatchResult:
    succeeded = {}
    failed = {}
    for idx, item in enumerate(items):
        try:
            succeeded[idx] = process(item)
        except Exception as e:
            failed[idx] = e
    return BatchResult(succeeded, failed)
```

### Missing Input Validation

```python
# BAD: No validation
def create_user(data: dict):
    return User(**data)  # Crashes deep in code on bad input

# GOOD: Validate early at API boundaries
def create_user(data: dict) -> User:
    validated = CreateUserInput.model_validate(data)
    return User.from_input(validated)
```

## Resource Anti-Patterns

### Unclosed Resources

```python
# BAD: File never closed
def read_file(path):
    f = open(path)
    return f.read()

# GOOD: Use context managers
def read_file(path):
    with open(path) as f:
        return f.read()
```

### Blocking in Async

```python
# BAD: Blocks the entire event loop
async def fetch_data():
    time.sleep(1)
    response = requests.get(url)

# GOOD: Use async-native libraries
async def fetch_data():
    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
```

## Type Safety Anti-Patterns

### Missing Type Hints

```python
# BAD: No types
def process(data):
    return data["value"] * 2

# GOOD: Annotate all public functions
def process(data: dict[str, int]) -> int:
    return data["value"] * 2
```

### Untyped Collections

```python
# BAD: Generic list without type parameter
def get_users() -> list: ...

# GOOD: Use type parameters
def get_users() -> list[User]: ...
```

## Testing Anti-Patterns

### Only Testing Happy Paths

```python
# BAD: Only tests success case
def test_create_user():
    user = service.create_user(valid_data)
    assert user.id is not None

# GOOD: Test error conditions and edge cases
def test_create_user_success():
    user = service.create_user(valid_data)
    assert user.id is not None

def test_create_user_invalid_email():
    with pytest.raises(ValueError, match="Invalid email"):
        service.create_user(invalid_email_data)
```

### Over-Mocking

```python
# BAD: Mocking everything
def test_user_service():
    mock_repo = Mock()
    mock_cache = Mock()
    mock_logger = Mock()
    # Test doesn't verify real behavior

# GOOD: Use integration tests for critical paths. Mock only external services.
```

## Quick Review Checklist

Before finalizing code, verify:

- [ ] No scattered timeout/retry logic (centralized)
- [ ] No double retry (app + infrastructure)
- [ ] No hard-coded configuration or secrets
- [ ] No exposed internal types (ORM models, protobufs)
- [ ] No mixed I/O and business logic
- [ ] No bare `except Exception: pass`
- [ ] No ignored partial failures in batches
- [ ] No missing input validation
- [ ] No unclosed resources (using context managers)
- [ ] No blocking calls in async code
- [ ] All public functions have type hints
- [ ] Collections have type parameters
- [ ] Error paths are tested
- [ ] Edge cases are covered

## Common Fixes Summary

| Anti-Pattern | Fix |
|-------------|-----|
| Scattered retry logic | Centralized decorators |
| Hard-coded config | Environment variables + pydantic-settings |
| Exposed ORM models | DTO/response schemas |
| Mixed I/O + logic | Repository pattern |
| Bare except | Catch specific exceptions |
| Batch stops on error | Return BatchResult with successes/failures |
| No validation | Validate at boundaries with Pydantic |
| Unclosed resources | Context managers |
| Blocking in async | Async-native libraries |
| Missing types | Type annotations on all public APIs |
| Only happy path tests | Test errors and edge cases |
