from itertools import combinations

t=int(input())
l=[]
while(t>0):
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    d=0
    for i in combinations(arr,2):
        a=[]
        a.extend(arr)
        for x in i:
            a.remove(int(x))

        s=0
        for x in i:
            s+=int(x)
        a.extend([s])

        print(a)
        d=0
        for i in a:
            if(i%4==0):
                d+=1
        l.append(d)

print(l)
# print(max(l))
