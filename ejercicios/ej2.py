# Binomio de newton iterativo


def expand(func:str):
    for i in range(len(func)):
        if func[i] == '^':
            func = func[:i] + '**' + func[i+1:]
    if n == k:
        return 1
    elif k == 0:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, n+1):
            c = a * (n - i + 1) / i
            a = b
            b = c
        return c

def main2():
    print('Sabiendo que ')
    n = int(input('Dame el valor de n\n'
                    '>>>'))
    k = int(input('Dame el valor de k\n'
                    '>>>'))
    print(binomio_newton_iterativo(n, k))