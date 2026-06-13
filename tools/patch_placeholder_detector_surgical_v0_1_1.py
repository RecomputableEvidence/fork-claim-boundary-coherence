from pathlib import Path
import re
import sys

runner = Path(sys.argv[1])
text = runner.read_text(encoding="utf-8-sig")
lines = text.splitlines()

if "placeholder_pattern = re.compile" in text:
    print("Runner already contains standalone placeholder detector. No patch needed.")
    raise SystemExit(0)

out = []
i = 0
patched = False

while i < len(lines):
    line = lines[i]
    normalized = line.replace(" ", "")

    if (not patched) and 'fortokenin["TBD","PLACEHOLDER"]:' in normalized:
        indent = line[:len(line) - len(line.lstrip())]

        out.append(indent + 'placeholder_pattern = re.compile(r"(?<![A-Z0-9_-])(TBD|PLACEHOLDER|TODO)(?![A-Z0-9_-])")')
        out.append(indent + 'for match in placeholder_pattern.finditer(text):')
        out.append(indent + '    placeholder_hits.append({"file": str(path.relative_to(ROOT)), "token": match.group(1), "offset": match.start()})')

        # Skip the original:
        #   for token in [...]
        #       if token in text:
        #           placeholder_hits.append(...)
        i += 3
        patched = True
        continue

    out.append(line)
    i += 1

if not patched:
    print("Could not locate compact raw placeholder detector.", file=sys.stderr)
    print("Lines containing PLACEHOLDER:", file=sys.stderr)
    for n, line in enumerate(lines, 1):
        if "PLACEHOLDER" in line:
            print(f"{n}: {line}", file=sys.stderr)
    raise SystemExit(3)

new_text = "\n".join(out) + "\n"

# Ensure runner has import re.
if not re.search(r"^import re$", new_text, re.MULTILINE):
    new_text = new_text.replace("import json\n", "import json\nimport re\n", 1)

# Bump receipt/runner metadata where the runner emits it.
new_text = new_text.replace('"receipt_version":"0.1.0"', '"receipt_version":"0.1.1"')
new_text = new_text.replace('"receipt_version": "0.1.0"', '"receipt_version": "0.1.1"')
new_text = new_text.replace('"version":"0.1.0","digest":runner_digest', '"version":"0.1.1","digest":runner_digest')
new_text = new_text.replace('"version": "0.1.0",\n        "digest": runner_digest', '"version": "0.1.1",\n        "digest": runner_digest')

runner.write_text(new_text, encoding="utf-8", newline="\n")
print("Surgical placeholder detector patch applied.")
