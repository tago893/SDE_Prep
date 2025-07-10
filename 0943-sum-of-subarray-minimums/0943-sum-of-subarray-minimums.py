class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        def NSL(arr):
            smallest_left_list = [-1]*(len(arr))
            stack = []
            for i in range(len(arr)):
                if len(stack) == 0:
                    smallest_left_list[i] = -1
                else:
                    while stack and arr[stack[-1]]>arr[i]:
                        stack.pop()
                    if len(stack)==0:
                        smallest_left_list[i] = -1
                    else:
                        smallest_left_list[i] = stack[-1]
                
                stack.append(i)
                
            return smallest_left_list
        def NSR(arr):
            n = len(arr)
            smallest_right_list = [-1]*(len(arr))
            stack = []
            for i in range(len(arr)-1,-1,-1):
                if len(stack) == 0:
                    smallest_right_list[i] = n
                else:
                    while stack and arr[stack[-1]]>=arr[i]:
                        stack.pop()
                    if len(stack) == 0:
                        smallest_right_list[i] = n
                    else:
                        smallest_right_list[i] = stack[-1]
                
                stack.append(i)
                
            return smallest_right_list
        nsl = NSL(arr)
        nsr = NSR(arr)
      
        M = (10**9) + 7
        total_sum = 0
        result = 0
        for i in range(n):
            left = i - nsl[i]
            right = nsr[i] - i
            total_ways = left * right
            total_sum = arr[i]*total_ways
            result=(result + total_sum)% M
        return result