"""
Extract the eight curated figures from the executed notebook
into report/figures/ as PNG files.

Re-run after any change that affects a figure.

Usage:
    cd report && python3 extract_figures.py
"""
import base64
import os
import sys
import nbformat

ROOT = os.path.dirname(os.path.abspath(__file__))
NOTEBOOK = os.path.join(ROOT, "..", "gas_welfare_analysis.ipynb")
FIG_DIR = os.path.join(ROOT, "figures")

# (notebook cell index, output filename, short description)
FIGURES = [
    (10, "fig01_prewar_eq.png",                "Pre-war European gas market equilibrium"),
    (13, "fig02_supply_shock.png",             "Supply shock: pre-war vs post-shock equilibrium"),
    (16, "fig03_norway_ps.png",                "Norwegian producer surplus, before and after"),
    (19, "fig04_price_volume_decomp.png",      "Price effect vs volume effect"),
    (24, "fig05_consumer_cv.png",              "Household compensating variation"),
    (30, "fig06_distributional.png",           "Distributional incidence: who gains and who loses"),
    (47, "fig07_2d_heatmap.png",               "Net welfare across demand elasticity and shock magnitude"),
    (49, "fig08_distributional_sensitivity.png","Distributional sensitivity to shock magnitude"),
]


def main() -> int:
    if not os.path.isfile(NOTEBOOK):
        print(f"Notebook not found: {NOTEBOOK}", file=sys.stderr)
        return 1
    os.makedirs(FIG_DIR, exist_ok=True)

    nb = nbformat.read(NOTEBOOK, as_version=4)
    written = 0
    for idx, fname, desc in FIGURES:
        if idx >= len(nb.cells):
            print(f"  SKIP cell {idx} ({fname}): index out of range", file=sys.stderr)
            continue
        cell = nb.cells[idx]
        png_b64 = None
        for out in cell.get("outputs", []):
            data = out.get("data") or {}
            if "image/png" in data:
                png_b64 = data["image/png"]
                break
        if png_b64 is None:
            print(f"  SKIP cell {idx} ({fname}): no image/png output. "
                  f"Re-execute the notebook first.", file=sys.stderr)
            continue
        out_path = os.path.join(FIG_DIR, fname)
        with open(out_path, "wb") as fh:
            fh.write(base64.b64decode(png_b64))
        size_kb = os.path.getsize(out_path) / 1024
        print(f"  wrote {fname:42s}  {size_kb:6.1f} KB  — {desc}")
        written += 1

    print(f"\n{written}/{len(FIGURES)} figures written to {FIG_DIR}")
    return 0 if written == len(FIGURES) else 2


if __name__ == "__main__":
    sys.exit(main())
