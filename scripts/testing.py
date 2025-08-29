import os

labelRoute = "./data/raw/valid/labels"
for file in os.listdir(labelRoute):
    path = os.path.join(labelRoute, file)
    print(path)
    with open(path, "r") as f:
        for i, line in enumerate(f):
            parts = line.strip().split()
            cls, coords = parts[0], parts[1:]
            if len(coords) % 2 != 0:
                print(f"Odd number of coordinates in {file} line {i + 1}")
            bad = [c for c in coords if not (0 <= float(c) <= 1)]
            if bad:
                print(f"Out of range coordinate in {file} line {i + 1}")