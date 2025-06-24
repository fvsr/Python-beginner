# Para definir uma função usa-se o comando "def".

# Este código não vai funcionar porque a função hello() não foi definida.
# Tire as aspas triplas e rode o programa para verificar a mensagem de erro.
"""
name = input("What's your name? ")
hello()
print(name)
"""

# Usando o mesmo código, desta vez com a função hello() sendo definida:
"""
def hello():
    print("Hello!")

name = input("What's your name? ")
hello()
print(name)
"""

# A mesma função, mas usando passagem de parâmetro:
def hello(to="world"): # Aqui o valor default para a variável to (to="world!") não funcionou, parece ser um erro comum em Python.
    print("Hello,",to)

name = input("What's your name? ")
hello(name)