## FAUST 3-D Mesh Pipeline
Small, self-contained script that batch-converts FAUST .ply human-body scans to .obj format, logs basic geometry statistics, and prints throughput.

| Metric            | Value                                     |
|-------------------|-------------------------------------------|
| Meshes processed  | **400** (all .ply files in FAUST scans)   |
| Runtime (CPU)     | **191 s total**  ≈  **0.48 s / mesh**     |
| Output files      | 400 converted meshes • `faust_stats.json` (verts/faces) |

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

---

## Mesh Processing Outcome
![Processing outcome](Mesh%20processing%20outcome.png)

---
