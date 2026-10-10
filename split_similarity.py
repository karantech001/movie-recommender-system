
from pathlib import Path

folder = Path(__file__).resolve().parent
source = folder / "similarity.pkl"
chunk_size = 20 * 1024 * 1024  # 20 MB

if not source.exists():
    raise FileNotFoundError("similarity.pkl project folder mein nahi mili.")

part_number = 0

with source.open("rb") as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break

        output = folder / f"similarity.part{part_number:03d}"
        output.write_bytes(chunk)
        print(f"Created: {output.name} ({len(chunk) / (1024 * 1024):.2f} MB)")
        part_number += 1

print(f"\nDone! Total parts: {part_number}")
