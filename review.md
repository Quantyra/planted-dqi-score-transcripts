# Manuscript review and reproducibility

This preprint received automated model review. Each reviewer was given the full manuscript. The technical checks below were also run directly from the repository.

## Scope and attribution

The main contribution is a total-variation estimate uniform over score settings on one randomly drawn table. It applies to stopped adaptive score histories for both the null law and a fixed plant. At the chosen degree, the prior DQI moment theorem guarantees the zeroth moment. Bazzi's fixed binary linear code and random coset do not model independently conditioned half-field lists. The manuscript credits the DQI score basis, the binomial moment comparison, prior optimization-quality screens and the power-sum interpolation count. The literature comparison supports a separate note. Priority beyond the sources checked is open. [Jordan et al.](https://arxiv.org/abs/2408.08292) · [Gil-Fuster et al.](https://arxiv.org/abs/2607.28120) · [Bazzi](https://arxiv.org/abs/1408.5681) · [Mazumder and Niroula](https://arxiv.org/abs/2610.06753) · [Childs et al.](https://doi.org/10.4230/LIPIcs.ICALP.2016.16)

## Review dispositions

The initial mathematical draft had SHA-256 66392c627eaf598a4db0a14657c1aae6ccb4849b136b7efa2c20cb18cce8fdbd. The two bounds involving multiple shots refer to fresh preparations on one table. No claim is made about coherent attacks, retained assignment labels, or algorithms that inspect the table.

- **Claude, proof and quantifiers.** Requested a concrete nonvacuous regime, explicit fresh-shot scope and clearer labeling of the small-field experiment. The revised proof gives a sufficient cutoff \(k\ge2048\), uses ensemble probability in the theorem, and labels the off-scaling check. The suggested replacement of \(4^{3(k-1)}\) by \(4^k\) did not account for patterns with \(k\le u\le3(k-1)\); the proof retains the larger factor. Claude rechecked the changes and returned PASS.
- **AGY, costs and reproducibility.** Returned PASS on the score-only observation model, adaptive coupling and reference sampler's precision costs. The revision lists all four active colors. The suggested example cutoff \(k=16\) is unsupported by the displayed constants; the paper gives the proved sufficient cutoff instead. AGY rechecked the cutoff and the revised scope and returned PASS.
- **Grok, priority and adversarial scope.** Returned REVISE with no fatal error or prior implication identified. Its requested revisions appear in the final text: the polynomial-shot assertion explicitly takes a limit, the two-ensemble bound is capped at one, and the perfect-fit probability is stated pointwise. The sufficient cutoff is explicit. We checked its objection at \(q=8\) by rational arithmetic: the log-density upper bound is \(8/7+8/3=80/21<4\). The paper now displays this calculation.

**Disposition for preprint preparation.** The requested substantive changes have been resolved. The final scientific source has SHA-256 bf8690719a82d2d35a3e10dc94a17d5257191716e301dcddf6f4d5e80c680613. The PDF has SHA-256 efa293e1bfd7404693de7906d971835670a4f1c3c1da98cc4ce76bdeecf965bd. These are manuscript reviews and arithmetic checks; formal certification and journal peer review are separate.

## Exact checks

Both standard-library scripts passed. The pair checker reconstructed the entire joint histogram for 1,296 null tables and for 81 planted tables under each of two fixed plants. The witness checker enumerated 4,096 assignments at \((q,k)=(8,4)\) and 256 at \((16,2)\), on three tables per parameter pair. At \((256,4)\) it obtained threshold 221 and expected witness counts \(1.13363\times10^{-25}\) (null) and \(1.12586\times10^{-25}\) (planted competitors) by exact rational summation. The two scale-free identities and the asymptotic theorem have different evidence.

The five-page PDF builds with Tectonic 0.17.0 and a fixed timestamp. An independent clean build reproduced its bytes. Citation metadata passed the CFF 1.2 schema. The Lean certification plan is prospective, with zero current formal coverage.
