#!/usr/bin/env python3
# =====================================================================
# nb35_nsa_bridge_exploratory.py
#
# EXPLORATORY (no body notes loaded yet). Tests whether the hypothesis
#   "minimal zero (rank-(n-1) cutoff)  =  standard-part truncation
#    st(f / eps^n)"
# closes logically, and whether it stays clear of the SEALED meaning-B
# (giving eps a physical numeric scale; killed by st(eps)=0, Nb52/Nb63).
#
# CONTEXT (from prior sessions, to be reconciled with body notes later):
#   Body NSA: measurement M(f)=st(f/eps^n); eps infinitesimal; eps^2 != 0
#   keeps the noncommutative bracket alive; st(eps)=0; eps grades by
#   INTEGER order n. Numeric scaling of eps is sealed.
#   This paper's tower (nb34): rank(G_n)=2K+[a0!=0]; modes indexed by
#   FREQUENCY omega_k (continuous); each mode = one rank unit.
#
# FINDINGS.
#   (1) Writing the correlation as an eps-graded hyperfinite sum
#         g(t) = a0 + sum_k eps^k a_k cos(omega_k t),
#       the grade-n readout st((g - lower grades)/eps^n) extracts EXACTLY
#       one mode. So "one grade <-> one mode" matches "one rank unit <->
#       one mode": the minimal-zero cutoff and the standard-part cutoff
#       are the SAME operation (high grades / high harmonics both die).
#   (2) BUT the rank tower COUNTS modes without ORDERING them: rank is
#       invariant under permuting which frequency is called mode 1,2,....
#       The eps-grade needs an integer order, so the map
#       omega_k -> grade-k requires an EXTERNAL ordering principle (freq
#       magnitude, or a dynamical/energy order from the body model, or
#       order-of-appearance as settings grow).
#   (3) That ordering is ORDINAL: eps stays formal, amplitudes a_k carry
#       the content, no numeric scale is assigned to eps. Hence the bridge
#       does NOT re-enter the sealed meaning-B.
#
# STATUS: hypothesis closes UP TO one external input (mode ordering).
# RESOLVED in nb36: the body's infinitesimal order ord(f)=min{k:st(f/eps^k)
# !=0} supplies that ordering. Body NSA definitions live in math_paper.tex
# (a separate project file), not in this project's nb1-35; an earlier draft
# referenced nonexistent body "nb42/43/52" (superseded by nb36).
#
# Conventions per handoff B-section (no I=0; window [-m,m], m=min F_eps;
# no R<=>C equivalence). No string-theoretic content claimed.
# =====================================================================

import sympy as sp
import numpy as np
import itertools

eps = sp.symbols('epsilon', positive=True)   # formal infinitesimal
t = sp.symbols('t', real=True)

print("=" * 66)
print("NSA bridge (exploratory): minimal zero  =?  st truncation  (nb35)")
print("=" * 66)

# ---------------------------------------------------------------------
# (1) eps-graded readout extracts one mode per grade.
# ---------------------------------------------------------------------
a = sp.symbols('a0:5', real=True)
w = sp.symbols('w1:5', positive=True)
K = 3
g = a[0] + sum(eps**k * a[k] * sp.cos(w[k-1]*t) for k in range(1, K+1))
print("\n(1) graded correlation g(t) = a0 + sum_k eps^k a_k cos(w_k t)")
for n in range(0, K+1):
    lower = a[0] + sum(eps**k*a[k]*sp.cos(w[k-1]*t) for k in range(1, n))
    readout = (g.subs(eps, 0) if n == 0
               else sp.limit((g - lower)/eps**n, eps, 0))
    print(f"    st-readout grade n={n}:  {sp.simplify(readout)}")
print("    => each grade yields exactly ONE mode (cf. one rank unit/mode).")

# ---------------------------------------------------------------------
# (2) rank counts modes but does not order them.
# ---------------------------------------------------------------------
def gram(gfun, xs):
    n = len(xs)
    return np.array([[gfun(xs[i]-xs[j]) for j in range(n)] for i in range(n)])

def numrank(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > tol*s[0]).sum())

rng = np.random.default_rng(0)
freqs = [1.3, 2.9, 5.1]
print("\n(2) rank is invariant under permuting the mode labels:")
for perm in list(itertools.permutations(freqs))[:3]:
    gg = lambda u, perm=perm: sum(np.cos(wk*u) for wk in perm)
    xs = rng.uniform(0, 3, 7)
    print(f"    freq order {perm}: rank = {numrank(gram(gg, xs))}")
print("    => omega_k -> grade-k needs an EXTERNAL ordering principle.")

# ---------------------------------------------------------------------
# (3) the ordering is ordinal; eps stays formal (no numeric scale).
# ---------------------------------------------------------------------
print("\n(3) st(eps)=0 so eps carries no numeric content; the grade is an")
print("    ordinal label and amplitudes a_k carry the physics.  This is")
print("    distinct from the sealed meaning-B (eps as a physical scale),")
print("    so the bridge does not re-enter the sealed region.")

print("\nStatus: hypothesis closes up to ONE external input (mode ordering).")
print("RESOLVED in nb36: the body's infinitesimal order ord(f) supplies")
print("that ordering (integer ord = eps-power carrying each mode), so the")
print("bridge closes CONDITIONALLY on the body's ord-assignment of modes.")
print("\nNOTE: the body NSA definitions live in math_paper.tex (a separate")
print("project file), NOT in this project's nb1-35. An earlier draft of")
print("this TODO referenced body 'nb42/43/52' to be uploaded; those nb")
print("files do not exist in this project. See nb36 for the reconstruction")
print("from math_paper.tex and the bridge closure.")
