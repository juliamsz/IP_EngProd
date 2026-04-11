opcao = int(input())

if opcao == 1:
    nomeCompleto = input("")
    
    print(f"{nomeCompleto.upper()}")
    print(f"{nomeCompleto.lower()}")
    nomeCompleto = nomeCompleto.strip()
    print(f"Total de letras: {len(nomeCompleto.replace(' ', ''))}")
    print(f"Letras no primeiro nome: {len(nomeCompleto.split()[0])}")
    
elif opcao == 2:
    nomeCompleto = input("")
    
    temSilva = "silva" in nomeCompleto.lower()
    print(f"O nome contém SILVA? {temSilva}")
    
elif opcao == 3:
    frase = input("")
    
    palindromo = frase.replace(" ", "").lower()
    ehPalindromo = palindromo == palindromo[::-1]
    
    print(f"A frase é um palíndromo: {ehPalindromo}")