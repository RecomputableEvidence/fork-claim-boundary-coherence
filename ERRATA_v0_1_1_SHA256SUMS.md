# Erratum ? v0.1.1 SHA256SUMS Publication Manifest Correction

## Scope

This erratum applies to the `manifests/SHA256SUMS` file published with Fork Claim Boundary Coherence v0.1.1.

## Issue

The published `manifests/SHA256SUMS` file contained incorrect SHA-256 declarations for a bounded set of seven files.

The affected file contents were not changed by this correction. The correction updates the declared SHA-256 values in `manifests/SHA256SUMS` so that they match the committed Git blob bytes for the listed files.

## Affected Entries

The corrected entries are:

- `bootstrap_materialize_and_run.py`
- `manifests/stack_manifest.json`
- `results/specification_coherence/preserved_failures/v0_1_placeholder_false_positive/IMPLEMENTATION_CORRECTION_SURGICAL_v0_1_to_v0_1_1.md`
- `results/specification_coherence/preserved_failures/v0_1_placeholder_false_positive/IMPLEMENTATION_CORRECTION_v0_1_to_v0_1_1.md`
- `results/specification_coherence/preserved_failures/v0_1_placeholder_false_positive/IMPLEMENTATION_CORRECTION_v0_1_to_v0_1_1_ROBUST.md`
- `tools/patch_placeholder_detector_surgical_v0_1_1.py`
- `tools/patch_placeholder_detector_v0_1_1.py`

## Verification Method

The corrected SHA-256 values were recomputed against Git blob bytes using `git show HEAD:<path>` rather than platform-local working-tree bytes, avoiding line-ending conversion effects from the Windows checkout environment.

## Non-Changes

This erratum does not change:

- the v0.1.1 release-lock values;
- the v0.1.1 coherence receipt;
- the coherence runner;
- schemas;
- verifier behavior;
- claim-boundary semantics;
- the v0.1 failure/correction lineage;
- the permitted or prohibited public claims for the release.

## Claim Boundary

This correction establishes only that `manifests/SHA256SUMS` has been repaired to match the committed bytes for the affected entries.

It does not establish any new implementation-conformance, empirical-validity, legal-sufficiency, institutional-sufficiency, or enterprise-readiness claim.
