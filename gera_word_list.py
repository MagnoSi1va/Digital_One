import itertools
string = input("DIGITE LETRAS E NUMEROS BASE: ")
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))