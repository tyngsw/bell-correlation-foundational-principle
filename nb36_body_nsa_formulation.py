#!/usr/bin/env python3
# =====================================================================
# nb36_body_nsa_formulation.py
#
# Reconstructs the body NSA formulation (from math_paper.tex, a separate
# project file confirmed via prior-session records) and connects it to the
# tower / NSA bridge of nb34-nb35.  This nb is the "(i)" task: the body
# notes nb35 was waiting for do NOT exist as nb files in THIS project; the
# definitions live in math_paper.tex.  Recorded here so the bridge no
# longer depends on an absent file.
#
# ------------------------------------------------------------------
# BODY NSA DEFINITIONS (verbatim structure from math_paper.tex).
# ------------------------------------------------------------------
#   eps in *R : fixed positive infinitesimal "lattice spacing".
#
#   Definition (Infinitesimal order).
#       ord(f) := min{ k in N_0 : st(f / eps^k) != 0 },  ord(0):=inf.
#       f is "measurable" iff ord(f) < inf.
#       If f = c eps^n + O(eps^{n+1}), c real nonzero, then ord(f)=n.
#       Standard (non-infinitesimal) quantities have ord = 0.
#
#   Definition (Measurement map).
#       M(f) := st( f / eps^{ord(f)} )  in R.
#
#   Remark (analogy with differentiation).
#       f'(x) = st( (f(x+eps)-f(x))/eps ): numerator and denominator both
#       infinitesimal, ratio finite. Likewise lambda_1 and eps^2 are both
#       infinitesimal but lambda_1/eps^2 is finite.
#
#   Lemma (orders of basic quantities), Bell-correlation framework:
#       (i)   ord(C(theta)) = 0 for theta != pi/4;  C(theta) = -cos(theta);
#             M(C) = C = -cos(theta).
#       (ii)  ord(D(theta)) = 0;  D(theta) = -log|C(theta)|;  M(D)=D.
#       (iii) ord(lambda_1) = 2     [lambda_1 = L^d (L^2-1)/(12 xi^2) * eps^2].
#
#   Sealed (meaning-B): assigning eps a physical NUMERIC scale fails;
#   st(eps)=0, only ratios survive. eps is an ordinal grading device.
#
# ------------------------------------------------------------------
# BRIDGE TO nb34/nb35 (the open question from nb35, now answered).
# ------------------------------------------------------------------
# nb35 found: the rank tower COUNTS spectral modes but does not ORDER them
# (rank is permutation-invariant in the frequencies); an external integer
# ordering was needed to identify "minimal zero = standard-part cut".
#
# ord IS that ordering.  A graded correlation
#       g(t) = c0 + c1 eps cos(w0 t) + c2 eps^2 cos(w1 t) + ...
# has ord(k-th mode) = k, and M reads out one mode per order:
#       M at order k = st( g_k / eps^k ) = the k-th mode.
# So "one rank unit = one mode" (nb34) becomes "one ord level = one
# measured mode" (body NSA).  The minimal-zero cutoff at rank (n-1) is the
# truncation that keeps ord <= (n-1)-worth of modes; higher-ord modes are
# killed by st -- exactly the standard-part cut.
#
# HONEST CAVEAT.  ord ranks modes by WHICH POWER OF eps CARRIES THEM. That
# assignment (which physical quantity sits at which eps-power) is a
# MODELLING CHOICE in the body, not forced by rank alone. The bridge
# therefore closes CONDITIONALLY: given the body's ord-assignment of modes,
# minimal-zero = standard-part truncation. It is NOT an unconditional
# theorem. This keeps us clear of overclaiming.
#
# RECONCILING THE TWO KERNELS.
#   Body:  C(theta) = -cos(theta)   (single cosine, power one).
#   Paper: E         =  cos(2 delta) (single cosine).
#   Both are single-harmonic, rank-2 stationary kernels; they differ by
#   delta = theta/2 (reparametrisation) and an overall sign (anti-
#   correlation). So at the BASE level (ord structure of the kernel) they
#   agree: rank 2, one harmonic, ord 0 for the kernel away from pi/4. The
#   tower's higher levels match higher-ord body quantities (e.g. lambda_1
#   at ord 2).
#
# Conventions per handoff B-section (no I=0; window [-m,m], m=min F_eps;
# no R<=>C equivalence). No string-theoretic content claimed.
# =====================================================================

import sympy as sp

eps = sp.symbols('epsilon', positive=True)
t = sp.symbols('t', real=True)
theta = sp.symbols('theta', real=True)
c0, c1, c2 = sp.symbols('c0 c1 c2', real=True, positive=True)
w0, w1 = sp.symbols('w0 w1', positive=True)


def st(expr):
    return sp.limit(expr, eps, 0)


def ord_of(f, kmax=6):
    for k in range(kmax + 1):
        if st(f / eps**k) != 0:
            return k
    return sp.oo


def measure(f):
    k = ord_of(f)
    return st(f / eps**k)


print("=" * 66)
print("Body NSA formulation + bridge to the tower   (nb36)")
print("=" * 66)

# --- reproduce the body Lemma (orders) ---
print("\nLemma (orders), reproduced:")
C = -sp.cos(theta)
print(f"  (i)  ord(C)=ord(-cos theta) = {ord_of(C)};  M(C) = {measure(C)}")
lam1 = c0 * eps**2          # lambda_1-like, living at eps^2
print(f"  (iii) ord(lambda_1 ~ c0 eps^2) = {ord_of(lam1)};  M = {measure(lam1)}")

# --- ord supplies the missing ordering (nb35 -> closed conditionally) ---
print("\nord ranks the graded modes (answers nb35's open question):")
modes = [c0, c1 * eps * sp.cos(w0 * t), c2 * eps**2 * sp.cos(w1 * t)]
names = ["constant c0", "c1 eps cos(w0 t)", "c2 eps^2 cos(w1 t)"]
for nm, md in zip(names, modes):
    print(f"  ord({nm}) = {ord_of(md)};  M = {measure(md)}")
print("  => integer ord = the external ordering nb35 required.")

# --- measurement reads out one mode per order ---
g = sum(modes)
print("\nMeasurement reads out one mode per order from")
print("  g(t) = c0 + c1 eps cos(w0 t) + c2 eps^2 cos(w1 t):")
for k in range(3):
    lower = sum(modes[:k])
    readout = st((g - lower) / eps**k) if k > 0 else st(g)
    print(f"  order {k}: M = {sp.simplify(readout)}")

# --- base-level kernel reconciliation ---
print("\nBase-level reconciliation of the two kernels:")
delta = sp.symbols('delta', real=True)
E_paper = sp.cos(2 * delta)
C_body = -sp.cos(theta)
print(f"  paper kernel  E = cos(2 delta)   -> ord = {ord_of(E_paper)}")
print(f"  body kernel   C = -cos(theta)    -> ord = {ord_of(C_body)}")
print("  both single-harmonic rank-2 kernels; delta=theta/2 + sign.")

print("\nStatus: bridge CLOSES CONDITIONALLY on the body's ord-assignment")
print("of modes (a modelling choice, not forced by rank). Given it,")
print("minimal-zero cutoff = standard-part truncation. No unconditional")
print("theorem is claimed; no string content; eps stays a formal ordinal")
print("grade (clear of sealed meaning-B).")
print("\nNOTE: the body definitions live in math_paper.tex (separate file),")
print("not in this project's nb1-35. nb35's TODO to 'await body nb42/43/52'")
print("referenced files that do not exist; superseded by this nb36.")
