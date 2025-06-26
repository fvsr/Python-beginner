# Este código exemplifica o uso de uma função que retorna um valor lógico,
# verdadeiro ou falso, através do uso de uma variável lógica.

"""
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
"""

# Em Python podemos otimizar a função is_even():
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False # Sintaxe particular do Python.

main()
