opcao = int(input())

if opcao == 1:
    nome = input("")
    nota1 = float(input())
    nota2 = float(input())
    nFaltas = int(input())
    nAulas = int(input())

    media = (nota1 + nota2) / 2
    frequencia = (nAulas - nFaltas) / nAulas
    notaAprovada = media >= 6
    frequenciaAprovada = frequencia >= 0.75

    if notaAprovada and frequenciaAprovada:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"Nome do aluno: {nome} \nMedia das notas: {media:.2f} \nFrequencia: {100*(frequencia)} \nSituação final: {situacao}")

elif opcao == 2:
    nome = input("")

    hamburguers = int(input())
    refrigerantes = int(input())
    sobremesas = int(input())

    valorDesconto = 0
    valorNovo = 0

    valorTotal = hamburguers * 18 + refrigerantes * 7 + sobremesas * 9

    if valorTotal > 50:
        valorDesconto = valorTotal * 0.1

    valorNovo = valorTotal - valorDesconto
    print(f"Nome do cliente: {nome} \nValor total sem descontos: R${valorTotal:.2f}  \nValor do desconto: R${valorDesconto:.2f} \nValor final: R${valorNovo:.2f}")

    if hamburguers >= 2 and sobremesas >= 1:
        print("Ganhou brinde, parabens!")
    else:
        print("Não ganhou o brinde.")