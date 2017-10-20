import sys

def str_to_hex():
    s = input('Escribe tu nombre:\n')
    print("Tu nombre en hexadecimal es:\n")
    for char in s:
        sys.stdout.write(hex(ord(char)))
        sys.stdout.write(' ')
    sys.stdout.flush()



if __name__ == '__main__':
    str_to_hex()
