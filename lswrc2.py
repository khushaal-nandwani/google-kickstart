class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [s[i: j] for i in range(len(s))
                for j in range(i + 1, len(s) + 1)]
        maxlen = 0
        for subs in res:
            lent = len(set(subs))
            if lent > maxlen:
                maxlen = lent
                