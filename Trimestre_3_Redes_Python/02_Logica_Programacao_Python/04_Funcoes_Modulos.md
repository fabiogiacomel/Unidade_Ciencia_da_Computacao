# Funções e Modularização

> **Metodologia:** Kumon (Pequenos passos, Exemplos, Prática imediata)

---

## Passo 1: O que é uma Função?

**Explicação:**
Uma função é um **bloco de código** que tem um nome e faz uma tarefa específica.
Em vez de copiar e colar código, você chama a função.
Já usamos algumas: `print()`, `input()`, `int()`. Agora vamos criar as nossas!

**Sintaxe:**
```python
def dar_oi(nome):
    print(f"Olá, {nome}! Tudo bem?")

# Usando a função
dar_oi("Fabio")
dar_oi("Maria")
```

### Exercício 1
Para criar uma função nova, qual palavra usamos?
( ) func
( ) def (Definir)

---

## Passo 2: Retorno (Return)

**Explicação:**
Algumas funções só mostram coisas na tela (`print`).
Outras calculam e **devolvem** um valor para quem chamou. Usamos `return`.

```python
def somar(a, b):
    resultado = a + b
    return resultado

x = somar(5, 5) # x vai valer 10
print(x)
```

### Exercício 2
Se eu não usar o `return`, a variável `x` vai receber o resultado da soma?
( ) Sim
( ) Não, vai receber "None" (Nada).

---

## Passo 3: Módulos (Import)

**Explicação:**
Módulos são arquivos com várias funções prontas.
O Python já vem com vários ("baterias inclusas").
- `math` (Matemática)
- `random` (Sorteio/Aleatório)
- `time` (Tempo)

**Exemplo:**
```python
import random
numero = random.randint(1, 100) # Sorteia de 1 a 100
print(numero)
```

---

## Exercício Prático (Arquivo: calculadora.py)

Vamos organizar.

```python
# Minhas Funções
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

# Programa Principal
print("--- Calculadora Simples ---")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

print(f"Soma: {somar(n1, n2)}")
print(f"Subtração: {subtrair(n1, n2)}")
```

**Checklist:**
[ ] Crie as funções `multiplicar` e `dividir` seguindo o modelo.
