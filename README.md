# Adaptive score measurements in decoded quantum interferometry on planted polynomial lists

Daniel Fredriksen, Quantyra Inc. · [Manuscript PDF](manuscript.pdf) · [LaTeX source](manuscript.tex) · [ORCID](https://orcid.org/0009-0002-9123-7435)

Version 1.0.0 was published on November 20, 2026. [Cite this version](https://doi.org/10.5281/zenodo.24407287) · [All versions](https://doi.org/10.5281/zenodo.24407286)

Can a sequence of ordinary decoded quantum interferometry (DQI) scores reveal a planted polynomial even when the algorithm almost never measures the polynomial itself? On the random low-rate balanced-list family studied here, every score-only policy using polynomially many fresh shots has negligible distinguishing advantage. The experiment retains one table across the whole transcript and allows the observer to change the degree weights after every score.

The preprint gives an explicit total-variation bound and a separate sharp probability for observing a unique high-scoring witness. Access to the written table, coefficient labels and joint register measurements poses different questions.

## Reproduce the exact checks

Run the following from the repository root with Python 3.10 or later. The scripts use only the standard library. Use ordinary Python with assertions enabled.

~~~sh
python checks/score_pairs.py
python checks/witness_count.py
~~~

The first checks all 1,296 null tables over the four-element field and 81 planted tables for each of two plants. The second checks six example tables and computes exact witness first moments at \(q=256,k=4\). Printed decimal approximations summarize exact rational computations. Both programs exit unsuccessfully on a failed assertion. Finite checks are diagnostics for the proof.

## Build and certification

Build the PDF with Tectonic 0.17.0 using the command below. Set the environment variable SOURCE_DATE_EPOCH to 1795132800 for the included build timestamp.

~~~sh
tectonic manuscript.tex
~~~

The release candidate includes the PDF, source, checks and metadata. [Review disposition](review.md) · [Lean certification plan](lean-certification-plan.md)

The manuscript and accompanying materials are available under [CC BY 4.0](LICENSE).
