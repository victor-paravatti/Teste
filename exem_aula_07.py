# Exemplo 6 - É o mesmo exemplo anterior, porém automatizando o número a ser descoberto. Utilize randint para escolher um número entre os intervalos
# inferior e superior informado.
from random import randint
cont = 0
i, j = int(input('Digite o número inicial: ')), int(input('Digite o número final: '))
k = randint(i, j)
print(f'O número está entre {i} e {j}.\n')
w = int(input('Qual é o número? Digite um:  '))
while w != k:
    if w > k:
        cont += 1
        w = int(input('Escolha um número menor: '))
    elif w < k:
        cont += 1
        w = int(input('Escolha um número maior: '))
else:
    print(f'Acertou!!! Parabéns!!! \nDemorou {cont} tentativas!')
