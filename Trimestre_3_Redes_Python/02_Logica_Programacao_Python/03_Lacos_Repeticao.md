# Laços de Repetição: For e While

> **Metodologia:** Kumon (Pequenos passos, Exemplos, Prática imediata)

---

## Passo 1: O Comando FOR (Para)

**Explicação:**
Usado quando sabemos **quantas vezes** queremos repetir.
O computador conta para nós.

```python
# Conta de 0 até 4 (O Python para ANTES do número final)
for i in range(5):
    print(f"Contando: {i}")
```

Vai mostrar: 0, 1, 2, 3, 4.

### Exercício 1
Se eu escrever `range(3)`, quais números aparecem?
( ) 1, 2, 3
( ) 0, 1, 2

---

## Passo 2: O Comando WHILE (Enquanto)

**Explicação:**
Usado quando **NÃO sabemos** quantas vezes vai repetir.
Ele repete **ENQUANTO** uma condição for verdadeira.

```python
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
print("Acertou!")
```
Ele vai perguntar para sempre até você acertar.

### Exercício 2
Se eu digitar a senha errada 100 vezes, o `while` vai continuar perguntando?
( ) Sim
( ) Não, ele desiste depois de 3 vezes.

---

## Passo 3: Loop Infinito (Cuidado!)

**Explicação:**
Se a condição nunca ficar Falsa, o programa trava e roda para sempre.
Exemplo Perigoso:
```python
while True:
    print("Isso nunca para!")
```
Para parar, aperte **Ctrl + C**.

---

## Exercício Prático (Arquivo: tabuada.py)

Vamos fazer a tabuada do 7 usando `for`.

```python
numero = 7

print(f"Tabuada do {numero}:")

for i in range(1, 11): # De 1 até 10 (O 11 não conta)
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

**Checklist:**
[ ] O programa mostrou a tabuada completa (7x1 até 7x10)?
