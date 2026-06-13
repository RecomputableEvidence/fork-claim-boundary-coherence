# Fork Claim Boundary Coherence Harness v0.1.1

## Release Summary

This release locks the first repository-backed Fork Claim Boundary Coherence Harness.

The v0.1.1 harness executed against the materialized Fork specification stack and produced a bounded specification-coherence `PASS` receipt under the recorded environment.

## Claim Boundary

This release establishes only:

> Fork Claim Boundary Coherence Harness v0.1.1 executed against the materialized Fork specification stack and produced a bounded specification-coherence `PASS` receipt under the recorded environment.

This release does **not** establish:

* implementation conformance of the full experimental apparatus;
* scorer correctness;
* boundary-enforcement conformance;
* measurement reliability;
* empirical effectiveness;
* external validity;
* legal, regulatory, institutional, or policy sufficiency;
* truth of the broader Boundary Language thesis.

## What Passed

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

Final result:

```text
OVERALL_RESULT: PASS
CHECKS: 11 PASS / 0 FAIL / 0 NOT_CHECKED
CLAIM_RUNG: SPECIFIED
EVALUATION_SCOPE: SPECIFICATION_COHERENCE
```

## Preserved Failure Lineage

The release preserves the v0.1 failure lineage:

```text
v0.1 bootstrap executed
→ FAIL on CHK-PLACEHOLDER-CLASSIFICATION
→ false-positive cause identified
→ brittle patch attempts failed and were preserved
→ surgical patch applied
→ v0.1.1 coherence run PASS
→ Git commit/tag release lock
```

The initial failure was caused by raw substring matching: the runner treated the valid identifier `CHK-PLACEHOLDER-CLASSIFICATION` as though it contained an unresolved placeholder token.

The correction replaced raw substring detection with standalone-token detection.

This is correction without historical substitution.

## Why This Release Matters

This release demonstrates claim boundaries as machine-checkable release controls.

It does not prove the broader hypothesis.

It establishes a narrower infrastructure milestone: Fork can preserve what passed, what failed, what was corrected, what remains unclaimed, and what higher-level claims remain prohibited.

## Permitted Public Claim

Fork Claim Boundary Coherence Harness v0.1.1 executed against the materialized Fork specification stack and produced a bounded specification-coherence `PASS` receipt under the recorded environment.

## Prohibited Public Claims

Do not claim:

* Claim Boundaries improve reconstruction.
* Fork prevents semantic collapse.
* The Claim Boundaries experiment is validated.
* The method is enterprise-proven.
* The system establishes legal or institutional sufficiency.
