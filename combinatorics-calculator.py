from math import factorial

def p(n):
    '''����� ������������'''
    return factorial(n)

def a(n, k):
    '''����� ����������'''
    return factorial(n) // factorial(n - k)

def c(n, k):
    '''����� ���������'''
    return factorial(n) // (factorial(k) * factorial(n - k))

def P(n, *args):
    '''����� ������������ � ������������'''
    m = 1
    for x in [factorial(y) for y in args]:
        m *= x
    return factorial(n) // m

def A(n, k):
    '''����� ���������� � ������������'''
    return n ** k

def C(n, k):
    '''����� ��������� � ������������'''
    return factorial(n + k - 1) // (factorial(k) * factorial(n - 1))
