import hashlib
import sys

fname = sys.argv[1]

original = "input/" + fname
modified = "output/" + fname

fo = open(original, "r")
lines_fo = fo.readlines()
fm = open(modified, "r")
lines_fm = fm.readlines()

# Comienza exactamente por los mismos contenidos que el primero (sin \n)
starts_with = lines_fo[:-1] == lines_fm[:-2] and lines_fo[-1] == lines_fm[-2][:-1]
print("Comienza exactamente por los mismos contenidos:", starts_with)

# Incluye una línea adicional con una secuencia de 8 caracteres en hexadecimal
string = lines_fm[-1]
length = len(string)
hexchars = "0123456789abcdef"
all_hex = all(c in hexchars for c in string)
print("Incluye una línea adicional con 8 caracteres en hexadecimal:", length == 8 and all_hex)

# El resumen MD5 del fichero debe comenzar por el carácter hexadecimal “0”
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

digest = md5(modified)
startswith0 = digest.startswith("0")

print("El resumen MD5 del fichero comienza por el carácter hexadecimal 0:", startswith0)

print("El archivo es correcto:", starts_with and length == 8 and all_hex and startswith0)