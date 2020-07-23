from sympy import *

# SOR fomular 에서 첫번째 시그마(LOW행렬 연산)를 계산할 함수를 정의해줍니다.
def LOW(i):
    if i == 6:
        res = A[i][3] * x[3]
        return res
    elif i == 7:
        res = A[i][6] * x[6]
        return res
    else:
        return 0

# SOR fomular 에서 두번째 시그마(UP행렬 연산)를 계산할 함수를 정의해줍니다.
def UP(i):
    if i == 0:
        res = (A[i][3] * x[3]) + (A[i][4] * x[4])
        return res
    elif i == 1:
        res = A[i][3] * x[3]
        return res
    elif i == 2:
        res = A[i][6] * x[6]
        return res
    elif i == 3:
        res = (A[i][5] * x[5]) + (A[i][6] * x[6])
        return res
    elif i == 4:
        res = A[i][7] * x[7]
        return res
    elif i == 7:
        res = A[i][7] * x[7]
        return res
    else:
        return 0

if __name__ == '__main__':
    w = 1
    n = 8
    A = [[-1, 0, 0, 1/(2**(0.5)), 1, 0, 0, 0],
         [0, -1, 0, 1/(2**(0.5)), 0, 0, 0, 0],
         [0, 0, -1, 0, 0, 0, 0.5, 0],
         [0, 0, 0, -1/(2**(0.5)), 0, -1, -0.5, 0],
         [0, 0, 0, 0, -1, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, -1/(2**(0.5)), 0, 0, 3**(0.5)/2, 0],
         [0, 0, 0, 0, 0, 0, -3**(0.5)/2, -1]]

    B = [0, 0, 0, 0, 0, 10000, 0, 0]
    x = [0, 0, 0, 0, 0, 0, 0, 0]
    prevx = [0, 0, 0, 0, 0, 0, 0, 0]
    # previous x 배열로 x(k-1)항을 받아 stopping criterion 을 계산할 때 이용합니다.
    while True:
        prevx = [i for i in x]
        print(x)
        for i in range(0, n):
            x[i] = (1 - w) * x[i] + (w / A[i][i]) * (B[i] - LOW(i) - UP(i))
        res1 = max([abs(a-b) for a, b in zip(prevx, x)])
        res2 = max(abs(a) for a in x)
        cut = res1 / res2
        if cut < 10 **(-6):
            break

    print(f'transposed x = {x} 이고', ', ', f'norm of (x(k) - x(k-1)) / x(k) = {cut} 입니다.')

