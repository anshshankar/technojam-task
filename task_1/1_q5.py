class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        english=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        edict = dict(zip(english, morse))
        res=[]
        for i in words:
            enc=""
            for l in i:
                enc=enc+edict.get(l)
            if(enc not in res):
                res.append(enc)

        return len(res)

