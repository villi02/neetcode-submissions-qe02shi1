class Solution:
    def isValid(self, s: str) -> bool:
        match = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in match:
                stack.append(match[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
        return not stack