from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
p=Path(__file__).resolve().parents[1]
with ZipFile(p/'dist/noor-interactive-preparations-v1.0.0.zip','w',ZIP_DEFLATED) as z:
    for f in sorted((p/'extension').rglob('*')):
        if f.is_file(): z.write(f,f.relative_to(p/'extension'))
