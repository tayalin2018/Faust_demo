#!/usr/bin/env python
"""
Batch-convert FAUST (or any) meshes and collect simple stats.

Usage:
    python process_faust.py <mesh_folder>
Example:
    python process_faust.py MPI-FAUST/training/registrations
"""

import pathlib, time, json, sys
import trimesh
from tqdm import tqdm


def main(mesh_dir: str) -> None:
    root = pathlib.Path(mesh_dir).expanduser()

    # Gather both .ply and .obj meshes so the script works on either set
    mesh_paths = sorted(root.rglob("*.ply"))
    if not mesh_paths:
        print(f"No .ply or .obj files found in {root}")
        sys.exit(1)

    stats, t0 = [], time.time()

    for mesh_path in tqdm(mesh_paths):
        mesh = trimesh.load(mesh_path, process=False)

        stats.append(
            {
                "file": mesh_path.name,
                "verts": len(mesh.vertices),
                "faces": len(mesh.faces),
            }
        )

        # Export with the opposite extension so we don’t overwrite originals
        new_suffix = ".obj" if mesh_path.suffix == ".ply" else ".ply"
        mesh.export(mesh_path.with_suffix(new_suffix))

    elapsed = time.time() - t0
    print(
        f"Processed {len(stats)} meshes in {elapsed:.1f}s "
        f"({elapsed / len(stats):.3f}s/mesh)"
    )

    with open("faust_stats.json", "w") as f:
        json.dump(stats, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_faust.py <mesh_folder>")
        sys.exit(1)

    main(sys.argv[1])
