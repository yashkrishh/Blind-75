class Solution:
    def isValid(self, s: str) -> bool:
        r=[]
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                r.append(s[i])
            elif s[i] == ')':
                if r == []:
                    return False
                elif r.pop() != '(':
                    return False
            elif s[i] == ']':
                if r == []:
                    return False
                elif r.pop() != '[':
                    return False
            elif s[i] == '}':
                if r == []:
                    return False
                elif r.pop() != '{':
                    return False
        if r == []:
            return True
        else:
            return False
