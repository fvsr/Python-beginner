
# O "meow" é o miado de um gato americano, e geralmente ele mia mais de uma vez.

# O comando "for" também gera um loop, e faz controle de repetições.

# Os tipos de variáveis em Python vistos até agora são:
# str, strings;
# int, inteiros;
# float, ponto flutuante;
# bool, variável booleana, uma variável que só assume os valores True ou False, verdadeiro ou falso.

# Iremos agora ver o  tipo "list", que é uma lista de coisas.

# Usando o loop for:
"""
for i in [0,1,2]: # A lista é o "[0,1,2]".
    print("meow")
"""

# Usando a função "range()" para otimizar o código.
# Aqui o sinal "_" representa uma variável que não importa o nome,
# porque não vai ser usada depois, nem recebe um valor anterior.
# A função "range(3)" atribui os valores 0, 1 e 2 para essa variável.
"""
for _ in range(3): 
    print("meow")
"""

# Perguntando ao usuário quantas vezes o gato deve miar.
# Se o usuário fornecer um valor positivo, o loop se interrompe,
# mas se o usuário fornecer um valor negativo,
# o programa vai pedir um valor novamente, até que um valor positivo seja inserido.
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


