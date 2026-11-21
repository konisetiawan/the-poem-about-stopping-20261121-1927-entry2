import os
from pathlib import Path

# The bag's return to its drawer makes staying visible as an action.
POEM = """The Bag

She packed the bag.
Then she unpacked it,
her hands folding each thing back
into its drawer.
Staying was not giving up.
It was choosing."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
entry_path = output_dir / "entry.txt"
entry_path.write_text(POEM, encoding="utf-8")
text = entry_path.read_text(encoding="utf-8")
assert 1 <= len(text) <= 280
assert text.strip()
print(len(text))
