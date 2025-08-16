class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1,len(asteroids)):
            curr = asteroids[i]
            while stack and curr<0 and stack[-1]>0:
                diff = curr+stack[-1]
                if diff<0:
                    stack.pop()
                elif diff==0:
                    curr = 0
                    stack.pop()
                else:
                    curr = 0
            if curr:
                stack.append(curr)

        return stack





