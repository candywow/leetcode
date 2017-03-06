class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        start = 0
        set = {}
        for i in range(len(s)):
            set[s[i]] = -1
        for i in range(len(s)):
            if set[s[i]] != -1:
                while start <= set[s[i]]:
                    set[s[start]] = -1
                    start += 1
            set[s[i]] = i
            if i - start + 1 > max:
                max = i - start + 1
        return max
