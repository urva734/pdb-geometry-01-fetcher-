import urllib.request
import pathlib

# Project 0: download 3 structures for all later projects
PDB_CODES = ["1AKI", "4HHB", "1PWC"]
BASE_URL = "https://files.rcsb.org/download/{}.pdb"

for code in PDB_CODES:
    filename = pathlib.Path(f"{code.lower()}.pdb")

    if filename.exists():
        print(f"skip {filename} already exists")
        continue

    url = BASE_URL.format(code)
    print(f"downloading {code} from {url} ...")
    urllib.request.urlretrieve(url, filename)
    print(f"saved -> {filename} ({filename.stat().st_size//1024} KB)")

print("\nDone. Total 3 files ready for Project 1-5")