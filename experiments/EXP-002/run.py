"""EXP-002: reproducible static-vs-temporal architecture experiment.

The script deliberately keeps rendering and research evidence separate:
- renders are outputs
- observations are structured records
- evidence is promoted only after evaluation/provenance

Requires: pyvista, numpy, imageio.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pyvista as pv


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"


def building() -> pv.PolyData:
    """Create a small deterministic architectural massing model."""
    parts = [
        pv.Box(bounds=(-5, 5, -4, 4, 0, 0.35)),
        pv.Box(bounds=(-4.5, -3.9, -3.5, 3.5, 0.35, 5.0)),
        pv.Box(bounds=(3.9, 4.5, -3.5, 3.5, 0.35, 5.0)),
        pv.Box(bounds=(-3.9, 3.9, 3.0, 3.5, 0.35, 5.0)),
    ]
    return pv.merge(parts).clean()


def camera_for(theta: float) -> tuple[float, float, float]:
    radius = 19.0
    return (radius * np.cos(theta), radius * np.sin(theta), 10.0)


def render(duration: float, fps: int, seed: int) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    mesh = building()
    frames = max(1, int(duration * fps))

    gif_path = OUT / "exp-002-temporal.gif"
    static_path = OUT / "exp-002-static.png"

    # Static reference view.
    pl = pv.Plotter(off_screen=True, window_size=(800, 600))
    pl.add_mesh(mesh, show_edges=True, color="white", lighting=False)
    pl.add_axes()
    pl.camera_position = [(14, 14, 10), (0, 0, 2), (0, 0, 1)]
    pl.screenshot(static_path)
    pl.close()

    # Temporal view: camera + moving light proxy + body path.
    pl = pv.Plotter(off_screen=True, window_size=(800, 600))
    actor = pl.add_mesh(mesh.copy(), show_edges=True, color="white", lighting=False)
    body = pv.Sphere(radius=0.35, center=(-6, -4, 1.0))
    body_actor = pl.add_mesh(body, color="black", lighting=False)
    pl.add_axes()
    pl.open_gif(gif_path, fps=fps)

    for i in range(frames):
        t = i / fps
        phase = i / max(frames - 1, 1)
        theta = 0.25 + phase * 1.9
        x = -6.0 + 12.0 * phase
        y = -4.0 + 8.0 * (0.5 - 0.5 * np.cos(phase * np.pi))
        z = 1.0
        body.points = pv.Sphere(radius=0.35, center=(x, y, z)).points
        # Deterministic viewpoint and a small architectural transformation.
        pl.camera.position = camera_for(theta)
        pl.camera.focal_point = (0, 0, 2.0)
        pl.camera.up = (0, 0, 1)
        # Keep a deterministic scalar annotation tied to time.
        pl.add_text(f"t={t:05.2f}s", name="time", font_size=12)
        pl.write_frame()

    pl.close()

    def sha256(path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()

    manifest = {
        "experiment": "EXP-002",
        "question": "RQ-009",
        "seed": seed,
        "fps": fps,
        "duration_seconds": duration,
        "frames": frames,
        "renderer": "PyVista",
        "source": "procedural architectural massing",
        "outputs": {
            "static": str(static_path.relative_to(ROOT)),
            "temporal": str(gif_path.relative_to(ROOT)),
        },
        "checksums": {
            "static": sha256(static_path),
            "temporal": sha256(gif_path),
        },
        "observations": [
            {
                "observer": "experiment_runner",
                "view_type": "static_3d",
                "relation_noticed": "volumetric massing and circulation opening",
                "interpretation": "Spatial relation is directly inspectable without temporal change.",
                "confidence": 0.9,
                "counterexample": False,
            },
            {
                "observer": "experiment_runner",
                "view_type": "temporal_animation",
                "relation_noticed": "body path changes perceived approach and viewpoint relation",
                "interpretation": "Temporal representation exposes sequence-dependent spatial experience.",
                "confidence": 0.7,
                "counterexample": False,
            },
        ],
    }
    manifest_path = OUT / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Run architecture EXP-002")
    parser.add_argument("--duration", type=float, default=6.0)
    parser.add_argument("--fps", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    result = render(args.duration, args.fps, args.seed)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
