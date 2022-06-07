import math

from intvalpy import Interval
from twin import *
from operation import *


# D_1  = (I_1l,I_1,α)= (T_1,α)=([a-,a+ ],[А-,А+ ],α),
# D_2= (I_2l,I_2,β) = (Т_2,β) = ([b-,b+ ],[B-,B+ ],β)
def gamma(D1: twin_Function, D2: twin_Function):
    if D1.alpha == D2.alpha and D1.alpha != '0' and D2 != '0' and D1.inside_width() != -1 and D2.inside_width() != -1:
        return D1.alpha
    elif D1.alpha != '0' and D1.inside_width() != -1 and D1.alpha != D2.alpha and \
            (D1.inside.b + D2.external.a) >= (D2.external.b + D1.inside.a):
        return D1.alpha
    elif D2.alpha != '0' and D2.inside_width() != -1 and D1.alpha != D2.alpha and \
            (D1.external.b + D2.inside.a) <= (D2.inside.b + D1.external.a):
        return D2.alpha
    else:
        return '0'


# D_1  = (I_1l,I_1,α)= (T_1,α)=([a-,a+ ],[А-,А+ ],α),
# D_2= (I_2l,I_2,β) = (Т_2,β) = ([b-,b+ ],[B-,B+ ],β)
def plus_func(D1: twin_Function, D2: twin_Function):
    if D1.alpha == D2.alpha and D1.alpha != '0' and D2 != '0' and \
            D1.inside_width() != -1 and D2.inside_width() != -1:
        return twin_Function(Interval(D1.inside.a + D2.inside.a, D1.inside.b + D2.inside.b),
                             Interval(D1.external.a + D2.external.a, D1.external.b + D2.external.b),
                             gamma(D1, D2))
    elif D1.alpha != '0' and D2 != '0' and D1.alpha != D2.alpha and \
            D1.inside_width() != -1 and D2.inside_width() != -1:
        if gamma(D1, D2) == '0':
            return twin_Function(Interval(None, None),
                                 Interval(min(D1.external.a + D2.inside.b, D2.external.a + D1.inside.b),
                                          max(D1.inside.a + D2.external.b, D2.inside.a + D1.external.b)),
                                 '0')
        elif gamma(D1, D2) == D1.alpha:

            return twin_Function(Interval(D1.inside.a + D2.external.b, D2.external.a + D1.inside.b),
                                 Interval(D1.external.a + D2.inside.b, D2.inside.a + D1.external.b),
                                 D1.alpha)
        elif gamma(D1, D2) == D2.alpha:
            return twin_Function(Interval(D2.inside.a + D1.external.b, D2.external.a + D1.inside.b),
                                 Interval(D2.external.a + D1.inside.b, D1.inside.a + D2.external.b),
                                 D2.alpha)
    elif D1.alpha == '0' or D2.alpha == '0' or D1.inside_width() == -1 or D2.inside_width() == -1:
        T1 = twin(D1.inside, D1.external)
        T2 = twin(D2.inside, D2.external)
        return (plus(T1, T2).Print_result(), print('gamma', gamma(D1, D2)))


def minus_function(D: twin_Function):
    if D.alpha == '-':
        return twin_Function(-D.inside, -D.external, '+')
    if D.alpha == '+':
        return twin_Function(-D.inside, -D.external, '-')
    else:
        return twin_Function(-D.inside, -D.external, '-')


def inverse_func(D: twin_Function):
    if 0 in D.inside or 0 in D.external:
        print("Cannot be divided into intervals containing 0.")
        exit()
    if D.alpha == '-':
        return twin_Function(1 / D.inside, 1 / D.external, '+')
    if D.alpha == '+':
        return twin_Function(1 / D.inside, 1 / D.external, '-')
    else:
        return twin_Function(1 / D.inside, 1 / D.external, '-')


# D_1  = (I_1l,I_1,α)= (T_1,α)=([a-,a+ ],[А-,А+ ],α),
# T-=[I-,Il-]  T+ = [Il+,I+]  I_1l :[a-,a+ ]
def S_1_multiply(D1: twin_Function, D2: twin_Function):
    T1 = twin(D1.inside, D1.external)
    T2 = twin(D2.inside, D2.external)
    # I1*I2
    if (T1.inside_width() == -1 or D1.alpha == '0') and (T2.inside_width() == -1 or D2.alpha == '0'):
        return Interval(T1.external.a, T1.external.b) * Interval(T2.external.a, T2.external.b)
    #I1*T2
    elif (T1.inside_width() == -1 or D1.alpha == '0') and T2.inside_width() != -1 and D2.alpha !='0':
        return Interval(T1.external.a, T1.external.b) * Interval(T2.external.a,T2.inside.a)
    # T1*I2
    elif (T2.inside_width() == -1 or D2.alpha == '0') and T1.inside_width() != -1 and D1.alpha!='0':
        return Interval(T1.external.a,T1.inside.a) * Interval(T2.external.a, T2.external.b)
    # T1*T2
    elif T2.inside_width() != -1 and D2.alpha != '0' and T1.inside_width() != -1 and D1.alpha!='0':
        return Interval(T1.external.a,T1.inside.a) * Interval(T2.external.a,T2.inside.a)

