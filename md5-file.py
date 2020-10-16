import hashlib
import sys

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if len(sys.argv) == 2:
    fname = sys.argv[1]
    file = "output/" + fname
    print(md5(file))
else:
    print("Usage: python md5-file.py <filename>")