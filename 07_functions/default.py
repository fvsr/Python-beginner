# Esta questão aparece no temp 1h e 38 m do curso.
# Verifique o código abaixo qual o valor de i que vai ser impresso:

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# Saída vai ser 5 porque i era igual a 5 quando a definição da função f() é lida.  