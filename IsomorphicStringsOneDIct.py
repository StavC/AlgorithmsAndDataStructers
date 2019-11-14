class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        for _ in range(2):
            mydict = {}
            for i in range(len(s)):
                if s[i] in mydict and mydict[s[i]] != t[i]:
                    return False
                else:
                    mydict[s[i]] = t[i]
            s, t = t, s

        return True

