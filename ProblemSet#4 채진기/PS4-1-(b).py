from sympy import *
# y의 일차도함수에 대한 식을 정의해줍니다.
def df(t, y):
    res = t**(2) - y**(2)
    return res

def dff(t, y):
    if t**(2) - y**(2) == 0:
        return 0
    else:
        res = (1/3) * t**(3) - y**(3) / 3 * (t**(2) - y**(2))
        return res

# Runge-Kutta 공식을 계산해줄 함수를 정의합니다.
def Runge1(t0, tn, y0, h):

    while t0 < tn:

        k1 = h * df(t0, y0)
        k2 = h * df(t0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * df(t0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * df(t0 + h, y0 + k3)

        y = y0 + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t0 = round(t0 + h, 6)
        y0 = y
    return y0

def Runge2(t0, tn, y0, h):

    while t0 < tn:

        k1 = h * dff(t0, y0)
        k2 = h * dff(t0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * dff(t0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * dff(t0 + h, y0 + k3)

        y = y0 + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t0 = round(t0 + h, 6)
        y0 = y
    return y0

if __name__ == '__main__':
    t0 = 0
    y0 = 0
    tn = 1000
    h = 0.001
    res1 = round(exp(Runge1(t0, tn, y0, h)), 10)
    res2 = round(exp(Runge2(t0, tn, y0, h)), 10)
    approx = res1 / res2
    print(approx)