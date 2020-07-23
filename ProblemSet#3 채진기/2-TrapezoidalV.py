from sympy import *

# 1차 미분방정식 중 첫번째 함수를 정의합니다. dU1(t) means that y'(t) = z(t) = cos(t)
def dU1(t):
    res = cos(t)
    return res

# 1차 미분방정식 중 두번째 함수를 정의합니다. dU2(t) means that y''(t) = -y(t) = -sin(t)
def dU2(t):
    res = -sin(t)
    return res

# Trapezoidal vector version method 를 계산해줄 함수를 정의합니다.
def TrapeV(y0, z0, h):
    y = [0 for _ in range(21)]
    z = [0 for _ in range(21)]

    y[0] = y0
    z[0] = z0

    for i in range(0, 20):
        y[i + 1] = y[i] + (h/2) * (dU1(i * h) + dU1((i * h) + h))
        z[i + 1] = z[i] + (h/2) * (dU2(i * h) + dU2((i * h) + h))
        print(y[i])
        # print(z[i])

    print(y[20])
    # print(z[20])
    return y, z

if __name__ == '__main__':

    y0 = 0
    z0 = 1
    h = round(pi / 10, 100)
    TrapeV(y0, z0, h)