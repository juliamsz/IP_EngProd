opcao = int(input())

if opcao == 1:

    usuario = tuple(input().split("-")) # separa os valores de acordo com o hífen
    nome, depto, seg = usuario
    seg = int(seg)

    # dicionário dos laboratórios
    laboratorios = {
        "L101": ("CC", 2),
        "L202": ("MAT", 3),
        "L303": ("FIS", 1)
    }

    lab = input()

    if lab not in laboratorios:
        print("Erro: Laboratório Inexistente.")

    else:
        depto_req, nivel_req = laboratorios[lab]

        if depto != depto_req:
            print("Acesso Negado: Departamento Inválido.")

        elif seg < nivel_req:
            print("Acesso Negado: Nível Insuficiente.")

        else:
            print("Acesso garantido.")

elif opcao == 2:
    compra = tuple(input().split("-"))
    pais, peso, preco = compra

    peso = float(peso)
    preco = float(preco)
    
    imposto = {
        "EUA": 0.20,
        "CHN": 0.10,
        "EUR": 0.15
    }
    
    if pais not in imposto:
        print("País não atendido.")
        
    else:
        preco += (preco * imposto[pais])
        
        if peso > 50:
            preco += 100
            print(f"{preco:.2f}")
        elif peso <= 50:
            preco += 50
            print(f"{preco:.2f}")
        