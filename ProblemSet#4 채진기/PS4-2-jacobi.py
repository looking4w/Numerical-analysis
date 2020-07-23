# Jacobi method fomular 안에 시그마 연산을 해줄 함수를 정의합니다.
def Cal(i):
    if i == 0:
        res = (A[i][3] * prevx[3]) + (A[i][4] * prevx[4])
        return res
    elif i == 1:
        res = A[i][3] * prevx[3]
        return res
    elif i == 2:
        res = A[i][6] * prevx[6]
        return res
    elif i == 3:
        res = (A[i][5] * prevx[5]) + (A[i][6] * prevx[6])
        return res
    elif i == 4:
        res = A[i][7] * prevx[7]
        return res
    elif i == 6:
        res = A[i][3] * prevx[3]
        return res
    elif i == 7:
        res = A[i][6] * prevx[6]
        return res
    else:
        return 0

if __name__ == '__main__':
    n = 8
    iter = 0
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
        for i in range(0, n):
            x[i] = (B[i] - Cal(i)) / (A[i][i])
        res1 = max([abs(a-b) for a, b in zip(prevx, x)])
        res2 = max(abs(a) for a in x)
        cut = res1 / res2
        iter += 1
        if cut < 10 **(-6):
            break
    print(f'{iter}번 반복한 결과로,')
    print(f'transposed x = {x} 이고')
    print(f'norm of (x(k) - x(k-1)) / x(k) = {cut} 입니다.')