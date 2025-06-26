# Este código exemplifica o uso do "or" em condicionais.
# Se x é maior ou menor que y, então x é diferente de y.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y: 
    print("x is not equal to y")
else:
    print ("x is equal to y")
    