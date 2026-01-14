class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res=0
        left_max,right_max=[0]*(n),[0]*(n)
        left_max[0]=height[0]
        for j in range(1,n):
            left_max[j] = max(left_max[j-1],height[j])
        right_max[-1] = height[-1]
        for k in range(n-2,-1,-1):
            right_max[k]=max(right_max[k+1],height[k])
        for i in range(n):
            res += min(left_max[i],right_max[i]) - height[i]
        
        return res
