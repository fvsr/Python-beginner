# O "meow" é o miado de um gato americano, e geralmente ele mia mais de uma vez.

# Este código exemplifica uma ação que deve ser repetida mais de uma vez.
"""
print("meow")
print("meow")
print("meow")
"""
# Entretanto este código não tem flexibiidade quanto ao número de repetições,
# nem quanto ao texto que é repetido.

# Vamos agora usar o comando "while" para controlar o número de repetições.

# O código abaixo é um exemplo do que não deve ser feito,
# pois a partir do momento que i = 3, não existe uma operação que mude o valor de i,
# o que faz com que o código entre em loop infinito, algo que é potencialmente perigoso.
"""
i = 3
while i!= 0:
    print("meow")
"""

# O código a seguir tem uma linha que muda o valor de i conforme as ações vão se repetindo,
# fazendo com que o número de repetições seja finito,
# assim o "while" funciona, proporcionando um controle do número de repetições.
# Quando i = 0 a expressão "while i!= 0" se torna falsa, e o loop interrompe sua execução.
"""
i = 3
while i!= 0:
    print("meow")
    i = i - 1
"""

# Aqui é feita uma otimização na contagem,
# seguindo o padrão em programação de contar a partir de zero até o valor desejado menos um.
i = 0
while i < 3:
    print("meow")
    i = i + 1 # Ou i += 1.
