def isprime(n):
    if(n==1):
        return False
    else:
        d=0
        for i in range(2,n):
            if(n%i==0):
                d+=1
    if(d==0):
        return True
    else:
        return False



n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    if(isprime(i)):
        s+=i

l=[]
while(s>0):
    d=int(s%10)
    s=int(s/10)
    if d not in l:
        l.append(d)
    else:
        print("No")
        break
    if s==0:
        print("Yes")


