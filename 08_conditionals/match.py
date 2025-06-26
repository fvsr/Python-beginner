# Este código exemplifica o comando "match".
# O comando "match" é o equivalente ao comando "switch" em outras linguagens.
# A comparação entre strings é case sensitive, isto é, maiúscula e minúscula fazem diferença.

"""
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

# Otimizando o código anterior.
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

