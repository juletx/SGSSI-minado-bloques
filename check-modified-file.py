import hashlib
import sys
import re

fname = sys.argv[1]

original = "input/" + fname
modified = "output/" + fname

fo = open(original, "r")
lines_fo = fo.readlines()
fm = open(modified, "r")
lines_fm = fm.readlines()

# Comienza exactamente por los mismos contenidos que el primero (sin \n)
starts_with = lines_fo[:-1] == lines_fm[:-2] and lines_fo[-1] == lines_fm[-2]
print("Comienza exactamente por los mismos contenidos:", starts_with)

# Incluye una línea adicional con una secuencia de 8 caracteres en hexadecimal
string_hex = lines_fm[-1][:8]
hexchars = "0123456789abcdef"
all_hex = all(c in hexchars for c in string_hex)
print("Incluye una línea adicional con 8 caracteres en hexadecimal:", all_hex)

# Incluye un identificador de grupo
string_group = lines_fm[-1][8:]
pattern = re.compile("^ G([0-3][0-9])+$")
match = bool(pattern.match(string_group))
print("Incluye un identificador de grupo:", match)

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

print("El archivo es correcto:", starts_with and all_hex and match and startswith0)