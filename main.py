from operation_Function import *
from operation import *

if __name__ == '__main__':
    # ....................................................................................................
    T1_a1 = 1
    T1_a2 = 10
    T1_b1 = 0
    T1_b2 = 11
    T2_a1 = 1
    T2_a2 = 5
    T2_b1 = 0
    T2_b2 = 6
    # ....................................................................................................
    # T1_data1 = Interval(T1_a1, T1_a2)
    # # T1_data1 = Interval(None,None)
    # T1_data2 = Interval(T1_b1, T1_b2)
    # T2_data1 = Interval(T2_a1,T2_a2)
    # T2_data2 = Interval(T2_b1, T2_b2)
    # T1 = twin(T1_data1, T1_data2)
    # T2 = twin(T2_data1, T2_data2)
    # print('twin plus')
    # plus(T1,T2).Print_result()

    # T2_data1 = Interval(None, None)
    #
    #
    # T1.Print_result()
    #
    # T2.Print_result()
    # print('p = ',p(T1 , T2) ,'q = ', q(T1,T2))
    # print('операция сложения')
    # plus(T1,T2).Print_result()
    # print('операция умножение')
    # multiply(T1,T2).Print_result()
    # unary_minus_twin(T1).Print_result()
    # inverse_twin(T1).Print_result()

    # ....................................................................................................
    print('function plus')
    D1_a = Interval(T1_a1, T1_a2)
    D1_b = Interval(T1_b1, T1_b2)
    D2_a = Interval(T2_a1, T2_a2)
    D2_b = Interval(T2_b1, T2_b2)
    D1_alpha = '+'
    D2_alpha = '+'
    D1 = twin_Function(D1_a, D1_b, D1_alpha)
    D1.print_result()
    D2 = twin_Function(D2_a, D2_b, D2_alpha)
    D2.print_result()
    plus_function(D1, D2)
    # .....................................................................................................
