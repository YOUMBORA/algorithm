T = int(input())

for _ in range(T):
    n = int(input())

    fibo = [[0, 0] for _ in range(2 + n + 1)]
    fibo[0] = [1, 0]
    fibo[1] = [0, 1]

    for i in range(2, n+1):
        fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
        fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

    print(f"{fibo[n][0]} {fibo[n][1]}")
