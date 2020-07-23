# y의 일차도함수에 대한 식을 정의해줍니다.
def df(t, y):
    res = t**(2) - y**(2)
    return res

# Runge-Kutta 공식을 계산해줄 함수를 정의합니다.
def Runge(t0, tn, y0, h):

    while t0 < tn:

        k1 = h * df(t0, y0)
        k2 = h * df(t0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * df(t0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * df(t0 + h, y0 + k3)

        y = y0 + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t0 = round(t0 + h, 4)
        print(y)
        y0 = y

if __name__ == '__main__':
    t0 = 0
    y0 = 0
    for i in range(1,19):

        Runge(t0, i, y0, 1/8)
        print()
# tn 값과 h값을 바꿔가면서 값이 튀는 지점을 체크했습니다.