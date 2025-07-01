# Exceções ocorrem quando aconteceu algum problema no código.
# Para isso existem as mensagens de erro.
# Comandos "try", "except" e "else".

# Vamos provocar um erro para vericar qual a mensagem de erro que é retornada.
"""
print("Hello, world!)
"""
# Foi retornada a seguinte mensagem de erro:
# SyntaxError: unterminated string literal (detected at line 6)
# Um erro de sintaxe quer dizer que o problema está no código que está escrito,
# na forma que foi escrito.
# Não terminada significa que não foi encerrada corretamente,
# string é uma sequência de caracteres,
# e literal quer dizer que não é uma variável, 
# é algo que foi digitado letra por letra dentro do código.
# O mesmo código corrigido:
"""
print("Hello, world!")
"""

# Run Time Errors
"""
x = int(input("What's x? "))
print(f"x is {x}")
"""
# ValueError: invalid literal for int() with base 10: 'cat'
# Aqui o problema foi escrever a palavra "cat" no input do usuário.
# A função "int()", usada para transformar números (1,2,...) em um valor inteiro,
# não está preparada para aceitar letras (a,b,...) como entrada,
# então as letras digitadas são inválidas para esta função.

# Programar defensivamente é se antecipar a erros que podem acontecer,
# ou mais, 
# pensar que o usuário pode estar distraído e digitar texto em uma entrada para números,
# o até mesmo que o usuário pode digitar texto maliciosamente para provocar o erro.

# Usando os comandos "try" e "except".
"""
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
""" 
# Desta vez, ao digitar 'cat' o programa está preparado para um erro na entrada de dados 
# excutando a linha 43.
# Este código é melhor e mais correto,
# porque gera uma mensagem de erro mais compreensiva para o usuário,
# e porque se antecipa a um erro que pode acontecer,
# o que é mais 'elegante'.

# O comando "try" só deve ser usado para linhas de código que podem realmente ocasionar um erro,
# e isso acontece com a função "int()" caso a entrada seja uma string,
# mas não acontece com a função "print()",
# que neste caso não vai dar origem a um erro.
# Vamos então tirar a função "print()" da indentação do comando "try".
"""
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
""" 
# Entretanto com a intenção de otimizar o código,
# acabamos por causar um novo erro,
# que foi provocado ao colocar como esntrada a palavra "cat".
# NameError: name 'x' is not defined
# Este erro ocorre porque ao inserir "cat" a execução da segunda linha se interrompe,
# e não ocorre a atribuição de um valor a "x",
# fazendo com que "x" não seja lido e portanto não esteja definido.
# Eu suponho que isso tenha a ver com a maneira pela qual o Python é compilado,
# vou pesquisar isso futuramente.

# Usando o comando "else" para resolver esse erro.
# Quando a primeira e segunda linhas são executadas sem erros,
# o código executa a quinta e sexta linhas e encerra.
# Caso haja um erro na segunda linha,
# são executadas e a terceira e quarta linhas e encerra.
# O comando "else" só é executado caso o comando "try" seja executado sem erros.   
"""
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
""" 

