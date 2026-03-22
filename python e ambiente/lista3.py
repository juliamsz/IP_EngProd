opcao = input()

if opcao == "1":
    nome = str(input())
    anoNascimento = int(input())
    idade = int(2026 - anoNascimento)

    print(f"Olá, {nome}! Você tem {idade} anos.")


elif opcao == "2":
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    media = (nota1 + nota2 + nota3) / 3

    print(f"A média das notas é: {media:.2f}.")

elif opcao == "3":
    forca = float(input())
    area = float(input())

    pressao = forca / area

    print(f"A pressão calculada é: {pressao:.2f} Pa.")

else:
    print("Opção inválida! Reinicie o programa.")