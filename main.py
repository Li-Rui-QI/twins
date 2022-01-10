from intvalpy import Interval
from twin import *
from operation import *

if __name__ == '__main__':
    T1_a1 = 2
    T1_a2 = 5
    T1_b1 = 1
    T1_b2 = 10
    T2_a1 = 1
    T2_a2 = 3
    T2_b1 = 5
    T2_b2 = 12

    T1_data1 = Interval(T1_a1, T1_a2)
    # T1_data1 = Interval(None,None)
    T1_data2 = Interval(T1_b1,T1_b2)
    # T2_data1 = Interval(T2_a1,T2_a2)
    T2_data1 = Interval(None, None)
    T2_data2 = Interval(T2_b1, T2_b2)

    T1 = twin(T1_data1,T1_data2)
    T1.Print_result()
    T2 = twin(T2_data1,T2_data2)
    T2.Print_result()
    # print('p = ',p(T1 , T2) ,'q = ', q(T1,T2))
    # print('операция сложения')
    # plus(T1,T2).Print_result()
    # print('операция умножение')
    # multiply(T1,T2).Print_result()
    # unary_minus_twin(T1).Print_result()
    inverse_twin(T1).Print_result()

