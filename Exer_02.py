nota_01, nota_02, nota_03 = float(input("Insira a primeira nota ")), float(input("Insira a segunda nota ")), float(input("Insira a terceira nota "))
peso_01, peso_02, peso_03 = float(input("Insira o primeiro peso ")), float(input("Insira o segundo peso ")), float(input("Insira o terceiro peso "))
media = ((peso_01 / 10) * nota_01) + ((peso_02 / 10) + nota_02) + ((peso_03 / 10) + nota_03) / (nota_03 + nota_02 + nota_03)
print("As suas notas são [",nota_01, nota_02, nota_03,"]")
print("Os Pesos são [",peso_01, peso_02, peso_03,"]")
print("A media Final é = ",media)