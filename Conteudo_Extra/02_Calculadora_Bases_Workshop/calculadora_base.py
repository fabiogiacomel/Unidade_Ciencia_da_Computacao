# PROJETO 2: Calculadora de Conversão
# Objetivo: Transformar decimal em Binário, Octal e Hexadecimal.

def menu():
    print("\n--- CALCULADORA DE BASES ---")
    print("1. Decimal -> Binário")
    print("2. Decimal -> Octal (Desafio!)")
    print("3. Decimal -> Hexadecimal (Desafio!)")
    
    escolha = input("Escolha: ")
    numero = int(input("Digite o número decimal: "))
    
    if escolha == '1':
        # bin() é a função pronta do Python
        # [2:] serve para tirar o '0b' do começo
        resultado = bin(numero)[2:]
        print(f"O número {numero} em Binário é: {resultado}")
        
    elif escolha == '2':
        # MISSÃO: Pesquise a função oct() e complete aqui
        print("AINDA NÃO IMPLEMENTADO! Sua vez de programar.")
        
    elif escolha == '3':
        # MISSÃO: Pesquise a função hex() e complete aqui
        print("AINDA NÃO IMPLEMENTADO! Sua vez de programar.")

# Loop Infinito (Roda para sempre até dar erro ou fechar)
while True:
    menu()
