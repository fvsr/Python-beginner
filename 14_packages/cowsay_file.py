# O "package" é como se fosse uma biblioteca, 
# mas em vez de ser apenas um arquivo, é um diretório com vários arquivos.

# O "pip" é um programa que permite instalar e gerenciar os "packges".
# Vamos usar o "pip" para isntalar um packge chamado "cowsay",
# para isso  vamos digitar o que segue no terminal:
# pip install cowsay
# e aguardar finalizar a instalação.
# Ao final aparece uma mensagem de instalação bem sucedida:
# Successfully installed cowsay-6.1

# Agora podemos usar a biblioteca "cowsay" num programa.
# Para executar este programa vamos digitar:
# cd diretorio_onde_esta_seu_programa
# e depois
# python cowsay_file.py seu_nome
# e verificar o resultado.
"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
"""

# Outro exemplo, com outra função da mesma biblioteca.
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])