# y에 대한 일차도함수에 대한 식을 정의해줍니다.
def df(t, y):
    res = 1 + (y / t)
    return res

# Runge-Kutta 공식을 계산해줄 함수를 정의합니다.
def Runge(t0, tn, y0, h):

    while t0 < tn:

        k1 = h * df(t0, y0)
        k2 = h * df(t0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * df(t0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * df(t0 + h, y0 + k3)

        y = y0 + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        print(y)
        t0 = round(t0 + h, 4)
        y0 = y

if __name__ == '__main__':
    t0 = 1
    tn = 2
    y0 = 2
    h = 1 / 40
    Runge(t0, tn, y0, h)