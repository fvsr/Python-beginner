# Este código exemplifica o uso do "or" em condicionais.
# Se x é maior ou menor que y, então x é diferente de y.
# O "or" indica que se uma ou outra proposição for verdadeira, o resultado da pergunta retorna verdadeiro.

"""
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y: 
    print("x is not equal to y")
else:
    print ("x is equal to y")
"""    

# Esta versão do código é otimizada em relação a anterior,
#pois obtém o resultado com um teste a menos.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y: 
    print("x is not equal to y")
else:
    print ("x is equal to y")