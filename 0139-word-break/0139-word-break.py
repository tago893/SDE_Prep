class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set  = set(wordDict)
        memo = {}
        def backtrack(i):
            if i==n:
                return True
            if i in memo:
                return memo[i]
            for end in range(i+1,n+1):
                if s[i:end] in word_set and backtrack(end):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return backtrack(0)
            