# Gerador de Dados para Excel (CSV)
# Este programa cria um arquivo que pode ser aberto no Excel!

import csv
import random

# Nome do arquivo que vamos criar
nome_arquivo = "notas_alunos.csv"

# Dados que vamos gravar (Cabeçalho)
dados = [
    ["Nome do Aluno", "Nota 1", "Nota 2", "Nota 3"], # Cabeçalho
]

# Gerando dados aleatórios para 5 alunos
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

print("Gerando notas aleatórias...")

for nome in nomes:
    n1 = random.randint(5, 10) # Nota entre 5 e 10
    n2 = random.randint(4, 9)
    n3 = random.randint(6, 10)
    dados.append([nome, n1, n2, n3]) # Adiciona na lista

# Gravando o arquivo CSV
try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';') # O Excel em PT-BR usa ponto e vírgula
        escritor.writerows(dados)
    
    print(f"✅ Sucesso! O arquivo '{nome_arquivo}' foi criado.")
    print("-> AGORA: Abra este arquivo no Excel e calcule a MÉDIA das notas!")
    
except Exception as e:
    print(f"❌ Erro ao criar arquivo: {e}")
