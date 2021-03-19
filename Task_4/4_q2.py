t=int(input())
a=[]
for i in range(0,t):
    a.append(list(input().split()))
for i in range(0,t):
    tot=0
    for x in range(2,7):
        tot += int(a[i][x])
    a[i].append(tot)
    tot=0
    for x in range(2,5):
        tot += int(a[i][x])
    a[i].append(tot)
    a[i]=a[i][7:]+a[i][:2]

a.sort(reverse=True)
for i in a:
    print("".join(i[2]+" "+i[3]))
