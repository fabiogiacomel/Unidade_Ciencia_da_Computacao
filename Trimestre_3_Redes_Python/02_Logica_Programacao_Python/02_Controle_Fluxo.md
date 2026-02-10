# Controle de Fluxo: IF e ELSE (Se / Senão)

> **Metodologia:** Kumon (Pequenos passos, Exemplos, Prática imediata)

---

## Passo 1: Tomando Decisões

**Explicação:**
O computador é burro. Ele só faz o que mandamos.
O `if` (se) permite que ele "escolha" um caminho.
O `else` (senão) é o caminho alternativo.

**Estrutura:**
```python
if idade >= 18:
    print("Pode dirigir")  # Caminho 1
else:
    print("Não pode dirigir") # Caminho 2
```

**ATENÇÃO:** O Python usa **INDENTAÇÃO** (espaço no começo da linha) para saber o que está dentro do `if`.

### Exercício 1
Se `idade = 15`, o que o código acima vai imprimir?
( ) Pode dirigir
( ) Não pode dirigir

---

## Passo 2: Elif (Senão Se)

**Explicação:**
E se tivermos 3 opções?
Usamos o `elif` (Else If).

```python
nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

### Exercício 2
Se a nota for **6**, qual mensagem aparece?
( ) Aprovado
( ) Recuperação
( ) Reprovado

---

## Passo 3: Comparadores

- `==` Igual (Dois iguais!)
- `!=` Diferente
- `>` Maior
- `<` Menor
- `>=` Maior ou Igual

### Exercício 3
Qual símbolo verifica se dois números são iguais?
( ) = (Um igual)
( ) == (Dois iguais)

---

## Exercício Prático (Arquivo: decisao.py)

Crie um arquivo chamado `decisao.py`:

```python
senha = input("Digite a senha: ")

if senha == "1234":
    print("Acesso Permitido! Bem-vindo.")
else:
    print("Acesso Negado! Senha incorreta.")
```
execute e teste com a senha certa e errada.

**Checklist:**
[ ] O programa funciona com a senha "1234"?
[ ] O programa bloqueia outras senhas?
