idade = int(input("Entre com sua idade: "))
if idade >= 18 and idade < 110:
    print("Parabéns! Você já é maior de idade.")
elif idade < 18:
    print("Espere mais um pouco! Você ainda não é maior de idade.")
elif idade >= 110:
    print("Você é um(a) verdadeiro(a) guerreiro(a)! Ou está mentindo a sua idade")
else: 
    print("Idade inválida! Entre com um número inteiro.")