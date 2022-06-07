from operation import *
from operation_Function import *
from math import e
if __name__ == '__main__':
    # ....................................................................................................
    T1_a1 = 1.4
    T1_a2 = 1.5
    T1_b1 = 1.4
    T1_b2 = 1.5
    T2_a1 = 1.4
    T2_a2 = 1.5
    T2_b1 = 1.4
    T2_b2 = 1.5
    T3_a1 = 10
    T3_a2 = 11
    T3_b1 = 3
    T3_b2 = 20
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
    # print('function plus')
    # D1_a = Interval(T1_a1, T1_a2)
    # D1_a = Interval(None, None)
    # D1_b = Interval(T1_b1, T1_b2)
    # D2_a = Interval(T2_a1, T2_a2)
    # # D2_a = Interval(None,None)
    # D2_b = Interval(T2_b1, T2_b2)
    # D3_a = Interval(T3_a1, T3_a2)
    # D3_b = Interval(T3_b1, T3_b2)
    # D1_alpha = '-'
    # D2_alpha = '+'
    # D3_alpha = '-'
    # D1 = twin_Function(D1_a, D1_b, D1_alpha)
    # D1.print_result()
    # D2 = twin_Function(D2_a, D2_b, D2_alpha)
    # D2.print_result()
    # D3 = twin_Function(D3_a, D3_b, D3_alpha)
    # D3.print_result()
    ### .................................. plus....................................................

    # print('D1 + D2')
    # plus_function(D1, D2)
    # print('D2 + D3',gamma(D2,D3))
    # plus_function(D2, D3)

    ### ..................................multiply.........................................................
    # print('multiply')
    # print(S_1_multiply(D2,D3))
    # print(S_2_multiply(D2,D3))
    # multiply_twin_function(D2,D3).print_result()
    ###...................................unary.........................................................

    # print('unary_minus')
    # unary_minus_twin_function(D2).print_result()

    ### .................................. inverse....................................................
    # print('inverse')
    # inverse_twin_function(D1).print_result()
    # ...................................f(x,y)=(10e^x-x)(tgy-x^2).................................................................
    D1_a = Interval(T1_a1, T1_a2)
    D1_b = Interval(T1_b1, T1_b2)
    D1_alpha = '+'
    D1 = twin_Function(D1_a, D1_b, D1_alpha)
    D1.print_result()
    print('применение направленной твинной арифметики ')
    # -x:
    print('-x:')
    minus_function(D1).print_result()
    D1_mius = twin_Function(minus_function(D1).inside,
                            minus_function(D1).external,minus_function(D1).alpha)
    # e^x
    print('e^x:')
    powerExp_func(e,D1).print_result()
    D1_e = twin_Function(powerExp_func(e,D1).inside,
                         powerExp_func(e,D1).external,powerExp_func(e,D1).alpha)
    # 10e^x
    print('10e^x')
    const_multi_func(10,D1_e).print_result()
    D1_10e = twin_Function(const_multi_func(10,D1_e).inside,
                           const_multi_func(10,D1_e).external,const_multi_func(10,D1_e).alpha)
    # 10*e^x-x
    print('10*e^x-x')
    plus_func(D1_10e,D1_mius).print_result()
    D1_left = twin_Function(plus_func(D1_10e,D1_mius).inside,
                            plus_func(D1_10e,D1_mius).external,plus_func(D1_10e,D1_mius).alpha)
    # tgx
    print('tgx')
    Trig_func('tg',D1).print_result()
    D1_tg = twin_Function(Trig_func('tg',D1).inside,
                          Trig_func('tg',D1).external,Trig_func('tg',D1).alpha)

    # x^2
    print('x^2')
    powerBase_func(2,D1).print_result()
    D1_x_2=twin_Function(powerBase_func(2,D1).inside,
                         powerBase_func(2,D1).external,powerBase_func(2,D1).alpha)
    # -x^2
    print('-x^2')
    minus_function(D1_x_2).print_result()
    D1_2_mius = twin_Function(minus_function(D1_x_2).inside,
                            minus_function(D1_x_2).external,minus_function(D1_x_2).alpha)
    # tgx-x^2
    print('tgx-x^2')
    plus_func(D1_tg, D1_2_mius).print_result()
    D1_right = twin_Function(plus_func(D1_tg, D1_2_mius).inside,
                            plus_func(D1_tg, D1_2_mius).external, plus_func(D1_tg, D1_2_mius).alpha)
    # f(x,y)=(10e^x-x)(tgy-x^2)
    print('(10e^x-x)(tgy-x^2)')
    multiply_func(D1_left,D1_right).print_result()

# ...................................f(x,y)=(10e^x-x)(tgy-x^2)...............................................................
    print('применение арифметики твинов')
    # T1_left = twin(plus_func(D1_10e, D1_mius).inside,
    #                         plus_func(D1_10e, D1_mius).external)
    # T1_right = twin(plus_func(D1_tg, D1_2_mius).inside,
    #                         plus_func(D1_tg, D1_2_mius).external)
    # multiply(T1_left,T1_right).Print_result()
