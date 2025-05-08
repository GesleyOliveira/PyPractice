soma = 0

numero = input("Entre com um número: ")

for i in numero:
    soma += int(i)
print(f"A soma dos números é {soma}.")


qtd = 0

while True:
    numero = input("Entre com um número: ")  
    if numero == "0":
        print(f"A quantidade de número digitados foi {qtd}.")
        break
    else: 
        soma = 0
        for i in numero:
            soma += int(i)
        print(f"A soma dos números é {soma}.")
        qtd += 1
        
          

    numero = int(input("Entre com um número: "))
    soma = 0    
    resta = 0
    
    while numero != 0:
        resta = numero % 10
        soma += resta
        numero = int(numero / 10)
    print(f"A soma dos números é {soma}.")



