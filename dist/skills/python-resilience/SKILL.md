---
name: Python Resilience Patterns
description: Python resilience patterns including automatic retries, exponential backoff, timeouts, and fault-tolerant decorators. Use when adding retry logic, implementing timeouts, building fault-tolerant services, or handling transient failures.
source: SWE-Skills-Bench (SWE-Skills-Bench/skills/python-resilience/SKILL.md)
license: MIT
tags: [software-development, python, resilience, retry, backoff, circuit-breaker, fault-tolerance, tenacity]
type: Playbook
---

# Python Resilience Patterns

Build fault-tolerant Python applications that gracefully handle transient failures, network issues, and service outages.

## When to Use This Skill

- Adding retry logic to external service calls
- Implementing timeouts for network operations
- Building fault-tolerant microservices
- Handling rate limiting and backpressure
- Designing circuit breakers

## Core Concepts

1. **Transient vs Permanent Failures** — Retry transient errors (network timeouts). Don't retry permanent errors (invalid credentials, bad requests).
2. **Exponential Backoff** — Increase wait time between retries to avoid overwhelming recovering services.
3. **Jitter** — Add randomness to backoff to prevent thundering herd.
4. **Bounded Retries** — Cap both attempt count and total duration.

## Quick Start

```python
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential_jitter(initial=1, max=10),
)
def call_external_service(request: dict) -> dict:
    return httpx.post("https://api.example.com", json=request).json()
```

## Fundamental Patterns

### Pattern 1: Basic Retry with Tenacity

```python
from tenacity import (
    retry, stop_after_attempt, stop_after_delay,
    wait_exponential_jitter, retry_if_exception_type,
)

TRANSIENT_ERRORS = (ConnectionError, TimeoutError, OSError)

@retry(
    retry=retry_if_exception_type(TRANSIENT_ERRORS),
    stop=stop_after_attempt(5) | stop_after_delay(60),
    wait=wait_exponential_jitter(initial=1, max=30),
)
def fetch_data(url: str) -> dict:
    response = httpx.get(url, timeout=30)
    response.raise_for_status()
    return response.json()
```

### Pattern 2: Retry Only Appropriate Errors

```python
RETRYABLE_EXCEPTIONS = (
    ConnectionError, TimeoutError,
    httpx.ConnectTimeout, httpx.ReadTimeout,
)

@retry(
    retry=retry_if_exception_type(RETRYABLE_EXCEPTIONS),
    stop=stop_after_attempt(3),
    wait=wait_exponential_jitter(initial=1, max=10),
)
def resilient_api_call(endpoint: str) -> dict:
    return httpx.get(endpoint, timeout=10).json()
```

Never retry: `ValueError`, `TypeError` (bugs), `AuthenticationError` (permanent), HTTP 4xx (except 429).

### Pattern 3: HTTP Status Code Retries

```python
RETRY_STATUS_CODES = {429, 502, 503, 504}

def should_retry_response(response: httpx.Response) -> bool:
    return response.status_code in RETRY_STATUS_CODES

@retry(
    retry=retry_if_result(should_retry_response),
    stop=stop_after_attempt(3),
    wait=wait_exponential_jitter(initial=1, max=10),
)
def http_request(method: str, url: str, **kwargs) -> httpx.Response:
    return httpx.request(method, url, timeout=30, **kwargs)
```

### Pattern 4: Combined Exception and Status Retry

```python
@retry(
    retry=(
        retry_if_exception_type(TRANSIENT_EXCEPTIONS) |
        retry_if_result(is_retryable_response)
    ),
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=1, max=30),
    before_sleep=before_sleep_log(logger, logging.WARNING),
)
def robust_http_call(method: str, url: str, **kwargs) -> httpx.Response:
    return httpx.request(method, url, timeout=30, **kwargs)
```

### Pattern 5: Logging Retry Attempts

```python
def log_retry_attempt(retry_state):
    exception = retry_state.outcome.exception()
    logger.warning(
        "Retrying operation",
        attempt=retry_state.attempt_number,
        exception_type=type(exception).__name__,
        exception_message=str(exception),
    )

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, max=10),
    before_sleep=log_retry_attempt,
)
def call_with_logging(request: dict) -> dict:
    ...
```

### Pattern 6: Timeout Decorator

```python
def with_timeout(seconds: float):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
        return wrapper
    return decorator

@with_timeout(30)
async def fetch_with_timeout(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
```

### Pattern 7: Cross-Cutting Concerns via Decorators

```python
@traced("fetch_user_data")
@with_timeout(30)
@retry(stop=stop_after_attempt(3), wait=wait_exponential_jitter())
async def fetch_user_data(user_id: str) -> dict:
    ...
```

### Pattern 8: Fail-Safe Defaults

```python
def fail_safe(default, log_failure: bool = True):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if log_failure:
                    logger.warning("Operation failed, using default", error=str(e))
                return default
        return wrapper
    return decorator

@fail_safe(default=[])
async def get_recommendations(user_id: str) -> list[str]:
    ...
```

## Best Practices Summary

1. **Retry only transient errors** — Don't retry bugs or authentication failures
2. **Use exponential backoff** — Give services time to recover
3. **Add jitter** — Prevent thundering herd from synchronized retries
4. **Cap total duration** — `stop_after_attempt(5) | stop_after_delay(60)`
5. **Log every retry** — Silent retries hide systemic problems
6. **Use decorators** — Keep retry logic separate from business logic
7. **Inject dependencies** — Make infrastructure testable
8. **Set timeouts everywhere** — Every network call needs a timeout
9. **Fail gracefully** — Return cached/default values for non-critical paths
10. **Monitor retry rates** — High retry rates indicate underlying issues
