t=int(input())
while(t>0):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    odd=0
    for i in a:
        if(i%2!=0):
            odd+=1
    if(odd==0):
        print("-1")
    else:
        print(n-odd)
