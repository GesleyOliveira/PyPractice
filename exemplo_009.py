cidades = []

while True:
    cidade = input("Entre com o nome da cidade, ou 'Sair': ")
    cidade = cidade.strip().title()
    if cidade in cidades:
        print(f"A cidade {cidade} já foi digitada.")
        continue
    elif len(cidade) < 3 or cidade == " ":
        print("Entre com uma cidade válida.")
        continue 
    elif cidade == "Sair":
        if cidades == []:
            print("Nenhuma cidade foi digitada.")
            print("Saindo...")
            break
        else:
            for i in range(len(cidades)):
                print(f"{i+1}° cidade: {cidades[i]}")
            break
    else:
        cidades.append(cidade)
        cidades.sort()
        continue