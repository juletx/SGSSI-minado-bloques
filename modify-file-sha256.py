import hashlib
import sys
from shutil import copyfile
import secrets

def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def startswith(string):
    digest = sha256(modified)
    return digest.startswith(string)

if len(sys.argv) == 2:
    fname = sys.argv[1]

    modified = "modified-sha256.txt"
    while 1:
        copyfile(fname, modified)
        hexadecimal30 = secrets.token_hex(15)
        hexadecimal8 = hexadecimal30[:8]
        with open(modified, "a") as fm:
            fm.write("\n" + hexadecimal8)
        if startswith("0000"):
            break

else:
    print("Usage: python modify-file-sha256.py <filename>")