# i = 0 부터 각각 x, y, z의 일반화된 해입니다.
def Cal(i):
    if i == 0:
        res = B[i] + 0.1 * (Sol[1])**(2) - 0.05 * (Sol[2])**(2)
        return res
    elif i == 1:
        res = B[i] -0.3 * (Sol[0])**(2) + 0.1 * (Sol[0] * Sol[2])
        return res
    else:
        res = B[i] -0.4 * (Sol[1])**(2) -0.1 * (Sol[0] * Sol[1])
        return res

# Sol 행렬은 x, y, z 를 의미합니다.
if __name__ == '__main__':
    Sol = [0, 0, 0]
    prev = [0, 0, 0]
    B = [0.7, 0.5, 1.2]
    n = 3
    iter = 0
    while True:
        prev = [i for i in Sol]
        for i in range(0, n):
            Sol[i] = Cal(i)
        res1 = max([abs(a-b) for a, b in zip(prev, Sol)])
        res2 = max(abs(a) for a in Sol)
        cut = res1 / res2
        iter += 1
        if cut < 10 **(-6):
            break
    print(f'{iter}번 반복한 결과로 x, y, z = {Sol} 입니다.')