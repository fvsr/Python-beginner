# Este código desenvolve operações com números inteiros (conjunto Z).

# Para rodar o código abaixo basta tirar as aspas triplas:
""""
x = 1
y = 2

z = x + y

print(z)
"""
# O código abaixo não funciona como esperado porque x e y são recebidos como str (strings).
""""
# Solicita ao usuário que digite números inteiros:
x = input("What's x? ")
y = input("What's y? ")

# Soma dois números inteiros
z = x + y

# Imprime o resultado 
print(z)
"""

# O código abaixo corrige isso.

# Solicita ao usuário que digite números inteiros:
x = input("What's x? ")
y = input("What's y? ")

# Soma dois números inteiros
z = int(x) + int(y)

# Imprime o resultado 
print(z)

# O mesmo código com "nested functions", ou funções aninhadas.
"""
# Solicita ao usuário que digite números inteiros:
x = int(input("What's x? "))
y = int(input("What's y? "))

# Imprime o resultado 
print(x + y)
"""
"""
# O mesmo código ainda mais resumido.
print(int(input("What's is x? ")) + int(input("What's is y? ")))
"""