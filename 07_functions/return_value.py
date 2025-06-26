# Este código demonstra o retorno de um valor a partir de uma função. 

# Este código eleva um número inteiro ao quadrado.
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n # Outras maneiras de calcular o quadrado de um número:
                 # n ** 2
                 # pow(n,2)

main()

