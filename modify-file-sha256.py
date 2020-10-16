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

    original = "input/" + fname
    modified = "output/" + fname
    while 1:
        copyfile(priginal, modified)
        hexadecimal30 = secrets.token_hex(15)
        hexadecimal8 = hexadecimal30[:8]
        group = " G27"
        with open(modified, "a") as fm:
            fm.write("\n" + hexadecimal8)
            fm.write(group)
        if startswith("0000"):
            break

else:
    print("Usage: python modify-file-sha256.py <filename>")