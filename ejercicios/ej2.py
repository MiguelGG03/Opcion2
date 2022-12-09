# Binomio de newton iterativo


def binomio_newton_iterativo(n, k):
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

