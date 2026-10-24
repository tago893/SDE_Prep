class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for ch in operations:
            if ch == "D":
                double_score = stack[-1]*2
                stack.append(double_score)
            elif ch == "C":
                stack.pop()
            elif ch == "+":
                sum_of_two_scores = stack[-1] + stack[-2]
                stack.append(sum_of_two_scores)
            else:
                stack.append(int(ch))
        return sum(stack)
              
