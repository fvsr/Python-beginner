# Este código desenvolve operações com números do tipo float,
# conjuntos dos números Racionais (Q) e Irracionais (I).

x = float(input("What's x? "))
y = float(input("What's y? "))

# z = (x / y) # Se o arredondamento não for feito aqui
            # é feito na formatação de texto como no terceiro exemplo de print()  
# z = round(x / y) # Arredonda para o inteiro mais próximo abaixo ou acima.
z = round(x / y, 3) # Aqui 3 é o número de casas decimais para o qual o arrendondamento vai ser feito.
                    # Pode-se conseguir o mesmo resultado formatando da função print
                    # como foi feito no terceiro modo abaixo.

print(z) # Saída sem formatação
# print(f"{z:,}") # Formata a saída com a vírgula entre a casa do milhar e das centenas, 
                  # o modo americano de representar 1000, assim: 1,000
# print(f"{z:.3f}") # Esta formatação arredonda para 3 casas decimais a váriavel tipo float.

# Função de arredondamento:
# round(number[, ndigits])
# Os colchetes, [], em inglês square brackets, onde bracket significa parêntese,
# indicam que algo é opcional.