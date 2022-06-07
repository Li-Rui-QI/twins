from intvalpy import Interval, intersection
from twin import *


def p(T1: twin, T2: twin):
    if T1.inside_width() == -1 and T2.inside_width() == -1:
        return None
    if T1.inside_width() == -1:
        return T2.inside.a + T1.external.b
    if T2.inside_width() == -1:
        return T1.inside.a + T2.external.b
    return min(T1.inside.a + T2.external.b, T2.inside.a + T1.external.b)


def q(T1: twin, T2: twin):
    if T1.inside_width() == -1 and T2.inside_width() == -1:
        return None
    if T1.inside_width() == -1:
        return T2.inside.b + T1.external.a
    if T2.inside_width() == -1:
        return T1.inside.b + T2.external.a
    return max(T1.inside.b + T2.external.a, T2.inside.b + T1.external.a)

def plus(T1: twin, T2: twin):
    if T1.external_width() <= T2.inside_width() or T2.external_width() <= T1.inside_width():
        return twin(Interval(p(T1, T2), q(T1, T2)),
                    Interval(T1.external.a + T2.external.a, T1.external.b + T2.external.b))
    else:
        return twin(
            Interval(None, None),
            Interval(T1.external.a + T2.external.a, T1.external.b + T2.external.b)
        )


def phi(I1, I2):
    Z = intersection(I1, I2)

    if isnan(float(Z.a)) or isnan(float(Z.b)):
        return Interval(float('nan'), float('nan'))
    else:
        min_ = abs(I1.a - I2.a)
        min_a = I1.a
        min_b = I2.a

        if abs(I1.b - I2.b) < min_:
            min_ = abs(I1.b - I2.b)
            min_a = I1.b
            min_b = I2.b

        if abs(I1.a - I2.b) < min_:
            min_ = abs(I1.a - I2.b)
            min_a = I1.a
            min_b = I2.b

        if abs(I1.b - I2.a) < min_:
            min_ = abs(I1.b - I2.a)
            min_a = I1.b
            min_b = I2.a

        return Interval(min_a, min_b)


def psi(I1, I2):
    return Interval(
        min(I1.a, I1.b, I2.a, I2.b),
        max(I1.a, I1.b, I2.a, I2.b)
    )


def multiply(T1: twin, T2: twin):
    if T1.inside_width() == -1 and T2.inside_width() == -1:
        return twin(
            Interval(None, None),
            Interval(T1.external.a, T1.external.b) * Interval(T2.external.a, T2.external.b)
        )

    if T1.inside_width() == -1:
        return twin(
            phi(
                T2.inside.a * Interval(T1.external.a, T1.external.b),
                T2.inside.b * Interval(T1.external.a, T1.external.b)
            ),
            Interval(T1.external.a, T1.external.b) * Interval(T2.external.a, T2.external.b)
        )

    if T2.inside_width() == -1:
        return twin(
            phi(
                T1.inside.a * Interval(T2.external.a, T2.external.b),
                T1.inside.b * Interval(T2.external.a, T2.external.b)
            ),
            Interval(T1.external.a, T1.external.b) * Interval(T2.external.a, T2.external.b)
        )

    return twin(
        psi(
            phi(
                (T1.inside.a) * Interval(T2.external.a, T2.external.b),
                (T1.inside.b) * Interval(T2.external.a, T2.external.b)
            ),
            phi(
                T2.inside.a * Interval(T1.external.a, T1.external.b),
                T2.inside.b * Interval(T1.external.a, T1.external.b)
            )
        ),
        Interval(T1.external.a, T1.external.b) * Interval(T2.external.a, T2.external.b)
    )


def unary_minus_twin(T: twin):
    return twin(-T.inside, -T.external)


def inverse_twin(T: twin):
    if 0 in T.inside or 0 in T.external:
        print("Cannot be divided into intervals containing 0.")
        exit()
    return twin(1 / T.inside, 1 / T.external)
