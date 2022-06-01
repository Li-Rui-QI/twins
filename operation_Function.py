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
            (D1.external.b + D2.inside.a) >= (D2.inside.b + D1.external.a):
        return D2.alpha
    else:
        return 0


# D_1  = (I_1l,I_1,α)= (T_1,α)=([a-,a+ ],[А-,А+ ],α),
# D_2= (I_2l,I_2,β) = (Т_2,β) = ([b-,b+ ],[B-,B+ ],β)
def plus_function(D1: twin_Function, D2: twin_Function):
    if D1.alpha == D2.alpha and D1.alpha != '0' and D2 != '0' and \
            D1.inside_width() != -1 and D2.inside_width() != -1:
        return twin_Function(Interval(D1.inside.a + D2.inside.a, D1.inside.b + D2.inside.b),
                             Interval(D1.external.a + D2.external.a, D1.external.b + D2.external.b),
                             gamma(D1, D2)).print_result()
    elif D1.alpha != '0' and D2 != '0' and D1.alpha != D2.alpha and \
            D1.inside_width() != -1 and D2.inside_width() != -1:
        if gamma(D1, D2) == '0':
            return twin_Function(Interval(None, None),
                                 Interval(min(D1.external.a + D2.inside.b),
                                          max(D1.inside.a + D2.external.b, D2.inside.a + D1.external.b)), '0').print_result()
        elif gamma(D1, D2) == D1.alpha:

            return twin_Function(Interval(D1.inside.a + D2.external.b, D2.external.a + D1.inside.b),
                                 Interval(D1.external.a + D2.inside.b, D2.inside.a + D1.external.b),
                                 D1.alpha).print_result()
        elif gamma(D1, D2) == D2.alpha:
            return twin_Function(Interval(D2.inside.a + D1.external.b, D2.external.a + D1.inside.b),
                                 Interval(D2.external.a + D1.inside.b, D1.inside.a + D2.external.b),
                                 D2.alpha).print_result()
    elif D1.alpha=='0' or D2.alpha=='0' or D1.inside_width() == -1 or D2.inside_width() == -1:
        T1=twin(D1.inside,D1.external)
        T2=twin(D2.inside,D2.external)
        return (plus(T1,T2).Print_result(), print('gamma',gamma(D1, D2)))
