# FAUST 3-D Mesh Pipeline

Small, self-contained script that batch-converts **FAUST** human-body scans between **PLY ↔ OBJ**, logs basic geometry stats, and prints throughput.

| Metric              | Value                                  |
|---------------------|----------------------------------------|
| Meshes processed    | **500** (FAUST training + test)        |
| Runtime (CPU)       | **190 s total**  ≈ **0.38 s / mesh**   |
| Output files        | 500 converted meshes<br>`faust_stats.json` (verts/faces) |

---

## Why this exists
The Max Planck Institute’s **FAUST** dataset is a canonical benchmark for shape analysis and avatar research.  
Before high-level modeling, raw scans often need format conversion and quick sanity checks—exactly what this script does in ~150 lines of Python.

---

## Quick start (3 commands)

```bash
git clone https://github.com/tayalin2018/faust_demo.git
cd faust_demo
python -m pip install trimesh numpy tqdm
python process_faust.py MPI-FAUST          # if the dataset sits in ./MPI-FAUST
