# Conversor de Números: Decimal <-> Binário
# Use este programa para conferir seus exercícios!

def decimal_para_binario(numero):
    if numero < 0:
        return "Erro: Apenas números positivos."
    # A função bin() do Python faz a conversão. Ex: bin(5) retorna '0b101'
    # Usamos [2:] para pular o '0b' inicial.
    return bin(numero)[2:]

def binario_para_decimal(texto_binario):
    try:
        # A função int() com base 2 converte texto binário para número.
        return int(texto_binario, 2)
    except ValueError:
        return "Erro: Digite apenas 0 e 1."

# Menu Principal
while True:
    print("\n=== CONVERSOR DE BASES ===")
    print("1. Decimal para Binário")
    print("2. Binário para Decimal")
    print("3. Sair")
    
    opcao = input("Escolha (1-3): ")
    
    if opcao == '1':
        num = int(input("Digite um número decimal (ex: 10): "))
        resultado = decimal_para_binario(num)
        print(f"✅ O binário de {num} é: {resultado}")
        
    elif opcao == '2':
        bin_str = input("Digite um binário (ex: 1010): ")
        resultado = binario_para_decimal(bin_str)
        print(f"✅ O decimal de {bin_str} é: {resultado}")
        
    elif opcao == '3':
        print("Saindo... Bons estudos!")
        break
    else:
        print("Opção inválida.")
