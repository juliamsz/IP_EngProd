import math
import random

opcao = int(input())

if opcao == 1:
    velocidade = float(input())
    angulo = float(input())
    g = 9.81
    
    def calcularAlcance(v0, angulo):
        angulo_rad = math.radians(angulo)
        alcance = (v0 ** 2) * math.sin(2 * angulo_rad) / g
        return alcance  
    
    def calcularAltura (v0, angulo):
        angulo_rad = math.radians(angulo)
        altura = (v0 ** 2) * (math.sin(angulo_rad) ** 2) / (2 * g)
        return altura
    
    print(f"Alcance: {calcularAlcance(velocidade, angulo):.2f} m")
    print(f"Altura: {calcularAltura(velocidade, angulo):.2f} m")
    
elif opcao == 2:
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())
    
    def analisarLeituras(v1, v2, v3):
        media = (v1 + v2 + v3) / 3
        maximo = max(v1, v2, v3)
        minimo = min(v1, v2, v3)
        
        return media, maximo, minimo
    
    print(f"Média: {analisarLeituras(valor1, valor2, valor3)[0]:.2f}")
    print(f"Máximo: {analisarLeituras(valor1, valor2, valor3)[1]:.2f}")
    print(f"Mínimo: {analisarLeituras(valor1, valor2, valor3)[2]:.2f}")
    
elif opcao == 3:
    semente = int(input())
    
    def gerarChaves(semente):
        random.seed(semente)
        chave1 = random.randint(0, 1000)
        chave2 = random.randint(0, 1000)
    
        return chave1, chave2
    
    print(f"Chave A: {gerarChaves(semente)[0]:.2f}")
    print(f"Chave B: {gerarChaves(semente)[1]:.2f}")