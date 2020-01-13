class Solution:
    '''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
96% faster
'''

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            s = s.lower()
            i = 0
            j = len(s) - 1

            while i < j:
                if not s[i].isalnum():
                    i += 1
                elif not s[j].isalnum():
                    j -= 1
                else:
                    if s[i] != s[j]:
                        return False
                    else:
                        i += 1
                        j -= 1
            return True


