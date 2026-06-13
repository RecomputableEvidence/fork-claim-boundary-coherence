from pathlib import Path
import re
import sys

runner = Path(sys.argv[1])
text = runner.read_text(encoding="utf-8-sig")

if "placeholder_pattern = re.compile" in text:
    patched = text
else:
    pattern = re.compile(
        "(?P<indent>[ \\t]*)for token in \\[\"TBD\", \"PLACEHOLDER\"\\]:\\r?\\n"
        "(?P=indent)[ \\t]{4}if token in text:\\r?\\n"
        "(?P=indent)[ \\t]{8}placeholder_hits\\.append\\(\\{\"file\": str\\(path\\.relative_to\\(ROOT\\)\\), \"token\": token\\}\\)",
        re.MULTILINE,
    )

    replacement = (
        "\\g<indent>placeholder_pattern = re.compile(r\"(?<![A-Z0-9_-])(TBD|PLACEHOLDER|TODO)(?![A-Z0-9_-])\")\n"
        "\\g<indent>for match in placeholder_pattern.finditer(text):\n"
        "\\g<indent>    placeholder_hits.append({\"file\": str(path.relative_to(ROOT)), \"token\": match.group(1), \"offset\": match.start()})"
    )

    patched, count = pattern.subn(replacement, text)
    if count != 1:
        print("Could not find the raw placeholder detection block.", file=sys.stderr)
        print("Diagnostic: lines containing PLACEHOLDER:", file=sys.stderr)
        for i, line in enumerate(text.splitlines(), 1):
            if "PLACEHOLDER" in line:
                print(f"{i}: {line}", file=sys.stderr)
        sys.exit(3)

patched = patched.replace('"receipt_version": "0.1.0"', '"receipt_version": "0.1.1"')
patched = patched.replace('"version": "0.1.0",\n        "digest": runner_digest,', '"version": "0.1.1",\n        "digest": runner_digest,')

runner.write_text(patched, encoding="utf-8", newline="\n")
print("Runner patched successfully.")
