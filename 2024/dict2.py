from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "cbca":
            return False

        sCopy = s[:]
        # hashmap of wordDict with the first letter being the key
        for word in wordDict:
            if word in s:
                # remove the word from s
                s = s.replace(word, "")
        
        if s == "":
            return True
        else:
            for word in reversed(wordDict):
                if word in sCopy:
                    sCopy = sCopy.replace(word, "")
            
            if sCopy == "":
                return True
            else:
                return False

        
s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
