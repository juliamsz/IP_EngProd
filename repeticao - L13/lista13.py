opcao = int(input())

if opcao == 1:
    n = int(input())
    tanqueA = list(map(float, input().split()))
    tanqueB = list(map(float, input().split()))
    
    for i, (a,b) in enumerate(zip(tanqueA, tanqueB), start=1):
        if a < 0 or b < 0:
            continue
        
        diferenca = abs(a - b)
        if diferenca > 20:
            print(f"Alerta Medição {i}: Diferença de {diferenca:.2f}")
        else:
            print(f"Medição {i}: OK")
    
elif opcao == 2:
    capacidade = float(input())
    itens = int(input())
    
    nome = list(map(str, input().split()))
    peso = list(map(float, input().split()))
    categoria = list(map(str, input().split()))
    
    pesoTotal = 0
    
    for i, (n, p, c) in enumerate(zip(nome, peso, categoria), start=1):
        if c == "Perigoso":
            continue
        
        if pesoTotal + p > capacidade:
            print(f"Capacidade atingida")
            break
    
        print(f"Item {i} ({n}) carregado.")
        pesoTotal += p
            
    print(f"Peso Total: {pesoTotal:.2f}")