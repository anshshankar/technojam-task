t=int(input())
while(t>0):
    t-=1
    n=int(input())
    stat=int(input())
    loc=1
    while(n>0):
        n-=1
        d=int(stat%10)
        stat=int(stat/10)
        if(d==0):
            loc+=1
        elif(d==1):
            loc-=1
    res=int(loc%4)
    if(res==0):
        print("The Mountain")
    elif(res==1):
        print("tywin")
    elif(res==2):
        print("The Hound")
    elif(res==3):
        print("Jaime")




