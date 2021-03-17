t=int(input())
while(t>0):
    t-=1

    word=list(input())
    word1="".join(word)

    char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    con_char=['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']

    edict=dict(zip(char,con_char))
    print("The original string is : " + (word1))
    K = 1
    res=[]
    arr=word[:]
    for i in word:
        ak=word[:]
        ak.remove(i)
        if(i=='a'):
            res.extend(arr)
            break
        arr.remove(i)
        trans=word1.maketrans(i,edict[i],("".join(ak)))
        res.extend(word1.translate(trans))

    print("".join(res))


