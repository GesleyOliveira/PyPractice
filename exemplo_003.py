nota = float(input("Entre com a nota: "))

if nota > 7 and nota <= 9.5:
    nota += 0.5
    print(f"Sua nota é {nota:.2f}.")
elif nota == 10:
    print("Sua nota é 10.0!")
elif nota <= 7:
    print(f"Sua nota é {nota:.2f}.")
elif nota > 10:
    print("Média inválida! Entre com um número entre 0 e 10.")
else:
    print("Média inválida! Entre com um número inteiro.")