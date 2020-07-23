from sympy import *

# 문제에서 제시된 1차 미분방정식을 정의해줍니다.
def f(t, y):
    res = y - (t ** 2) + 1
    return res

# 미분방정식의 해인, 함수 y 를 정의해줍니다.
def sol(t):
    res = ((t + 1) ** 2) - 0.5 * exp(t)
    return res

# Adams-Bashforth four-step을 이용해 얻은 추정치로 Moulton three-step에 적용하여 새로운 추정값을 계산합니다.
def Pred(h):
    t = [0 for _ in range(21)]
    w = [0 for _ in range(21)]
    neww = [0 for _ in range(21)]

    for i in range(0, 21):
        t[i] = i * h

    for i in range(0, 4):
        w[i] = sol(i * h)

    for i in range(3, 20):
        w[i + 1] = w[i] + (h/24) * ((55 * f(t[i], w[i])) - (59 * f(t[i - 1], w[i - 1])) + (37 * f(t[i - 2], w[i - 2])) - (9 * f(t[i - 3], w[i - 3])))

    for i in range(0, 21):
        neww[i] = w[i]

    for i in range(2, 20):
        neww[i + 1] = neww[i] + (h/24) * ((9 * f(t[i + 1], neww[i + 1])) + (19 * f(t[i], neww[i])) - (5 * f(t[i - 1], neww[i - 1])) + f(t[i - 2], neww[i - 2]))
    return neww

if __name__ == '__main__':
    approx = Pred(0.1)

    for i in range(0, 21):
        print(approx[i])