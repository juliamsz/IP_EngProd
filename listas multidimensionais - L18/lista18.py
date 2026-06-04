opcao = int(input())

if opcao == 1:
    nCidades = int(input())
    nDias = int(input())

    matrizTemp = []

    def analisarTemperaturas():
        mediasTemps = []

        maiorTemp = matrizTemp[0][0]
        menorTemp = matrizTemp[0][0]

        maiorCidade = 0
        menorCidade = 0

        maiorDia = 0
        menorDia = 0

        for i in range(len(matrizTemp)):
            soma = 0

            for j in range(len(matrizTemp[i])):
                temp = matrizTemp[i][j]
                soma += temp

                if temp > maiorTemp:
                    maiorTemp = temp
                    maiorCidade = i
                    maiorDia = j

                if temp < menorTemp:
                    menorTemp = temp
                    menorCidade = i
                    menorDia = j

            mediasTemps.append(soma / len(matrizTemp[i]))

        return (
            mediasTemps,
            maiorTemp,
            maiorCidade,
            maiorDia,
            menorTemp,
            menorCidade,
            menorDia
        )

    for i in range(nCidades):
        linha = list(map(float, input().split()))
        matrizTemp.append(linha)

    resultado = analisarTemperaturas()

    medias = resultado[0]
    maiorTemp = resultado[1]
    maiorCidade = resultado[2]
    maiorDia = resultado[3]
    menorTemp = resultado[4]
    menorCidade = resultado[5]
    menorDia = resultado[6]

    for i in range(len(medias)):
        print(f"Cidade {i + 1}: Média de {medias[i]:.2f}°C")

    print(f"Pico de calor: {maiorTemp}°C registrado no Dia {maiorDia + 1} e na Cidade {maiorCidade + 1}")
    print(f"Pico de frio: {menorTemp}°C registrado no Dia {menorDia + 1} e na Cidade {menorCidade + 1}.")

elif opcao == 2:
    nLinhas = int(input())
    nColunas = int(input())

    grade = []

    def avaliarTerreno():
        totalObstaculos = 0

        alvoLinha = -1
        alvoColuna = -1

        for i in range(len(grade)):
            for j in range(len(grade[i])):

                if grade[i][j] == 1:
                    totalObstaculos += 1

                elif grade[i][j] == 2:
                    alvoLinha = i
                    alvoColuna = j
                    grade[i][j] = "X"

        return totalObstaculos, alvoLinha, alvoColuna, grade

    for i in range(nLinhas):
        entrada = input().strip()

        linha = []

        for j in entrada:
            if j.isdigit():
                linha.append(int(j))

        grade.append(linha)

    resultado = avaliarTerreno()

    totalObstaculos = resultado[0]
    alvoLinha = resultado[1]
    alvoColuna = resultado[2]
    gradeAtualizada = resultado[3]

    if alvoLinha == -1:
        print("Alerta: Alvo não encontrado na grade. Pouso abortado.")
        print(f"Total de obstáculos detectados: {totalObstaculos}")
        print("Quadricóptero não pousou.")

    else:
        print(f"Alvo localizado em: ({alvoLinha}, {alvoColuna})")
        print(f"Total de obstáculos detectados: {totalObstaculos}")
        print("Quadricóptero pousado:")

        for i in range(len(gradeAtualizada)):
            for j in range(len(gradeAtualizada[i])):
                print(gradeAtualizada[i][j], end="")
            print()