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
# A função tem que ser definida em linhas anteriores, antes de ser chamada.

# A mesma função, mas usando passagem de parâmetro:
def hello(to="world"): # É atribuido o valor default caso não seja passado um valor para a função.
    print("Hello,",to)

hello() # Na primeira vez que a função é chamada,
        # não está sendo passado um parâmetro para função, 
        # então entra o valor default.

name = input("What's your name? ")
hello(name)