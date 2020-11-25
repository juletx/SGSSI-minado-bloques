import hashlib
import sys
import re

def starts_with(lines_fo, lines_fm):
    # Comienza exactamente por los mismos contenidos que el primero
    starts_with = lines_fo[:-1] == lines_fm[:-2] and lines_fo[-1] == lines_fm[-2]
    print("Comienza exactamente por los mismos contenidos:", starts_with)
    return starts_with

def includes_hex(lines_fm):
    # Incluye una línea adicional con una secuencia de 8 caracteres en hexadecimal
    string_hex = lines_fm[-1][:8]
    hexchars = "0123456789abcdef"
    all_hex = all(c in hexchars for c in string_hex)
    print("Incluye una línea adicional con 8 caracteres en hexadecimal:", all_hex)
    return all_hex

def includes_group(lines_fm):
    # Incluye un identificador de grupo
    string_group = lines_fm[-1][8:]
    pattern = re.compile("^ G([0-3][0-9])+$")
    match = bool(pattern.match(string_group))
    print("Incluye un identificador de grupo:", match)
    return match

def md5_digest(text):
    hash_md5_new = hashlib.md5()
    hash_md5_new.update(text)
    return hash_md5_new.hexdigest()

def starts_with0s(text_fm, ceros):
    # El resumen MD5 del fichero debe comenzar 0s
    digest = md5_digest(text_fm)
    starts_with0s = digest.startswith("0"*(ceros))
    print("El resumen MD5 del fichero comienza por " + str(ceros) + " ceros:", starts_with0s)
    return starts_with0s

def main():
    if len(sys.argv) == 2:
        fname = sys.argv[1]

        original = "input/" + fname
        modified = "output/" + fname

        with open(original, "r") as fo:
            lines_fo = fo.readlines()
        with open(modified, "r") as fm:
            lines_fm = fm.readlines()
        with open(modified, "rb") as fm:
            text_fm = fm.read()

        starts_w = starts_with(lines_fo, lines_fm)

        incl_hex = includes_hex(lines_fm)

        incl_group = includes_group(lines_fm)

        starts_w0s = starts_with0s(text_fm, 6)

        print("El archivo es correcto:", starts_w and incl_hex and incl_group and starts_w0s)

    else:
        print("Use: python " + sys.argv[0] + " <filename>")

if __name__ == "__main__":
    main()