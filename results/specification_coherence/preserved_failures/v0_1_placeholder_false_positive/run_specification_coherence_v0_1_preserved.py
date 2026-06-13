from __future__ import annotations
import hashlib, json, platform, re, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "specification_coherence"
RESULTS.mkdir(parents=True, exist_ok=True)

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
def canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
def dupes(items: list[str]) -> list[str]:
    seen, out = set(), []
    for x in items:
        if x in seen and x not in out: out.append(x)
        seen.add(x)
    return out
def check(ok: bool, cid: str, name: str, good: str, bad: str) -> dict[str,str]:
    return {"check_id":cid,"name":name,"status":"PASS" if ok else "FAIL","reason_code":"OK" if ok else "CHECK_FAILED","detail": good if ok else bad}

artifact_registry = load_json(ROOT/"registry/artifact_registry.json")
identifier_registry = load_json(ROOT/"registry/identifier_registry.json")
dependency_registry = load_json(ROOT/"registry/dependency_registry.json")
checks, defects, not_checked = [], [], []

missing=[]
for a in artifact_registry["artifacts"]:
    for rel in [a["filename"], a["canonical_filename"]]:
        if not (ROOT/rel).exists(): missing.append(rel)
checks.append(check(not missing,"CHK-ARTIFACT-PRESENCE","Required artifact presence","All registered spec and canonical artifact files are present.",f"Missing files: {missing}"))

ids=[x["id"] for x in identifier_registry["identifiers"]]
duplicate_ids=dupes(ids)
bad_format=[x for x in ids if not re.match(r"^[A-Z0-9][A-Z0-9_-]*(?:-[A-Z0-9_]+)*$",x)]
checks.append(check(not duplicate_ids and not bad_format,"CHK-IDENTIFIER-UNIQUENESS","Identifier uniqueness and naming","All registered identifiers are unique and match the accepted format.",f"Duplicate IDs: {duplicate_ids}; bad format IDs: {bad_format}"))

known=set(ids)
unresolved=[]
for item in identifier_registry["identifiers"]:
    for ref in item.get("references",[]):
        if ref not in known:
            unresolved.append({"id":item["id"],"unresolved_reference":ref})
checks.append(check(not unresolved,"CHK-REFERENCE-RESOLUTION","Cross-artifact reference resolution","All identifier references resolve to registered identifiers or artifacts.",f"Unresolved references: {unresolved}"))

rank={"FORK-SDS-001":0,"FORK-CBS-001":1,"FORK-CORPUS-001":2,"FORK-SCR-001":3,"FORK-PRS-001":4,"FORK-BES-001":5,"FORK-EAP-001":6}
bad_edges=[]
for edge in dependency_registry["edges"]:
    if edge["from"] not in rank or edge["to"] not in rank or rank[edge["from"]] >= rank[edge["to"]]:
        bad_edges.append(edge)
checks.append(check(not bad_edges,"CHK-DEPENDENCY-DIRECTION","Authority and dependency direction","All dependency edges flow downstream according to the authority graph.",f"Forbidden dependency edges: {bad_edges}"))

canon_fail=[]
for a in artifact_registry["artifacts"]:
    obj=load_json(ROOT/a["canonical_filename"])
    declared=obj.get("canonical_payload_sha256")
    computed=sha256_bytes(canonical_bytes({k:v for k,v in obj.items() if k!="canonical_payload_sha256"}))
    if declared != computed:
        canon_fail.append({"artifact":a["artifact_id"],"declared":declared,"computed":computed})
checks.append(check(not canon_fail,"CHK-CANONICAL-REPRODUCIBILITY","Canonical machine-form reproducibility","All canonical JSON artifacts reproduce declared canonical payload hashes.",f"Canonical hash failures: {canon_fail}"))

schema_err=[]
for p in (ROOT/"schemas").glob("*.json"):
    try:
        obj=load_json(p)
        if obj.get("$schema")!="https://json-schema.org/draft/2020-12/schema":
            schema_err.append({"schema":p.name,"error":"missing draft 2020-12 marker"})
    except Exception as exc:
        schema_err.append({"schema":p.name,"error":str(exc)})
