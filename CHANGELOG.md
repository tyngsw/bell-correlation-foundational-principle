# Changelog

All notable changes to this project are documented here. This project is a
clean restart on a clarified foundation; history begins at v0.1.

## [v0.4] — Additional-principle search: sign principle established, (3+1) model constructed

The framework-internal no-go (v0.3) forced a search for principles *outside*
`cos2θ`. Four candidates were evaluated; the search converged onto a single
source for the time/non-compact structure, and a conditional (3+1) model.

### Established (this cycle, notebooks 13–16)
- **Sign principle, covering formulation (nb13).** Of the two formulations of the
  sign principle, the *orientation* form cannot produce a single time on its own
  (the sign-reversal count of `cos2θ` is a structural constant unchanged by
  orientation). The *covering* form — lifting the setting space `S^1` to its
  universal cover `R` and identifying the cover coordinate with time — is
  self-standing: a single topological choice forces time dimension = covering
  rank = 1, restores a transitive causal order (resolving the non-transitivity of
  nb09 L-A), and yields non-compactness simultaneously. It carries no continuous
  parameter (deck group `Z` discrete, fundamental-domain width fixed at the given
  period `2pi`), so it escapes the epsilon-trap that killed the decay principle.
- **Dynamics principle does not break periodicity (nb14).** A fully-connected
  system has no real-space RG scale (effective correlation stays rank-2 at all
  sizes); running `N(mu)` only rescales the amplitude `1/(2N)`, not the angular
  (periodic) structure. Consistent with the main no-go; acts on continuum
  limit/dimension, not on time/non-compactness.
- **Non-pair interaction reduces to the covering principle (nb14).** Within the
  given data (compositions of `cos2`), three-body correlations keep an
  even-order (periodic) Fourier support and do not break the no-go. Breaking
  periodicity requires a non-periodic functional form, whose non-periodicity is
  exactly the `S^1 -> R` covering of nb13. So C-4 is not an independent principle.
- **Spatial dimension 3 is not derivable from the given data (nb15).** `N` does
  not enter dimension; the `4` in `beta*=4N` is a statistical coefficient
  (`2/<cos^2>`), not spacetime dimension 4; the `SO(3)` measurement-axis origin is
  non-circular but rests on the external fact that measurement happens in 3-space.
  Net insight: time and space have different origins — time from the inside of
  the data (the periodicity of `cos2theta`, via covering), spatial dimension from
  the outside (independent settings / measurement axes).
- **(3+1) minimal model `R x T^3` is internally consistent (nb16).** Conditional
  on accepting `p=4`: signature `(3+1)` (time = covering coordinate, 1; space =
  the 6-eigenvalue block of `T^3`'s MDS, intrinsic 3), a globally transitive
  causal order along time, preserved `k*` structure, and non-compactness
  localised to time (space `T^3` compact). All consistent with nb02/04/09/13.

### Discipline / lessons added
- A free continuous parameter makes an addition a tuning knob, not a principle;
  qualitative ("present / absent") structure can be a principle.
- Numerical coincidences (space 3 = colour 3; the 4 of `beta*` = dimension 4) are
  not principles — trace the origin before identifying.
- Classify target features by inside-vs-outside the given data.
- Build composite geometry element-by-element; a single mixed Lorentzian
  embedding splits time into many dimensions (artefact).

### Open (most important)
- **Origin of dimension 4 (nb15/16 open-1).** Why `p=4`? The target `R x T^3` is
  now fixed; the question is purified to "what forces the number of independent
  settings to be 4." This is the next chapter.

## [v0.3] — Main no-go closed (action level); additional-principle search begun

### Established (notebooks 10–12)
- **Mean-field transition (nb10).** Fully-connected signed-`cos2` system has a
  continuous transition at `beta*=4N` (12 for `N=3`), output from the given `N`.
  But the broken-phase effective correlation stays rank-2 / `k=2` (periodic);
  symmetry breaking only selects a direction on the circle.
- **Direct Monte Carlo, all fluctuation orders (nb11, Julia/M4).** At and around
  `beta*` the bath distribution grows only even orders; odd orders stay at the
  noise floor and are `n`-independent under FSS (`n=1000->4000`). `C_eff` is
  exactly rank-2. No non-periodic mode stands up. Verdict (alpha): the main no-go
  is closed at the action level — `cos2theta`'s periodicity is unbroken by
  fluctuations.
- **Additional-principle stage entered; decay principle ruled out (nb12).** The
  target `(3+1)` needs principles outside `cos2theta`. The decay principle
  requires a correlation length `xi` fixed by the given `N` alone; three
  mechanisms all fail (`N` enters only the amplitude, not the angular scale), so
  `xi` stays an external tuning knob -> not a principle.

## [v0.2] — Compactness intrinsic; route-A and lightcone no-go (notebooks 05–09)

- Decompactification attempts collapse back to the circle; compactness is an
  algebraic fact (rank-2 kernel from `(cos2theta, sin2theta)`), independent of
  distance, `st`, and embedding. Lorentzian/causal/curved readings all fail on
  the same periodicity obstruction; sign does make timelike directions but not a
  single one.

## [v0.1] — Clean restart on the Bell-correlation foundation

### Foundation fixed
- **Bell correlations adopted as a foundational principle** (Clauser, Aspect,
  Zeilinger), expressed as `E(theta) = cos(2theta)/(2N)`, with `N = 3` an
  identification with QCD (not a derivation).
- **Measurement = the standard-part map `st`** throughout, in the graded form
  `M(f) = st(f / eps^ord(f))`. Bell measurement is itself an instance of this `st`.
- **The graph is the support of the correlation matrix, not a spatial lattice.**
  Vertices are measurement settings; spatial geometry is an output (via MDS),
  not an input. No rectangular spacetime lattice is used as the substrate.

### Notes on conventions
- README, CHANGELOG, and code comments: English.
- Notebook prose: Japanese.
- Every claim is labelled established / in progress / open; no claim is upgraded
  beyond what is demonstrated.

### License
- Released under the MIT License.
