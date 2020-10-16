import hashlib
import sys
from shutil import copyfile
import secrets

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def startswith(string):
    digest = md5(modified)
    return digest.startswith(string)

if len(sys.argv) == 2:
    fname = sys.argv[1]

    original = "input/" + fname
    modified = "output/" + fname
    while 1:
        copyfile(original, modified)
        hexadecimal30 = secrets.token_hex(15)
        hexadecimal8 = hexadecimal30[:8]
        group = " G27"
        with open(modified, "a") as fm:
            fm.write(hexadecimal8)
            fm.write(group)
        if startswith("0000"):
            break

else:
    print("Usage: python modify-file-md5.py <filename>")