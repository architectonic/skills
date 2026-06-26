---
name: python-performance-optimization
description: Profile and optimize Python code for performance. Use when debugging slow Python code, optimizing bottlenecks, reducing latency, optimizing CPU-intensive operations, reducing memory consumption, or improving data processing pipeline speed. Covers cProfile, line_profiler, memory_profiler, py-spy, and common optimization patterns.
type: Playbook
---

# Python Performance Optimization

Profile first, optimize second. Measure before and after every change.

## Profiling Tools

### cProfile — CPU Profiling

```python
import cProfile
import pstats
from pstats import SortKey

profiler = cProfile.Profile()
profiler.enable()
main()
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats(SortKey.CUMULATIVE)
stats.print_stats(10)  # Top 10 functions
stats.dump_stats("profile_output.prof")
```

Command-line: `python -m cProfile -o output.prof script.py`

### line_profiler — Line-by-Line

```bash
kernprof -l -v script.py
```

### memory_profiler — Memory Usage

```python
from memory_profiler import profile

@profile
def memory_intensive():
    big_list = [i for i in range(1000000)]
    return sum(big_list)
```

Run: `python -m memory_profiler script.py`

### py-spy — Production Profiling

```bash
py-spy top --pid 12345              # Live view
py-spy record -o profile.svg --pid 12345  # Flamegraph
py-spy dump --pid 12345             # Current call stack
```

## Optimization Patterns

### 1. List Comprehensions vs Loops

```python
# Slow
result = []
for i in range(n):
    result.append(i**2)

# Fast
result = [i**2 for i in range(n)]
```

### 2. Generator Expressions for Memory

```python
# Memory-intensive
data = [i**2 for i in range(1000000)]

# Memory-efficient (constant memory regardless of size)
data = (i**2 for i in range(1000000))
```

### 3. String Concatenation

```python
# Slow
result = ""
for item in items:
    result += str(item)

# Fast
result = "".join(str(item) for item in items)
```

### 4. Dictionary Lookups vs List Searches

```python
# O(n) — slow for large collections
target in items_list

# O(1) — fast
target in items_dict
```

### 5. Local Variable Access

```python
# Faster: local variable access is cheaper than global
def use_local():
    local_value = GLOBAL_VALUE
    for i in range(10000):
        total += local_value
```

### 6. NumPy for Numerical Operations

```python
import numpy as np

# Vectorized operations are orders of magnitude faster
a = np.arange(100000)
b = np.arange(100000)
result = a * b  # vs [x*y for x,y in zip(a,b)]
```

### 7. Caching with lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 8. __slots__ for Memory

```python
class WithSlots:
    __slots__ = ['x', 'y', 'z']
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
# Uses ~40% less memory than regular class with __dict__
```

### 9. Set Operations for Membership Testing

```python
# O(n)
if item in my_list:
    pass

# O(1)
if item in my_set:
    pass
```

### 10. Avoid Repeated Work in Loops

```python
# Slow: recomputes len() every iteration
for i in range(len(my_list)):
    pass

# Fast: compute once
n = len(my_list)
for i in range(n):
    pass
```

## Key Metrics

- **Execution Time**: `timeit.timeit()` for accurate measurements
- **Memory Usage**: `memory_profiler`, `sys.getsizeof()`, `tracemalloc`
- **CPU Utilization**: `cProfile`, `py-spy`
- **I/O Wait**: `py-spy` can show blocked threads

## Optimization Workflow

1. **Profile first** — identify the actual bottleneck
2. **Measure baseline** — record before metrics
3. **Optimize the bottleneck** — focus on the top offender
4. **Measure after** — confirm improvement
5. **Repeat** — next bottleneck

## Source

Distilled from `GeniusHTX/SWE-Skills-Bench` → `skills/python-performance-optimization/SKILL.md` (MIT).
