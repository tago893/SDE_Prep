class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        isLast = True
        for i in range(0,len(num)-1):
            if num[i] == '6':
                num = num[0:i] + '9' + num[i+1:]
                isLast = False
                break
        if num[-1]=='6' and isLast == True:
            num = num[:-1] + '9'
        return int(num)