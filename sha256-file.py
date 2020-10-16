import hashlib
import sys

def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

if len(sys.argv) == 2:
    fname = sys.argv[1]
    file = "output/" + fname
    print(sha256(file))
else:
    print("Usage: python sha256-file.py <filename>")