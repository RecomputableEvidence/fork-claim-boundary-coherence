# Claim Boundaries in AI Evidence Systems

## From Cryptographic Integrity to Governed Inference

**Release:** Fork Claim Boundary Coherence Harness v0.1.1
**Tag:** `v0.1.1-specification-coherence-pass`
**Claim rung:** `SPECIFIED`
**Evaluation scope:** `SPECIFICATION_COHERENCE`
**Result:** `PASS`

---

## Executive Summary

A verified record can still be misused.

A hash can prove that a file has not changed. A manifest can show that an artifact set remains intact. A verifier can report that a packet still recomputes against its declared contents.

But none of that, by itself, prevents someone from saying too much about what the evidence proves.

This paper introduces **claim boundaries**: explicit constraints on what a piece of evidence, verifier, receipt, release, or system state is permitted to establish.

Claim boundaries do not merely say what happened.

They say what cannot be inferred from what happened.

Fork’s v0.1.1 Claim Boundary Coherence Harness demonstrates a narrow but important milestone: claim boundaries can be represented as machine-checkable release controls for a materialized specification stack.

This release does **not** prove that claim boundaries improve reconstruction fidelity. It does **not** validate the broader thesis. It does **not** establish legal, regulatory, institutional, or enterprise sufficiency.

It establishes something narrower:

> Fork Claim Boundary Coherence Harness v0.1.1 executed against the materialized Fork specification stack and produced a bounded specification-coherence `PASS` receipt under the recorded environment.

That boundary is the mechanism.

---

## 1. The Problem: Verification Without Boundary Can Become Overclaiming

Most technical evidence systems focus on preserving artifacts and checking whether they changed.

That is necessary.

Without integrity, reconstruction collapses immediately.

But an integrity result is often narrower than the conclusions people later want to draw from it.

A packet may prove that a model output was recorded.

It does not prove the model was correct.

A workflow event may show that an account clicked or approved something.

It does not prove the natural person behind the account was identified, authorized, or performed meaningful review.

A sealed record may show that a notice was generated.

It does not prove the notice was legally sufficient.

A verification receipt may report `PASS`.

It does not mean every possible claim about the underlying workflow has passed.

This is where evidentiary systems become dangerous if they preserve artifacts without preserving limits.

The failure mode is not only data corruption.

It is semantic expansion.

| Bounded Fact                      | Overclaim                                |
| --------------------------------- | ---------------------------------------- |
| Model output recorded             | Model was correct                        |
| Account activity logged           | Natural person identified and authorized |
| Workflow status set               | Legal sufficiency established            |
| Routing approval marked           | Human judgment performed                 |
| Cryptographic verification passed | Decision correctness proven              |

Claim boundaries are designed to resist this expansion.

---

## 2. What Is a Claim Boundary?

A **claim boundary** is an explicit constraint on what a piece of evidence, verifier, receipt, release, or system state is permitted to establish.

It preserves the distinction between:

| Boundary                                        | Distinction                                       |
| ----------------------------------------------- | ------------------------------------------------- |
| Observation vs. truth                           | Data captured vs. data accurate                   |
| Account activity vs. human identity             | Account action vs. verified natural person        |
| Identity vs. authority                          | Who someone is vs. what they were permitted to do |
| Routing approval vs. substantive approval       | Workflow routing vs. human judgment               |
| Timestamping vs. legal admissibility            | Recorded time vs. legal effect                    |
| Integrity vs. correctness                       | Unchanged vs. correct                             |
| Reconstruction vs. operational replay           | Evidence review vs. system execution              |
| Allegation vs. established fact                 | Claimed vs. proven                                |
| Model recommendation vs. institutional judgment | AI output vs. accountable decision                |
| Checked vs. failed vs. not checked              | Distinct result states                            |

A verified system must preserve not only what its evidence establishes, but also what its evidence does **not** establish.

Without that second half, verification can become a machine-assisted overclaim.

---

## 3. Fork’s Current Hypothesis

Fork’s narrow current hypothesis is:

