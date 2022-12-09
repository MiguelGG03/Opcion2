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