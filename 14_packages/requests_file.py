# Uso do package "requests", 
# que pode ser instalado usando o comando "pip".
# O packge "requests" nos permite fazer requisições pela internet,
# usando um código em Python.

# Esse package permite o uso de APIs.
# API é Application Programming Interface, 
# que geralmente se referem a serviços de terceiros,
# com os quais podemos conversar através de códigos escritos por nós mesmos.
# Vamos escrever um código que 'finge' ser um navegador de internet,
# e assim ele se conecta a uma API através da internet e 
# faz o download de informações que nos interessam.

# Para instalar este package, 
# vamos escrever a linha de comando abaixo no terminal:
# pip install requests
# e aguardar a instalação.

# Para executar este programa,
# escrever no terminal:
# python itunes.py weezer
"""
import requests
import sys

if len(sys.argv) != 2: # Para execuar o programa eu preciso do nome do programa e da banda
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
"""
# O texto de resposta está originalmente no formato JSON,
# JavaScript Object Notation,
# mas a biblioteca "requests" transforma em um formato "Python dictionary".
# O formato "Python dictionary" usa chaves no início e no fim, "{}",
# usa colchetes "[]" para listas internas,
# usa aspas para marcar as palavras-chave do dicionário,
# depois das palavras chave os dois pontos ":" antes de um valor.

# Esse dicionário é bem difícil de ler,
# então vamos chamar outra função para formatar o texto JSON.
"""
import json
import requests
import sys

if len(sys.argv) != 2: # Para execuar o programa eu preciso do nome do programa e da banda
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
"""


import json
import requests
import sys

if len(sys.argv) != 2: # Para execuar o programa eu preciso do nome do programa e da banda
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# O limite foi aumentado para 50, para retornar 50 faixas.
o = response.json() # Pega a resposta do servidor e coloca no formato json.
for result in o["results"]: # Extrai o resultado que está numa lista chamada "results".
    print(result["trackName"])
