numero = int(input("Entre com um número: "))

if numero % 2 == 0 and numero > 0:
    print(f"O número {numero} é par e positivo.")
elif numero % 2 == 0 and numero < 0:
    print(f"O número {numero} é par e negativo.")
elif numero % 2 != 0 and numero > 0:
    print(f"O número {numero} é ímpar e positivo.")
elif numero % 2 != 0 and numero < 0:
    print(f"O número {numero} é ímpar e negativo.")
elif numero == 0:
    print("O número é zero.")
else:   
    print("Número inválido! Entre com um número inteiro.")

# numero = [n for n in range(1, 101) if n % 2 == 0]