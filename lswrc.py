class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_used_letters = set()
        word_len = 0
        max_word_len = 0
        restart_index = 0

        i = 0
        while i < len(s):
            if word_len == 1:
                restart_index = i 
            letter = s[i]
            if letter not in word_used_letters:
                word_used_letters.add(letter)
                word_len += 1
            else:
                max_word_len = max(max_word_len, word_len)
                word_len = 0
                i = restart_index
                word_used_letters = set()
            i += 1
        return max(max_word_len, word_len)
            
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))