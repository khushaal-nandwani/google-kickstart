from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        shortest_len_word = len(wordDict[0])
        longest_len_word = len(wordDict[0])

        for word in wordDict:
            if len(word) > longest_len_word:
                longest_len_word = len(word)
            if len(word) < shortest_len_word or shortest_len_word == 0:
                shortest_len_word = len(word)

        for i in range(len(s)):
            if i < shortest_len_word - 1:
                continue
            if i == shortest_len_word - 1:
                if s[:i + 1] in wordDict:
                    dp[i] = True
                continue
            if i > shortest_len_word - 1:
                for j in range(i - longest_len_word, i):
                    if j  < 0:
                        continue
                    if dp[j] and s[j + 1:i] in wordDict:
                        dp[i] = True
                        continue
            if not dp[i]:
                dp[i] = False
        return dp[-1]
    


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
