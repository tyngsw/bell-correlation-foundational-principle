# TeX skeleton — Bell Correlation as a Foundational Principle

Two-part write-up, per README §7 (TeX holds only established statements;
notebooks hold exploration and verification).

## Files
- `preamble.tex` — shared: theorem environments (one numbering scheme across
  both parts), status labels (`\established` / `\conditional` /
  `\deferred` / `\TODO`), symbol macros.
- `physics.tex` — Part I (Physics): emergent spacetime.
- `math.tex` — Part II (Mathematics): st-measurement, spectral geometry, mass gap.

## Build
Standard pdflatex via latexmk. **Compile `physics` first**, then `math`
(math.tex pulls Part I labels via `xr` / `\externaldocument`):
```
latexmk -pdf physics.tex
latexmk -pdf math.tex
```

## Status labels (visible in the PDF)
- **[established]** — proven/verified, ready to write up.
- **[conditional]** — holds under a stated hypothesis (e.g. mass gap under (H1)).
- **[TODO: ...]** — section body still to be written (red in PDF).

## Section ↔ notebook map
Physics
- §2 no-go ← nb10–11, analytic nb22
- §3 covering II ← nb13
- §4 R×T³ ← nb16, nb18
- §5 SO(3) emergence ← nb19, nb20
- §6 dimension external ← nb15, nb17, nb21

Mathematics
- §1 st measurement ← README §2c, nb17
- §2 MDS geometry ← nb01, nb04, nb16, nb18
- §3 mass gap ← README §3 (conditional, H1)
- §5 climbing map ← nb21

## Next
Fill TODO bodies section by section, promoting only established results.
Mass gap and SU(3) remain conditional until (H1) and the Wilson-action
derivation are firmed up.
