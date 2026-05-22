opcao = int(input())

if opcao == 1:
    categoria = input()
    valor = float(input())

    match categoria:
        case "Estudante":
            desconto = valor * 0.15

        case "Aposentado":
            desconto = valor * 0.20

        case "Fiel":
            desconto = valor * 0.10

        case _:
            desconto = 0

    total = valor - desconto

    print(f"Desconto: {desconto:.2f}")
    print(f"Total: {total:.2f}")
    
elif opcao == 2:
    comando = input().split()

    match comando[0]:

        case "subir":
            valor = int(comando[1])

            if valor > 100:
                valor = 100
                print("Limite atingido: Subindo 100mm")
            else:
                print(f"Subindo {valor}mm")

        case "girar":
            valor = int(comando[1])

            if valor % 90 == 0:
                print(f"Girando {valor} graus")
            else:
                print("Ângulo inválido")

        case "garra":
            valor = comando[1]

            if valor == "abrir" or valor == "fechar":
                print(f"Garra {valor}")
            else:
                print("Erro: Comando desconhecido")

        case _:
            print("Erro: Comando desconhecido")
    