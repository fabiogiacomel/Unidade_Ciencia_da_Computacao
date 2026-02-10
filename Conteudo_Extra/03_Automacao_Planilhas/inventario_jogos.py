# PROJETO 3: Gerente de Inventário de Jogos
# Objetivo: Criar uma planilha (Excel) automaticamente usando Python.

import csv

# Lista de Jogos (Dicionário)
inventario = [
    {"Nome": "Minecraft", "Preço": 120.00, "Plataforma": "PC"},
    {"Nome": "FIFA 2026", "Preço": 300.00, "Plataforma": "PS5"},
    {"Nome": "Zelda: Tears of the Kingdom", "Preço": 250.00, "Plataforma": "Switch"},
    {"Nome": "Fortnite", "Preço": 0.00, "Plataforma": "Multi"}
]

# Nome do arquivo
arquivo_nome = "meus_jogos.csv"

print(f"Criando arquivo '{arquivo_nome}'...")

# Escrevendo no arquivo
with open(arquivo_nome, mode='w', newline='', encoding='utf-8') as arquivo:
    # Definindo as colunas
    campos = ["Nome", "Preço", "Plataforma"]
    
    # Criando o escritor
    escritor = csv.DictWriter(arquivo, fieldnames=campos, delimiter=';')
    
    # Escrevendo o cabeçalho
    escritor.writeheader()
    
    # Escrevendo os dados
    for jogo in inventario:
        escritor.writerow(jogo)
        print(f"Adicionado: {jogo['Nome']}")

print("\n✅ Sucesso! Abra o arquivo 'meus_jogos.csv' no Excel.")
