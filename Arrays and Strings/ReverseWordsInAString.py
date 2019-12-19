class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        space = [' ']
        while i < len(s):

            if s[i] not in space:
                word_start = i

                while (i < len(s)) and (s[i] != ' '):
                    i += 1

                words.append(s[word_start:i])
                words.append(' ')
            i += 1

        reversed_words = ""
        while len(words) > 0:
            reversed_words += words.pop()
        return reversed_words.strip()