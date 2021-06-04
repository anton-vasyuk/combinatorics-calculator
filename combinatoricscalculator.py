from math import factorial

def p(n):
    '''number of permutations'''
    return factorial(n)

def a(n, k):
    '''number of k-permutations of n'''
    return factorial(n) // factorial(n - k)

def c(n, k):
    '''number of k-combinations of n'''
    return factorial(n) // (factorial(k) * factorial(n - k))

def P(n, *args):
    '''number of permutations with repetitions'''
    m = 1
    for x in [factorial(y) for y in args]:
        m *= x
    return factorial(n) // m

def A(n, k):
    '''number of permutations with repetitions'''
    return n ** k

def C(n, k):
    '''number of k-permutations with repetitions of n'''
    return factorial(n + k - 1) // (factorial(k) * factorial(n - 1))
