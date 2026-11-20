#!/usr/bin/env python3
"""Read-only standard-library validator for the NEON STAGE asset manifest."""
import argparse, hashlib, json, struct, sys
from pathlib import Path

EXPECTED_CONTROLS = {"ampGain","eqHigh","eqMid","eqLow","velocity","dynamics","swing","humanize","accent"}
EXPECTED_FX = {"compressorOn","eqOn","distortionOn","chorusOn","delayOn","reverbOn","cabinetOn"}
EXPECTED_STATES = {"normal","hover","pressed","active","disabled"}

def png_info(path):
    data = path.read_bytes()
    if len(data) < 26 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG header")
    width, height, depth, colour = struct.unpack(">IIBB", data[16:26])
    return width, height, (colour in (4, 6) or b"tRNS" in data)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--repo-root", type=Path, default=None)
    args = ap.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    root = (args.repo_root or args.manifest.resolve().parent.parent).resolve()
    errors, warnings = [], []
    if data.get("skin", {}).get("skin_id") != "skin-053":
        errors.append("skin ID differs from locked skin-053 baseline")
    if {x.get("parameter_id") for x in data.get("controls", [])} != EXPECTED_CONTROLS:
        errors.append("REV.20 parameter ID set mismatch")
    if {x.get("parameter_id") for x in data.get("fx_switches", [])} != EXPECTED_FX:
        errors.append("primary FX parameter ID set mismatch")
    if set(data.get("button_states", [])) != EXPECTED_STATES:
        errors.append("five required button states are not present")
    hashes = {}
    for item in data.get("source_assets", []):
        p = root / item["path"]
        if not p.is_file():
            warnings.append("source not available in checkout: " + item["path"])
            continue
        digest = hashlib.sha1(p.read_bytes()).hexdigest()
        if digest in hashes:
            warnings.append("duplicate file content: %s == %s" % (item["path"], hashes[digest]))
        hashes[digest] = item["path"]
        if p.suffix.lower() == ".png":
            try:
                w, h, alpha = png_info(p)
                if not w or not h: errors.append("zero-sized PNG: " + item["path"])
                print("PNG", item["path"], "%dx%d alpha=%s" % (w, h, alpha))
            except Exception as exc:
                errors.append("PNG inspection failed for %s: %s" % (item["path"], exc))
        if item.get("license_status") != "verified":
            warnings.append("licence not verified: " + item["path"])
    for item in data.get("runtime_assets", {}).get("required", []):
        if item.get("status") == "not_imported":
            warnings.append("runtime asset not imported: " + item["id"])
        elif item.get("path") and not (root / data["runtime_assets"]["root"] / item["path"]).exists():
            errors.append("manifest marks missing runtime asset as imported: " + item["path"])
    for w in warnings: print("WARNING:", w)
    for e in errors: print("ERROR:", e)
    print("RESULT: %d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
