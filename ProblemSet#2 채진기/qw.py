from sympy import *

# 이번 문제의 피적분함수를 정의합니다.
def f(x):
    y = sin(x) / x
    return y

# 시그마를 계산해줄 함수를 정의합니다.
def Sigma(NumberofSubinterval, a, b):
    A = 0
    iterationNum = NumberofSubinterval - 1
    h = abs(b - a)/ NumberofSubinterval
    for i in range(1, (iterationNum + 1)):
        A += f(a + i * h)
    return A

# Composite Trapezoidal rule을 이용해 2^(n-1)개의 subinterval 로부터 0부터 1까지의 f(x)의 적분값을 근사하는 함수입니다.
def Trape(n, a, b):
    NumberofSubinterval = 2 ** (n - 1)
    h = abs(b - a) / NumberofSubinterval
    res = (h/2) * (f(a) + f(b) + 2 * Sigma(NumberofSubinterval, a, b))
    return res

# a = 0 일 때, 분모의 x 때문에 값이 정의되지 않습니다. 따라서 0에 가까운 근사값을 넣어줍니다.
# 2차원 배열을 통해 roomberg의 행렬을 표현했습니다.
if __name__ == '__main__':
    a = 0.000000001
    b = round(pi, 6)
    num = 8
    arr = [[0 for col in range(11)] for row in range(11)]
    arr[0][0] = Trape(1, a, b)
    for i in range(1, num + 2):
        arr[i][0] = Trape(i + 1, a, b)
        for j in range(1, num + 2):
            arr[i][j] = arr[i][j - 1] + (1 / ((4 ** (j)) - 1)) * (arr[i][j - 1] - arr[i - 1][j - 1])
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print(f'R8,8의 값은 {arr[9][9]}입니다.')