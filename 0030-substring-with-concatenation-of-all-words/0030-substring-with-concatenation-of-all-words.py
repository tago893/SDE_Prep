class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = set()
        total_len = len(words) * len(words[0])

        def permute(words_list, l, r, all_perms):
            if l == r:
                all_perms.append(''.join(words_list))
            else:
                for i in range(l, r + 1):
                    words_list[l], words_list[i] = words_list[i], words_list[l]
                    permute(words_list, l + 1, r, all_perms)
                    words_list[l], words_list[i] = words_list[i], words_list[l]  # backtrack

        all_perms = []
        permute(words, 0, len(words) - 1, all_perms)

        for word in all_perms:
            for i in range(len(s) - total_len +1):
                if s[i:i+total_len] == word:
                    result.add(i)
        
        return list(result)
        
