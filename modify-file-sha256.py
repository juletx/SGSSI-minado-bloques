import hashlib
import sys
import time


def print_header():
    print("Length | Proof              | Digest                           | Tries      | Time    ")
    print("--------------------------------------------------------------------------------------")


def print_data(length, proof, digest, tries, time):
    print("{}      | {} | {} | {} | {}".format(
        length, proof, digest, str(tries)+" "*(10-len(str(tries))), time))


def print_summary(counts):
    print("Number of digests found:")
    print("Length 8: {} | Length 7: {} | Length 6: {} | Length 5: {}".format(
        counts[0], counts[1], counts[2], counts[3]))


def sha256_digest(text):
    hash_sha256_new = hashlib.sha256()
    hash_sha256_new.update(text)
    return hash_sha256_new.hexdigest()


def get_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)


def main():
    if len(sys.argv) == 2:
        start_time = time.time()
        fname = sys.argv[1]
        count = 0
        MAX = 16 ** 8
        counts = [0, 0, 0, 0]

        group = "G05061227"
        original = "input/" + fname
        modified = "output/" + fname

        print()
        print_header()

        with open(original, 'rb') as original_file:
            original_text = original_file.read()

        while count < MAX:
            hexadecimal8 = '{:0>8x}'.format(count)
            proof = hexadecimal8 + " " + group
            modified_text = original_text + proof.encode()
            digest = sha256_digest(modified_text)

            if digest.startswith("00000"):
                seconds = time.time() - start_time
                str_time = get_time(seconds)
                if digest.startswith("00000000"):
                    print_data(8, proof, digest, count+1, str_time)
                    counts[0] += 1
                elif digest.startswith("0000000"):
                    print_data(7, proof, digest, count+1, str_time)
                    counts[1] += 1
                elif digest.startswith("000000"):
                    print_data(6, proof, digest, count+1, str_time)
                    counts[2] += 1
                    break
                else:
                    print_data(5, proof, digest, count+1, str_time)
                    counts[3] += 1

            count = count + 1
        if count < MAX:
            print()
            print("Success: Proof found before reaching maximum(" + str(MAX) + ")")
            with open(modified, 'wb') as modified_file:
                modified_file.write(modified_text)
        else:
            print()
            print("Fail: Proof not found before reaching maximum(" + str(MAX) + ")")

        print()
        print_summary(counts)

    else:
        print("Use: python " + sys.argv[0] + " <filename>")


if __name__ == "__main__":
    main()
