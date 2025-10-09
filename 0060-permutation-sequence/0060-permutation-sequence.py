class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        numbers = []
        fact = 1
        for i in range(1,n):
            fact = fact*i
            numbers.append(i)
        numbers.append(n)
        k = k-1
        while True:
            res+=str(numbers[k//fact])
            numbers.remove(numbers[k//fact])
            if len(numbers) == 0:
                break
            k = k%fact
            fact = fact//len(numbers)
        return res
    
