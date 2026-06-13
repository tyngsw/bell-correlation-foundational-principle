# CHANGELOG

Bell-correlation / emergent-geometry project. TeX deliverables:
`physics.tex` (Part I), `math.tex` (Part II), `preamble.tex` (shared),
`paper_combined.tex` (standalone rank-two companion paper).

Format: reverse chronological. Dates ISO. "companion" = paper_combined.

-----

## [2026-06-13] — Inverse problem, harmonic tower, external-input study

### Added
- **preamble.tex** (new file). Shared preamble that `physics.tex` and
  `math.tex` `\input` but which had never been committed (only a throwaway
  stub existed). Defines: unified theorem numbering across both parts;
  status labels (`\established`, `\conditional`, `\deferred`, `\TODO`); NSA
  symbols (`\st`, `\ord`, `\stR`, `\eps`, measurement `\Meas`); the
  categorical chain `\Ccorr`→`\Cdist`→`\Cact`→`\Ceq`; body macros (`\RR`,
  `\ZZ`, `\Cmat`, `\dent`, `\Tcirc`=torus, `\Scirc`=circle, `\LamQCD`,
  `\Eang`=angular correlation E). Verified by bidirectional `xr` build on
  the real files (physics 10pp / math 10pp, 0 errors, 0 undefined refs).
- **math.tex**: Remark 2.5 (`rem:st-ordering`) — records the spectral-mode
  ordering as an external input, alongside dimension (`rem:st-limits`) and
  commutation relations (`rem:st-algebra`). st via `ord` gives an integer
  ordering, but the rank only counts modes, so the order assignment is a
  modelling input.
- **math.tex**: Remark 7.3 (`rem:extremal-2sqrt2`) — the Tsirelson value
  2√2 as the extremum of CHSH under the commutator bound, given only the
  ±1 spectrum (B3); the value is downstream of B3. Explicitly does not
  weaken `thm:noncomm` (B3 gives the bound; the noncommutativity itself
  stays the independent datum).
- **math.tex**: two conditional remarks bridging the rank-two rigidity
  (`prop:nophase`) to the companion paper's graded tower (`rem:tower`,
  `rem:tower-nsa`); bibitems for the companion paper and Cheung et al.
- **companion (paper_combined.tex)**: Proposition that the product-identity
  RHS is intrinsic Gram cofactors (closes Outlook iv); §5.4 inverse problem
  (circle from a minimal rank-two zero); §5.5 graded harmonic tower; §5.6
  bridge to the body programme; §5.7 depth m vs surplus (sign of m governs
  definability); prior-work paragraph + bibitems for Le–Meroni–Sturmfels–
  Werner–Ziegler (arXiv:2111.06270) and Cheung et al. (arXiv:2508.09246).

### Changed
- **physics.tex, math.tex**: bibliography unification (deferred from a
  prior session):
  - `emergentdist2025` → v2 title "Emergent distance and metricity of
    mutual information in 1D quantum chains" (arXiv:2507.09749);
  - `persistenthom` → add B. Olsthoorn, Phys. Rev. B **107**, 115174 (2023);
  - `entdist-states` → add Vesperini, Bel-Hadj-Aissa, Franzosi (physics);
  - `finberg` → "proves" changed to "argues" (math; pre-review hedge).
  No scientific claim changed.
- **math.tex** Summary/open-problems: enumeration of what `st` does not fix
  now includes mode ordering; the 2√2 sentence refined to "descends partway
  (extremal given B3) while the noncommutativity stays independent".
- **companion** Outlook items (i) and (iv) rewritten to point at the new
  propositions (surplus dichotomy; product identity as Gram data).

### Fixed
- `\Tcirc`/`\Scirc` corrected to `\mathbb{T}`/`\mathbb{S}` (used with
  superscripts, e.g. `\Tcirc^{3}`); the earlier `T^{\circ}` guess produced
  "double superscript".
- Added the `principle` theorem environment used by `physics.tex`.

### Notes
- No string-theoretic content is claimed anywhere; the Cheung et al.
  template is used only as a logical analogy. Outputs are Bell
  correlations, not amplitudes.
- Conventions throughout: window [−m, m] with m = min_eps F_eps; the
  notation I=0 is avoided; no R⇔C equivalence is asserted.
- Build: `physics.tex`, `math.tex` need `preamble.tex` in the same
  directory; both issue their own `\documentclass`. Bootstrap once, then
  run pdflatex twice each to converge bidirectional `xr` refs. `microtype`
  is omitted (container font limitation); restore in a scalable-font env.

-----

## [earlier sessions] — pre-existing state (summary)

- companion: rank-two rigidity of Bell correlations; elliptope boundary
  det G = 0; tensor hierarchy; product identity; bridge (2-setting mutual
  information closed, 3-setting joint absent → 3-point slot undefined).
- Part I (physics): correlation→distance→MDS construction; entanglement
  distance d = −log|C|; spatial dimension three as an external input
  (`thm:dim`); isotropy from the given correlation; SO(3); covering.
- Part II (math): standard-part measurement; spectral/MDS recovery;
  upstream analysis of the Tsirelson bound (saturation quality on-the-given
  vs value); noncommutativity as an independent datum (`thm:noncomm`);
  no phase transition (`prop:nophase`); mass-gap positivity (conditional,
  H1); SU(3) Wilson (conditional/deferred); three-layer Lorentz emergence.
- For full per-statement status see `external_inputs_inventory.md`.
