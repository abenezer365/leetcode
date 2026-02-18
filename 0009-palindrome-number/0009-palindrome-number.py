class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        reversedNum = ""
        for i in range(len(num)-1,-1,-1):
            reversedNum += num[i]
        if x == int(reversedNum):
            return True
        else:
            return False



        