t=int(input())
while(t>0):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    one=0
    two=0
    three=0
    for i in a:
        if(i%4==0):
            ans+=1
        else:
            if(i%4==1):
                one+=1
            elif(i%4==2):
                two+=1
            elif(i%4==3):
                three+=1

    ans+=int(two/2)
    ans+=int(one/4)
    one%=4
    ans+=min(one,three)
    print(ans)


