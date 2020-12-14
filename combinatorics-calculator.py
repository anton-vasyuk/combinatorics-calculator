from math import factorial

def p(n):
    '''Число перестановок'''
    return factorial(n)

def a(n, k):
    '''Число размещений'''
    return factorial(n) // factorial(n - k)

def c(n, k):
    '''Число сочетаний'''
    return factorial(n) // (factorial(k) * factorial(n - k))

def P(n, *args):
    '''Число перестановок с повторениями'''
    m = 1
    for x in [factorial(y) for y in args]:
        m *= x
    return factorial(n) // m

def A(n, k):
    '''Число размещений с повторениями'''
    return n ** k

def C(n, k):
    '''Число сочетаний с повторениями'''
    return factorial(n + k - 1) // (factorial(k) * factorial(n - 1))