> Claim boundaries can be represented as machine-checkable controls that govern what a system may claim from its own evidence, releases, and verification receipts.

This is an infrastructure claim.

It is not an empirical victory claim.

The broader research hypothesis remains open:

> In AI-assisted institutional workflows, schema-bound claim boundaries may improve later reconstruction by reducing unsupported claims, prohibited inferences, and semantic drift.

That broader hypothesis remains untested.

It requires further implementation, conformance fixtures, scoring validation, enforcement testing, measurement reliability work, experimental execution, and external review.

---

## 4. The v0.1.1 Claim Boundary Coherence Harness

The v0.1.1 harness materialized a repository-backed specification stack for claim-boundary research.

The purpose was not to prove the full thesis.

The purpose was to determine whether the specification stack could be checked for internal coherence under declared rules.

The stack includes seven core artifacts:

| Artifact          | Purpose                                   |
| ----------------- | ----------------------------------------- |
| `FORK-SDS-001`    | Synthetic Decision Scenario Specification |
| `FORK-CBS-001`    | Canonical Boundary Set                    |
| `FORK-CORPUS-001` | Experimental Representation Corpus        |
| `FORK-SCR-001`    | Scoring and Coder Rubric                  |
| `FORK-PRS-001`    | Prompt and Reconstruction Stress Suite    |
| `FORK-BES-001`    | Boundary Enforcement Specification        |
| `FORK-EAP-001`    | Experimental Analysis Plan                |

The coherence runner checked:

* required artifact presence;
* identifier uniqueness and naming;
* cross-artifact reference resolution;
* dependency direction under the authority graph;
* canonical payload reproducibility;
* schema-stub parseability;
* placeholder classification;
* valid fixture behavior;
* invalid fixture behavior;
* preservation of `PASS`, `FAIL`, and `NOT_CHECKED`;
* digestability and digest coverage.

The output was a machine-readable specification-coherence receipt.

The receipt claimed only that the declared specification-coherence checks executed and passed under the recorded environment.

---

## 5. What the v0.1.1 Release Establishes

The v0.1.1 release establishes:

> Fork Claim Boundary Coherence Harness v0.1.1 executed against the materialized Fork specification stack and produced a bounded specification-coherence `PASS` receipt under the recorded environment.

This means:

* claim boundaries are no longer only prose;
* they are represented in a running coherence harness;
* the harness checks a materialized artifact stack;
* it emits receipts;
* it preserves result states;
* it records hashes;
* it retains failure lineage;
* it constrains the claims available after execution.

---

## 6. What the v0.1.1 Release Does Not Establish

The v0.1.1 release does **not** establish:

* that claim boundaries improve reconstruction;
* that Fork prevents semantic collapse;
* that the broader experiment is validated;
* scorer correctness;
* enforcement conformance;
* measurement reliability;
* enterprise readiness;
* legal, regulatory, institutional, or policy sufficiency;
* the truth of the broader Boundary Language thesis.

Those are higher rungs.

They require later implementation, conformance testing, reliability measurement, experimental execution, and external validation.

This restraint is not weakness.

It is the mechanism.

---

## 7. The Most Important Result: The System Failed First

The strongest part of the v0.1.1 release is not that it eventually passed.

It is that it failed first.

The initial run failed on `CHK-PLACEHOLDER-CLASSIFICATION`.

The runner incorrectly treated the valid identifier `CHK-PLACEHOLDER-CLASSIFICATION` as if it contained an unresolved placeholder, simply because the substring `PLACEHOLDER` appeared inside the identifier.

That was an implementation defect in the coherence runner.

It was not a thesis result.

It was not evidence that the claim-boundary doctrine failed.

The failed receipt was preserved.

The failed runner was preserved.

Patch attempts that did not match the compact runner format were preserved.

A surgical correction replaced raw substring matching with standalone-token detection.

The coherence suite was rerun.

The v0.1.1 receipt reported `PASS`.

The repository was committed and tagged.

This is correction without historical substitution.

