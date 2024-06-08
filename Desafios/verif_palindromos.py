# Teste se uma palavra é um palíndromo

# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Remove espaços em branco e converte a palavra para minúsculas
palavra = palavra.replace(" ", "").lower()

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
