import urllib.request
import pathlib
import matplotlib.pyplot as plt

# Project 0: download 3 structures for all later projects
PDB_CODES = ["1AKI", "4HHB", "1PWC"]
BASE_URL = "https://files.rcsb.org/download/{}.pdb"

stats = [] # for plot

for code in PDB_CODES:
    filename = pathlib.Path(f"{code.lower()}.pdb")

    if filename.exists():
        print(f"skip {filename} already exists")
    else:
        url = BASE_URL.format(code)
        print(f"downloading {code} from {url}...")
        urllib.request.urlretrieve(url, filename)
        print(f"saved -> {filename} ({filename.stat().st_size//1024} KB)")

    # collect info for image
    size_kb = filename.stat().st_size / 1024
    atoms = sum(1 for line in open(filename) if line.startswith("ATOM"))
    stats.append((code, size_kb, atoms))

print("\nDone. Total 3 files ready for Project 1-5")

# ---- Create image like Ramachandran project (FIXED) ----
codes = [s[0] for s in stats]
sizes = [s[1] for s in stats]
atom_counts = [s[2] for s in stats]

plt.figure(figsize=(9,5.5)) # taller figure
max_atoms = max(atom_counts)

plt.bar(codes, atom_counts, color=['#1f77b4','#ff7f0e','#2ca02c'])
plt.xlabel('PDB Code')
plt.ylabel('Number of ATOM records')
plt.title('PDB Fetcher - Dataset Summary (Project 01)\n1AKI, 4HHB, 1PWC', pad=20) # pad moves title up
plt.ylim(0, max_atoms * 1.35) # give 35% space on top so text doesn't hit title

for i, v in enumerate(atom_counts):
    plt.text(i, v + max_atoms*0.05, f"{v} atoms\n{sizes[i]:.0f} KB", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('fetcher_plot.png', dpi=200)
print("Image saved: fetcher_plot.png - FIXED, no merge")