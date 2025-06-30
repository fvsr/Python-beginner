# O "dict" é ma estrutura de dados que permite associar um valor a outro, ou uma chave a um valor.

# Os exemplos a seguir usam os personagens da saga Harry Potter.

# Este é um contraexemplo, 
# que mostra que associar um elemento de uma lista com os elementos de outra lista,
# (usando o tipo "list"), pode ficar confuso,
# e em datasets maiores levar a perda da conexão, neste caso,
# entre os elementos da lista "students" e os elementos da lista "houses".
# Em um dataset de fichas cadastrais por exemplo, o nome e o telefone de uma pessoa
# são elementos indissociáveis, então precisamos de uma estrutura de dados que garanta isso,
# no caso a estrutura de dados "dict".
"""
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
"""

# Exemplo de "dict".
# No "dict", a primeira coluna, que contém os nomes, 
# pode funcionar como o índice,
# e usando o comando "print" imprimir as "houses" a partir do nome.
"""
students = {
    "Hermione": "Gryffindor",
    "Harry":    "Gryffindor",
    "Ron":      "Gryffindor",
    "Draco":    "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""

# Usando uma estrutura de repetição para percorrer todos os elementos do dicionário
# podemos imprimir todas as chaves, que são os elementos da primeira coluna.
"""
students = {
    "Hermione": "Gryffindor",
    "Harry":    "Gryffindor",
    "Ron":      "Gryffindor",
    "Draco":    "Slytherin"
}

for student in students:
    print(student)
"""

# A seguir vamos imprimir o nome e a casa respectiva.
# Os parâmetros são as variáveis definidas na declaração da função.
# Os argumentos são os valores passados durante a chamada da função.
# Neste caso a função print suporta um parâmetro de separador entre duas palavras,
# que pode ser qualquer carctere passado como argumento do parâmetro "sep".
"""
students = {
    "Hermione": "Gryffindor",
    "Harry":    "Gryffindor",
    "Ron":      "Gryffindor",
    "Draco":    "Slytherin"
}

for student in students:
    print(student, students[student], sep=",  ")
"""

# Neste exemplo vamos fazer uma lista com vários dicionários dentro.
# A palavra "None" em Python representa oficialmente a ausência de um valor.
# Um dicionário é um conjunto de pares chave (key) e valor, entre chaves.
# Cada dicionário tem três chaves ou palavras, "name", "house" e "patronus"
# e as chaves tem três definições ou valores, "Hermione", "Gryffindor" e "Otter".

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry",    "house": "Gryffindor", "patronus": "Stag" },
    {"name": "Ron",      "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco",    "house": "Slytherin",  "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")