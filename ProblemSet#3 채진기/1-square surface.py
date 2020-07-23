from sympy import *

# are length 공식의 피적분함수 sqrt(1 + (dy/dx)^2)을 변형한 입체도형의 둘레를 구하기 위한 피적분함수 입니다.
# z값을 움직여주면서 단면 원의 둘레를 계산한 후 합쳐주고자 합니다.
def f(x, z):
    res = sqrt( 1 + ((-x ** 3) * ((1 - (z ** 4) - (x ** 4)) ** (-0.75))) ** 2 )
    return res

# 둘레의 범위가 될 x값을 계산해줄 함수를 정의합니다. z 값이 바뀌면서 y = x 함수와 x-y 평면의 단면적 함수가 만나는 점을 계산해줍니다.
def df(z):
    x = Symbol('x')
    equation = (1 - (x ** 4) - (z ** 4)) ** (0.25) - x
    res = solve(equation, dict=true)
    return res[0][x]

# z 를 움직여주면서 각 단면적에 대한 둘레를 구하고 그것들을 더해주는 방식으로 Composite Trapezoidal 방식을 이용했습니다.
def Trape(n):
    arr = [0 for _ in range(n)]
    add = 0

    for i in range(0, n):
        A = 0
        h1 = df(i * h2) / n

        for j in range(1, n - 1):
            A += f((j * h1), (i * h2))

        arr[i] = (h1 / 2) * (f((0), (i * h1)) + f((n * h1), (i * h1)) + 2 * A)

    for i in range(1, n - 1):
        add += 2 * arr[i]

    res = (h2 / 2) * (add + arr[0] + arr[n - 1])

    return res

if __name__ == '__main__':
    n = 100
    h2 = 1 / n
    res = Trape(n)
    Surface = 16 * res
    print(f'\n표면적의 근삿값은 {Surface} 입니다.')
