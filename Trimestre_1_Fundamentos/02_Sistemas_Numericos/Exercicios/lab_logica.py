# Laboratório de Lógica em Python
# Experimente mudar os valores das variáveis!

def testar_logica(a, b):
    print(f"\nAnalisando: A={a}, B={b}")
    print(f"1. A é maior que B? (A > B) -> {a > b}")
    print(f"2. A é igual a B? (A == B) -> {a == b}")
    print(f"3. A é diferente de B? (A != B) -> {a != b}")

def testar_conectivos(tem_dinheiro, tem_tempo):
    print("\n--- Planejando Viagem ---")
    print(f"Dinheiro: {tem_dinheiro} | Tempo: {tem_tempo}")
    
    # Lógica AND (Precisa dos dois)
    viagem = tem_dinheiro and tem_tempo
    print(f"Posso viajar? (AND) -> {viagem}")
    
    # Lógica OR (Basta um)
    feliz = tem_dinheiro or tem_tempo
    print(f"Estou pelo menos um pouco feliz? (OR) -> {feliz}")

# --- Execução ---
print("=== AULA DE LÓGICA ===")

# Teste 1: Comparação de Números
testar_logica(10, 5)
testar_logica(5, 5)

# Teste 2: Conectivos (Mude True/False para testar)
testar_conectivos(True, False) # Tenho dinheiro, mas não tenho tempo
testar_conectivos(True, True)  # Tenho os dois!
