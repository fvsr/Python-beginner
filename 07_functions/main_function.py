# Este arquivo é sobre o uso da função main.

# No arquivo functions.py está exemplificado que 
# uma função em Python só pode ser chamada caso esteja completamente definida em linhas anteriores.
# Em códigos grandes isso dificulta a leitura, pois deixa o código assim:
"""
def função_1()
def função_2()
...
def função_n()
código_principal
"""
# Para evitar isso fazemos:
def main(): # Deixa claro que esta é a parte principal do programa
    hello() # Nesta chamada de função é usado o valor default que está em to="world!"
    name = input("What's your name? ")
    hello(name)

def hello(to="world!"):
    print("Hello,",to)

main() # Sem a chamada da função main o código não roda.

# Este é o erro com relação ao escopo da variável:
"""
def main():
    name = input("What's your name? ") # A variável "name" só é reconhecida dentro da função main.
    hello()

def hello():
    print("Hello,",name) # A variável name não foi definida dentro desta função, vai dar erro.
"""