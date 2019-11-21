class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1;
                end -= 1

        reverse(s, 0, len(s) - 1)
        i = left = 0
        while i < len(s):
            if s[i] == " ":
                reverse(s, left, i - 1)
                left = i + 1
            elif i == len(s) - 1:
                reverse(s, left, i)
            i += 1