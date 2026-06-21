class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stk.append(ch)
            else:
                if len(stk) == 0:
                    return False

                top = stk[-1]

                if (
                    (ch == ')' and top != '(')
                    or (ch == '}' and top != '{')
                    or (ch == ']' and top != '[')
                ):
                    return False

                stk.pop()

        return len(stk) == 0