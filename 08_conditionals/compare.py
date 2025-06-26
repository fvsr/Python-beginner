# Este código exemplifica o uso de condicionais.

# Símbolos que podem ser usados para perguntar questões matemáticas:
# >, maior que;
# >=, maior ou igual a;
# <, menor que;
# <=, menor ou igual a;
# ==, igual a (o = é operador de atribuição);
# !=, diferente de, não igual a;
# if, condicional.

# Este programa sempre executa os três ifs, independentemente de x e y.
"""
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
"""

# Este programa pára de executar os condicionais a partir do momento em que obtém uma resposta.
"""
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
"""

# Este programa evita a última pergunta, 
# pois pela lógica se as duas primeiras perguntas retornam falso,
# então a última resposta é obrigatoriamente verdadeira.
# Esta otimização reduz o tempo de processamento e pode fazer diferenças em programas grandes,
# ou em grandes quantidades de dados onde se repete o teste muitas vezes.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: 
    print("x is equal to y")