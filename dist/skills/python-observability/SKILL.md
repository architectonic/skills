---
name: python-observability
description: Python observability patterns including structured logging with structlog, Prometheus metrics, and OpenTelemetry distributed tracing. Use when adding logging, implementing metrics collection, setting up tracing, or debugging production Python systems.
type: Metric
---

# Python Observability

> Source: SWE-Skills-Bench — `skills/python-observability/SKILL.md`

Instrument Python applications with structured logs, metrics, and traces to answer "what, where, and why" without deploying new code.

## When to Use

- Adding structured logging to Python apps
- Implementing Prometheus metrics in Python services
- Setting up OpenTelemetry tracing in Python
- Propagating correlation IDs through request chains
- Debugging production Python systems

## Core Concepts

1. **Structured Logging** — JSON logs with consistent fields, machine-readable for queries and alerts
2. **Four Golden Signals** — Latency, traffic, errors, saturation at every service boundary
3. **Correlation IDs** — Thread a unique ID through all logs and spans for a single request
4. **Bounded Cardinality** — Never use unbounded values (user IDs) as metric labels

## Pattern 1: Structured Logging with structlog

```python
import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    cache_logger_on_first_use=True,
)
logger = structlog.get_logger()
```

## Pattern 2: Correlation ID Propagation

```python
from contextvars import ContextVar
import uuid

correlation_id: ContextVar[str] = ContextVar("correlation_id", default="")

def set_correlation_id(cid=None):
    cid = cid or str(uuid.uuid4())
    correlation_id.set(cid)
    structlog.contextvars.bind_contextvars(correlation_id=cid)
    return cid

# FastAPI middleware example:
async def correlation_middleware(request: Request, call_next):
    cid = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
    set_correlation_id(cid)
    response = await call_next(request)
    response.headers["X-Correlation-ID"] = cid
    return response
```

Propagate to downstream services via `X-Correlation-ID` header on all outbound HTTP calls.

## Pattern 3: Semantic Log Levels

| Level | Purpose | Examples |
|-------|---------|----------|
| `DEBUG` | Diagnostics | Variable values, internal state |
| `INFO` | Operations | Request start/end, job completion |
| `WARNING` | Recoverable anomalies | Retries, fallbacks used |
| `ERROR` | Failures needing attention | Exceptions, service unavailable |

Never log expected behavior at `ERROR` (e.g., wrong password → `INFO`).

## Pattern 4: Prometheus Four Golden Signals

```python
from prometheus_client import Counter, Histogram, Gauge

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency", ["method", "endpoint", "status"],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10],
)
REQUEST_COUNT = Counter("http_requests_total", "Total requests", ["method", "endpoint", "status"])
ERROR_COUNT = Counter("http_errors_total", "Total errors", ["method", "endpoint", "error_type"])
DB_POOL_USAGE = Gauge("db_connection_pool_used", "DB connections in use")
```

## Pattern 5: Bounded Cardinality

```python
# BAD: unbounded user IDs
REQUEST_COUNT.labels(method="GET", user_id=user.id)

# GOOD: bounded label values only
REQUEST_COUNT.labels(method="GET", endpoint="/users", status="200")
REQUEST_COUNT.labels(method="GET", user_tier="premium")  # bounded set
```

## Pattern 6: OpenTelemetry Tracing

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=otlp_endpoint))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

async def process_order(order_id: str):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        with tracer.start_as_current_span("validate_order"):
            validate_order(order_id)
        with tracer.start_as_current_span("charge_payment"):
            charge_payment(order_id)
```

## Pattern 7: Timed Operations Context Manager

```python
from contextlib import contextmanager
import time

@contextmanager
def timed_operation(name: str, **extra):
    start = time.perf_counter()
    logger.debug("Operation started", operation=name, **extra)
    try:
        yield
    except Exception as e:
        elapsed = (time.perf_counter() - start) * 1000
        logger.error("Operation failed", operation=name, duration_ms=round(elapsed, 2), error=str(e), **extra)
        raise
    else:
        elapsed = (time.perf_counter() - start) * 1000
        logger.info("Operation completed", operation=name, duration_ms=round(elapsed, 2), **extra)

with timed_operation("fetch_orders", user_id=user.id):
    orders = await get_orders(user.id)
```

## Best Practices

1. Use structured logging with JSON output in production
2. Propagate correlation IDs across all service boundaries
3. Track the four golden signals for every service
4. Keep metric label cardinality bounded
5. Don't log expected behavior at ERROR level
6. Include context in every log entry
7. Use `@contextmanager` for consistent timing
8. Separize observability code from business logic
9. Test observability in integration tests
10. Set up alerts on metrics — metrics without alerts are useless