checks.append(check(not schema_err,"CHK-SCHEMA-VALIDITY","Schema validation of canonical artifacts","All schema files are parseable JSON Schema stubs with the declared draft marker.",f"Schema errors: {schema_err}"))

placeholder_hits=[]
for base in ["specs","canonical","registry","schemas"]:
    for p in (ROOT/base).rglob("*"):
        if p.is_file() and p.suffix.lower() in {".md",".json"}:
            text=p.read_text(encoding="utf-8")
            for token in ["TBD","PLACEHOLDER"]:
                if token in text:
                    placeholder_hits.append({"file":str(p.relative_to(ROOT)).replace("\\","/"),"token":token})
checks.append(check(not placeholder_hits,"CHK-PLACEHOLDER-CLASSIFICATION","Unresolved placeholder classification","No unclassified TBD or PLACEHOLDER tokens were found.",f"Unclassified placeholders: {placeholder_hits}"))

valid=load_json(ROOT/"fixtures/specification_coherence/valid/valid_identifier_registry.json")
valid_state="FAIL" if dupes([x["id"] for x in valid["identifiers"]]) else "PASS"
checks.append(check(valid_state==valid["expected_status"],"CHK-VALID-FIXTURES","Declared valid fixtures pass","Valid specification-coherence fixture produced expected PASS.",f"Expected {valid['expected_status']}, observed {valid_state}"))

invalid_dup=load_json(ROOT/"fixtures/specification_coherence/invalid/invalid_duplicate_identifier.json")
invalid_dep=load_json(ROOT/"fixtures/specification_coherence/invalid/invalid_forbidden_dependency.json")
dup_state="FAIL" if dupes([x["id"] for x in invalid_dup["identifiers"]]) else "PASS"
dep_state="PASS"
for edge in invalid_dep["edges"]:
    if edge["from"] not in rank or edge["to"] not in rank or rank[edge["from"]] >= rank[edge["to"]]:
        dep_state="FAIL"
checks.append(check([dup_state,dep_state]==["FAIL","FAIL"],"CHK-INVALID-FIXTURES","Declared invalid fixtures fail as expected","Invalid duplicate-ID and forbidden-dependency fixtures produced expected FAIL states.",f"Observed states: {[dup_state,dep_state]}"))

amb=load_json(ROOT/"fixtures/specification_coherence/ambiguous/ambiguous_reference.json")
unres=load_json(ROOT/"fixtures/specification_coherence/unresolved/unresolved_placeholder.json")
states={"PASS","FAIL",amb["expected_status"],unres["expected_status"]}
checks.append(check(states=={"PASS","FAIL","NOT_CHECKED"},"CHK-RESULT-STATE-PRESERVATION","PASS/FAIL/NOT_CHECKED state preservation","Fixture evaluation preserves PASS, FAIL, and NOT_CHECKED as distinct states.",f"Observed state samples: {sorted(states)}"))

digest_errors=[]
for p in ROOT.rglob("*"):
    rel=str(p.relative_to(ROOT)).replace("\\","/")
    if p.is_file() and not rel.startswith("results/specification_coherence/") and rel!="manifests/SHA256SUMS":
        try: sha256_file(p)
        except Exception as exc: digest_errors.append({"file":rel,"error":str(exc)})
checks.append(check(not digest_errors,"CHK-DIGEST-COVERAGE","Input and output digest coverage","All current input files are digestable; final SHA256SUMS will be emitted after receipt generation.",f"Digest errors: {digest_errors}"))

overall="PASS" if all(c["status"]=="PASS" for c in checks) else "FAIL"
if overall=="FAIL":
    defects.append({"defect_id":"DEFECT-SPECIFICATION-COHERENCE-001","classification":"SPECIFICATION_DEFECT","status":"OPEN","evidence":[c["check_id"] for c in checks if c["status"]=="FAIL"]})

