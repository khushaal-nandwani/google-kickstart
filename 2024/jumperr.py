class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            element = haystack[i]
            if element == needle[0]:
                if len(needle) == 1:
                    return i
                for j in range(1, len(needle)):
                    needleElement = needle[j]
                    if needleElement != haystack[i+j]:
                        break
                    if j == len(needle)-1:
                        return i
        return -1
                    
                
               