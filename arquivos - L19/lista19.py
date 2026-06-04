opcao = int(input())

if opcao == 1:
    nomeArquivo = input()
    nRegistros = int(input())

    arquivo = open(nomeArquivo, "w")

    for i in range(nRegistros):
        linha = input()
        arquivo.write(linha + "\n")

    arquivo.close()

    arquivoLeitura = input()

    try:
        arquivo = open(arquivoLeitura, "r")

        totalVendas = 0

        maiorVenda = 0
        vendedorMaiorVenda = ""

        print("Conteúdo do Arquivo")

        for linha in arquivo:
            linha = linha.strip()

            print(linha)

            dados = linha.split(",")

            vendedor = dados[0]
            valorVenda = float(dados[1])
            regiao = dados[2]

            totalVendas += valorVenda

            if valorVenda > maiorVenda:
                maiorVenda = valorVenda
                vendedorMaiorVenda = vendedor

        arquivo.close()

        print("---")
        print(f"Total geral de vendas: R$ {totalVendas:.2f}")
        print(f"Maior venda: {vendedorMaiorVenda} (R$ {maiorVenda:.2f})")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivoLeitura}' nao foi encontrado. Operacao abortada.")
        
elif opcao == 2:
    nomeArquivo = input()

    nAlunos = int(input())

    arquivo = open(nomeArquivo, "w")

    for i in range(nAlunos):
        linha = input()
        arquivo.write(linha + "\n")

    arquivo.close()

    arquivoLeitura = input()

    arquivo = open(arquivoLeitura, "r")
    relatorio = open("relatorio.txt", "w")
    erros = open("erros_notas.txt", "w")

    houveErro = False

    for linha in arquivo:
        linha = linha.strip()

        dados = linha.split(";")

        ra = dados[0]
        nome = dados[1]

        try:
            nota1 = float(dados[2])
            nota2 = float(dados[3])

            media = (nota1 + nota2) / 2

            if media >= 5:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"

            relatorio.write(f"{ra};{nome};{media:.2f};{situacao}\n")

        except ValueError:
            erros.write(f"Dados inválidos encontrados no RA {ra}\n")
            houveErro = True

    arquivo.close()
    relatorio.close()
    erros.close()

    print("Relatório de Notas")

    relatorio = open("relatorio.txt", "r")

    for linha in relatorio:
        print(linha.strip())

    relatorio.close()

    print("---")
    print("Detecção de Erros")

    if houveErro:
        erros = open("erros_notas.txt", "r")

        for linha in erros:
            print(linha.strip())

        erros.close()

    else:
        print("Nenhum erro encontrado.")