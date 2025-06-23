# Este programa pergunta seu nome,
# e depois imprime "Hello, " junto com seu nome na saída.

# Parâmetros que a fnção print pode receber:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=false)

# Escrever alguma coisa direto no programa, assim
# print("Hello, fvsr") se chama em inglês "to hardcode your name",
# e não é isso que queremos.

# Return Values: quando enviamos um dados para uma função
# (caso ela não seja uma função void), ela faz uma cálculo
# e te retorna um valor

# Variables: são as váriaveis, um espaço de memória reservado no computador
# que tem a função de armazenar um valor.

# Assignment operator: é o operador de atribuição, sinal =,
# que faz com que o valor captado pela função da direita
# seja escrito na variável a esquerda.
# É importante lembrar que o movimento da informação na atribuição é da direita para esquerda.

# Pseudocode: é o pseudocódigo, que são tarefas descritas em linguagem comum
# para serem postariormente escritas em linguagem de programação.

# pergunta ao usuário seu nome (exemplo de pseudocode)
name = input("What's your name? ") # Observar o espaço depois do sinal de interrogação.

# Diz hello para o usuário (exemplo de pseudocode)
print("Hello, ",)
print(name)

# Aqui corrige o problema de a saída estar em duas linhas:
print("Hello, ", end="")
print(name)

# Acrescenta algo entre os objetos de saída: 
print("Hello", end="|")
print(name)

# A mesma coisa de outra forma
print("Hello, " + name) # Observar o espaço depois da vírgula.

# Outro exemplo:
print("Hello ",name,sep="- ")

# E assim também:
print("Hello,",name) #Esta linha de comando acrescenta um espaço para cada argumento depois do texto.

# Para fazer as aspas aparecerem no texto final:
print("Hello, \"friend\"",name)

#Saída usando uma "f str", ou uma string formatada, equivalente aos operadores de formatação (%) em C:
print(f"Hello, {name}") # o 'f' indica que as chaves são para formatar o texto


