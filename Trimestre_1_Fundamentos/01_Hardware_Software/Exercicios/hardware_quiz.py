# Quiz Interativo: Hardware ou Software?
# Este programa ajuda você a testar seus conhecimentos sobre o conteúdo da Aula 01.

def perguntar(pergunta, resposta_correta):
    print("--------------------------------------------------")
    print("PERGUNTA: O item '" + pergunta + "' é Hardware (h) ou Software (s)?")
    resposta = input("Sua resposta (h/s): ").lower()
    
    if resposta == resposta_correta:
        print("✅ CORRETO! Muito bem.")
        return 1
    else:
        print("❌ INCORRETO. A resposta certa era '" + resposta_correta + "'.")
        return 0

# Início do Quiz
print("=== QUIZ DE INFORMÁTICA: HARDWARE vs SOFTWARE ===")
print("Instruções: Digite 'h' para Hardware ou 's' para Software.\n")

pontos = 0

# Perguntas (Repetição para fixação - Método Kumon)
pontos += perguntar("Teclado", "h")
pontos += perguntar("Windows 10", "s")
pontos += perguntar("Monitor", "h")
pontos += perguntar("Microsoft Word", "s")
pontos += perguntar("Placa de Vídeo", "h")
pontos += perguntar("Jogo Minecraft", "s")

# Resultado Final
print("--------------------------------------------------")
print(f"Fim do Quiz! Você acertou {pontos} de 6 perguntas.")

if pontos == 6:
    print("🏆 PARABÉNS! Você dominou o conceito!")
elif pontos >= 4:
    print("👍 Bom trabalho! Revise os erros para chegar à perfeição.")
else:
    print("📚 Precisa estudar mais um pouco a Aula 01.")
