# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def multiplicar(a, b):
    return a * b
    
print("Bem-vindo ao Menu de Operações!")
print("1. Somar")
print("2. Subtrair")
print("3. Dividir")
print("4. Multiplicar")

escolha = input("Escolha uma opção (1-4): ")

if escolha == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = somar(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "2":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = subtrair(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "3":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = dividir(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "4":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = multiplicar(num1, num2)
    print("Resultado: ", resultado)
else:
    print("Opção inválida.")