The failure was not erased by the later pass.

The later pass did not rewrite the earlier failure.

Both now exist in the lineage.

That is claim-boundary discipline in miniature.

---

## 8. Why This Matters

Many systems treat failure as something to hide, smooth over, or reframe.

Fork treats failure as evidence.

A correction is not a replacement for history.

A correction is a new event in the lineage.

If a system cannot preserve the distinction between:

* the failed run;
* the defect classification;
* the correction;
* the rerun;
* and the later pass;

then it cannot be trusted to preserve harder distinctions later.

Those harder distinctions include:

* model output vs. model correctness;
* account activity vs. human review;
* workflow status vs. legal meaning;
* policy reference vs. policy compliance;
* source assertion vs. source truth;
* verified packet integrity vs. verified decision correctness.

If the system overclaims about itself, it will eventually overclaim about the workflows it records.

---

## 9. The Broader Research Roadmap

The broader research hypothesis remains open.

A proper experiment would compare different representations of the same decision record:

* sparse cryptographic record;
* prose-annotated record;
* schema-bound record with explicit claim boundaries;
* boundary-aware enforcement layer.

The question would not be whether the record remained intact.

The question would be whether later reconstructions preserved the boundaries between:

* what was observed;
* what was asserted;
* what was mechanically checked;
* what failed;
* what was unresolved;
* and what was explicitly not claimed.

Candidate metrics include:

* Semantic Boundary Preservation Rate;
* Unsupported Claim Rate;
* Prohibited Inference Rate;
* source-to-fact upgrade rate;
* authority-conflation rate;
* `NOT_CHECKED` preservation rate;
* temporal-substitution rate;
* inter-reviewer agreement.

Those metrics remain future work.

---

## 10. Core Distinction

Cryptographic systems answer:

> Has this record changed?

Claim-boundary systems answer:

> What is this record allowed to prove?

Both questions are necessary.

The first protects the artifact.

The second protects the inference.

Fork’s current work is an attempt to bring those together.

Not by replacing legal judgment, compliance review, human authority, or institutional accountability.

But by giving later reviewers a record that has not already smuggled conclusions into its own verification language.

---

## 11. Conclusion

A verified record is dangerous if verification is allowed to mean whatever later readers want it to mean.

For AI-assisted institutional workflows, the future problem is not only preserving data.

It is preserving evidentiary meaning under drift.

That requires claim boundaries.

The v0.1.1 Fork Claim Boundary Coherence Harness is a narrow first implementation of that idea.

It does not prove the thesis.

It does not validate the experiment.

It does not establish enterprise readiness.

It establishes something smaller and necessary:

> Claim boundaries can be treated as machine-checkable release controls, with explicit receipts, preserved failures, correction lineage, bounded claims, and prohibited higher-level conclusions.

The next step is harder: implementation conformance, scoring reliability, enforcement testing, empirical evaluation, and external review.

But the foundation is now in place.

A system that governs evidence must also govern what it says its evidence establishes.

That is the role of claim boundaries.

---

## Appendix A — Release Details

| Field            | Value                                  |
| ---------------- | -------------------------------------- |
| Release          | `FORK_CLAIM_BOUNDARY_COHERENCE_v0_1_1` |
| Tag              | `v0.1.1-specification-coherence-pass`  |
| Claim rung       | `SPECIFIED`                            |
| Evaluation scope | `SPECIFICATION_COHERENCE`              |
| Result           | `PASS`                                 |
| Coherence checks | `11 PASS / 0 FAIL / 0 NOT_CHECKED`     |

## Appendix B — Permitted Public Claim

Fork Claim Boundary Coherence Harness v0.1.1 executed against the materialized Fork specification stack and produced a bounded specification-coherence `PASS` receipt under the recorded environment.

## Appendix C — Prohibited Public Claims

Do not claim:

* claim boundaries improve reconstruction;
* Fork prevents semantic collapse;
* the Claim Boundaries experiment is validated;
* the method is enterprise-proven;
* the system establishes legal or institutional sufficiency.