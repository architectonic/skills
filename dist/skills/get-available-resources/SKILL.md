---
name: Get Available Resources
description: Detect available computational resources (CPU cores, GPUs, memory, disk space) at the start of any computationally intensive task. Generates a resource report with strategic recommendations for parallel processing, memory management, GPU acceleration, and large-data handling. Use proactively before data analysis, model training, or large-scale processing.
source: K-Dense-AI/scientific-agent-skills (MIT)
distilled: 2026-06-23
type: Playbook
---

# Get Available Resources

## When to Use

Run this skill **proactively** before any computationally intensive task:

- **Before data analysis**: Determine if datasets fit in memory or need out-of-core processing
- **Before model training**: Check GPU availability and backend
- **Before parallel processing**: Identify optimal worker count
- **Before large file operations**: Verify disk space
- **At project initialization**: Understand baseline capabilities

## Resource Detection

```bash
python scripts/detect_resources.py
# Output: .claude_resources.json
```

Detects:
1. **CPU**: physical/logical cores, architecture, frequency
2. **GPU**: NVIDIA (nvidia-smi), AMD (rocm-smi), Apple Silicon (Metal)
3. **Memory**: total, available, usage percentage, swap
4. **Disk**: total, available for working directory
5. **OS**: type, version, Python version

## Strategic Recommendations

### Parallel Processing
| Cores | Strategy | Workers |
|---|---|---|
| 8+ | High parallelism | cores - 2 |
| 4-7 | Moderate | cores - 1 |
| < 4 | Sequential | 1 |

### Memory Strategy
| Available | Strategy |
|---|---|
| < 4GB | Out-of-core (Dask, Zarr, H5py) |
| 4-16GB | Dask/Zarr for datasets > 2GB |
| > 16GB | Load into memory |

### GPU Backends
| Hardware | Backend | Libraries |
|---|---|---|
| NVIDIA | CUDA | PyTorch, TensorFlow, JAX, CuPy, RAPIDS |
| AMD | ROCm | PyTorch-ROCm, TensorFlow-ROCm |
| Apple Silicon | Metal | PyTorch-MPS, TF-Metal, JAX-Metal |
| None | CPU | CPU-optimized libraries |

## Using Recommendations in Code

```python
import json, torch

with open('.claude_resources.json') as f:
    resources = json.load(f)

# Parallel processing
n_jobs = resources['recommendations']['parallel_processing']['suggested_workers']

# GPU device selection
backends = resources['gpu']['available_backends']
if 'CUDA' in backends:
    device = torch.device('cuda')
elif 'Metal' in backends:
    device = torch.device('mps')
else:
    device = torch.device('cpu')
```

## Best Practices

1. **Run early** — at project start or before major tasks
2. **Re-run periodically** — resources change over time
3. **Check before scaling** — verify before increasing workers or data sizes
4. **Document decisions** — keep resource files for portability

## Dependencies

```bash
uv pip install psutil
```

## Attribution

From K-Dense-AI/scientific-agent-skills (MIT), authored by K-Dense Inc.
