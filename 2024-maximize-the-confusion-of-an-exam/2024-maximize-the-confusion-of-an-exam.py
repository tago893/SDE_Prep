class Solution:
    def flipper(self, c, s, k):
        i = 0
        flips = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] != c:
                flips += 1

            while flips > k:
                if s[i] != c:
                    flips -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(
            self.flipper('T', answerKey, k),
            self.flipper('F', answerKey, k)
        )
