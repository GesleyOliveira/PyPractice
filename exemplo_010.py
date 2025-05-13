idades = []

while True:
    idade = int(input("Digite a idade: "))
    if idade == -1:
        break
    else:
        idades.append(idade)
        continue

tupla_idades = tuple(idades)
quantidade_idades = len(tupla_idades)
media_idades = sum(tupla_idades) / quantidade_idades
print(f"A tupla é: {tupla_idades}, com {quantidade_idades} idades, e média de {media_idades:.2f} anos.")