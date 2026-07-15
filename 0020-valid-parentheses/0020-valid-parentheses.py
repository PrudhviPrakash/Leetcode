class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={")":"(","]":"[","}":"{"}
        for i in s:
            if i in '(,[,{':
                l.append(i)
            else:
                if len(l)==0:
                    return False
                else:
                    m=l.pop()
                    if(d[i]!=m):
                        return False
                        break
        if len(l)==0:
            return True
        else:
            return False
                


        