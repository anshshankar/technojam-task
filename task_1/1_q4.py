class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1,word2=list(word1),list(word2)
        fin=[]
        k=0
        while(True):
            fin+=word1[0]+word2[0]
            word1.pop(0)
            word2.pop(0)
            if(word1==[]):
                fin+=word2
                break
            elif(word2==[]):
                fin+=word1
                break
        return "".join(fin)
