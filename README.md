# 🧬 PDB Geometry 01 - Fetcher

A pure-Python console tool that downloads 3 curated PDB structures needed for the full PDB Geometry series (Projects 1-5). No external dependencies.

## 👤 Author
**Urva Sohail**

## ✨ Features
- **📥 Auto Download**: Fetches 3 structures from RCSB PDB
- **📂 Smart Skip**: Skips file if already exists locally
- **✅ Validation**: Checks file size after download
- **🧹 Clean Repo**: Data files ignored via `.gitignore`
- **🐍 Pure Python**: Only stdlib `urllib` + `pathlib`

## 💻 Technologies Used
- **Python 3+**: Core programming language
- **urllib.request**: For downloading from RCSB
- **pathlib**: For file handling
- **Console I/O**: For download progress

## 🚀 How to Run

### Using VS Code
1. Open folder `pdb-geometry-01-fetcher-`
2. Open terminal
3. Run:

```
bash
python main.py
```

## 📥 Sample Input & Output
## Input
No input needed - runs automatically
## Output
```
downloading 1AKI from https://files.rcsb.org/download/1AKI.pdb ...
saved -> 1aki.pdb (113 KB)
downloading 4HHB from https://files.rcsb.org/download/4HHB.pdb ...
saved -> 4hhb.pdb (462 KB)
downloading 1PWC from https://files.rcsb.org/download/1PWC.pdb ...
saved -> 1pwc.pdb (537 KB)
```
Done. Total 3 files ready for Project

## Downloaded Files
```
1aki.pdb - Lysozyme 129aa 1.5Å (113 KB)
4hhb.pdb - Hemoglobin 574aa 1.74Å (462 KB)
1pwc.pdb - DD-peptidase 1.1Å ultra high-res (537 KB)
```
## ⚙️ How It Works
- The program creates a list PDB_CODES = ["1AKI", "4HHB", "1PWC"]
- For each code, it builds URL https://files.rcsb.org/download/{CODE}.pdb
- It checks if file already exists locally - if yes, it skips to save time
- If not, it downloads via urllib.request.urlretrieve()
- It saves file as lowercase name like 1aki.pdb and shows size in KB
- At end it counts total files and prints "Ready for Project "

## 🔮 Future Improvements
- [ ] Read input from `.cif` files too
- [ ] Calculate download speed and time
- [ ] Export results to CSV for data analysis
- [ ] Add support for large batch downloads (100+ PDBs)
