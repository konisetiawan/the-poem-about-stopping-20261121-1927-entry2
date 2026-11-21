import os
from pathlib import Path

# A hand at the threshold turns a pause into a deliberate choice.
POEM = """The Door

Her hand stayed on the door.
She did not push it open.
The hallway waited,
and so did she —
staying was the bravest thing
her hand had ever done."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
entry_path = output_dir / "entry.txt"
entry_path.write_text(POEM, encoding="utf-8")
written_text = entry_path.read_text(encoding="utf-8")
assert 1 <= len(written_text) <= 280
assert written_text.strip()
print(len(written_text))
