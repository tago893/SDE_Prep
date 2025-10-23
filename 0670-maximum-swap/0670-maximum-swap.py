class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}  # track last index of each digit
        
        for i, d in enumerate(digits):
            for x in range(9, int(d), -1):  # check for bigger digit
                if x in last and last[x] > i:
                    digits[i], digits[last[x]] = digits[last[x]], digits[i]
                    return int("".join(digits))
        return num
