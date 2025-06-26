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
"""
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

# otimizando ainda mais com o comando 'match'.
"""
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # Similar ao "default" do "switch" em C.
        print("Who?")
"""

# Otimizando com o uso do 'or'.
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?") 