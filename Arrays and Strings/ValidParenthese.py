class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        opening = ["{", "[", "("]
        if len(s) == 1 or len(s) % 2 != 0:
            return False
        for par in s:
            if par in opening:
                mystack.append(par)
            else:
                if not mystack:
                    return False
                if par == "}" and mystack.pop() == "{":
                    continue
                elif par == "]" and mystack.pop() == "[":
                    continue
                elif par == ")" and mystack.pop() == "(":
                    continue
                else:
                    return False
        if not mystack:
            return True



