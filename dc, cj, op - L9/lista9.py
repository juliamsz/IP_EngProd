import math
import random

opcao = int(input())

if opcao == 1:
    estoque = {}
    
    produto1, qntd1 = input().split() # separa os valores de acordo com o espaço
    produto2, qntd2 = input().split()
    estoque[produto1] = int(qntd1) # converte a quantidade para inteiro e armazena no dicionário    
    estoque[produto2] = int(qntd2)
    
    estoque[produto1] += int(input())
    
    produto3, qntd3 = input().split()
    estoque[produto3] = int(qntd3)
    
    print(estoque)
    
elif opcao == 2:
    listaA = input().split()   
    listaB = input().split()
    
    interseccao = sorted(set(listaA) & set(listaB))
    uniao = sorted(set(listaA) | set(listaB))
    
    print(f"Intersecção: {interseccao}")
    print(f"União: {uniao}")  
    
elif opcao == 3:
    lista = {}
    
    nomeA, nota1A, nota2A, nota3A = input().split()
    nota1A, nota2A, nota3A = float(nota1A), float(nota2A), float(nota3A)
    
    nomeB, nota1B, nota2B, nota3B = input().split()
    nota1B, nota2B, nota3B = float(nota1B), float(nota2B), float(nota3B)
    
    nomeC, nota1C, nota2C, nota3C = input().split()
    nota1C, nota2C, nota3C = float(nota1C), float(nota2C), float(nota3C)
    
    lista[nomeA] = [nota1A, nota2A, nota3A]
    lista[nomeB] = [nota1B, nota2B, nota3B]
    lista[nomeC] = [nota1C, nota2C, nota3C]
    
    busca = input()
    
    notas = lista[busca]
    
    media = (notas[0] + notas[1] + notas[2]) / 3
    
    print(f"{busca} - Média: {media:.2f}")
    
    if media > 7:
        print("Status: Aprovado")
    else:
        print("Status: Reprovado")
    