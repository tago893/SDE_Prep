class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeArray = []
        n = len(startTime)
        freeArray.append(startTime[0] - 0)
        for i in range(1,n):
            freeArray.append(startTime[i] - endTime[i-1])
        freeArray.append(eventTime - endTime[n-1])

        j = 0
        i = 0
        maxSum = 0
        currSum = 0
        n = len(freeArray)
        while j<n:
            currSum += freeArray[j]
            if i<n and j-i+1 > k+1:
                currSum -= freeArray[i]
                i += 1
            
            maxSum = max(maxSum,currSum)
            j+=1
        
        return maxSum


