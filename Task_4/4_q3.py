t=int(input())
while(t>0):
    t-=1

    word=list(input())
    word1="".join(word)

    char=['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c_ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']

    edict=dict(zip(char,c_ch))
    print("The original string is : " + (word1))
    res=[]
    arr=word[:]
    for i in word:
        ak=word[:]
        ak.remove(i)
        if(i=='a'):
            res.extend(arr)
            break
        arr.remove(i)
        res.extend("{}".format(edict[i]))

    print("".join(res))


