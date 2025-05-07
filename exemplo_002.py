nota_um = float(input("Entre com a primeira nota: "))
nota_dois = float(input("Entre com a segunda nota: "))
media = (nota_um + nota_dois) / 2

if media >= 5 and media <= 10:
    print(f"Você foi aprovado(a) com a média {media:.2f}.")
elif media < 5:
    print(f"Você foi reprovado(a) com a média {media:.2f}.")
elif media > 10:
    print("Média inválida! Entre com um número entre 0 e 10.")
else:
    print("Média inválida! Entre com um número inteiro.")