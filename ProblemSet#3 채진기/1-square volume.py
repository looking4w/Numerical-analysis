# z값을 계산해줄 함수를 정의합니다.
def f(x, y):
    res = (1 - (x ** 4) - (y ** 4)) ** (0.25)
    return res

# y값을 계산해줄 함수를 정의합니다.
def y(x):
    res = ((1 - (x ** 4)) ** 0.25)
    return res

# x-y plane 에서 직선함수 x 를 뺀 결과인, y값의 도메인을 계산해줄 함수를 정의합니다.
def df(x):
    res = ((1 - (x ** 4)) ** 0.25) - x
    return res

# 고정된 x 값위에 y 값들을 더해주는 용도로 Composite Trapezoidal 방식을 이용했습니다.
def Trape(n):
    arr = [0 for _ in range(n + 1)]
    add = 0
    for i in range(0, (n + 1)):
        A = 0
        h2 = df(i * h1) / n
        # 고정된 x 값에서 y 를 움직이면서 z 값들을 차곡차곡 더해주는 반복문 입니다.
        for j in range(1, n):
            A += f((i * h1), (i * h1) + (j * h2))

        arr[i] = (h2 / 2) * (f((i * h1), (i * h1)) + f((i * h1), (i * h1) + (j * h2)) + 2 * A)

    for i in range(1, n):
        add += 2 * arr[i]

    res = (h1 / 2) * (add + arr[0] + arr[n - 1])

    return res

if __name__ == '__main__':
    n = 1000
    a = 0
    b = 0.8409
    h1 = (b - a) / n
    res = Trape(n)
    Volume = 16 * res
    print(f'\n부피의 근삿값은 {Volume} 입니다.')