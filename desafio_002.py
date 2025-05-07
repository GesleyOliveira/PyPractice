altura = float(input("Entre com sua altura em metros: "))
peso = float(input("Entre com seu peso em kg: "))
sexo = input("Entre com seu sexo (M/F): ").upper()
if peso <= 0 or altura <= 0:
    print("Peso ou altura inválidos! Entre com um número positivo.")
else:
    if sexo == "M":
        imc = (72.7 * altura) - 58
        print(f"Seu peso ideal é {imc:.2f}kg.")
    elif sexo == "F":
        imc = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é {imc:.2f}kg.")
    elif sexo != "M" and sexo != "F":
        print("Sexo inválido! Entre com M ou F.")
    else:
        print("Dados inválidos! Entre com um dados válidos.")
