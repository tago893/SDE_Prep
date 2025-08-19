from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def build_adjacency_list(words):
            word_set = set(words)  # for O(1) lookup
            adj = defaultdict(list)

            for word in words:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue  # skip same letter
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            adj[word].append(new_word)
            return adj
        
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = build_adjacency_list(wordList)
        visited = set([beginWord])
        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for neighbor in adj[word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return 0