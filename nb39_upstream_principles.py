#!/usr/bin/env python3
# =====================================================================
# nb39_upstream_principles.py
#
# Cheung-type search: can the external inputs of the theory be DERIVED
# from an upstream selection principle, in the way Cheung-Remmen-Sciotti-
# Tarquini (arXiv:2508.09246) derive the string amplitude from
# ultrasoftness + minimal zeros, rather than being posited?
#
# We assess each external input (see external_inputs_inventory.md) and run
# the two tractable cases. Two clean outcomes:
#
#  ATTEMPT 1 -- MODE ORDERING: NO derivation (sharpens the external claim).
#     The natural upstream principles -- (a) rate of vanishing under st in
#     eps, (b) detection threshold in number of settings, (c) the ultrasoft
#     analogue (high-frequency decay) -- each constrain only the spectral
#     ENVELOPE (a_k vs omega_k), not the integer LABELLING of individual
#     modes. So mode ordering resists a unique Cheung-type derivation and
#     is genuinely external. (Positive residue: "smoothest kernel of rank
#     two" = single cosine, which only restates nb33.)
#
#  ATTEMPT 2 -- TSIRELSON VALUE 2*sqrt2: YES, from an extremal principle,
#     and it REDUCES to the B3 datum (two-valued/+-1 measurement).
#     Identity for dichotomic observables (A_i^2=B_j^2=1):
#         S = A0(B0+B1) + A1(B0-B1),   S^2 = 4 + [A0,A1][B0,B1].
#     Norm algebra with eigenvalues in [-1,1]:
#         ||[A0,A1]|| <= 2||A0|| ||A1|| <= 2,
#     hence ||S||^2 <= 4 + 2*2 = 8, ||S|| <= 2*sqrt2. The only input is the
#     commutator bound, which follows from the +-1 spectrum = B3. So the
#     2*sqrt2 VALUE is not an independent external input; it is downstream
#     of B3 via a max-CHSH extremal principle (Cheung-style: extremize
#     subject to one constraint).
#
# CAVEAT / relation to math.tex sec:qcorr & thm:noncomm: the body already
# locates the 2*sqrt2 value as external, tied to noncommutativity
# (thm:noncomm, an independent representational datum). The present result
# says that value follows from the +-1 spectrum via norm algebra. These can
# be read as CONSISTENT (both 2*sqrt2 and the relevant commutator bound
# trace back to B3) OR in TENSION (the body calls noncommutativity
# independent). This nb does NOT overwrite the body; it records a candidate
# reduction to be reconciled with thm:noncomm before any TeX change.
#
# No string-theoretic content. Conventions per handoff B-section.
# =====================================================================

import numpy as np

print("=" * 66)
print("Cheung-type search for upstream principles   (nb39)")
print("=" * 66)

# ---------------------------------------------------------------------
# ATTEMPT 1: mode ordering -- show three candidate principles fail to
# order individual modes (they fix only the envelope).
# ---------------------------------------------------------------------
print("\nATTEMPT 1 -- mode ordering")

# (a) st-vanishing rate in eps: deviation of block-average from DC.
print("  (a) st-vanishing rate: 1 - sinc(w*eps) ~ (w eps)^2/6")
print("      leading eps-order is 2 for EVERY w => order not separated by w.")
for w in [1.0, 4.0, 16.0]:
    eps = 1e-3
    dev = 1 - np.sin(w*eps)/(w*eps)
    print(f"      w={w:5.1f}: deviation/eps^2 = {dev/eps**2:.4f}  (coefficient ~ w^2/6={w**2/6:.4f})")

# (b) detection threshold: rank vs settings -- amplitude-driven, a choice.
def gram(g, xs):
    n = len(xs)
    return np.array([[g(xs[i]-xs[j]) for j in range(n)] for i in range(n)])

def numrank(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > tol*s[0]).sum())

print("  (b) detection threshold: rank saturates by amplitude dominance")
freqs, amps = [1.0, 2.7, 5.1], [0.5, 0.3, 0.15]
rng = np.random.default_rng(0)
for n in range(2, 8):
    g = lambda u: sum(amps[k]*np.cos(freqs[k]*u) for k in range(3))
    print(f"      n={n}: rank={numrank(gram(g, rng.uniform(0,3,n)))}")
print("      => order of saturation = amplitude order = still a choice.")

# (c) ultrasoft decay: each pure cosine is entire; decay constrains the
#     envelope, not the label.
print("  (c) ultrasoft decay constrains the envelope a_k vs w_k, not labels.")
print("  CONCLUSION 1: mode ordering resists derivation => genuinely external.")

# ---------------------------------------------------------------------
# ATTEMPT 2: 2*sqrt2 from a max-CHSH extremal principle, reducing to B3.
# ---------------------------------------------------------------------
print("\nATTEMPT 2 -- Tsirelson value 2*sqrt2")
print("  identity: S^2 = 4 + [A0,A1][B0,B1] for dichotomic observables")
print("  norm algebra: ||[A0,A1]|| <= 2||A0|| ||A1|| <= 2  (spectrum in [-1,1])")
print("  => ||S|| <= 2*sqrt2, input = +-1 spectrum = B3.")

def dich():
    n = np.random.randn(3); n /= np.linalg.norm(n)
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    return n[0]*sx + n[1]*sy + n[2]*sz

maxnorm = 0.0
rng2 = np.random.default_rng(1)
for _ in range(30000):
    A0, A1, B0, B1 = dich(), dich(), dich(), dich()
    S = np.kron(A0, B0+B1) + np.kron(A1, B0-B1)
    maxnorm = max(maxnorm, np.linalg.norm(S, 2))
print(f"  numerical max ||S|| = {maxnorm:.4f}   (2*sqrt2 = {2*np.sqrt(2):.4f})")
print("  CONCLUSION 2: 2*sqrt2 follows from an extremal principle given B3;")
print("  candidate reduction of the 2*sqrt2 external input to B3.")
print("  (To reconcile with thm:noncomm before any body-TeX change.)")

print("\nSummary:")
print("  - dim 3, N=3: no-go / out of scope (not attempted).")
print("  - mode ordering: NOT derivable; external status sharpened.")
print("  - 2*sqrt2: derivable from B3 via max-CHSH; candidate input reduction.")
print("  - noncommutativity: linked to the same B3 bound; reconcile w/ thm:noncomm.")
