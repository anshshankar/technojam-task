def diagonalOrder1(arr, n, m):
    ans = [[] for i in range(n + m - 1)]

    for i in range(m):
        for j in range(n):
            ans[i + j].append(arr[j][i])

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = " ")
        print()

def diagonalOrder2(arr, n, m):
    ans = [[] for i in range(n + m - 1)]
    for i in range(m-1,-1,-1):
        for j in range(0,n):
            ans[min(m,n)-1-i+j].append(arr[j][i])

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = " ")
        print()

def diagonalOrder3(arr, n, m):
    ans = [[] for i in range(n + m - 1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            ans[m+n-2-i - j].append(arr[i][j])
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = " ")
        print()

def diagonalOrder4(arr, n, m):
    ans = [[] for i in range(n + m - 1)]
    for i in range(m-1,-1,-1):
        for j in range(0,n):
            ans[min(m,n)-1-i+j].append(arr[i][j])

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = " ")
        print()


m,n,p=input().split()
m,n,p=int(m),int(n),int(p)
a=[]
for i in range(0,m):
    a.append(list(input().split()))


if(p==1):
    diagonalOrder1(a, n, m)
elif(p==2):
    diagonalOrder2(a,n,m)
elif(p==3):
    diagonalOrder3(a,n,m)
elif(p==4):
    diagonalOrder4(a,n,m)



