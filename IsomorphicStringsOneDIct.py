class Solution:
    '''
           Given two strings s and t, determine if they are isomorphic.

           Two strings are isomorphic if the characters in s can be replaced to get t.

           All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
       '''
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

