from operation_Function import *
from operation import *

if __name__ == '__main__':
    # ....................................................................................................
    T1_a1 = 5
    T1_a2 = 10
    T1_b1 = 1
    T1_b2 = 20
    T2_a1 = 1
    T2_a2 = 5
    T2_b1 = 0
    T2_b2 = 6
    T3_a1 = 1
    T3_a2 = 5
    T3_b1 = 0
    T3_b2 = 7
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
    D3_a = Interval(T3_a1, T3_a2)
    D3_b = Interval(T3_b1, T3_b2)
    D1_alpha = '-'
    D2_alpha = '+'
    D3_alpha = '-'
    D1 = twin_Function(D1_a, D1_b, D1_alpha)
    D1.print_result()
    # D2 = twin_Function(D2_a, D2_b, D2_alpha)
    # D2.print_result()
    # D3 = twin_Function(D3_a, D3_b, D3_alpha)
    # D3.print_result()
    # print('D1 + D2')
    # plus_function(D1, D2)
    # print('D2 + D3',gamma(D2,D3))
    # plus_function(D2, D3)
    # print('unary_minus')
    # unary_minus_twin_function(D2).print_result()
    print('inverse')
    inverse_twin_function(D1).print_result()
    # .....................................................................................................
