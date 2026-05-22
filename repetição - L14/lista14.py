opcao = int(input())

if opcao == 1:
    numero = int(input())
    
    pares = 0
    somaImpares = 0
    maiorPar = 0
    
    while numero != 0:
        if numero < 0:
            numero = int(input())
            continue
        else:
            if numero % 2 == 0:
                pares += 1
                if numero > maiorPar:
                    maiorPar = numero
            else:
                somaImpares += numero
                
        numero = int(input())
        
    if maiorPar == 0:
        maiorPar = "Nenhum"
        
    print(f"Quantidade de pares: {pares}")
    print(f"Soma dos ímpares: {somaImpares}")
    print(f"Maior par: {maiorPar}")
    
if opcao == 2:
    cargaBateria = float(input())
    
    semBateria = False
    qntdManobras = 1
    
    while qntdManobras <= 5:
        consumo = float(input())
        
        if consumo == 999:
            break
        
        if consumo <= 0:
            continue
        
        cargaBateria -= consumo
            
        if cargaBateria < 0:
            print("Bateria esgotada: Drone pousando")
            print("Carga final: 0.00")
            print(f"Total de manobras: {qntdManobras}")
            
            semBateria = True
            break
                        
        qntdManobras += 1
    
    if not semBateria:
        print("Pouso de segurança: Resfriamento necessário")
        print(f"Carga final: {cargaBateria:.2f}")
        print(f"Total de manobras: {qntdManobras - 1}")