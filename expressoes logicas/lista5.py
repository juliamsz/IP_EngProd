import math

def main():
    opcao = input()

    if opcao == "1":
        # tirar duvida se era assim que era pra fazer

        idade = int(input())
        temAutorizacao = bool(int(input())) 
        estaAcompanhado = bool(int(input()))

        acesso = bool(idade >= 18 or (temAutorizacao == 1 and estaAcompanhado == 1))
    
        print(f"Acesso permitido: {acesso}")

    elif opcao == "2":
        # reexplicando a proposta: XOR é uma operação lógica que retorna 1 se os bits comparados forem diferentes e 0 se forem iguais.
        # logo, é so comparar os bits de valor e chaveMask usando XOR (^) para obter o resultado, depois deslocar os bits
        valor = int(input())
        chaveMask = int(input())

        resultado = (valor ^ chaveMask) << 1

        print(f"Resultado: {resultado}")

    elif opcao == "3":
        ladoA = float(input())
        ladoB = float(input())
        ladoC = float(input())

        trianguloValido = bool(ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB)

        if trianguloValido:
            print(f"É um triângulo: Sim")
        else:
            print(f"É um triângulo: Não")

    else:
        print("Opção inválida! Reinicie o programa.")

if __name__ == "__main__":
    main()