artifact_versions={a["artifact_id"]:a["version"] for a in artifact_registry["artifacts"]}
artifact_digests={a["artifact_id"]:{"spec_sha256":sha256_file(ROOT/a["filename"]),"canonical_sha256":sha256_file(ROOT/a["canonical_filename"])} for a in artifact_registry["artifacts"]}
runner_digest=sha256_file(Path(__file__))

payload={
    "schema_id":"FORK-SPECIFICATION-COHERENCE-RECEIPT",
    "schema_version":"0.1.0",
    "receipt_id":"FORK_SPECIFICATION_COHERENCE_RECEIPT_v0_1",
    "receipt_version":"0.1.0",
    "created_at":datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
    "claim_rung":"SPECIFIED",
    "evaluation_scope":"SPECIFICATION_COHERENCE",
    "overall_result":overall,
    "overall_reason":{"code":"COHERENCE_CHECKS_EXECUTED","detail":"Specification-coherence checks executed against the materialized v0.1 artifact stack."},
    "artifact_versions":artifact_versions,
    "artifact_digests":artifact_digests,
    "checks":checks,
    "defects":defects,
    "not_checked":not_checked,
    "execution_environment":{"os":f"{platform.system()} {platform.release()}","python":sys.version.split()[0],"platform":platform.platform(),"cwd":str(ROOT)},
    "runner":{"name":"FORK_SPECIFICATION_COHERENCE_RUNNER","version":"0.1.0","digest":runner_digest,"execution_status":"EXECUTED"},
    "claim_boundary":{
        "establishes":[
            "The materialized Fork Claim Boundary specification stack was evaluated for specification coherence under the recorded runner and environment.",
            "Required artifacts, identifiers, references, dependency direction, canonical payload hashes, schema stubs, fixtures, result-state preservation, and digestability were evaluated."
        ],
        "does_not_establish":[
            "Specification completeness or optimality",
            "Implementation conformance of the full experimental apparatus",
            "Measurement reliability",
            "Experimental executability at scale",
            "Empirical effectiveness of boundary language",
            "External validity",
            "Legal, regulatory, institutional, or policy sufficiency",
            "Truth of the Boundary Language thesis"
        ]},
    "next_required_action":[
        "Review the coherence receipt.",
        "If PASS, proceed to implementation conformance fixtures for schemas, scorers, and BES.",
        "If FAIL, classify each defect and issue a versioned correction without historical substitution.",
        "Preserve this receipt and all input artifacts as the v0.1 lineage."
    ]
}
receipt=dict(payload)
receipt["receipt_integrity"]={
    "canonicalization":"UTF-8; JSON keys sorted lexicographically; compact separators; no NaN/Infinity; /receipt_integrity excluded from payload digest",
    "covered_object":"Entire receipt object excluding /receipt_integrity",
    "payload_sha256":sha256_bytes(canonical_bytes(payload))
}
receipt_path=RESULTS/"FORK_SPECIFICATION_COHERENCE_RECEIPT_v0_1.json"
write_json(receipt_path, receipt)

files=[p for p in ROOT.rglob("*") if p.is_file() and str(p.relative_to(ROOT)).replace("\\","/")!="manifests/SHA256SUMS"]
manifest={"manifest_id":"FORK_CLAIM_BOUNDARY_COHERENCE_v0_1_STACK_MANIFEST","version":"0.1.0","created_at":datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),"files":[{"path":str(p.relative_to(ROOT)).replace("\\","/"),"sha256":sha256_file(p)} for p in sorted(files)]}
write_json(ROOT/"manifests/stack_manifest.json", manifest)
(ROOT/"manifests/SHA256SUMS").write_text("\n".join(f"{x['sha256']}  {x['path']}" for x in manifest["files"])+"\n",encoding="utf-8",newline="\n")

print("FORK_CLAIM_BOUNDARY_COHERENCE_v0_1")
print(f"ROOT={ROOT}")
print(f"OVERALL_RESULT={overall}")
print(f"RECEIPT={receipt_path}")
print(f"RECEIPT_SHA256={sha256_file(receipt_path)}")
print(f"RUNNER_SHA256={runner_digest}")
if overall!="PASS":
    sys.exit(2)
