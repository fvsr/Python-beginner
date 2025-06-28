# Este código exemplifica o uso do tipo de variável "list".

# Os tipos de variáveis em Python vistos até agora são:
# str, strings;
# int, inteiros;
# float, ponto flutuante;
# bool, variável booleana, uma variável que só assume os valores True ou False, verdadeiro ou falso.

# Iremos agora ver o  tipo "list", que é uma lista de coisas.
# No caso "students" é uma lista de nomes, então usamos aspas em cada nome.
"""
students = ["Hermione","Harry","Ron"]

print(students[0])
print(students[1])
print(students[2])
"""

# Otimizando o código com um loop for.
# Notar que no "for" em Python não é necessário iniciar a variável que vaz o papel de índice,
# nem incrementar essa variável, nem testar se a lista chegou ao fim.
# Aqui o "for" simpesmente imprime a lista inteira.
# A variável "student" não é um índice,
# ela assume os elementos da lista de nomes "students",
# um a cada impressão. 
"""
students = ["Hermione","Harry","Ron"]

for student in students:
    print(student)
"""

# Neste caso "i" é um índice.
# A função "range()" faz o índice variar,
# mas para isso precisamos saber o número de elementos da lista,
# para isso usamos a função "len()".
# Não podemos passar a lista "students" para a função "range()" diretamente
# porque "range()" só aceita inteiros como entrada. 
students = ["Hermione","Harry","Ron"]

for i in range(len(students)):
    print(students[i])