"""numero_um = int(input("Entre com um número: "))
numero_dois = int(input("Entre com outro número: "))
print(f"A soma dos números é: {numero_um + numero_dois}")
print(f"A subtração dos números é: {numero_um - numero_dois}")
print(f"A multiplicação dos números é: {numero_um * numero_dois}")"""

# Comentário em uma linha
"""Comentário em múltiplas linhas
    Comentário em múltiplas linhas
    Comentário em múltiplas linhas
"""
# Ou
'''
Comentário em múltiplas linhas  
Comentário em múltiplas linhas
Comentário em múltiplas linhas
'''

# slice: serve para pegar partes de uma string, um fatiamento
# Exemplo: "0123456789"[:5] = 01234

'''numero = "0123456789"
print(numero[0:6:2])''' 

# Ou seja: primeiro quando inicia, 
# depois o limite superior (não incluso), depois o passo

#strip: serve para remover espaços em branco no início e no final da string
# Exemplo: "   Olá, Mundo!   ".strip() = "Olá, Mundo!"
# lstrip: serve para remover espaços em branco no início da string 
# Exemplo: "   Olá, Mundo!   ".lstrip() = "Olá, Mundo!   "
# rstrip: serve para remover espaços em branco no final da string   
# Exemplo: "   Olá, Mundo!   ".rstrip() = "   Olá, Mundo!"

nome = "   Gesley de Oliveira Rosa   "  
'''print(nome.strip())
print(nome.lstrip())
print(nome.rstrip())'''
'''
print(nome.upper()) # transforma a string em maiúscula
print(nome.lower()) # transforma a string em minúscula
print(nome.title()) # transforma a string em título (primeira letra de cada palavra em maiúscula)
print(nome.capitalize()) # transforma a string em título (primeira letra da string em maiúscula)
'''

# def formatar nome_completo(nome_completo):
# email = input("Entre com seu e-mail: ")

#dividir_email = email.strip('@', '.')

"""partes_uteis = email.split('@')
partes_uteis = email.split('.')

quantidade_palavras = len(partes_uteis)

print(f"Seu email: {email} está dividido em {quantidade_palavras} partes: {partes_uteis}, mas as mais importantes são: {partes_uteis[0]} e {partes_uteis[1]}")
"""

'''numero = int(input("Entre com um número: "))
type(numero) # verifica o tipo da variável
texto = input("Entre com um texto: ")
x = float(numero)
texto = texto.upper()
print(f"Seu número é: {x} e seu texto é: {texto}")'''

# Exemplo de função 
# def soma(a, b):
#     return a + b
#
# def subtracao(a, b):
#     return a - b
#
# def multiplicacao(a, b):
#     return a * b
#
# def divisao(a, b):    
#     return a / b
#
# def calculadora(a, b, operacao):
#     if operacao == '+':
#         return soma(a, b)
#     elif operacao == '-':
#         return subtracao(a, b)
#     elif operacao == '*':
#         return multiplicacao(a, b)
#     elif operacao == '/':
#         return divisao(a, b)
#     else:
#         return "Operação inválida"
#
# numero_um = int(input("Entre com um número: "))
# numero_dois = int(input("Entre com outro número: "))
# operacao = input("Entre com a operação (+, -, *, /): ")
# resultado = calculadora(numero_um, numero_dois, operacao)
# print(f"O resultado da operação {operacao} entre {numero_um} e {numero_dois} é: {resultado}")
# Exemplo de função com retorno