def S_2_multiply(D1: twin_Function, D2: twin_Function):
    T1 = twin(D1.inside, D1.external)
    T2 = twin(D2.inside, D2.external)
    # I1 * I2
    if (T1.inside_width() == -1 or D1.alpha == '0') and (T2.inside_width() == -1 or D2.alpha == '0'):
        return Interval(T1.external.a, T1.external.b) * Interval(T2.external.a, T2.external.b)
    #I1 * T2
    elif (T1.inside_width() == -1 or D1.alpha == '0') and T2.inside_width() != -1 and D2.alpha !='0':
        return Interval(T1.external.a, T1.external.b) * Interval(T2.inside.b,T2.external.b)
    # T1 * I2
    elif (T2.inside_width() == -1 or D2.alpha == '0') and T1.inside_width() != -1 and D1.alpha!='0':
        return Interval(T1.inside.b,T1.external.b) *Interval(T2.external.a, T2.external.b)
    # T1 * T2
    elif T2.inside_width() != -1 and D2.alpha != '0' and T1.inside_width() != -1 and D1.alpha!='0':
        return Interval(T1.inside.b,T1.external.b) * Interval(T2.inside.b,T2.external.b)


def multiply_func(D1: twin_Function, D2: twin_Function):
    S_1 = S_1_multiply(D1, D2)
    S_2 = S_2_multiply(D1, D2)
    # min1<min2<=max1<max2 or min2<min1<=max2<max1
    if S_1 == None or S_2 == None or S_1 == S_2:
        return twin_Function(Interval(None, None),Interval(min(S_1.a,S_2.a),max(S_2.a,S_2.b)),'0')
    if (S_1.a < S_2.a <= S_1.b and S_1.b < S_2.b) or (S_2.a < S_1.a and S_1.a <= S_2.b and S_2.b < S_1.b):
        return twin_Function(Interval(None, None),Interval(min(S_1.a,S_2.a),max(S_2.a,S_2.b)),'0')
    elif S_1.b <= S_2.a:
        return twin_Function(Interval(S_1.b,S_2.a),Interval(S_1.a,S_2.b),'+')
    elif S_1.a >= S_2.b:
        return twin_Function(Interval(S_2.b,S_1.a),Interval(S_2.a,S_1.b),'-')

def const_multi_func(n,D1: twin_Function):
    if n >= 0:
        return twin_Function(Interval(n*D1.inside.a,n* D1.inside.b),Interval(n * D1.external.a,n* D1.external.b),D1.alpha)

# x^n
def powerBase_func(n,D1: twin_Function):
    return twin_Function(Interval(pow(D1.inside.a,n), pow(D1.inside.b,n)),
                         Interval(pow(D1.external.a,n),pow(D1.external.b,n)), D1.alpha)
# n^x
def powerExp_func(n,D1: twin_Function):
    return twin_Function(Interval(pow(n,D1.inside.a), pow(n,D1.inside.b)),
                         Interval(pow(n,D1.external.a),pow(n,D1.external.b)), D1.alpha)

def Trig_func (n,D1: twin_Function):
    if n=='sin':
        return twin_Function(Interval(min(math.sin(D1.inside.a),math.sin(D1.inside.b)),
                                      max(math.sin(D1.inside.a),math.sin(D1.inside.b))),
                             Interval(min(math.sin(D1.external.a),math.sin(D1.external.b)),
                                      max(math.sin(D1.external.a),math.sin(D1.external.b))),D1.alpha)
    if n=='cos':
        return twin_Function(Interval(min(math.cos(D1.inside.a), math.cos(D1.inside.b)),
                                      max(math.cos(D1.inside.a), math.cos(D1.inside.b))),
                             Interval(min(math.cos(D1.external.a), math.cos(D1.external.b)),
                                      max(math.cos(D1.external.a), math.cos(D1.external.b))), D1.alpha)
    if n=='tg':
        return twin_Function(Interval(min(math.tan(D1.inside.a), math.tan(D1.inside.b)),
                                      max(math.tan(D1.inside.a), math.tan(D1.inside.b))),
                             Interval(min(math.tan(D1.external.a), math.tan(D1.external.b)),
                                      max(math.tan(D1.external.a), math.tan(D1.external.b))), D1.alpha)