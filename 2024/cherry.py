class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        sCurr = s[index]
        for i in range(len(t)):
            if t[i] == sCurr:
                if index >= len(s) - 1:
                    return True
                index += 1
                sCurr = s[index]
        
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("acb", "ahbgdc"))