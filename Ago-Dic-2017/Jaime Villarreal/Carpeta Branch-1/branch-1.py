def str_to_bin():
    s = input('Escribe tu nombre:\n')
    bin_s = ' '.join(format(ord(x), 'b') for x in s)
    print("Tu nombre en binario es:\n{}".format(bin_s))


if __name__ == '__main__':
    str_to_bin()
