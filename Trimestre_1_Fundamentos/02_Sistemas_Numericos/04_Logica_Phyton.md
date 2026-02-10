# Lógica Matemática e Introdução ao Python

> **Metodologia:** Kumon (Pequenos passos, Exemplos, Prática imediata)

---

## Passo 1: Verdadeiro ou Falso (Boolean)

**Explicação:**
Na computação e na lógica, só existem duas "verdades":
- **True** (Verdadeiro) = 1
- **False** (Falso) = 0

O computador usa isso para tomar decisões.

### Exercício 1 (Marque V ou F)
1.  O céu é verde. ( )
2.  Computadores usam eletricidade. ( )
3.  10 é maior que 5. ( )

---

## Passo 2: Operadores Lógicos (AND, OR, NOT)

**Explicação:**
Podemos combinar frases usando "E" (AND), "OU" (OR) e "NÃO" (NOT).

1.  **AND (E):** Só é verdade se **TUDO** for verdade.
    - "Tenho dinheiro" E "Tenho tempo" -> Vou viajar. (Precisa dos dois).
2.  **OR (OU):** É verdade se **PELO MENOS UM** for verdade.
    - "Como pizza" OU "Como hambúrguer" -> Fico feliz. (Basta um).
3.  **NOT (NÃO):** Inverte o valor.
    - NÃO (Verdade) = Falso.

### Exercício 2
- Verdadeiro **AND** Verdadeiro = ______
- Verdadeiro **AND** Falso = ______
- Verdadeiro **OR** Falso = ______

---

## Passo 3: Lógica no Python

**Explicação:**
O Python entende essa lógica perfeitamente. Vamos ver como escrever.

```python
print(10 > 5)   # Vai escrever: True
print(10 < 5)   # Vai escrever: False
print(True and False) # Vai escrever: False
```

### Exercício 3 (Prevendo o futuro - O que o Python vai mostrar?)
```python
a = 10
b = 20
print(a < b)
```
Resultado: ( ) True   ( ) False

---

## Exercícios de Repetição (Fixação)

1. Qual operador exige que **todas** as condições sejam verdadeiras?
   ( ) OR
   ( ) AND

2. Se `x = 5`, qual é o resultado de `x > 10`?
   ( ) True
   ( ) False

3. O operador **NOT** faz o quê?
   ( ) Deixa tudo igual
   ( ) Inverte (Vira o oposto)

**Gabarito:**
*Ex 1:* F, V, V
*Ex 2:* V, F, V
*Ex 3:* True
*Fixação:* 1-AND, 2-False, 3-Inverte
