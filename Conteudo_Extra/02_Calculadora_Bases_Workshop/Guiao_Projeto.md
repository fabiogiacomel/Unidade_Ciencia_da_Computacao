# Projeto Extra 2: Workshop da Calculadora Binária 🧮

Este projeto conecta a teoria de **Sistemas Numéricos** (Trimestre 1) com a prática de **Python** (Trimestre 3).

## 🎯 O Desafio
Você recebeu um código incompleto. Ele só sabe converter para Binário.
Seu chefe pediu para adicionar **Octal** e **Hexadecimal** até o fim do dia!

## 🛠️ Como Funciona o Código
O Python já "sabe" converter números. Ele tem funções mágicas:
1.  `bin(10)` -> Transforma 10 em binário (`0b1010`).
2.  `oct(10)` -> Transforma 10 em octal (`0o12`).
3.  `hex(10)` -> Transforma 10 em hexadecimal (`0xa`).

## 🚀 Missão Kumon (Pequenos Passos)

1.  **Nível 1 (Pesquisa):**
    - Abra o código `calculadora_base.py`.
    - Veja como foi feito o `bin(numero)[2:]`.
    - O `[2:]` serve para cortar as duas primeiras letras (`0b`).

2.  **Nível 2 (Implementação Octal):**
    - Vá no `elif escolha == '2':`.
    - Apague o `print` de erro.
    - Escreva: `resultado = oct(numero)[2:]`
    - Mande imprimir o resultado.

3.  **Nível 3 (Implementação Hexa):**
    - Faça a mesma coisa para o `elif escolha == '3':`.
    - Use a função `hex()`.

**Teste Final:**
- Converta o número **255**.
- Binário deve dar: `11111111`
- Hexadecimal deve dar: `ff`
