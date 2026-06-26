---
name: distributed-tracing
description: Implement distributed tracing with Jaeger and Tempo to track requests across microservices. Use when debugging latency in microservices, analyzing request flows, or implementing observability for distributed systems.
type: Playbook
---

# Distributed Tracing

> Source: SWE-Skills-Bench — `skills/distributed-tracing/SKILL.md`

Track requests across distributed systems to understand latency, dependencies, and failure points.

## When to Use

- Debug latency issues across services
- Understand service dependencies
- Identify bottlenecks in request paths
- Trace error propagation
- Analyze end-to-end request flows

## Tracing Concepts

```
Trace (Request ID: abc123)
  └─ Span: frontend [100ms]
       └─ Span: api-gateway [80ms]
            ├─ Span: auth-service [10ms]
            └─ Span: user-service [60ms]
                 └─ Span: database [40ms]
```

**Trace** — End-to-end request journey. **Span** — Single operation. **Context** — Propagated metadata. **Baggage** — Key-value pairs carried across boundaries.

## Quick Start: Jaeger with Docker Compose

```yaml
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686"  # UI
      - "14268:14268"  # Collector HTTP
      - "6831:6831/udp"  # Thrift compact
```

## Instrumentation

### Python (Flask + OpenTelemetry)

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

resource = Resource(attributes={"service.name": "my-service"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(
    JaegerExporter(agent_host_name="jaeger", agent_port=6831)
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

FlaskInstrumentor().instrument_app(app)
tracer = trace.get_tracer(__name__)
```

### Node.js (Express + OpenTelemetry)

```javascript
const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");
const { JaegerExporter } = require("@opentelemetry/exporter-jaeger");
const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");
const { registerInstrumentations } = require("@opentelemetry/instrumentation");
const { HttpInstrumentation } = require("@opentelemetry/instrumentation-http");
const { ExpressInstrumentation } = require("@opentelemetry/instrumentation-express");

const provider = new NodeTracerProvider({
  resource: { attributes: { "service.name": "my-service" } },
});
provider.addSpanProcessor(new BatchSpanProcessor(
  new JaegerExporter({ endpoint: "http://jaeger:14268/api/traces" })
));
provider.register();

registerInstrumentations({
  instrumentations: [new HttpInstrumentation(), new ExpressInstrumentation()],
});
```

### Go + OpenTelemetry

```go
exporter, _ := jaeger.New(jaeger.WithCollectorEndpoint(
    jaeger.WithEndpoint("http://jaeger:14268/api/traces")))
tp := sdktrace.NewTracerProvider(
    sdktrace.WithBatcher(exporter),
    sdktrace.WithResource(resource.NewWithAttributes(
        semconv.SchemaURL,
        semconv.ServiceNameKey.String("my-service"))))
otel.SetTracerProvider(tp)
```

## Context Propagation

Always propagate trace context across service boundaries:

```python
# Python: inject into outbound headers
from opentelemetry.propagate import inject
headers = {}
inject(headers)
response = requests.get(url, headers=headers)

# Extract on the receiving side
from opentelemetry.propagate import extract
context = extract(request.headers)
```

## Sampling Strategies

| Strategy | Config | Use Case |
|----------|--------|----------|
| Probabilistic | `type: probabilistic, param: 0.01` | 1% of traces, general prod |
| Rate Limiting | `type: ratelimiting, param: 100` | Max traces/second |
| Adaptive | Parent-based with trace ID ratio | Deterministic, keeps whole traces |

## Trace Analysis Queries

```
# Slow requests
service=my-service duration > 1s

# Error traces
service=my-service error=true tags.http.status_code >= 500
```

## Correlate Traces with Logs

```python
from opentelemetry import trace
span = trace.get_current_span()
trace_id = span.get_span_context().trace_id

logger.info("Processing request", extra={
    "trace_id": format(trace_id, '032x'),
    "span_id": format(span.get_span_context().span_id, '016x'),
})
```

## Grafana Tempo (Alternative to Jaeger)

Tempo integrates with Grafana for traces alongside metrics and logs. Uses same OpenTelemetry instrumentation — just change the exporter endpoint to Tempo's OTLP endpoint.

## Best Practices

1. Sample 1-10% in production (probabilistic or adaptive)
2. Add meaningful span attributes (user_id, request_id)
3. Propagate context across ALL service boundaries
4. Record exceptions in spans
5. Use consistent operation naming
6. Monitor tracing overhead (<1% CPU)
7. Use batch span processors in production
8. Implement baggage for cross-cutting context
9. Add span events for important milestones
10. Document instrumentation standards for your team
