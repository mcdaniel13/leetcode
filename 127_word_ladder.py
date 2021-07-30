from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                dic[word[:i] + "*" + word[i+1:]].append(word)

        que = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)

        while len(que) != 0:
            word, level = que.pop(0)
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                for value in dic[key]:
                    if value == endWord:
                        return level + 1

                    if value not in visited:
                        visited.add(value)
                        que.append((value, level + 1))

        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))