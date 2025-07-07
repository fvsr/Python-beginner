# Este arquivo de código não pode ter o mesmo nome que uma biblioteca Python,
# caso contrário as funções "import" e "from" vão buscar funções neste arquivo e não vão encontrar.

# Comandos "import" e "from", para bibliotecas e funções,
# e biblioteca "sys".
# A biblioteca "sys" tem funções realcionadas ao sistema,
# e está relacionada a comandos digitados no terminal.
# O arquivo "sys.argv" é uma lista comandos que podem ser digitados no terminal
# que vão influenciar o programa que vai ser executado.
# A palavra "argv" significa "argument vector".

# Usar a função ou o arquivo "sys.argv" para receber um nome.
# Para executar este programa a partir do terminal escrever
# python sys_file.py seu_nome
# A saída vai ser
# Hello, my name is seu_nome
# Se o programa for executado sem escrever um nome, assim
# python sys_file.py
# haverá a seguinte mensagem de erro
# IndexError: list index out of range
# Essa mensagem ocorre quando é feita uma tentativa de acesso,
# dentro de um array por exemplo, a um elemento que não existe.
"""
import sys

print("Hello, my name is", sys.argv[1])
"""

# Escrevendo um código que antecipa esse erro,
# usando os comandos "try" e "except".
"""
import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("To few arguments")
"""

# Otimizando o código anterior,
# acrescentado mensagens de erro para entrada de dados a menos
# e também dados a mais, usando a função "len".
# Este programa precisa de dois dados para ser executado,
# o nome do programa e o nome do usuário, assim
# pyhton sys_file.py nome_do_usuario
# Para escrever u nome composto como um nome só,
# usar aspas, assim
# pyhton sys_file.py "primeiro_nome segundo_nome"
"""
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
"""

# Colocando o tratamento de erros num bloco separado, e a real intenção do programa,
# que no caso é escrever o nome do usúario, em outro bloco.
# O problema é que se não escrevermos o nome, voltaremos a recer esta mensagme de erro,
# que vem da última linha de código
# IndexError: list index out of range
"""
# Importa bibliotecas
import sys

# Verifica se o usuário digitou os dados corretamente
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

# Escreve o nome do usuário
print("Hello, my name is", sys.argv[1])
"""

# Usando a função "sys.exit" para garantir o encerramento do programa
# a encontrar um erro.
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")

print("Hello, my name is", sys.argv[1])
"""

# Imprimindo o conteúdo de "sys.argv".
"""
import sys

if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv:
    print("Hello, my name is", arg)
"""

# A primeira posição em sys.argv é o nome do arquivo de código,
# e ele não precisa ser impresso.
# Então não vamos imprimir todo o arquivo "sys.argv",
# mas apenas da segunda posição para frente.
# Em Python isso significa imprimir um "slice" de uma lista,
# ou um subset da lista.
# A primeira posição é o nímero zero.
"""
import sys

if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
"""

# A seguinte sintaxe subtrai além da posição 0 da lista,
# um ou mais elementos ao final da lista.
import sys

if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv[1:-2]: # Nâo imprime o primeiro, nem o penúltimo e o último elementos da lista.
    print("Hello, my name is", arg)