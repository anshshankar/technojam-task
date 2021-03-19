def c11(m,n,a):
    k,l = 0,0
    while (k < m and l < n):
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1

def c12(m,n,arr):
    k,l = 0,0
    cnt = 0
    t = m * n
    while (k < m and l < n) :
        if (cnt == t) :
            break
        for i in range(k, m) :
            print(arr[i][l], end = " ")
            cnt += 1
        l += 1
        if (cnt == t) :
            break
        for i in range (l, n) :
            print( arr[m - 1][i], end = " ")
            cnt += 1
        m -= 1
        if (cnt == t) :
            break
        if (k < m) :
            for i in range(m - 1, k - 1, -1) :
                print(arr[i][n - 1], end = " ")
                cnt += 1
            n -= 1
        if (cnt == t) :
            break
        if (l < n) :
            for i in range(n - 1, l - 1, -1) :
                print( arr[k][i], end = " ")
                cnt += 1
            k += 1

def c21(m,n,a):
    k,l = 0,0
    while (k < m and l < n):

        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1

def c22(m,n,arr):
    k,l = 0,0
    cnt = 0
    t = m * n
    while (k < m and l < n) :
        if (cnt == t) :
            break
        if (l < n) :
            for i in range(n - 1, l - 1, -1) :
                print( arr[k][i], end = " ")
                cnt += 1
            k += 1
        if (cnt == t) :
            break
        for i in range(k, m) :
            print(arr[i][l], end = " ")
            cnt += 1
        l += 1
        if (cnt == t) :
            break
        for i in range (l, n) :
            print( arr[m - 1][i], end = " ")
            cnt += 1
        m -= 1
        if (cnt == t) :
            break
        if (k < m) :
            for i in range(m - 1, k - 1, -1) :
                print(arr[i][n - 1], end = " ")
                cnt += 1
            n -= 1


def c31(m,n,a):
    k,l = 0,0
    while (k < m and l < n):

        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1

def c32(m,n,arr):
    k,l = 0,0
    cnt = 0
    t = m * n
    while (k < m and l < n) :
        if (cnt == t) :
            break
        if (k < m) :
            for i in range(m - 1, k - 1, -1) :
                print(arr[i][n - 1], end = " ")
                cnt += 1
            n -= 1
        if (cnt == t) :
            break
        if (l < n) :
            for i in range(n - 1, l - 1, -1) :
                print( arr[k][i], end = " ")
                cnt += 1
            k += 1
        if (cnt == t) :
            break
        for i in range(k, m) :
            print(arr[i][l], end = " ")
            cnt += 1
        l += 1
        if (cnt == t) :
            break
        for i in range (l, n) :
            print( arr[m - 1][i], end = " ")
            cnt += 1
        m -= 1


def c41(m,n,a):
    k,l = 0,0
    while (k < m and l < n):
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1

def c42(m,n,arr):
    k,l = 0,0
    cnt = 0
    t = m * n
    while (k < m and l < n) :
        if (cnt == t) :
            break
        for i in range (l, n) :
            print( arr[m - 1][i], end = " ")
            cnt += 1
        m -= 1
        if (cnt == t) :
            break
        if (k < m) :
            for i in range(m - 1, k - 1, -1) :
                print(arr[i][n - 1], end = " ")
                cnt += 1
            n -= 1
        if (cnt == t) :
            break
        if (l < n) :
            for i in range(n - 1, l - 1, -1) :
                print( arr[k][i], end = " ")
                cnt += 1
            k += 1
        if (cnt == t) :
            break
        for i in range(k, m) :
            print(arr[i][l], end = " ")
            cnt += 1
        l += 1


a=[]
m,n,d,p=input().split()
m,n,d,p=int(m),int(n),int(d),int(p)
matrix=[]
for x in range(0,m):
    a=list(input().split())
    matrix.append(a)

if(p==1):
    if(d==1):
        c11(m,n,matrix)
    elif(d==2):
        c12(m,n,matrix)
elif(p==2):
    if(d==1):
        c21(m,n,matrix)
    elif(d==2):
        c22(m,n,matrix)
elif(p==3):
    if(d==1):
        c31(m,n,matrix)
    elif(d==2):
        c32(m,n,matrix)
elif(p==4):
    if(d==1):
        c41(m,n,matrix)
    elif(d==2):
        c42(m,n,matrix)



