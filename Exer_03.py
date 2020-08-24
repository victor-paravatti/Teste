e = (input("Insira {e} se quiser entrar "))
while (e == e ):
        salario, persentual = float(input("Insira o seu Salario  ")), float(input("Insira o Presentual De aumento  "))
        aumento = (salario * persentual) / 100
        salario_novo = aumento + salario
        print("O Aumento é = ",aumento)
        print("O novo Salario é = ",salario_novo)
        s = (input("Insira {s} se quiser sair ou {e} para continuar "))