fruta = str(input("Digite o nome de uma fruta (Banana, Maça ou Cereja): ")).lower()

if fruta == "banana":   
    print("O kg da banana custa R$ 5,23.")
elif (fruta == "maça") or (fruta == "maca"):
    print("O kg da maça custa R$ 12,10.")
elif fruta == "cereja":
    print("O kg da cereja custa R$ 58,00.")
else:
    print("Fruta inválida! Entre com uma fruta válida.")