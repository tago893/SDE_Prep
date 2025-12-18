class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n  = len(heights)
        maxArea = 0

        stack = []
        leftmost = [-1]*(n)

        for i in range(0,n):
            while stack and heights[stack[-1]]>= heights[i]:
                stack.pop()
            if stack:
                leftmost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightmost = [n]*n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>= heights[i]:
                stack.pop()
            if stack:
                rightmost[i] = stack[-1]
            stack.append(i)
        
        print(leftmost)
        print(rightmost)

        for i in range(0,n):
            leftmost[i]+=1
            rightmost[i]-=1
            maxArea = max(maxArea,heights[i]*(rightmost[i]-leftmost[i]+1))
            print(maxArea)
        return maxArea
        