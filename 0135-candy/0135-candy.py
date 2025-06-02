class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total = n
        i = 1
        # Traverse from left to right
        while i < n:

            # if rating of ith children is
            # equal to the previous children
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            # to find the increasing sequence
            peak = 0
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                total += peak
                i += 1

            if i == n:
                return total

            # to find the decreasing sequence
            valley = 0
            while i < n and ratings[i] < ratings[i - 1]:
                valley += 1
                total += valley
                i += 1

            # remove the extra candy added twice
            total -= min(peak, valley)

        return total