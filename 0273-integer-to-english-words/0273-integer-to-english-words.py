class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven",
            12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
            40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
        }

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return d[n]
            elif n < 100:
                return d[n // 10 * 10] + (" " + d[n % 10] if n % 10 != 0 else "")
            elif n < 1000:
                return d[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
            else:
                for div in [1000000000, 1000000, 1000]:
                    if n >= div:
                        return helper(n // div) + " " + d[div] + (" " + helper(n % div) if n % div != 0 else "")
            return ""

        if num == 0:
            return "Zero"
        return helper(num).strip()
