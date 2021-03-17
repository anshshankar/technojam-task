def diagonalOrder(arr, n, m):
    ans = [[] for i in range(n + m - 1)]

    for i in range(m):
        for j in range(n):
            ans[i + j].append(arr[j][i])

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = " ")
        print()
