import hashlib
import sys
import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count
import shutil as sh
import getopt as opt
import multiprocessing


# http://zetcode.com/python/multiprocessing/
# https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/multiprocessing/communication.html
# https://stackoverflow.com/questions/56587410/how-to-generate-a-counter-for-finding-a-hash-with-9-leading-zeroes


def print_header():
    print("Process | Length | Proof              | Digest                           | Tries      | Time    ")
    print("------------------------------------------------------------------------------------------------")


def print_data(process, length, proof, digest, tries, time):
    print("P{}      | {}      | {} | {} | {} | {}".format(
        process, length, proof, digest, str(tries)+" "*(10-len(str(tries))), time))


def print_summary(counts, ceros):
    print("Number of digests found:")
    print("Length {}: {} | Length {}: {}".format(
        ceros, counts[0], ceros-1, counts[1]))


def md5_digest(text):
    hash_md5_new = hashlib.md5()
    hash_md5_new.update(text)
    return hash_md5_new.hexdigest()


def get_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)


def minado(process_number, number_of_processes, max_counter, results, ceros, fname, start_time):
    # fname = sys.argv[1]
    # print("P" + str(process_number) + " comienza la ejecución.")
    count = process_number
    max = 16 ** 8

    group = "G05061227"
    original = "input/" + fname
    modified = "output/" + fname

    with open(original, 'rb') as original_file:
        original_text = original_file.read()

    while count < max:
        hexadecimal8 = '{:0>8x}'.format(count)
        proof = hexadecimal8 + " " + group
        modified_text = original_text + proof.encode()
        digest = md5_digest(modified_text)
        if digest.startswith("0"*(ceros-1)):
            seconds = time.time() - start_time
            str_time = get_time(seconds)
            if digest.startswith("0"*(ceros)):
                print_data(process_number, ceros, proof,
                           digest, count+1, str_time)
                results.put((str(digest), str(count)))
                break
            else:
                print_data(process_number, ceros-1, proof,
                           digest, count+1, str_time)
        count += number_of_processes  # Saltar al siguiente chunk.

    if count < max_counter:
        print()
        print("Success: Proof found before reaching maximum(" + str(max_counter) + ")")
        with open(modified, 'wb') as modified_file:
            modified_file.write(modified_text)
    else:
        print()
        print("Fail: Proof not found before reaching maximum(" + str(max_counter) + ")")


##### MAIN ####
if __name__ == '__main__':
    start_time = time.time()
    ceros = 6  # by default, a no ser que se especifique cuantos ceros.
    try:
        """
        f = input file
        o = output file
        g = group name
        c = zero quantity
        t = time limit (minutes)
        p = number of processes
        """
        opts, args = opt.getopt(sys.argv[1:], "f:o:g:c:t:p:")
    except:
        sys.exit("Error: parametros erróneos")

    for opt, arg in opts:
        if opt in ("-f"):
            fname = arg
        if opt in ("-o"):
            # no funciona
            output_file = arg
        if opt in ("-g"):
            grupo = arg
        if opt in ("-c"):
            ceros = int(arg)
        if opt in ("-t"):
            # time limit in minutes
            time_limit = int(arg)
        if opt in ("-p"):
            number_of_processes = int(arg)

    # Calcular hasta donde tiene que contar cada nodo.
    hondarra = (16 ** 8)/number_of_processes
    max_counter = []
    for i in range(number_of_processes):
        max_counter.append(hondarra)
        hondarra += max_counter[i]

    # para que todos los procesos puedan meter aqui el resultado
    results = multiprocessing.Queue()

    # en este vector guardaremos todos los procesos (para poder gestionarlos, terminate...)
    processes = []

    print("Obteniendo %d ceros para %s con %s procesos" %
          (ceros, fname, number_of_processes))

    # iniciar N procesos
    for i in range(number_of_processes):
        p = multiprocessing.Process(target=minado, args=(
            i, number_of_processes, max_counter[i], results, ceros, fname, start_time))
        p.start()
        processes.append(p)

    print()
    print_header()

    # LOOPEAR HASTA OBTENER UNA RESPUESTA
    while results.empty():
        pass
    print(results.get())
    seconds = time.time() - start_time
    str_time = get_time(seconds)
    print("==================================================================")
    print("El tiempo necesitado para obtener un hash de " +
          str(ceros) + " ceros: " + str_time)
    print("==================================================================")
    # MATAR LOS PROCESOS
    for p in processes:
        p.terminate()
