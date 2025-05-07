idades = []

for i in range(5):
    idades.append(int(input(f"Entre com a idade da {i+1}ª pessoa: ")))
media = sum(idades) / len(idades)
print(f"A média das idades é {media:.2f}.")

