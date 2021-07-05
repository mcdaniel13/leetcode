class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for i in range(len(s)):
            if s[i] is '(':
                stack += ')'
            elif s[i] is '{':
                stack += '}'
            elif s[i] is '[':
                stack += ']'
            else:
                if len(stack) != 0 and stack[len(stack) - 1] == s[i]:
                    stack = stack[:-1]
                else:
                    return False

        return len(stack) == 0

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
