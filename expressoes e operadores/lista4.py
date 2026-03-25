import math

def main():
    opcao = input()

    if opcao == "1":

        angulo = math.radians(float(input())) # recebe o ângulo em graus e converte para radianos
        altura = float(input())
        compEscada = altura / math.sin(angulo)

        print(f"O comprimento da escada é: {compEscada:.2f}")

    elif opcao == "2":
        # infos
        # '//' é o operador de divisão inteira, que retorna o quociente sem a parte decimal
        # '%' é o operador de módulo, que retorna o resto da divisão

        totalSegundos = int(input())
        horas = totalSegundos // 3600 
        minutos = (totalSegundos % 3600) // 60 
        segundos = totalSegundos % 60

        print(f"Horas: {horas}\nMinutos: {minutos}\nSegundos: {segundos}")


    elif opcao == "3":
        raio = float(input())
        altura = float(input())
        area = 2 * math.pi * raio * (raio + altura)

        print(f"A área da superfície é: {area:.2f}")

    else:
        print("Opção inválida! Reinicie o programa.")

if __name__ == "__main__":
    main()