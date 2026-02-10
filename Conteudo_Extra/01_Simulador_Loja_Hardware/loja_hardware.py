# PROJETO 1: Simulador de Loja de Hardware (Desafio)
# Objetivo: Você é o vendedor. O cliente pede uma peça pelo que ela FAZ,
# e você tem que entregar a peça certa pelo NOME.

def atender_cliente():
    print("\n--- Cliente chegando na loja... ---")
    print("Cliente: 'Olá! Meu computador está muito lento para pensar. Preciso da peça que processa os dados.'")
    print("Opções: [HD] [CPU] [Placa-Mãe]")
    
    resposta = input("Você entrega: ").upper() # Transforma em maiúsculo
    
    if resposta == "CPU" or resposta == "PROCESSADOR":
        print("✅ Cliente: 'Isso mesmo! O cérebro do PC. Obrigado!'")
        return 10 # Ganha 10 moedas
    else:
        print(f"❌ Cliente: 'Hã? {resposta}? Isso não processa nada. Vou embora.'")
        return 0

def atender_cliente_2():
    print("\n--- Outro cliente... ---")
    print("Cliente: 'Quero guardar minhas fotos para sempre. Mesmo se desligar a luz.'")
    print("Opções: [Memória RAM] [HD] [Fonte]")
    
    resposta = input("Você entrega: ").upper()
    
    if resposta == "HD" or resposta == "SSD" or resposta == "DISCO RIGIDO":
        print("✅ Cliente: 'Perfeito! Vou salvar tudo aqui.'")
        return 10
    else:
        print("❌ Cliente: 'Isso perde os dados se desligar. Não serve!'")
        return 0

# --- Início do Jogo ---
print("=== BEM-VINDO À LOJA DE HARDWARE ===")
saldo = 0

saldo += atender_cliente()
saldo += atender_cliente_2()

print(f"\n💰 Fim do dia! Você ganhou {saldo} moedas.")

if saldo == 20:
    print("🏆 Funcionário do Mês!")
elif saldo == 0:
    print("💀 A loja faliu...")
else:
    print("😐 Dá para melhorar.")
