# Comandos "break", "return", "pass" e "prompt".

# Colocamos agora um loop de repetição no prompt do usuário,
# desse modo podemos dar mais de uma oportunidade de inserir o tipo de dado desejado.
# Vamos usar agora o comando "break", ele é importante aqui,
# é o modo pelo qual o programa eventualmente sai do loop.
"""
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else: 
        break

print(f"x is {x}")
"""

# Uma outro versão possível do programa acima.
# A vantegem desta versão é que ela é mais sintética.
# O interessante da versão anterior
# é que dentro do comando "try" está somente a linha de
# código que eu suspeito que pode dar algum problema.
""" 
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")
"""

# Usando funções para isolar uma funcionalidade do código, tornar o código modular.
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
    
main()
"""

# Podemos dispensar o comando "break", e deixar somente o comando "return x",
# pois dentro do comando "return" já existe um "break".
# O comando "return x" não pode ser dispensado,
# pois é ele que entrega o valor que a função calculou de volta para a função principal,
# para que na sequência seja atribuído a variável "x".
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
    
main()
"""

# Lembrar que o escopo de uma variável definida dentro de uma função
# se limita à função onde ela foi definida.
# Então a variável "x" da função "main()" não é a mesma variável "x" da função "get_int()".
# Para verificar isso vamos trocar a variável da função "get_int()".
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            y = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return y
    
main()
"""

# Podemos fazer duas versões mais abreviadas do mesmo código,
# ambas variando o ponto a partir do qual o retorno do valor é feito.
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            y = int(input("What's x? "))
            return y
        except ValueError:
            print("x is not an integer")
    
main()
"""

# Resumindo ainda mais o código.
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
    
main()
"""

# Na linha seguinte à instrução "except ValueError:" existe a instrução "print("x is not an integer")".
# Para lidar com o erro de maneira diferente,
# sem ficar constantemente escrevendo essa mensagem para o usuário,
# podemos usar o comando "pass", não faz nada com relação ao erro.
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
    
main()
"""

# Usando o comando "prompt".
# Aqui a mensagem para o usuário é impressa pela chamada da função "get_int()",
# e a leitura do teclado é feita pela função "input()", dentro da função "get_int()".
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
    
main()