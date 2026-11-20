# Lean certification plan

**Target.** Theorem 1, Lemma 2 and Proposition 3 of the manuscript, with fixed-table, random-table and adaptive probabilities distinguished. Current formal coverage is zero. PaperMill owns prospective certification. An accepted declaration requires a kernel-checked proof against the pinned statement, an allowed-axiom audit, and a comparison to the mathematical claim.

| Gate | Statement to formalize | Acceptance test |
|---|---|---|
| C1. Finite pattern lemma | For two colored pattern laws on finitely many rows with identical restrictions through order \(k\), one an independent row law with activity \(\rho\), their full \(\ell_1\) distance is at most \(2(2^k+1)\binom qk\rho^k\). | Prove the colored Bonferroni remainder and both tail bounds. Check truncation at \(r=k-1\). |
| C2. Row kernel and exceptional patterns | For the actual table laws and fixed plant, prove the conditional product kernel for hits, its mass bound, the union-of-roots cap \(3(k-1)\) and the \(3q^{-k}B^2\) term. | Instantiate the finite model with balanced subsets and sampled functions. Handle zero-probability patterns without dividing by their mass. Discharge field interpolation and denominator assumptions. |
| C3. Pair-to-transcript theorem | Prove the weighted pair estimate, diagonal bound, common envelope, uniform one-step TV bound, and stopped adaptive transcript comparison on a single table. | Recover the explicit finite bound and exceptional-table probability. Keep the table fixed and allow access only to scores and policy coins. |
| C4. Asymptotic and witness corollaries | For \(q=k^4\) and \(2\ell=k\), derive the stated exponent; formalize the Hoeffding estimates, exact peak and shot cost. | Check factorials, threshold strictness, exceptional probability and the witness-specific optimal weights. |

**First bounded action when scheduled.** Spend at most 90 minutes auditing mathlib coverage for finite distributions, inclusion–exclusion and Bonferroni inequalities. State C1 over finite alphabets and attempt the case of one prescribed colored support. Stop and report the missing library lemma if the remainder cannot be derived in that budget. The direct finite-counting proof in the manuscript is the fallback.

Report partial coverage by gate. The efficient sampler additionally needs a bit-cost model and a finite-precision proof before computation can be called certified. Full circuit derivation, literature priority and empirical usefulness fall outside these declarations. Use the lane's existing execution routing, source pins and audit rules.
