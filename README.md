# Bell Correlation as a Foundational Principle: Spacetime Emergence and Universal Action

Reconstructing spacetime geometry, SU(3) Yang–Mills theory, and the mass gap
from **Bell correlations adopted as a foundational principle**, using
**non-standard analysis** and the **standard-part map** as the universal model
of measurement.

> **Status:** This repository is a clean restart on a clarified foundation.
> Earlier material (notebooks and TeX from the predecessor project) is **not**
> carried over and is **not** to be referenced. Everything is rebuilt and
> re-verified from the foundation described below.

---

## 1. The foundational principle

The experimentally established **Bell correlations** of Clauser (1972),
Aspect (1982), and Zeilinger *et al.* (Nobel Prize 2022) are **adopted as a
first principle** — not derived, not modelled, but taken as the empirical
given on which everything else is built.

The correlation is written

```
E(θ) = cos(2θ) / (2N),     with N = 3  ⇒  E(θ) = cos(2θ)/6.
```

- `N = 3` is an **identification with QCD**, *not* a derivation. We never write
  "N = 3 is derived."
- The functional form `cos(2θ)` is, in the present (maximal) working stance,
  part of the adopted principle. A later goal is to climb from a minimal
  principle (the mere existence of a Bell-inequality-violating correlation) up
  to this full form (see §5).

## 2. Method: three pillars

**(a) Correlation → distance.** The entanglement distance is

```
d = − log |C|,
```

with `C` the Bell correlation. This converts the empirical correlation into a
metric quantity.

**(b) The graph is the support of the correlation matrix — not a spatial
lattice.** Vertices are **measurement settings** (e.g. angles θ on a
hyperfinite partition of the setting space), and edge data are the
correlation/distance values between settings. The graph carries the
correlation data; it is **not** a pre-given lattice of space points. Spatial
geometry is an **output** (via multidimensional scaling on the correlation
matrix), never an input. We do **not** adopt a rectangular spacetime lattice as
the substrate.

**(c) Measurement = the standard-part map `st`.** All measurement is modelled
as the standard part of a non-standard quantity. Concretely, a graded
measurement

```
M(f) = st( f / ε^ord(f) )
```

is used, where `ε > 0` is a positive infinitesimal lattice spacing (in the NSA
sense, with `ε² > 0`) and `ord(f)` is the infinitesimal order of `f`. Bell
measurement itself is an instance of this single `st`. Non-near-standard
quantities (e.g. where the correlation distance becomes unlimited at
`cos 2θ = 0`) fall outside the standard category and are thereby excluded
automatically.

## 3. Main claims (each to be (re-)verified from scratch)

- **Mass gap** `Δ = ℏc/ξ = Λ_QCD ≈ 200 MeV > 0`, under hypothesis (H1) that the
  Bell two-point function is the Euclidean Yang–Mills two-point function. The
  argument uses the Bell-derived transfer operator, the Jentzsch–Perron theorem
  (strict positivity of the kernel, `T ≥ 1 > 0`), and the transfer principle.
  The positivity `Δ > 0` is the mathematical result; the value `Λ_QCD` is an
  empirical input via `ξ`. **The argument is lattice-independent** (it lives on
  the continuous/hyperfinite space of measurement settings, not on a spacetime
  lattice).
- **Emergent spatial geometry** from the correlation matrix via multidimensional
  scaling (MDS), with reconstruction of spatial coordinates.
- **Universal action** `S = −β Σ e^(−d)`, whose minimisation is intended to be
  equivalent to maximum-likelihood estimation and to geodesics in the
  entanglement metric.
- **SU(3) gauge structure** from the colour-singlet qutrit correlation
  `E(θ) = cos(2θ)/6`, yielding a Wilson action.

Each item is marked, in the notebooks and TeX, as **established / in progress /
open**. No claim is upgraded beyond what is shown.

## 4. What this framework does *not* claim

- It does **not** derive `N = 3` (QCD identification only).
- It does **not** adopt a rectangular spacetime lattice as the substrate.
- It does **not** treat the emergent dimension as assumed; integer-dimensionality
  is a property to be exhibited via `st`, not put in by hand.
- It does **not** claim the value `Λ_QCD`; only its positivity is derived.

## 5. Research strategy (two stages)

1. **Maximal stance first.** With `cos 2θ` taken as the entry point, determine
   the **minimal set of additional principles** needed to reconstruct current
   physics (spacetime dimension, SU(3), mass gap), and map their dependencies.
2. **Then climb down.** Once the map is complete, investigate whether `cos 2θ`
   itself (and the quantitative facts such as the Tsirelson bound) can be
   obtained from a **minimal principle** — ideally just the existence of a
   Bell-inequality-violating correlation — via the `st` structure.

## 6. Repository layout

```
README.md        — this file
CHANGELOG.md     — versioned record, starting at the clean restart (v0.1)
notebooks/       — Jupyter notebooks (Japanese prose), numbered from 01
                   01: Bell correlation → distance d = −log|C| → correlation
                       matrix → emergent space via MDS
TeX              — NOT included yet. A fresh TeX will be written at a later
                   stage. Until then, the predecessor TeX is consulted only as
                   needed and is not committed here. After the new TeX exists,
                   neither the old TeX nor old notebooks are to be referenced.
```

## 7. TeX vs. notebooks

TeX is the place for **carefully established** statements only. The
**notebooks** hold the background, exploration, and numerical/symbolic
verification behind those statements. A result is promoted into TeX only once it
is solid.

## 8. Open problems (provisional; to be re-confirmed)

- Whether the additional principles needed for `(3+1)` dimensions are truly
  minimal and mutually independent.
- Whether `cos 2θ` / the Tsirelson bound can be obtained from a minimal
  principle (Stage 2 of §5).
- The numerical factor `≈ 7.5` between `Λ_QCD` and the lightest glueball mass.

## Author

T. Yanagisawa — Independent Researcher, Japan.

## License

Released under the MIT License. See [`LICENSE`](LICENSE) for details.
