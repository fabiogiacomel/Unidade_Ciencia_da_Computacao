# Python: Variáveis e Tipos de Dados

> **Metodologia:** Kumon (Pequenos passos, Exemplos, Prática imediata)

---

## Passo 1: O que é uma Variável?

**Explicação:**
Uma variável é uma **caixinha** na memória do computador onde guardamos informações.
Você dá um nome para a caixinha e põe um valor dentro.

**Exemplo:**
```python
idade = 15      # Guardei o número 15 na caixa 'idade'
nome = "Ana"    # Guardei o texto "Ana" na caixa 'nome'
```

### Exercício 1
Se eu escrever `pontos = 100`, qual é o nome da variável?
( ) 100
( ) pontos

---

## Passo 2: Tipos de Dados

**Explicação:**
O Python precisa saber O QUE tem dentro da caixa.
1.  **Inteiro (int):** Números sem vírgula (1, 10, -5).
2.  **Real (float):** Números com ponto (2.5, 3.14). *[Python usa ponto, não vírgula!]*
3.  **Texto (str):** Palavras entre aspas ("Olá", 'Python').
4.  **Booleano (bool):** Verdadeiro (True) ou Falso (False).

### Exercício 2
Qual é o tipo da variável `altura = 1.75`?
( ) int (Inteiro)
( ) float (Real)
( ) str (Texto)

---

## Passo 3: Entrada e Saída (Input e Print)

**Explicação:**
- `print()`: O computador **fala** (mostra na tela).
- `input()`: O computador **escuta** (pede para você digitar).

**Exemplo:**
```python
nome = input("Qual seu nome? ")
print("Olá, " + nome)
```

### Exercício 3
O comando `input()` serve para:
( ) Mostrar texto na tela.
( ) Ler o que o usuário digita.

---

## Exercício Prático (Arquivo: variaveis.py)

Crie um arquivo chamado `variaveis.py` e digite:

```python
# Meu primeiro programa
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) # Converte para número inteiro

print(f"Olá {nome}, você tem {idade} anos!")
print(f"Em 10 anos, você terá {idade + 10} anos.")
```

**Checklist:**
[ ] O programa perguntou o nome?
[ ] O programa calculou a idade futura corretamente?
