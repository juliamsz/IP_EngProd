opcao = int(input())

if opcao == 1:
    diasTreino = int(input())
    distanciaTotal = 0
    
    def avaliarTreino (distancia, tempo):
        velocidade = distancia * 60 / tempo
        if velocidade >= 12:
            return velocidade, "Desempenho: Alta Performance"
        elif velocidade >= 8:
            return velocidade, "Desempenho: Moderado"
        else:
            return velocidade, "Desempenho: Baixo"

    for i in range(diasTreino):
        distancia, tempo = map(float, input().split())
        distanciaTotal += distancia
        
        print(f"Velocidade: {avaliarTreino(distancia, tempo)[0]:.2f} km/h - {avaliarTreino(distancia, tempo)[1]}")
        
    print(f"Distancia total: {distanciaTotal:.2f} km")
    
elif opcao == 2:
    malas = 0

    while True:

        peso = float(input())

        if peso < 0:
            print("Erro de leitura: Peso negativo ignorado")
            continue

        if peso == 0:
            print("Processamento encerrado pelo operador.")
            break

        if peso > 32:
            print("Alerta: Limite de peso excedido! Esteira bloqueada.")
            break

        malas += 1

        if peso <= 23:
            print(f"Mala {malas}: Padrao")

        else:
            print(f"Mala {malas}: Excesso leve")

        if malas == 5:
            print("Lote concluído: Enviar para inspeção")
            break

    print(f"Total de malas processadas: {malas}")
