class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        vstack = []

        i,j = 0,0
        n = len(pushed)

        for i in range(0,n):
            vstack.append(pushed[i])
            while vstack and j< n and vstack[-1] == popped[j]:
                vstack.pop()
                j+=1
       
        return len(vstack) == 0