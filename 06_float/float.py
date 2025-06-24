# Este código desenvolve operações com números do tipo float,
# conjuntos dos números Racionais (Q) e Irracionais (I).

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y) # Arredonda para o inteiro mais próximo abaixo ou acima.

# print(z) # Saída sem formatação

print(f"{z:,}") # Formata a saída com a vírgula entre a casa do milhar e das centenas, 
                # o modo americano de representar 1000, assim: 1,000

# Função de arredondamento:
# round(number[, ndigits])
# Os colchetes, [], em inglês square brackets, onde bracket significa parêntese,
# indicam que algo é opcional.