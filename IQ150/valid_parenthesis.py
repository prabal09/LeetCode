from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        brackets = {')':'(','}':'{',']':'['}
        stack = deque()
        for ch in s:
            if ch in brackets:
                top_el = stack.pop() if stack else ''
                if brackets[ch] != top_el:
                    return False
            else:
                stack.append(ch)
        return not stack
