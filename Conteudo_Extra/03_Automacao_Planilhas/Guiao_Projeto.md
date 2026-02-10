# Projeto Extra 3: Automação de Escritório 📊

Este projeto conecta a teoria de **Planilhas** (Trimestre 2) com a prática de **Programação** (Trimestre 3).

## 🎯 O Desafio
Em vez de digitar 100 jogos no Excel um por um, vamos criar um **Robô** (Script) que faz isso para nós.
Isso se chama **Automação**. É uma habilidade muito valorizada no mercado de trabalho!

## 🛠️ Como Funciona o Código
O script `inventario_jogos.py` usa a biblioteca `csv`.
Ela pega uma lista de dados no Python e transforma em um arquivo que o Excel entende.

## 🚀 Missão Kumon (Pequenos Passos)

1.  **Nível 1 (Execução):**
    - Rode o código.
    - Baixe o arquivo `meus_jogos.csv` (no Colab, fica na pastinha lateral).
    - Abra no Excel ou Google Sheets. Veja a mágica!

2.  **Nível 2 (Expansão):**
    - Adicione mais 2 jogos na lista `inventario` dentro do código.
    - Rode de novo e veja se eles aparecem na planilha.

3.  **Nível 3 (Interatividade - Desafio Final):**
    - Mude o código para perguntar o nome do jogo (`input`) em vez de já ter a lista pronta.
    - Use um `while` para adicionar jogos até o usuário digitar "pare".

---
**Exemplo de código para o Nível 3:**
```python
while True:
    nome = input("Nome do Jogo (ou 'pare'): ")
    if nome == "pare":
        break
    # ... adicione na lista ...
```
