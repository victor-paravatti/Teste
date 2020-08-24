N1 = int(input("insira un numero inteiro"))
while N1 <= 0:
    N1 = int(input("insira un numero inteiro"))
else:
    quadrado = N1 ** 2
    cubo = N1 ** 3
    raiz = N1 ** (1 / 2)
    raiz3 = N1 ** (1 / 3)
    soma = raiz + raiz3
    print(quadrado, " ", cubo, " ", raiz, " ", raiz3, " ", soma)
