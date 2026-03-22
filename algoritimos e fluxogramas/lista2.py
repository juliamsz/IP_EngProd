print("=== MENU DE EXERCÍCIOS DE ALGORITMOS E FLUXOGRAMAS ===")
print("1 - Cálculo de Desconto")
print("2 - Conversor de Moedas (R$ para US$)")
print("3 - Calculadora de IMC")
print("0 - Sair")
print("==================================")

opcao = input("Escolha uma opção (0, 1, 2 ou 3): ")

if opcao == "1":
    print("\n[EXERCÍCIO 1: CÁLCULO DE DESCONTO]")

    #ADICIONAR AQUI O ALGORITMO DO EXERCÍCIO 1
    valor_inicial = input("")
    percentual = input("")
    desconto = float(valor_inicial) * (float(percentual)/100)
    valor_final = float(valor_inicial) - desconto

    print(f"O desconto foi de: R$ {desconto:.2f}")
    print(f"O valor final a pagar é: R$ {valor_final:.2f}")


elif opcao == "2":
    print("\n[EXERCÍCIO 2: CONVERSOR DE MOEDAS]")

    #ADICIONAR AQUI O ALGORITMO DO EXERCÍCIO 2
    valor_reais = input("")
    cotacao_dolar = input("")
    cotacao = float(valor_reais) / float(cotacao_dolar)

    print(f"Com R$ {float(valor_reais):.2f}, você pode comprar US$ { cotacao:.2f}")


elif opcao == "3":
    print("\n[EXERCÍCIO 3: CALCULADORA DE IMC]")

    #ADICIONAR AQUI O ALGORITMO DO EXERCÍCIO 3
    peso = input("")
    altura = input("")
    imc = float(peso) / (float(altura) ** 2)
    
    print(f"Seu IMC é: {imc:.2f}")


elif opcao == "0":
    print("Saindo do programa...")

else:
    print("Opção inválida! Reinicie o programa.")