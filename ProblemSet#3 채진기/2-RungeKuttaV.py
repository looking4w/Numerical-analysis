from sympy import *

# 1차 미분방정식 중 첫번째 함수를 정의합니다. dU1(t) means that y'(t) = z(t) = cos(t)
def dU1(t):
    res = cos(t)
    return res

# 1차 미분방정식 중 두번째 함수를 정의합니다. dU2(t) means that y''(t) = -y(t) = -sin(t)
def dU2(t):
    res = -sin(t)
    return res

# Runge Kutta 4 order vector version을 계산해줄 함수를 정의합니다.
def RungeV(y0, z0, h):
    y = [0 for _ in range(21)]
    z = [0 for _ in range(21)]

    y[0] = y0
    z[0] = z0

    for i in range(0, 20):

        k1 = h * dU1(i * h)
        dk1 = h * dU2(i * h)
        k2 = h * dU1((i * h) + (h/2))
        dk2 = h * dU2((i * h) + (h/2))
        k3 = h * dU1((i * h) + (h/2))
        dk3 = h * dU2((i * h) + (h/2))
        k4 = h * dU1((i * h) + h)
        dk4 = h * dU2((i * h) + h)

        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        z[i + 1] = z[i] + (dk1 + 2*dk2 + 2*dk3 + dk4) / 6
        print(y[i])
        # print(z[i])

    print(y[20])
    # print(z[20])
    return y, z

if __name__ == '__main__':

    y0 = 0
    z0 = 1
    h = round(pi / 10, 10)
    RungeV(y0, z0, h)