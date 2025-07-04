# Comandos "import" e "from", para bibliotecas e funções,
# biblioteca "random" e as funções "choice" e "randint".

# Bibliotecas são arquivos de códigos que outras pessoas escreveram 
# que eu posso usar em meus programas.
# É a habilidade de compartilhar código entre pessoas ou entre meus programas.
# Isso é feito através de "modules".
# Um módulo em Python é uma biblioteca que possui uma ou mais funções construídas dentro dela.
# Geralmente o propósito de uma biblioteca ou módulo é encorajar o reuso do código.
# Se durante o trabalho de programação copiamos e colamos trechos de códigos várias vezes,
# sempre a mesma funcionalidade, quer dizer que esse código pode ser material para ma biblioteca.

# Comando "import" carrega toda a biblioteca "random".
# Biblioteca random.
# Os colchetes "[]" indicam que a função "choice" recebeu uma lista como argumento.
# O ponto indica que a função "choice" pertence à biblioteca "random".
"""
import random
moeda = random.choice(["cara", "coroa"])
print(moeda)
"""

# Aqui "from random import choice" permite carregar somente uma função, evitando o uso do ponto. 
"""
from random import choice
moeda = choice(["cara", "coroa"])
print(moeda)
"""

# Usando a função "randint" para sortear um número dentro de um range.
"""
import random
number = random.randint(1,10)
print(number)
"""