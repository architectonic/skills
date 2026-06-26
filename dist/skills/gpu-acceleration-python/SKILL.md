---
name: gpu-acceleration-python
description: GPU-accelerate Python code using CuPy, Numba CUDA, Warp, cuDF, cuML, cuGraph, and the NVIDIA RAPIDS ecosystem. Use whenever the user mentions GPU/CUDA/NVIDIA acceleration, or wants to speed up NumPy, pandas, scikit-learn, NetworkX, or image processing workloads. Covers physics simulation, differentiable rendering, particle systems, vector search, and interactive dashboards.
type: Playbook
---

# GPU Acceleration for Python

## Overview

GPU-accelerate Python code using NVIDIA's RAPIDS ecosystem and related libraries. Transform CPU-bound Python code to run on NVIDIA GPUs for dramatic speedups — often 10x to 1000x for suitable workloads.

## When This Skill Applies

- User wants to speed up numerical/scientific Python code
- User mentions CUDA, GPU, NVIDIA, or parallel computing
- User has NumPy, pandas, SciPy, scikit-learn, or NetworkX code processing large datasets
- User needs physics simulation, particle systems, or differentiable simulation
- User is doing vector search, nearest neighbor search, or similarity search
- User wants GPU-accelerated interactive dashboards
- User is doing image processing, computer vision, or medical imaging
- User has geospatial analysis with large datasets

## Decision Framework: Which Library to Use

### CuPy — Array/Matrix Operations (NumPy replacement)

Use when code is primarily NumPy array operations (element-wise math, linear algebra, FFT, sorting). CuPy is a drop-in replacement — often just change `import numpy as np` to `import cupy as cp`.

**Best for:** Linear algebra, FFTs, array math, signal processing, Monte Carlo with array ops.

### Numba CUDA — Custom GPU Kernels

Use when you need custom algorithms that don't map to standard array operations, or fine-grained control over GPU threads, blocks, and shared memory.

**Best for:** Custom kernels, particle simulations, stencil codes, algorithms needing shared memory.

### Warp — Simulation and Spatial Computing

Use for physics simulation (particles, cloth, fluids, rigid bodies), geometry processing (mesh operations, ray casting), robotics, and differentiable simulation.

**Best for:** Physics simulation, mesh ray casting, particle systems, differentiable rendering, robotics kinematics.

### cuDF — DataFrame Operations (pandas replacement)

Use for pandas DataFrame operations (filtering, groupby, joins, aggregations). `cudf.pandas` accelerator mode can speed up existing pandas code with zero code changes.

**Best for:** Data wrangling, ETL, groupby/aggregations, joins, string processing on dataframes.

### cuML — Machine Learning (scikit-learn replacement)

Use for scikit-learn estimators (classification, regression, clustering, dimensionality reduction). `cuml.accel` accelerator mode speeds up existing sklearn code with zero changes.

**Best for:** Classification, regression, clustering, preprocessing pipelines, model inference.

### cuGraph — Graph Analytics (NetworkX replacement)

Use for NetworkX graph algorithms (centrality, community detection, shortest paths, PageRank). `nx-cugraph` backend accelerates existing NetworkX code via environment variable.

**Best for:** PageRank, betweenness centrality, community detection, BFS/SSSP, link prediction.

### cuVS — Vector Search (Faiss/Annoy replacement)

Use for approximate nearest neighbor (ANN) search on high-dimensional vectors, similarity search for RAG, recommender systems.

**Best for:** Embedding search, RAG retrieval, recommender systems, image/text/audio similarity search.

### cuSpatial — Geospatial Analytics (GeoPandas replacement)

Use for GeoPandas spatial operations (point-in-polygon, spatial joins, distance calculations), trajectory analysis.

**Best for:** Point-in-polygon tests, spatial joins, haversine distance, trajectory analysis.

### cuCIM — Image Processing (scikit-image replacement)

Use for scikit-image operations (filtering, morphology, segmentation, feature detection), digital pathology, medical imaging.

**Best for:** Image filtering, morphology, thresholding, whole-slide image processing, DL preprocessing.

### cuxfilter — Interactive Dashboards

Use for interactive cross-filtering dashboards on large datasets (millions of rows), exploratory data analysis with linked charts.

**Best for:** Interactive data exploration, multi-chart cross-filtering, geospatial visualization.

### KvikIO — High-Performance GPU File IO

Use for loading large binary data files directly into GPU memory, reading from remote storage (S3, HTTP) into GPU memory, GPUDirect Storage (GDS).

**Best for:** Loading binary data to GPU, saving GPU arrays to disk, reading from S3/HTTP directly to GPU.

### RAFT — Low-Level GPU Primitives

Use for GPU-accelerated sparse eigenvalue problems, low-level device memory management, multi-node multi-GPU communication.

**Best for:** Sparse eigenvalue decomposition, R-MAT graph generation, multi-GPU orchestration.

## Combining Libraries

Many real workloads benefit from using multiple libraries together. They interoperate via the CUDA Array Interface — zero-copy data sharing.

**Common combinations:**
- cuDF + cuML: Load/preprocess data with cuDF, train/predict with cuML
- cuDF + cuGraph: Build graphs from cuDF edge lists, run graph analytics
- cuML + cuVS: Train embedding model with cuML, index/search with cuVS
- CuPy + cuVS: Generate embeddings with CuPy, build search index with cuVS
- Warp + PyTorch: Differentiable simulation in Warp, backpropagate into PyTorch
- cuDF + cuxfilter: Load data with cuDF, build interactive dashboards

