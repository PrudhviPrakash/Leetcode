class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<=3:
            return True
        else:
            return n%4!=0        