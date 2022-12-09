def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        print('Secuencia de Fibonacci hasta', n, ':\n')
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c

# Sacado de https://www.programiz.com/python-programming/examples/fibonacci-sequence

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Sacado de https://www.linuxhispano.net/2013/08/07/fibonacci-recursivo-python/

def main4():
    pr1= input('De que marea quieres la secuencia de Fibonacci?\n'
               '1. Iterativa\n'
               '2. Recursiva\n'
               '>>>')
    if pr1 == '1':
        pr2 = int(input('Hasta que numero quieres la secuencia?\n'
                        '>>>'))
        print(fibonacci_iterativo(pr2))
    elif pr1 == '2':
        pr2 = int(input('Hasta que numero quieres la secuencia?\n'
                        '>>>'))
        print(fibonacci_recursivo(pr2))
    else:
        print('Opcion no valida')
        main4()