## Installation

```bash
# CuPy
uv add cupy-cuda12x

# Numba with CUDA support
uv add numba numba-cuda

# Warp
uv add warp-lang

# RAPIDS ecosystem (CUDA 12)
uv add --extra-index-url=https://pypi.nvidia.com cudf-cu12
uv add --extra-index-url=https://pypi.nvidia.com cuml-cu12
uv add --extra-index-url=https://pypi.nvidia.com cugraph-cu12
uv add --extra-index-url=https://pypi.nvidia.com cuvs-cu12
uv add --extra-index-url=https://pypi.nvidia.com cuspatial-cu12
uv add --extra-index-url=https://pypi.nvidia.com cucim-cu12
uv add --extra-index-url=https://pypi.nvidia.com cuxfilter-cu12
uv add kvikio-cu12
uv add --extra-index-url=https://pypi.nvidia.com pylibraft-cu12
```

## Optimization Workflow

### 1. Profile First
Before optimizing, understand where time is actually spent. Don't guess — measure.

### 2. Assess GPU Suitability
GPU excels when:
- **Data parallelism is high**: Same operation applies to thousands/millions of elements
- **Compute intensity is high**: Many FLOPs per byte of memory accessed
- **Data is large enough**: GPU overhead means small arrays (< ~10K elements) may be slower
- **Memory fits**: Data must fit in GPU memory (typically 8-80 GB)

GPU is a poor fit when:
- Data is tiny (< 10K elements)
- Algorithm is inherently sequential with data dependencies
- Code is I/O bound (disk, network)
- Many small, heterogeneous operations (kernel launch overhead dominates)

### 3. Start Simple, Then Optimize
1. **Try the drop-in replacement first** — CuPy for NumPy, cudf.pandas for pandas, cuml.accel for sklearn
2. **Minimize host-device transfers** — Keep data on GPU
3. **Batch operations** — Fewer large GPU operations beat many small ones
4. **Only write custom kernels if needed** — CuPy and cuDF use NVIDIA's hand-tuned libraries
5. **Profile the GPU version** — Use `nsys` or CuPy's built-in benchmarking

### 4. Memory Management Principles
- Pre-allocate output arrays instead of creating new ones in loops
- Reuse GPU memory — use memory pools (CuPy has this built-in)
- Use pinned (page-locked) host memory for faster CPU-GPU transfers
- Avoid unnecessary copies — use in-place operations where possible
- Stream operations for overlapping compute and data transfer

### 5. Common Pitfalls
- **Implicit CPU fallback**: Some operations silently fall back to CPU
- **Synchronization overhead**: GPU operations are asynchronous; calling `.get()` forces a sync
- **dtype mismatches**: Use `float32` instead of `float64` when precision allows — GPU float32 throughput is 2x-32x higher
- **Small kernel launches**: Each kernel launch has ~5-20us overhead; fuse operations when possible

## Code Transformation Patterns

### NumPy to CuPy
```python
# Before (CPU)
import numpy as np
a = np.random.rand(10_000_000)
b = np.fft.fft(a)

# After (GPU) — often just change the import
import cupy as cp
a = cp.random.rand(10_000_000)
b = cp.fft.fft(a)
```

### pandas to cuDF
```python
# Before (CPU)
import pandas as pd
df = pd.read_parquet("large_data.parquet")
result = df.groupby("category")["value"].mean()

# After (GPU)
import cudf
df = cudf.read_parquet("large_data.parquet")
result = df.groupby("category")["value"].mean()

# Or zero-code-change: python -m cudf.pandas your_script.py
```

### Custom Loop to Numba CUDA Kernel
```python
# Before (CPU) — slow Python loop
def process(data, out):
    for i in range(len(data)):
        out[i] = math.sin(data[i]) * math.exp(-data[i])

# After (GPU) — Numba kernel
from numba import cuda
@cuda.jit
def process(data, out):
    i = cuda.grid(1)
    if i < data.size:
        out[i] = math.sin(data[i]) * math.exp(-data[i])

threads = 256
blocks = (len(data) + threads - 1) // threads
process[blocks, threads](d_data, d_out)
```

### NetworkX to cuGraph
```python
# Before (CPU)
import networkx as nx
G = nx.read_edgelist("edges.csv", delimiter=",", nodetype=int)
pr = nx.pagerank(G)

# After (GPU)
import cugraph, cudf
edges = cudf.read_csv("edges.csv", names=["src", "dst"], dtype=["int32", "int32"])
G = cugraph.Graph()
G.from_cudf_edgelist(edges, source="src", destination="dst")
pr = cugraph.pagerank(G)

# Or zero-code-change: NX_CUGRAPH_AUTOCONFIG=True python your_script.py
```

### scikit-learn to cuML
```python
# Before (CPU)
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# After (GPU)
from cuml.ensemble import RandomForestClassifier
from cuml.preprocessing import StandardScaler
from cuml.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Or zero-code-change: python -m cuml.accel your_script.py
```

## Integration

- Use with `performance-optimization` skill for profiling before GPU acceleration
- Use with `python-resilience` skill for error handling in GPU pipelines
- Use with `jupyter-live-kernel` skill for interactive GPU development
