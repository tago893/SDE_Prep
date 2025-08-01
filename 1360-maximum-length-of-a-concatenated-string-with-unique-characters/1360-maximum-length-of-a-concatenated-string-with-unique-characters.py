class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isUnique(s):
            return len(s) == len(set(s))

        def backtrack(index, path):
            if isUnique(path):
                max_len[0] = max(max_len[0], len(path))
            else:
                return

            for i in range(index, len(arr)):
                backtrack(i + 1, path + arr[i])

        max_len = [0]
        if len(arr) == 1:
            if isUnique(arr[0]):
                return len(arr[0])
            else:
                return 0
                
        backtrack(0, "")
        return max_len[0]
