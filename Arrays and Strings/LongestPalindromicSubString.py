class Solution:
'''Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

'''
    def check_pal(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:

        res = ""

        for i in range(len(s)):
            odd = self.check_pal(s, i, i)
            if len(odd) > len(res):
                res = odd
            even = self.check_pal(s, i, i + 1)
            if len(even) > len(res):
                res = even
        return res



