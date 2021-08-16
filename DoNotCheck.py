from math import sin,exp
import matplotlib.pyplot as  plt

def count_odd_even(N):
    error_msg = 'The number inserted in not a natural number.'
    if N > 0 and isinstance(N,int):
        odd = 0
        even = 0
        for i in range(1,N+1):
            if i%2 == 0:
                even+=1
            else:
                odd+=1
        return even,odd
    else:
        return error_msg
        

def sum_AP(start,difference,N):
    sum = 0
    for i in range(N):
        sum = start + i*difference
    return sum

def sum_GP(start,ratio,N):
    sum = 0
    for i in range(N):
        sum = start*ratio**i
    return sum

def sum_HP(start,difference,N):
    sum = 0
    for i in range(N):
        sum = 1/(start + i*difference)
    return sum

def factorial(N) :
    product = 1
    for i in range(1,N+1):
        product*=i
    return product


def approx_sin(digits,x,Plot = True):
    sin_at_x = 0
    n = 0
    list_iter = []
    list_sine = []
    while abs(sin(x) - sin_at_x) >= 10**(-(digits + 1)):
        sin_at_x += ((-1)**n)*(x**(2*n + 1)/factorial(2*n + 1))
        n += 1
        list_iter.append(n)
        list_sine.append(abs(sin(x) - sin_at_x))
    if Plot is True:
        plt.xlabel('Iteration Nuumber (n)')
        plt.ylabel('Modulus of Error')
        plt.plot(list_iter,list_sine, '-h')
        plt.show()
    else:
        return list_sine, sin_at_x

def approx_neg_exp(digits,x,Plot = True):
    exp_at_neg_x = 0
    n = 0
    list_iter = []
    list_exp = []
    while abs(exp(-x) - exp_at_neg_x) >= 10**(-(digits + 1)):
        exp_at_neg_x += ((-x)**n)/factorial(n)
        n += 1
        list_iter.append(n)
        list_exp.append(abs(exp(-x) - exp_at_neg_x))
    if Plot is True:
        plt.xlabel('Iteration Nuumber (n)')
        plt.ylabel('Modulus of Error')
        plt.plot(list_iter,list_exp, '-h')
        plt.show()
    else:
        return list_exp, exp_at_neg_x, exp(-x)

approx_neg_exp(4,1.5)