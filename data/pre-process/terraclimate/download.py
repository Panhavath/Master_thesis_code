import os
from pathlib import Path
import subprocess
import datetime

def download_terraclimate(var="vpd", year=None, out_dir="pre_data"):
    year = year or datetime.datetime.now().year
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    url = f"https://climate.northwestknowledge.net/TERRACLIMATE-DATA/TerraClimate_{var}_{year}.nc"
    out_path = out_dir / f"TerraClimate_{var}_{year}.nc"
    os.makedirs(out_dir, exist_ok=True)
    cmd = ["curl", "-L", "-C", "-", "--retry", "5", "--retry-delay", "5", "-o", str(out_path), url]
    subprocess.run(cmd, check=True)
    return out_path

if __name__ == "__main__":
    p = download_terraclimate(var="vpd", year=2024, out_dir="pre_data")
    print("Saved:", p)